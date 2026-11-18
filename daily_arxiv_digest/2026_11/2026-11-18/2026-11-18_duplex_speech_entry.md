<!-- direction: duplex_speech_core -->

+ **Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18112)
![architecture](https://img.shields.io/badge/SpheraAudio_Spatial_Multimodal_LALM-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Konoyo-014/SpheraQA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SpheraAudio 把任意通道数的复数谱压成空间 token，与音频 token 按时间位置交织后经 SMRoPE 注入注意力；在 20492 题的 SpheraQA 上整体准确率 60.18%，比 Spatial-Omni-7B 高 18.53 个百分点，坐标与轨迹类分别高 33.84 与 35.67 个点。**</p>

+ **Factorized Self-Supervised Speech Tokenization**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18898)
![architecture](https://img.shields.io/badge/Facto_Factorized_Speech_Tokenizer-red)
![task](https://img.shields.io/badge/Speech_Tokenization-magenta)
![organization](https://img.shields.io/badge/Ubisoft_La_Forge-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ubisoft/ubisoft-laforge-facto/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Facto 把自监督语音特征线性因子分解为时变部分（内容与韵律）和静态部分（说话人与录音条件），只对时变空间做 k-means 聚类得到单层 8192 码本；噪声扰动下单位编辑距离比基线低约 50%，Seed-TTS test-en 上 WER 2.7%、SIM 0.94、MUSHRA 参考相似度 78.7±2.3。**</p>

+ **Decode Early, Verify Late: Streaming Offline Speech Recognizers Without Accuracy Loss**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20064)
![architecture](https://img.shields.io/badge/DEVL_Draft_Commit_Streaming_ASR-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Nari_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DEVL 训练无关地把离线 ASR 变成流式服务：服务端保留逐段草稿，turn 结束时用一次前向把最新草稿与完整音频比对定稿，五个识别器上 95–100% 的终稿与离线贪心输出逐字节一致，WER 距离线不超过 0.13 个点，单流终稿提前 1.5–7.3 倍到达。**</p>

+ **VoxMel TTS Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20254)
![architecture](https://img.shields.io/badge/VoxMel_Haar_Factorized_Mel_TTS-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Shanghai_Innovation_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://voxdance.github.io/voxmel-demo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VoxMel 用固定且严格可逆的双轴 Haar 变换把 mel 谱拆成频率残差与粗 mel，再把粗 mel 沿时间拆出时间残差，自回归语言模型只生成粗 mel、两级非自回归残差层补细节；0.6B 模型在 100K 小时 Emilia 上取得 test-en 1.51% WER，GRPO 后进一步到 1.15%。**</p>

+ **DuoFlow: Towards Synchronized Speech and Motion Generation with Fine-Grained Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21530)
![architecture](https://img.shields.io/badge/DuoFlow_Dual_Stream_Flow_Transformer-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DuoFlow 用双流潜空间 flow transformer 在共享噪声级与统一秒级时间轴上联合去噪语音与全身动作，配套的 MotionSpeech 基准有 34950 段、约 125.2 小时并带两级动作与语音风格描述；WER 4.71%、说话人相似度 0.94、L1/L2 指令遵循率 87.43% 与 90.40%。**</p>

+ **ProSing: Zero-Shot Fine-Grained Singing Technique Conversion**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19223)
![architecture](https://img.shields.io/badge/ProSing_Paired_Technique_Conditioning-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://howardguan24.github.io/prosing-demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ProSing 在预训练 flow-matching 声学模型上加帧级技巧条件，用同一段演唱的配对版本消除条件捷径，实现零样本细粒度歌声技巧转换；N-MOS 3.36 对 TCSinger 1.48 与 Vevo1.5 2.41，CER 降到 27.6%，音高轨迹条件把音高技巧 F1 从 0.097 提到 0.162。**</p>

+ **ProTTS: End-to-End Prominence-aware Natural and Controllable Text-to-Speech via Automatic Word Stress Discovery**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19832)
![architecture](https://img.shields.io/badge/ProTTS_Clustering_Head_Variance_Adaptor-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/IIIT_Hyderabad-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ProTTS 在 FastSpeech2 的方差适配器里加聚类头，从聚合的长短音高能量时长特征中自动发现词重音，再由强调方差预测器改写重音词的音高、能量与时长，全程无需重音标注；MOS 3.96 对基线 3.12、偏好率 83.5%，ISLE 德语与意大利语 L2 的重音 F1 达 0.839 与 0.861。**</p>

+ **Sada-ASR: A Production Multidialectal Arabic Speech Recognition System**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19512)
![architecture](https://img.shields.io/badge/Sada_ASR_Encoder_Decoder_Recognizer-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/EchoNova_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/echonova-ai-solutions/arabic-asr-benchmark)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Sada-ASR 是 EchoNova 生产阿拉伯语音 agent 的识别器，用自有标注加网页弱标注双路数据训练；120 小时、53597 条测试集 WER 11.69%、CER 4.76% 为 12 系统最低，较 MAI-Transcribe-2 相对降 13.5%，六个公开集平均 WER 17.17%，开源 20 小时子集。**</p>

<!-- direction: speech_rl -->

+ **Rethinking Post-Training for Expressive Zero-Shot Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19787)
![architecture](https://img.shields.io/badge/DPO_GSPO_OPSD_TTS_Pipeline-red)
![task](https://img.shields.io/badge/RL_for_TTS-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://hujingbin1.github.io/TTS-Post-Train/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把零样本语音克隆重述为文本自适应韵律合成后，用 DPO 冷启动、GSPO 多目标强化、OPSD 自蒸馏三阶段后训练 Qwen3-TTS：情感分 18.5 提到 81.2、副语言分 38.4 提到 73.9，弱参考下 ABX 偏好 67.4% 对 25.7%，代价是英文说话人相似度从 0.72 降到 0.59。**</p>

