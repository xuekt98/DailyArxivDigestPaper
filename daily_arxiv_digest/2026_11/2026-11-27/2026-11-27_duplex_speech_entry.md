<!-- direction: duplex_speech_core -->

+ **TigerTTS: Draft-Guided Multi-Frame Parallel Speech-Token Language Model for Fast and Robust Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34241)
![architecture](https://img.shields.io/badge/Frame_Aligned_Draft_Guided_LM-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Wiz_Holdings_Pte._Ltd.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TigerTTS 用 28.8M 非自回归模型为整句起草语音 token，帧级对齐后注入 145.7M 的自回归 LLM，每步并行预测 3 帧共 12 个 token；CUDA Graph 解码 RTF 0.05 约 20 倍实时，Fast mode 还可在 LLM 起步前先输出 500 ms 音频。**</p>

<!-- direction: speech_rl -->

+ **BEARING: Who Is Talking to Whom? Grounding Acoustic Direction in Vision for Online Multi-Party Conversation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31735)
![architecture](https://img.shields.io/badge/Direction_Grounded_Verifiable_Reward-red)
![task](https://img.shields.io/badge/RLVR_Speech-magenta)
![organization](https://img.shields.io/badge/University_of_Denver-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BEARING 把麦克风阵列测到的声源方向无标签标定进图像，既作视觉提示把说话人准确率从 52.4% 提到 79.7%，又当可核对奖励去 GRPO 对齐多模态模型，在 AMI 上比自评估奖励高 4.6 分。**</p>

