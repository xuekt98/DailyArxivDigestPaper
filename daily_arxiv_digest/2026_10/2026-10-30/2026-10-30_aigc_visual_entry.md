# 2026-10-30 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40495)
![architecture](https://img.shields.io/badge/LucidLyra_MultiTask_Distillation-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research.nvidia.com/labs/sil/projects/lucidlyra)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LucidLyra 把相机可控视频扩散模型与冻结 2D 视觉基础模型的知识蒸馏进一个前馈模型，同时推断高斯几何、外观、开放词表语义与类无关实例线索，无需逐场景优化即可做新视角渲染、开放词表分割与物体分组，并可扩展到单目视频的动态场景重建。**</p>
+ **Coupled Guidance for Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40109)
![architecture](https://img.shields.io/badge/Coupled_Guidance_Flow_Matching-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Huawei-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Coupled Guidance 从几何视角重构 flow matching 的 guidance 机制，指出直接照搬 diffusion guidance 会破坏训练时的 coupling 分布；在机器人避障、灵巧操作与 inpainting 等任务上，样本质量与 guidance 稳定性同时提升且无额外开销。**</p>
+ **MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39530)
![architecture](https://img.shields.io/badge/MorphSIG_PseudoFlow_Feature_Transport-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/UESTC-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MorphSIG 以 training-free 方式把 subject-driven 图像生成重写为伪视频特征传输：Progressive Decoupled Anchoring 在去噪早期用频域解耦打破结构锁定，伪流场引导的特征传输在潜空间搬运主体语义，在姿态多样性与主体保真度上显著超过基线，并提出风格化主体基准。**</p>
+ **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39663)
![architecture](https://img.shields.io/badge/AB_Attention_Block_Sparse_Sampling-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/InfRec-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/InfRec-Cardinal/AB-Attention)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AB-Attention 在视频扩散 Transformer 中精确逼近稠密注意力：按 inclusion probability 采样并逆概率重加权，把稀疏注意力从截断变成估计；在 Wan2.1 与 HunyuanVideo 上跳过 89%–92% 注意力计算，PSNR 最高提升 4.4 dB，端到端加速最高 2.23 倍。**</p>
+ **CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39160)
![architecture](https://img.shields.io/badge/CLaW_Codec_Latent_Watermarking-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CLaW 用预训练水印 codec 把每条消息映射为潜空间残差，在扩散模型去噪后期窗口注入，实现低成本且免反演的用户级溯源；再以解码置信度为反馈自适应校准水印强度，在 SD3.5-medium 与 FLUX.1-dev 上保持高视觉保真，并取得图像变换下的 state-of-the-art 鲁棒性。**</p>
+ **EPC-RawDC: Equivariant Physics Constrained 3D Diffusion with Raw Data Consistency for CBCT to CT Image Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40046)
![architecture](https://img.shields.io/badge/EPC_RawDC_Equivariant_Physics_Constrained_Diffusion-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Jordan_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ALZAHRAALTALIB/EPC-RawDC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EPC-RawDC 是条件 3D latent diffusion 框架，把源自 CBCT 前向模型的几何等变投影约束与原始数据一致性并入体数据生成；在 JUST 实测与 SynthRAD2025 模拟投影队列上 SSIM 均达 0.97，PSNR 相对 DDPM 提升 2.66 dB 与 2.10 dB，MAE 下降约两成。**</p>
+ **ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39399)
![architecture](https://img.shields.io/badge/ACD_GS_Curvature_Aware_Densification-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://waveviewer.github.io/ACD-GS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ACD-GS 用二阶深度响应的曲率先验替代一阶 screen-space 梯度来触发 3DGS 的 densification，对 cloning 与 splitting 做非对称调节，并配合多视角光度一致性筛除单视角误差；在多个数据集上把高斯数量与存储减少近 60%，同时保持有竞争力的渲染保真度。**</p>
+ **GradSplat: Gradients Inside the Forward Pass for Feed-Forward 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38951)
![architecture](https://img.shields.io/badge/GradSplat_In_Forward_Gradient_Refinement-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/South_Dakota_State_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Jingong-Chen/GradSplat/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GradSplat 把前馈式 3DGS 与逐场景优化的差距定位到高斯形状，并用学习到的梯度步在前向内部修正：渲染回输入视角求光度梯度，先更新 opacity 与 color 再更新形状，用 log-anisotropy 保持体积不变地调整轴比，在 RealEstate10K、DL3DV 与 ScanNet++ 上取得最佳结果。**</p>
+ **Edited Endpoints as Partial Goals for Image-to-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39179)
![architecture](https://img.shields.io/badge/Partial_Endpoint_Conditioning-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://wannagetacat.github.io/Edited-Endpoints-I2V/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把编辑后的末帧当作 image-to-video 的部分目标：以 Hard-Cut、Background Motion Reversal 与 Dynamic Degree 刻画全帧条件化伪影，再提出 Partial，约束编辑器 attention 估计的编辑区域，在三个 backbone 上降低伪影且转换完成度无显著差异。**</p>
+ **Calibrating Attention-Based Token Pruning for Efficient Multi-Image Synthesis in UMMs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39467)
![architecture](https://img.shields.io/badge/CATP_Guidance_Consistent_Token_Pruning-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CATP 是首个面向 UMM 多图生成的 training-free 上下文压缩方法：Guidance-Consistent Pruning 同步各条件分支的剪枝决策，Taylor-Calibrated Attention Metric 用二阶修正校正池化偏差，在多个 UMM 与基准上一致优于既有方法，最高加速 2.09 倍。**</p>
