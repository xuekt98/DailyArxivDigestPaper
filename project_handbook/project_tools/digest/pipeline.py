#!/usr/bin/env python3
"""Daily digest pipeline for the daily-arxiv-paper project.

Reusable, date-parameterised machinery around scrape.py / read.py. Everything
mechanical lives here so a daily run only has to author two inputs:

  <work>/selection_input.json   -- the 70 picked papers (id / relevance /
                                   quality / wild) + wild-card reasons
  <work>/index_section.md        -- the index.md toc row + detail section

Subcommands:
  pool      build wide keyword candidate pools for the 7 tracks
  vocab     write per-track task badge vocabularies
  spec      write meta_spec.md + assign_meta_{a..d}.json for the meta workers
  select    validate the authored selection and emit selection.json/shortlist.json
  checkmeta validate the 4 meta modules against the meta contract
  render    write 14 md files + res/ figures
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

TRACKS = ["aigc_visual", "aigc_audio", "audio_lm", "embodied",
          "rl_core", "rl_llm", "rl_aigc"]

TRACK_CN = {
    "aigc_visual": ("AIGC 视觉生成", "AIGC-visual",
                    "图像 / 视频 / 3D / 4D 内容的生成与编辑，含扩散与流匹配模型的训练方法、加速与评测基准"),
    "aigc_audio": ("AIGC 音频生成", "AIGC-audio",
                   "音频 / 语音 / 音乐的生成、合成、编辑与生产工具链，含 TTS、语音水印攻防与神经音频编解码"),
    "audio_lm": ("音频与语音语言模型", "audio-lm",
                 "音频 / 语音语言模型与多模态助手，含语音记忆、长音频检索、空间音频与多语种对话评测"),
    "embodied": ("具身智能与世界模型", "embodied",
                 "具身智能与世界模型，含移动操作、人形控制、触觉反射、VLA 策略与世界动作模型"),
    "rl_core": ("核心强化学习", "rl-core",
                "RL 算法与理论、多智能体 RL、sim-to-real 与离线 / 元 RL"),
    "rl_llm": ("LLM 后训练 RL", "rl-llm",
               "LLM 后训练的 RL：RLHF / DPO / GRPO / RLAIF / RLVR / on-policy 蒸馏与 RLVR 调度"),
    "rl_aigc": ("生成式内容模型的 RL", "rl-aigc",
                "生成式内容模型的 RL：扩散 / 流匹配 RL、生成式奖励模型与推理期采样扩展"),
}

# ---------------------------------------------------------------------------
# task badge vocabularies (skill assets/entry.template.md base + tracked extras)
# ---------------------------------------------------------------------------
VOCAB_BASE = {
    "aigc_visual": [
        "Image_Generation", "Video_Generation", "3D_Generation", "4D_Generation",
        "Image_Editing", "Video_Editing", "3D_Editing",
        "Multi_Subject_Personalization", "Layout_to_Image",
        "Controllable_Generation", "Inpainting", "Style_Transfer",
    ],
    "aigc_audio": [
        "Audio_Generation", "Music_Generation", "TTS", "Voice_Cloning",
        "Audio_Editing", "Voice_Conversion", "Sound_Synthesis",
        "Audio_Super_Resolution", "Text_to_Audio",
    ],
    "audio_lm": [
        "Audio_Understanding", "Audio_Captioning", "Audio_QA",
        "Audio_Reasoning", "Audio_LM", "Speech_LM",
        "Full_Duplex", "Voice_Assistant", "Speech_to_Speech",
        "Real_Time_Speech", "Spoken_Dialogue", "Streaming_ASR",
    ],
    "embodied": [
        "Embodied_Agent", "Visual_Navigation", "Manipulation",
        "Sim_to_Real", "Robot_Learning", "VLA_Model",
        "World_Model", "Model_Based_RL", "Video_as_World_Model",
        "Neural_Simulator", "Visual_Exploration", "Tactile_Sensing",
    ],
    "rl_core": [
        "Policy_Gradient", "PPO", "SAC", "DQN", "A2C", "TRPO",
        "Offline_RL", "Model_Free_RL", "Exploration",
        "Multi_Agent_RL", "MARL", "QMIX", "MAPPO",
        "Hierarchical_RL", "Meta_RL", "Imitation_Learning",
        "Inverse_RL", "Sim_to_Real_RL", "RL_Theory",
    ],
    "rl_llm": [
        "RLHF", "PPO_RLHF", "RLAIF",
        "DPO", "IPO", "KTO", "ORPO",
        "GRPO", "RLVR", "Reward_Modeling",
        "Constitutional_AI", "LLM_Alignment", "Preference_Optimization",
    ],
    "rl_aigc": [
        "RL_for_Diffusion", "RL_for_Flow_Matching",
        "DPO_Diffusion", "Diffusion_DPO", "Preference_Alignment",
        "Reward_Weighted_Regression", "RWR",
        "Best_of_N", "BoN", "Rejection_Sampling",
        "Classifier_Guidance", "CFG_Distillation", "Reward_Model_Image",
        "GenEval", "DrawBench", "HPSv2", "Aesthetic_Scoring",
    ],
}

VOCAB_EXTRA = {
    "aigc_visual": [
        "Diffusion_Acceleration", "KV_Cache_Compression", "Autoregressive_Generation",
        "Few_Step_Generation", "Identity_Preservation", "Scene_Reconstruction",
        "Video_Acceleration", "Tokenizer_Compression", "World_Evolution",
    ],
    "aigc_audio": [
        "Video_to_Audio", "Speech_Deepfake_Detection", "Voice_Identity",
        "Acoustic_Measurement", "Acoustic_Communication", "Audio_Visual_Segmentation",
        "Audio_Representation_Learning", "Sound_Source_Localization", "Speech_Forensics",
        "TTS_Control", "Cross_Codec_Robustness",
    ],
    "audio_lm": [
        "Omni_Understanding", "Simultaneous_Speech_Translation", "Target_Speech_Extraction",
        "Speech_Summarization", "Phonological_Knowledge", "ASR_Error_Repair",
        "Low_Resource_ASR", "Conversation_Evaluation", "Streaming_Dialogue",
        "Emotion_Recognition",
    ],
    "embodied": [
        "Humanoid_Control", "Motion_Priors", "Latent_Action", "Closed_Loop_Evaluation",
        "Whole_Body_Control", "Mobile_Manipulation", "Memory_Benchmark",
        "Force_Control", "World_Action_Model", "Policy_Diffusion",
        "Self_Improvement", "Loco_Manipulation",
    ],
    "rl_core": [
        "TD_Learning", "Digital_Twin", "Inverse_Kinematics", "Human_Feedback_RL",
        "Multi_Objective_RL", "Vision_Language_Control", "Policy_Regularization",
        "Eligibility_Traces", "Reward_Shaping", "Experience_Replay",
        "Safe_RL", "Curriculum_Learning",
    ],
    "rl_llm": [
        "On_Policy_Distillation", "Process_Reward", "Rubric_Reward", "Reward_Budgeting",
        "Multi_Turn_RL", "Token_Level_Credit", "Data_Selection", "Alignment_Tax",
        "Conformal_Policy_Optimization", "Test_Time_Compute", "Self_Distillation",
        "Reward_Model_Quality", "Preference_Learning",
    ],
    "rl_aigc": [
        "RL_for_Video", "On_Policy_Distillation", "Few_Step_Distillation",
        "Source_Attribution", "T2I_Evaluation", "Reward_Calibration",
        "Image_Generation_RL", "Speech_Generation_RL", "Adversarial_Distillation",
        "Image_Provenance", "Reward_Search",
    ],
}

# ---------------------------------------------------------------------------
# wide candidate-pool sweep (supplementary to scrape.py's own taxonomy)
# ---------------------------------------------------------------------------
POOL_EXTRA = {
    "aigc_visual": r"""
        \bgenerat\w+ (image|video|scene|3d|view|avatar|character|mesh|point cloud)\b
        |\bimage-to-video\b|\bvideo-to-video\b|\btext2image\b|\btext2video\b|\bt2i\b|\bt2v\b
        |\bautoregressive (image|video)\b|\bdiffusion\b|\bflow matching\b|\bdiffusion policy\b
        |\bgaussian splatting\b|\b3dgs\b|\bnerf\b|\bnovel view\b|\bview synthesis\b
        |\bimage editing\b|\bvideo editing\b|\bediting (task|method|framework)\b
        |\bcontent (creation|generation)\b|\bvisual generation\b|\bvisual (tokenizer|autoencoder)\b
        |\bmulti-view\b|\bvideo diffusion\b|\bworld action model\b|\bwam\b
        |\bpersonaliz\w+ (image|video|subject)\b|\bsubject-driven\b
        |\bicon generation\b|\bposter\b|\bfont generation\b|\btext rendering\b|\btext-rendering\b
        |\bgeneration benchmark\b|\bsynthetic data\b
    """,
    "aigc_audio": r"""
        \btts\b|\btext-to-speech\b|\bspeech synthesis\b|\bspeech generation\b|\bvoice (cloning|conversion|design)\b
        |\baudio (generation|synthesis|editing|codec|diffusion|watermark)\b|\bmusic (generation|synthesis|editing)\b
        |\bsound generation\b|\bsound (design|synthesis)\b|\bvocoder\b|\bsinging\b|\bmelody\b|\blyric\b
        |\bspeech enhancement\b|\bspeech separation\b|\bsource separation\b|\bdeepfake\b|\bwatermark\b
        |\btranscription\b|\bspeech recognition\b|\basr\b|\bprosod\w+|\bspeech emotion\b
        |\baudio caption\w+|\bsound event\b|\bparalinguistic\b|\bacoustic (model|scene)\b
        |\bvideo-to-audio\b|\btext-to-audio\b|\baudio representation\b|\bself-supervised audio\b
        |\baudio question\b|\baudio reasoning\b|\baudio understanding\b|\bspeech understanding\b
    """,
    "audio_lm": r"""
        \baudio (llm|language model|foundation model)\b|\bspeech (llm|language model)\b|\blalm\b
        |\bomni(modal)?\b|\bomni-?model\b|\bmultimodal (llm|assistant)\b|\bvisual llm\b
        |\bvoice (agent|assistant)\b|\bvoice interaction\b|\bconversational (ai|system|agent)\b
        |\bduplex\b|\bturn-taking\b|\bbarge-in\b|\bfull-duplex\b|\bhalf-duplex\b
        |\bspeech-to-speech\b|\bs2s\b|\bspoken dialogue\b|\bspoken language\b
        |\baudio (understanding|question|reasoning|qa|caption\w*|retrieval|memory|agent)\b
        |\bspeech (understanding|instruction|recognition|translation|emotion)\b|\basr\b|\bwhisper\b
        |\bstreaming (speech|audio)\b|\breal-time speech\b|\blow-latency speech\b|\binterruptible\b
        |\bmulti-turn\b.*\b(speech|audio|voice)\b|\b(speech|audio|voice).*\bmulti-turn\b
        |\blistening\b|\bhearing\b|\bauditory\b|\bspeech dataset\b|\baudio dataset\b|\bbenchmark.*\b(speech|audio)\b
    """,
    "embodied": r"""
        \bembodied\b|\brobot\w*\b|\bhumanoid\b|\bmanipulat\w+\b|\bgrasp\w*\b|\bdexterous\b
        |\bvla\b|\bvision-language-action\b|\bworld model\b|\bjepa\b|\bnavigation\b
        |\blocomo(tion|otion)\b|\bwhole-body\b|\bmanipulator\b|\brobot arm\b|\bquadruped\b|\bdrone\b|\buav\b
        |\btactile\b|\bvisuotactile\b|\bpropriocept\w+\b|\bforce (feedback|control)\b
        |\bsim-to-real\b|\bsim2real\b|\bdomain randomization\b|\bembodied (ai|agent|question|reasoning)\b
        |\bhousehold\b|\bscene (understanding|reconstruction)\b|\b3d (reconstruction|scene)\b
        |\bpolicy (learning|optimization|distillation)\b|\bdiffusion polic\w+\b|\baction chunk\w*\b
        |\bplanning\b|\btrajectory (prediction|optimization)\b|\bteleoperat\w+\b|\breward model\w*.*\brobot
    """,
    "rl_core": r"""
        \breinforcement learning\b|\bpolicy gradient\b|\bactor-critic\b|\bactor critic\b|\bppo\b|\bsac\b|\btd3\b|\bddpg\b
        |\bdqn\b|\bbandit\w*\b|\bmulti-agent reinforcement\b|\bmarl\b|\bqmix\b|\bmaddpg\b|\bmappo\b
        |\boffline rl\b|\bonline rl\b|\bmodel-based rl\b|\bmodel-free rl\b|\bmeta-rl\b|\bcontinual rl\b
        |\bvalue function\b|\badvantage\b|\bpolicy optimization\b|\bexploration\b|\bintrinsic motivation\b
        |\bself-play\b|\bzero-sum\b|\bmatrix game\b|\bgame-theoretic\b|\bsubgoal\b|\bhierarchical rl\b
        |\binverse reinforcement\b|\bimitation learning\b|\bbehavior cloning\b|\bgail\b|\bcredit assignment\b
        |\bcontrol barrier\b|\bmodel predictive control\b|\bsafe rl\b|\bconstrained rl\b|\bcurriculum\b
        \breward (shaping|design|model\w*)\b|\bstate value\b|\btemporal difference\b|\bq-function\b
        |\bmeta-reinforcement\b|\btask distribution\b|\bcontinual learning\b.*\brl\b
    """,
    "rl_llm": r"""
        \brlhf\b|\bdlpo\b|\bdpo\b|\bgrpo\b|\brlaif\b|\brlvr\b|\bverifiable reward\w*\b
        |\bpreference optimiz\w+\b|\bpolicy optimization\b.*\b(llm|language model)\b
        |\breinforcement learning\b.*\b(llm|language model|reasoning)\b|\bpost-training\b
        |\bon-policy (self-)?distillation\b|\bprocess reward model\b|\bprm\b|\bverifier\b
        |\breinforcement learning with verifiable\b|\bgrpo-style\b|\breward model\w*\b.*\bllm\b
        |\bagentic reinforcement learning\b|\bmulti-turn reinforcement learning\b
        |\btest-time (compute|scaling|search)\b.*\b(llm|reasoning)\b|\bself-rewarding\b
        \breasoning (model|policy)\b.*\breinforcement\b|\bdynamic rubric\w*\b|\brubric\b
        \balignment\b.*\breinforcement\b|\banswer-level reward\b|\boutcome reward\b
        \bchat model\b.*\brl\b|\bllm agent\b.*\brl\b
    """,
    "rl_aigc": r"""
        \breinforcement learning\b.*\b(diffusion|flow matching|image gener|video gener|generation model)\b
        |\b(diffusion|flow matching|image gener\w+|video gener\w+)\b.*\breinforcement learning\b
        \bgrpo\b.*\b(diffusion|image|video)\b|\b(diffusion|image|video)\b.*\bgrpo\b
        \breward model\w*\b.*\b(image|video|diffusion|generat)\b|\bgenerative reward model\b
        \btest-time scaling\b.*\b(diffusion|image|video|generation)\b|\bbest-of-n\b
        \breinforcement learning\b.*\btts\b|\btts\b.*\breinforcement learning\b
        \bfeedback[- ]driven\b.*\b(generation|diffusion)\b|\bhuman feedback\b.*\b(video|image|diffusion)\b
        \bdiffusion[- ]policy\b|\breinforcement fine-tuning\b.*\b(video|image)\b
        \bpreference alignment\b.*\b(video|image|diffusion)\b|\bdpo\b.*\b(diffusion|image|video)\b
        \brl\b.*\bprompt (engineering|enhancement|optimization)\b.*\bgenerat\w+\b
    """,
}

META_ASSIGN = {
    "meta_a": ["aigc_visual", "aigc_audio"],
    "meta_b": ["audio_lm", "embodied"],
    "meta_c": ["rl_core", "rl_llm"],
    "meta_d": ["rl_aigc"],
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

    pools = {t: [] for t in TRACKS}
    for p in papers:
        hay = f"{p.get('title','')}\n{p.get('abstract','')}"
        hit = {t: False for t in TRACKS}
        for src, rx in base.items():
            for pat, _w in rx:
                if pat.search(hay):
                    hit["rl_core" if src == "rl" else src] = True
        for t in TRACKS:
            if extra[t].search(hay):
                hit[t] = True
        for t in TRACKS:
            if hit[t]:
                pools[t].append(p)

    out = []
    for t in TRACKS:
        out.append(f"===== {t}: {len(pools[t])} =====")
        for p in sorted(pools[t], key=lambda x: x["base_id"]):
            out.append(f"  {p['base_id']}  {p.get('title','')[:110]}")
    (a.work / "pools.txt").write_text("\n".join(out), encoding="utf-8")
    (a.work / "pool.json").write_text(
        json.dumps({t: [p["base_id"] for p in pools[t]] for t in TRACKS},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    for t in TRACKS:
        print(f"{t}: {len(pools[t])}")
    return 0


def cmd_vocab(a) -> int:
    out = []
    for t in TRACKS:
        seen, uniq = set(), []
        for x in VOCAB_BASE[t] + VOCAB_EXTRA[t]:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        out.append(f"=== {t} ({len(uniq)}) ===")
        out += [f"  - {x}" for x in uniq]
        out.append("")
    (a.work / "task_vocab.txt").write_text("\n".join(out), encoding="utf-8")
    for t in TRACKS:
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
    A("你负责其中一部分论文的**手写分析元数据**。产物是一个 Python 模块文件 `meta_<x>.py`，")
    A("定义一个顶层字典 `META`，把 arxiv id 映射到分析字段。")
    A("")
    A("## 输出文件格式（严格遵守）")
    A("")
    A("```python")
    A("# meta_a.py")
    A('META = {')
    A('    "2611.xxxxx": {')
    A('        "arch": "Snake_Case_Architecture_Name",')
    A('        "task": "Task_Tag_From_This_Track_Vocab",')
    A('        "tags": ["kebab-case-tag", "kebab-case-tag", "kebab-case-tag"],')
    A('        "why": "为什么它进本线前 10 —— 中文，>= 30 字符，给出可核对的具体数字或方法要点。",')
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
    A("| `task` | **必须**取自下面「本线 task 词表」，不得跨线取词 |")
    A("| `tags` | 3-5 个，kebab-case（小写字母、数字、`-`），只允许 `[a-z0-9][a-z0-9-]*` |")
    A("| `why` | 中文，>= 30 字符，说明「为什么排这个位置」，要有具体数字 |")
    A("| `find` | 长度恰好 3 的**字符串列表**，每项以 `Finding: ` / `Inference: ` / `Recommendation: ` 开头（半角冒号 + 一个空格），每项 >= 15 字符 |")
    A("| `entry_desc` | 中文，77-165 字符（不是字节），不得包含 `**`，不得嵌套粗体 |")
    A("| `proj` | 可选，项目主页 URL（必须以 http 开头）；论文没有就**不要写这个 key** |")
    A("")
    A("## 硬性约束")
    A("")
    A("- 只写你被分配的那几篇，不要写别的论文，也不要改动其他文件。")
    A("- 每篇论文只出现在一条研究线里，模块之间不要重复 id。")
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
    A("## 本线 task 词表（`task` 只能从这里取）")
    A("")
    for t in TRACKS:
        A(f"### {t}  ({len(vocab[t])})")
        A("")
        A("```")
        A("\n".join(vocab[t]))
        A("```")
        A("")
    A("## 逐篇建议 task")
    A("")
    A("下面是按分数排序的分配建议。**可以**在同线词表内调整，但必须留在本线词表里。")
    A("")
    for t in TRACKS:
        A(f"### {t}")
        A("")
        for r in sel["selection"][t]:
            wc = "  **[wild-card]**" if r["wild"] else ""
            A(f"- `{r['id']}` (score {r['score']}) — {r['title'][:96]}{wc}")
        A("")
    (a.work / "meta_spec.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    for name, tracks in META_ASSIGN.items():
        ids = [r["id"] for t in tracks for r in sel["selection"][t]]
        wild = sorted({r["id"] for t in tracks for r in sel["selection"][t] if r["wild"]})
        (a.work / f"assign_{name}.json").write_text(json.dumps(
            {"module": name, "tracks": tracks, "ids": ids, "wild": wild},
            ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{name}: {tracks} -> {len(ids)} papers ({len(wild)} wild)")
    print(f"wrote meta_spec.md ({len(L)} lines)")
    return 0


def cmd_select(a) -> int:
    src = json.loads((a.work / "selection_input.json").read_text(encoding="utf-8"))
    papers = json.loads((a.work / "raw_papers.json").read_text(encoding="utf-8"))
    by_id = {p["base_id"]: p for p in papers}

    selection, shortlist, all_ids = {}, {}, []
    for t in TRACKS:
        rows = src["tracks"][t]
        out = []
        for r in rows:
            pid = r["id"]
            if pid not in by_id:
                raise SystemExit(f"[FATAL] {pid} ({t}) not in scraped batch")
            rel, qual = int(r["relevance"]), int(r["quality"])
            out.append({
                "id": pid,
                "title": by_id[pid].get("title", ""),
                "relevance": rel,
                "quality": qual,
                "score": round(rel * 0.7 + qual * 0.3, 2),
                "wild": bool(r.get("wild")),
            })
            all_ids.append(pid)
        out.sort(key=lambda r: (-r["score"], r["id"]))
        selection[t] = out
        shortlist[t] = [r["id"] for r in out]

    if len(all_ids) != 70:
        raise SystemExit(f"[FATAL] {len(all_ids)} papers != 70")
    dupes = {i for i in all_ids if all_ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"[FATAL] duplicate ids: {dupes}")

    (a.work / "selection.json").write_text(json.dumps(
        {"date": a.date, "listing_day": a.listing,
         "tracks": TRACKS, "selection": selection},
        ensure_ascii=False, indent=1), encoding="utf-8")
    (a.work / "shortlist.json").write_text(
        json.dumps(shortlist, ensure_ascii=False, indent=1), encoding="utf-8")
    for t in TRACKS:
        w = sum(1 for r in selection[t] if r["wild"])
        print(f"{t}: {len(selection[t])} papers, {w} wild-card")
    print(f"total unique: {len(set(all_ids))}  wild-card total: "
          f"{sum(1 for t in TRACKS for r in selection[t] if r['wild'])}")
    return 0


def cmd_checkmeta(a) -> int:
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    TRACK_TASK = load_vocab(a.work)
    PID_TRACK = {r["id"]: t for t in TRACKS for r in sel["selection"][t]}
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

    for pid, tr in PID_TRACK.items():
        if pid not in meta:
            errs.append(f"{pid} ({tr}) missing from meta")
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
        if "task" in m and m["task"] not in TRACK_TASK[tr]:
            errs.append(f"{pid} task {m['task']!r} not in {tr} vocabulary")
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
    extra = set(meta) - set(PID_TRACK)
    if extra:
        errs.append(f"meta contains ids not in selection: {sorted(extra)}")

    print(f"\nmeta entries: {len(meta)} / 70")
    for t in TRACKS:
        ids = [r["id"] for r in sel["selection"][t]]
        print(f"  {t}: {sum(1 for i in ids if i in meta)}/10")
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
    for t in TRACKS:
        for row in sel["selection"][t]:
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

    for t in TRACKS:
        cn, tag, scope = TRACK_CN[t]
        rows = sel["selection"][t]
        wc = [r["id"] for r in rows if r["wild"]]
        L: list[str] = []
        L.append(f"# ArXiv Daily Digest - {a.date} ({cn}, {len(rows)} papers)")
        L.append("")
        L.append(f"**Generated**: {a.generated}")
        L.append("")
        L.append("**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG submissions, "
                 f"listing day {a.listing} (announced {a.announced})")
        L.append("")
        L.append(f"**Batch window**: {a.win_a} .. {a.win_b}（arXiv 公告批次横跨两个 UTC 日："
                 f"从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），"
                 f"到当日的同一时刻为止）")
        L.append("")
        L.append(f"**Track**: {t} (top {len(rows)} of {src['scan_unique']} papers scanned, "
                 f"{src['full_reads']} full reads)")
        L.append("")
        L.append(f"**Scope**: {scope}")
        L.append("")
        if wc:
            # wild_summary[t] = [summary, reason_paragraph, (optional more paragraphs)]
            parts = list(wild_summary[t])
            L.append(f"⚠️ **Wild-card**: {parts[0]}")
            L.append("")
            for para in parts[1:]:
                L.append(para)
                L.append("")
        L.append("---")
        L.append("")
        L.append(f"## Top 10 - {cn}")
        L.append("")
        for i, row in enumerate(rows, 1):
            pid = row["id"]
            c = cards[pid]
            m = meta[pid]
            orgs = orgs_of(pid)
            L.append(f"### {i}. {c['title']}")
            L.append("")
            L.append(f"**arXiv**: [{pid}]({strip_ver(c['abs_url'])}) | **Score**: {row['score']:.1f} "
                     f"(relevance {row['relevance']} x 0.7 + quality {row['quality']} x 0.3) | "
                     f"**Tags**: {tag}, {', '.join(m['tags'])}, {short_org(orgs[0])} | "
                     f"**Categories**: {', '.join(c.get('categories', []))} | **Pages**: {c.get('pages', '?')}")
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
                why += "  [wild-card=yes] " + wild_reason.get(pid, "本线该批次供给不足，按相邻方向补位。")
            L.append(f"**Why this ranks #{i}**: {why}")
            L.append("")
            L.append("---")
            L.append("")
        (out_dir / f"{a.date}_{t}_report.md").write_text("\n".join(L) + "\n", encoding="utf-8")

        E: list[str] = []
        E.append(f"# {a.date} - {cn} 条目目录（{len(rows)} 篇）")
        E.append("")
        E.append("每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。")
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
        (out_dir / f"{a.date}_{t}_entry.md").write_text("\n".join(E) + "\n", encoding="utf-8")

    print("wrote", len(TRACKS) * 2, "files ->", out_dir)
    print("figures copied:", nfig)
    for t in TRACKS:
        print(f"  {t}: {len(sel['selection'][t])} papers, "
              f"{sum(1 for r in sel['selection'][t] if r['wild'])} wild-card")
    return 0


def cmd_verify(a) -> int:
    repo = Path(a.repo)
    out_dir = repo / "daily_arxiv_digest" / a.date[:7].replace("-", "_") / a.date
    res = out_dir / "res"
    sel = json.loads((a.work / "selection.json").read_text(encoding="utf-8"))
    TRACK_TASK = load_vocab(a.work)
    errs, warns = [], []

    all_ids = [r["id"] for t in TRACKS for r in sel["selection"][t]]
    if len(all_ids) != 70:
        errs.append(f"selection total {len(all_ids)} != 70")
    if len(set(all_ids)) != len(all_ids):
        errs.append(f"duplicate ids: {[i for i in set(all_ids) if all_ids.count(i) > 1]}")
    for t in TRACKS:
        if len(sel["selection"][t]) != 10:
            errs.append(f"{t}: {len(sel['selection'][t])} papers != 10")
        sc = [r["score"] for r in sel["selection"][t]]
        if sc != sorted(sc, reverse=True):
            errs.append(f"{t}: scores not descending")

    if not out_dir.exists():
        print(f"[FATAL] output dir missing: {out_dir}")
        return 2
    for t in TRACKS:
        for kind in ("report", "entry"):
            if not (out_dir / f"{a.date}_{t}_{kind}.md").exists():
                errs.append(f"missing {a.date}_{t}_{kind}.md")

    for t in TRACKS:
        rp, ep = out_dir / f"{a.date}_{t}_report.md", out_dir / f"{a.date}_{t}_entry.md"
        if not (rp.exists() and ep.exists()):
            continue
        rtxt, etxt = rp.read_text(encoding="utf-8"), ep.read_text(encoding="utf-8")
        ids = [r["id"] for r in sel["selection"][t]]
        wild = [r["id"] for r in sel["selection"][t] if r["wild"]]

        heads = re.findall(r"^### (\d+)\. ", rtxt, re.M)
        if len(heads) != 10 or [int(h) for h in heads] != list(range(1, 11)):
            errs.append(f"{t} report: bad '### N.' headings {heads}")
        for block in ("**arXiv**:", "**Authors**:", "**Affiliation**:", "**Abstract**",
                      "**Key findings**", "**Why this ranks #"):
            if rtxt.count(block) != 10:
                errs.append(f"{t} report: block {block} count {rtxt.count(block)} != 10")
        for b in rtxt.split("\n### ")[1:]:
            head = b.split("\n", 1)[0][:60]
            if ("**Key figures**" in b) != ("![" in b and "res/" in b):
                errs.append(f"{t} report: figure block/image mismatch in '{head}'")
        for lbl in ("Finding", "Inference", "Recommendation"):
            if rtxt.count(f"- **{lbl}**:") != 10:
                errs.append(f"{t} report: {lbl} count != 10")
        rscores = [float(x) for x in re.findall(r"\*\*Score\*\*: ([0-9.]+)", rtxt)]
        if len(rscores) != 10 or rscores != sorted(rscores, reverse=True):
            errs.append(f"{t} report: scores {rscores}")
        rep_ids = re.findall(r"\[(\d{4}\.\d{4,5})\]\(https://arxiv\.org/abs/", rtxt)
        if rep_ids != ids:
            errs.append(f"{t} report: arxiv id order mismatch")
        ent = [u.rsplit("/", 1)[-1] for u in re.findall(
            r"\[!\[paper\]\(https://img\.shields\.io/badge/Arxiv_\d{4}\.\d{2}-blue\)\]"
            r"\((https://arxiv\.org/abs/[0-9.]+)\)", etxt)]
        if ent != ids:
            errs.append(f"{t} entry: arxiv id order mismatch")
        if etxt.count("+ **") != 10:
            errs.append(f"{t} entry: {etxt.count('+ **')} title lines != 10")
        for lbl in ("architecture", "task", "organization"):
            if etxt.count(f"![{lbl}]") != 10:
                errs.append(f"{t} entry: {lbl} badge count != 10")
        for tb in re.findall(r"!\[task\]\(https://img\.shields\.io/badge/([^)]+?)-magenta\)", etxt):
            if tb not in TRACK_TASK[t]:
                errs.append(f"{t} entry: task badge {tb!r} not in {t} vocabulary")
        for ob in re.findall(r"!\[organization\]\(https://img\.shields\.io/badge/([^)]*)-green\)", etxt):
            if not ob.strip():
                errs.append(f"{t} entry: empty organization badge")
        for desc in re.findall(r'<p style="font-size: 14px;">\*\*(.+?)\*\*</p>', etxt, re.S):
            if "**" in desc:
                errs.append(f"{t} entry: nested ** in desc")
            if not (77 <= len(desc) <= 165):
                warns.append(f"{t} entry_desc length {len(desc)}")
        for aff in re.findall(r"\*\*Affiliation\*\*: (.+)", rtxt):
            if not aff.strip() or aff.strip() == "[unverified]":
                warns.append(f"{t} affiliation unverified: {aff[:50]}")
        nmark = rtxt.count("[wild-card=yes]")
        if len(wild) and nmark != len(wild):
            errs.append(f"{t} report: {nmark} wild-card markers != {len(wild)}")
        if not wild and nmark:
            errs.append(f"{t} report: {nmark} wild-card markers but none declared")
        if wild and "Wild-card" not in rtxt:
            errs.append(f"{t} report: wild-card without declaration")
        if "wild" in etxt.lower():
            errs.append(f"{t} entry: contains 'wild' marker (must not)")
        for tok in ("TODO", "FIXME", "XXX", "TBD", "PLACEHOLDER"):
            if tok in rtxt or tok in etxt:
                errs.append(f"{t}: placeholder {tok} found")

    referenced = set()
    for t in TRACKS:
        rp = out_dir / f"{a.date}_{t}_report.md"
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

    print(f"selection: {len(all_ids)} papers, {len(set(all_ids))} unique")
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

    # newest toc row = the row for the most recent dated directory already in the table
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

    def common(p, need_date=False):
        p.add_argument("--work", required=True, help="working dir, e.g. codex_temp/2026-11-06")
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
