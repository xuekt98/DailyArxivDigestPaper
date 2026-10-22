# 2026-10-22 - AIGC 图像 / 视频 / 3D 生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29989)
![architecture](https://img.shields.io/badge/Future_Chunk_Prediction-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University,_ARC_Lab_Tencent_IEG,_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散逐 chunk 生成，但「续得上」不等于「懂场景怎么演化」。**</p>
+ **Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.28954)
![architecture](https://img.shields.io/badge/DINO_R2C_C2R-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Universidad_Rey_Juan_Carlos-green)
[![project](https://img.shields.io/badge/project-blue)](https://gonzalognogales.github.io/coarse2real-sharp/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**C2R（coarse-to-real）视频生成把粗动画 / 仿真 / 游戏渲染视频转成照片级真实视频，同时保持场景布局、相机运动和动态。**</p>
+ **Spatially Gated Demographic Steering for Debiasing Multi-Person Text-to-Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29651)
![architecture](https://img.shields.io/badge/Spatially_Gated_Steering-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Technische_Hochschule_Ingolstadt,_Germany-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/cvims/spatially-gated-steering)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**T2I 模型会复现社会刻板印象，既有缓解手段对整个场景施加一次人口统计修正。**</p>
+ **Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29441)
![architecture](https://img.shields.io/badge/ALLOT_Sparsity_Allocation-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/UCAS,_CASIA,_PKU,_KlingAI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频 Diffusion Transformer 的全 3D 注意力代价高昂，block-sparse 注意力只算选中的注意力块。**</p>
+ **ER-Chord: Spatially Consistent One-Step Image Editing via Equal-Energy Reliability Redistribution**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29248)
![architecture](https://img.shields.io/badge/ER_Chord-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Peizeli1/ER-Chord)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一步生成模型能做快速文本引导图像编辑，但常会意外改动本应保持不变的区域。**</p>
+ **NeuralSRender: G-Buffer Guided Video Diffusion for Sim-to-Real Rendering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29200)
![architecture](https://img.shields.io/badge/NeuralSRender-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Wuhan_University,_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/WHU-USI3DV/NeuralSRender)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自动驾驶感知受限于高质量标注视觉数据的稀缺；仿真器能提供规模训练数据，但真实感不足会拖累真实世界表现。**</p>
+ **RealMe: Immersive Volumetric Video from Minimal Captures**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30023)
![architecture](https://img.shields.io/badge/RealMe-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/State_Key_Laboratory_of_CAD&CG,_Zhejiang_University,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从稀疏低分辨率采集创建沉浸式体积视频是核心问题。**</p>
+ **CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29915)
![architecture](https://img.shields.io/badge/CausalAlign-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Peking_University,_BIGAI,_NVIDIA,_Tsinghua_University,_University_of_Wisconsin-Madison-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散视频生成模型能产出视觉上合理的视频，但相机自运动在长时间跨度上会漂移。**</p>
+ **CCG Diffusion: Combinatory Categorial Grammar-Driven Compositional and Syntactically Disambiguated Text-to-Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.29415)
![architecture](https://img.shields.io/badge/CCG_Diffusion-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Ritsumeikan_University,_Ibaraki,_Osaka_567-8570,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**T2I 模型不显式接收 prompt 的句法结构，因此经常把属性绑错对象、画错空间关系和数量、或在句法歧义处给出错误解读。**</p>
+ **Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30107)
![architecture](https://img.shields.io/badge/Velocity_Ambiguity_Profile-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**流匹配训练的是一族连续的速度回归问题，但通常只报告跨插值时间平均后的损失，掩盖了哪些区间受制于内在歧义、哪些仍受制于数据不足。**</p>
