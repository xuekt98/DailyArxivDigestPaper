# 2026-10-23 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Scaling Laws for Generative Reward Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30765)
![architecture](https://img.shields.io/badge/GenRM_Scaling_Laws-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/RaychevAngel/generative-reward-models)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇系统研究生成式奖励模型作为在线偏好提供者：GRPO 训练的 Thinking 裁判静态准确率更高，但在线 DPO 中排序反转（8 组里 7 组 Answer-Only 更优），并提出「评测者-奖励者鸿沟」——静态判断准确率不决定下游优化质量。**</p>
+ **UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31641)
![architecture](https://img.shields.io/badge/UniVOE-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UniVOE 用「移除驱动」同时训练视频物体移除与注入：训练好的移除器把真实有物体视频转成无物体配对，为注入提供大规模监督，再用专有奖励模型做基于奖励的后训练对齐人类偏好，两项任务均达 SOTA。**</p>
+ **Where Do Long Captions Fail? Position-Aware Diagnosis and Reinforcement Learning for Detailed Image Captioning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31111)
![architecture](https://img.shields.io/badge/PAGER-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PAGER 把长图像描述当作位置问题而非数量问题：用位置感知 rubric 把密集参考分解为原子断言并按四分位诊断（中段假具体、尾段假含糊），再用分离的 GRPO 信号分别修复中段证据、尾部续写、覆盖度与长度控制。**</p>
+ **HimmBO: High-Dimensional Interactive Model-Merging Bayesian Optimization for Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30875)
![architecture](https://img.shields.io/badge/HimmBO-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HimmBO 用两阶段偏好贝叶斯优化把 T2I 适配器合并扩展到 1080 个：筛选阶段在预生成图像上做水平集估计恢复活跃集合（无需图像生成），精修阶段在低维子空间优化系数，达到给定相似度所需生成量不到此前方法的十分之一。**</p>
+ **Building Presentation Intelligence for High-Quality Slide Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30888)
![architecture](https://img.shields.io/badge/Presentation_Intelligence-red)
![task](https://img.shields.io/badge/Aesthetic_Scoring-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇提出面向高质量幻灯片生成的统一训练框架：交叉验证数据合成 + 教师增强 + 混合教师 SFT，再以一套可验证美学指标配合 GRPO 优化幻灯片级视觉属性，PresentBench 上比 GLM-5.2 更高，RL 在五个美学维度上进一步提升。**</p>
+ **To Route or to Adapt? Multi-Expert Diffusion Planners in Unseen Regions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31095)
![architecture](https://img.shields.io/badge/Route_or_Adapt-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/The_University_of_Tokyo-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/tlab-wide/RouteOrAdapt)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇对比「测试时路由」与「奖励微调」：三个留出地图上八种路由方案无一优于静态默认，逐场景挑最优专家的 oracle 也只减少 0.9 m 偏移；而 20 个目标区域场景的奖励微调把车队平均偏移从 12.4 m 降到 6.9 m。**</p>
+ **Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31592)
![architecture](https://img.shields.io/badge/PC-DAPS-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Max_Planck_Institute_for_Intelligent_Systems-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PC-DAPS 指出非线性逆问题上「报告 best-of-k」本身会掩盖先验不一致的失败，转而在单次采样运行内维护多个候选解、按先验一致性剪枝替换，全程无需真值访问。**</p>
+ **ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30704)
![architecture](https://img.shields.io/badge/ParaLin++-red)
![task](https://img.shields.io/badge/GenEval-magenta)
![organization](https://img.shields.io/badge/City_University_of_Hong_Kong_(Dongguan)-green)
[![project](https://img.shields.io/badge/project-blue)](https://paralinplus.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ParaLin++ 先系统审计训练无关减步的质量指标：这类方法在 FID / CLIP 下近乎无损，却在 GenEval、DPG-Bench、LongTextBench 上实质退化；据此提出保持完整步数离散化的并行采样器 ParaLin++，加速 2.6×–4.8×。**</p>
+ **SplatLab: Autonomous Scientific Discovery for 3DGS Research**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30468)
![architecture](https://img.shields.io/badge/SplatLab-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![project](https://img.shields.io/badge/project-blue)](https://seemandhar.github.io/splatlab)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SplatLab 是面向 3DGS 的自主科研系统：用实测 GPU PSNR 驱动跨八岛的级联加权 Elo 锦标赛给候选打分，并设常设反证者在失败时扣 Elo；手稿比复现目标高 +0.18 到 +3.78 dB，且每个数字都绑定到已记录的训练运行。**</p>
+ **SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31120)
![architecture](https://img.shields.io/badge/SetCommit-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Kissmetothemoon/SetCommit)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SetCommit 是训练无关的扩散语言模型并行承诺方法：不再按置信度独立选 token，而是在 token 可靠性与局部联合承诺风险之间选集合，并做预算中性局部交换；32 次评估下准确率最高提升 7.4 点，等质量下加速 1.44×–1.74×。**</p>
