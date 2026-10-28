# 2026-10-28 - LLM 后训练强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **AudioRSI: Recursively Self-Improving Audio Reasoners**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36578)
![architecture](https://img.shields.io/badge/AudioRSI_Recursive_Self_Critic-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AudioRSI 让一个音频 LLM 同时充当 actor 与 critic，用自身成对比较产生过程级奖励并周期性用当前策略刷新 critic；冻结外部评判时分布外准确率停滞而递归 critic 持续上升，在四个不相交数据集上于 MMAU/MMSU/MMAU-Pro 领先，并自发发展出减少幻觉的结构化推理行为。**</p>
+ **Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37211)
![architecture](https://img.shields.io/badge/BSPO_Bifocal_Self_Distillation-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示视频 RLVR 的「捷径放大」：结果级优化让模型越来越倾向选文本先验支持的答案，作者以视频条件熵与视觉条件熵差距作为可测量的退化指纹，并提出 Bifocal Self-Distillation Policy Optimization，在保留 RLVR 推理收益的同时鼓励既对推理敏感又有视觉依据的更新。**</p>
+ **Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37041)
![architecture](https://img.shields.io/badge/Guided_RLVR_Logic_Controller-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对标准 RLVR 在有限 rollout 预算下几乎采不到低先验困难轨迹的问题，Guided-RLVR 引入一个轻量学得的 Logic Controller 在采样分布层面引导探索，在 GRPO 与 DAPO、数学推理基准上一致有效，并用 t-SNE 对比引导前后末层 rollout 表征的方差变化。**</p>
+ **Exploring the Limits of the Delta Learning Hypothesis: Single-Pair Generator Biases in Direct Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37058)
![architecture](https://img.shields.io/badge/Delta_Learning_Hypothesis_Limits-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Okkam-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**考察 delta learning 假说的边界：固定单对生成器会引入与回答质量无关、却能预测偏好标签的系统性偏差，使单对数据训练的 DPO 持续不如多模型偏好数据（即便大生成器回答质量更高），差距可追溯为对偏差的 reward hacking；论文指出仅增加生成器数量即可部分缓解。**</p>
+ **On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37085)
![architecture](https://img.shields.io/badge/Dual_Sparsity_DPO_NTK-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/The_University_of_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 NTK 线性化下把 DPO 归约为最大间隔分类并提出「双重稀疏性」：数据级稀疏由支持向量驱动、参数级稀疏来自偏好与非偏好回答梯度的相互抵消；论文实证 DPO 产生的跨任务权重内积比 SFT 小一个数量级，GPT-2 Medium 上绝大多数梯度特征分量接近零。**</p>
+ **Bayes-Adaptive MDPs for Rollout Allocation to Enhance GRPO Training**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37429)
![architecture](https://img.shields.io/badge/AdaRoll_GRPO_Bayes_Adaptive_MDP-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/University_of_Toronto-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRPO 的 rollout 预算分配形式化为序贯决策问题：AdaRoll-GRPO 用贝叶斯自适应 MDP 学习难度感知的自适应分配策略，在与标准 GRPO 相同的总预算下最大化训练效用，动机分析给出 MATH 与 GSM8K 上首次解出所需 rollout 次数的难度分布。**</p>
+ **When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36849)
![architecture](https://img.shields.io/badge/PICO_Distribution_Constrained_Decoding-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对一组 rollout 全错时 GRPO 无正样本可用的问题，PICO 用分布约束的联合解码从离策略轨迹中恢复正学习信号：专家数据在 token 级引导解码但保留学生相对 token 概率，动态 top-k 把联合分布限制在有限散度预算内，构造出既可验证又策略兼容的轨迹替换失败 rollout。**</p>
+ **Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37553)
![architecture](https://img.shields.io/badge/Collective_Dynamics_Self_Reinforcement-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把无监督 RLVR 中「数据集变小就崩塌」解释为参数空间共享方向的不稳定性：极简模型显示问题未判定时平衡群体会放大共享扰动，并由两个时间尺度的竞争推导出崩塌的临界问题数量，实验给出七种耦合强度下崩塌概率随 N 的变化并推广到异质置信度与多答案情形。**</p>
+ **SetGRPO: Calibrating Grader-Induced Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36807)
![architecture](https://img.shields.io/badge/SetGRPO_Joint_Coefficient_Uncertainty-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Shandong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 GRPO 的组内训练系数本质上来自不可靠评分器，因而应被建模为不确定量：SetGRPO 用同一回答组上两个评分器的分数构造联合系数不确定集，用它选择回答组并构造策略更新，另配几何引导的安全恢复机制来应对打分分歧。**</p>
+ **PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37471)
![architecture](https://img.shields.io/badge/PerceptRL_Perception_Error_Tree-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PerceptRL 在单轮回答与多轮视觉交互两个层次上强化 MLLM 感知，用层级化能力图与模型探测暴露基座自身的感知弱点，据此构造有针对性的可验证训练数据；并指出工具调用下仍存在坐标漂移——错误裁剪或标注会扭曲后续证据并传播错误。**</p>