# 2026-11-03 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02430)
![architecture](https://img.shields.io/badge/InteractionBench_Full_Duplex_Eval_Harness-red)
![task](https://img.shields.io/badge/Full_Duplex_Evaluation-magenta)
![organization](https://img.shields.io/badge/AveraLabs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**InteractionBench 用 13 个场景、每系统 221 项、1519 次评分运行，在同一批录音上同时测全双工语音系统的时序、口语任务准确率、耳语音量与长对话 groundedness，并指出 GPT-Live 去掉约 1.5 秒网络延迟后时序分从 86% 跌到 56%。**</p>
+ **Voice-Native LLMs Hear Frustration but Do Not Listen to It**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02893)
![architecture](https://img.shields.io/badge/VoxAffect_Frustration_Perception_Protocol-red)
![task](https://img.shields.io/badge/Audio_Language_Model_Analysis-magenta)
![organization](https://img.shields.io/badge/New_York_University_Abu_Dhabi-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Astarojth/hear-not-listen)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VoxAffect 用 353 任务、1412 条 clip 的措辞与声音 2x2 被试内设计，测出 8 个语音原生模型里有 7 个听得出不满的声音却不用它（标注正确率最高仅 3.1%），但线性探针能从两个开源模型编码器以 0.67 与 0.69 解码出不满。**</p>
+ **GigaSpeech 3: Scaling Multi-Dialect Arabic Speech Recognition with Weakly Labeled Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02476)
![architecture](https://img.shields.io/badge/GigaSpeech3_Weakly_Supervised_Dialect_ASR-red)
![task](https://img.shields.io/badge/Low_Resource_ASR_Data-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/speechcolab/gigaspeech3)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GigaSpeech 3 用每方言 60 小时人工转写自举出标注模型，收集 39000 小时、1000 万条弱标注阿拉伯语方言语音，方言专属模型 macro WER 23.86%、较最强第三方系统相对下降 16.6%，Zipformer 在八个外部条件下均为六个模型中 WER 最低。**</p>
+ **Omni-Life: Benchmarking Omnimodal Real-Time AI Assistants in People's Daily Lives**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02835)
![architecture](https://img.shields.io/badge/OmniLife_Real_Time_Omnimodal_Benchmark-red)
![task](https://img.shields.io/badge/Conversational_Agent_Evaluation-magenta)
![organization](https://img.shields.io/badge/Hong_Kong_Polytechnic_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/todayai-labs/omni-life)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Omni-Life 用 400 个视频（290 个需协助含 555 个介入事件、110 个要求全程沉默）与 12 种实时全模态配置评测日常助手的该说不说，至多 4.48% 视频被完全正确处理，提醒可提升 17.12 个百分点召回却带来每分钟约 4.6 次多余响应。**</p>
+ **How Much Prosody Does Your ASR Encoder Already Know**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02602)
![architecture](https://img.shields.io/badge/Zipformer_Prosody_Encoder_Representation_Probe-red)
![task](https://img.shields.io/badge/Turn_Taking_In_Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Uniphore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文在流式 Zipformer 编码器四个深度上验证手工韵律对端点检测是否还有增益：原始滤波器组上 Δbits=+0.053，一层编码器后降到 +0.021，最终层剔除说话人捷径后仅剩 ΔAUC=+0.0015，Whisper、wav2vec2 与公开 CASPER 语料均复现。**</p>
+ **R$^2$-Omni: Reducing Structural and Precision Redundancy in Omni-LLMs for Long-Form Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03247)
![architecture](https://img.shields.io/badge/R2Omni_Token_Consolidation_Precision_Allocation-red)
![task](https://img.shields.io/badge/Efficient_Audio_LLM-magenta)
![organization](https://img.shields.io/badge/InfRec_Cardinal_AI_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**R2-Omni 以免训练方式同时削减结构冗余与精度冗余：结构感知 token 合并加语义敏感度精度分配，在长文生成基准上平均显存降到基线的五分之一、保留 97.98% 生成质量并获得 1.48 倍端到端加速。**</p>
+ **Sequence-to-Sequence Refinement for EEND-VC Diarization with a Shared Encoder**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02709)
![architecture](https://img.shields.io/badge/Shared_Encoder_S2S_Diarization_Refinement-red)
![task](https://img.shields.io/badge/Speaker_Diarization-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该工作用共享编码器把 DiariZen 自监督表征接到 EEND-VC 的序列到序列精修头上，8 个域上 WavLM 冻结特征把宏平均 DER 从 12.95% 降到 12.40%、说话人混淆相对下降 17.4%，联合训练后到 11.90%，实时率代价约 15%。**</p>
+ **SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03119)
![architecture](https://img.shields.io/badge/SPATEX_Array_Flexible_MIMO_TSE-red)
![task](https://img.shields.io/badge/Target_Speaker_Extraction-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Wenanzhi/SPATEX)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPATEX 首个支持麦克风数与阵列几何可变的 MIMO 目标语音提取框架，用几何感知通道交换与共享时序注意力保持置换等变，在未见阵列上最高取得 15.98 dB SI-SNRi，相对固定阵列 MIMO 基线最多提升 3.06 dB。**</p>
+ **Maswao: An automatically collected, prepared, and benchmarked dataset for the South African Sign language**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02903)
![architecture](https://img.shields.io/badge/Maswao_SASL_Sign_To_Text_Dataset-red)
![task](https://img.shields.io/badge/Speech_To_Speech_Translation-magenta)
![organization](https://img.shields.io/badge/University_of_Pretoria-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dsfsi/maswo-south-african-sign-language-dataset)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Maswao 用南非广播新闻全自动采集并弱对齐出 2944 个手语句对的南非手语平行语料，在首个 SASL 手语转文本基准上让 AlexNet 加 Transformer 取得 BLEU-1 至 4 为 13.78、5.21、2.52、1.54，ChrF 18.09，ROUGE-L 10.51。**</p>
+ **Inner-Speech Decoding from EEG Across Three Corpora Under a Fixed Architecture and Protocol**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02180)
![architecture](https://img.shields.io/badge/VC_DATNet_Dual_Attention_Inner_Speech_Decoder-red)
![task](https://img.shields.io/badge/Speech_Brain_Computer_Interface-magenta)
![organization](https://img.shields.io/badge/American_International_University-Bangladesh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在统一预处理与被试内五折协议下，约 13.1 万参数的双注意力 Transformer 在三个公开内言语 EEG 语料上分别取得 39.48%、20.60%、25.53% 的准确率，十种解码器收敛到同一狭窄区间，瓶颈指向信号与数据规模而非模型容量。**</p>
