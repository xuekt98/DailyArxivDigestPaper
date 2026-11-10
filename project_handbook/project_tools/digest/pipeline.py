#!/usr/bin/env python3
"""Daily digest pipeline for the daily-arxiv-paper project.

Reusable, date-parameterised machinery around scrape.py / read.py. Everything
mechanical lives here so a daily run only has to author two inputs:

  <work>/selection_input.json   -- the picked papers (id / relevance /
                                   quality / wild) per direction + wild-card
                                   reasons + per-direction summaries
  <work>/index_section.md        -- the index.md toc row + detail section

Subcommands:
  pool      build wide keyword candidate pools for the 4 axes
  vocab     write per-direction task badge vocabularies
  spec      write meta_spec.md + assign_meta_{a..d}.json for the meta workers
  select    validate the authored selection and emit selection.json/shortlist.json
  checkmeta validate the 4 meta modules against the meta contract
  render    write 8 md files + res/ figures
  verify    full structural verification of the rendered output
  index     insert the authored toc row + detail section into index.md

Usage:
  python -X utf8 pipeline.py <subcommand> --work <dir> [--date D --listing L --repo R]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------------------
# skill v0.8.0: 4 axes x 10 directions, day target 60.
#   aigc_visual   = AIGC image/video/3D/4D generation & editing
#                   (aigc_generation / aigc_editing / aigc_rl)
#   llm_vlm       = LLM + VLM + their RL
#                   (llm_core / vlm_core / llm_vlm_rl)
#   duplex_speech = full-duplex / real-time / streaming speech LMs, TTS
#                   (duplex_speech_core / speech_rl)
#   world_embodied= world models + embodied AI / VLA / robot learning
#                   (world_model / embodied_ai)
# ---------------------------------------------------------------------------
AXES = ["aigc_visual", "llm_vlm", "duplex_speech", "world_embodied"]
DAILY_TOTAL = 60
AXIS_CAP = 20
AXIS_BASE = {"aigc_visual": 15, "llm_vlm": 18,
             "duplex_speech": 12, "world_embodied": 15}
DIR_BASE = {"aigc_generation": 8, "aigc_editing": 4, "aigc_rl": 3,
            "llm_core": 8, "vlm_core": 5, "llm_vlm_rl": 5,
            "duplex_speech_core": 8, "speech_rl": 4,
            "world_model": 7, "embodied_ai": 8}
AXIS_DIRS = {
    "aigc_visual": ["aigc_generation", "aigc_editing", "aigc_rl"],
    "llm_vlm": ["llm_core", "vlm_core", "llm_vlm_rl"],
    "duplex_speech": ["duplex_speech_core", "speech_rl"],
    "world_embodied": ["world_model", "embodied_ai"],
}
DIRECTIONS = [d for a in AXES for d in AXIS_DIRS[a]]
DIR_AXIS = {d: a for a, ds in AXIS_DIRS.items() for d in ds}

AXIS_CN = {
    "aigc_visual": ("AIGC 视觉生成与编辑", "AIGC-visual",
                    "图像 / 视频 / 3D / 4D 内容的生成与编辑，以及面向视觉生成的 "
                    "RL / 偏好优化与奖励模型"),
    "llm_vlm": ("LLM / VLM 与其强化学习", "LLM-VLM",
                "大语言模型与视觉语言模型的设计、推理、agent、效率与上下文工作，"
                "以及面向 LLM / VLM 的 RL 与偏好优化、奖励模型"),
    "duplex_speech": ("全双工语音与语音 LM", "duplex-speech",
                      "全双工 / 实时 / 流式语音语言模型、speech-to-speech 语音助手、"
                      "TTS / 语音克隆 / 语音转换，以及语音大模型的 RL 与奖励模型"),
    "world_embodied": ("具身智能与世界模型", "embodied",
                       "世界模型、学习型模拟器与具身智能，含移动操作、人形控制、"
                       "触觉反射、VLA 策略与面向具身任务的强化学习"),
}
DIR_CN = {
    "aigc_generation": "AIGC 生成（图像 / 视频 / 3D / 4D）",
    "aigc_editing": "AIGC 编辑（指令编辑 / 修补 / 个性化）",
    "aigc_rl": "面向视觉生成的 RL 与奖励模型",
    "llm_core": "LLM 核心（架构 / 推理 / agent / 效率 / 上下文）",
    "vlm_core": "VLM 核心（多模态架构 / 理解 / 视频 / GUI agent）",
    "llm_vlm_rl": "LLM / VLM 的 RL 与偏好优化",
    "duplex_speech_core": "全双工语音与语音 LM",
    "speech_rl": "语音 LM 的 RL 与偏好优化",
    "world_model": "世界模型与学习型模拟器",
    "embodied_ai": "具身智能与机器人学习",
}

# ---------------------------------------------------------------------------
# task badge vocabularies (skill v0.8.0 assets/entry.template.md, 10 disjoint
# per-direction lists) + a small number of tracked extras
# ---------------------------------------------------------------------------
VOCAB_BASE = {
    "aigc_generation": [
        "Image_Generation", "Video_Generation", "3D_Generation", "4D_Generation",
        "Diffusion_Model", "Flow_Matching", "Consistency_Model",
        "Controllable_Generation", "Multi_Subject_Personalization", "Layout_to_Image",
    ],
    "aigc_editing": [
        "Image_Editing", "Video_Editing", "3D_Editing",
        "Inpainting", "Outpainting", "Instruction_Editing",
        "Identity_Preservation", "Style_Transfer", "Subject_Personalization",
    ],
    "aigc_rl": [
        "RL_for_Diffusion", "RL_for_Flow_Matching", "Diffusion_DPO",
        "Reward_Model_Image", "Reward_Weighted_Regression",
        "Best_of_N", "Rejection_Sampling", "Classifier_Guidance",
        "GenEval", "DrawBench", "HPSv2", "Aesthetic_Scoring",
    ],
    "llm_core": [
        "LLM_Architecture", "MoE", "State_Space_Model", "Pretraining", "Scaling_Law",
        "Reasoning", "Chain_of_Thought", "Test_Time_Compute", "Verifier",
        "Agent", "Tool_Use", "Function_Calling", "Multi_Agent", "Code_Agent",
        "Inference_Efficiency", "Quantization", "KV_Cache", "Speculative_Decoding",
        "Distillation", "Long_Context", "RAG", "Retrieval", "In_Context_Learning",
        "Hallucination", "Safety_Alignment", "Watermarking", "Model_Editing",
        "Code_Generation", "Math_Reasoning",
    ],
    "vlm_core": [
        "VLM_Architecture", "MLLM", "Vision_Language_Model", "Visual_Instruction_Tuning",
        "Image_Captioning", "VQA", "Visual_Grounding", "Spatial_Reasoning",
        "Video_Understanding", "Video_QA", "Temporal_Grounding",
        "GUI_Agent", "Screen_Understanding", "Computer_Use",
        "Document_Understanding", "Chart_Understanding", "OCR",
        "Multimodal_Hallucination", "Multimodal_Reasoning",
    ],
    "llm_vlm_rl": [
        "RLHF", "PPO_RLHF", "RLAIF", "DPO", "IPO", "KTO", "ORPO",
        "GRPO", "RLVR", "Reward_Modeling", "Preference_Optimization",
        "Process_Reward_Model", "Outcome_Reward_Model",
        "Agent_RL", "RL_Reasoning", "Exploration", "Reward_Hacking",
        "Multimodal_RLHF", "Multimodal_DPO", "Multimodal_GRPO",
        "VLM_Reward_Model", "VLFeedback", "MMAU", "RewardBench",
    ],
    "duplex_speech_core": [
        "Full_Duplex", "Voice_Assistant", "Speech_to_Speech",
        "Real_Time_Speech", "Streaming_ASR", "Turn_Taking", "Barge_In",
        "Speech_LM", "Audio_LM", "Audio_Understanding",
        "TTS", "Voice_Cloning", "Voice_Conversion",
        "Streaming_TTS", "Expressive_TTS", "Spoken_Dialogue",
    ],
    "speech_rl": [
        "RLHF_Speech", "GRPO_Speech", "RLAIF_Speech", "DPO_Speech",
        "Speech_Reward_Model", "Audio_Quality_Optimization", "Reward_Modeling",
        "RLVR_Speech", "Dialogue_Policy_Optimization",
        "RL_for_ASR", "RL_for_TTS", "Exploration_Speech", "Rejection_Sampling",
    ],
    "world_model": [
        "World_Model", "Video_as_World_Model", "Latent_Dynamics",
        "Neural_Simulator", "Learned_Simulator", "JEPA", "Dreamer",
        "Model_Based_RL", "Planning_with_World_Model", "Action_Conditioned_Prediction",
    ],
    "embodied_ai": [
        "Embodied_Agent", "Visual_Navigation", "Manipulation", "Dexterity",
        "Sim_to_Real", "Robot_Learning", "VLA_Model", "Robot_Foundation_Model",
        "Diffusion_Policy", "Action_Chunking", "Tactile_Sensing",
        "Long_Horizon_Task", "Household_Task", "Imitation_Learning",
    ],
}

VOCAB_EXTRA = {
    "aigc_generation": [
        "Video_Acceleration", "Diffusion_Distillation", "Tokenizer_Compression",
        "Motion_Generation", "4D_Reconstruction", "Scene_Generation",
    ],
    "aigc_editing": ["Video_Inpainting", "Layout_Control", "Identity_Generation"],
    "aigc_rl": ["Reward_Model_Video", "RL_for_Video", "Preference_Optimization_Visual",
                 "RL_for_3D_Generation"],
    "llm_core": [
        "Reasoning_Distillation", "LLM_Evaluation", "Agent_Memory",
        "Long_Context_Compression", "Data_Curation", "Sparse_Attention",
        "Training_Infrastructure",
    ],
    "vlm_core": ["Video_Captioning", "Grounding_Accuracy", "Omni_Model",
                 "Test_Time_Adaptation"],
    "llm_vlm_rl": ["RL_for_Reasoning", "GRPO_Video", "Reward_Model_Multimodal"],
    "duplex_speech_core": [
        "Speech_Recognition", "Speech_Enhancement", "Speech_Editing",
        "Neural_Audio_Codec", "Low_Resource_ASR", "Accent_Conversion",
        "Speech_Tokenization", "Audio_Editing", "Speech_Embedding",
        "Speech_Emotion_Recognition",
    ],
    "speech_rl": ["Reward_Model_Audio", "Audio_RL", "Speech_Preference_Learning",
                   "RL_for_Audio_Generation"],
    "world_model": ["World_Action_Model", "Video_Prediction", "Driving_Simulation",
                    "Traversability_Estimation"],
    "embodied_ai": [
        "Mobile_Manipulation", "Humanoid_Control", "Policy_Diffusion",
        "Scene_Reconstruction", "Robot_Foundation_Pretraining",
        "Planning_with_Reward_Model", "Physics_Simulator",
        "Computer_Use_Embodied",
    ],
}

META_ASSIGN = {
    "meta_a": ["aigc_generation", "aigc_editing", "aigc_rl"],
    "meta_b": ["llm_core", "vlm_core"],
    "meta_c": ["llm_vlm_rl"],
    "meta_d": ["duplex_speech_core", "speech_rl"],
    "meta_e": ["world_model", "embodied_ai"],
}

# ---------------------------------------------------------------------------
# wide candidate-pool sweep (supplementary to scrape.py's own taxonomy)
# ---------------------------------------------------------------------------
POOL_EXTRA = {
    "aigc_visual": r"""
        \bgenerat\w+ (image|video|scene|3d|view|avatar|character|mesh|point cloud)\b
        |\bimage-to-video\b|\bvideo-to-video\b|\btext2image\b|\btext2video\b|\bt2i\b|\bt2v\b
        |\bautoregressive (image|video)\b|\bdiffusion\b|\bflow matching\b
        |\bgaussian splatting\b|\b3dgs\b|\bnerf\b|\bnovel view\b|\bview synthesis\b
        |\bimage editing\b|\bvideo editing\b|\bediting (task|method|framework)\b
        |\bcontent (creation|generation)\b|\bvisual generation\b|\bvisual (tokenizer|autoencoder)\b
        |\bmulti-view\b|\bvideo diffusion\b
        |\bpersonaliz\w+ (image|video|subject)\b|\bsubject-driven\b
        |\bicon generation\b|\bposter\b|\bfont generation\b|\btext rendering\b|\btext-rendering\b
        |\bgeneration benchmark\b
        |\b(reinforcement learning|grpo|dpo|rlhf|policy optimization|reward model\w*)\b.{0,120}?
          \b(diffusion|image|video|visual|flow matching|3d|generation)\b
        |\b(diffusion|image|video|visual|flow matching|generation)\b.{0,120}?
          \b(reinforcement learning|grpo|dpo|rlhf|policy optimization|reward model\w*)\b
        |\bpreference (optimization|alignment)\b|\bbest[- ]of[- ]n\b|\bclassifier[- ]free guidance\b
        |\bgeneval\b|\bdrawbench\b|\bhpsv2\b|\bpickscore\b|\bimagereward\b|\baesthetic score\b
        |\bverifiable reward\w*|\brubric\b
    """,
    "llm_vlm": r"""
        \b(large language model|llm|decoder-only|encoder-decoder)\b
        |\bmixture[- ]of[- ]experts\b|\bmoe\b|\bstate[- ]space model\w*|\bmamba\b|\brwkv\b
        |\blinear attention\b|\bgqa\b|\bmqa\b|\brope\b|\bscaling law\w*
        |\b(chain[- ]of[- ]thought|reasoning (model|distillation|trace|scaling)|test[- ]time compute|self-consistency)\b
        |\bverifier\w*\b|\bprocess reward model\b|\boutcome reward model\b
        |\b(llm[- ]?(based )?agent\w*|agentic (workflow|system)|tool use|function calling|react|multi[- ]agent|code agent|swe[- ]?bench|web agent|computer[- ]use agent)\b
        |\b(quantiz\w+|kv[- ]cache|speculative decoding|pruning|inference accelerat\w+|serving throughput)\b
        |\b(long[- ]context|context (extension|window|compression)|in-context learning)\b
        |\b(rag|retrieval[- ]augmented|dense retrieval|re[- ]ranker|knowledge editing|model editing)\b
        |\b(hallucinat\w+|factualit\w+|jailbreak\w*|guardrail\w*|safety alignment|watermarking|unlearning|memorization)\b
        |\b(code generation|program synthesis|theorem prov\w+|mathematical reasoning|formal proof)\b
        |\b(vision[- ]language model\w*|vlm\w*|multimodal llm|mllm|omni[- ]modal|vision encoder|visual encoder)\b
        |\b(q[- ]former|resampler|connector|visual token\w*|visual instruction tuning|multimodal sft)\b
        |\b(image caption\w+|video caption\w+|vqa|visual question answer\w+|visual grounding|referring expression|spatial reasoning)\b
        |\b(video understanding|video[- ]llm|video question answer\w+|temporal grounding|moment retrieval)\b
        |\b(gui agent|screen understanding|computer[- ]use|document understanding|chart understanding|ocr)\b
        |\b(rlhf|ppo[- ]rlhf|rlaif|dpo|ipo|kto|orpo|preference (data|optimization|alignment)|grpo|rlvr|reward model\w*|reward modeling)\b
        |\b(reward hacking|overoptimiz\w+|length bias|agentic rl|iterative rl|online rl|rejection sampling)\b
        |\b(multimodal rlhf|mm[- ]rlhf|multimodal preference|multimodal grpo|vlm[- ]as[- ]judge|vlm reward model|vlfeedback)\b
    """,
    "duplex_speech": r"""
        \b(tts|text-to-speech|speech synthesis|speech generation)\b
        |\bvoice (cloning|conversion|design|identity)\b|\bvoice (agent|assistant|interaction)\b
        |\bduplex\b|\bhalf-duplex\b|\bfull-duplex\b|\bturn-taking\b|\bbarge-in\b|\bfloor control\b
        |\bspeech-to-speech\b|\bs2s\b|\bspoken dialogue\b|\bspoken language\b|\bconversational (ai|system|agent)\b
        |\baudio (llm|language model|foundation model)\b|\bspeech (llm|language model)\b|\blalm\b
        |\bomni(modal)?\b|\bomni-?model\b|\bmultimodal (llm|assistant)\b
        |\bstream\w*\b.{0,40}\b(asr|speech recogn\w+|transducer|tts)\b|\bstreaming (speech|audio|tts)\b
        |\breal-time speech\b|\blow-latency speech\b|\binterruptible\b
        |\baudio (understanding|question|reasoning|qa|caption\w*|retrieval|memory|agent)\b
        |\bspeech (understanding|instruction|recognition|translation|emotion|tokeniz\w+)\b|\basr\b|\bwhisper\b
        |\bneural audio codec\b|\bspeech codec\b|\bvocoder\b|\bprosod\w+|\bspeech emotion\b
        |\bspeech enhancement\b|\bspeech denoising\b|\bspeech separation\b|\bspeech editing\b
        |\bparalinguistic\b|\bacoustic (model|scene|communication)\b
        |\bmultilingual\b.{0,30}\bspeech\b|\bcode-switch\w+\b|\blow-resource speech\b
        |\b(listening|hearing|auditory)\b|\bspeech dataset\b|\baudio dataset\b
        |\b(reinforcement learning|rlhf|grpo|rlaif|rlvr|dpo|ipo|kto|orpo|policy optimization|reward model\w*)\b
          .{0,140}?\b(speech|audio|tts|voice|spoken|asr)\b
        |\b(speech|audio|tts|voice|spoken|asr)\b.{0,140}?
          \b(reinforcement learning|rlhf|grpo|rlaif|rlvr|dpo|reward model\w*|preference optimiz\w+)\b
    """,
    "world_embodied": r"""
        \bembodied\b|\brobot\w*\b|\bhumanoid\b|\bmanipulat\w+\b|\bgrasp\w*\b|\bdexterous\b
        |\bvla\b|\bvision-language-action\b|\bworld model\b|\bjepa\b|\bnavigation\b
        |\blocomo(tion|otion)\b|\bwhole-body\b|\bmanipulator\b|\brobot arm\b|\bquadruped\b|\bdrone\b|\buav\b
        |\btactile\b|\bvisuotactile\b|\bpropriocept\w+\b|\bforce (feedback|control)\b
        |\bsim-to-real\b|\bsim2real\b|\bdomain randomization\b|\bembodied (ai|agent|question|reasoning)\b
        |\bhousehold\b|\bscene (understanding|reconstruction)\b|\b3d (reconstruction|scene)\b
        |\bpolicy (learning|optimization|distillation)\b|\bdiffusion polic\w+\b|\baction chunk\w*\b
        |\bplanning\b|\btrajectory (prediction|optimization)\b|\bteleoperat\w+\b|\breward model\w*.*\brobot
        \b(reinforcement learning|policy optimization|policy gradient|sim-to-real|domain randomization|reward shaping|reward model\w*)\b
          .{0,120}?\b(robot|manipulat\w+|embodied|vla|locomotion|grasping|humanoid|dexterous|simulation|simulator)\b
        |\b(robot|manipulat\w+|embodied|vla|locomotion|grasping|humanoid|dexterous)\b.{0,120}?
          \b(reinforcement learning|policy optimization|policy gradient|reward shaping|reward model\w*|sim-to-real)\b
    """,
}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def scrape_module(repo: Path):
    spec = importlib.util.spec_from_file_location(
        "scrape_mod", repo / "project_handbook" / "project_tools" / "digest" / "scrape.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_vocab(work: Path) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    cur = None
    for line in (work / "task_vocab.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("=== "):
            cur = line[4:].split(" ")[0]
            out[cur] = set()
        elif line.startswith("  - ") and cur:
            out[cur].add(line[4:].strip())
    return out


def badge(text: str) -> str:
    t = str(text).strip()
    t = t.replace("—", "-").replace("–", "-").replace("·", "_")
    t = re.sub(r"\s+", "_", t)
    t = re.sub(r"[()\[\],;:!?'\"/\\]+", "", t)
    return t


def clean_caption(cap: str, limit: int = 250) -> str:
    c = re.sub(r"\s+", " ", str(cap or "")).strip()
    if len(c) > limit:
        c = c[:limit].rsplit(" ", 1)[0] + "…"
    return c


def short_org(org: str) -> str:
    o = str(org or "").strip()
    o = re.sub(r"^(The|Department of|Dept\.? of)\s+", "", o)
    o = o.split(",")[0].strip()
    o = re.sub(r"\s+(Inc\.|LLC|Ltd\.?|Ltd|Corp\.?|Corporation|Co\.,? Ltd\.?)$", "", o).strip()
    if len(o) > 42:
        o = o[:42].rsplit(" ", 1)[0]
    return o or "Unknown"


def strip_ver(u: str) -> str:
    return re.sub(r"v\d+$", "", str(u or ""))


def dir_section(rtxt: str, direction: str) -> str:
    """Return the `## <CN> · `<direction>` (N papers)` block of an axis report."""
    m = re.search(rf"^## .*`{re.escape(direction)}`.*$", rtxt, re.M)
    if not m:
        return ""
    rest = rtxt[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def load_meta(work: Path) -> dict:
    meta: dict = {}
    for name in META_ASSIGN:
        p = work / f"{name}.py"
        if not p.exists():
            raise SystemExit(f"[FATAL] missing {p}")
        ns: dict = {}
        exec(compile(p.read_text(encoding="utf-8"), str(p), "exec"), ns)
        for pid, v in ns["META"].items():
            if pid in meta:
                raise SystemExit(f"[FATAL] duplicate id across meta modules: {pid}")
            meta[pid] = v
    return meta


# ---------------------------------------------------------------------------
# subcommands
# ---------------------------------------------------------------------------
def cmd_pool(a) -> int:
    repo = Path(a.repo)
    sm = scrape_module(repo)
    papers = json.loads((a.work / "raw_papers.json").read_text(encoding="utf-8"))
    base = {k: [(re.compile(p, re.I), w) for p, w in v] for k, v in sm.TRACKS.items()}
    extra = {t: re.compile(p, re.I | re.X) for t, p in POOL_EXTRA.items()}

    pools = {t: [] for t in AXES}
    for p in papers:
        hay = f"{p.get('title','')}\n{p.get('abstract','')}"
        hit = {t: False for t in AXES}
        for src, rx in base.items():
            for pat, _w in rx:
                if pat.search(hay):
                    hit[src] = True
        for t in AXES:
            if extra[t].search(hay):
                hit[t] = True
        for t in AXES:
            if hit[t]:
                pools[t].append(p)

    out = []
    for t in AXES:
        out.append(f"===== {t}: {len(pools[t])} =====")
        for p in sorted(pools[t], key=lambda x: x["base_id"]):
            out.append(f"  {p['base_id']}  {p.get('title','')[:110]}")
    (a.work / "pools.txt").write_text("\n".join(out), encoding="utf-8")
    (a.work / "pool.json").write_text(
        json.dumps({t: [p["base_id"] for p in pools[t]] for t in AXES},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    for t in AXES:
        print(f"{t}: {len(pools[t])}")
    return 0


def cmd_vocab(a) -> int:
    out = []
    for t in DIRECTIONS:
        seen, uniq = set(), []
        for x in VOCAB_BASE[t] + VOCAB_EXTRA[t]:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        out.append(f"=== {t} ({len(uniq)}) ===")
        out += [f"  - {x}" for x in uniq]
        out.append("")
    (a.work / "task_vocab.txt").write_text("\n".join(out), encoding="utf-8")
    for t in DIRECTIONS:
        n = len(set(VOCAB_BASE[t] + VOCAB_EXTRA[t]))
        print(f"{t}: {n}")
    return 0


def cmd_spec(a) -> int:
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    vocab, cur = {}, None
    for line in (a.work / "task_vocab.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("=== "):
            cur = line[4:].split(" ")[0]
            vocab[cur] = []
        elif line.startswith("  - ") and cur:
            vocab[cur].append(line[4:].strip())

    L: list[str] = []
    A = L.append
    A(f"# meta 写作契约 — {a.date} 日报（listing day {a.listing}）")
    A("")
    A(f"你负责其中一部分论文的**手写分析元数据**。产物是一个 Python 模块文件 `meta_<x>.py`，")
    A("定义一个顶层字典 `META`，把 arxiv id 映射到分析字段。")
    A("")
    A(f"全天上限 {DAILY_TOTAL} 篇，4 个 axis × 10 个 direction；每篇论文只出现在一个 direction 里。")
    A("")
    A("## 输出文件格式（严格遵守）")
    A("")
    A("```python")
    A("# meta_a.py")
    A('META = {')
    A('    "2611.xxxxx": {')
    A('        "arch": "Snake_Case_Architecture_Name",')
    A('        "task": "Task_Tag_From_This_Direction_Vocab",')
    A('        "tags": ["kebab-case-tag", "kebab-case-tag", "kebab-case-tag"],')
    A('        "why": "为什么它进本 direction —— 中文，>= 30 字符，给出可核对的具体数字或方法要点。",')
    A('        "find": [')
    A('            "Finding: <从论文中直接抽取的事实，带具体数字>",')
    A('            "Inference: <由 finding 推出的判断，一行推理>",')
    A('            "Recommendation: <给读者的可执行建议>",')
    A('        ],')
    A('        "entry_desc": "中文一句话摘要，77-165 字符，不含 ** 粗体标记",')
    A('        "proj": "https://... 可选，项目主页；没有就省略这个 key",')
    A("    },")
    A("}")
    A("```")
    A("")
    A("## 字段规则")
    A("")
    A("| 字段 | 规则 |")
    A("| --- | --- |")
    A("| `arch` | 只允许 `[A-Za-z0-9_]+`（snake_case），不超过 5 个词 |")
    A("| `task` | **必须**取自该论文所属 **direction** 的词表，不得跨 direction 取词 |")
    A("| `tags` | 3-5 个，kebab-case（小写字母、数字、`-`），只允许 `[a-z0-9][a-z0-9-]*` |")
    A("| `why` | 中文，>= 30 字符，说明「为什么排这个位置」，要有具体数字 |")
    A("| `find` | 长度恰好 3 的**字符串列表**，每项以 `Finding: ` / `Inference: ` / `Recommendation: ` 开头（半角冒号 + 一个空格），每项 >= 15 字符 |")
    A("| `entry_desc` | 中文，77-165 字符（不是字节），不得包含 `**`，不得嵌套粗体 |")
    A("| `proj` | 可选，项目主页 URL（必须以 http 开头）；论文没有就**不要写这个 key** |")
    A("")
    A("## 硬性约束")
    A("")
    A("- 只写你被分配的那几篇，不要写别的论文，也不要改动其他文件。")
    A("- 每篇论文只出现在一个 direction 里，模块之间不要重复 id。")
    A("- **不得编造**数字、作者、机构。数字必须来自论文正文 / 摘要 / 图表；")
    A("  如果某个数字你在 `phase2_cards/<id>.json` 与 `extracted/<id>.txt` 里看不到，")
    A("  就不要写具体数值，改写成定性描述。")
    A("- 机构不由你负责（渲染器用 `orgs.json` + PDF 首页抽取的结果）。")
    A("- `find` 三条不要写成同一句话的改写：Finding 是事实，Inference 是推论，Recommendation 是行动建议。")
    A("- 全部用中文写（`arch` / `task` / `tags` 除外，它们是英文标识符）。")
    A("")
    A("## 数据来源")
    A("")
    A(f"- `{a.work.name}/selection.json` — 选稿与分数")
    A(f"- `{a.work.name}/phase2_cards/<arxiv_id>.json` — PDF 抽取的卡片（标题、摘要、作者、机构、图注）")
    A(f"- `{a.work.name}/extracted/<arxiv_id>.txt` — PDF 全文文本，`<<<PAGE n>>>` 分页")
    A(f"- `{a.work.name}/figures/` — 抽取的论文原图")
    A("")
    A("注意：`extracted/*.txt` 部分文件含 NUL 字节，ripgrep 会判为 binary 跳过；")
    A("取数请用 PowerShell `Select-String` 或 Python 读取，不要用 grep 工具。")
    A("")
    A("## 各 direction 的 task 词表（`task` 只能取自论文自己那个 direction）")
    A("")
    for t in DIRECTIONS:
        A(f"### {t}  ({len(vocab[t])})")
        A("")
        A("```")
        A("\n".join(vocab[t]))
        A("```")
        A("")
    A("## 逐篇建议 task")
    A("")
    A("下面是按分数排序的分配建议。**可以**在同 direction 词表内调整，但必须留在该 direction 词表里。")
    A("")
    for t in DIRECTIONS:
        A(f"### {t}  (axis: {DIR_AXIS[t]})")
        A("")
        for r in sel["selection"].get(t, []):
            wc = "  **[wild-card]**" if r["wild"] else ""
            A(f"- `{r['id']}` (score {r['score']}) — {r['title'][:96]}{wc}")
        A("")
    (a.work / "meta_spec.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    for name, dirs in META_ASSIGN.items():
        axes = sorted({DIR_AXIS[d] for d in dirs})
        ids, wild = [], []
        for d in dirs:
            for r in sel["selection"].get(d, []):
                ids.append(r["id"])
                if r["wild"]:
                    wild.append(r["id"])
        (a.work / f"assign_{name}.json").write_text(json.dumps(
            {"module": name, "axes": axes, "directions": dirs, "ids": ids,
             "wild": sorted(set(wild))},
            ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{name}: {dirs} -> {len(ids)} papers ({len(wild)} wild)")
    print(f"wrote meta_spec.md ({len(L)} lines)")
    return 0


def cmd_select(a) -> int:
    src = json.loads((a.work / "selection_input.json").read_text(encoding="utf-8"))
    papers = json.loads((a.work / "raw_papers.json").read_text(encoding="utf-8"))
    by_id = {p["base_id"]: p for p in papers}

    selection: dict[str, list] = {d: [] for d in DIRECTIONS}
    all_ids: list[str] = []
    for d in DIRECTIONS:
        rows = src["directions"].get(d, [])
        out = []
        for r in rows:
            pid = r["id"]
            if pid not in by_id:
                raise SystemExit(f"[FATAL] {pid} ({d}) not in scraped batch")
            rel, qual = int(r["relevance"]), int(r["quality"])
            out.append({
                "id": pid,
                "title": by_id[pid].get("title", ""),
                "relevance": rel,
                "quality": qual,
                "score": round(rel * 0.7 + qual * 0.3, 2),
                "wild": bool(r.get("wild")),
                "direction": d,
                "axis": DIR_AXIS[d],
            })
            all_ids.append(pid)
        out.sort(key=lambda r: (-r["score"], r["id"]))
        selection[d] = out

    dupes = {i for i in all_ids if all_ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"[FATAL] duplicate ids: {dupes}")

    # ---- allocation checks (skill v0.8.0 flexible allocation) --------------
    axis_count = {ax: sum(len(selection[d]) for d in AXIS_DIRS[ax]) for ax in AXES}
    day_total = sum(axis_count.values())
    if day_total > DAILY_TOTAL:
        raise SystemExit(f"[FATAL] day total {day_total} > {DAILY_TOTAL}")
    for ax, n in axis_count.items():
        if n > AXIS_CAP:
            raise SystemExit(f"[FATAL] axis {ax}: {n} papers > cap {AXIS_CAP}")
    over = sum(max(0, axis_count[ax] - AXIS_BASE[ax]) for ax in AXES)
    under = sum(max(0, AXIS_BASE[ax] - axis_count[ax]) for ax in AXES)
    if over > under:
        raise SystemExit(
            f"[FATAL] axis over-base {over} exceeds available under-base {under}: {axis_count}")
    for ax in AXES:
        dcount = {d: len(selection[d]) for d in AXIS_DIRS[ax]}
        dir_base_sum = sum(DIR_BASE[d] for d in AXIS_DIRS[ax])
        dir_over = sum(max(0, dcount[d] - DIR_BASE[d]) for d in AXIS_DIRS[ax])
        dir_under = sum(max(0, DIR_BASE[d] - dcount[d]) for d in AXIS_DIRS[ax])
        # a direction may exceed its base either by taking over slots a thin
        # sibling direction yielded, or by absorbing axis-level surplus
        axis_surplus = max(0, axis_count[ax] - dir_base_sum)
        allowed = max(dir_under, axis_surplus)
        if dir_over > allowed:
            raise SystemExit(
                f"[FATAL] axis {ax}: direction over-base {dir_over} exceeds "
                f"allowed {allowed}: {dcount}")
    for d in DIRECTIONS:
        nw = sum(1 for r in selection[d] if r["wild"])
        if nw > 2:
            raise SystemExit(f"[FATAL] direction {d}: {nw} wild-card > 2")

    (a.work / "selection.json").write_text(json.dumps(
        {"date": a.date, "listing_day": a.listing,
         "axes": AXES, "directions": DIRECTIONS,
         "axis_counts": axis_count, "day_total": day_total,
         "selection": selection},
        ensure_ascii=False, indent=1), encoding="utf-8")
    (a.work / "shortlist.json").write_text(
        json.dumps({d: [r["id"] for r in selection[d]] for d in DIRECTIONS},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    for d in DIRECTIONS:
        w = sum(1 for r in selection[d] if r["wild"])
        print(f"  {d:20s} {len(selection[d]):2d} papers, {w} wild-card  (base {DIR_BASE[d]})")
    for ax in AXES:
        print(f"  == {ax:16s} {axis_count[ax]:2d} papers (base {AXIS_BASE[ax]}, cap {AXIS_CAP})")
    print(f"day total: {day_total} / {DAILY_TOTAL}   unique ids: {len(set(all_ids))}")
    return 0


def cmd_checkmeta(a) -> int:
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    DIR_TASK = load_vocab(a.work)
    PID_DIR = {r["id"]: d for d in DIRECTIONS for r in sel["selection"][d]}
    meta: dict = {}
    errs: list[str] = []
    warns: list[str] = []
    for name in META_ASSIGN:
        p = a.work / f"{name}.py"
        if not p.exists():
            errs.append(f"[FATAL] missing {name}.py")
            continue
        ns: dict = {}
        try:
            exec(compile(p.read_text(encoding="utf-8"), str(p), "exec"), ns)
        except SyntaxError as e:
            errs.append(f"[FATAL] {name}.py syntax error: {e}")
            continue
        got = ns["META"]
        print(f"{name}.py -> {len(got)} entries")
        for pid, v in got.items():
            if pid in meta:
                errs.append(f"{pid} appears in two meta modules")
            meta[pid] = v

    for pid, dr in PID_DIR.items():
        if pid not in meta:
            errs.append(f"{pid} ({dr}) missing from meta")
            continue
        m = meta[pid]
        for k in ("arch", "task", "tags", "why", "find", "entry_desc"):
            if k not in m:
                errs.append(f"{pid} missing field '{k}'")
        if "find" in m:
            f = m["find"]
            if not isinstance(f, list) or len(f) != 3:
                errs.append(f"{pid} find must be a list of exactly 3")
            else:
                for pre, s in zip(("Finding: ", "Inference: ", "Recommendation: "), f):
                    if not isinstance(s, str) or not s.startswith(pre):
                        errs.append(f"{pid} find item must start with '{pre.strip()}: '")
                    elif len(s) < 15:
                        errs.append(f"{pid} find item too short")
        if "task" in m and m["task"] not in DIR_TASK[dr]:
            errs.append(f"{pid} task {m['task']!r} not in {dr} vocabulary")
        if "arch" in m and not re.fullmatch(r"[A-Za-z0-9_]+", str(m["arch"])):
            errs.append(f"{pid} arch must be [A-Za-z0-9_]+, got {m['arch']!r}")
        if "tags" in m:
            if not (3 <= len(m["tags"]) <= 5):
                errs.append(f"{pid} tags must be 3-5, got {len(m['tags'])}")
            for tg in m["tags"]:
                if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", str(tg)):
                    errs.append(f"{pid} tag {tg!r} not kebab-case")
        if "why" in m and len(m["why"]) < 30:
            errs.append(f"{pid} why too short")
        if "entry_desc" in m:
            d = m["entry_desc"]
            if "**" in d:
                errs.append(f"{pid} entry_desc contains '**'")
            if not (77 <= len(d) <= 165):
                warns.append(f"{pid} entry_desc length {len(d)} outside 77-165")
            if not re.search(r"[一-鿿]", d):
                errs.append(f"{pid} entry_desc not Chinese")
        if "proj" in m and m["proj"] and not str(m["proj"]).startswith("http"):
            errs.append(f"{pid} proj must be an http(s) URL")
    extra = set(meta) - set(PID_DIR)
    if extra:
        errs.append(f"meta contains ids not in selection: {sorted(extra)}")

    print(f"\nmeta entries: {len(meta)} / {len(PID_DIR)}")
    for d in DIRECTIONS:
        ids = [r["id"] for r in sel["selection"][d]]
        print(f"  {d:20s} {sum(1 for i in ids if i in meta)}/{len(ids)}")
    if warns:
        print(f"\nWARNINGS ({len(warns)}):")
        for w in warns:
            print("  -", w)
    if errs:
        print(f"\nERRORS ({len(errs)}):")
        for e in errs:
            print("  -", e)
        return 1
    print("\ncheckmeta: OK (0 errors)")
    return 0


def cmd_render(a) -> int:
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    src = json.loads((a.work / "selection_input.json").read_text(encoding="utf-8"))
    meta = load_meta(a.work)
    org_override = {}
    orgp = a.work / "orgs.json"
    if orgp.exists():
        org_override = json.loads(orgp.read_text(encoding="utf-8"))

    cards: dict = {}
    for p in (a.work / "phase2_cards").glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        cards[d["arxiv_id"]] = d

    repo = Path(a.repo)
    out_dir = repo / "daily_arxiv_digest" / a.date[:7].replace("-", "_") / a.date
    res = out_dir / "res"
    res.mkdir(parents=True, exist_ok=True)
    nfig = 0
    for d in DIRECTIONS:
        for row in sel["selection"][d]:
            for fg in cards[row["id"]].get("figures", []):
                s = a.work / fg["path"]
                if s.exists():
                    shutil.copy2(s, res / f"{row['id']}_{fg['name']}.png")
                    nfig += 1

    def orgs_of(pid: str) -> list[str]:
        if pid in org_override:
            return org_override[pid]
        o = [x for x in cards[pid].get("affiliation_block", []) if x and "@" not in x
             and not x.lower().startswith("correspondence")
             and not x.lower().startswith("corresponding") and len(x) > 2]
        return o[:4] or ["[unverified]"]

    wild_summary = src.get("wild_summary", {})
    wild_reason = src.get("wild_reasons", {})
    dir_summaries = src.get("direction_summaries", {})
    axis_notes = src.get("axis_notes", {})
    day_total = sel["day_total"]

    for ax in AXES:
        cn, tag, scope = AXIS_CN[ax]
        dirs = AXIS_DIRS[ax]
        rows_all = [r for d in dirs for r in sel["selection"][d]]
        wc = [r["id"] for r in rows_all if r["wild"]]
        L: list[str] = []
        L.append(f"# Mine Arxiv Daily Digest - {a.date} ({cn} Axis, {len(rows_all)} papers)")
        L.append("")
        L.append(f"**Generated**: {a.generated}")
        L.append("")
        L.append(f"**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG, cs.IR "
                 f"submissions, listing day {a.listing} (announced {a.announced})")
        L.append("")
        L.append(f"**Batch window**: {a.win_a} .. {a.win_b}（arXiv 公告批次横跨两个 UTC 日："
                 f"从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），"
                 f"到当日的同一时刻为止）")
        L.append("")
        L.append(f"**Axis**: {ax} ({len(rows_all)} papers, base {AXIS_BASE[ax]}, cap {AXIS_CAP})")
        L.append("")
        L.append("**Directions**: " + ", ".join(
            f"{d} ({len(sel['selection'][d])})" for d in dirs))
        L.append("")
        L.append(f"**Selection**: {len(rows_all)} papers ranked by relevance x quality, "
                 f"with {len(wc)} wild-card slot{'s' if len(wc) != 1 else ''}"
                 if rows_all else
                 "**Selection**: 0 papers（本批次该 axis 无够格论文，按规则不凑数）")
        L.append("")
        L.append(f"**Day total**: {day_total} papers across 4 axes (target {DAILY_TOTAL})")
        L.append("")
        L.append(f"**Scope**: {scope}")
        L.append("")
        if wc:
            parts = list(wild_summary.get(ax, []))
            L.append(f"⚠️ **Wild-card**: {parts[0] if parts else f'{len(wc)} 篇'}")
            L.append("")
            for para in parts[1:]:
                L.append(para)
                L.append("")
        elif rows_all:
            L.append("**Wild-card**: 0（本 axis 本批次够格供给充足，未启用补位名额）")
            L.append("")
        else:
            L.append("**Wild-card**: 0（本 axis 本批次供给断供，未启用任何补位名额）")
            L.append("")
        for para in axis_notes.get(ax, []):
            L.append(para)
            L.append("")
        L.append("---")
        L.append("")

        idx = 0
        for d in dirs:
            rows = sel["selection"][d]
            if not rows:
                continue
            L.append(f"## {DIR_CN[d]} · `{d}` ({len(rows)} papers)")
            L.append("")
            summ = dir_summaries.get(d)
            if summ:
                L.append(summ)
                L.append("")
            for row in rows:
                idx += 1
                pid = row["id"]
                c = cards[pid]
                m = meta[pid]
                orgs = orgs_of(pid)
                L.append(f"### {idx}. {c['title']}")
                L.append("")
                L.append(f"**arXiv**: [{pid}]({strip_ver(c['abs_url'])}) | **Score**: {row['score']:.1f} "
                         f"(relevance {row['relevance']} x 0.7 + quality {row['quality']} x 0.3) | "
                         f"**Direction**: `{d}` | "
                         f"**Tags**: {tag}, {', '.join(m['tags'])}, {short_org(orgs[0])} | "
                         f"**Categories**: {', '.join(c.get('categories', []))} | "
                         f"**Pages**: {c.get('pages', '?')}")
                L.append("")
                L.append(f"**Authors**: {'; '.join(x['name'] for x in c.get('authors', []))}")
                L.append("")
                L.append(f"**Affiliation**: {'; '.join(orgs)}")
                L.append("")
                L.append("**Abstract**")
                L.append("")
                L.append("> " + re.sub(r"\s+", " ", c.get("abstract", "")).strip())
                L.append("")
                L.append("**Key findings**")
                L.append("")
                for f in m["find"]:
                    kind, _, body = f.partition(": ")
                    L.append(f"- **{kind}**: {body}")
                L.append("")
                figs = c.get("figures", [])
                if figs:
                    L.append("**Key figures**")
                    L.append("")
                    for fg in figs:
                        kind = "Framework" if fg["name"] == "framework" else "Result"
                        L.append(f"*{kind} - {clean_caption(fg.get('caption', ''))}*")
                        L.append("")
                        L.append(f"![{c['title']} - {kind.lower()}](res/{pid}_{fg['name']}.png)")
                        L.append("")
                why = m["why"].strip()
                if row["wild"]:
                    why += "  [wild-card=yes] " + wild_reason.get(
                        pid, "本 direction 该批次供给不足，按相邻方向补位。")
                L.append(f"**Why this ranks #{idx}**: {why}")
                L.append("")
                L.append("---")
                L.append("")
        L.append("## Footer")
        L.append("")
        L.append(f"- Total papers reviewed across all 4 axes: {day_total}")
        L.append(f"- {ax} axis final count: {len(rows_all)}")
        L.append(f"- Wild-cards in this axis: {len(wc)}")
        L.append(f"- Figure assets: {a.date}/res/")
        L.append("")
        L.append(f"Generated by `mine-arxiv-daily-digest` skill. "
                 f"Sister file: `{a.date}_{ax}_entry.md`.")
        (out_dir / f"{a.date}_{ax}_report.md").write_text("\n".join(L) + "\n", encoding="utf-8")

        E: list[str] = []
        for d in dirs:
            rows = sel["selection"][d]
            if not rows:
                continue
            E.append(f"<!-- direction: {d} -->")
            E.append("")
            for row in rows:
                pid = row["id"]
                c = cards[pid]
                m = meta[pid]
                orgs = orgs_of(pid)
                ym = re.search(r"(\d{4})\.(\d{2})", pid).group(0)
                E.append(f"+ **{c['title']}**")
                E.append(f"[![paper](https://img.shields.io/badge/Arxiv_{ym}-blue)]({strip_ver(c['abs_url'])})")
                E.append(f"![architecture](https://img.shields.io/badge/{badge(m['arch'])}-red)")
                E.append(f"![task](https://img.shields.io/badge/{badge(m['task'])}-magenta)")
                E.append(f"![organization](https://img.shields.io/badge/{badge(orgs[0])}-green)")
                if m.get("proj"):
                    E.append(f"[![project](https://img.shields.io/badge/project-blue)]({m['proj']})")
                E.append(f"[![note](https://img.shields.io/badge/note-mediumorchid)]() "
                         f'<p style="font-size: 14px;">**{m["entry_desc"]}**</p>')
                E.append("")
        if not rows_all:
            E.insert(0, f"<!-- axis: {ax} · 本批次 0 篇（供给断供，未做补位）-->")
            E.insert(1, "")
            E.insert(2, f"**{cn}**：本批次无够格论文，按「薄方向让出名额而不是被填充」的口径发 0 篇。")
            E.insert(3, "")
            for para in axis_notes.get(ax, []):
                E.append(para)
                E.append("")
        (out_dir / f"{a.date}_{ax}_entry.md").write_text("\n".join(E) + "\n", encoding="utf-8")

    print("wrote", len(AXES) * 2, "files ->", out_dir)
    print("figures copied:", nfig)
    for ax in AXES:
        rows_all = [r for d in AXIS_DIRS[ax] for r in sel["selection"][d]]
        print(f"  {ax}: {len(rows_all)} papers, "
              f"{sum(1 for r in rows_all if r['wild'])} wild-card")
    return 0


def cmd_verify(a) -> int:
    repo = Path(a.repo)
    out_dir = repo / "daily_arxiv_digest" / a.date[:7].replace("-", "_") / a.date
    res = out_dir / "res"
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    DIR_TASK = load_vocab(a.work)
    errs, warns = [], []

    all_ids = [r["id"] for d in DIRECTIONS for r in sel["selection"][d]]
    if not all_ids:
        errs.append("selection is empty")
    if len(set(all_ids)) != len(all_ids):
        errs.append(f"duplicate ids: {[i for i in set(all_ids) if all_ids.count(i) > 1]}")
    if sel["day_total"] > DAILY_TOTAL:
        errs.append(f"day total {sel['day_total']} > {DAILY_TOTAL}")
    for ax, n in sel["axis_counts"].items():
        if n > AXIS_CAP:
            errs.append(f"axis {ax}: {n} > cap {AXIS_CAP}")

    if not out_dir.exists():
        print(f"[FATAL] output dir missing: {out_dir}")
        return 2
    for ax in AXES:
        for kind in ("report", "entry"):
            if not (out_dir / f"{a.date}_{ax}_{kind}.md").exists():
                errs.append(f"missing {a.date}_{ax}_{kind}.md")

    for ax in AXES:
        rp, ep = out_dir / f"{a.date}_{ax}_report.md", out_dir / f"{a.date}_{ax}_entry.md"
        if not (rp.exists() and ep.exists()):
            continue
        rtxt, etxt = rp.read_text(encoding="utf-8"), ep.read_text(encoding="utf-8")
        rows_all = [r for d in AXIS_DIRS[ax] for r in sel["selection"][d]]
        n = len(rows_all)
        wild = [r["id"] for r in rows_all if r["wild"]]

        heads = re.findall(r"^### (\d+)\. ", rtxt, re.M)
        if len(heads) != n or [int(h) for h in heads] != list(range(1, n + 1)):
            errs.append(f"{ax} report: bad '### N.' headings {heads}")
        for d in AXIS_DIRS[ax]:
            k = len(sel["selection"][d])
            if k and f"({k} papers)" not in rtxt:
                errs.append(f"{ax} report: direction {d} count {k} not declared")
        for block in ("**arXiv**:", "**Authors**:", "**Affiliation**:", "**Abstract**",
                      "**Key findings**", "**Why this ranks #"):
            if rtxt.count(block) != n:
                errs.append(f"{ax} report: block {block} count {rtxt.count(block)} != {n}")
        for b in rtxt.split("\n### ")[1:]:
            head = b.split("\n", 1)[0][:60]
            if ("**Key figures**" in b) != ("![" in b and "res/" in b):
                errs.append(f"{ax} report: figure block/image mismatch in '{head}'")
        for lbl in ("Finding", "Inference", "Recommendation"):
            if rtxt.count(f"- **{lbl}**:") != n:
                errs.append(f"{ax} report: {lbl} count != {n}")
        rscores = [float(x) for x in re.findall(r"\*\*Score\*\*: ([0-9.]+)", rtxt)]
        if len(rscores) != n:
            errs.append(f"{ax} report: {len(rscores)} score lines != {n}")
        # v0.8.0: axis 是报告单元，direction 是排名单元 —— 分数在 direction 内降序即可
        for d in AXIS_DIRS[ax]:
            k = len(sel["selection"][d])
            if not k:
                continue
            dscores = [float(x) for x in re.findall(
                r"\*\*Score\*\*: ([0-9.]+)",
                dir_section(rtxt, d))]
            if len(dscores) != k:
                errs.append(f"{ax}/{d}: {len(dscores)} score lines != {k}")
            elif dscores != sorted(dscores, reverse=True):
                errs.append(f"{ax}/{d}: scores not descending {dscores}")
        rep_ids = re.findall(r"\[(\d{4}\.\d{4,5})\]\(https://arxiv\.org/abs/", rtxt)
        if rep_ids != [r["id"] for r in rows_all]:
            errs.append(f"{ax} report: arxiv id order mismatch")
        ent = [u.rsplit("/", 1)[-1] for u in re.findall(
            r"\[!\[paper\]\(https://img\.shields\.io/badge/Arxiv_\d{4}\.\d{2}-blue\)\]"
            r"\((https://arxiv\.org/abs/[0-9.]+)\)", etxt)]
        if ent != [r["id"] for r in rows_all]:
            errs.append(f"{ax} entry: arxiv id order mismatch")
        if etxt.count("+ **") != n:
            errs.append(f"{ax} entry: {etxt.count('+ **')} title lines != {n}")
        for lbl in ("architecture", "task", "organization"):
            if etxt.count(f"![{lbl}]") != n:
                errs.append(f"{ax} entry: {lbl} badge count != {n}")
        # task badge must come from its own direction vocabulary
        ent_ids = ent
        for tb, pid in zip(re.findall(
                r"!\[task\]\(https://img\.shields\.io/badge/([^)]+?)-magenta\)", etxt), ent_ids):
            dr = next(r["direction"] for r in rows_all if r["id"] == pid)
            if tb not in DIR_TASK[dr]:
                errs.append(f"{ax} entry: task badge {tb!r} not in {dr} vocabulary")
        for ob in re.findall(r"!\[organization\]\(https://img\.shields\.io/badge/([^)]*)-green\)", etxt):
            if not ob.strip():
                errs.append(f"{ax} entry: empty organization badge")
        for desc in re.findall(r'<p style="font-size: 14px;">\*\*(.+?)\*\*</p>', etxt, re.S):
            if "**" in desc:
                errs.append(f"{ax} entry: nested ** in desc")
            if not (77 <= len(desc) <= 165):
                warns.append(f"{ax} entry_desc length {len(desc)}")
        for aff in re.findall(r"\*\*Affiliation\*\*: (.+)", rtxt):
            if not aff.strip() or aff.strip() == "[unverified]":
                warns.append(f"{ax} affiliation unverified: {aff[:50]}")
        nmark = rtxt.count("[wild-card=yes]")
        if len(wild) and nmark != len(wild):
            errs.append(f"{ax} report: {nmark} wild-card markers != {len(wild)}")
        if not wild and nmark:
            errs.append(f"{ax} report: {nmark} wild-card markers but none declared")
        if wild and "Wild-card" not in rtxt:
            errs.append(f"{ax} report: wild-card without declaration")
        if re.search(r"wild[-_ ]?card", etxt, re.I):
            errs.append(f"{ax} entry: contains 'wild-card' marker (must not)")
        for tok in ("TODO", "FIXME", "XXX", "TBD", "PLACEHOLDER"):
            if tok in rtxt or tok in etxt:
                errs.append(f"{ax}: placeholder {tok} found")

    referenced = set()
    for ax in AXES:
        rp = out_dir / f"{a.date}_{ax}_report.md"
        if rp.exists():
            for m in re.findall(r"!\[.*?\]\((res/[^)]+)\)", rp.read_text(encoding="utf-8")):
                referenced.add(m.replace("res/", "").replace("/", "\\"))
    for f in sorted(res.glob("*.png")):
        if f.name not in referenced:
            errs.append(f"orphan figure: {f.name}")
    for m in sorted(referenced):
        if not (res / m).exists():
            errs.append(f"missing figure: {m}")

    idx = (repo / "index.md").read_text(encoding="utf-8")
    if f"## {a.date}" not in idx:
        errs.append(f"index.md missing {a.date} section")
    toc = re.findall(r"^\| \[(\d{4}-\d{2}-\d{2})\]\(daily_arxiv_digest/(\d{4}_\d{2})/(\d{4}-\d{2}-\d{2})",
                     idx, re.M)
    toc_dates = [r[0] for r in toc]
    if toc_dates != sorted(toc_dates, reverse=True):
        errs.append("index.md toc not strictly descending")
    for d, ym, dd in toc:
        if d != dd or d[:7].replace("-", "_") != ym:
            errs.append(f"index.md toc row mismatch: {d} {ym} {dd}")
    secs = re.findall(r"^## (\d{4}-\d{2}-\d{2})", idx, re.M)
    if len(toc) != len(secs):
        errs.append(f"index.md toc rows {len(toc)} != sections {len(secs)}")
    if secs != sorted(secs, reverse=True):
        errs.append("index.md sections not strictly descending")
    if len(secs) != len(set(secs)):
        errs.append("index.md has duplicate sections")

    print(f"selection: {len(all_ids)} papers, {len(set(all_ids))} unique, "
          f"day total {sel['day_total']}/{DAILY_TOTAL}")
    print(f"axis counts: {sel['axis_counts']}")
    print(f"figures: {len(list(res.glob('*.png')))} png, {len(referenced)} referenced")
    print(f"index.md: {len(toc_dates)} toc rows, {len(secs)} sections")
    if warns:
        print(f"\nWARNINGS ({len(warns)}):")
        for w in warns:
            print("  -", w)
    if errs:
        print(f"\nERRORS ({len(errs)}):")
        for e in errs:
            print("  -", e)
        return 1
    print("\nverify: OK (0 errors)")
    return 0


def cmd_index(a) -> int:
    repo = Path(a.repo)
    idx = repo / "index.md"
    blob = (a.work / "index_section.md").read_text(encoding="utf-8")
    if "<!--SPLIT-->" not in blob:
        raise SystemExit("[FATAL] index_section.md must contain a <!--SPLIT--> marker")
    toc_row, section = blob.split("<!--SPLIT-->", 1)
    toc_row = toc_row.strip()
    section = section.strip("\n")

    text = idx.read_text(encoding="utf-8")
    if f"## {a.date}" in text:
        print(f"[SKIP] {a.date} already present")
        return 0

    rows = re.findall(r"^\| \[(\d{4}-\d{2}-\d{2})\]\(daily_arxiv_digest/", text, re.M)
    if not rows:
        raise SystemExit("[FATAL] no toc rows found in index.md")
    newest = rows[0]
    anchor_row = f"| [{newest}](daily_arxiv_digest/"
    pos = text.index(anchor_row)
    text = text[:pos] + toc_row + "\n" + text[pos:]

    secs = re.findall(r"^## (\d{4}-\d{2}-\d{2})", text, re.M)
    if not secs:
        raise SystemExit("[FATAL] no detail sections found in index.md")
    anchor_sec = f"\n## {secs[0]}\n"
    pos = text.index(anchor_sec)
    text = text[:pos] + "\n" + section + "\n" + text[pos:]

    idx.write_text(text, encoding="utf-8")
    toc_dates = re.findall(r"^\| \[(\d{4}-\d{2}-\d{2})\]\(daily_arxiv_digest/", text, re.M)
    secs2 = re.findall(r"^## (\d{4}-\d{2}-\d{2})", text, re.M)
    assert toc_dates == sorted(toc_dates, reverse=True), f"toc not descending: {toc_dates}"
    assert secs2 == sorted(secs2, reverse=True), f"sections not descending: {secs2}"
    assert len(toc_dates) == len(secs2), f"toc {len(toc_dates)} != sections {len(secs2)}"
    assert len(secs2) == len(set(secs2)), "duplicate sections"
    print("index.md updated")
    print(f"toc rows: {len(toc_dates)}, sections: {len(secs2)}, both strictly descending")
    return 0


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--work", required=True, help="working dir, e.g. codex_temp/2026-11-09")
        p.add_argument("--repo", default=r"X:\learning\daily-arxiv-paper")
        p.add_argument("--date", default=None)
        p.add_argument("--listing", default=None)
        p.add_argument("--generated", default=None)
        p.add_argument("--announced", default=None)
        p.add_argument("--win-a", dest="win_a", default=None)
        p.add_argument("--win-b", dest="win_b", default=None)

    for name, fn in (("pool", cmd_pool), ("vocab", cmd_vocab), ("select", cmd_select),
                     ("checkmeta", cmd_checkmeta), ("render", cmd_render),
                     ("verify", cmd_verify), ("index", cmd_index)):
        p = sub.add_parser(name)
        common(p)
        p.set_defaults(func=fn)
    p = sub.add_parser("spec")
    common(p)
    p.set_defaults(func=cmd_spec)

    a = ap.parse_args()
    a.work = Path(a.work)
    if a.work.is_absolute() is False:
        a.work = (Path(a.repo) / a.work).resolve()
    if a.generated is None and a.date:
        a.generated = f"{a.date} 17:30 CST"
    if a.announced is None and a.date:
        a.announced = f"{a.date} 00:00 UTC"
    return a.func(a)


if __name__ == "__main__":
    raise SystemExit(main())
