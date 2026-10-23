# 2026-10-23 - 音频与语音语言模型、双工语音助手 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Spark-Audio 1.0 Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31292)
![architecture](https://img.shields.io/badge/Spark-Audio_1.0-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/iFlytek_Spark_Audio_Team-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spark-Audio 1.0 用 0.65B 稠密音频编码器加 30B-A3B MoE LLM，在 1300 万小时音频上训练，支持 99 种语言与 202 种方言，后训练用 SFT 加 on-policy 蒸馏，多语种识别与口语对话超过 Qwen3.5-Omni-Flash。**</p>
+ **SyRA-CS: Synthetic-to-Real Adaptation for Code-Switched ASR with Meta-Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31415)
![architecture](https://img.shields.io/badge/SyRA-CS-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SyRA-CS 用 Reptile 元学习把合成代码切换语音当作「适配友好的初始化」而非普通监督：先在合成 CS-FLEURS 子集元训练，再用一小时真实标注适配，16 个模型-语言对的 WER 全部优于持续微调。**</p>
+ **Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30860)
![architecture](https://img.shields.io/badge/Nepali-English_Code-Switched_ASR-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Wiseyak_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/SamaFiroz/nepali-english-codeswitch-podcasts)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇发布 13,044 条（15.45 小时）尼泊尔语-英语代码切换播客基准，并给出诚实的量化：合成 SFT 把 MER 从 23.40% 降到 21.52%、SPER 从 35.89% 降到 28.77%，而后续 GRPO 仅带来极小调整——因合成数据上脚本方差近零。**</p>
+ **Text-Only LLM Correctors Break Correct Transcripts: A Repair-Damage Analysis of Audio Grounding in ASR Error Correction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30385)
![architecture](https://img.shields.io/badge/Repair-Damage_Decomposition-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/BitmanagerAI,_Dubai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇把每次 WER 变化精确分解为修复 / 损坏 / 新增 token：Gemini 2.5 Flash 的纯文本纠错会破坏 13–32% 本已正确的转写，带音频时降到 1–3%，证明「无音频 LLM 纠错 ASR」这一默认设定并不安全。**</p>
+ **Query-Conditioned Liquid Temporal Grounding for Long-Form Audio**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31252)
![architecture](https://img.shields.io/badge/Query-Conditioned_Liquid_TAG-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Surrey-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**查询条件化液体时间定位框架用 FiLM 注入查询语义、闭式连续时间网络建模长程依赖，由冻结的大音频语言模型在多个候选中挑选并做局部边界精修，在 LAT-Bench 上对 MOSS-Audio 与 Qwen3-Omni 均有效。**</p>
+ **A Systematic Comparison of Search Space Complexity and Efficiency for Time-Synchronous End-to-End ASR Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31259)
![architecture](https://img.shields.io/badge/Time-Synchronous_ASR_Search_Study-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/RWTH_Aachen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇横向比较 CTC 与神经转写器在不同剪枝与 LM 配置下的搜索复杂度：端到端模型多数时间搜索空间很小，但不确定时段假设数会临时激增，基于分数的动态剪枝显著降低实时因子。**</p>
+ **Muting Tokens: Exploring Token Sparsification for Efficient Audio Transformers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31235)
![architecture](https://img.shields.io/badge/Muting_Tokens-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Eindhoven_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇系统评测音频 Transformer 的 token 稀疏化：把注意力分数与 token embedding 的频谱线索结合，频率感知方法（谱平坦度、低频能量）持续优于纯注意力方法，频谱 patch 强度对长音频尤其有效。**</p>
+ **AGF-Net: A Robust Multimodal Emotion Recognition Model for Asynchronous Audio-Visual Signals Based on Predictive Dynamic Fusion with Negative Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30651)
![architecture](https://img.shields.io/badge/AGF-Net-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/National_Yang_Ming_Chiao_Tung_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AGF-Net 用预测式动态融合与负学习做异步音视频情绪识别：自动从连续对话生成候选话语片段并抽取音视频特征，免去人工边界标注，同时抑制误切分带来的噪声片段。**</p>
+ **Hear Every Sound Object: Rescuing Overlooked Sources in Auditory Scene Analysis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30874)
![architecture](https://img.shields.io/badge/Object-Based_ASA-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇研究基于对象的听觉场景分析：用 CKA 定位各声源之间的显著性能差距来源，并针对「直到最后一层才拆源」这一架构惯例提出改进，让被忽略的声源获得更均衡的表征。**</p>
+ **Predicting Music Valence and Arousal via Textual and Multimodal In-Context Learning in Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31202)
![architecture](https://img.shields.io/badge/Textual-Multimodal_ICL-red)
![task](https://img.shields.io/badge/Audio_Reasoning-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇研究音乐情绪价与唤醒度的预测：鉴于价主观且依赖语境、而唤醒度可从音频可靠预测，框架用文本与多模态的上下文示例驱动 LLM 推断，而非直接回归情绪分数。**</p>
