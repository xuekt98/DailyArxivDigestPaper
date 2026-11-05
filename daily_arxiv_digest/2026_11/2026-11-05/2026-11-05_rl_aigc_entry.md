# 2026-11-05 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Learning Noise Optimization for Reward Alignment in Few-Step Generative Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06255)
![architecture](https://img.shields.io/badge/Learning_Noise_Optimization-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LeNO 用 Local GRPO 把奖励引导的初始噪声优化摊销成学到的残差传输，少步生成器推理时只做一次噪声修正即可提升美学分、PickScore 与 ImageReward，并在蛋白结构生成上把可设计率从 0.15 提到 0.31。**</p>
+ **EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06518)
![architecture](https://img.shields.io/badge/EmoReward-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://emoreward-project.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EmoReward 从一次完整训练留下的轨迹反推各奖励通道的可信度，用反射式门控与跨轮记忆校准多奖励权重，让 HunyuanVideo 1.5 上的 VideoAlign Overall 在 SAGE-GRPO 下提升 0.5645，缓解主观情绪目标的奖励黑客。**</p>
+ **Ruby-OPD: Enhancing Pronunciation Controllability and Accuracy for Flow-Matching Text-to-Speech via On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06403)
![architecture](https://img.shields.io/badge/Ruby_OPD-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Baidu_Inc._Shenzhen_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ruby-OPD 用冻结的 Ruby 教师在学生自己的 rollout 轨迹上做 on-policy 蒸馏，把上下文相关的多音字读法迁移到纯表记文本输入，无需成对语音即可把日语音符读音准确率推到 97.13%。**</p>
+ **From Handcrafted to Generative: RLVR-Optimized Icon Generation for Alexa+**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06123)
![architecture](https://img.shields.io/badge/Objective_Verifier_Flow_GRPO-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Alexa+ 的 Alexicon 流水线把设计规范写成自动判定笔画间距的客观验证器，用 Flow-GRPO 微调 FLUX.2 [klein] 4B，在独立 VLM 评委下把 1,000 个概念的通过率从 15.7% 提到 58.7%，并已上线生产。**</p>
+ **Whose Values Are Generated? Measuring Visual Value Leakage in Multilingual Text-to-Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05578)
![architecture](https://img.shields.io/badge/VisionValueBench-red)
![task](https://img.shields.io/badge/T2I_Evaluation-magenta)
![organization](https://img.shields.io/badge/University_of_Wisconsin-Madison-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VisionValueBench 用 Hofstede 六维文化价值构造 2,773 条多语场景，在 960 个场景上评测 6 个 T2I 系统，发现所有系统都偏好低权力距离、个人主义与享乐主义，提示语言的影响很小。**</p>
+ **NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05648)
![architecture](https://img.shields.io/badge/Text_Stream_Adversarial_Distillation-red)
![task](https://img.shields.io/badge/Adversarial_Distillation-magenta)
![organization](https://img.shields.io/badge/SketchX_CVSSP_University_of_Surrey-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NitroFusion2 把对抗蒸馏的判别器从图像流搬到 MMDiT 文本流，并用方面提示控制排版、物体与风格等六个维度，使 6B 学生模型在 1 步下就把 GenEval 提到 75.86、DPG-Bench 提到 86.48。**</p>
+ **VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06796)
![architecture](https://img.shields.io/badge/Velocity_Adversarial_Distillation-red)
![task](https://img.shields.io/badge/Few_Step_Distillation-magenta)
![organization](https://img.shields.io/badge/Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Luo-Yihong/VA-TDM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VA-TDM 用学到的 critic 比较师生速度场，把 score 蒸馏、Fisher 匹配与矩匹配统一到同一框架，在 SD3.5-Medium 上把四步 GenEval 从 0.61 提到 0.67，并成功扩展到 33B 的 MiniMax-H3。**</p>
+ **Same Layout, Different Count: What Number Words Do Past Ten in Text-to-Image Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06840)
![architecture](https://img.shields.io/badge/Number_Word_Count_Benchmark-red)
![task](https://img.shields.io/badge/T2I_Evaluation-magenta)
![organization](https://img.shields.io/badge/University_of_Colorado_Boulder-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**五个开源文生图模型上的数量词研究让标注者数了 3,088 张图，发现超过十个物体后数量指令基本失效，SD3.5-M 画对数量仅 4%，而把计数画进起始潜变量网格后命中率升到 59%。**</p>
+ **Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05755)
![architecture](https://img.shields.io/badge/CtrlFlow-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Northeastern_University_Boston_MA_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CtrlFlow 给冻结骨干挂两个各 2.5% 参数的 LoRA，在单次前向同时输出基流与引导方向，把 CFG 的两路预测蒸馏成可调尺度的单次前向，N=25 时每图耗时由 843 毫秒降到 437 毫秒。**</p>
+ **Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06000)
![architecture](https://img.shields.io/badge/Style_Conditioned_MoE-red)
![task](https://img.shields.io/badge/Source_Attribution-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Technology_Kharagpur_INDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mallikagarg/IntrAA-SD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**IntrAA-SD 提出同架构源模型溯源任务与 140K 张图像的基准，用冻结 CLIP 门控的 MoE 配合 LoRA 适配的 DINOv2 特征，在 10 个 SDXL 微调模型上取得域内 99.03%、域外 88.55% 的归因准确率。**</p>
