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
from datetime import date, datetime, timedelta, timezone, time as _time
from pathlib import Path

API = "https://export.arxiv.org/api/query"
RATE = 5.0
PAGE = 300
# arXiv closes submissions at 14:00 US Eastern and announces at 20:00 ET.
# The announcement arXiv lists under date D therefore holds every paper whose
# v1 `published` timestamp falls between the 14:00-ET deadline on D-1 and the
# 14:00-ET deadline on D -- the batch straddles two UTC calendar days.
# Filtering on the calendar date of `published` alone would silently drop the
# D-1 evening half of every announcement (~21% of the tracked categories on
# the 2026-10-21 listing).
#
# The deadline is NOT a fixed UTC instant: 14:00 ET is 18:00 UTC while Eastern
# is on daylight time (EDT, UTC-4) and 19:00 UTC while it is on standard time
# (EST, UTC-5). Eastern leaves daylight time on the first Sunday of November,
# so from 2026-11-01 onward the cutoff sits one hour later in UTC. The hard
# coded 18:00 the digest used during EDT therefore started missing the final
# hour of every announcement (and duplicated the first hour of the previous
# one) after the 2026-10-31 -> 2026-11-01 transition. `deadline_utc()` below
# resolves the offset per date instead.
NS = {"atom": "http://www.w3.org/2005/Atom"}
CATS = ["cs.CV", "cs.SD", "eess.AS", "cs.CL", "cs.AI", "cs.RO", "cs.LG"]


def _us_eastern_is_dst(d: date) -> bool:
    """True when US Eastern is on daylight time (EDT, UTC-4) on date `d`.

    US daylight time runs from the 2nd Sunday of March to the 1st Sunday of
    November. The 14:00-ET submission deadline is never inside the ambiguous
    01:00-03:00 local hour, so the date-level rule is exact for our purpose.
    """
    mar1 = date(d.year, 3, 1)
    nov1 = date(d.year, 11, 1)
    dst_start = mar1 + timedelta(days=(6 - mar1.weekday()) % 7 + 7)
    dst_end = nov1 + timedelta(days=(6 - nov1.weekday()) % 7)
    return dst_start <= d < dst_end


