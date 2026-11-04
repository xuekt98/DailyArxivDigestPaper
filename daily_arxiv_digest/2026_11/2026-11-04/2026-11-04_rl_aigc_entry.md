# 2026-11-04 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04386)
![architecture](https://img.shields.io/badge/Multi_Teacher_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/StepFun-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把能力整合与步数蒸馏合并为一次训练：StepX-OPD 在 SD3.5-Medium 和 FLUX.1-dev 上四步采样归一化均分达 0.8901 与 0.8902，超过 40 步的 Flow-OPD，训练还省下约 37% GPU 小时。**</p>
+ **PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04948)
![architecture](https://img.shields.io/badge/Parallel_Trajectory_Verifier_Search-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Australian_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Ringo-Star/PATTS.git)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PATTS 在并行多模态离散扩散 LLM 上做轨迹级推理期搜索，用模型内部可靠性信号给外部 VLM 验证加权，在 MMaDA-Parallel 固定 N=32 时把 GenEval 提到 0.844，高于 Best-of-N 的 0.787 与 FKD 的 0.810。**</p>
+ **Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04792)
![architecture](https://img.shields.io/badge/Density_Aware_Reward_Scaling-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DARS 用组内局部密度反向缩放奖励，不改策略梯度目标也不用额外 critic；在多模态导航上把 GRPO 的模式 TV 距离从 0.750 降到 0.014，在文生图提示适配上把 MS-COCO 图像 Vendi 从 8.76 提到 13.04 且 CLIP 对齐不变。**</p>
+ **Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04916)
![architecture](https://img.shields.io/badge/Multimodal_Understanding_Stack-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Kling_Team-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可灵团队拆解视频生成背后的多模态理解栈：Kling-MLLM 统一图像视频音频输入，提示增强用文本级与生成器在环的强化学习，奖励建模拆成可解释的通用奖励模型与快速多维打分的决策奖励模型。**</p>
+ **Multi-Objective Generative Optimization via Expected Hypervolume Fine-Tuning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05207)
![architecture](https://img.shields.io/badge/Expected_Hypervolume_Fine_Tuning-red)
![task](https://img.shields.io/badge/Multi_Objective_Fine_Tuning-magenta)
![organization](https://img.shields.io/badge/Mohamed_Bin_Zayed_University_of_Artificial_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HVFT 用一阶变分把期望超体积写成候选的期望边际超体积贡献，得到无偏可解的自适应奖励并分解为 KL 近似的标量奖励子问题；在三个治疗性肽段任务上 100-超体积达 11.67，超过 TR2D2 的 7.78。**</p>
+ **Bidirectional Centered Score Matching for Discrete Diffusion Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04279)
![architecture](https://img.shields.io/badge/Bidirectional_Centered_Score_Matching-red)
![task](https://img.shields.io/badge/Discrete_Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Academy_of_AI_for_Science-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BCSM 用 O(K) 双向活跃集和 O(K) 目标改进离散扩散蒸馏，单步推理下 MMMU 达 35.67，超过未蒸馏学生 32 步时的 32.14，NFE 最多可降 6 倍，属本线的相邻方向补位工作。**</p>
+ **Perturb, Repair, Verify: Self-Play Vision-Language Verifiers for Compositional Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05158)
![architecture](https://img.shields.io/badge/Self_Play_Vision_Language_Verifier-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PROVE 用同一 Qwen3.5-2B 骨干自博弈跑扰动-验证-修复-验证闭环训练视觉语言验证器，组合理解均分从 83.22 提到 86.85，广泛任务均分从 58.77 到 61.03，属本线的奖励模型方向补位。**</p>
+ **Denoising Is Stein: Moment Access and a Resource Hierarchy for Learning Hidden Structure in Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04043)
![architecture](https://img.shields.io/badge/Stein_Moment_Score_Learning-red)
![task](https://img.shields.io/badge/Diffusion_Learning_Theory-magenta)
![organization](https://img.shields.io/badge/Microsoft-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该 75 页理论工作把去噪损失关联到 Stein 差异，协方差匹配时需 d^{k*-1} 阶特征、两阶段学习器用 O(d^{k*/2} log d) 个干净样本即得固定分数增益，为扩散后训练给出样本与特征的资源边界。**</p>
+ **Policy Network Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04614)
![architecture](https://img.shields.io/badge/Latent_Diffusion_Policy_Generator-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Tencent-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DPPG 反过来用扩散生成 RL 策略网络参数，Transformer 自编码器压缩参数后，任务条件扩散可在 20 个 Atari、5 个 Classic Control、5 个 MuJoCo 任务上共训一个模型，同显存下可生成参数量约为 pdiff 的 100 倍。**</p>
+ **Seeing Through the Illusion: Test-Time Scaling for World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03585)
![architecture](https://img.shields.io/badge/Pre_Execution_Candidate_Selector-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Huawei_Technologies_Canada-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WISE 在冻结的世界动作模型前加一道候选选择器，按动作有效性、时序规则、逆动力学一致性与指令进度给每个决策的 4 个候选打分，RoboLab 成功率从 6.0% 提到 24.0%，属推理期扩展方向的补位。**</p>
