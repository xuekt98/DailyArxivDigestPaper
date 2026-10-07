+ **RefRoute: Decoupling Conditioning Cost from References via Compact Residual Conditioning and Spatial Routing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07720)
![architecture](https://img.shields.io/badge/Sparse_Reference_Conditioning-red)
![task](https://img.shields.io/badge/Multi_Reference_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Dartmouth_College-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多参考图生成里，参考图通常被编码成稠密视觉 token 网格并与全局注意力一起算，成本随参考数量和分辨率双涨。RefRoute 用压缩残差条件表示加空间路由同时处理表示成本与注意力开销。**</p>

+ **DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07958)
![architecture](https://img.shields.io/badge/Density_Tokenizer-red)
![task](https://img.shields.io/badge/Feed_Forward_3D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/1Yonsei_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**前馈式 3D Gaussian Splatting 用一次前向重建场景替代逐场景优化，但输入视图数一少质量就急剧下降。DensiTok 论证瓶颈在重建头之前的内部表示本身，并给出密度 token 化来补足未观测区域的证据。**</p>

+ **Two Halves are More than One: Phase-wise Velocity Distillation for Fast and High-Quality Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08070)
![architecture](https://img.shields.io/badge/Phase_Wise_Velocity_Distillation-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/1Department_of_Computing,_The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散图像生成骨干越来越大，推理成本随之上升。已有单步方法把整个前向预算全部花在一次单体学生模型评估上，而这篇指出粗到细的非齐次传输无法被单体模型单次评估逼近，于是按阶段分解速度场来分配预算。**</p>

+ **ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08779)
![architecture](https://img.shields.io/badge/First_Frame_Guided_Interactive_Editing-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/2Adobe_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**现有视频编辑器能插入物体，但插入的物体常常无法真正参与交互——不会被拿起或操纵。ALIVE 用编辑过的首帧加一条只点名新增物体的指令，并为此整理了 35,800 条编辑对。**</p>

+ **Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08772)
![architecture](https://img.shields.io/badge/Backend_Agnostic_Sparse_Attention-red)
![task](https://img.shields.io/badge/High_Resolution_Image_Generation-magenta)
![organization](https://img.shields.io/badge/1School_of_Artificial_Intelligence,_Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DiT 在图像与视频生成上表现强，但全注意力的二次复杂度让高分辨率生成很贵。窗口注意力虽省算力，孤立窗口却阻断了跨窗口交互，常常留下可见的网格状伪影。这篇给出后端无关的稀疏注意力实现。**</p>

+ **Diverse Motion Customization via Control-based Dynamic Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07911)
![architecture](https://img.shields.io/badge/Control_Based_Motion_Customization-red)
![task](https://img.shields.io/badge/Motion_Customization-magenta)
![organization](https://img.shields.io/badge/1Seoul_National_University,_2AIM_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频生成中的运动定制受制于内容泄漏：参考视频的外观属性会不受控地传播到生成结果。作者把泄漏归因于生成过程向参考视频坍缩，而坍缩又源于把学习目标写成对参考的直接回归。**</p>

+ **Disentangling Dual Image References in Frequency Aware Diffusion Models for Personalized Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07684)
![architecture](https://img.shields.io/badge/Frequency_Aware_Diffusion-red)
![task](https://img.shields.io/badge/Personalized_Image_Generation-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_and_Information_Engineering-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**个性化图像生成通常把前景当作图像定制、背景当作风格迁移，两个任务混在一次去噪里。作者观察到文本错位源于去噪过程中混合频带的纠缠，提出在频域上把两个任务解耦。**</p>

+ **4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08782)
![architecture](https://img.shields.io/badge/Conditional_Flow_Matching_4D-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/1Texas_A&M_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**4D 手-物重建以往依赖逐序列优化，生成式方法则从随机噪声合成交互，导致预测不稳定。4D-HOF 走前馈路线：用条件流匹配把视觉基础模型给出的手-物状态搬运到目标。**</p>

+ **Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08756)
![architecture](https://img.shields.io/badge/Post_Training_Semantic_Lifting-red)
![task](https://img.shields.io/badge/3D_Semantic_Segmentation-magenta)
![organization](https://img.shields.io/badge/University_of_Málaga-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**3DGS 的同一个 Gaussian 会从多个视角被看到，而这些视角对它属于哪一类的判断并不一致——可能被遮挡，检测器置信度也不同。这篇提出后训练式的语义提升，一次针对一个目标类别工作。**</p>

+ **Rethinking Visual Provenance: Detection and Watermarking Across Direct Visual Generation and LLM-Driven Code Rendering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08137)
![architecture](https://img.shields.io/badge/Provenance_Verification_Framework-red)
![task](https://img.shields.io/badge/Image_Provenance_Detection-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AI 系统生成图像有两条路径：直接用生成模型，或由 LLM 写代码描述再渲染。两条路会产生相似的视觉伪影，但暴露不同的表示、可干预位置与溯源证据。这篇以生产为中心比较了两条路上的检测与水印。**</p>