def deadline_utc(d: date) -> datetime:
    """arXiv's submission deadline for date `d`: 14:00 US Eastern, in UTC.

    18:00 UTC during EDT, 19:00 UTC during EST.
    """
    offset = -4 if _us_eastern_is_dst(d) else -5
    return datetime.combine(d, _time(14, 0, 0)) - timedelta(hours=offset)


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
    listing. The corresponding announcement fires the next day and contains v1
    timestamps from the 14:00-ET deadline on `listing_day - 1` up to the
    14:00-ET deadline on `listing_day` -- i.e. 18:00 UTC during EDT and
    19:00 UTC during EST, so the window is not a fixed UTC instant.
    """
    d = datetime.strptime(listing_day, "%Y-%m-%d").date()
    lo = deadline_utc(d - timedelta(days=1))
    hi = deadline_utc(d)
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

        That announcement spans two UTC calendar days: the 14:00-ET deadline on
        the previous day through the 14:00-ET deadline on `listing_day`
        (18:00 UTC during EDT, 19:00 UTC during EST). Papers stamped after that
        deadline belong to the *next* announcement and are excluded here.
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

        The newest v1 timestamp on arXiv always falls before the 14:00-ET
        deadline of its own UTC day (everything from the deadline onwards waits
        for the next announcement), so the calendar date of the newest entry is
        exactly the listing date of the newest batch.
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
    # ---- skill v0.4.0: 4 tracks -------------------------------------------
    # aigc_visual   = AIGC image/video/3D/4D generation & editing
    #                 + RL / preference optimization for visual generation
    # duplex_speech = full-duplex / real-time / streaming speech LMs, TTS
    # speech_rl     = RL / preference optimization for speech & audio LMs
    # world_embodied= world models + embodied AI / VLA / robot learning
    #                 + RL used for embodied work
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
        (r"\bpersonaliz\w+|\bsubject-driven\b|\bidentity preservation\b|\bmulti-subject\b", 2),
        (r"\bconsistency model\b|\bdistillation\b|\bdistill\w+ (model|step)|\bone-step\b|\bfew-step\b", 1),
        (r"\bvisual generation\b|\bsynthesiz\w+ (image|video|scene)", 1.5),
        (r"\b4d generation\b|\bdynamic 3d\b|\b4d reconstruction\b|\b4d\b", 2),
        (r"\bautoregressive.*\b(image|video)\b|\bvisual tokenizer\b|\bvideo tokenizer\b|\btokenizer\b", 2),
        (r"\bmotion (generation|synthesis|transfer)\b|\bhuman motion\b|\bmotion customization\b", 1),
        (r"\bwatermark\w*|\bprovenance\b|\bdeepfake\b", 1),
        (r"\bcache\b.*\b(diffusion|denois)|\bacceleration\b|\bsparse attention\b|\baccelerat\w+\b", 1),
        # RL / preference optimization for visual generation (folded in from the
        # removed rl_aigc track) - conjunctions only, so text-only RL stays out.
        (r"\bdpo\b|\bdiffusion[- ]dpo\b|\bpreference optimiz\w+|\bpreference alignment\b", 3),
        (r"\bverifiable reward\w*|\brubric\b|\bprocess reward\w*|\bartifact-as-rubric\b", 2.5),
        (r"\bbest[- ]of[- ]n\b|\brejection sampling\b|\bclassifier[- ]free guidance\b|\bcfg\b", 2),
        (r"\bgeneval\b|\bdrawbench\b|\bhpsv2\b|\bpickscore\b|\bimagereward\b|\baesthetic score\b", 2.5),
        (r"(?s)\b(reinforcement learning|rlhf|grpo|policy optimization|policy gradient|"
         r"reward model|preference optimization|reward-weighted)\b.{0,120}?"
         r"\b(diffusion|image|video|visual|flow matching|3d|4d|generative|generation)\b", 4),
        (r"(?s)\b(diffusion|image|video|visual|flow matching|generative|generation)\b.{0,120}?"
         r"\b(reinforcement learning|rlhf|grpo|policy optimization|reward model|"
         r"preference optimization|reward-weighted)\b", 4),
    ],
    "duplex_speech": [
        (r"\bduplex\b|\bhalf-duplex\b|\bfull-duplex\b|\bturn-taking\b|\bbarge-in\b|\bfloor control\b", 3.5),
        (r"\bspeech-to-speech\b|\bs2s\b|\bspoken dialogue\b|\bvoice agent\b|\bvoice assistant\b", 3),
        (r"\baudio (llm|language model|foundation model)\b|\bspeech (llm|language model)\b", 3),
        (r"\blarge audio model\b|\bomni-modal\b|\bmulti-modal audio\b|\bmulti-modal llm\b|\bvisual llm\b|\blalm\b", 2),
        (r"\bconversational (ai|system)\b|\bspeech assistant\b|\bdialogue system\b|\bspoken (dialog|assistant)", 2.5),
        (r"\binterruptible\b|\bstreaming (speech|audio|tts)\b|\blow-latency speech\b|\breal-time speech\b", 2.5),
        (r"\btext-to-speech\b|\btts\b|\bspeech synthesis\b|\btts\b", 3),
        (r"\bvoice cloning\b|\bvoice conversion\b|\bvoice design\b|\bvoice identity\b|\btimbre\b", 3),
        (r"\bexpressive (tts|speech)\b|\bprosod\w+|\bspeech emotion\b|\bparalinguistic\b", 2),
        (r"\bneural audio codec\b|\bspeech codec\b|\bspeech tokeniz\w+|\baudio tokeniz\w+|\bvocoder\b", 2.5),
        (r"\bstream\w*\b.{0,40}\b(asr|speech recogn\w+|transducer)\b|\btransducer\b|\bspeech recognition\b|\basr\b", 2),
        (r"\bword error rate\b|\bcharacter error rate\b|\bwhisper\b|\bphoneme\b|\bspeaker embedding\b", 1.5),
        (r"\bspeech enhancement\b|\bspeech denoising\b|\bspeech separation\b|\bspeech editing\b|\bspeech restoration\b", 2),
        (r"\baudio understanding\b|\baudio question\b|\baudio reasoning\b|\bspeech understanding\b", 2),
        (r"\bvoice assistant\b|\bvoice agent\b|\bcall center\b|\bvoice pipeline\b", 2),
        (r"\bmultilingual\b.{0,30}\bspeech\b|\bcode-switch\w+\b|\blow-resource speech\b", 1.5),
        # music / general sound synthesis: no longer a tracked interest, kept
        # at low weight so it can only surface as a wild card
        (r"\bmusic generation\b|\btext-to-music\b|\bsound generation\b|\bsource separation\b", 0.8),
    ],
    "speech_rl": [
        (r"(?s)\b(reinforcement learning|rlhf|grpo|rlaif|rlvr|dpo|ipo|kto|orpo|"
         r"policy optimization|policy gradient|ppo|reward model\w*|reward modeling|"
         r"preference optimiz\w+|preference learning|rejection sampling|best[- ]of[- ]n)\b"
         r".{0,140}?\b(speech|audio|tts|voice|spoken|asr|sound|acoustic|music)\b", 5),
        (r"(?s)\b(speech|audio|tts|voice|spoken|asr|sound|acoustic|music)\b.{0,140}?"
         r"\b(reinforcement learning|rlhf|grpo|rlaif|rlvr|dpo|ipo|kto|orpo|"
         r"policy optimization|policy gradient|ppo|reward model\w*|reward modeling|"
         r"preference optimiz\w+|preference learning|rejection sampling|best[- ]of[- ]n)\b", 5),
        (r"\bexploration\b.{0,40}\bspeech\b|\bentropy\b.{0,40}\bspeech\b|\bexploration\b.{0,40}\baudio\b", 2.5),
        (r"\bdialogue policy\b|\bmulti-turn spoken\b|\bspoken dialogue optimiz\w+|\blong-horizon dialogue\b", 3),
        (r"\boveroptimiz\w+|\breward hacking\b|\blength bias\b|\blatency bias\b", 2),
        (r"\bllm-as-judge\b.{0,40}\b(speech|audio)\b|\bjudge\b.{0,40}\b(speech|audio)\b", 2),
        (r"\bverifiable reward\w*", 1),
        (r"\bself-improv\w+.{0,40}\b(speech|audio)\b", 2),
    ],
    "world_embodied": [
        (r"\bembodied (ai|agent|intelligence)\b|\bembodied\b", 3),
        (r"\brobot(ic)? (learning|policy|policies|manipulation|navigation)\b|\bmanipulation\b|\bgrasping\b", 3),
        (r"\bvla\b|\bvision-language-action\b|\bvtla\b|\bgeneralist robot\b", 3.5),
        (r"\bworld model\b|\bworld models\b|\blatent dynamics\b|\bjepa\b|\bv-jepa\b|\bdino-wm\b", 3.5),
        (r"\bvisual navigation\b|\bvisual exploration\b|\bnavigation\b|\bembodied navigation\b", 2),
        (r"\bmobile manipulation\b|\bhousehold task\b|\bopen x-embodiment\b|\bhumanoid\b|\bdexterous\b", 3),
        (r"\bsim-to-real\b|\bsim2real\b|\bdomain randomization\b|\breal-to-sim\b", 3),
        (r"\baction chunk\w*|\bdiffusion polic\w+\b|\bpolicy learning\b|\bpolicy optimization\b", 2),
        (r"\bneural simulator\b|\blearned simulator\b|\bdynamics model\b|\bforward model\b", 2),
        (r"\bteleoperat\w+|\bquadruped\b|\bdrone\b|\buav\b|\brobot arm\b", 1.5),
        (r"\btactile\b|\bvisuotactile\b|\bforce (feedback|control|sensing)\b|\bcontact\b", 2),
        (r"\bmodel-based planning\b|\bplanning\b|\btrajectory (prediction|optimization)\b", 1.5),
        # RL used for embodied work (folded in from the removed rl_core track)
        (r"(?s)\b(reinforcement learning|rl|policy optimization|policy gradient|sim-to-real|"
         r"domain randomization|reward shaping|reward model\w*|offline rl|model-based rl)\b"
         r".{0,120}?\b(robot|manipulat\w+|embodied|vla|locomotion|grasping|humanoid|"
         r"dexterous|simulation|simulator)\b", 4),
        (r"(?s)\b(robot|manipulat\w+|embodied|vla|locomotion|grasping|humanoid|dexterous)\b"
         r".{0,120}?\b(reinforcement learning|policy optimization|policy gradient|"
         r"reward shaping|reward model\w*|sim-to-real)\b", 4),
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
