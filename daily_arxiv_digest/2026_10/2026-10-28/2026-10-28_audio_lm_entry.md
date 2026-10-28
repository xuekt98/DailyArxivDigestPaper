# 2026-10-28 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **S3-S2ST: Semantically Supervised Streaming Speech-to-Speech Translation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36777)
![architecture](https://img.shields.io/badge/S3_S2ST_Thinker_Commit_Policy-red)
![task](https://img.shields.io/badge/Speech_to_Speech-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向流式语音翻译的核心难题是「何时开口」：S3-S2ST 把话语级语音对转成增量样例，用 MLP 的 READ/WRITE 策略学习提交时机并以可调阈值在 640 ms 网格上控制质量-延迟权衡，在 FLEURS 英译中有竞争力、内部 9 语言对测试集领先并计划开源模型与代码。**</p>
+ **Tap2Listen: Instant Target Switching for Streaming Audio-Visual Speaker Extraction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36643)
![architecture](https://img.shields.io/badge/Tap2Listen_Target_Agnostic_Encoder-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Sungkyunkwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向流式音视频目标说话人抽取的即时切换：Tap2Listen 把计算按模态切分，与目标无关的音频编码器只处理混合信号、目标相关视觉线索只条件化解码器，使一次切换仅需 0.12 ms 重投影立即生效，在 LRS3-2mix 上把 SI-SNRi 从 8.85 提到 9.68 dB 且可在单 CPU 核实时运行。**</p>
+ **From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36713)
![architecture](https://img.shields.io/badge/EvoSpeakerMem_Online_Speaker_Memory-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong,_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**主张「声纹是关于身份的观测而非身份本身」，据此提出在线说话人记忆构建 EvoSpeakerMem：免训练地做因果说话人路由、选择性声学状态更新与按身份分区的记忆写入检索，并建隐藏身份的 LoCoMo-ID 基准；在未见说话人上把攻击者 EER 从 2.8% 提到 26.3%，且无错误跨用户授权。**</p>
+ **Developing a Speech Language Model for Basque**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36911)
![architecture](https://img.shields.io/badge/Basque_SLM_LLaMA_Omni-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/University_of_the_Basque_Country_(UPV/EHU)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个公开的巴斯克语语音语言模型：基于 LLaMA-Omni 以 Latxa 为骨干微调多个模块迁移语言能力到语音模态，并用英文 VoiceAssistant-400K 翻译后经巴斯克语 TTS 合成音频补足数据缺失，取得内容质量 3.86/5、9.94% WER 与 3.07 UTMOS。**</p>
+ **Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37605)
![architecture](https://img.shields.io/badge/Matched_Same_Class_Controls_Audio-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_(Guangzhou)-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/huaruoji/beyond-answer-changes)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为区分音频语言模型是「听到事件类别」还是「对波形改写敏感」，设计配对的同类与异类替换对照（相同区间、电平、供体拟合与交叉淡化，仅类别不同）：在 600 个合成声景、三个模型上，异类替换引发的答案变化比同类多 49.7–60.9 个百分点。**</p>
+ **A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36834)
![architecture](https://img.shields.io/badge/Dual_Branch_Visual_Frontend_AVTSE-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对轻量分离骨干中视觉编码占用过高算力的问题，提出按空间特性分层的双分支视觉前端：紧凑唇部 ROI 用卷积建模局部发音线索、面部关键点用轻量时序卷积表示全局几何运动，在 LRS3-2mix 上把视觉编码计算量相对 ResNet18 降低 90% 以上而性能仅适度下降。**</p>
+ **Agentic Data Sampling Framework for Multilingual ASR via Linguistic-Aware Error-Driven Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36538)
![architecture](https://img.shields.io/badge/Linguistic_Aware_Agentic_Sampling_ASR-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把数据采样 LLM agent 引入多语种 ASR 训练循环，按当前错误分布决定下一批该训什么，在 12 个 Common Voice 语言上以相同累积训练预算超过不采样与随机采样基线，且用更少数据与更低算力取得优于全量训练的效果。**</p>
+ **Lipi-Ghor: A Large-Scale, Diarized, Multi-Domain Bengali Speech Corpus and a Scalable Pipeline for Building It**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36184)
![architecture](https://img.shields.io/badge/Lipi_Ghor_Bengali_Diarized_Corpus-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Khulna_University_of_Engineering_&_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**885 小时弱监督孟加拉语语音语料 Lipi-Ghor：来自 998 个 YouTube 视频与 596 个频道、覆盖 17 个领域，以 SSTT 格式标注说话人、转写与时间戳；发布可复现的语料构建流水线、四模型零样本与微调基线，以及 17 名标注者 30 小时人机协同修正的黄金评测划分。**</p>
+ **EmbeddingGemma 2: Unified and Efficient Multimodal Representations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37364)
![architecture](https://img.shields.io/badge/EmbeddingGemma2_Elastic_Modality_Lm-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Google_DeepMind-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/google/embeddinggemma-2)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EmbeddingGemma 2：7.44 亿参数的通用多模态嵌入模型，把文本、图像、视频、音频及其交错组合映射到同一向量空间；以简化逐层嵌入与模态-目标递进的多阶段课程训练，在覆盖代码、图像、视频、视觉文档与音频的基准上建立新帕累托前沿，并支持按需加载模态编码器与量化。**</p>
+ **Understanding Everyday Communication Patterns, Stress, and Productivity in Hybrid Work through Egocentric Wearable Audio Sensing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37270)
![architecture](https://img.shields.io/badge/Wearable_Audio_FG_BG_Diarization-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可穿戴音频感知系统用教师-学生蒸馏把大规模语音基础模型的知识压进紧凑 ResNet，在三个第一人称语音数据集上稳定优于基线；四个月 16 人纵向部署发现办公室场景说话负荷与更高自报压力、更低生产力显著相关，而居家说话活跃度放大生产力与情感负荷。**</p>