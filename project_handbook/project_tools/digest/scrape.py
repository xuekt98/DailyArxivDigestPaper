#!/usr/bin/env python3
"""Digest Phase 1 — arXiv scraper + keyword prefilter.

Project tool for the daily arXiv digest. Sequential arxiv calls only, 3s apart
(skill rate limit). Fetches per (category, day) so no category-day is silently
truncated by max_results.

Usage:
  python scrape.py --out <workdir> [--days 20261015] [--days 20261015,20261016]
  python scrape.py --out <workdir> --auto 3   # probe back N days, use newest non-empty

Outputs into <workdir>: raw_papers.json, phase1_listing.md, candidates.json

Why no submittedDate in the query (2026-10-21):
  arXiv's API answers `submittedDate:[... TO ...]` range searches with HTTP 429
  / 503 for this host, while plain `cat:<c>` queries answered normally. The
  range search is therefore done locally: fetch each category sorted by
  submittedDate (descending) and keep the entries whose v1 `published` date
  equals the batch day. The API only exposes announced papers, so a batch day
  is exactly the set of papers whose v1 timestamp falls on it.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone, time as _time
from pathlib import Path

API = "https://export.arxiv.org/api/query"
RATE = 5.0
PAGE = 300
# arXiv closes submissions at 14:00 US Eastern (= 18:00 UTC, EDT) and announces
# at 20:00 ET (= 00:00 UTC the next day). The announcement arXiv lists under
# date D therefore holds every paper whose v1 `published` timestamp falls
# between 18:00 UTC on D-1 and 17:59:59 UTC on D -- the batch straddles two
# UTC calendar days. Filtering on the calendar date of `published` alone would
# silently drop the D-1 evening half of every announcement (~21% of the
# tracked categories on the 2026-10-21 listing).
CUTOFF = "18:00:00"
NS = {"atom": "http://www.w3.org/2005/Atom"}
CATS = ["cs.CV", "cs.SD", "eess.AS", "cs.CL", "cs.AI", "cs.RO", "cs.LG"]


def fetch(url: str, label: str) -> bytes:
    """GET with arXiv-friendly backoff. 429/503 are throttles, not failures."""
    wait = 20.0
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "arxiv-daily-digest/0.2 (daily paper digest)"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 503) and attempt < 5:
                print(f"  throttle [{label}] attempt {attempt}: HTTP {exc.code}; "
                      f"sleep {wait:.0f}s", file=sys.stderr)
                time.sleep(wait)
                wait = min(wait * 2, 120)
                continue
            raise
        except Exception as exc:
            if attempt >= 5:
                raise
            print(f"  retry {attempt} [{label}]: {exc}", file=sys.stderr)
            time.sleep(wait)
            wait = min(wait * 2, 120)
    raise RuntimeError("unreachable")


def parse(b: bytes, day: str) -> list[dict]:
    root = ET.fromstring(b)
    out = []
    for e in root.findall("atom:entry", NS):
        rid = e.findtext("atom:id", default="", namespaces=NS)
        aid = rid.split("/")[-1]
        pdf = ""
        for link in e.findall("atom:link", NS):
            if link.get("title") == "pdf":
                pdf = link.get("href", "")
                break
        if not pdf:
            pdf = rid.replace("/abs/", "/pdf/") + ".pdf"
        out.append({
            "arxiv_id": aid, "base_id": aid.split("v")[0],
            "title": " ".join((e.findtext("atom:title", default="", namespaces=NS) or "").split()),
            "abstract": " ".join((e.findtext("atom:summary", default="", namespaces=NS) or "").split()),
            "authors": [" ".join((a.findtext("atom:name", default="", namespaces=NS) or "").split())
                        for a in e.findall("atom:author", NS)],
            "abs_url": rid, "pdf_url": pdf,
            "categories": [c.get("term", "") for c in e.findall("atom:category", NS)],
            "published": e.findtext("atom:published", default="", namespaces=NS),
            "updated": e.findtext("atom:updated", default="", namespaces=NS),
            "batch_day": day,
            "comment": " ".join((e.findtext("arxiv:comment", default="",
                                             namespaces={"arxiv": "http://arxiv.org/schemas/atom"}) or "").split()),
        })
    return out


def url_for(cat: str, start: int = 0, n: int = PAGE) -> str:
    query = f"cat:{cat}"
    return (f"{API}?search_query={urllib.parse.quote(query)}"
            f"&sortBy=submittedDate&sortOrder=descending&max_results={n}&start={start}")


def window_bounds(listing_day: str) -> tuple[str, str]:
    """UTC half-open window [lo, hi) of the announcement arXiv lists on `listing_day`.

    `listing_day` is the date arXiv shows on its "new submissions for <date>"
    listing. The corresponding announcement fires at 00:00 UTC on the *next* day
    and contains v1 timestamps from 18:00 UTC on `listing_day - 1` up to
    17:59:59 UTC on `listing_day`.
    """
    d = datetime.strptime(listing_day, "%Y-%m-%d").date()
    lo = datetime.combine(d - timedelta(days=1), _time(18, 0, 0))
    hi = datetime.combine(d, _time(18, 0, 0))
    return lo.strftime("%Y-%m-%dT%H:%M:%SZ"), hi.strftime("%Y-%m-%dT%H:%M:%SZ")


def in_batch(published: str, listing_day: str) -> bool:
    """True when a v1 timestamp falls inside the announcement listed on `listing_day`."""
    lo, hi = window_bounds(listing_day)
    return lo <= published < hi


class Fetcher:
    """Cached page reader: one arXiv call per (category, start)."""

    def __init__(self) -> None:
        self._cache: dict[tuple[str, int], list[dict]] = {}
        self.calls = 0

    def page(self, cat: str, start: int = 0) -> list[dict]:
        key = (cat, start)
        if key not in self._cache:
            rows = parse(fetch(url_for(cat, start), f"{cat}@{start}"), "")
            self._cache[key] = rows
            self.calls += 1
            time.sleep(RATE)
        return self._cache[key]

    def day(self, cat: str, listing_day: str) -> list[dict]:
        """Entries of one category inside the announcement listed on `listing_day`.

        That announcement spans two UTC calendar days: 18:00 on the previous
        day through 17:59:59 on `listing_day`. Papers stamped after the 18:00
        UTC deadline on `listing_day` belong to the *next* announcement and are
        excluded here.
        """
        out, start = [], 0
        lo_date = window_bounds(listing_day)[0][:10]
        while True:
            rows = self.page(cat, start)
            if not rows:
                break
            out.extend([r for r in rows if in_batch(r["published"], listing_day)])
            oldest = min(r["published"][:10] for r in rows)
            if len(rows) == PAGE and oldest >= lo_date:
                start += PAGE
                continue
            break
        return out

    def latest_day(self) -> str:
        """Listing date of the newest announced batch.

        The newest v1 timestamp on arXiv always falls in the 00:00-17:59:59 UTC
        half of its day (everything from 18:00 UTC onwards waits for the next
        announcement), so the calendar date of the newest entry is exactly the
        listing date of the newest batch.
        """
        latest = ""
        for cat in CATS:
            for r in self.page(cat):
                d = r["published"][:10]
                if d > latest:
                    latest = d
        return latest


# --------------------------------------------------------------------------
# Keyword taxonomy. Title hit counts double. Tunes the candidate pools; the
# final per-paper scoring/ranking is still authored per run in render.py.
# --------------------------------------------------------------------------
TRACKS = {
    "aigc_visual": [
        (r"\btext-to-image\b|\bimage synthesis\b|\bimage generation\b", 3),
        (r"\bdiffusion (model|transformer|modeling)\b|\bdiffusion transformer\b|\bmmdit\b", 2),
        (r"\bflow matching\b|\bscore-based\b|\brectified flow\b", 2),
        (r"\btext-to-video\b|\bvideo generation\b|\bvideo synthesis\b|\bvideo diffusion\b", 3),
        (r"\bvideo prediction\b|\bvideo latent\b|\bworld-action model\b|\bworld action model\b|\bimage-to-video\b", 2),
        (r"\btext-to-3d\b|\bimage-to-3d\b|\b3d generation\b|\b3d gaussian splatting\b|\b3dgs\b", 3),
        (r"\bnerf\b|\bneural radiance field\b|\bnovel view synthesis\b|\bmesh generation\b", 2),
        (r"\bimage editing\b|\bvideo editing\b|\b3d editing\b|\binpainting\b|\boutpainting\b|\bediting\b", 3),
        (r"\bcontrollable generation\b|\binstruction-based editing\b|\bdrag-based\b|\bstylization\b", 2),
        (r"\bpersonaliz\w+|\bsubject-driven\b|\bidentity preservation\b|\bmulti-subject\b|\breward model\w*\b", 2),
        (r"\bconsistency model\b|\bdistillation\b|\bdistill\w+ (model|step)|\bone-step\b|\bfew-step\b", 1),
        (r"\bvisual generation\b|\bsynthesiz\w+ (image|video|scene)", 1.5),
        (r"\b4d generation\b|\bdynamic 3d\b|\b4d reconstruction\b|\b4d\b", 2),
        (r"\bautoregressive.*\b(image|video)\b|\bvisual tokenizer\b|\bvideo tokenizer\b|\btokenizer\b", 2),
        (r"\bmotion (generation|synthesis|transfer)\b|\bhuman motion\b|\bmotion customization\b", 1),
        (r"\bwatermark\w*|\bprovenance\b|\bdeepfake\b", 1),
        (r"\bcache\b.*\b(diffusion|denois)|\bacceleration\b|\bsparse attention\b|\baccelerat\w+\b", 1),
    ],
    "aigc_audio": [
        (r"\btext-to-audio\b|\btext-to-music\b|\btext-to-speech\b|\btts\b|\bspeech synthesis\b", 3),
        (r"\bmusic generation\b|\bsound generation\b|\baudio generation\b|\baudio synthesis\b", 3),
        (r"\baudio diffusion\b|\blatent audio\b|\bmusic diffusion\b|\baudio codec\b|\bneural audio codec\b", 2.5),
        (r"\bvoice cloning\b|\bvoice conversion\b|\bvoice design\b|\bsinging voice\b|\bvoice anonymiz\w+|\btimbre\b", 3),
        (r"\bspeech enhancement\b|\bspeech denoising\b|\bspeech separation\b|\bsource separation\b", 2),
        (r"\bsound event\b|\baudio caption\w+|\bsound (design|synthesis)\b|\baudio scene\b", 1.5),
        (r"\baudio morphing\b|\bexpressive (audio|speech)\b|\bemotion control\b|\bstyle (control|planning)\b", 2),
        (r"\bmusic (editing|restoration|separation|transcription|evaluation)\b|\bsoundtrack\b|\bambient\b|\bchoral\b", 2),
        (r"\bsinging\b|\bvocoder\b|\blyric\b|\bmelody\b|\binstrument\b", 1.5),
        (r"\bspeech emotion\b|\bprosod\w+|\bparalinguistic\b", 1.5),
    ],
    "audio_lm": [
        (r"\baudio (llm|language model|foundation model)\b|\bspeech (llm|language model)\b", 3),
        (r"\blarge audio model\b|\bomni-modal\b|\bmulti-modal audio\b|\bmulti-modal llm\b|\bvisual llm\b|\blalm\b", 2),
        (r"\bspeech-to-speech\b|\bs2s\b|\bspoken dialogue\b|\bvoice agent\b|\bvoice assistant\b", 3),
        (r"\bduplex\b|\bhalf-duplex\b|\bfull-duplex\b|\bturn-taking\b|\bbarge-in\b|\bfloor control\b", 3.5),
        (r"\bconversational (ai|system)\b|\bspeech assistant\b|\bdialogue system\b|\bspoken (dialog|assistant)", 2.5),
        (r"\binterruptible\b|\bstreaming (speech|audio)\b|\blow-latency speech\b|\breal-time speech\b", 2),
        (r"\baudio understanding\b|\baudio question\b|\baudio reasoning\b|\bspeech understanding\b", 2),
        (r"\bspeech instruction\b|\baudio instruction\b|\bspeech translation\b|\bspoken language understanding\b", 1.5),
        (r"\bphoneme\b|\bspeaker embedding\b|\bspeech representation\b|\bspeech recognition\b|\basr\b|\bwhisper\b", 1.5),
        (r"\bdialect\b|\bcode-switch\w+\b|\blanguage identification\b|\blid\b|\baccent\b", 1.5),
        (r"\bspeech deepfake\b|\bacoustic foundation model\b|\bspeaker verification\b|\blong-term memory\b", 1.5),
    ],
    "embodied": [
        (r"\bembodied (ai|agent|intelligence)\b|\bembodied\b", 3),
        (r"\brobot(ic)? (learning|policy|policies|manipulation|navigation)\b|\bmanipulation\b|\bgrasping\b", 3),
        (r"\bvla\b|\bvision-language-action\b|\bvtla\b", 3.5),
        (r"\bworld model\b|\bworld models\b|\blatent dynamics\b|\bjepa\b|\bv-jepa\b|\bdino-wm\b", 3.5),
        (r"\bvisual navigation\b|\bvisual exploration\b|\bnavigation\b|\bembodied navigation\b", 2),
        (r"\bmobile manipulation\b|\bhousehold task\b|\bopen x-embodiment\b|\bhumanoid\b|\bdexterous\b", 3),
        (r"\bsim-to-real\b|\bsim2real\b|\bdomain randomization\b|\breal-to-sim\b", 3),
        (r"\baction chunk\w*|\bdiffusion polic\w+\b|\bpolicy learning\b|\bpolicy optimization\b", 2),
        (r"\bneural simulator\b|\blearned simulator\b|\bdynamics model\b|\bforward model\b", 2),
        (r"\bteleoperat\w+|\bquadruped\b|\bdrone\b|\buav\b|\brobot arm\b", 1.5),
        (r"\btactile\b|\bvisuotactile\b|\bforce (feedback|control|sensing)\b|\bcontact\b", 2),
        (r"\bmodel-based planning\b|\bplanning\b|\btrajectory (prediction|optimization)\b", 1.5),
    ],
    "rl": [
        (r"\breinforcement learning\b|\brl algorithm\b|\bpolicy gradient\b", 3),
        (r"\bppo\b|\bsac\b|\btd3\b|\bdqn\b|\bactor-critic\b|\bflow (policy|reinforcement)|\bgrpo\b", 3),
        (r"\boffline rl\b|\bmodel-free rl\b|\bmodel-based rl\b|\bonline rl\b", 3),
        (r"\brlhf\b|\bdpo\b|\bgrpo\b|\bpreference optimiz\w+|\bverifiable reward\w*|\brlvr\b", 3.5),
        (r"\breward model\w*\b|\balignment\b|\bprocess reward\w*|\bprocess supervision\b|\brubric\b", 2.5),
        (r"\bmulti-agent reinforcement\b|\bmarl\b|\bqmix\b|\bmaddpg\b|\bmappo\b|\bcooperative rl\b", 3.5),
        (r"\bexploration\b|\bintrinsic motivation\b|\bcount-based\b|\bcuriosity\b|\bnovelty\b|\bentropy\b", 2.5),
        (r"\bhierarchical rl\b|\boptions framework\b|\bsubgoal\b", 2),
        (r"\binverse reinforcement\b|\bimitation learning\b|\bbehavioral cloning\b|\bbehavior cloning\b|\bgail\b", 2.5),
        (r"\bmeta-rl\b|\bfew-shot rl\b|\bcontinual rl\b|\btest-time\b.*\brl\b|\bcredit assignment\b", 2.5),
        (r"\bvalue function\b|\badvantage\b|\bpolicy optimization\b|\bactor\b", 2),
        (r"\bself-play\b|\bzero-sum game\b|\bmatrix game\b|\bgame-theoretic\b|\bself-improv\w+\b", 2),
        (r"\brl agent\w*|\bagentic rl\b|\bswe agent\w*|\bweb agent\w*|\bvlm\b.*\brl\b", 2),
    ],
}

OFF = re.compile(
    r"\bmedical imag|\bclinical\b|\bdiagnos|\bsepsis|\btumor\b|\bradiolog|\bprotein|\bmolecul"
    r"|\bdrug\b|\bgenom|\bneurosurg|\bremote sensing|\bsar image|\bsatellite|\bhyperspectral"
    r"|\bnetwork traffic\b|\bmalware\b|\bphishing\b|\bfinancial\b|\bstock\b|\beeg\b|\bfraud\b",
    re.I)


def write_outputs(work: Path, papers: list[dict], days: list[str], per_day: dict) -> None:
    (work / "raw_papers.json").write_text(json.dumps(papers, ensure_ascii=False, indent=1), encoding="utf-8")
    esc = lambda s: s.replace("|", "\\|")
    label = days[0] if len(days) == 1 else f"{days[0]}..{days[-1]}"
    L = [f"# Phase 1 - arxiv Listing ({label} listing date)", "", f"Count: {len(papers)}", "",
         "| arxiv_id | title | authors | categories | abs_url | pdf_url |",
         "| --- | --- | --- | --- | --- | --- |"]
    for p in papers:
        a = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        L.append(f"| {p['arxiv_id']} | {esc(p['title'])} | {esc(a)} | "
                 f"{esc(', '.join(p['categories']))} | {esc(p['abs_url'])} | {esc(p['pdf_url'])} |")
    (work / "phase1_listing.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    bounds = {d: window_bounds(d) for d in days}
    (work / "window.json").write_text(json.dumps(
        {"listing_days": days, "utc_windows": bounds, "per_day_raw": per_day,
         "unique_total": len(papers)}, indent=1), encoding="utf-8")


def prefilter(work: Path, papers: list[dict]) -> None:
    pools = {t: [] for t in TRACKS}
    for p in papers:
        ti, al = p["title"], p["title"] + " " + p["abstract"]
        if OFF.search(ti):
            continue
        for t, kws in TRACKS.items():
            s = 0.0
            for pat, w in kws:
                if re.search(pat, ti, re.I):
                    s += w * 2
                elif re.search(pat, al, re.I):
                    s += w
            if s > 0:
                pools[t].append({"base_id": p["base_id"], "title": ti, "score": round(s, 1),
                                 "categories": p["categories"]})
    for t in pools:
        pools[t].sort(key=lambda x: -x["score"])
    (work / "candidates.json").write_text(json.dumps(pools, ensure_ascii=False, indent=1), encoding="utf-8")
    print("pools:", {t: len(v) for t, v in pools.items()})
    for t in TRACKS:
        print(f"\n=== {t} top 16 ===")
        for x in pools[t][:16]:
            print(f"  {x['score']:5.1f} {x['base_id']:12s} {x['title'][:88]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="workdir under codex_temp/")
    ap.add_argument("--days", help="comma-separated arXiv listing dates (YYYYMMDD)")
    ap.add_argument("--auto", type=int, help="probe back N days, use newest non-empty day")
    ap.add_argument("--top", type=int, default=16)
    args = ap.parse_args()
    work = Path(args.out)
    work.mkdir(parents=True, exist_ok=True)

    fetcher = Fetcher()

    if args.days:
        days = []
        for d in (x.strip() for x in args.days.split(",") if x.strip()):
            # accept YYYYMMDD or YYYY-MM-DD; the value is the arXiv *listing*
            # date, i.e. the date arXiv shows on its "new submissions" page
            d = d.replace("-", "")
            if len(d) != 8 or not d.isdigit():
                raise SystemExit(f"bad --days value: {d!r} (expected YYYYMMDD)")
            days.append(f"{d[:4]}-{d[4:6]}-{d[6:]}")
    else:
        today = datetime.now(timezone.utc)
        newest = fetcher.latest_day()
        print(f"[probe] newest announced listing day = {newest}", file=sys.stderr)
        if not newest:
            print("[probe] no announced batch found", file=sys.stderr)
            return 1
        days = [newest]
        lag = (today - datetime.strptime(newest, "%Y-%m-%d").replace(tzinfo=timezone.utc)).days
        lo, hi = window_bounds(newest)
        print(f"[probe] using listing day {newest} (UTC window {lo} .. {hi})", file=sys.stderr)

    merged, per_day = {}, {}
    for day in days:
        n0 = 0
        for cat in CATS:
            rows = fetcher.day(cat, day)
            n0 += len(rows)
            for r in rows:
                k = r["base_id"]
                if k in merged:
                    merged[k]["categories"] = sorted(set(merged[k]["categories"]) | set(r["categories"]))
                else:
                    r["categories"] = sorted(r["categories"])
                    merged[k] = r
            print(f"  [fetch] {day}/{cat}: {len(rows)}", file=sys.stderr)
        per_day[day] = n0
        print(f"[fetch] {day}: {n0} raw, merged {len(merged)}", file=sys.stderr)

    papers = sorted(merged.values(), key=lambda p: p["arxiv_id"], reverse=True)
    write_outputs(work, papers, days, per_day)
    from collections import Counter
    c = Counter(x for p in papers for x in p["categories"])
    print(f"\nTOTAL {len(papers)} unique | days {days} | arxiv calls {fetcher.calls}")
    print("per-day raw:", per_day)
    print("cats:", dict(c.most_common(10)))
    prefilter(work, papers)
    return 0


if __name__ == "__main__":
    sys.exit(main())
