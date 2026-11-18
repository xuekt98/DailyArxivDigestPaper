<!-- direction: duplex_speech_core -->

+ **A$^3$: Adaptive Audio Agent Framework for Collaborative Edge Computing**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18064)
![architecture](https://img.shields.io/badge/A3_Hedged_Edge_Audio_Agent-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZexinLi0w0/A3)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**A3 把音频 agent 的 ASR、LLM、TTS 按整段卸载到边缘服务器，同时在 Jetson 上保留一条完整的本地回退链，并用链路感知的截止时间对两条路径做对冲执行：带宽受限下延迟从 17.6 秒降到 9.7 秒，完全断网时仍能回答全部请求。**</p>

+ **What Do Multilingual Self-Supervised Speech Encoders Know About Sentence Meaning?**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17686)
![architecture](https://img.shields.io/badge/Cross_Modal_Linear_Probe-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/The_Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用线性探针把 76 种语言的自监督语音表征映射到冻结文本空间做跨模态检索，发现句级语义线性可解却跨语言极不均衡：OmniASR-W2V-7B 留一语言探针 33% 反超单语 30%，580M 的 w2v-BERT-2.0 多语探针 47% 胜过 7B 模型。**</p>

+ **FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18561)
![architecture](https://img.shields.io/badge/FETTUCCINE_Neural_Adapter_ASR_Decoder-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Georgia_Tech-green)
[![project](https://img.shields.io/badge/project-blue)](https://fettuccine-brain2text.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FETTUCCINE 用神经适配器与 LoRA 改造 Whisper、Parakeet 等 ASR 主干做端到端脑到文本解码，在 brain-to-text 2025 上 WER 低至 4.39%，并首次把脑机解码搬上 iPhone 15 Pro Max，吞吐可达 370 倍实时。**</p>

+ **CamSpokenNLI: A Pilot Resource for Cross-Variety Transfer Evaluation in Cameroon Pidgin English and Camfranglais**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17573)
![architecture](https://img.shields.io/badge/CamSpokenNLI_Spoken_NLI_Resource-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/University_of_Buea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CamSpokenNLI 为喀麦隆 Pidgin 与 Camfranglais 各做 114 条口语前提 NLI 样本，并用不重叠跨变体迁移与对应泄露审计说明 XLM-RoBERTa 的 44.7%/46.2% 准确率多半来自假设措辞，零样本 Whisper 转写 WER 高达 66.6%/45.5%。**</p>

<!-- direction: speech_rl -->

+ **CoTTAGE: An Explainable Judge for Text-to-Audio Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17644)
![architecture](https://img.shields.io/badge/Thurstone_Preference_RL_Judge-red)
![task](https://img.shields.io/badge/RLHF_Speech-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/YuXiangLin1234/CoTTAGE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文本到音频生成的可解释评判器：先生成有音频依据的理由再给分，RL 阶段用 Thurstone 模型把 K=8 条推理轨迹的分数分布转成成对偏好概率，与人工 MOS 导出的排序对齐作为奖励，支撑 1 万余条新采集的 OVL 标注，在六个基准上同时刷新 REL 与 OVL 相关性。**</p>

