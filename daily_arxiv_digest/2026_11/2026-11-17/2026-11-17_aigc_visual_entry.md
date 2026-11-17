<!-- direction: aigc_generation -->

+ **Split-and-scale Latent 3D Representations**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16126)
![architecture](https://img.shields.io/badge/Split_And_Scale_3D_Latent-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把预训练 3D tokenizer 切块复用到场景子区域，训练峰值显存 73.51GB 即可，推理端扩到 131072 个 latent 后 32768 token 的 LPIPS 降到 0.091，并配自回归体素 flow matching 生成器。**</p>

+ **Structural Self-Teaching for Compositional Generation in Unified Multimodal Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18261)
![architecture](https://img.shields.io/badge/Structural_Self_Teaching-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://bellos1203.github.io/sst)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**利用统一多模态模型自身理解路径的注意力图提取短语级支持掩码，训练期做短语局部对比对齐与结构脚手架、推理期零开销，GenEval2 上四个骨干的几何均值全面超过同数据 LoRA 微调。**</p>

+ **JVT: Just Video Transformer makes pixel-space video diffusion simple**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18549)
![architecture](https://img.shields.io/badge/JVT_Pixel_Space_Video_DiT-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://zhoutimemachine.github.io/JVT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**无预训练自编码器、无级联、无 U-Net 跳连的像素空间视频 DiT，UCF-101 类条件 FVD@2048 达 136.5、register guidance 后 129.2，并能联合生成像素对齐的 RGB-视差以提升相机跟随精度。**</p>

+ **Restoring Diversity in Distilled Image and Video Generators by Probing Activations**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18550)
![architecture](https://img.shields.io/badge/ReDiverse_Activation_Steering-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_at_Urbana-Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**探针发现少步蒸馏学生模型并非「方差丢失」而是「方向塌缩」：总方差反超教师 1.03–2.92 倍，参与比只剩 37%–60%，据此提出训练无关与轻量微调两条恢复多样性的路径。**</p>

+ **Role-Separated Diffusion Transformers: Global Rule Isolation and Deterministic Sampling Manifold Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19009)
![architecture](https://img.shields.io/badge/Role_Separated_Diffusion_Transformer-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Missouri-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把全局规则从图像 token 剥离到 12 个 controller token 并让 adaLN 按 controller 指令计算，ImageNet 256×256 上 L/2 以 458M 参数取得 15.34 FID，优于 675M 参数的 SiT-XL/2。**</p>

+ **Elliptic Sampling: Optimal Interpolant Schedules for Gaussians and Beyond**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18542)
![architecture](https://img.shields.io/badge/Elliptic_Interpolant_Schedule-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Laboratory_for_Information_and_Decision_Systems_LIDS-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**由概率流 ODE 轨迹的解析性出发联合设计插值调度与离散化，得到 Jacobi 椭圆函数参数化的保方差椭圆调度与 Zoloflow 采样器，在高斯目标上达到所有 oblivious score-span 算法的 minimax 最优。**</p>

+ **Sprint3D: Accelerating End-to-End 3D Asset Generation through Pipeline Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16701)
![architecture](https://img.shields.io/badge/Sprint3D_Pipeline_Optimization-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Alaya_Lab-green)
[![project](https://img.shields.io/badge/project-blue)](https://alaya-lab.github.io/sprint3d/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**剖析开源 Pixal3D 流水线后把 mesh 后处理搬到 GPU 并移出关键路径，再把 76 次网络评估蒸馏到 8 次，单资产中位耗时从 133.0 秒降到 4.05 秒，2,653 个 Toys4K 留出对象上指标全面改善。**</p>

+ **Kosmo-GFM: A Production-Ready Geometry Foundation Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16840)
![architecture](https://img.shields.io/badge/Kosmo_GFM_PoseEngine-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Kosmo_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://kosmoresearch.github.io/Kosmo-GFM/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**几何基础模型 GFM 一次预测相机、深度、跨视图对应与动态 3D 点，PoseEngine 再做几何优化给出场景级位姿与几何，位姿 AUC 在 1°/3°/5° 阈值下领先，累计 14.07 小时约为 GLUEMAP 的五分之一。**</p>

+ **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17930)
![architecture](https://img.shields.io/badge/Token2Tile_Sparse_Attention-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**训练无关的稀疏注意力算子，逐 query 打分后按 query 簇合并选择并打包成 GPU tile 执行，在 MiniMax-H3 与 Wan2.1-14B 上取得 1.48–1.54× 端到端加速且 VBench 几乎不掉分。**</p>

+ **TelePhysica: Agentic Reconstruction of Physically Interactive Scenes**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18078)
![architecture](https://img.shields.io/badge/TelePhysica_ClosedLoop_World-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/Institute_of_Artificial_Intelligence_China_Telecom_TeleAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://interactive4d.vercel.app/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视觉-语言编码 agent 在轮廓批评与零力平衡预检两级闭环里生成可执行物理场景程序，统一求解器耦合刚体、连杆、布料与四面体弹性体并把模拟轨迹喂给视频扩散模型，平衡验证率从 0% 升到 81%。**</p>

<!-- direction: aigc_editing -->

+ **ATune: Unsupervised Photo Retouching Through Image-Editor Controls**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16236)
![architecture](https://img.shields.io/badge/ATune_Attribute_Retouching-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把修图学成 13 个可测属性的声明式目标，再交由 RawTherapee 或 darktable 搜索滑块落地；54M 参数用 10M 无配对商用图训练，157 人 9,253 次二选一中 54.3% 胜过 GPT-6 Astra、与 Claude Opus 5 持平。**</p>

+ **DecoEdit: Beyond Flat Control for 3D-Aware Unified Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19121)
![architecture](https://img.shields.io/badge/DecoEdit_Decoupled_Pipeline-red)
![task](https://img.shields.io/badge/3D_Editing-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 1D 文本、2D 空间与 3D 体量控制统一进一个编辑器，用 SAM-3D 结构渲染锚定几何与朝向、另设细节通路保纹理，DecoBench 261 例上宏平均 8.97 并在人类排名中居首。**</p>

+ **Consistent Video-to-Video Translation via Explicit Correspondences**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17298)
![architecture](https://img.shields.io/badge/Correspondence_CrossAttention_Memory-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://www.cs.cmu.edu/~vid2vid-long/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用输入视频的 patch 级对应关系去检索此前已生成输出的对应区域，再经 correspondence cross-attention 注入，在不加长因果窗口的前提下保住长程一致性，LongLive 上 LPIPS 下降 47%、DreamSim 下降 74%。**</p>

+ **Open Vision Banana: A Fully Open Recipe for Generative Visual Perception**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15844)
![architecture](https://img.shields.io/badge/Open_Vision_Banana-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Fundamental_AI_Lab_University_of_Technology_Nuremberg-green)
[![project](https://img.shields.io/badge/project-blue)](https://openvisionbanana.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把语义分割、实例分割与深度等视觉任务改写成条件图像编辑指令来训练开源生成器，零样本 Cityscapes 达 73.9 mIoU 超过 Vision Banana 的 69.9，再用测试期 legend 集成把 mIoU 最多再提 8.7 分。**</p>

<!-- direction: aigc_rl -->

+ **Mem2Fair: Online Fairness Control for Text-to-Video Generation via Fair Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19215)
![architecture](https://img.shields.io/badge/Mem2Fair_Online_Fair_Memory-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 T2V 属性级公平写成条件在线可达性问题，用概念条件化的 Fair Memory 记录已生成视频的属性分布并在线挑选提示级干预，不改权重、无需预部署采样，均匀目标下 NP 由 0.336 升到 0.917。**</p>

