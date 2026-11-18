<!-- direction: duplex_speech_core -->

+ **High-Fidelity Binarized Neural Vocoder**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22593)
![architecture](https://img.shields.io/badge/Binarized_TF_Neural_Vocoder-red)
![task](https://img.shields.io/badge/Neural_Audio_Codec-magenta)
![organization](https://img.shields.io/badge/Institute_of_Acoustics_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Andong-Li-speech/BiVoC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 1-bit 权重与激活的 BiVoC：把 range-null 分解、层级子带建模与混合精度设计搬进时频域神经声码器，理论参数压缩 32×、算力下降 64×，在 LibriTTS 上用 AAE 代理梯度把 PESQ 做到 3.055。**</p>

+ **Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22628)
![architecture](https://img.shields.io/badge/Subband_Aware_Transformer-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/Institute_of_Acoustics_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Andong-Li-speech/BAME)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BAME 回到 Mel 频谱这一结构化表示：用 25 个子带、11.2 M 参数的 SaT 流匹配骨干替代 331 M 的 DiT，配相感知神经声码器与一步保真-感知对齐，在 DNS-Challenge 2020 上 PESQ 2.487、WER 9.242%。**</p>

<!-- direction: speech_rl -->

+ **Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22627)
![architecture](https://img.shields.io/badge/Constraint_Aware_GRPO_SpeechLLM-red)
![task](https://img.shields.io/badge/GRPO_Speech-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/caiyunrui/MT-GRPO)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRPO 用于未知说话人数的多说话人 ASR 与说话人日志：先用 CoT 前缀显式估计全局人数，再用 MCAR 多维约束奖励做 on-policy 探索，Dynamic-Mix 上 cpWER 9.24%、WDER 1.12%、CoT-Acc 99.72%。**</p>

