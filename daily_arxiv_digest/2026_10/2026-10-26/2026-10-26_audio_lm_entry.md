# 2026-10-26 - 音频与语音语言模型、双工语音助手 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Why Full-Duplex Speech Models Collapse in Long Conversations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32349)
![architecture](https://img.shields.io/badge/Full_Duplex_Long_Horizon_Benchmark-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工模型每帧都要出 token，几分钟就会耗尽上下文；五个模型在长对话中无一幸免。定位出「首个 KV 条目被滑窗丢弃」这一机制后，用锚点固定与重复惩罚两个免训练补丁大幅缓解崩溃。**</p>
+ **CounselPlex: A Stressor-Aware Full-Duplex Counseling Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32702)
![architecture](https://img.shields.io/badge/Stressor_State_Prompting-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出「压力源盲视」失败模式：全双工模型只看最新一句话，丢掉来访者的核心困扰。CounselPlex 在静默期更新短 stressor 状态、倾听期注入 <PAD>，并用 RPSA 拓宽位置覆盖。**</p>
+ **Uni-Stream: A Unified Streaming Speech Language Model for Speech Synthesis and Recognition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32187)
![architecture](https://img.shields.io/badge/Streaming_Speech_LM-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**统一的流式语音语言模型，两阶段训练即在识别与合成两个方向都追平专用模型；表征分析发现即使架构统一，语音与文本仍住在不同隐特征空间。公开转写与词级时间戳。**</p>
+ **DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32214)
![architecture](https://img.shields.io/badge/Latency_LoRA_Self_Distillation-red)
![task](https://img.shields.io/badge/Speech_to_Speech-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 lookahead 自蒸馏而非奖励来学推理期时延控制，无需成对目标数据；跨多个档位联合训练单个 LoRA 适配器，仅 10 小时源语音即可获得可调的时延-质量权衡。**</p>
+ **MusicTwins: Training Audio-Language Models to Listen like Their Persona**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32495)
![architecture](https://img.shields.io/badge/Persona_Conditioned_Post_Training-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Bryel_Labs_UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把人格摘要、个人记忆与后训练结合，让音频语言模型「像某个人一样听音乐」；SFT 加 RL 后训练 Audio Flamingo Next，10 个留出人格上的一致性（个性、文风、对音乐的反应）显著提升。**</p>
+ **SURE-Tagger: Structured Speech Representations for Compositional Evaluation and Targeted Data Selection**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32198)
![architecture](https://img.shields.io/badge/Structured_Speech_Tagging-red)
![task](https://img.shields.io/badge/Audio_Captioning-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University_X-LANCE_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把语音描述从自由文本变成带属性值、可弃权的半结构化标签；29 维评测中真实语音拿下 25 维最高分，并用该表示做数据选择，在一小时微调预算下把 ASR 错误率相对降低 14.3%。**</p>
+ **RVG-Bench: A Benchmark for Reasoning-Driven Audio-Visual Temporal Grounding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32268)
![architecture](https://img.shields.io/badge/Reasoning_Grounding_Benchmark-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/AIM3_Lab_Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**要求先推理意图再定位片段的视听时序定位基准，1255 个视频、1890 个查询区间对、八种推理类型；22 个模型中最强的 Qwen3.8-Omni-Flash 也只有 49.6 mIoU。**</p>
+ **Concentrated Causal Influence, Distributed Diagnostic Information: Cognitive Impairment Decisions in Large Audio-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32061)
![architecture](https://img.shields.io/badge/CI_Contrast_Neurons-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Johns_Hopkins_University_CLSP-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用类别对比激活频率选出认知障碍对比神经元并做因果干预：消融少量神经元即造成类定向预测偏移；但冻结表征的线性读出 AUC（0.92–0.97）远高于模型自身答案（0.67–0.84），随机读出同样能达到。**</p>
+ **CoupleFlow: Null-Calibrated Auditory Attention Decoding With Time-Locked Brain-Speech Coupling and Flow-Matching Likelihood Ratios**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32950)
![architecture](https://img.shields.io/badge/Conditional_Flow_Matching_Decoder-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/The_Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出「1 秒 EEG 近 100% 准确」的解码器实际用的是试次泄漏、视线与声学线索；提出脑-声时间耦合加流匹配似然比判据，无耦合时预测恒为随机，并给出证据累积定律。**</p>
+ **Sounding Surgical Instrument Localisation through Audio-Visual Correspondence**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32816)
![architecture](https://img.shields.io/badge/Weakly_Supervised_AV_Localization-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_Hospital_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用单麦克风加单相机、靠图像与声音的共现关系，在无位置标注下定位正在发声的手术器械；换用不同相机与麦克风的独立语料仍能正确定位并区分静音与背景噪声。**</p>
