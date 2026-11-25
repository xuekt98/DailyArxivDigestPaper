<!-- direction: aigc_generation -->

+ **Draft Forcing: Target-guided Speculative Drafting and Learned Verifier for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30328)
![architecture](https://img.shields.io/badge/Target_Guided_Speculative_Verifier-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向自回归视频扩散提出块级投机解码：用目标模型隐藏状态引导特征级草稿，再由在线训练的特征空间验证器判定接受，在 14B Self-Forcing 目标上取得 1.63 倍 DiT 加速。**</p>

+ **CineAct: Interaction-State Agents for Playable, Branching Film Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30613)
![architecture](https://img.shields.io/badge/Interaction_State_Agent_Framework-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把长视频生成从像素续写改成显式世界状态驱动：架构师先建相机布局与场景图，逐步生成并校验目标帧再合成中间运动，多步一致性比纯像素基线高 11.4 分，分支成功率提升 30.8 分。**</p>

+ **Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31239)
![architecture](https://img.shields.io/badge/Persistent_3D_Layout_Memory-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research.nvidia.com/labs/sil/projects/lyris/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用持久点云记忆加视觉语言模型写的 3D 框布局给视频模型持续锚点，单张照片即可生成超三分钟、50 米的可控漫游，分钟级往返评测中相机误差降低 3.8 倍、回访一致性提升 22%。**</p>

+ **Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31358)
![architecture](https://img.shields.io/badge/Pixel_As_Code_Agentic_Creation-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以 Pixel as Code 统一栅格与结构化产物：图像走自回归离散视觉 token，图表网页文档走显式程序，tokenizer 在约 178K 张图上把重建 PSNR 从 26.08 提到 29.57 dB，编码解码各快 7 倍以上。**</p>

+ **BodyWeave: Native Body-Conditioned 3D Garment Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32034)
![architecture](https://img.shields.io/badge/Body_Conditioned_Garment_Geometry-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://gavin-jy.github.io/bodyweave-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用原生 3D 身体条件统一服装生成与试穿：全局身体适配器定位置、局部身体注意力细化表面、表面穿透损失抑制穿模，配套 293K 条衣人对齐观测与 114K 条同款跨身体配对。**</p>

+ **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32345)
![architecture](https://img.shields.io/badge/Low_Rank_Quantized_Feature_Cache-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频扩散的时序缓存常驻显存达每段 109-346 GiB，LRQ-Cache 用训练无关的低秩加 INT8 量化把预测型缓存压到 2.3-4.9 GiB（缩小 42-71 倍），VBench 仅下降 0.25 个百分点并能装进单张 80 GB H100。**</p>

+ **MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32462)
![architecture](https://img.shields.io/badge/Executable_Scene_Construction_Agent-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/School_of_Artificial_Intelligence_Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把多参考图构图显式化成一段可执行 Blender 程序：编码 agent 把每个场景实例绑到参考图并按指令校验几何与视角，再训练生成器照此蓝图作画，FLUX 上 DreamOmni2 总成功率提升 28.21 个百分点。**</p>

+ **One Take, Many Cameras: Audio-Grounded Shot Synthesis for Dialogue Re-Cinematography**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33147)
![architecture](https://img.shields.io/badge/Speaker_Aware_Audio_Gated_Recut-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://recinematography.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**对话场景补拍正反打的新思路：用语音驱动任意视角下的唇形，以目标帧、源视频与音频为条件生成新镜头，并用免训练的说话人感知音频门控消除替别人说话，相对 Wan 3.0 语音泄漏下降 97%。**</p>

+ **Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29850)
![architecture](https://img.shields.io/badge/Wrist_View_Synthesis_Ego2Wrist-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Yale_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://adonis-galaxy.github.io/Ego2Wrist/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从人类第一视角视频合成同步腕部视角以造机器人训练数据，在约 940 小时头戴加腕部配对录像上训练，提出免真值的手部中心跨视角一致性 HCC，四个数据集上 LPIPS 比 WorldWander 低 28%。**</p>

+ **Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29897)
![architecture](https://img.shields.io/badge/Mamba_Diffusion_Persistent_Memory-red)
![task](https://img.shields.io/badge/Motion_Generation-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://aigeeksgroup.github.io/MotionMamba2.0)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Mamba 式根-身体扩散架构结合局部注意力、可恢复循环状态与持久内容记忆实现长程可控动作生成，重定向 HiPHI 上 rollout 可达 39.52 秒，RTX 4090 上完整窗口中位延迟从 1685 毫秒降到 276 毫秒。**</p>

<!-- direction: aigc_editing -->

+ **BEND: Spectral Bregman Losses for Multi-Image Unlearning in Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30532)
![architecture](https://img.shields.io/badge/Spectral_Bregman_Unlearning-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_ETH_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把扩散遗忘的损失函数本身当成可学习对象：在 Bregman 散度族里双层拟合谱 Bregman 损失，一个模型同时擦除 48 张可验证记忆图，SSCD 0.084 优于 ReTrack 的 0.094-0.120，并保住遗忘前画质。**</p>

+ **Every Edit Its Own Budget: Per-Instruction Token Freezing for Training-Free Acceleration of Multi-Edit Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32407)
![architecture](https://img.shields.io/badge/Per_Instruction_Token_Freezing-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Technology_Delhi-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多编辑指令编辑里全局跳过阈值会先冻掉小改动，TIDE 用无平衡最优传输在编辑器自身注意力里定位每个指令片段并各给一份算力预算，在 FLUX.2 Klein 上同等速度下少丢 77% 的编辑。**</p>

+ **FireDesmoke: Fire Smoke Removal via Real Smoke Transfer and Semantic Rectification**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30057)
![architecture](https://img.shields.io/badge/Real_Smoke_Transfer_Rectifier-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/National_Yang_Ming_Chiao_Tung_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真实火烟的空间局部性是建模前提：用真实火场录像迁移烟场合成训练对，再用像素特征修正被烟污染的冻结编码器 token，在首个真实火烟配对数据集上浓烟与中烟 PSNR 各提升 3.73 与 2.63 dB。**</p>

+ **What Remains After Concept Erasure? Sparse Autoencoder Probes for Auditing Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30117)
![architecture](https://img.shields.io/badge/Sparse_Autoencoder_Concept_Audit-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Shanghai_Artificial_Intelligence_Laboratory-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 SAE-Audit 白盒审计：用共享的稀疏自编码表示找出擦除后被削弱的特征，把稀疏方向注回被编辑模型检验概念能否恢复，跨 6 种擦除方法、13 个概念与 4 个领域，物体与裸体上恢复最明显。**</p>

<!-- direction: aigc_rl -->

+ **Loupe: Reinforcing Knowledge-Intensive Video Generation Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31895)
![architecture](https://img.shields.io/badge/Rubric_Based_Credit_Video_Agent-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/DP_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://zengkaiya.github.io/Loupe/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**知识密集型视频生成的 RL 用请求派生的 rubric 给搜索与规划步骤打 step 级 credit，渲染视频前即完成强化：MiniMax-H3 总分从 32.80 提升到 70.67，完整 RBC 比 SFT 加轨迹级 GRPO 高 5.27 分。**</p>

+ **Towards a Multimodal Aesthetic Agent for Photographic Reference Grading**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32299)
![architecture](https://img.shields.io/badge/JarvisAura_Grading_Agent-red)
![task](https://img.shields.io/badge/Preference_Optimization_Visual-magenta)
![organization](https://img.shields.io/badge/Xiamen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把摄影参考调色建模为可编辑参数空间里的结构化决策，经参数锚定预训练、参考锚定微调与参考对齐 GRPO 三阶段训练，用渲染结果的多维奖励优化参数，Ref-Bench 人工成功率 74%，高出 GPT-Image-2.5 九个百分点。**</p>

+ **SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31163)
![architecture](https://img.shields.io/badge/Objective_Grounded_Prompt_Selector-red)
![task](https://img.shields.io/badge/Rejection_Sampling-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ADDAPT-ML/SPROUT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**偏好微调的算力大头是生成候选图，SPROUT 用纯文本模型预测每个 prompt 的目标梯度范数效用并按随机接受规则组批，被拒 prompt 完全不生成图，在 GenEval 上约 44% 的迭代就追平均匀采样的最终分数。**</p>

