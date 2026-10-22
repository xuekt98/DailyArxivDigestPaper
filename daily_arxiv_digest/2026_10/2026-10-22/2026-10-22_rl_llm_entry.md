# 2026-10-22 - 强化学习 · LLM 后训练与对齐 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.28770)
![architecture](https://img.shields.io/badge/ReAPO-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RLVR 改进语言模型推理，但通常依赖独立的随机 rollout 来探索，这会反复采样相似的失败策略。**</p>
+ **Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity in LLMs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29281)
![architecture](https://img.shields.io/badge/Flat_RLVR-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Ulsan_National_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RLVR（尤其是 GRPO）已成为大语言模型后训练的核心范式，在增强推理能力上非常有效。**</p>
+ **Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29671)
![architecture](https://img.shields.io/badge/Uni_Mem-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长期智能体记忆正从预定义工作流转向可学习的构建与检索策略。**</p>
+ **ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29410)
![architecture](https://img.shields.io/badge/ECHO_Common_Mode_Offset-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Graduate_School_of_Information_Science_and_Technology,_The_University_of_Tokyo,_Tokyo,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**偏好优化可以改进每一个排序指标，同时却在建立一个隐藏的、共享的表征位移，而相对损失几乎察觉不到它，最终可能摧毁生成能力。**</p>
+ **RubricOpt: Self-Revision of Semantic Rubrics for Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29491)
![architecture](https://img.shields.io/badge/RubricOpt-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/South_China_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**模型的失败可以揭示训练所用行为标准的缺口。**</p>
+ **One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29427)
![architecture](https://img.shields.io/badge/EMPO-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/Tianjin_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多轮 RL 显著提升了 LLM 智能体在复杂长时程交互任务上的表现。**</p>
+ **TeachBack: Learning to Teach via Bidirectional Preference Optimization for On-Policy Self-Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29167)
![architecture](https://img.shields.io/badge/TeachBack-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**on-policy 自蒸馏（OPSD）让语言模型从一个教师学习，教师由同一模型实例化但拥有特权信息（如参考答案）。**</p>
+ **Stochastic Pruning of the DPO Computation Graph: 1.4x Faster Training and Lower Peak Memory**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29538)
![architecture](https://img.shields.io/badge/DPO_Graph_Pruning-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/South_China_University_of_Technology,_Shenzhen_Technology_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DPO 在输出打分、序列执行与反向传播上都有训练开销，因此仅减少监督并不必然节省计算。**</p>
+ **Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29552)
![architecture](https://img.shields.io/badge/Generalized_CycleGRPO-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/NUS,_UCAS,_NTU-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**细粒度多模态智能要求模型既能理解指定区域、又能从语言定位它。**</p>
+ **Differentially Private Sparse Reward Estimation with Preference Feedback**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30099)
![architecture](https://img.shields.io/badge/Private_Sparse_RLHF-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/University_of_Massachusetts_Boston-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RLHF 已成为对齐大语言模型与人类价值的核心范式，但对敏感偏好数据的依赖要求严格的差分隐私（DP）保证。**</p>
