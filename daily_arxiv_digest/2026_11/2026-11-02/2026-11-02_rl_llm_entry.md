# 2026-11-02 - 强化学习 · LLM 后训练与对齐 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Steering Vectors as a Training Signal in LLM Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40998)
![architecture](https://img.shields.io/badge/SteeringVector_AdvantageRepair_SFT_Hook-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Arizona_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 steering vector 从推理期的后验开关改造成训练期信号：监督阶段在隐状态上注入，RL 阶段用 correctness-contrast 方向修复错误 rollout 的优势，在数学基准上验证并给出三条明确的失效边界。**</p>
+ **Reliability-Weighted Direct Preference Optimization: Penalized Weights for Robust Preference Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41588)
![architecture](https://img.shields.io/badge/RW_DPO_ReliabilityWeighted_MinimaxConcave-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Kennesaw_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为每条偏好对比引入可学习的可靠度权重并与策略联合估计，用 minimax-concave 惩罚把模型不认同的标注自动识别为低权重，仿真与含 10–30% 翻转标签的 DPO 微调上均优于原方法。**</p>
+ **CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42054)
![architecture](https://img.shields.io/badge/CRoS_Scrambled_CoT_CausalityReward-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/UNC_Chapel_Hill-green)
[![project](https://img.shields.io/badge/project-blue)](https://xxiaoyuuuu.github.io/CRoS-Page)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CRoS 因果性奖励：只打乱 CoT 步骤顺序而保留步内信息，避免把信息量变化误当作因果性，在 Reasoning Gym 上同时提升域外准确率、CoT-Pass@K 与推理忠实度。**</p>
+ **bf16 Rounding Silently Discards Most RL Policy Updates: A Hidden Training-Inference Mismatch and an Unbiased One-Line Fix**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41073)
![architecture](https://img.shields.io/badge/FairCast_Unbiased_Export_StochasticRounding-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示 bf16 舍入会静默丢弃多数 RL 策略更新（Qwen3-1.7B 每步仅 0.4–0.5% 服务权重变化、策略滞后 50–150 步），提出一行无偏导出的 Fair Cast，25 组配对种子平均领先 6.1 个点。**</p>
+ **CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40926)
![architecture](https://img.shields.io/badge/CoFiBreak_CoarseToFine_DiversityReward-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Simon_Fraser_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出粗到细两层的 GRPO 多样性奖励：粗层鼓励使用组内被低估的策略，细层在抹除有害意图信息后抑制人设与格式重复，仅作用于已达有效性阈值的攻击，在 AdvBench 达到 98.8% ASR@10 且多样性翻倍。**</p>
+ **MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41104)
![architecture](https://img.shields.io/badge/MuonRT_TeacherDisplacement_NoMomentum-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Muon-RT 复用 EMA 教师与学生的位移替代动量缓冲，理论说明该位移等价于更新历史的指数加权表示，在 Qwen2.5-7B 自蒸馏上比 AdamW 高 2.6 个点且持久显存少 42%。**</p>
+ **What Should LLMs Forget: Reinforcement Unlearning of Knowledge Associations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41616)
![architecture](https://img.shields.io/badge/KARU_KnowledgeAssociation_RL_Unlearning-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 Knowledge Association 作为遗忘的基本目标，并用统一的强化学习框架 KARU 落地：token 级奖励 KATR 提供细粒度遗忘监督、分布级正则化推动分布层面遗忘、邻域采样缓解附带损伤。**</p>
+ **DecisionRank: On-Policy Distillation for Decision-Model Rerankers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42128)
![architecture](https://img.shields.io/badge/DecisionRank_ItemSpace_OnPolicyDistillation-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/Meta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DecisionRank 用 item 空间自策略蒸馏把生成式教师的排序知识迁移到只看首 token 打分的重排器：1.7B 模型在 TREC DL19–23 上超过 27B 教师，8B 时在 TREC DL 与 BRIGHT 上分别快 24.5 倍与 16.7 倍。**</p>
+ **On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40945)
![architecture](https://img.shields.io/badge/DLC_DiscrepancyLag_Correction-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/George_Washington_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把训练—推理不一致精确拆成引擎数值差异与训练器策略滞后，并据各自性质提出 DLC 修正：中心化数值偏差、裁剪滞后比并在有效样本量不足时重同步采样器，使 KL 保持在 on-policy 噪声底线的两倍内。**</p>
+ **Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41296)
![architecture](https://img.shields.io/badge/UIDConj_Entropy_Confidence_AuxiliaryReward-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究辅助轨迹偏好能否在有限监督下提升小模型自改进：比较基于置信度的 SC 与结合全局熵变化与局部平滑度的 UID-Conj，前者更会评轨迹质量，后者在若干设定下训练结果更强并可迁移。**</p>
