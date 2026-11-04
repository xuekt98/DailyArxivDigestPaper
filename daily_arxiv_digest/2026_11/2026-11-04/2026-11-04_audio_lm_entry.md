# 2026-11-04 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **VeriSpoof: Beyond Real or Fake with One Audio LLM**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04634)
![architecture](https://img.shields.io/badge/Unified_Forensic_Audio_Language_Model-red)
![task](https://img.shields.io/badge/Audio_Language_Model-magenta)
![organization](https://img.shields.io/badge/The_University_of_Melbourne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**墨尔本大学 VeriSpoof 用一套权重统一深伪检测、生成器归因、合成片段定位与源验证，14 个 Speech-DF-Arena 测试集 pooled EER 2.14%、开源第一，PartialEdit 上 99.6% 对 78.4%，且训练只更新 2.85B 参数中的 29.7M。**</p>
+ **ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04480)
![architecture](https://img.shields.io/badge/Self_Scanning_Evidence_Localization-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Microsoft-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**微软 ReListen 让冻结的音频语言模型按 20 秒窗口自打分挑证据再作答，VoiceGiraffe 上 88.5% 的问题所选分钟覆盖标注证据，比整段转写高 9.2 分，且内存恒定、速度领先转写系统。**</p>
+ **Do Multi-Turn Conversational Capabilities Carry Over from Text to Speech? A Parallel Multilingual Benchmark**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04390)
![architecture](https://img.shields.io/badge/Parallel_Multilingual_Speech_Benchmark-red)
![task](https://img.shields.io/badge/Spoken_Dialogue_Evaluation-magenta)
![organization](https://img.shields.io/badge/College_of_Computer_Science_Nankai_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/QwenLM/Omnilingua-Bench/tree/main/Omnilingua-AudioMC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**南开与阿里发布 Omnilingua-AudioMC，354 段对话、1404 个评分项、10 种语言严格平行评测六个语音语言模型，证明文本多轮能力不可靠迁移到语音，且历史轮次是可恢复退化的主要来源。**</p>
+ **Confidence-Aware Aggregation for Multimodal Audio Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04580)
![architecture](https://img.shields.io/badge/Confidence_Aware_Aggregation_Framework-red)
![task](https://img.shields.io/badge/Audio_Reasoning-magenta)
![organization](https://img.shields.io/badge/LTCI_Télécom_Paris_Institut_Polytechnique_de_Paris_France-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/michelolzam/lalm-self-consistency)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**巴黎电信学院提出免训练的置信度感知聚合，用对数概率为 LALM 候选答案加权，在 Qwen3-Omni 等四个模型上同时改善准确率与校准，高分歧场景下明显优于经典多数投票。**</p>
+ **The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05124)
![architecture](https://img.shields.io/badge/Role_Value_Causal_Intervention_Analysis-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**北京理工大学等四家机构证明语音大模型的多轮记忆问题是历史值把答案导向特定竞争答案，且多选题中屏蔽直接访问也无法消除，来源角色信息与答案值信息需要分别干预，并给出联合干预方案。**</p>
+ **SciPhi-Chat: Training a Spatial Audio Agent for Question Answering, Dialogue, and Tool Use**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04114)
![architecture](https://img.shields.io/badge/Spatial_Audio_Agent_With_Tool_Use-red)
![task](https://img.shields.io/badge/Spatial_Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Microsoft_Research_Redmond_WA_USA-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/microsoft/sciphi-chat)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**微软研究院发布空间音频智能体 SciPhi-Chat 与含 42 类任务、1.2 万样本的 MASU 基准，得分 44.9% 领先先前 SOTA 7.4 个百分点，ASA-Bench 方位角 74.5%、仰角 60.0%，去掉推理监督掉 17.4 点。**</p>
+ **PianoBench: Evaluating Musical Perception and Reasoning in Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03839)
![architecture](https://img.shields.io/badge/Music_Reasoning_Benchmark_Suite-red)
![task](https://img.shields.io/badge/Music_Understanding-magenta)
![organization](https://img.shields.io/badge/Queen_Mary_University_of_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://gclef-cmu.org/pianobench)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**玛丽女王学院等推出 PianoBench 与两小时量级的 PianoTalk 数据集，开源音频语言模型最高 52.8%、几乎不超过无音频对照，而给转写文本的前沿模型用思维链可达 93.2%。**</p>
+ **ufakzeka-kulak: Building and Evaluating a 31.6M-Parameter Turkish Speech Recognizer from Scratch**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03605)
![architecture](https://img.shields.io/badge/FastConformer_TDT_CTC_Turkish_ASR-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/ufak_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://kulak.ufakzeka.com)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**31.6M 参数的土耳其语 ASR 从零训起并开源，仅用二次独立听读一致的 4,696 小时机翻数据，FLEURS 测试集 WER 0.0921、Common Voice 0.0916，均优于 Whisper base 与 small。**</p>
+ **Clean-anchored excess-emission control for CTC adaptation under competing speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03900)
![architecture](https://img.shields.io/badge/Clean_Anchored_Collapsed_Count_Penalty-red)
![task](https://img.shields.io/badge/Robust_ASR_Evaluation-magenta)
![organization](https://img.shields.io/badge/Missouri_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**密苏里理工用干净教师锚定的塌缩计数惩罚压住 CTC 多余发射，仅训 147,456 个参数就让语音干扰 WER 从 45.198% 降到 44.323%，干净 WER 仅变化 0.004 个百分点。**</p>
+ **Attendance-guided speaker enrollment across meetings**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04394)
![architecture](https://img.shields.io/badge/Attendance_Guided_Speaker_Enrollment-red)
![task](https://img.shields.io/badge/Speaker_Diarization-magenta)
![organization](https://img.shields.io/badge/NAVER_Cloud_Corporation_South_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NAVER Cloud 用预期出席名单交叉索引会议归档中的匿名说话人聚类来自动注册声纹，提出含污染敏感评测的新基准，并如实指出合成阈值迁移到真实会议仍存在合成-真实差距。**</p>
