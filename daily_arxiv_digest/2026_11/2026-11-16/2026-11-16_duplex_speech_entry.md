<!-- direction: duplex_speech_core -->

+ **What Do Multilingual Self-Supervised Speech Encoders Know About Sentence Meaning?**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17686)
![architecture](https://img.shields.io/badge/Cross_Modal_Linear_Probe-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/The_Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用线性探针把 76 种语言的自监督语音表征映射到冻结文本空间做跨模态检索，发现句级语义线性可解却跨语言极不均衡：OmniASR-W2V-7B 留一语言探针 33% 反超单语 30%，580M 的 w2v-BERT-2.0 多语探针 47% 胜过 7B 模型。**</p>

+ **Anomalous Sound Detection Using Separation Features and Paired-Mixture Representation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17895)
![architecture](https://img.shields.io/badge/Paired_Mixture_Representation_Learning-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Kyungpook_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向工业声学监测的异常声音检测：分离器估计目标成分后，在冻结分离特征上用成对混合做对比与一致性学习，再以干扰协方差校正后按余弦最近邻对正常参考打分，在 DCASE 2022 Task 2 上取得 64.56% 的整体 H。**</p>

<!-- direction: speech_rl -->

+ **CoTTAGE: An Explainable Judge for Text-to-Audio Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17644)
![architecture](https://img.shields.io/badge/Thurstone_Preference_RL_Judge-red)
![task](https://img.shields.io/badge/RLHF_Speech-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/YuXiangLin1234/CoTTAGE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文本到音频生成的可解释评判器：先生成有音频依据的理由再给分，RL 阶段用 Thurstone 模型把 K=8 条推理轨迹的分数分布转成成对偏好概率，与人工 MOS 导出的排序对齐作为奖励，支撑 1 万余条新采集的 OVL 标注，在六个基准上同时刷新 REL 与 OVL 相关性。**</p>

