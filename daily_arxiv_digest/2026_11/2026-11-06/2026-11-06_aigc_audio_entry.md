# 2026-11-06 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ProCraft: Instruction-Driven Music Production from Free-Form Text**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07423)
![architecture](https://img.shields.io/badge/Gated_Cross_Attn_Codec_LM-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ProCraft 用 0.5B 参数自回归编解码语言模型端到端执行自由文本音乐编辑，支持 30 秒片段上的七类操作与八类乐器，并用即时编辑对合成造训练数据，复合指令上优于四个自由文本编辑器。**</p>
+ **VoxCanvas-41M: A Large-Scale Bilingual Dataset for Instruction-Based Speech Editing and Its Learning Dynamics**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08251)
![architecture](https://img.shields.io/badge/Span_Level_Instruction_Editing-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/X-LANCE_Lab_Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://zhikangniu.github.io/voxcanvas/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VoxCanvas-41M 释出约 4100 万条中英双语语音编辑对，覆盖内容编辑与 39 类副语言事件增删，配 VoxCanvas-Edit 模型并系统梳理了数据规模与训练策略对编辑能力的影响。**</p>
+ **Adaptive and High-Fidelity Matching Algorithm for Retrieval-Based Accent Conversion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07420)
![architecture](https://img.shields.io/badge/Anisotropy_Aware_Adaptive_KNN-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/East_China_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://aa-knn-ac.github.io/demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**检索式口音转换 AA-kNN-AC 的三处改动分别针对匹配池音素覆盖不足、邻域大小固定与谱连续性差，辅以渐进式 AdaIN 解码器，仅用 100 小时通用语音训练就在 L2-ARCTIC 与 VCTK 上取得最低字错误率。**</p>
+ **FUSEMOS: Perceptual Evaluation of Text-to-Music Generation with Dual-Encoder Fusion and Ranking-Aware Composite Loss**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07562)
![architecture](https://img.shields.io/badge/CLAP_MERT_Dual_Encoder-red)
![task](https://img.shields.io/badge/Text_to_Audio-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FUSEMOS 针对文本生成音乐的感知评测，把 CLAP 与音乐自监督模型 MERT 融合以兼顾高层语义对齐和音色细节，并提出排序感知复合损失，在 MusicEval 上大幅降低整体印象与文本对齐的误差。**</p>
+ **Route-DMD: Distribution Matching Distillation with Task-Routed Mechanism for Speech Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08011)
![architecture](https://img.shields.io/badge/Task_Routed_Distribution_Matching-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/X-LANCE_Lab_Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://route-dmd.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Route-DMD 指出分布匹配目标并不适合所有语音任务，分离任务中教师对偏离分布的学生样本预测不可靠，于是按任务把分离样本路由到回归损失、其余保留解耦分布匹配，四步学生即可匹配三十二步教师。**</p>
+ **SubRoformer: Subband Time-Domain Representation for Music Source Separation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08130)
![architecture](https://img.shields.io/badge/Subband_Residual_RoFormer-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ArchiMickey/SubRoformer)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SubRoformer 用子带模块把混合信号拆成频率局部化的低采样率子带分别处理，再由残差 RoFormer 在时间压缩特征上建模时间与跨带关系，在 MUSDB18-HQ 上单模型联合分离四轨取得 11.59 dB 平均 SDR。**</p>
+ **Latent Terrain: Adapting Neural Audio Autoencoders as Design Materials in NIME**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07210)
![architecture](https://img.shields.io/badge/MLP_Latent_Space_Mapping-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Centre_for_Digital_Music_Queen_Mary_University_of_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://jasper-zheng.github.io/nn_terrain/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Latent Terrain 面向 NIME 社区提出把神经音频自编码器当作设计材料的思路，做成 Max/MSP 工具包把隐空间整形成可导航的语料声音空间，并与四位创作者协作产出带注释作品集讨论落地门槛。**</p>
+ **Design of a Speech Enhancement-Based Deep Semantic Autoencoder for Wireless Communications**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07361)
![architecture](https://img.shields.io/badge/Semantic_Noise_Decoupling_Autoencoder-red)
![task](https://img.shields.io/badge/Acoustic_Communication-magenta)
![organization](https://img.shields.io/badge/Dalian_Maritime_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音增强式深度语义自编码通信系统 S-DSA 用双分支语义编码与自适应语义噪声解耦，在低信噪比下保住目标语音语义，低 SNR 与强衰落信道上的 PESQ 与 STOI 均明显超过 CNN-AE 与 DeepSC-S 基线。**</p>
+ **Joint Higher-Order Low-Rank Tensor Decompositions for Multichannel Acoustic System Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07975)
![architecture](https://img.shields.io/badge/Joint_Block_Term_Decomposition-red)
![task](https://img.shields.io/badge/Acoustic_Measurement-magenta)
![organization](https://img.shields.io/badge/KU_Leuven-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文揭示极点-零点房间脉冲响应模型与张量低秩分解之间的对应关系，并据此设计堆叠式与联合式多通道块项分解，联合分解能在相同压缩率下把远场重构误差压到 -16 dB，且张量化阶数 3 是实用甜点。**</p>
+ **Auditory and Visual Virtualization in 6DoF XR: Effects on Plausibility and Dynamic Auditory Distance Perception**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07612)
![architecture](https://img.shields.io/badge/Real_Time_Ambisonic_Rendering-red)
![task](https://img.shields.io/badge/Acoustic_Measurement-magenta)
![organization](https://img.shields.io/badge/Aalto_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文首次从合理性与行为两个层面评估六自由度 XR 的听觉与视觉虚拟化，用实时房间声学模拟与双耳渲染搭建实验，发现 VR 中双耳渲染更可信，但任何虚拟化都会降低动态听觉距离判断的准确度并增加任务负荷。**</p>
