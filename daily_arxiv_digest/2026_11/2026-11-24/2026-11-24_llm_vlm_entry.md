<!-- direction: llm_core -->

+ **Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25123)
![architecture](https://img.shields.io/badge/GrepMem_Append_Only_Log-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GrepMem 用只追加的纯文本日志加正则 grep 工具替代嵌入式结构记忆，在 ContextBench 上把 Qwen3.5-9B 训到 95-97% 准确率，比有损基线的 21% 高出 4 倍以上，并在 BCP-Multi 上比 SUPO 的摘要高 8.8 个百分点。**</p>

+ **Beam Model Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26358)
![architecture](https://img.shields.io/badge/Beam_Sparse_MoE_Transformer-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Beam 是 Reflection 开源的稀疏 MoE 技术报告：501.3B 总参数、23.4B 激活参数，52 层每层 256 专家、每 token 激活 8 个，23.8T token 预训练后在 10.5K 张 GB300 上跑 4 周产生逾 1 亿条 rollout，并配 1M 上下文与 1.93B 投机解码草稿模型。**</p>

+ **Search From the Start: Search-Native Pretraining for Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26809)
![architecture](https://img.shields.io/badge/QueryLM_Search_Native_Pretraining-red)
![task](https://img.shields.io/badge/Pretraining-magenta)
![organization](https://img.shields.io/badge/EPFL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Search-Native Pretraining 在预训练阶段就把网页搜索查询与本地索引检回的响应注入语料，训出的 QueryLM 在知识密集任务上更强：1.4B 的 QueryLM 稳定追平或超过 FLOP 对齐的 3.3B 基线，且该优势在 SFT 之后依然保留。**</p>

+ **NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26157)
![architecture](https://img.shields.io/badge/NariQ_Trellis_Coded_PTQ-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Nari_Labs-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NariQ 用 trellis 编码做后训练量化，校准数据改为 BF16 模型在 Agent 会话中实际生成的 token，使 Qwen3.8-27B 在 3.0 与 2.5 bit 下 DeepSWE 得 84.9% 与 84.5%、反超 BF16 的 83.0%，而此前同位宽方案最多只解出 72% 的任务。**</p>

+ **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27901)
![architecture](https://img.shields.io/badge/QuantStream3D_Mixed_Precision_KV-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**QuantStream3D 系统刻画了流式视觉几何 Transformer 的 KV 量化敏感度，提出几何引导的混合精度 KV 量化与几何对齐的量化感知蒸馏，在 5 个基准 2 个骨干上以主流量 2-bit 缓存把 TUM 轨迹误差降低 57.4%，并带来 5.05 倍压缩与 23.1% 延迟下降。**</p>

+ **AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25582)
![architecture](https://img.shields.io/badge/AutoRAGBench_Open_Code_Space-red)
![task](https://img.shields.io/badge/RAG-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University_Beijing_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://zhanghang9991.github.io/AutoRAGBench)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AutoRAGBench 是首个让 LLM Agent 在开放代码空间从零搭建 RAG 系统的基准：9 个任务、单张 H800、每个 6 小时预算，最强的 GPT-6.1 Sol 配 Codex CLI 平均得 56.1 分，比人写的组合基线 44.4 高 11.7 分，接手人工系统后还能再提 16.6 分。**</p>

+ **CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25673)
![architecture](https://img.shields.io/badge/CompAct_Bench_Compaction_Boundary-red)
![task](https://img.shields.io/badge/Long_Context_Compression-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CompAct-Bench 在 200 个成功 Agent 轨迹的中途插入压缩边界，用同一执行器续跑以衡量压缩对任务完成度的真实影响，覆盖 79 个 BrowseComp、96 个 SWE-bench 与 25 个 CompanyBench 任务，并指出压缩的真正风险是把未决问题改写成已有结论。**</p>

+ **Characterizing and Detecting Unfaithful Work Reports by Coding Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25760)
![architecture](https://img.shields.io/badge/FaithDetector_Unfaithful_Report_Detector-red)
![task](https://img.shields.io/badge/Code_Agent-magenta)
![organization](https://img.shields.io/badge/Peking_University_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文基于 SWE-chat 真实开发对话归纳出 4 类 11 种 Coding Agent 失实报告模式，夸大任务成功最常见；435 份抽样工作报告中 37.24% 含不实陈述，用户平均需 4.3 轮、12.71 分钟纠正，而其提出的 FaithDetector 取得 93.06% macro-F1。**</p>

<!-- direction: vlm_core -->

+ **StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27915)
![architecture](https://img.shields.io/badge/StereoVLM_Hierarchical_Geometric_Supervision-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_HKUST-green)
[![project](https://img.shields.io/badge/project-blue)](https://xpeng-robotics.github.io/stereovlm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StereoVLM 从标定双目观测直接学习可迁移的 3D 表征，用视差、度量深度到语义空间推理的层级监督训练首个几何感知双目 VLM；其 8B 版本在自建 Stereo3D-Bench 上深度 δ1 达 95.17%，把对应 MAE 从 9.27 降到 3.80 像素。**</p>

+ **SKILL.PNG: Learning Agent Skills in Pixel Space**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26296)
![architecture](https://img.shields.io/badge/Skill_PNG_Pixel_Optimization-red)
![task](https://img.shields.io/badge/Visual_Instruction_Tuning-magenta)
![organization](https://img.shields.io/badge/Hasso_Plattner_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/omseeth/skill.png)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SKILL.PNG 把 Agent 技能放到像素空间，用梯度下降穿过冻结 VLM 的视觉编码器优化图像本身，在 4 个 VLM 乘 4 个基准的 16 组设定中 9 组胜过 LLM 优化的文本技能，推理只需 64-256 个图像 token 而非约 900-2000 个文本 token。**</p>

+ **TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25387)
![architecture](https://img.shields.io/badge/TuringSpace_CAPTCHA_Gym-red)
![task](https://img.shields.io/badge/GUI_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Pennsylvania-green)
[![project](https://img.shields.io/badge/project-blue)](https://xuweid.com/turingspace/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TuringSpace 用 125 个必须点击拖拽才能通过的交互式 CAPTCHA 检验 MLLM 的空间智能：人类通过率 94.1%，GPT-6 Astra 仍失败 25.9%、最佳开源 Kimi K3 失败 68.0%，在该环境微调后 Qwen3.5-9B 成功率由 1.6% 升至 33.1%。**</p>

+ **What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25814)
![architecture](https://img.shields.io/badge/Eleven_Feature_Frozen_Probe-red)
![task](https://img.shields.io/badge/Multimodal_Hallucination-magenta)
![organization](https://img.shields.io/badge/Key_Laboratory_of_Computing_Power_Network_and_Information_Security_Ministry_of_Education-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文把 VLM 抗幻觉训练的收益拆成「少说」「廉价剪枝」「其余」三块，用在 500 张标注图上拟合的 11 特征冻结探针做对照，发现 LLaVA-1.5-7B 上 8 个公开方法在 COCO、AMBER、Object HalBench 的大部分超额提升都能被这一弱探针复现。**</p>

+ **VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25069)
![architecture](https://img.shields.io/badge/VisAlloc_Dual_Level_Reweighting-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Kaelyn01/VisAlloc)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VisAlloc 提出样本级视觉过滤加 token 级反事实重加权的双重框架，把特权视觉证据只投给真正依赖视觉的样本与 token，在 8 个基准上把 4B 与 9B 模型的宏平均提到 81.44 与 84.92，分别比 Vision-OPD 复现高 0.97 与 0.52 分。**</p>

<!-- direction: llm_vlm_rl -->

+ **Blind Spots Travel, Knowledge Stays Home: What RL Inherits from an LLM Judge**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25191)
![architecture](https://img.shields.io/badge/Judge_Knowledge_Transfer-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/University_of_Colorado_Boulder_Boulder_Colorado_USA-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/liyu2195/blind-spots-travel)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**拆解 LLM 评判者作为 RL 奖励到底传递了什么：814 次训练显示单题知识几乎不迁移，而对某类问题的整体怀疑会被 12 个样本放大成 98% 的拒答规则。**</p>

+ **Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27780)
![architecture](https://img.shields.io/badge/Search_RSI_Recursive_Improvement-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Hunan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把检索索引从固定背景改造成训练变量：当前策略诊断自己的能力边界、连同证据一起长出新任务，再由自身探针决定送 RL 还是转为提示引导的自演示，全程无需外部教师模型。**</p>

+ **EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26380)
![architecture](https://img.shields.io/badge/EgoCaptioner_Two_Level_Caption-red)
![task](https://img.shields.io/badge/GRPO_Video-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**第一视角视频字幕模型：粗到细标注产出 5 万条训练样本，用 GRPO 以事实、时序、文风三项互补奖励精修，在 PhysCapBench 上比底座高 27.6 分。**</p>

+ **Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25135)
![architecture](https://img.shields.io/badge/RLCDR_Calibrated_Decision_Model-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/FuturiX_AI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用一次前向读出概率分布的决策模型替代打分类 LLM 评判者，只需约 100 条标签校准，即在 MATH500 上带来 4.65 分提升且在策略变化中保持低校准误差。**</p>

+ **When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25793)
![architecture](https://img.shields.io/badge/Tool_Contrastive_Grounding_RL-red)
![task](https://img.shields.io/badge/Multimodal_RLHF-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断多模态安全护栏的理由幻觉，并用工具对比式强化学习只奖励“真的更 grounded”的工具调用，使四个安全基准上的视觉证据分大幅提升且不牺牲分类准确率。**</p>

+ **RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26179)
![architecture](https://img.shields.io/badge/RegionAgent_Two_Stage_DPO-red)
![task](https://img.shields.io/badge/Multimodal_DPO-magenta)
![organization](https://img.shields.io/badge/Northwestern_Polytechnical_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让 VLM 每轮为退化区域挑选修复动作：先用 1 万组动作对做步级 DPO，再用 2 万组轨迹对做轨迹级 DPO，混合退化 PSNR 比基线高 1.22 dB。**</p>

+ **Sequential Anytime Valid Tests for Efficient Inference-Time Alignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26413)
![architecture](https://img.shields.io/badge/E_RWSC_Anytime_Valid_Stopping-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Technology_Kanpur_India-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用可随时成立的 e-process 序贯检验替代拍脑袋的早停阈值：奖励模型只决定下注力度而不影响有效性，认证成本按 1/dKL 随提示难度自适应，并给出近乎最优的样本复杂度。**</p>

