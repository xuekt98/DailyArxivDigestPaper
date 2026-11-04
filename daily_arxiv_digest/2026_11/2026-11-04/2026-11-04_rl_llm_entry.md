# 2026-11-04 - LLM 后训练 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03627)
![architecture](https://img.shields.io/badge/Strategy_Incentivized_RLVR-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ziqipang/rl_meta_thinking)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在可控方程求解框架上揭示 RLVR 的策略崩塌：分布内推导占比 85% 的模型在 OOD 跌破 50%、准确率跌至 6%，与双射反演任务共同训练可恢复正确策略并提升零样本数学迁移。**</p>
+ **FADE: Factored Ability--Difficulty Filtering for Online RLVR Scheduling**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03625)
![architecture](https://img.shields.io/badge/Bilinear_Ability_Difficulty_State_Space_Filter-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 FADE 双线性状态空间滤波器，把 RLVR 调度中策略能力与题目难度分离到两个时间尺度，闭式 Woodbury 更新后同预算下五基准平均分最高提升 2.9 个点，每步开销不足 0.6 毫秒。**</p>
+ **On the Primacy Bias in RLVR Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04061)
![architecture](https://img.shields.io/badge/Primacy_Bias_RLVR_Diagnostics-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Notre_Dame-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用首因偏误统一解释 RLVR 的冲突结论：混合训练只锐化简单题并造成 Pass@k 覆盖收缩，难题训练初期扩展表示但久训遗忘简单题，RL 微调模型的更新稀疏率高达 45.5%–79.9%。**</p>
+ **AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04079)
![architecture](https://img.shields.io/badge/Steer_Guide_Execute_Triad-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://sites.google.com/view/algopilot)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 AlgoPilot 跨范式推理框架，用 SteerLM 选范式、GuideLM 生成结构化指导、ExecutionLM 执行，在 Qwen3-8B 上把平均准确率从 38.4% 提升到 72.9%，超过 GLM-5 提示基线 11.7 个百分点。**</p>
+ **ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04787)
![architecture](https://img.shields.io/badge/Recoverable_Frontier_Search_RLVR-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Capital_Normal_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://cnu-bot-group.github.io/ReSI-Math/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出可恢复能力前沿与 ReSI-Math 框架，用进化搜索在 Qwen3-VL-8B 上从 621 次尝试得到 272 个验证器确认的正确子代（43.8%），三轮顺序 one-shot RLVR 后 MATH500 与 WE-MATH 平均分由 78.71 提升到 80.16。**</p>
+ **JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05263)
![architecture](https://img.shields.io/badge/Joint_Hierarchical_MARL_Web_Agent-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Center_for_Advanced_AI_Accenture-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 JHiMA-WebRL 联合分层多智能体框架，用教师标注的子任务监督加扩展 GRPO 联合训练分解器与 actor，WebArena-Lite-v2 上两个 7B 角色拿到 37.2% 成功率，高于同协议 RL 微调的 32B 单体的 24%。**</p>
+ **Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05266)
![architecture](https://img.shields.io/badge/Targeted_Turn_Level_Self_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Cursor_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 targeted guidance：用逐轮文本反馈做 on-policy 自蒸馏，且只对策略失败的轮施加反馈并叠加逐条 RL 奖励，在五项风格判据上取到 0.55–0.99 的同时把编码通过率稳在 0.33 与基线持平。**</p>
+ **Shuffled OPSD: When Semantic Consistency Hurts On-Policy Self-Distillation?**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04958)
![architecture](https://img.shields.io/badge/Shuffled_Problem_OPSD-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出语义连贯性并非自蒸馏的无条件收益：只打乱共享题面词序、保留教师示例，可同时超过完整题面对照与标准 OPSD，Qwen3-1.7B 上最大领先 3.52 个百分点。**</p>
+ **P$^2$-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03953)
![architecture](https://img.shields.io/badge/Parameter_Prior_Multi_Teacher_OPD-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Australian_Institute_for_Machine_Learning_Adelaide_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 P²-MOPD，把学生与专家参数的线性组合当作可微模型并联合优化混合系数与学生权重，使专家充当参数先验，1.7B 模型平均恢复率达 94.7%（MOPD 80.9%）且用一半步数超过 MOPD 终值。**</p>
+ **Think Less, Locally: Local Preference Learning for Reasoning Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04814)
![architecture](https://img.shields.io/badge/Local_Overthinking_DPO_Compression-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/MOEKLINNS_School_of_Computer_Science_and_Technology_Xian_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/MuyaoYuan/LoCo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出局部偏好学习压缩推理长度：从自生成轨迹检测过度思考状态并用 DPO 教模型何时收尾，数学任务长度下降 41.7%–45.4%、代码下降 23.4%–36.3%，准确率持平或更好。**</p>
