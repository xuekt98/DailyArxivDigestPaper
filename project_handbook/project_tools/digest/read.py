#!/usr/bin/env python3
"""Digest Phase 2 — PDF reader: download (3s rate limit), extract affiliations,
contribution sentences and key figures, write phase2_cards/*.json.

Shortlist comes from shortlist.json in the workdir:
  {"track": ["2610.xxxxx", ...], ...}
Report mode (structure + which fields are written) is produced separately by
render.py; this script only fills phase2_cards/<id>.json.

Usage:
  python read.py --out <workdir>

Extraction notes (these were fixes found by inspecting real PDFs):
  - caption regex accepts 'Fig. 1.\nCaption', 'Figure 1 | X', 'Figure 1: X'
  - body-text refs like 'Figure 3(a) shows that' are rejected via a verb blacklist
  - affiliations carry footnote markers ('*Duke Kunshan University'), so the
    author-line filter must not reject them; pages 1-2 are scanned
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import pymupdf

RATE = 3.0

VERB = re.compile(r"^(shows?|demonstrates?|illustrates?|depicts?|compares?|presents?|reports?|"
                  r"summarizes?|describes?|highlights?|outlines?|details|gives?|plots?|"
                  r"visualiz|lists?)\b", re.I)
CAPTION = re.compile(r"^(?:Figure|Fig\.)\s*(\d+)\s*[.:|\u2013\u2014-]?\s*([A-Za-z0-9][\w-]*)")
NUM_ONLY = re.compile(r"^(?:Figure|Fig\.)\s*(\d+)\s*[.:|\u2013\u2014-]?\s*$", re.I)

STRONG = re.compile(
    r"(\buniversit|\buniv\b|\binstitut|\blaborator|\bcollege\b|\bschool of\b|\bacademy of|"
    r"\bgraduate school\b|\bresearch (institute|lab)|\binc\b|\bcorp\b|\bcorporation\b|"
    r"\bcompany\b|\bltd\b|\bgmbh\b|\bsa\b|\bag\b|"
    r"alibaba|tencent|baidu|huawei|bytedance|sensetime|kuaishou|\bant group|adobe|amazon|apple|"
    r"openai|deepmind|google|microsoft|\bmeta\b|nvidia|qualcomm|samsung|sony|toyota|honda|"
    r"stanford|berkeley|caltech|carnegie mellon|\btsinghua|\bpku\b|peking university|zhejiang university|"
    r"fudan|jiao ?tong|chinese academy of sciences|\beth\b|epfl|oxford|cambridge|imperial college|"
    r"\bucl\b|\bkth\b|karlsruhe|\bdelft\b|\bghent\b|\binria\b|\bmila\b|\bvector institute\b|"
    r"\bnserc\b|\bmcgovern|\bamii\b|\binsa\b|\bsap\b|\bcnrs\b|\brail\b|\bseek\b|\bjstc\b|"
    r"\bcriteo\b|\bkddi\b|yale|harvard|princeton|cornell|jhu|uiuc|gatech|\bnus\b|\bntu\b|kaist|"
    r"\bpolyu\b|cuhk|\bhku\b|\bhkust\b|hkust|toronto|mcgill|waterloo|max planck|dfki|surrey|"
    r"boise|semio|\bhanyang\b|pusan|kyung hee|adelaide|curtin|\bsydney\b|fordham|"
    r"northeastern|sungkyunkwan|\bsutd\b|\bntt\b|kyushu|nagoya|osaka|waseda|\bhokkaido\b|"
    r"technion|bar-ilan|heidelberg|leuven|\bnec\b|philips|\bsiemens\b|\bmeituan\b|\boppo\b|"
    r"amii|naver|kakao|distyl|\bxiaomi\b|\bnpu\b|\baslp\b|\bsichuan\b|\bguangdong\b|"
    r"\bbuaa\b|\bseu\b|\bjlu\b|\braunschweig\b|\bfraunhofer\b|\bupf\b|\bwisc\b|"
    r"\bits\b|\bpisa\b|\bdcu\b|\bswansea\b|\byue\b|\bscu\b|\bhhu\b|\bwhu\b|"
    r"\bai singapore\b|\baisingapore\b|\bwuhan\b|\bshandong\b|\bharbin\b|\bhohai\b|"
    r"\bjiangsu\b|\bsysu\b|\bscau\b|\bautonomous\b|\binstitut|\blaborator)", re.I)

EMAILISH = re.compile(r"@")
FOOT = re.compile(r"^\s*(\{[^}]*\}|[A-Za-z0-9._%+-]+)\s*(emails?|e-mail|correspond)", re.I)
BADLINE = re.compile(r"^(abstract|introduction|keywords|index terms|arxiv:|preprint|this manuscript|"
                     r"published|accepted|license|figure|table|\d+\s*$|in th)", re.I)
CONTRIB = re.compile(
    r"(our (main )?contributions? (are|is|include)|we (propose|present|introduce|develop|design|"
    r"build|contribute)|in this (paper|work), we|to (this end|address) (we|our)|we show that|"
    r"our (key )?(insight|finding|approach|method|framework)|extensive experiments show|"
    r"experiments (on|across) .{0,40}(show|demonstrate)|we find that|we identify that|"
    r"we (observe|argue|reveal)|we (release|introduce)|this (paper|work) (proposes|introduces|studies))",
    re.I)


def clean(s: str) -> str:
    return " ".join(s.split())


def caption_of(raw: str):
    probe = clean(raw[:200])
    m = CAPTION.match(probe)
    if m and not VERB.match(m.group(2)):
        return m.group(1), probe[m.end() - len(m.group(2)):].strip()
    first = raw.strip().split("\n", 1)[0]
    m2 = NUM_ONLY.match(first)
    if m2:
        parts = raw.strip().split("\n", 1)
        return m2.group(1), (clean(parts[1])[:240] if len(parts) > 1 else "")
    return None


def sentences(t: str) -> list[str]:
    return [clean(x) for x in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", t) if clean(x)]


def is_prose(line: str) -> bool:
    words = line.split()
    if len(words) < 7:
        return False
    return sum(1 for wd in words[1:] if wd[:1].islower()) / max(1, len(words) - 1) > 0.6


def extract_figures(doc, outdir: Path, bid: str) -> list[dict]:
    found = []
    for pno in range(min(len(doc), 9)):
        page = doc[pno]
        blocks = [b for b in page.get_text("blocks") if b[6] == 0 and b[4].strip()]
        for b in blocks:
            if len(b[4].strip()) > 900:
                continue
            got = caption_of(b[4])
            if not got:
                continue
            num, cap = got
            r = pymupdf.Rect(b[0], b[1], b[2], b[3])
            above = [x for x in blocks if x[3] <= r.y0 + 2 and not caption_of(x[4])]
            top = min((x[3] for x in above if x[3] >= page.rect.y0), default=page.rect.y0 + 20)
            top = min(max(top, r.y0 - 340), r.y0 - 24)
            if r.y1 - top < 70:
                continue
            found.append((pno, num, pymupdf.Rect(page.rect.x0 + 18, top,
                                                 page.rect.x1 - 18, r.y1 + 4), cap))
    best = {}
    for pno, num, rect, cap in found:
        if num not in best or pno < best[num][0]:
            best[num] = (pno, rect, cap)
    out = []
    for name, num in (("framework", "1"), ("result", "2")):
        if num not in best:
            continue
        pno, rect, cap = best[num]
        pix = doc[pno].get_pixmap(clip=rect & doc[pno].rect, dpi=150)
        if pix.width < 60 or pix.height < 60:
            continue
        (outdir / bid).mkdir(parents=True, exist_ok=True)
        pix.save(outdir / bid / f"{name}.png")
        out.append({"name": name, "path": f"figures/{bid}/{name}.png",
                    "page": pno + 1, "fig_no": int(num), "caption": cap})
        if len(out) >= 2:
            break
    return out


def extract_affils(doc) -> list[str]:
    aff = []
    for pno in range(min(len(doc), 2)):
        for b in doc[pno].get_text("blocks"):
            if b[6] != 0:
                continue
            for line in b[4].split("\n"):
                line = clean(line)
                if not (3 < len(line) <= 230) or BADLINE.match(line):
                    continue
                if FOOT.match(line) and len(aff) < 5:
                    aff.append(line)
                    continue
                if "@" in line and STRONG.search(line) and line not in aff:
                    aff.append(line)
                    continue
                if "@" in line and re.match(r"^[^@\s]{1,40}@[\w-]+\.[\w.]+$", line) and line not in aff:
                    aff.append(line)
                    continue
                if STRONG.search(line) and line not in aff:
                    aff.append(line)
                if len(aff) >= 5:
                    break
            if len(aff) >= 5:
                break
        if len(aff) >= 5:
            break
    seen, ordered = set(), []
    for a in aff:
        if a not in seen and not is_prose(a):
            seen.add(a)
            ordered.append(a)
    return ordered[:4]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    W = Path(args.out)
    DL, TXT, FIG, CARD = W / "downloads", W / "extracted", W / "figures", W / "phase2_cards"
    for d in (DL, TXT, FIG, CARD):
        d.mkdir(parents=True, exist_ok=True)

    shortlist = json.loads((W / "shortlist.json").read_text(encoding="utf-8"))
    papers = {p["base_id"]: p for p in json.loads((W / "raw_papers.json").read_text(encoding="utf-8"))}
    ids = [i for t in shortlist.values() for i in t]
    assert len(ids) == len(set(ids)), f"duplicate shortlist ids: {len(ids)} vs {len(set(ids))}"
    print(f"shortlist: {len(ids)} unique papers", flush=True)
    nfig = 0

    for n, bid in enumerate(ids, 1):
        print(f"[{n}/{len(ids)}] {bid}", flush=True)
        pdf = DL / f"{bid}.pdf"
        if not (pdf.exists() and pdf.stat().st_size > 20000):
            try:
                req = urllib.request.Request(f"https://arxiv.org/pdf/{bid}",
                                             headers={"User-Agent": "arxiv-daily-digest/0.2"})
                with urllib.request.urlopen(req, timeout=90) as r:
                    data = r.read()
                if len(data) < 20000:
                    print(f"  [dl-skip] {bid}")
                    time.sleep(RATE)
                    continue
                pdf.write_bytes(data)
            except Exception as exc:
                print(f"  [dl-fail] {bid}: {exc}")
                time.sleep(RATE)
                continue
            time.sleep(RATE)

        doc = pymupdf.open(pdf)
        npages = len(doc)
        raw = "\n".join(f"<<<PAGE {p+1}>>>\n" + doc[p].get_text() for p in range(min(npages, 9)))
        figures = extract_figures(doc, FIG, bid)
        nfig += len(figures)
        aff = extract_affils(doc)
        doc.close()

        (TXT / f"{bid}.txt").write_text(raw, encoding="utf-8")
        intro = ""
        for pg in re.split(r"<<<PAGE \d+>>>", raw)[1:4]:
            body = pg.split("Abstract", 1)[-1]
            if len(body) > 1200:
                intro += "\n" + body[:6000]
        contribs = []
        for s in sentences(intro):
            if CONTRIB.search(s) and 40 < len(s) < 460 and s not in contribs:
                contribs.append(s)
            if len(contribs) >= 4:
                break
        meta = papers.get(bid, {})
        if not contribs:
            contribs = sentences(meta.get("abstract") or "")[:3]

        (CARD / f"{bid}.json").write_text(json.dumps({
            "arxiv_id": bid, "title": meta.get("title"),
            "authors": [{"name": a, "affiliation": "[unverified]"}
                        for a in (meta.get("authors") or [])[:12]],
            "affiliation_block": aff, "categories": meta.get("categories"),
            "abs_url": (meta.get("abs_url") or "").replace("http://", "https://"),
            "abstract": meta.get("abstract"), "contributions": contribs,
            "figures": figures, "read_mode": "full", "pages": npages,
            "batch_day": meta.get("batch_day"),
            "page_citations": {f"contribution_{i+1}": 1 for i in range(len(contribs))},
            "comment": meta.get("comment") or "",
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    cards = list(CARD.glob("*.json"))
    nofig = [f.stem for f in cards if not json.loads(f.read_text(encoding="utf-8"))["figures"]]
    noaff = [f.stem for f in cards if not json.loads(f.read_text(encoding="utf-8"))["affiliation_block"]]
    print(f"\ncards: {len(cards)}  figures: {nfig}")
    print(f"no-figure: {len(nofig)} {nofig}")
    print(f"no-affiliation: {len(noaff)} {noaff}")
    return 0


if __name__ == "__main__":
    sys.exit(main())