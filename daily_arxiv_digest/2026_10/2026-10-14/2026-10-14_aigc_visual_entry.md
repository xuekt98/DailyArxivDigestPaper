+ **Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14685)
![architecture](https://img.shields.io/badge/Autoregressive_Video_Rerendering-red)
![task](https://img.shields.io/badge/4D_World_Generation-magenta)
![organization](https://img.shields.io/badge/4Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频扩散的进展使从单条输入视频做 novel-view 视频合成成为可能，支撑世界建模、具身智能与机器人仿真。但既有方法**独立处理各条相机轨迹**，缺乏形成连贯可导航 4D 世界所需的跨轨迹一致性。**</p>

+ **Simplifying and Improving On-Policy Distillation for Few-Step Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.18472)
![architecture](https://img.shields.io/badge/On_Policy_Distillation_Simplification-red)
![task](https://img.shields.io/badge/Few_Step_Diffusion-magenta)
![organization](https://img.shields.io/badge/Microsoft_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**少步蒸馏降低扩散与流模型的采样成本，但既有方法常需要辅助分数模型或专用架构。作者表明**简单的在策略速度回归**已为 4-NFE 生成提供坚实基础，并引入额外机制以刻画每个粗略转移内的教师速度变化。**</p>

+ **Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.15922)
![architecture](https://img.shields.io/badge/Frequency_Step_Cache-red)
![task](https://img.shields.io/badge/Efficient_Autoregressive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/Rice_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频生成支持长时程合成，但需要在大型扩散 transformer 上反复前向。免训练缓存通过复用中间计算降低成本，然而既有控制器往往把两个决策**耦合**在一起：何时精确同步缓存，以及在两次同步之间投入多少计算去修复。**</p>

+ **Prospective Forcing: Learning to Look Ahead for Autoregressive Long Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14654)
![architecture](https://img.shields.io/badge/Multi_Head_Prospective_Prediction-red)
![task](https://img.shields.io/badge/Long_Video_Diffusion-magenta)
![organization](https://img.shields.io/badge/1Mohamed_bin_Zayed_University_of_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频生成器通过分块 rollout 合成长视频，但它们通常只被训练来预测**紧邻的**未来。这个受限的预测时程使它们难以在长时间 rollout 中保持质量。**</p>

+ **Adversarial Gradient Forcing for Robust Few-Step Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14553)
![architecture](https://img.shields.io/badge/Adversarial_Gradient_Forcing-red)
![task](https://img.shields.io/badge/Few_Step_Autoregressive_Video-magenta)
![organization](https://img.shields.io/badge/1Zhejiang_University,_2Alibaba_Group,_3Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频生成模型逐序列生成视频，每个新块以先前生成的块为条件。在模型自己的 rollout 上训练，Self Forcing 及其后续方法显著缓解了训练与推理时历史分布不匹配导致的暴露偏差。然而这些模型仍然……**</p>

+ **TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.15324)
![architecture](https://img.shields.io/badge/Predictive_KV_Quantization-red)
![task](https://img.shields.io/badge/Autoregressive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1_Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散模型支持长视频流式生成，但因 KV 缓存快速增长而有显著内存开销。既有 KV 缓存量化方法主要为 LLM 设计，迁移到视频模型效果差，因为激活用有不同的统计特性与强时空冗余。**</p>

+ **TGuide: Faster Autoregressive Video Diffusion via Historical Trajectory Guidance**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14657)
![architecture](https://img.shields.io/badge/Historical_Trajectory_Guidance-red)
![task](https://img.shields.io/badge/Fast_Autoregressive_Video_Diffusion-magenta)
![organization](https://img.shields.io/badge/3National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**当只剩四个去噪步时，自回归视频扩散还能不能再加速？既有特征缓存方法在这个区间表现挣扎，因为去噪时间步之间的特征变化很大，破坏了直接复用与轻量预测器。**</p>

+ **FrameFold: Response-Guided KV Cache Consolidation for Autoregressive Long Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14568)
![architecture](https://img.shields.io/badge/Response_Guided_KV_Consolidation-red)
![task](https://img.shields.io/badge/Long_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1ShanghaiTech_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在自回归视频生成中，保留全部历史 KV 状态会随视频变长而增加内存占用与每步注意力成本。固定缓存预算能界定这些成本，但带来了在固定预算下保留支撑一致高质量生成的历史内容这一挑战。**</p>

+ **Competition Domains Matter: Selective Head Globalization for Training-Free Sparse Attention in Video Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.14672)
![architecture](https://img.shields.io/badge/Head_Heterogeneous_Competition_Domain-red)
![task](https://img.shields.io/badge/Sparse_Attention_Efficiency-magenta)
![organization](https://img.shields.io/badge/University_of_Chinese_Academy_of_Sciences,_Beijing,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练稀疏注意力是视频扩散 transformer 推理提效的一条实用路径，但既有方法通常在每个 query 行、每个注意力头上固定竞争域。先前工作主要关注在固定域内如何估计 token 级重要性；而域本身是否应随头的异质性自适应……**</p>

+ **Look Back to Move Forward: Learning to Revisit for Agentic Compositional Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.16224)
![architecture](https://img.shields.io/badge/Agentic_Revisit-red)
![task](https://img.shields.io/badge/Compositional_Image_Generation-magenta)
![organization](https://img.shields.io/badge/NUDT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文生图模型在视觉保真与指令遵循上进展显著，但复杂组合生成仍然困难。既有 agentic 路线通过迭代生成与编辑解决这一点，依据交互历史调整动作——但它们通常固定了续写状态。**</p>

