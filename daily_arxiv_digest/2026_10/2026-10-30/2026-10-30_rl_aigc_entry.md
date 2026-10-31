# 2026-10-30 - 生成式内容模型强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **EmpDPO: Enabling Emphasis Control in TTS via Direct Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39427)
![architecture](https://img.shields.io/badge/EmpDPO_TwoStage_DPO_Diffusion_TTS-red)
![task](https://img.shields.io/badge/DPO_Diffusion-magenta)
![organization](https://img.shields.io/badge/Adobe_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EmpDPO 用两阶段配方给预训练 diffusion TTS 补上词级重音控制：先 supervised fine-tuning 再 DPO，两阶段信号都来自现成的多语种重音检测器，只需几千条偏好对即可明显增强重音且保持自然度。**</p>
+ **DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39265)
![architecture](https://img.shields.io/badge/DeCoRL_Objectwise_Consistency_RL-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Xiaohongshu_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DeCoRL 把多图合成的一致性拆成物体级一致性：先建立跨参考图的物体对应并定位生成区域，再用单物体标注训练的 VLM reward model 产出逐物体反馈并聚合成 RL 奖励，在 DeCo-Bench 与 MICo-Bench 上一致提升。**</p>
+ **EditAgent: Rethinking Agentic Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39664)
![architecture](https://img.shields.io/badge/EditAgent_VerificationRecord_Listwise_Judge-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/UC_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EditAgent 指出 agentic 编辑器受限于动作空间与 judge 的观测空间，用路由加验证记录扩展二者，并发现现成 VLM judge 优于微调 reward model；并行候选加一次 listwise 评判获专家 78.5% 偏好。**</p>
+ **Skillful and realistic precipitation forecasting with reinforced diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38775)
![architecture](https://img.shields.io/badge/FitzRoy_Reinforced_Discrete_Diffusion-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FitzRoy 用强化学习精修 conditional discrete diffusion 预测降水，在最长 24 小时预见期内同时保持最先进预报技巧与结构真实性并捕捉极端事件，在 2025 年 Texas Hill Country 洪水中给出破纪录累积信号。**</p>
+ **SelfThinker: Self-Evolving Reasoning via Reliability-Verified Intrinsic Visual Thoughts**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40115)
![architecture](https://img.shields.io/badge/SelfThinker_CPMI_Scored_VisualThoughts-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Tsinghua_Shenzhen_International_Graduate_School,_Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zhangquanchen/SelfThinker)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SelfThinker 让统一多模态模型用自生成的辅助图按 conditional pointwise mutual information 打分，再以高效用视觉思维做 flow matching 精修与 on-policy 自蒸馏，推理时无需生成中间图像即把 ThinkMorph-7B 七基准均值从 52.7 提到 64.0。**</p>
+ **VEvo-Harness: Causally-Guarded Self-Evolving Harness for Agentic Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39158)
![architecture](https://img.shields.io/badge/VEvo_Harness_Causal_Skill_Governance-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Taobao_&_Tmall_group_of_Alibaba-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VEvo-Harness 用 visual traceback、反事实双臂回放的因果治理、三层技能库与异构 sandbox 策略，把 agentic 图像生成从浅层生成-验证-重写循环升级为持续自我进化的 harness。**</p>
+ **ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39539)
![architecture](https://img.shields.io/badge/ROAD_Representation_Grounded_Adversarial_Distill-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ROAD 用单一对抗目标与受 Lipschitz 控制的 Transformer critic head 做 one-step text-to-image 蒸馏，配合周期性重抽随机混合与 Jacobian R1，一步内在 SDXL 达到 11.03 FID、SD3.5-M 达到 13.73。**</p>
+ **sDMD: Sinkhorn Distribution Matching Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39889)
![architecture](https://img.shields.io/badge/sDMD_Sinkhorn_Corrected_Distribution_Matching-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**sDMD 把 DMD 接到 Wasserstein 梯度流视角，用有限 batch 估计的 Sinkhorn divergence 增广 integral KL，并依据 discriminator 输出自适应启用修正，在 FLUX 与 Qwen-Image 上以 2 到 4 步超越蒸馏基线。**</p>
+ **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39277)
![architecture](https://img.shields.io/badge/CAViLD_Covariance_Aware_Progressive_Distill-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CAViLD 用密度自适应 vicinal 学习与 NIQE 引导的负数据增广净化条件感知隐空间，再用 EMA teacher 内化 classifier-free guidance 方向实现单分支推理，并以协方差感知渐进蒸馏把采样压到 4 个 NFE 以内。**</p>
+ **An ODE-based Sampler for Discrete Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40618)
![architecture](https://img.shields.io/badge/ERF_Exponential_Residual_Flows_Discrete_Diffusion-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/CMAP,_Ecole_polytechnique-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 exponential residual flows，为离散扩散构造保持边缘分布的确定性分段 ODE 采样器，推导其实用离散化并专门化到 masked 与 uniform 扩散，其确定性轨迹可支持一致性蒸馏并在代码与文本基准上取得提升。**</p>
