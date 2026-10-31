# 2026-10-30 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Streaming Speech Recognition on a Microcontroller: a 65.7M-Parameter Transducer in 2 and 4 Bits on the ESP32-P4**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38739)
![architecture](https://img.shields.io/badge/ESP32_PIE_Quantized_Kroko_Transducer-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_Houari_Boumediene_(USTHB)-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/BoumedineBillal/esp32-pie-asr)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 6570 万参数的流式 Zipformer2 transducer Kroko 跑在没有 NPU 的 ESP32-P4 上，用 Hadamard 旋转分组加 GPTQ 做 2/4 bit 量化把权重压到 26.65 MB，LibriSpeech test-clean WER 为 4.34%。**</p>
+ **Towards Multilingual End-of-Turn Detection using Frozen Speech Encoders**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39755)
![architecture](https://img.shields.io/badge/Frozen_Encoder_EoT_Head-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Uniphore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在冻结的多语语音编码器上只训练一个小检测头来做端到端检测，在五种 CALLHOME 语言上验证零样本迁移可行、声调语言之间同样有效，且少量目标语言音频即可补回几乎全部性能损失。**</p>
+ **The Importance of Speech Genre for End-of-Turn Detector Training**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39742)
![architecture](https://img.shields.io/badge/Genre_Matched_ConvLSTM_EoT-red)
![task](https://img.shields.io/badge/Real_Time_Speech-magenta)
![organization](https://img.shields.io/badge/Uniphore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用同一标注流程构造对话式与单人机式配对语料，只让训练体裁成为变量，同一流式 ConvLSTM 端到端检测器在对话式语料上 F1 最高提升 0.45，收益主要来自更少的话语中停顿误报。**</p>
+ **Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38960)
![architecture](https://img.shields.io/badge/TwoTool_OmniModal_Agent-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/University_of_Edinburgh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文从专用工具版 OmniAgent 出发，通过分阶段受控实验剪枝工具集并把模态专用工具合并为 omni-modal 工具，最终得到只含 captioning 与 QA 的双工具智能体，在三个 AVQA 基准上准确率持平或更好且推理成本降低约 70%。**</p>
+ **How Architecture, Typology, and Adaptation Strategies Shape ASR for Low-Resource African Languages: A Controlled Empirical Study**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39004)
![architecture](https://img.shields.io/badge/LowResource_ASR_Architecture_Typology_Study-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Microsoft_Research_Africa-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在五种低资源非洲语言与斯瓦希里语上统一微调 Phi-4-multimodal、Whisper-large-v3-turbo 与 MMS-1B-all，比较数据充分性、单语多语适配、领域微调与语言适配器迁移，给出实用的数据效率目标。**</p>
+ **SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39828)
![architecture](https://img.shields.io/badge/SpeakerTurn_Reference_Conditioned_Turn_LLM-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Tianjin_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 SpeakerTurn，从语音混合加独立目标说话人参考联合预测目标转写与轮次状态，区分完整、不完整、附和、等待与目标缺席五类并单设打断任务，合成多说话人测试集上宏 F1 为 0.811、转写 CER 为 4.20%。**</p>
+ **Wav2Aug: A Drop-In Speech Augmentation Policy**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38656)
![architecture](https://img.shields.io/badge/Wav2Aug_Waveform_Augmentation_Policy-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/Concordia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出波形域即插即用的增强策略 Wav2Aug，从校准过的波形变换池随机采样两种增强并一次校准全局复用，在十个语音基准上 ASR 表现持平而非 ASR 任务平均相对误差降低 12.8%，双视图训练再提升 19.6%。**</p>
+ **Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39301)
![architecture](https://img.shields.io/badge/Youtu_Omni_Encoder_OmniSchema-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Tencent_Cloud_ADP_(Youtu-Parsing-Omni_Team)-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/TencentCloudADP/youtu-parsing)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Youtu-Parsing-Omni 用共享编码器与统一 schema 解析文档、图像、音频与视频，靠自演化的 OmniSchema-Aware On-Policy Distillation 统一十类任务，单个 50 亿参数 checkpoint 在 OmniParsingBench 上取得 75.08 平均分。**</p>
+ **Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End Inline Audio Descriptions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39955)
![architecture](https://img.shields.io/badge/MTG_AD_Inline_Description_Eval-red)
![task](https://img.shields.io/badge/Audio_Captioning-magenta)
![organization](https://img.shields.io/badge/Google_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://hf.co/datasets/google/mind-the-gap-inline-ad)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文发布 36 小时、433 个专业标注视频共 8 千余条描述的 MTG-AD 数据集，并提出 MTG-AD-Eval 评测框架，把生成脚本文本渲染回音轨以检验是否落入原视频静音区间，还验证了自动指标与 7 名盲障用户评分显著相关。**</p>
+ **AVPS-360: A Spatial Audio-Visual Benchmark for Instance Segmentation and Tracking of Sound-Producing Persons**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40480)
![architecture](https://img.shields.io/badge/AVPS360_Spatial_AVIS_Benchmark-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Audio_Research_Group,_Tampere_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AVPS-360 在 STARSS23 基础上把一阶 Ambisonics 音频与 360 度视频配对，覆盖 230 段录音共 10.5 小时，提供 31,678 个人工审核实例掩码并关联声源身份与声音事件标签，实验显示既有 AVIS 方法在长录音间歇发声上难以应付。**</p>
