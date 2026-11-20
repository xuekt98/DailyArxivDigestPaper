<!-- direction: duplex_speech_core -->

+ **Duopra: From Full-Duplex Conversation to Full-Duplex Agency**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25773)
![architecture](https://img.shields.io/badge/Duopra_Three_Stage_Full_Duplex-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Duopra 在 RV-Audio 上把全双工对话模型从「会聊天」推到「会办事」：后端被包装成 query(task) 工具，用协议 SFT、Dr. GRPO 全双工 RL 与仅投影器修复三阶段训练，同一 Qwen3-8B 后端下 FDB v3 的 Pass@1 从 4.7% 升至 44.7%。**</p>

+ **Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25503)
![architecture](https://img.shields.io/badge/Source_Aware_Codec_Interleaved_LM-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Institute_of_New_Media_and_Communications_Department_of_Electrical_and_Computer_Engineering_Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**源感知神经音频编解码器从混合录音中抽出时间对齐的语音与环境双 token 流，预训练 LLM 以交错自回归方式生成二者；混单 token 目标 WER 为 11.33%，改为分离表示后降到 6.43%，真实场景适配后 CLAP 升到 0.264。**</p>

+ **UMelCodec: An Ultra-Low-Bitrate and Lightweight Mel-Domain Neural Speech Codec**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25569)
![architecture](https://img.shields.io/badge/UMelCodec_Two_Stage_Mel_Codec-red)
![task](https://img.shields.io/badge/Neural_Audio_Codec-magenta)
![organization](https://img.shields.io/badge/National_Engineering_Research_Center_of_Speech_and_Language_Information_Processing_University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://redmist328.github.io/UMelCodecdemo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UMelCodec 用 AF-SC 骨干、因子化单码本 VQ 与 MSMD 判别器在 mel 域做 325 bps 纯声学编码，再由轻量 MDCT 声码器还原波形；仅 19.67 M 参数、1.93 G MACs，GPU 达 156.37 倍实时，test-clean 的 ViSQOL 为 3.80。**</p>

+ **When Sounds Turn Heads: Recovering Event Timing That Audio LLMs Fail to Say**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25960)
![architecture](https://img.shields.io/badge/Head_Guided_Decoding_Audio_LLM-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**音频 LLM 常「听得到却说不出来」时间点：该文用 query-following 选出 8 个跟踪被查询声音的注意力头，以 head prior 无需训练地重打分候选时间戳，在 RealDESED 上把录音级 mIoU 从 0.07–0.36 提升到 0.48–0.56。**</p>

+ **Xing-Audio-NVVASR: Scaling and Refining Supervision for Joint Recognition of Speech and Non-Verbal Vocalizations**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26000)
![architecture](https://img.shields.io/badge/Cross_Audit_Supervision_NVV_ASR-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Xingchen_AGI_Lab_China_Telecom_Artificial_Intelligence_Technology_Co._Ltd-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Xing-Audio-NVVASR 用交叉审计加全语料呼吸筛选迭代五轮，把 17 万条公开语料标注打磨、新增 63 万条挖掘语料，凑出约 80 万条训练 1.7B 模型；四套人标基准复合分均值 64.46，超过次强对手 6.03 分。**</p>

