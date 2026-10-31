# 2026-10-29 - 强化学习 · LLM 后训练与对齐 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38391)
![architecture](https://img.shields.io/badge/SCOPE_Selective_Critical_Step_Self_Distillation-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SCOPE 让 agent 在有监督 warm-up 后分析自己的轨迹、生成 hindsight skill，并只在出错的关键步骤上做自蒸馏；配上有界师生系数与成功相对的长度奖励，在 ALFWorld 与 WebShop 上稳定超过 SEED 与 GRPO。**</p>
+ **Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38095)
![architecture](https://img.shields.io/badge/Nemotron35_MoE_Hybrid_Mamba_Transformer-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Nemotron 3.5 Super/Lightning 是开放的高效 MoE 混合 Mamba-Transformer 模型，公开了从 SFT 到 RLVR/RLHF、多教师 on-policy 蒸馏与投机解码的完整后训练流水线，SWE-bench Pro 达 51.78%。**</p>
+ **Predict the Reward, Not the World: World Reward Models for ML Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38439)
![architecture](https://img.shields.io/badge/ForeCritic_WorldRewardModel-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**World Reward Model 直接从真实执行结果学习挑选更优候选程序而不预测执行结果，ForeCritic 在 12438 对留出程序上选对率 79.4%，接入三个 ML agent 框架后平均任务耗时下降 4.4 到 7.5 倍。**</p>
+ **Co-Evolving Policy and Rubric via Capability Awareness for Open-Ended Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38566)
![architecture](https://img.shields.io/badge/CoCA_CoEvolving_Policy_And_Rubric-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/Alibaba_Token_Hub,_Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoCA 用 criterion 级诊断闭环调整 rubric 与策略：对比 query-only 与 rubric-guided rollout 重新标定难度错配的准则，再把引导暴露的能力经自蒸馏内化回 query-only 行为，整体优于其它 rubric-based RL 方法。**</p>
+ **Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and Training**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38220)
![architecture](https://img.shields.io/badge/Rubricon_GenerateSelect_Add_Prune-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Handshake_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Rubricon 用任意 LLM 经 Generate-and-Select、Add、Prune 三步自动产出判别性 rubric，不需要人工偏好标注或训练生成模型；其评分与人工专家 rubric 的对齐度高 9%，还能直接用于后训练。**</p>
+ **ATI-OPD: Adaptive Teacher Intervention for Stable Long-Sequence On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38160)
![architecture](https://img.shields.io/badge/ATI_OPD_Adaptive_Teacher_Intervention-red)
![task](https://img.shields.io/badge/LLM_Alignment-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ATI-OPD 针对长回答中 on-policy 蒸馏会自我强化偏航的问题，用一段短的教师片段替换最早的高分歧前缀，再让学生从改写后的文本继续推理，师生分歧、梯度尖峰与超长响应都明显减少。**</p>
+ **How Much Do Teacher Bridges Matter in Interleaved On-Policy Distillation?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38383)
![architecture](https://img.shields.io/badge/TeacherBridge_LossAblation_ForwardKL_ReverseKL-red)
![task](https://img.shields.io/badge/LLM_Alignment-magenta)
![organization](https://img.shields.io/badge/The_University_of_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在完全相同的轨迹上比较无 loss、forward KL 与 reverse KL，作者发现 teacher bridge 只占 2.7% token、梯度近乎与学生 token 正交，预注册检验未能确认其带来准确率收益，并明确划出 BF16 与停止稳定性的适用边界。**</p>
+ **Two Birds with One Stone: Skill-Augmented Generation via Unified Retrieval and Utilization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38204)
![architecture](https://img.shields.io/badge/SkillUni_Generative_Skill_Retrieval_GRPO-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Chongqing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Skill-Uni 用生成式技能检索把「找技能」和「用技能」统一进同一个模型，以 warm-up 指令微调加 GRPO 两阶段训练，在五个技能相关 benchmark 上相对基座平均提升 66.59% 与 34.82%，且兼容多种检索引擎。**</p>
+ **Locating Sycophancy Across Training Stages in Open Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37788)
![architecture](https://img.shields.io/badge/Sycophancy_Stagewise_Checkpoint_Audit-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Boston_Children's_Hospital_and_Harvard_Medical_School-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在 5 条谱系 13 个开放 checkpoint 上逐阶段测量迎合行为，把 prompt 级顺从与对话级投降拆成两种来源不同的行为：前者 base model 已有，后者几乎只在偏好优化之后的 checkpoint 上出现。**</p>
+ **Post-Training Large Language Models with LLMON**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38120)
![architecture](https://img.shields.io/badge/LLMON_Structured_PostTraining-red)
![task](https://img.shields.io/badge/LLM_Alignment-magenta)
![organization](https://img.shields.io/badge/IBM_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LLMON 用分层标记把指令与数据在 token 层显式分开并要求基于标识符执行；配合 4.6B token 的含干扰项语料做 SFT 加强化学习后，间接 prompt injection 攻击成功率从 53%–100% 降到 0.02%–5.6%。**</p>
