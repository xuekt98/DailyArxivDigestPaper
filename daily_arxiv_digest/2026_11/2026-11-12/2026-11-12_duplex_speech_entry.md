<!-- direction: duplex_speech_core -->

+ **Walrus Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13689)
![architecture](https://img.shields.io/badge/Gemma4_USM_Speech_LM-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/Sony_Group_Corporation-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sony-speech/walrus)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**索尼 Walrus 以不变的 Gemma 4 E4B 解码器骨干加 USM 编码器，在 600M 样本、20+ 任务、100+ 语言上做三阶段数据课程；CS-FLEURS 字符准确率 92.8%、LibriMix 多人 cpWER 19.32，宣称数据工程是多任务语音质量的主要驱动。**</p>

+ **Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13845)
![architecture](https://img.shields.io/badge/VoxCPM_Diffusion_TTS-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/PatientDesk_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/PatientdeskAI/freya-tr-eval-rerun)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Alania-2 是 488M 参数的土耳其语 TTS，采用 VoxCPM 扩散头架构，在 18195 小时（90% 合成）数据上从零训练；Freya-TR-Eval 上 WER 1.44%，克隆改为条件编码参考音频后跳词率由 21.9% 降至 1.7%，单流首包音频 32 ms。**</p>

+ **Earlybird: Predictive Streaming Speech Recognition in 29M Parameters**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14421)
![architecture](https://img.shields.io/badge/Moonshine_Tiny_Predictive_ASR-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/sahilmahendrakar/Earlybird-29M)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Earlybird 是 29M 参数（4 bit 权重 16.8 MB）的预测式流式识别器，从 Moonshine Tiny 裁词表后在随机截断音频上训练；LibriSpeech clean 上中位词提前 90 ms 正确输出，同批音频提前正确率 68.8%，对未说完词的期望校准误差仅 3.7 到 5.5。**</p>

+ **Emilia2: A Large-Scale Dataset for Controllable Long-Form Speech Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13614)
![architecture](https://img.shields.io/badge/Emilia2_Pipe_Longform-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong_Shenzhen-green)
[![project](https://img.shields.io/badge/project-blue)](https://charlesnii.github.io/Emilia2-demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Emilia2 是 229388 小时、41 语言的长文本可控语音生成数据集，由短句、单人长音频与多说话人对话三个视图构成；超 5 分钟样本占单人长音频 50.0%、对话 66.8%，配 23 小时 Emilia2-testset，0.6B 骨干 NAR 模型在 TTSD-Eval 中英错误率 5.27%/9.93%。**</p>

+ **Omni-JEV: Text and Dual-Stream Speech Decisions**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13777)
![architecture](https://img.shields.io/badge/MiniMindO_Dual_Stream_Thinker-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/Merit_Interactive_Research_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Omni-JEV 把全双工交互决策统一为 listen、start、continue、stop、recover 五个动作，用共享 SenseVoice 前端分别编码用户与助手参考语音；高斯 logit 版 RLCD 音频准确率 84.08%、文本 96.55%，并给出分类精度与概率质量的权衡对照。**</p>

+ **DialInstruct-TTS: Interactive Expressive Speech Generation via Multi-Turn Dialogue with Fine-Grained Temporal Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13875)
![architecture](https://img.shields.io/badge/TemporalPlan_Control_Module-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/Nara_Institute_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://anonymous.4open.science/w/eacl-demo-17C5/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DialInstruct-TTS 用 Qwen3-8B 规划器把多轮反馈折成 TemporalPlan，对冻结的流匹配 TTS 骨干做情感、语速、音量与音色的区间级控制；非目标锁定把第 5 轮非目标 mel 距离从 23.48 dB 降到 4.19 dB，人评最终偏好 29 比 1。**</p>

+ **GigaEdge Spench: An SDK for Practical Streaming Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13243)
![architecture](https://img.shields.io/badge/Shared_CPP_Enhancement_Core-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/SberDevices-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/salute-developers/gigadenoiser)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GigaEdge Spench 是跨服务器、移动端与浏览器的开源流式增强 SDK，C++ 内核支持 ONNX Runtime、TensorFlow Lite、WebAssembly；EARS-WHAM v2 上 48 kHz 混合模型 SIGMOS 提高 0.46，8 kHz INT8 模型 SI-SDR 高 1.96 dB。**</p>

+ **Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13811)
![architecture](https://img.shields.io/badge/VoxCPM2_Student_Finetuned_Vocoder-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/PatientDesk_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/cloud0day3/antalia-mini)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Antalia-2 Mini 是 7620931 参数的土耳其语 TTS，训练音频全部由约大 300 倍的 VoxCPM2 合成（约 1790 小时），在 M5 CPU 双线程上 41 倍实时；Freya-TR-Eval 上 WER 1.09%、CER 0.22%，声码器在自身 mel 上微调后 WER 降至 1.75%。**</p>

+ **AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13957)
![architecture](https://img.shields.io/badge/AVCC_NSP_Benchmark-red)
![task](https://img.shields.io/badge/Turn_Taking-magenta)
![organization](https://img.shields.io/badge/KTH_Royal_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Haotian-Qi/AVCC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AVCC 把 31 小时、单相机单麦克风录制的两三人在线对话整理成公共下一说话人预测基准，新增 7 段说话人不重叠视频、1730 个 hold 与 shift 事件与 154 人的人工参考；音频版 RoleVAP 在 hold/shift 上 66.5%，高于人类平均 64.0% 但低于多数票 70.1%。**</p>

+ **ESDCodec: Ultra-Low Bitrate Speech Codec with Enhanced Semantic Disentanglement and Subband Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14043)
![architecture](https://img.shields.io/badge/Dual_Stream_Semantic_Acoustic_Codec-red)
![task](https://img.shields.io/badge/Neural_Audio_Codec-magenta)
![organization](https://img.shields.io/badge/WeChat_Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/vspeech/ESDCodec)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ESDCodec 是腾讯的双流神经语音编解码器，用冻结随机码本加线性投影器在 0.85 kbps 下分离语义与声学，并用仅 9.6M 参数的条件网络注入子带先验；LibriSpeech test-clean 上 PESQ 2.49、ViSQOL 2.74、WER 4.18%，消融显示去掉条件网络后 WER 升到 6.38%。**</p>

+ **Nepali-English Code-Mixed Speech Recognition: Data Preparation and Adaptation of a Speech Foundation Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13512)
![architecture](https://img.shields.io/badge/SraVaani_Hybrid_TDT_CTC-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/AI_Lab_Pvt._Ltd._Nepal-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AI-Lab-Pvt-Ltd/nepali-codemixed-asr)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文用 172.8 小时、115107 条的尼泊尔语英语混合语料全量微调 449M 的 SraVaani 混合 TDT-CTC 模型，测试 WER 从 48.6% 降到 17.1%（12 轮 16.3%），与微调后 Whisper large-v3-turbo 的 16.4% 相当；冻结编码器则退化到 25.5%。**</p>

+ **Swanada: Split-Encoder Capability-Routed Conformer CTC and Sub-30 MB On-Device Speech Recognition Across Twelve Scripts**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13814)
![architecture](https://img.shields.io/badge/Capability_Routed_Split_Encoder-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/hemanth/swanada)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Swanada 是覆盖梵语、印度英语与十种印度语言的端侧流式 ASR 系统，用能力路由的共享 INT8 Conformer 编码器加 12 个可热插拔的 515.0 KiB CTC 头，12 语言体积从 2128.5 MiB 压到 183.4 MiB 与 31.39 MiB；留出集 CER 5.43%，流式首字 30.6 ms。**</p>

