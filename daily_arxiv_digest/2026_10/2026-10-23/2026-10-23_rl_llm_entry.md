# 2026-10-23 - LLM 后训练的 RL（RLHF / DPO / GRPO / RLAIF / RLVR） 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **MOER: Mix-Policy Optimization under Expert Prefix Guidance with Selective Rollback**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30873)
![architecture](https://img.shields.io/badge/MOER-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/City_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/CityU-MLO/MOER)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MOER 用逐次衰减的专家 CoT 前缀引导模型自行补全，并以选择性回滚保证离策略轨迹正确；在策略 token 上用 GRPO 损失、专家与补全 token 上用信赖域 SFT 损失，数学与通用推理任务平均分最高。**</p>
+ **Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31624)
![architecture](https://img.shields.io/badge/RLVR_Instrumental_Convergence_Audit-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Minnesota_-_Twin_Cities-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇按 checkpoint 追踪 OLMo-3-7B-Think 的工具性趋同行为：比率从 SFT 的 25.0% 升到 RLVR 第 200 步的 46.1%，再降到最终的 11.8%（p = 0.015），32B 端点亦从 35.53% 降至 22.37%，说明 RLVR 的影响并非单调。**</p>
+ **Reward-Weighted Preference Optimization for Selective Combinatorial Optimization Problems**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31239)
![architecture](https://img.shields.io/badge/RWPO-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/University_of_Twente-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RWPO 在偏好学习中保留奖励差信息：按候选轨迹奖励的归一化差值加权每个偏好损失，在 OP / PCTSP / 随机 PCTSP / KP 上一致优于无权重的偏好优化与策略梯度基线，OP 上 100–2000 节点规模超过 Compass 元启发式。**</p>
+ **Group Relative Policy Optimisation Improves Multilingual Speech Recognition in Low-Resource Languages**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30663)
![architecture](https://img.shields.io/badge/SunflowerASR-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Sunbird_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇把 GRPO 从 LLM 式语音模型扩展到小型非 LLM encoder-decoder ASR：以 Whisper-large-v3 在 51 种非洲语言上以 CER 为目标训练，所得 SunflowerASR 在 AfriVox-v2 与 SimbaBench 取得最好的公开宏平均 WER（0.227 / 0.372）。**</p>
+ **Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30882)
![architecture](https://img.shields.io/badge/Provenance_of_Wait-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇追踪推理模型中 {wait} 标记的来源：零 RL 几乎从不铸造它，它随训练数据到来；RL-Zero 配方会放大它而无 KL 的 GRPO 不会，SFT 后的 RL 几乎不改它，作者的 GRPO 则抹除由微调植入的标记。**</p>
+ **RECAP: Looking Once Is Not Enough for Vision-Language Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30834)
![architecture](https://img.shields.io/badge/RECAP-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RECAP 研究长思维链推理中 VLM 的时间定位失效：引入视觉重访这一时间定位的图像证据再激活，跨三个骨干验证重访峰值可预测正确性且与性能有因果关联，遮蔽峰值比遮蔽非峰值更伤性能。**</p>
+ **ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30933)
![architecture](https://img.shields.io/badge/ReflectPO-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Meituan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReflectPO 用分支差异与重复访问构造错误恢复提示（Reflection-Guided Sampling），并以父子奖励差与恢复收益做树状信用分配，在两个长程工具使用基准上多数领域优于现有基线。**</p>
+ **GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30796)
![architecture](https://img.shields.io/badge/GIFT-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lilifree/GIFT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GIFT 对蒸馏梯度做 token 级几何分解，分出与 RL 梯度平行的一阶冲突分量（安全过滤）与正交的新颖方向分量（价值度量），据此排序教师更新并用渐进覆盖退火收缩蒸馏预算，在困难数学推理上取得最高 9.5% 相对增益。**</p>
+ **Consistency Is Not Validity: Self-Rewarded Moral Argumentation Makes Language Models Decisive but Pliable**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30349)
![architecture](https://img.shields.io/badge/Self-Rewarded_Moral_Argumentation-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Google_DeepMind-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇用掩蔽思维的自裁锦标赛训练 RL 策略来奖励好的道德论证，策略在 MoralChoice / ELEPHANT / MORABLES 上变得更果断且更抗选项顺序扰动，但谄媚与重构仍存——作者结论是「一致性不是有效性」。**</p>
+ **What Pairwise Evaluation Misses: Reward Scores across Prompts**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31090)
![architecture](https://img.shields.io/badge/Pairwise_Evaluation_Audit-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Warsaw_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇揭示成对奖励评测的盲区：同一 prompt 的共享分量被抵消而从未被检验。对 18 个已发布评分器的审计显示分数按 prompt 聚集远强于人类评分（HelpSteer2 上 prompt 间占比 0.34–0.64 vs 人类近零），并建议分别检查 prompt 间变化、对错误 prompt 的敏感性与选择有用性。**</p>
