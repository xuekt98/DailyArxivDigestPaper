# 2026-11-05 - LLM 后训练 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **C-GRPO: Conformal Group Relative Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05591)
![architecture](https://img.shields.io/badge/Conformal_Adaptive_Rollout_Budget-red)
![task](https://img.shields.io/badge/Conformal_Policy_Optimization-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRPO 的固定 rollout 预算换成基于共形校准的停止阈值：闭式推理用 APS 式分数、执行式代码用 first-success 分数，并证明停止规则具有有限样本覆盖；6 个基准上平均训练 rollout 减少 49–70%，跨模型迁移时最多再省 82%。**</p>
+ **Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06543)
![architecture](https://img.shields.io/badge/Online_Rubric_Self_Distillation-red)
![task](https://img.shields.io/badge/Process_Reward-magenta)
![organization](https://img.shields.io/badge/Computer_Network_Information_Center_University_of_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AnnaXChun/ORSD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让策略自己从同组 on-policy 轨迹蒸馏出多份自然语言过程 rubric，由冻结验证器选出最优一份作为特权信息，再用有无 rubric 的似然差构造 token 级过程信用并叠加到 GRPO 优势上；ALFWorld 上比 GRPO 高 12.12 与 3.36 个百分点，WebShop 上成功率 63.00%。**</p>
+ **On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05609)
![architecture](https://img.shields.io/badge/Multi_Teacher_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Chicago-green)
[![project](https://img.shields.io/badge/project-blue)](https://yichenzw.com/opd-generalization.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 on-policy 蒸馏的分布内近乎完美会掩盖分布外能力没有真正固化：外推设定下 OPD/MOPD 拿到教师 IND 分数的 96.04–102.73%，但 OOD 仍比基座低 2.45–16.25%，组合设定下比最强教师低 18.19–24.34%，并提出几何修补加以改进。**</p>
+ **Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06244)
![architecture](https://img.shields.io/badge/Rubric_Curriculum_Preference_RL-red)
![task](https://img.shields.io/badge/Rubric_Reward-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对「判定比生成容易」的生成-验证鸿沟，用 rollout 之间的成对偏好加上 rubric 准则课程，把静态评分换成非平稳信号：基线几百步即 plateau 而 RcRL 在 1000 步后仍在提升，创意写作对基座取得 70.5% 人类胜率，HealthBench 上提升 14.6% 与 25.4%。**</p>
+ **Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05942)
![architecture](https://img.shields.io/badge/Reward_Budget_Advantage_Construction-red)
![task](https://img.shields.io/badge/Reward_Budgeting-magenta)
![organization](https://img.shields.io/badge/Qwen_Business_Unit_Alibaba-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从隐式目标策略视角导出 sharpness 因子 κ 及其有效对应 κ_eff，据此提出每个 prompt 分配固定总奖励预算的即插即用优势构造：在 Qwen3-8B 与 Llama3.2-3B 上稳定提升多个 RL 基线，AMC23 最多 +12.50，AIME24 与 AIME25 各 +10.00。**</p>
+ **The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06476)
![architecture](https://img.shields.io/badge/Graded_Task_Selective_Alignment_Tax-red)
![task](https://img.shields.io/badge/Alignment_Tax-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yuan-phd/delta-filing)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用预注册研究与 TOST 等效检验证明对齐税是分级且任务选择性的：8 个种子跟踪隐式奖励 margin 增长到约 7 个 β 单位，抽取几乎无损（Δ=−0.55 点、±5 点内等效），json 小幅下降（Δ=−3.52 点），router 崩塌（Δ=−30 点）。**</p>
+ **Suppressing Misaligned Behaviors in Language Models, Durably**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05358)
![architecture](https://img.shields.io/badge/Prefix_Expanded_Adversarial_RL-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把事后抑制不良行为形式化为「立即抑制、继续训练下的持久性、通用能力保持」三准则，并提出 PEARL：用缓存 organism 轨迹的中间状态做前缀扩充 rollout 的 GRPO 变体，GPT-OSS-20B 上作弊率压到 2.0%，而无 warmup 的 GRPO 在 Qwen3-4B 上崩塌到 74.8%。**</p>
+ **GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06395)
![architecture](https://img.shields.io/badge/Gibbs_Targeted_Hierarchical_Data_Selection-red)
![task](https://img.shields.io/badge/Data_Selection-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从 KL 正则化 RLVR 的 Gibbs 最优策略出发，用双向 KL 分解区分正确回复的前向项与错误回复的反向项，再据此做两级数据选择：Qwen3-0.6B/GSM8K 上用 4.55M 监督 token 达 45.79% 严格准确率，比全量候选的 13.60M token 少 66.6% 而准确率更高。**</p>
+ **What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06483)
![architecture](https://img.shields.io/badge/Budget_Mix_Multi_Turn_RL-red)
![task](https://img.shields.io/badge/Multi_Turn_RL-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation_Chinese_Academy_of_Sciences_Beijing_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://rethinking-agentic-rl.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用二维指标 Pass@(K,T) 同时扫采样广度与交互深度，指出多轮 agentic RL 的收益高度依赖交互预算：单步动作质量只在 46.8% 与 42.8% 的状态上占优，优势集中在错误恢复与长程韧性；并提出 BudgetMix 在紧预算下平均提升 4.0 到 7.5 个百分点。**</p>
+ **Turns Matter: Advancing Streaming Video RL via Turn-Level Credit**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06728)
![architecture](https://img.shields.io/badge/Turn_Level_Group_Relative_Optimization-red)
![task](https://img.shields.io/badge/Token_Level_Credit-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出流式视频 RL 把一个轨迹级优势摊给所有轮次会造成粒度错配，TurnWise 用静默完成前缀打分构造轮次级组内优势并做轮次内 token 损失平均：Qwen2.5-VL-3B 上 ProactiveVQA 达 43.56 PAUC，超过最强非本方法结果 3.96 点，重复率降到 5.98。**</p>
