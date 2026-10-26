# 2026-10-26 - AIGC 图像 / 视频 / 3D 生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Scaling Transformer Energy-based Models For High Quality Image Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31889)
![architecture](https://img.shields.io/badge/Transformer_EBM-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/MIT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出隐空间 Transformer 能量模型（TEM），多层能量求和组合局部纹理与全局语义约束，并用视觉基础模型监督中间表征；在 ImageNet 256 上不用 CFG 即达 FID-50K 3.82，并验证组合式生成、零样本补全与分布外检测。**</p>
+ **SyncVid: World-Equivariant Diffusion for Synchronized Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31765)
![architecture](https://img.shields.io/badge/World_Equivariant_Diffusion-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Qualcomm_AI_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://qualcomm-ai-research.github.io/SyncVid-Webpage/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把噪声先验放到源视频导出的规范 3D 空间采样、再光栅化到目标相机，并用跨视角一致白化修复光栅化引入的相关性；仅靠 LoRA 适配即可让多视角视频生成在感知质量与跨视角一致性上同时提升。**</p>
+ **LOCI: Localized Continuous Control for Multi-Subject Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31950)
![architecture](https://img.shields.io/badge/Regional_LoRA-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Meta_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用主体级注意力绑定做空间隔离，用 Regional LoRA 把标量系数换成按 token 对齐空间布局的缩放向量；单个适配器只训练一次，推理期缩放区域残差即可连续调节每个主体的编辑强度，跨区域干扰显著下降。**</p>
+ **AlphaAnything: Extending Pretrained RGB Generators to RGBA**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32413)
![architecture](https://img.shields.io/badge/LoRA_Alpha_Branch-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在预训练 RGB 生成器的原隐空间里直接插入 LoRA 与 alpha 分支扩展出 RGBA，不做重建预训练，且保证任意固定隐变量下 RGB 解码与原解码器完全一致；配套 EA Loss 支持精确端点与连续半透明。**</p>
+ **PASTA: Prompt-Aware Annealed Diffusion Sampling**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32390)
![architecture](https://img.shields.io/badge/Annealed_Diffusion_Sampling-red)
![task](https://img.shields.io/badge/Layout_to_Image-magenta)
![organization](https://img.shields.io/badge/Hosei_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**training-free 的留白保持框架：在共享潜变量轨迹上用掩码引导融合完整 prompt 与 context prompt 引导，并用退火调度在早期去噪压制语义泄漏、后期恢复风格一致性。**</p>
+ **ChoreoStudio: Planning What, When, and Who in Music-Driven Group Choreography**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32325)
![architecture](https://img.shields.io/badge/Diffusion_With_Planning-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Monash_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把编舞显式拆成「演什么队形、什么时候变、谁去变」三个决策，由冻结的全模态模型当编剧、扩散生成器执行；在 AIOZ-GDance 上动作质量、群体组织与队形动态三项均达 SOTA。**</p>
+ **CityLift: Compositional 3D Urban Generation from a Single Image**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32728)
![architecture](https://img.shields.io/badge/Flow_Model_Spatial_Inheritance-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Xi'an_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://ranhaogong.github.io/CityLift/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从单张城景图生成可编辑的带纹理建筑 mesh：场景流与实例流先出粗结构，再用流模型在局部体素里细化，同一套坐标映射把建筑放回场景；并发布 4997 个合成场景的 CityLift-5K。**</p>
+ **TIE: Training-free CLIP Embedding Guidance for Compositional Text-to-Image Alignment**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32407)
![architecture](https://img.shields.io/badge/CLIP_Embedding_Guidance-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Yonsei_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://hong-sujung.github.io/TIE/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**嵌入层诊断发现 prompt 中越靠后的概念熵越高、第一层 CLIP 注意力就刻画对象-属性绑定强度；据此用一次文本嵌入更新（熵感知奇异值放大 + 插值外推绑定）在推理期修复概念丢失与概念混淆。**</p>
+ **CompMVR: Compression-Aware Multi-View Restoration Using Diffusion Models for Geometrically Consistent 3D Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32800)
![architecture](https://img.shields.io/badge/Multi_View_Diffusion_Restoration-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Kyungpook_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://mchaewon.github.io/CompMVR-project-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出压缩伪影先破坏跨视角几何一致性、再毁掉整个 3D 重建管线；提出压缩感知的多视角扩散复原框架，在恢复视觉细节的同时提升几何可靠性，显著改善新视角合成与相机位姿估计。**</p>
+ **PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31908)
![architecture](https://img.shields.io/badge/Pixel_Space_Flow_Matching-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Imperial_College_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://ranrhuang.github.io/pixgr/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把可微渲染与像素空间流匹配搬进前馈式 3D 高斯重建，避开 VAE 隐空间压缩带来的误差传播；稀疏视图与视角外推下优于回归式方法，同时保持亚秒级推理。**</p>
