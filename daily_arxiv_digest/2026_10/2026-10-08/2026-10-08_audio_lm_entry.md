+ **Dialect-Robust Speech Language Models with Synthetic Pseudo-Dialect Augmentation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09321)
![architecture](https://img.shields.io/badge/Synthetic_Pseudo_Dialect_Augmentation-red)
![task](https://img.shields.io/badge/Speech_Language_Model-magenta)
![organization](https://img.shields.io/badge/∗SB_Intuitions,_†Waseda_University,_Tokyo,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音语言模型在方言上因数据稀缺而性能下降。常规 TTS 增强难以覆盖多样方言，因为它需要一定量的真实方言语音。作者改为合成伪方言语音：把 LLM 生成的方言文本经标准语言 TTS 模型转换。**</p>

+ **TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09408)
![architecture](https://img.shields.io/badge/Audio_Visual_LLM-red)
![task](https://img.shields.io/badge/Audio_Visual_Temporal_Grounding-magenta)
![organization](https://img.shields.io/badge/1Department_of_Artificial_Intelligence,_Ewha_Womans_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**音视频多片段定位（AV-MSG）要在未剪辑视频中推理音视频证据并为查询预测多个片段。仅视觉模型忽略互补的声学线索，音视频模型又常无法校准事件数量。作者把后者称为一种特定现象。**</p>

+ **Boundary-Free Contextual Biasing: Depth-Adaptive Gating and Reading-Space Matching for Unsegmented Languages**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09467)
![architecture](https://img.shields.io/badge/Boundary_Free_Biasing_Decoder-red)
![task](https://img.shields.io/badge/Streaming_ASR_Contextual_Biasing-magenta)
![organization](https://img.shields.io/badge/R&D_Team,_Recho_Inc.,_Tokyo,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**上下文偏置让 ASR 系统在推理时获得一份期望词表，但现有方法依赖词边界，而日语与中文并不提供词边界。作者为冻结的公开 CTC 模型提出无边界偏置解码器，基于字符级 Aho-Corasick 自动机，无需训练也无需二次解码。**</p>

+ **Itgan at NADI 2026 shared task: Parameter-Efficient Whisper Adaptation for Robust, Mixed-Dialect and Code-Switched Arabic ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09934)
![architecture](https://img.shields.io/badge/LoRA_Whisper_Adaptation-red)
![task](https://img.shields.io/badge/Multilingual_Code_Switched_ASR-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Itgan 在 NADI 2026 共享任务的三个 ASR 子任务上的系统：鲁棒国家级 ASR、混合方言 ASR、突尼斯语代码切换 ASR。三者共用一个配方——Whisper + LoRA 在消费级 GPU 上适配，各由不同附加项支撑。**</p>

+ **Mitigating Accent-Language Confusion in Self-Supervised Speech Representations for Language Identification**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09486)
![architecture](https://img.shields.io/badge/Accent_Language_Disentanglement-red)
![task](https://img.shields.io/badge/Language_Identification-magenta)
![organization](https://img.shields.io/badge/1Signal_Analysis_and_Interpretation_Lab_(SAIL),_University_of_Southern_California,_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**口语语言识别（LID）目标是无论口音如何都识别目标语言，但实践中从自监督语音表征微调的 LID 模型常把口音与语言混淆，把非母语（L2）语音误判为说话者的第一语言（L1）。作者显示非母语语音的表征位于……**</p>

+ **Source-Directed Trajectory Perturbation at First-Order Cost for Domain Generalization in Speech Deepfake Detection**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10094)
![architecture](https://img.shields.io/badge/Source_Directed_Trajectory_Perturbation-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/Dept._of_Electrical_and_Electronic_Engineering,_The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音深伪检测器在测试分布不同于训练分布时精度常下降。元学习做域泛化（MLDG）用情节式的元训练/元测试划分模拟域偏移，但 MLDG 元目标只考虑一条干净的适应轨迹，且不……**</p>

+ **Backdooring Acoustic Foundation Models for Physically Realizable Triggers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09819)
![architecture](https://img.shields.io/badge/Acoustic_Backdoor-red)
![task](https://img.shields.io/badge/Acoustic_Foundation_Model_Security-magenta)
![organization](https://img.shields.io/badge/Tel_Aviv_University,_Tel_Aviv,_Israel-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**声学基础模型让语音识别到说话人验证等任务只需极少资源即可强大，但其应用的安全性仍基本未被探索。作者提出声学基础模型后门（FAB）攻击，面向物理可实现的触发条件。**</p>

+ **DuRe-ST: Dual-Relation Spectro-Temporal Modeling for Speech Deepfake Detection**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10121)
![architecture](https://img.shields.io/badge/Dual_Relation_Graph_Filtering-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University,_Hong_Kong_SAR-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**既有语音深伪检测器能通过图注意力自适应捕获谱时依赖，但大体忽略了谱表示与时序表示之间的协变关系。作者从二者的联合协方差构造归一化亲和图，用多项式图滤波捕捉高阶协变。**</p>

+ **Benchmarking Adult Addressee Classification Across Child- and Adult-Directed Speech Datasets**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10240)
![architecture](https://img.shields.io/badge/Addressee_Classification_Benchmark-red)
![task](https://img.shields.io/badge/Child_Directed_Speech-magenta)
![organization](https://img.shields.io/badge/Tampere_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文对用语音数据区分儿童导向语（CDS）与成人导向语（ADS）的分类性能做了全面分析，语料包含实验室内的自然与野外 CDS/ADS。作者用自监督表征等建立了这些数据集的分类基准。**</p>

+ **CARES: A Controlled Synthetic Benchmark of Speaker Reactions to Sound**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10208)
![architecture](https://img.shields.io/badge/Controlled_Synthetic_Benchmark-red)
![task](https://img.shields.io/badge/Audio_Scene_Description-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自动音频场景描述要把录音变成一段描述情境的文本，困难之一是决定保留哪些音频元素——描述无法涵盖全部。标注者之间存在分歧，使真值难以获取。作者先定义真值，再生成数据。**</p>

