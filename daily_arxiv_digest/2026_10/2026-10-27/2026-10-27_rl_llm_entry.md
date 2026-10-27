# 2026-10-27 - LLM 后训练的强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35518)
![architecture](https://img.shields.io/badge/S3AC_Actor_Critic-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/Shanghai_AI_Laboratory-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**S3AC 为 RLVR 补回 token 级 critic：给出 token 级优势与 prompt 级基线，并借 prompt 级基线估计难度做 Difficulty-Aware Prompt Sampling 以减少 rollout 浪费；在 1.5B–397B 稠密与 MoE 模型上优于 GRPO-X。**</p>
+ **Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35716)
![architecture](https://img.shields.io/badge/Low_Pass_Budgeted_Audits-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRPO 中「有限的强验证器预算怎么花」推导成可优化的问题：优先审计弱通过数最少的组（LB）能在固定修正量下最小化留在奖励黑客身上的优势质量；实测把黑客压到接近零，只用了全量审计 28% 的标签。**</p>
+ **FOCUS: Active Critic Learning for Long-Horizon Language Model Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35801)
![architecture](https://img.shields.io/badge/FOCUS_Active_Critic-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Johns_Hopkins_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FOCUS 用选择性分支让 rollout 控制器从最能降低 critic 估计误差的状态采样续写，把主动学习引入 RL；配合压缩产生的片段边界做 TD(λ) 信用分配，在相同生成预算下优于 GRPO 与 VinePPO，BrowseComp-Plus 领先 7.2 个百分点。**</p>
+ **Audio-R1: Audio Reasoning through Reinforcement Learning on Self-Supervised Tasks**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34609)
![architecture](https://img.shields.io/badge/Audio_R1-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Mila_Quebec_AI_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Audio-R1 把音频自监督任务构造时已确定的答案当作可验证奖励，对多个 LALM 做 RL 后训练：除自监督任务外，在与训练任务不同的下游音频基准上也取得提升，消融显示各任务贡献明确且联合训练有额外增益。**</p>
+ **Improving Reasoning with Rollout Agreement for Group-Based Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34951)
![architecture](https://img.shields.io/badge/RoAR_Rollout_Agreement-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Kyung_Hee_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ldi-kyunghee/RoAR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoAR 用既有 on-policy rollout 分组为已答对的轨迹计算推理一致度并加进奖励，零额外标注与采样；1.5B 模型用 7K 样本零样本达 55.5% 平均 pass@1，比 GRPO 高 6.0 个百分点，盲审虚假推理率也最低（18% vs 32%）。**</p>
+ **Correlation-Aware Exploration for Long-Trace Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34949)
![architecture](https://img.shields.io/badge/Info_GRPO-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/JD.com-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Info-GRPO 用隐式种子把探索从逐 token 的熵正则化转到整条推理轨迹层面：让策略与隐式先验互信息最大化以承载多样性，同时把种子条件熵引向收敛；在 AIME24 上相对 GRPO 的 Avg@8 提升 1.66%–4.17%，并以 8 倍更少采样达到同等多数投票准确率。**</p>
+ **Integrate the Reward, Don't Sample It: Window Likelihood for Interruptions and Backchannels in Full-Duplex Speech Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35581)
![architecture](https://img.shields.io/badge/Window_Likelihood-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**窗口似然（WL）指出 whole-rollout GRPO 在全双工语音模型上的两处结构性失败——最需学习窗口零优势、与奖励不对齐的信用泄漏；改为对停止决策做闭式积分并最大化正确行动对数似然，在六个后训练模型上取得最好的 yield/hold F1。**</p>
+ **Multiscale Policy Optimization for Long-Horizon LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35013)
![architecture](https://img.shields.io/badge/Multiscale_Policy_Optimization-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Multiscale Policy Optimization 基于「critic 价值主要在轮之间变化」的观察，结合多尺度优势估计与轮级重要性采样，把信用分配与策略更新对齐到轮尺度；在搜索、工具使用与自动化任务上用 4B 与 30B-A3B 模型相对强 RL 基线取得一致增益。**</p>
+ **End-to-End MXFP8 Reinforcement Learning on Blackwell: What Matching Buys, When It Pays Off, and How It Fails**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34915)
![architecture](https://img.shields.io/badge/MXFP8_RL_On_Blackwell-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/wengeezhang@gmail.com-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**端到端 MXFP8 RL 实证：采样器跑在学习器的 FP8 网格上可使 train-rollout KL 降低 11%–16%（优于 BF16 采样器），端到端把 MoE step 时间削减 10.7%、生成时间削减 24%；并给出权重同步必须满足的七条条件与静默失败检查。**</p>
+ **Selective Tie Learning: Mitigating Spurious Correlations in Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35787)
![architecture](https://img.shields.io/badge/Selective_Tie_Learning-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**对 log-linear 策略推导出每个 tie 对伪相关依赖的影响影响量，证明取「预测下降最大」的子集在同规模下一阶最优；并以 tie 的隐式奖励边际作代理，在策略、神经模型与 LLM 上以更少的 tie 达到同等去伪相关效果。**</p>