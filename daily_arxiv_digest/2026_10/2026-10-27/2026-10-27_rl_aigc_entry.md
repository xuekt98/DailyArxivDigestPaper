# 2026-10-27 - 生成式内容模型的强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **VaLoP: Value Gradient Lookahead and Pullback for Reward-Guided Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35607)
![architecture](https://img.shields.io/badge/VaLoP_Value_Gradient-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/GIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VaLoP 指出奖励引导扩散的两种梯度估计在高噪声处的误差同源于后验协方差，因而提出向前看一步评估价值再把梯度拉回，用一次向量-雅可比积补上修正项；其摊销版 VaLoP-Fast 用一个奖励训练即可复用到其他奖励。**</p>
+ **DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35201)
![architecture](https://img.shields.io/badge/DTCA_Denoising_Token_Credit-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DTCA 为扩散语言模型的 RL 提出 token 级信用分配：以「提交 token 后剩余掩位置预测置信度的改善量」估计贡献，并按词性分组用于挑选去噪时间步与分配学习信号；LLaDA-8B-Instruct 上 MATH500 最高提升 9.0 个百分点。**</p>
+ **S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35491)
![architecture](https://img.shields.io/badge/S2_RL_SampleSet_Dual-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Northwestern_Polytechnical_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**S²-RL 把语义分割数据集蒸馏重写为扩散模型的文本到图像生成，并用 GRPO 的样本集双奖励微调扩散策略——样本级强制语义对齐与类内多样性、样本集级用上下文多臂老虎机最大化分布多样性，在 ADE20K 与 COCO 上显著超越基线。**</p>
+ **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35594)
![architecture](https://img.shields.io/badge/SF2_Self_Flow_Forcing-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SF² 在不改动 DMD 输出目标的前提下加入预测式表征损失：给学生与 EMA 教师异质噪声水平以建立信息不对称，迫使学生从更脏输入预测教师内部表征；据此缓解时间闪烁并持续改善空间保真与运动质量。**</p>
+ **Cumulative Marginal Matching for One-Step Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34575)
![architecture](https://img.shields.io/badge/CMM_Cumulative_Marginal-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Rochester_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CMM 把流匹配视作一串中间边际分布，直接优化基座与少步模型之间的累积 Wasserstein 差异，并用 pushforward 表示把不可解目标化为可解代理；同时证明 Shortcut-CSL 目标只是 CMM 的一阶近似，建立了两条路线的理论联系。**</p>
+ **Stable Continuous-Time Consistency Distillation: An Empirical Study with a Multistep Extension**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34704)
![architecture](https://img.shields.io/badge/Multistep_sCD-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/The_Pennsylvania_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**对 TrigFlow 做独立实证：CIFAR-10 上复现了 1/2 步 FID，ImageNet-64 上未能复现并指出约 5% 的参数量差距来源；再提出连续时间分段条件的多步一致性蒸馏 MS-sCD，在 M=1 时退化为 sCD，报告 M=2/4/8 的 FID。**</p>
+ **Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35804)
![architecture](https://img.shields.io/badge/dSpark_Schedule_Distillation-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/MBZUAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/VILA-Lab/dSpark)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**dSpark 学习扩散语言生成中「何时提交 token」：构造优先选择能解锁其他位置可预测性的 unmasking 调度，并蒸馏进模型配 KL 正则以保质量；GSM8K 上 LLaDA-8B-Instruct 加速 10.12 倍、Dream-7B-Instruct 加速 5.12 倍。**</p>
+ **CounterFlow: Target-Conditioned Flow Matching for Visual Counterfactuals**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35679)
![architecture](https://img.shields.io/badge/CounterFlow_Target_Conditioned-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Inria_IRISA_Rennes-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CounterFlow 用目标条件化流匹配把源图像直接导向用户指定的目标类别，生成视觉反事实解释；借目标条件向量场识别高度逼真的语义修改，算力开销远低于 GAN 与扩散架构，并在视觉真实感与类别切换上达到 SOTA。**</p>
+ **From Denoising Dynamics to Endpoint Uncertainty in Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35425)
![architecture](https://img.shields.io/badge/Denoising_Dynamics_Uncertainty-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/SiftyML-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在四个掩码扩散语言模型上采集 32,000 条去噪轨迹后发现：轨迹内集中度越高、端点熵越低（控制模型与数据集后 β=-0.222，p<10⁻²⁵），且该关系随去噪推进增强；单条运行的特征即可预测留出运行会否收敛到同一端点。**</p>
+ **VibeVideoBench:Evaluating Multimodal Agents on Code-Driven Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35864)
![architecture](https://img.shields.io/badge/VibeVideoBench-red)
![task](https://img.shields.io/badge/DrawBench-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VibeVideoBench 用 239 个中英双语任务评测代码驱动视频生成：分层评测包含交付规格程序检查、约 13k 项 rubric 检查与三个 VLM 评判面板；九个前沿系统中 GPT-6 Astra 与 Claude Opus 5.5 领先，但最好的系统仍在约四分之一任务上失败于核心要求。**</p>