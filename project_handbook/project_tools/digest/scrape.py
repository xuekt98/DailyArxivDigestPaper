#!/usr/bin/env python3
"""Digest Phase 1 — arXiv scraper + keyword prefilter.

Project tool for the daily arXiv digest. Sequential arxiv calls only, 3s apart
(skill rate limit). Fetches per (category, day) so no category-day is silently
truncated by max_results.

Usage:
  python scrape.py --out <workdir> [--days 20261015] [--days 20261015,20261016]
  python scrape.py --out <workdir> --auto 3   # probe back N days, use newest non-empty

Outputs into <workdir>: raw_papers.json, phase1_listing.md, candidates.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "http://export.arxiv.org/api/query"
RATE = 3.0
NS = {"atom": "http://www.w3.org/2005/Atom"}
CATS = ["cs.CV", "cs.SD", "eess.AS", "cs.CL", "cs.AI", "cs.RO", "cs.LG"]


def fetch(url: str, label: str) -> bytes:
    s = RATE
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "arxiv-daily-digest/0.2"})
            with urllib.request.urlopen(req, timeout=60) as r:
                if r.status == 429:
                    raise RuntimeError("429")
                return r.read()
        except Exception as exc:
            if attempt >= 3:
                raise
            print(f"  retry {attempt} [{label}]: {exc}", file=sys.stderr)
            time.sleep(s)
            s *= 2
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


def url_for(cats: list[str], start: str, end: str, n: int = 300) -> str:
    clause = " OR ".join(f"cat:{c}" for c in cats)
    query = f"({clause}) AND submittedDate:[{start} TO {end}]"
    return f"{API}?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results={n}"


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
    L = [f"# Phase 1 - arxiv Listing ({label} UTC)", "", f"Count: {len(papers)}", "",
         "| arxiv_id | title | authors | categories | abs_url | pdf_url |",
         "| --- | --- | --- | --- | --- | --- |"]
    for p in papers:
        a = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        L.append(f"| {p['arxiv_id']} | {esc(p['title'])} | {esc(a)} | "
                 f"{esc(', '.join(p['categories']))} | {esc(p['abs_url'])} | {esc(p['pdf_url'])} |")
    (work / "phase1_listing.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (work / "window.json").write_text(json.dumps(
        {"days": days, "per_day_raw": per_day, "unique_total": len(papers)}, indent=1), encoding="utf-8")


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
    ap.add_argument("--days", help="comma-separated YYYYMMDD UTC days")
    ap.add_argument("--auto", type=int, help="probe back N days, use newest non-empty day")
    ap.add_argument("--top", type=int, default=16)
    args = ap.parse_args()
    work = Path(args.out)
    work.mkdir(parents=True, exist_ok=True)

    if args.days:
        days = [d.strip() for d in args.days.split(",") if d.strip()]
    else:
        today = datetime.now(timezone.utc)
        days = None
        for back in range(0, (args.auto or 7) + 1):
            d = (today - timedelta(days=back)).strftime("%Y%m%d")
            rows = parse(fetch(url_for(CATS, d + "0000", d + "2359", 5), f"probe {d}"), d)
            print(f"[probe] {d} -> {len(rows)}", file=sys.stderr)
            if rows:
                days = [d]
                print(f"[probe] using {d} ({back}d behind)", file=sys.stderr)
                break
            time.sleep(RATE)
        if not days:
            print("[probe] no announced batch found", file=sys.stderr)
            return 1

    merged, per_day = {}, {}
    for day in days:
        n0 = 0
        for cat in CATS:
            rows = parse(fetch(url_for([cat], day + "0000", day + "2359"), f"{day}/{cat}"), day)
            n0 += len(rows)
            for r in rows:
                k = r["base_id"]
                if k in merged:
                    merged[k]["categories"] = sorted(set(merged[k]["categories"]) | set(r["categories"]))
                else:
                    r["categories"] = sorted(r["categories"])
                    merged[k] = r
            if len(rows) >= 300:
                print(f"[warn] {day}/{cat} truncated at max_results=300", file=sys.stderr)
            time.sleep(RATE)
        per_day[day] = n0
        print(f"[fetch] {day}: {n0} raw, merged {len(merged)}", file=sys.stderr)

    papers = sorted(merged.values(), key=lambda p: p["arxiv_id"], reverse=True)
    write_outputs(work, papers, days, per_day)
    from collections import Counter
    c = Counter(x for p in papers for x in p["categories"])
    print(f"\nTOTAL {len(papers)} unique | days {days}")
    print("per-day raw:", per_day)
    print("cats:", dict(c.most_common(10)))
    prefilter(work, papers)
    return 0


if __name__ == "__main__":
    sys.exit(main())