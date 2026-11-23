<!-- direction: duplex_speech_core -->

+ **From Attention to Semantics: Detecting and Mitigating Sound Event Hallucinations in Large Audio-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25789)
![architecture](https://img.shields.io/badge/Differential_Audio_Masking_Framework-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 LatentLens 改造成音频语义探针后可见，真实事件与幻觉事件的音频注意力质量几乎相同（34.64% 对 30.08%），差别在于被关注位置的语义是否支撑生成内容；据此给出免训练的检测-缓解框架，在 3 个 LALM、2 个数据集上把 AF3 的 ECHO-I 从 22.7% 降到 14.9%。**</p>

+ **Embodied Interaction Policy: A Unified Model for Full-Duplex Human-Robot Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27327)
![architecture](https://img.shields.io/badge/Chunkwise_Causal_Joint_Attention-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/Sichuan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://youqiang-gui.github.io/EIP/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EIP 用 400 ms 分块的层间联合注意力，把 Qwen2.5-3B 语音交互专家与 380M 动作专家统一成一个流式模型，可边说边动并处理打断；Astribot S1 上 FGD 由 74.51 降到 43.83，运动自然度 6.33 超过 RoboGesture 的 3.20，warm-start 延迟降低 64%。**</p>

+ **PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27601)
![architecture](https://img.shields.io/badge/Style_Prompt_Interleaved_Tuning-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/bigai-ai/PromptTTSD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从 107 部中文、20 部英文多人有声书出发，改进的两阶段对齐把引文句匹配率从 71.39% 提到 94.13%，据此发布中文 8,383 小时、79% 语句带开放式风格描述的 PromptDialog；PromptTTSD 支持零样本克隆与自然语言风格控制，CA-MOS 从 3.06 提到 3.52。**</p>

+ **EAF-TTS: Rethinking Codec-Latent Coordinates for Flow TTS**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27214)
![architecture](https://img.shields.io/badge/Embedded_Acoustic_Flow_TTS-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/AI_Lab_Country_Garden_Services_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EAF-TTS 把 ELF 的共享生成与末端修正迁到 64 维 WaveVAE 潜变量，只用训练集统计做 ZCA 变换、不增加可学习参数；面对 LJSpeech 训练潜变量 1355.44 的条件数，三组匹配种子在 Val399 严格 GT 上把 UTMOS 提高 0.405，ZCA-5 同时把生成路径 RTF 降到三分之一。**</p>

<!-- direction: speech_rl -->

+ **SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27810)
![architecture](https://img.shields.io/badge/Claim_Factuality_GRPO_Reward-red)
![task](https://img.shields.io/badge/GRPO_Speech-magenta)
![organization](https://img.shields.io/badge/Callyope_Paris_France-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SLP-Bench 用 5 个临床语音数据集、25 个感知维度和 3,452 条提示，逐条核对推理 ALM 思维链里的声学断言；10 个开源模型零样本断言平衡准确率仅 0.52 至 0.58，用 GRPO 奖励与临床评分一致的断言后，7B 模型断言 BA 由 0.54 升到 0.60、κ 由 0.39 升到 0.61。**</p>

