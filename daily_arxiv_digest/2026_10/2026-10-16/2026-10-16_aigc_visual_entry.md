+ **Speculative Forcing for Efficient Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22347)
![architecture](https://img.shields.io/badge/Speculative_Forcing-red)
![task](https://img.shields.io/badge/Efficient_Autoregressive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1KAIST_AI,_2NAVER_AI_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**少步自回归视频生成器支持流式生成，但它们**让每个 token 都走一遍最终去噪步**，不论该 token 需要多少精修。作者发现这种统一计算往往没有必要：许多 token 在初始步就已接近其最终全步输出，而另一些……（摘要在此处截断）。**</p>

+ **Edit4D: Editable 4D Scene Generation with Textual Control**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21668)
![architecture](https://img.shields.io/badge/Background_Character_Decomposition-red)
![task](https://img.shields.io/badge/Editable_4D_Scene_Generation-magenta)
![organization](https://img.shields.io/badge/1Korea_Institute_of_Science_and_Technology_(KIST),_Republic_of_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Edit4D 是一个可编辑的文生 4D 场景生成框架，由**分离的背景与动态角色表示**构成 4D 场景。生成模型的近期进展使文本驱动的动态场景合成成为可能，但可编辑的 4D 场景生成仍具挑战（摘要在此处截断）。**</p>

+ **FeaTok: Feature-Loss Tokenization for Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22060)
![architecture](https://img.shields.io/badge/Feature_Loss_Tokenization-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/1Mila_-_Québec_AI_Institute,_2Université_de_Montréal,_3FAIR_at_Meta,_4McGill_University,_5Canada-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**离散图像生成器学习图像 tokenizer 所产生 token 的分布。这些 token 表示应当**易于被生成器建模**，而不仅仅是能忠实重建图像。然而这些 tokenizer 通常被训练来重建像素，这优先保证低保真度并可能破坏……（摘要在此处截断）。**</p>

+ **ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22328)
![architecture](https://img.shields.io/badge/Asymmetric_Conditioning_Multi_Turn-red)
![task](https://img.shields.io/badge/Multi_Turn_Image_Editing-magenta)
![organization](https://img.shields.io/badge/Tel_Aviv_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**图像编辑模型对单次编辑产出令人印象深刻的结果，但质量在多轮编辑中常**退化**。每一轮编辑引入小的分布偏移，在连续编辑中累积，从而造成编辑器原始训练所遇到的输入分布与……（摘要在此处截断）之间的差距。**</p>

+ **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21129)
![architecture](https://img.shields.io/badge/Growing_Sparsity_Sparse_Attention-red)
![task](https://img.shields.io/badge/Video_Generation_Acceleration-magenta)
![organization](https://img.shields.io/badge/1South_China_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散 transformer 主导视频生成，但因自注意力的二次复杂度而推理成本高。稀疏注意力通过跳过注意力矩阵中不必要的计算缓解这一点，但既有方法在整个去噪过程中**应用固定的稀疏率**，难以准确……（摘要在此处截断）。**</p>

+ **Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21634)
![architecture](https://img.shields.io/badge/Anchor_Based_3DGS_Representation-red)
![task](https://img.shields.io/badge/Feed_Forward_3D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/1Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期前馈 3D Gaussian Splatting 方法已能通过单次前向有效完成多视角三维重建。然而既有做法主要采用**像素对齐**范式，每输入像素预测一个 Gaussian，从而把 Gaussian 数量与输入分辨率……（摘要在此处截断）。**</p>

+ **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22370)
![architecture](https://img.shields.io/badge/Diffusion_Dynamics_Token_Merging-red)
![task](https://img.shields.io/badge/Efficient_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Hanyang_University,_South_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**token 合并已成为一种有效的免训练加速策略，通过减少冗余 token 计算来加速扩散模型，同时最小化生成退化。一个关键挑战是确定哪些 token 可以被**安全合并**、哪些应被保留用于后续计算（摘要在此处截断）。**</p>

+ **SUPRA-TEX: 3D Generation with Super-Aligned Texture**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22352)
![architecture](https://img.shields.io/badge/Super_Aligned_Texture-red)
![task](https://img.shields.io/badge/Single_Image_3D_Generation-magenta)
![organization](https://img.shields.io/badge/1Huawei_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**单图 3D 生成旨在为给定 3D 网格**赋予可重光照的材质**，同时忠实保留参考图像的视觉细节。既有方法或在融合不一致的多视角预测时引入伪影，或难以通过隐式图像特征条件化保留精细细节（摘要在此处截断）。**</p>

+ **Rethinking Classifier-Free Guidance for TI2I Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21550)
![architecture](https://img.shields.io/badge/CFG_Reassessment_TI2I-red)
![task](https://img.shields.io/badge/Image_To_Image_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/⋆Imperial_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**我们研究用于可控图像编辑的文图到图（TI2I）流匹配方法。在更广的生成建模语境下，无分类器引导（CFG）被确立为高质量输出的关键组件。然而作者论证它在 TI2I 建模中的角色被**理解不足**（摘要在此处截断）。**</p>

+ **TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21515)
![architecture](https://img.shields.io/badge/Typed_Reference_Editing-red)
![task](https://img.shields.io/badge/Humanoid_Motion_Editing-magenta)
![organization](https://img.shields.io/badge/1Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语言条件的人形运动生成让用户用自然语言创建与精修机器人动作。核心挑战是把**欠指定的请求**连接到具体的运动结构上，而这些结构随后可以相对一个已接受的参考被修订。TRACE 提出一个生成与编辑框架（摘要在此处截断）。**</p>

