<!-- direction: duplex_speech_core -->

+ **Hy ASR 3.0 Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14908)
![architecture](https://img.shields.io/badge/Hy_ASR_3_0-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Hy_ASR_team_Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**腾讯混元 Hy ASR 3.0 是基于 Hy3 大模型的 LLM 式 ASR 系统，支持普通话、英语与 13 个汉语方言群；公开基准聚合中文 CER 4.64%、英文 WER 5.22%、方言 4.80%，可用热词、问答对话与摘要做外部上下文偏置，并能在句内消解同音关键词。**</p>

+ **Distributionally Robust BEST-RQ For Speech Representation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14801)
![architecture](https://img.shields.io/badge/DRO_BEST_RQ_KL_Regularized-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/Rensselaer_Polytechnic_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把随机量化目标按码本分成 group 做分布鲁棒优化并加 KL 正则，让 BEST-RQ 不再押注单一次随机抽样：在 Multilingual LibriSpeech 五语种上平均 WER 从均匀多码本的 8.9% 降到 λ=1.0 时的 8.4%，葡萄牙语等低资源语种收益最大。**</p>

+ **Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14929)
![architecture](https://img.shields.io/badge/T_SemAttack_ROSETok_Pipeline-red)
![task](https://img.shields.io/badge/Speech_Tokenization-magenta)
![organization](https://img.shields.io/badge/Shenzhen_International_Graduate_School_Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://wxzyd123.github.io/t-semattack)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现语音 tokenizer 在语义层极其脆弱：T-SemAttack 联合四个代理编码器做语义漂移，把 LibriTTS 上 7 个目标 ASR 的平均 WER 从 2.503% 抬到 61.348%；对应的 ROSETok 用带噪训练加鲁棒语义蒸馏，把受攻击后的下游 FSC 分数从基线最高的 35.0 提升到 77.9。**</p>

