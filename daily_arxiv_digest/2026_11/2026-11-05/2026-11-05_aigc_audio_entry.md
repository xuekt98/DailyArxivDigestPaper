# 2026-11-05 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05988)
![architecture](https://img.shields.io/badge/Trailing_Sliding_Window_Varhop-red)
![task](https://img.shields.io/badge/Video_to_Audio-magenta)
![organization](https://img.shields.io/badge/Monash_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://dalision.github.io/livefoley-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出流式因果自回归扩散的实时音画生成方案，用尾部滑窗把非因果视觉前端免训练地转成流式模块，并以统一 Varhop 框架适配不同算力预算。DeSync 达 0.48，追平离线模型。**</p>
+ **GraphSeal: Graph-Augmented Speech Deepfake Detection via Temporal-Spectral Artifact Propagation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06171)
![architecture](https://img.shields.io/badge/Temporal_Spectral_Graph_Attention-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/Pusan_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出图增强的语音伪造检测方法，在短语音片段上构建时序与谱相似度联合的动态图，经图注意力传播伪影线索再分层读出。四个基准上 EER 为 0.52%、2.41%、8.17% 与 5.24%，且前端无关。**</p>
+ **VIPBench: A Human-Aligned Benchmark for Voice Identity Perception in the Age of Voice Cloning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05638)
![architecture](https://img.shields.io/badge/Voice_Identity_Perception_Benchmark-red)
![task](https://img.shields.io/badge/Voice_Identity-magenta)
![organization](https://img.shields.io/badge/Northwestern_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/sendfuze/vipbench)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出人类对齐的语音身份感知基准 VIPBench，收录 1,290 名听众对 9,800 对录音的 124,876 次同异判断，并定义四项对齐任务。克隆语音有 41% 的回答被判为不同人，最好模型仅解释 61% 可解释方差。**</p>
+ **CLRM: Cross-Layer Relation Modeling for Audio Deepfake Detection**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05678)
![architecture](https://img.shields.io/badge/Cross_Layer_Relation_Modeling-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出跨层关系建模 CLRM，显式编码自监督编码器不同层表征之间的差异与交互，并与层内特征并列送入检测头。在 5 个外部数据集上把三个检测器的平均 EER 相对降低 7.8%-16.7%，主干保持冻结。**</p>
+ **SonoDyno: A Sonic Dynamometer for Engine Speed and Load Estimation from Audio**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06262)
![architecture](https://img.shields.io/badge/Harmonic_Order_Speed_Decoder-red)
![task](https://img.shields.io/badge/Acoustic_Measurement-magenta)
![organization](https://img.shields.io/badge/Audio_Research_&_Development_Impulse_Audio_Lab_GmbH_Munich_Germany-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出声学测功仪 SonoDyno，仅凭麦克风信号估计转速、气缸数与归一化负载强度，无需转速表或总线信息。模型仅 124,302 参数，在未知引擎上 93%-97% 的帧转速误差在 2% 内，气缸数准确率 80%。**</p>
+ **Which One Is Sounding? Binaural Sounding Instance Disambiguation for Audio-Visual Segmentation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06074)
![architecture](https://img.shields.io/badge/Binaural_Spatial_Disambiguation-red)
![task](https://img.shields.io/badge/Audio_Visual_Segmentation-magenta)
![organization](https://img.shields.io/badge/Taiyuan_University_of_Technology_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出双耳发声实例消歧方法 BiSID-AVS，用音频提示先定位类别一致候选区，再把双耳线索投影为图像平面空间响应并在特征与解码两级做空间条件。在双耳 AVS-Synthetic 与 Habitat-AVS 上实例级 mIoU 大幅领先。**</p>
+ **Cross-Modal Semantic Successive Refinement for Generative Image Communication over Underwater Acoustic Channels**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06205)
![architecture](https://img.shields.io/badge/Cross_Modal_Semantic_Refinement-red)
![task](https://img.shields.io/badge/Acoustic_Communication-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出面向水下声信道的跨模态语义逐级精修通信框架，发送端传文本、瓶颈特征与残差矢量量化视觉边信息，接收端用一步 Pixel MeanFlow 重建。10 dB 下 RVQ 增深可把 PSNR 从 26.7 提到 27.9 dB。**</p>
+ **The Hearpiece Database of Binaural Room Impulse Responses and Driver Responses on KEMAR**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06345)
![architecture](https://img.shields.io/badge/Binaural_Impulse_Response_Database-red)
![task](https://img.shields.io/badge/Acoustic_Measurement-magenta)
![organization](https://img.shields.io/badge/Carl_von_Ossietzky_Universität_Oldenburg_Germany-green)
[![project](https://img.shields.io/badge/project-blue)](https://doi.org/10.5281/zenodo.23667308)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**公开 Hearpiece 双耳房间脉冲响应数据库，记录 KEMAR 在两种佩戴配置、三种房间条件、三次独立佩戴与 24 个水平声源方向上的 BRIR，合计 4320 条脉冲响应，并附驱动响应与播放录制系统的环路响应。**</p>
+ **Drowning in Noise: On Signal Saliency in Self-Supervised Learning for Ocean Acoustics**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06725)
![architecture](https://img.shields.io/badge/Saliency_Curated_SSL_Pretraining-red)
![task](https://img.shields.io/badge/Audio_Representation_Learning-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出海洋声学中数据规模并不等于学习信号：用含动物发声的 30 小时精选片段预训练 BEATs，效果超过 1,240 小时未过滤数据，在 31 类海洋哺乳动物分类上以少 41 倍的数据取得更高准确率。**</p>
+ **Virtual Microphone Array for Direction-of-Arrival Estimation Based on Fiber-Optic Position Sensing**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06285)
![architecture](https://img.shields.io/badge/Fiber_Optic_Virtual_Array-red)
![task](https://img.shields.io/badge/Sound_Source_Localization-magenta)
![organization](https://img.shields.io/badge/Technische_Universität_Ilmenau_Germany-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出虚拟麦克风阵列方法，用光纤位置感知重建麦克风运动轨迹，构成时变阵列几何并以多双曲面交点估计来波方向。16 个声源位置中方位与俯仰分别有 13 个和 12 个的中位误差落在容差内。**</p>
