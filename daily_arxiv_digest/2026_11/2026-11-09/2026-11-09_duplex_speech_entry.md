<!-- direction: duplex_speech_core -->

+ **Real-Time Short-Response Selection for Spoken Dialogue Systems**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09057)
![architecture](https://img.shields.io/badge/VAP_Contrastive_Short_Response-red)
![task](https://img.shields.io/badge/Turn_Taking-magenta)
![organization](https://img.shields.io/badge/Graduate_School_of_Engineering_Science_The_University_of_Osaka-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 CEJC 日语对话上用对比学习给轮次预测模型外挂短响应选择头，14,446 个测试事件的文本 Top-1 准确率达 15.72%，超过 LLM 基线的 7.55%，轮次时序性能几乎不受影响。**</p>

+ **AccentCanvas: Activity-Guided Bidirectional Accent Conversion**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08972)
![architecture](https://img.shields.io/badge/Activity_Guided_Discrete_Diffusion-red)
![task](https://img.shields.io/badge/Accent_Conversion-magenta)
![organization](https://img.shields.io/badge/Korea_Advanced_Institute_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://smokedindia.github.io/accentcanvas/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AccentCanvas 用共享离散扩散模型同时做口音归一化与 L1 到 L2 转换，靠帧级语音活动引导保住配音时间轴，边界误差比最佳基线低逾 73%，代价是 L1 到 L2 的 WER 升到 17.1%。**</p>

+ **Improving Large Audio-Language Model Embedding Baselines for Instruction-Aware Speech Retrieval**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09122)
![architecture](https://img.shields.io/badge/Instruction_Aware_Layer_Weighting-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lca0503/IRIS)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**IRIS-Embed 把大型音频语言模型改造成指令感知的语音检索嵌入器，用指令预测音频编码器层权重，约 90 万训练样本在 INSPIRE 上取得 62.92% 的宏平均 Recall@50，远超最强基线的 45.15%。**</p>

+ **Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09516)
![architecture](https://img.shields.io/badge/Speaker_Embedder_Benchmark-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在亚秒级实时语音代理的严格延迟预算下评测五种说话人嵌入器，发现去噪普遍抬高等错误率、截断音频一律变差，且 TitaNet 前 92 维已承载全部判别信息，验证应吃原始音频。**</p>

+ **An Effective Spoken Language Understanding Approach Leveraging Query-Adaptive Intent Detection**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09491)
![architecture](https://img.shields.io/badge/Prototype_Guided_Two_Stage_Retrieval-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**APEX 用固定意图原型先做候选意图筛选再检索示例，在 SLURP 上以 Qwen3-4B 把完整转写下的 EMA 提升 4.34 个百分点，高困惑子集上提升 7.66 个百分点，且全程无需微调。**</p>

+ **GTCRN-SS: Lightweight Causal Speech Separation with Residual Allocation and Reconstruction Refinement**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09358)
![architecture](https://img.shields.io/badge/GTCRN_SS_Residual_Allocation-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/Dept._of_Electrical_Engineering_National_Chi_Nan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GTCRN-SS 把紧凑 GTCRN 增强骨干改造为两级因果语音分离器，用内部残差汇配合重建条件精修，在含噪 Libri2Mix 上以 0.9M 参数、6.1G MACs 取得 10.1 dB SDRi。**</p>

+ **Asymmetric Correspondence Learning for Lexical and Style Embeddings: Interpreting Latent Space via Acoustic Features**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09313)
![architecture](https://img.shields.io/badge/Asymmetric_Correspondence_Learning-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_University_of_Sheffield-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**非对称对应学习把 HuBERT 特征蒸馏为声学词嵌入与声学风格嵌入两个空间，但探针近乎地板时两个空间仍按声道滤波与基频动态结构化，提示常规诊断基准不足以验证特征隔离。**</p>

+ **Fuzzy-FedAvg: Server-Aware Client Selection for Federated Speech Emotion Recognition in Heterogeneous Environments**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08818)
![architecture](https://img.shields.io/badge/Fuzzy_Q_Learning_Client_Selection-red)
![task](https://img.shields.io/badge/Speech_Emotion_Recognition-magenta)
![organization](https://img.shields.io/badge/College_of_Aeronautical_Engineering_National_University_of_Sciences_&_Technology_NUST_Islamabad-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Fuzzy-FedAvg 用模糊 Q 学习在服务器端学习客户端选择权重，并让同一组权重同时决定选谁与如何聚合，在 IEMOCAP 与 CREMA-D 强非独立同分布下全面超过 FedAvg，累计训练时间减少 81.2%。**</p>

+ **FoleyForge: Free-form, Controllable, Rectified-flow Editing of Sound Effects**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08695)
![architecture](https://img.shields.io/badge/Sequence_Prepend_Rectified_Flow-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Adobe-green)
[![project](https://img.shields.io/badge/project-blue)](https://giovana-morais.github.io/2027_icassp_foleyforge_demo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FoleyForge 用音频语言模型合成 46.4 万条编辑三元组微调整流流音频模型，以序列前置方式注入源片段并支持响度、编辑强度与包络可控，在指令跟随上达到最好水平。**</p>

<!-- direction: speech_rl -->

+ **AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09351)
![architecture](https://img.shields.io/badge/Structured_Acoustic_Plan_Generator-red)
![task](https://img.shields.io/badge/RL_for_Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Jilin_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AUTEUR 把红队测试描述表示为前景声、上下文与副语言属性构成的结构化声学计划，用 RLOO 加音频反馈优化计划生成器，在 TangoFlux 与 Kling 上分别取得 79.4% 与 95.6% 的攻击成功率。**</p>

