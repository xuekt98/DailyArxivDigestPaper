# 2026-10-27 - AIGC 视觉生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35756)
![architecture](https://img.shields.io/badge/Video_Diffusion_3DGS-red)
![task](https://img.shields.io/badge/3D_Editing-magenta)
![organization](https://img.shields.io/badge/Westlake_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 3D 场景编辑重构成轨迹式视频编辑，借预训练视频扩散模型的时空先验保证多视角一致性；TGR 选关键帧、FAVE 用编辑一致性引导做免训练传播，RS-GS 再把更新限制在目标 primitive 上。**</p>
+ **FL4N: Feed-forward Latent Model for 4D Novel View Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35854)
![architecture](https://img.shields.io/badge/Feedforward_Latent_4D-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个前馈式隐空间 4D 新视角合成模型：不用显式 4D Gaussian，而是把动态学成预训练静态隐先验之上的残差，并用轻量动态编码器分离物体运动与相机视差；仅用图像合成目标训练即达 SOTA 质量且可实时渲染。**</p>
+ **Generative Structure from Motion with Native 3D Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35522)
![architecture](https://img.shields.io/badge/Native_3D_Diffusion_MMDiT-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://dotb1ue.github.io/GenSfm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GenSfM 把图像 3D 重建与原生 3D 扩散合进一个多模态扩散 Transformer，在共享注意力下联合去噪形状隐与位姿隐；4 个无标定视角下新视角 PSNR 提升 3.2–4.5 dB，并在不借助外部位姿骨干的前提下以 96% 以上准确率恢复输入视角位姿。**</p>
+ **OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35684)
![architecture](https://img.shields.io/badge/Geometry_Conditioned_Video_Diffusion-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://justin4ai.github.io/OmniShowcase)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OmniShowcase 用全自动合成管线按 3D 主体几何驱动相机轨迹生成训练视频，并给视频模型提供由参考视角重建的法向图转盘做几何条件；由此构建的 Showcase-4K 与 ShowcaseBench 上，主体身份与 3D 一致性达到 SOTA。**</p>
+ **Triage: Skip, Skim, or Refine Attention Tiles in Video Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35706)
![architecture](https://img.shields.io/badge/Attention_Tile_Triage_NVFP4-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/tional_University,_Seoul,_Republic_of_Korea._Correspondence_to:-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Triage 依据 block 统计预测每个注意力 tile 在各近似档位下的误差，把视频 DiT 的注意力 tile 分成跳过、粗读 NVFP4、精修残差校正三档并动态分配；在 Wan2.2 等模型上端到端最高加速 2.32 倍，PSNR 还高出最强基线 0.3–3.0 dB。**</p>
+ **More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35001)
![architecture](https://img.shields.io/badge/VMem_Bench_Diagnostic-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VMem-Bench 用双轨诊断拆解长视频生成里的视觉记忆：检索把实体召回从 0.559 提到 0.63–0.69，却让精度从 0.977 跌到 0.92、禁现实体规避从 0.968 跌到 0.85；作者并指出 prompt 泄漏造成的高召回是必须排除的混淆。**</p>
+ **DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35002)
![architecture](https://img.shields.io/badge/Self_Corrective_Coupled_Guidance-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_(Guangzhou)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DUET4D 让 4D Gaussian 表征反向引导生成先验产生时空一致监督，再用 Sequential Fidelity Resampling 把生成监督提升回 Gaussian 空间、筛出被反复支持的 primitive，从而抑制稀疏视角重建中的冗余 primitive 与漂浮伪影。**</p>
+ **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34782)
![architecture](https://img.shields.io/badge/Downsampled_Self_Probing-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ToDoPro 先让 DiT 在空间 2 倍降采样的参考图上跑几步去噪来自探测参考 token 重要性，再做分层削减——丢弃低重要性 token、用降采样副本替换中等重要性 token；无需额外参数即可显著加速并降低峰值显存。**</p>
+ **GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35224)
![architecture](https://img.shields.io/badge/Adaptive_Bezier_4DGS-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/Ben_Gurion_University_of_the_Negev-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GaussianSpline 用自适应非均匀三次 Bézier 样条建模每个 Gaussian 的运动，联合学习控制点与时间划分，并借反射式控制点约束保证相邻段 G1 连续；在 Neural 3D Video 等数据集上对高动态场景重建质量显著提升。**</p>
+ **Copying As Defense: Protecting Images from Editing By Eliciting Model Copying**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35566)
![architecture](https://img.shields.io/badge/Attention_Intervention_CaD-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Copying-as-Defense 反其道而行：不去抑制模型对参考图的注意力，而是在早期 transformer block 里最大化 target 到参考图的注意力质量，让模型转而复现输入；平均编辑成功率从 81.4% 降到 24.0%，比最强基线再降 44.3%。**</p>