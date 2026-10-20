+ **Text-to-Image Generative Modeling Without Language Pretraining**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.26863)
![architecture](https://img.shields.io/badge/Language_Free_Autoregressive_T2I-red)
![task](https://img.shields.io/badge/Text_To_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Keshigeyan_Chandrasegaran1,2_Yue_Zhao1_Armin_W._Thomas2-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**现代文生图系统使用互联网规模的**语言预训练**来做文本条件图像生成。我们问：语言预训练对强 T2I 生成是否必要？本文引入 Halcyon——一族早期融合的多模态自回归模型，完全从零预训练于 GPIC（1 亿图文……摘要在此处截断）。**</p>

+ **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.26262)
![architecture](https://img.shields.io/badge/Dynamics_Aware_Sparse_Attention-red)
![task](https://img.shields.io/badge/Efficient_Autoregressive_Video-magenta)
![organization](https://img.shields.io/badge/1Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归扩散 transformer 已成为长视频生成的强范式，但常受制于可观的计算开销与内存占用。这一低效源于**稠密计算机制在所有时空区域上均匀分配处理资源**（摘要在此处截断）。**</p>

+ **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.26165)
![architecture](https://img.shields.io/badge/Tri_Partite_Trajectory_Distillation-red)
![task](https://img.shields.io/badge/Real_Time_Autoregressive_Video-magenta)
![organization](https://img.shields.io/badge/1The_University_of_Hong_Kong,_2ByteDance_Seed,_3Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散已成为高效视频生成的主导范式，但其实际部署仍受**生成质量与推理效率的权衡**所限。作者把该瓶颈归因于 AR rollout 中的三个误差来源：基座模型误差、训练-推理分布……（摘要在此处截断）。**</p>

+ **Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.25634)
![architecture](https://img.shields.io/badge/Drift_Resistant_Frozen_Base_AR-red)
![task](https://img.shields.io/badge/Autoregressive_Video_Diffusion-magenta)
![organization](https://img.shields.io/badge/1Northeastern_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散模型以已生成为条件生成任意长度视频流。然而它们遭受**暴露偏差**：在干净上下文上训练的模型必须从自身不完美的输出继续，误差不断累积直到数秒内质量崩溃（摘要在此处截断）。**</p>

+ **PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.26711)
![architecture](https://img.shields.io/badge/Object_Level_Physical_Measurement-red)
![task](https://img.shields.io/badge/Video_Generation_Physics_Benchmark-magenta)
![organization](https://img.shields.io/badge/1APRIL_Lab,_Zhejiang_University,_2Huazhong_University_of_Science_and_Technology,_3Tencent_Youtu-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期视频生成模型产出视觉上有说服力的输出，但其**物理合理性**仍未被充分度量。物理合理性追问生成的物体是否遵守几何、运动学、动力学与守恒律。既有基准依赖粗糙的视觉语言模型判断或面向具身世界模型（摘要在此处截断）。**</p>

+ **RxGS: Relightable Gaussian Stylization via BRDF Decomposition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.25681)
![architecture](https://img.shields.io/badge/BRDF_Decomposition_Stylization-red)
![task](https://img.shields.io/badge/Relightable_3D_Stylization-magenta)
![organization](https://img.shields.io/badge/1School_of_Computer_Science,_University_of_Technology_Sydney,_Sydney,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于参考的 3D 场景风格化把参考图像的外观转移到重建的 3D 场景上，同时保持场景几何。近期方法通过优化神经场景模型（NeRF/3DGS）的外观表示来执行这种转移（摘要在此处截断）。**</p>

+ **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.26244)
![architecture](https://img.shields.io/badge/Reciprocal_Sparse_Attention_Caching-red)
![task](https://img.shields.io/badge/Efficient_Video_Diffusion-magenta)
![organization](https://img.shields.io/badge/1University_of_Cambridge,_2Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散 transformer 生成高质量视频但计算昂贵。稀疏注意力与时间缓存分别在去噪步内与跨去噪步减少计算，天然可组合。然而**用稀疏注意力产生的预测会成为时间复用的来源**，使其误差……（摘要在此处截断）。**</p>

+ **LEAP: Accelerating ODE-based Diffusion Sampling with Optimal Linear Leaps**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.25918)
![architecture](https://img.shields.io/badge/Optimal_Linear_Leaps-red)
![task](https://img.shields.io/badge/Accelerated_Diffusion_Sampling-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散模型主要依赖通用的基于 ODE 的数值方法做免训练加速采样，但**时间离散过粗时性能会退化**。本文提出最优线性跳跃（LEAP），一种建立在采样轨迹几何的理论与实证研究之上的专门方法（摘要在此处截断）。**</p>

+ **Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.25887)
![architecture](https://img.shields.io/badge/Few_Shot_Overfitting_View_3DGS-red)
![task](https://img.shields.io/badge/Sparse_View_Novel_View_Synthesis-magenta)
![organization](https://img.shields.io/badge/LEJIA_YE∗,_School_of_Aeronautics_and_Astronautics,_Sun_Yat-sen_University,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**稀疏视角新视角合成对 AR/VR 与实时通信应用至关重要，但在有限视角下重建 3D 场景仍具挑战。虽然 3DGS 在稠密视角下表现优异，但在稀疏输入下会**过拟合并发生几何退化**（摘要在此处截断）。**</p>

+ **PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.25664)
![architecture](https://img.shields.io/badge/Postdictive_Smoothing_Caching-red)
![task](https://img.shields.io/badge/Revisable_Diffusion_Caching-magenta)
![organization](https://img.shields.io/badge/1School_of_Software,_Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散与流匹配模型取得出色视觉质量但因迭代采样而昂贵。基于缓存的加速是实用的免训练方案，通过复用或预测中间特征实现。然而既有方法大多强制**只向前**的信息流（摘要在此处截断）。**</p>

