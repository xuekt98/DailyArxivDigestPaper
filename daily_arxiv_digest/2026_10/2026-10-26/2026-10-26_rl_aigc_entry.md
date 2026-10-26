# 2026-10-26 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32222)
![architecture](https://img.shields.io/badge/Reference_Free_Reward_Model-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频世界模型的奖励要同时判视觉质量与动作跟随，而逆向动力学模型在生成视频上根本不可靠；ACWM-RM 用「动作不匹配 / 视频不匹配」两类互补偏好（50.6 万对）训练，无需真值视频即可联合评估两项标准。**</p>
+ **ImageRSI: Verification-Driven Recursive Self-Improvement for Agentic Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32120)
![architecture](https://img.shields.io/badge/Verification_Driven_Self_Improvement-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Alibaba_Qwen_Business_Unit-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**图像生成器全程冻结，把改进放在验证、修复、跨任务经验库与裁判训练上：候选经验需通过成对 A/B 验证才入库，裁判用 SFT + GRPO 更新；MindBench 取得 52.6% 清单严格准确率。**</p>
+ **ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32966)
![architecture](https://img.shields.io/badge/Diffusion_Motion_DPO-red)
![task](https://img.shields.io/badge/Diffusion_DPO-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用扩散模型直接从视频生成人形参考动作，绕过重建与重定向，再用运动跟踪结果对生成器做 DPO 后训练；Unitree G1 上动作质量与可执行性双超 SOTA 流水线，且换跟踪器反馈照样有效。**</p>
+ **EditJev: System One Routing for Image Editing Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32635)
![architecture](https://img.shields.io/badge/Preference_Model_Routing-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不同编辑模型在不同请求上强弱不同：EditJev 用一次前向直出候选编辑器的样本级偏好分数（成对排序目标训练），在 ImgEdit/GEdit-En 上质量小幅提升的同时把估计延迟降低 60.8%/31.7%。**</p>
+ **Spatial Heuristic Strategy based Diffusion Reinforcement Learning for Online 3D Bin Packing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32241)
![architecture](https://img.shields.io/badge/Diffusion_RL_With_Heuristics-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Shandong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把经典装箱启发式当先验塞进扩散 RL：启发式动作预筛压缩动作空间、GNN 建模空间拓扑、复合奖励里加平整度抑制空间碎片化，实现先验知识与自适应优化的结合。**</p>
+ **Fast and Useful: Adapting Distilled Generators for Visual Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32512)
![architecture](https://img.shields.io/badge/Guided_Adapter_Distillation-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Adam_Mickiewicz_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**被蒸馏快的 T2I 生成的图不适合训分类器；只给学生的第一步预测加一个低秩更新、让它回到未引导基座的中间状态即可（基座推理时不存在），ImageNet 上 ResNet-50 top-1 从 8.4% 提到 34.2%。**</p>
+ **Compatible Likelihoods for Flow Matching on Manifolds**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31981)
![architecture](https://img.shields.io/badge/Compatible_Flow_Objectives-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在平坦环面上构造出一个反例：黎曼流匹配扩展的最优速度场把样本推离数据分布；作者提出「兼容性」判据，并给出既兼容又只支撑可行速度的新目标。**</p>
+ **MDMR-Bench: A Multi-Dimensional Benchmark for Multi-Reference Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32459)
![architecture](https://img.shields.io/badge/Multi_Dimensional_Gen_Benchmark-red)
![task](https://img.shields.io/badge/GenEval-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多参考图像生成的多维评测基准，覆盖实体融合与属性迁移、多元素抽取、信息图操作与视觉推理四类挑战，并用「全局级 + 原子级查询」的清单式协议替代整体打分。**</p>
+ **ACVA-Bench: Beyond Prompt Following in Abstract Concept Visualization Ability for Text-to-Image Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32058)
![architecture](https://img.shields.io/badge/Abstract_Concept_Vis_Benchmark-red)
![task](https://img.shields.io/badge/GenEval-magenta)
![organization](https://img.shields.io/badge/Beijing_Language_and_Culture_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让 T2I 画「忠诚」这类没有视觉指涉的抽象概念：基于心理语言学规范构建类别平衡基准，从语义充分性、表征多样性与概念可区分性三维评测，发现模型普遍依赖同一套原型化视觉模式。**</p>
+ **Concept Acupuncturist: An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32059)
![architecture](https://img.shields.io/badge/SAE_Concept_Erasure-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Eran-Xia/ConceptACP)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散模型概念擦除不再全轨迹微调：先把语义概念映射到 U-Net 的 cross-attention 块并只优化最相关的那一块，再用 SAE 特征级修正提供监督；SDXL-Turbo 上遗忘成功率相对基线提升 36.34 个百分点。**</p>
