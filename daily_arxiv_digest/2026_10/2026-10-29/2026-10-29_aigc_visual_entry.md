# 2026-10-29 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37983)
![architecture](https://img.shields.io/badge/WanAR_FixAR_Hierarchical_Denoising-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://kaihua-chen.github.io/wanar_fixar/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WanAR 与 FixAR 组合成一个轻量框架，用两级去噪分别管住漂移与全局一致性，并把相机可控的视频生成重述为 warping-and-inpainting 问题。**</p>
+ **BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38278)
![architecture](https://img.shields.io/badge/BudSplat_Budget_Aware_Gaussian_Pruning-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BudSplat 把前馈 3DGS 的紧凑性当作渲染预算分配问题，用多层 token 提取的 detail-aware 重要度指导 voxel fusion 与 quality-aware 剪枝，在有限基元数下保住高价值区域。**</p>
+ **Self-Consistency Geometry Injection for Multi-view Consistent Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38518)
![architecture](https://img.shields.io/badge/RGMV_SelfConsistency_Geometry_Gate-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Guangdong_University_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/WISLab-GDUT/RGMV)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RGMV 用无参数的 SCG 测量多次几何采样之间的空间一致性得到可靠性图，再由 RGI 按图调制几何条件残差的注入强度，稳住多视图 RGB 生成的几何质量。**</p>
+ **GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37818)
![architecture](https://img.shields.io/badge/GOFish_Calibrated_Fisheye_Reconstruction-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![project](https://img.shields.io/badge/project-blue)](https://3dgofish.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GOFish 是首个直接在鱼眼图像上训练、光栅化超过 180° 视场并抽出对齐网格的 3DGS 表面重建方法，在 200° FIORD 上把 PSNR 相对最优基线提升 2.28 dB。**</p>
+ **Aligning Misaligned Benchmarks for Single-View Novel View Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38349)
![architecture](https://img.shields.io/badge/Aligned_Benchmark_Pose_Matching-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_British_Columbia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文指出单视图新视角合成的评测长期受坐标对齐误差污染，改用 2D-to-2D 匹配加 PnP 对齐重建、只在共可见区域比较后，显式 3D Gaussian 方法反而成为 SOTA。**</p>
+ **V-CAPE: Visual Consistency Assessment for Product Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38611)
![architecture](https://img.shields.io/badge/V_CAPE_Visual_Consistency_Benchmark-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**V-CAPE 提供 4 万对带接受或拒绝标签与结构化失败模式的商品图编辑对，用于评测编辑是否保住几何、纹理、颜色等视觉一致性；所有规模的 VLM 准确率都低于 65%。**</p>
+ **3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38231)
![architecture](https://img.shields.io/badge/3DCodeEdit_Instruction_Edit_Benchmark-red)
![task](https://img.shields.io/badge/3D_Editing-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**3DCodeEdit 用 2,592 个指令引导编辑任务覆盖 108 个 Blender 程序，17 个模型平均成功率仅 37%；引入独立 reviewer 模型的渲染差异反馈后，27B 模型可超过 2.8T 模型。**</p>
+ **StepControl: Long-Horizon Human Motion Generation from Foot-Contact Schedules**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38153)
![architecture](https://img.shields.io/badge/StepControl_FootContact_Schedule-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StepControl 以未来的二值左右脚接触时间表为条件做自回归扩散，无需根节点姿态或语义 prompt，只用专用 cross-attention 注入接触事件，即可在长 rollout 中稳定控制节奏。**</p>
+ **ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38259)
![architecture](https://img.shields.io/badge/ETA_Motion_Sparse_Joint_Learning-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://sy-hwang.github.io/eta-motion-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ETA-Motion 只在紧凑的关节子集上训练动作生成器，靠结合文本与视觉线索的语义关节嵌入与 topology-aware 目标跨骨架对齐，推理时仍可输出完整骨架动作。**</p>
+ **MEV: A Multi-Event Video Dataset for Long-Take Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38241)
![architecture](https://img.shields.io/badge/MEV_Event_Centric_Discretization-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://mev-dataset.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MEV 收集主体依次完成多个互不重叠事件的真实长镜头视频，给出精确时间边界与全局、事件两级结构化 caption，支持按时间锚定的事件条件做长镜头多事件生成。**</p>
