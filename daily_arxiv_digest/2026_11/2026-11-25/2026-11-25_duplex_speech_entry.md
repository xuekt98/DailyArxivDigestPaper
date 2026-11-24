<!-- direction: duplex_speech_core -->

+ **From Spatial Perception to Speech Recovery: Binaural Semantic Adaptation for Spatially Grounded Multi-Talker Transcription**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29012)
![architecture](https://img.shields.io/badge/BiSA_Binaural_Semantic_Adaptation-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Xi’an_Jiaotong-Liverpool_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断出空间音频大模型 MiDashengLM-Spatial 的语义编码器只用了单耳信号，这是它能定位说话人却无法在重叠语音中恢复对话的主因；BiSA 用共享双耳编码加跨耳差分交互，只训练 0.027% 参数，就把同时起音联合转写的空间归属成功率从 0% 提到 57.81%。**</p>

+ **Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28248)
![architecture](https://img.shields.io/badge/Granary_v2_Curation_Pipelines-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio/granary_v2)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Granary-v2 把同一段录音对齐成口语忠实转写、含或去掉口语化的书面稿、code-switched 文本、上下文 ASR 与翻译等目标并配套指令；处理后 843,579.22 小时覆盖 48 语种，同等训练步数下标签过滤把九个基准的平均 WER 从 4.91% 降到 4.67%。**</p>

<!-- direction: speech_rl -->

+ **Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29226)
![architecture](https://img.shields.io/badge/Tenlai_TTS_2_0-red)
![task](https://img.shields.io/badge/RL_for_TTS-magenta)
![organization](https://img.shields.io/badge/Tencent_Yuanbao-green)
[![project](https://img.shields.io/badge/project-blue)](https://tenlai-tts.github.io/Tenlai-TTS-2.0/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Tenlai-TTS 2.0 让连续语音表征端到端学出来：容量受控的高斯瓶颈、AR-DiT 头、FM 解码器与多任务识别模型联合训练，再用可微重建与识别反馈优化潜变量预测；最后以奖励加权的 DiffusionNFT 式 RL 把 test-hard-zh 的 CER 压到 6.29%。**</p>

