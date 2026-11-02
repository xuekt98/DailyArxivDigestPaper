# 2026-11-02 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42031)
![architecture](https://img.shields.io/badge/AnyForcing_Unified_Adversarial_AR-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Xidian_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Any Forcing 用一个统一对抗判别器同时约束真实分布、采样步间一致性与首帧质量，再配免训练的长期记忆选择机制，让自回归视频模型在同一套权重下自由切换采样步数并稳定生成一步长视频。**</p>
+ **MoETok: Sparse Expert Routing for 1D Visual Tokenizers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41992)
![architecture](https://img.shields.io/badge/MoETok_Sparse_Expert_Routing-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://gjhhust.github.io/moetok-project)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MoETok 系统研究 1D 视觉 tokenizer 中可学习查询的分工，发现语义监督会让查询自发分化为抓语义的 Content 查询与保细节的 Detail 查询，再用稀疏专家路由按 token 角色分派计算量。**</p>
+ **From Evaluation to Evolution: Benchmarking Image Editing and Evolving Image Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41210)
![architecture](https://img.shields.io/badge/WeGenEditBench_Checklist_RSI-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WeGenEditBench 用 2,740 个实例、148 类任务的原子级 checklist 拆解图像编辑的局部要求，并配套多智能体 harness WeGenEvoStudio，把失败诊断、数据构造与再评估串成能驱动模型演化的闭环。**</p>
+ **VoxLution: Evolving Voxels for High-Fidelity 3D Scene Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41501)
![architecture](https://img.shields.io/badge/VoxLution_Sparse_AR_Voxel_Cascade-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Munich-green)
[![project](https://img.shields.io/badge/project-blue)](https://daoyig.github.io/VoxLution/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VoxLution 把 3D 超分辨率重写为多分辨率稀疏体素上的序列建模，用免训练的分辨率无关八分体编码与逐块自回归级联，把高保真室内场景生成推到 1.5625 cm 体素分辨率。**</p>
+ **GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42002)
![architecture](https://img.shields.io/badge/GeoFlip_Geometry_Flip_Benchmark-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/City_University_of_New_York-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GeoFlip 用受控几何干预构造 482 组场景对与 964 个参考视频，在提示词与物理设定不变时让物理结局翻转，评测 16 个图生视频模型在事件正确性、结构完整性与参考相似度上的表现。**</p>
+ **Coarse3D: Controllable and Faithful Sparse Structure Generation for Image-to-3D**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41231)
![architecture](https://img.shields.io/badge/Coarse3D_DualTower_DiT-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Coarse3D 面向 image-to-3D 的第一阶段稀疏结构，用首帧锚定的规范空间、dual-tower DiT 与像素-体素对应先验，让朝向可控且结构忠实，可直接替换现有流水线的粗阶段。**</p>
+ **RADI3N: GeometRic ImAge EDiting via ParametrIc 3D CoNtrol**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40973)
![architecture](https://img.shields.io/badge/RADI3N_CS_ARAP_Texture_Transfer-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Surrey-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RADI3N 用 CS-ARAP 协方差平滑的形变能量在 SO(3) 旋转场上抑制部件边界突变，再配无反演的调制纹理迁移，让编辑后的纹理跟随部件的新几何，实现几何一致的外观编辑。**</p>
+ **Prior-Guided Single-Exposure HDR Novel View Synthesis via Base-Gain Representation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41011)
![architecture](https://img.shields.io/badge/PriorGS_Base_Gain_3DGS-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Waterloo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PriorGS 是基于 3D Gaussian Splatting 的单曝光 HDR 新视角合成方法，用 LDR 到 HDR 重建先验与可学习 CRF 先验补齐监督缺口，并用 base-gain 分解把 HDR 辐亮度拆成 LDR 底图加 3D 增益场。**</p>
+ **GenDSR: Transferring Representations from Video Generation Models for Dynamic Spatial Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41314)
![architecture](https://img.shields.io/badge/GenDSR_Raw_Delta_Branch-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GenDSR 把视频生成模型的中间表征拆成保留整体时空上下文的 raw 分支与强调时序变化的 delta 分支，用任务条件的 token 门控注入 VLM，在 DSR-Bench 上把 Qwen3-VL-8B 从 62.0% 提到 67.2%。**</p>
+ **PBSR: Pseudo-Burst Super-Resolution via Zero-Shot Novel View Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41258)
![architecture](https://img.shields.io/badge/PBSR_Pseudo_Burst_NVS-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Toyota_Technological_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PBSR 用零样本新视角合成为单张低清图造出带视差的伪连拍帧，再配几何感知对齐与伪影感知微调，让 burst 超分模型在只有一张输入图时也能吃到多帧的亚像素信息。**</p>
