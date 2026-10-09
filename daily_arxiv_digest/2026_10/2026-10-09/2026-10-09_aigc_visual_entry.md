+ **Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11479)
![architecture](https://img.shields.io/badge/Conditional_Residual_Prediction-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/1The_Chinese_University_of_Hong_Kong,_Shenzhen,_2Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**因果视频扩散模型适合流式、交互与长视频生成，但标准训练下质量常低于同规模双向模型。现有做法多是初始化自或蒸馏一个预训练双向教师；这篇改为直接训练因果模型，用条件残差预测来补上双向教师本应提供的监督。**</p>

+ **WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12382)
![architecture](https://img.shields.io/badge/Decoupled_4D_Reward-red)
![task](https://img.shields.io/badge/World_Consistent_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1The_Hong_Kong_University_of_Science_and_Technology_(Guangzhou)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**忠实的视觉世界模拟要求生成视频保持 4D 世界一致性，含静态与动态两部分：静态要求静态环境跨视角的 3D 结构连贯，动态要求主体运动合理且外观随时间一致。几何感知的后训练是可行路径。**</p>

+ **Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11756)
![architecture](https://img.shields.io/badge/Memory_Forcing-red)
![task](https://img.shields.io/badge/Streaming_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1State_Key_Laboratory_for_Novel_Software_Technology,_Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散能在不对整段做双向遍历的前提下做因果视频流，但现有少步系统通常只在固定大小 KV 缓存里保留开头与最近帧。一旦事件滑出这个窗口，后续帧就无法再关注它——作者称之为中程遗忘。**</p>

+ **Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12469)
![architecture](https://img.shields.io/badge/Reward_Verified_Self_Distillation-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/1Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指令引导的图像编辑器已相当强，但继续改进仍依赖人工编辑的训练对或外部奖励模型。这类监督获取成本高，而且可能奖励「看似合理的失败」——一个逼真的输出可能根本没完成所请求的修改，或改动了本应保持不变的内容。**</p>

+ **Parametric Trajectory Distillation for Few-Step Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11498)
![architecture](https://img.shields.io/badge/Parametric_Trajectory_Distillation-red)
![task](https://img.shields.io/badge/Few_Step_Video_Generation-magenta)
![organization](https://img.shields.io/badge/3Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频扩散与流模型需要大量串行评估，生成代价高昂。少步蒸馏能降本，但造成一个容量分配问题：学生要用远少的串行计算去匹配教师的迭代生成。既有轨迹方法要求学生复现高度弯曲且长程依赖的教师转移。**</p>

+ **LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12442)
![architecture](https://img.shields.io/badge/Lifting_Free_View_Transform-red)
![task](https://img.shields.io/badge/Egocentric_Video_Generation-magenta)
![organization](https://img.shields.io/badge/GenGenAI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从单条第三人称（exocentric）录像生成第一人称视频是新视角合成中困难的特例：两个相机几乎不重叠，目标视角大部分未被观测。当前最优方法显式重建场景——估计深度、把视频提升到点云、再从第一人称相机重渲染以条件化视频扩散模型。**</p>

+ **3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11198)
![architecture](https://img.shields.io/badge/Texture_Space_Inpainting-red)
![task](https://img.shields.io/badge/3D_Gaussian_Splatting_Editing-magenta)
![organization](https://img.shields.io/badge/1Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**3D 物体移除要从重建场景中移除目标物体并补全被遮挡区域的几何与外观。既有 NeRF/3DGS 方法通常先补全 2D 图像来引导 3D 补全，但复杂的多物体布局限制了每个视角可见的上下文，使 2D 补全容易产生伪影，且跨视角补全不一致。**</p>

+ **iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11302)
![architecture](https://img.shields.io/badge/Interaction_Aware_Sparse_Attention-red)
![task](https://img.shields.io/badge/Fast_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1Hangzhou_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的稀疏注意力为 DiT 提供了实用的加速方案：估计 query-key 区域的重要性、推导稀疏掩码只计算重要候选。这必然引入近似误差，可能损害生成质量。这篇在稀疏结构与时间步之间做自适应权衡。**</p>

+ **FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11364)
![architecture](https://img.shields.io/badge/Post_Training_Invariant_Watermark-red)
![task](https://img.shields.io/badge/3DGS_Watermarking-magenta)
![organization](https://img.shields.io/badge/1Department_of_Computer_Science,_Hong_Kong_Baptist_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**训练好的 3DGS 场景以可移植参数数组的形式发布，可以在训练流水线之外被复制、剪枝、重量化或重新打包，因此所有权证据最好活在发布的参数里、并在嵌入工具消失很久之后仍可检验。既有 3DGS 水印通常把嵌入或提取与场景优化绑定。**</p>

+ **Transforming Image Editors into Video Editors** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11037)
![architecture](https://img.shields.io/badge/Image_To_Video_Editor_Adaptation-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/1ByteDance_Seed_2Johns_Hopkins_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**图像编辑系统在语义理解、视觉保真与指令遵循上已有出色表现，而视频编辑仍显著更难也更贵。这篇提出一个简单替代：不训练单体视频编辑器，而是通过锚定把强图像编辑器改造成视频编辑器。**</p>

