+ **RepForcing: Representation-Space Initialization for Autoregressive Video Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20111)
![architecture](https://img.shields.io/badge/Representation_Space_Initialization-red)
![task](https://img.shields.io/badge/Autoregressive_Video_Distillation-magenta)
![organization](https://img.shields.io/badge/2Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把预训练视频扩散模型蒸馏为少步自回归生成器，通常要把学生初始化与分布匹配蒸馏（DMD）结合。一个中间 AR 教师可以提供**因果兼容**的 ODE 初始化目标，但因果兼容的目标本身并不保证高质量生成（摘要在此处截断）。**</p>

+ **Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20220)
![architecture](https://img.shields.io/badge/Glance_Forcing-red)
![task](https://img.shields.io/badge/Bidirectional_To_Autoregressive_Conversion-magenta)
![organization](https://img.shields.io/badge/1Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归生成支撑实时、因果的视频合成，是视频世界模型的骨干。当前主流方法把双向扩散模型蒸馏为因果的少步学生，但现有流程使这一转换**代价高昂**——需要离线的概率流 ODE 轨迹。**</p>

+ **BluePixel: Toward Native 4K Agentic Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.19882)
![architecture](https://img.shields.io/badge/Agentic_4K_Image_Editing-red)
![task](https://img.shields.io/badge/Agentic_Image_Editing-magenta)
![organization](https://img.shields.io/badge/1vivo_Mobile_Communication_Co.,_Ltd.,_2Nanjing_University,_3Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指令驱动的图像编辑已达原生 4K，但这类编辑器**如何训练仍未公开**，而从零预训练超出多数团队的能力。该任务本身加剧了难度：单个端到端编辑器无法做精确参数调整、无法匹敌专用专家、也无法解释用户所用的模糊指令。**</p>

+ **Speculative Sampling in Interactive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20556)
![architecture](https://img.shields.io/badge/Speculative_Sampling_Interactive_Video-red)
![task](https://img.shields.io/badge/Interactive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/2The_Chinese_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**交互式视频生成通常依赖小的双向块以降低响应延迟。然而作者的初步实验显示：**更大的块提升视频质量**且更好地利用 GPU 并行性，使更多 latent 得以采样而采样时间仅小幅增加。**</p>

+ **Are We Overthinking One-Step Generation?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20331)
![architecture](https://img.shields.io/badge/One_Step_Generation_Reassessment-red)
![task](https://img.shields.io/badge/One_Step_Generation-magenta)
![organization](https://img.shields.io/badge/1Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散与流匹配已成为连续域生成建模的主流框架，但它们在推理时通常需要多次网络评估。这促使了大量关于一步生成建模的研究，主要建立在扩散与流之上，然而既有方法往往依赖复杂的训练机制。**</p>

+ **Self-Conditioning Enables Deep Sequential Reasoning in Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.19628)
![architecture](https://img.shields.io/badge/Self_Conditioned_Flow_Reasoning-red)
![task](https://img.shields.io/badge/Visual_Reasoning_Generation-magenta)
![organization](https://img.shields.io/badge/1Shanghai_Qi_Zhi_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期工作探索通过图像生成进行视觉推理——模型直接生成解题图像。直觉上，诸如流匹配这类迭代采样器很适合该任务，因为每个采样步可能类似一个推理步。然而本文从**电路复杂度**角度出发（摘要在此处截断）。**</p>

+ **RDCompGS: Rate-Distortion Optimization for Compression of 3D Gaussian Splatting with Image Codecs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.19538)
![architecture](https://img.shields.io/badge/Rate_Distortion_3DGS_Compression-red)
![task](https://img.shields.io/badge/Gaussian_Splatting_Compression-magenta)
![organization](https://img.shields.io/badge/Huiping_Ren,_Shuai_Wan_and_Luqian_Bai_are_with_the_School_of_Electron--green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**3DGS 实现高质量实时新视角合成，但需要可观的存储与传输资源。把高斯属性映射到 2D 表示可用成熟图像编解码器高效压缩。然而达到可比渲染质量的高斯表示通常被当作……（后续详见正文）。**</p>

+ **DreamHMR: From Video Generation to Human Motion Modeling via Structural Focusing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20124)
![architecture](https://img.shields.io/badge/Structural_Focusing_HMR-red)
![task](https://img.shields.io/badge/Human_Mesh_Recovery-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**人体网格恢复为人体运动理解提供几何基础，但从视频中准确重建身体运动与精细手部articulation 仍具挑战性——尤其在遮挡与部分可见普遍的真实场景中。视频生成预训练提供了丰富的空间与时间先验（摘要在此处截断）。**</p>

+ **Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20571)
![architecture](https://img.shields.io/badge/World_State_Centric_Agentic_Video-red)
![task](https://img.shields.io/badge/Agentic_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长篇 agentic 视频生成必须把剧本转换为镜头，并在**非连续请求之间**保持空间与时间一致。在镜头间传递提示或最近若干帧，无法为重访一个场景提供共享空间框架，也无法为重播早期事件提供时间索引记录。ATAS 提出世界状态为中心的框架。**</p>

+ **CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.20603)
![architecture](https://img.shields.io/badge/SKU_Main_Image_Pipeline-red)
![task](https://img.shields.io/badge/Commercial_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CommerceGen-Studio 是面向电商 SKU 的商业级主图生成端到端框架，组织为信息抽取、语义改写与多条件生成三阶段；Prompt-Eval-Refine-Loop Agent（PERL-Agent）从异构 SKU 元数据中蒸馏（摘要在此处截断）。**</p>

