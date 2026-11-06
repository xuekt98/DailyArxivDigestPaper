# 2026-11-06 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07551)
![architecture](https://img.shields.io/badge/Predictive_Spatio_Temporal_Pruning-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PreSTP 重新审视少步自回归视频扩散，发现跨帧静态冗余与跨步早收敛两类 token 级冗余，直接用模型自身去噪轨迹的早期 clean 估计在线构造掩码，无需重训即可在 5 秒生成上取得 1.52 至 3.20 倍加速。**</p>
+ **WeLM-Image: A Unified Image Generation Model towards Visual Intelligence**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07392)
![architecture](https://img.shields.io/badge/MoT_MoE_Backbone-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/WeChat_Vision_Tencent_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**统一图像基础模型 WeLM-Image 用共享注意力的 MoT 骨干分离理解与生成参数并以 MoE 稀疏扩容，存储参数 31.7B 而每个目标 token 仅激活 5.4B，少步蒸馏版在单张 H20 上 4.98 秒生成 1024 图像。**</p>
+ **Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07294)
![architecture](https://img.shields.io/badge/Householder_Motion_Embedding-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/The_Australian_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Householder 运动嵌入用一串 Householder 反射在通道维构成正交变换，把运动信号写进扩散初始噪声，既精确保留帧内高斯结构又建立跨帧相关，噪声处理比噪声搬运快 2.7 倍且运动贴合度更高。**</p>
+ **ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07658)
![architecture](https://img.shields.io/badge/Triplet_Attention_Slot_DiT-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Qualcomm_AI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ArtCrafter 用 1+2N 个 slot 在单次前向里同时生成铰接物体的静止态与展开态部件网格，靠 Triplet Attention 与排斥损失保持跨状态几何一致，URDF 关节参数则由两态之间的刚体变换解析推出。**</p>
+ **StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07922)
![architecture](https://img.shields.io/badge/Per_Layer_Gradient_Probe-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://guoqincode.github.io/StitchEdit/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StitchEdit 先用逐层梯度探测量出深度目标与编辑目标在各层的兼容性，再用探测曲线定制每层学习率并裁剪冲突层，在自建的 150 例几何编辑基准上全面超过深度条件化基线。**</p>
+ **IDPrior: Decoupling Identity Generation from Facial Image Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07941)
![architecture](https://img.shields.io/badge/Identity_Diffusion_Prior-red)
![task](https://img.shields.io/badge/Identity_Preservation-magenta)
![organization](https://img.shields.io/badge/Fraunhofer_Institute_for_Computer_Graphics_Research_IGD-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fdbtrs/IDperturb)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**IDPrior 两阶段解耦身份生成与人脸合成：先在识别模型嵌入空间学扩散先验生成新身份嵌入，再条件化身份扩散模型出图，兼顾身份唯一性与分布保真，支撑大规模合成识别训练数据。**</p>
+ **Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07961)
![architecture](https://img.shields.io/badge/Scene_Anchor_Voxel_Refiner-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Bri3D 用实例感知的体素场景锚点搭桥单图到组合式 3D 场景生成：先出彩色场景脚手架定排布，再由锚点细化为体素支撑交给冻结物体生成器，几何与布局指标全面领先且脚手架预测只要 5.1 秒。**</p>
+ **LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06856)
![architecture](https://img.shields.io/badge/Graph_Grounded_Checklist-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/South_China_Normal_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://long-banana.com/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LongBanana 给出首个专家设计与专家校验的长上下文多参考图合成基准，90 个任务覆盖 3x3 分类，每任务约 32 张参考图与 20 条约束，用图结构化的 checklist 展开成 4670 个可逐条审计的原子评测项。**</p>
+ **FFMT: Frequency-Factorized Multi-Rate Tokenization for Music-to-Dance Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07384)
![architecture](https://img.shields.io/badge/Frequency_Factorized_Motion_Tokenizer-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FFMT 研究显式的时频分解如何指导离散动作表示的时间分辨率与码本容量，把根相对运动拆为低频编舞骨架与高频残差并非对称配置 token 率与码本，配合先计划后细化的自回归结构，在两个舞蹈数据集上分布保真度领先。**</p>
+ **TRACEMARK: Editor-Aware Watermarking for User Attribution in Text-Guided Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07632)
![architecture](https://img.shields.io/badge/Editor_Aware_Watermarking-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Queens_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**编辑器感知水印框架 TRACEMARK：共享编码器在编辑前埋入用户信号、共享检测器比对参考向量反查请求用户，两端经固定编辑器联合训练，在三个图像域上把编辑后的用户归属识别率推到 87.5%。**</p>
