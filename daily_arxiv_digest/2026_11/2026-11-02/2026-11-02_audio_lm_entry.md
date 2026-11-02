# 2026-11-02 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41390)
![architecture](https://img.shields.io/badge/AudioHelix_Hierarchical_DualGraph_RAG-red)
![task](https://img.shields.io/badge/Audio_Reasoning-magenta)
![organization](https://img.shields.io/badge/Ewha_Womans_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AudioHelix 为长音频推理搭建分层 DualGraph，把长录音离线切成 chunk 并抽取语言与声学信息，构成 chunk、unit 与语义概念三级图谱，查询时先定位种子概念再传播相关性，跨三个长音频基准稳定超过整段处理与已有 RAG。**</p>
+ **From Transcription to Reformulation: Defining and Benchmarking Grounded Generative Speech Recognition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41292)
![architecture](https://img.shields.io/badge/GSR_Bench_Reformulation_Hierarchy-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/China_Telecom_Artificial_Intelligence_Technology_Co._Ltd-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 Grounded Generative Speech Recognition，把语音识别从还原单条转写改成生成语义有据的文本，定义字面转写、规范化改写、语义改写与语音支撑结构化四级能力，并配套 GSR-Bench 与结合语音 grounding 与 LLM 判定的多维评测框架。**</p>
+ **Incongruence-Aware Evaluation of Multimodal Speech Emotion Recognition in Audio Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40883)
![architecture](https://img.shields.io/badge/VAD_Incongruence_Gaussian_Mixture_Score-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把文本与音频映射到同一套 valence-arousal-dominance 空间，用双成分高斯混合把两通道距离转成连续无阈值的失配分数，跨 eNTERFACE、MELD 与 CMU-MOSEI 三个语料证明失配会显著抬高语音大模型的出错几率。**</p>
+ **TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42010)
![architecture](https://img.shields.io/badge/TurnTurk_GPT2_TurnGPT_TurnTaker-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Ata_Technology_Platforms-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TurnTurk-GPT 用 TurnGPT 目标微调土耳其语 GPT-2 做纯文本的轮次结束预测，在词级决策点上以录音隔离与说话人隔离两种切分评测，发现土耳其语的结束线索主要落在动词后缀的黏着形态上。**</p>
+ **GhostPrefix: Synchronization-Free Universal Prefix Attacks for ASR Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42026)
![architecture](https://img.shields.io/badge/GhostPrefix_Universal_Adversarial_Prefix-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Michigan_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GhostPrefix 提出首个免同步、通用且可复用的 ASR 前缀攻击，把一段短音频接到任意实时语音之前即可实时操控识别结果，覆盖提示引导、定向劫持与非定向降质三种模式，数字域与空对空场景的成功率均超过 89%。**</p>
+ **Parameter-Efficient Fine-Tuning of Transformer Encoders for Audio-Image-Symbolic Music Retrieval**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41512)
![architecture](https://img.shields.io/badge/PEFT_LoRA_QLoRA_Music_Retrieval-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Alicante-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在九个音频、图像与符号乐谱预训练编码器上系统比较全量微调、LoRA 与 QLoRA，再用编码器适配与共享投影的 2×2 设计拆解两者作用，得出单模态判别力提升并不自动带来更好的跨模态表示这一结论。**</p>
+ **TalkFlow: Structured Latent Flow Matching for Speech Driven Holistic Motion Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40972)
![architecture](https://img.shields.io/badge/TalkFlow_Structured_Latent_Flow_Matching-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Stony_Brook_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TalkFlow 为语音驱动的整体动作生成提出结构化潜空间流匹配，把上半身、下半身与面部表情拆成三条连续潜流并以轻量跨流交互保持协调，再在 BEAT2 上用语音条件流匹配生成与语音对齐的全身动作。**</p>
+ **SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding in Conversational XAI**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41856)
![architecture](https://img.shields.io/badge/SimXAI_ToolCalling_LLM_ConvXAI_Layer-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/University_of_Marburg-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SimXAI 把对话式可解释 AI 的意图识别、对话管理与模板生成三个模块换成单个会调工具的 LLM 层，做成可插拔接口，在 TalkToModel 上仅替换对话层就让 30 人用户研究中的任务完成更准、轮次更少。**</p>
+ **PersonaChatBench: Evaluating Chat Assistants with Diverse Simulated Users**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42060)
![architecture](https://img.shields.io/badge/PersonaChatBench_Simulated_User_Evaluation-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Brown_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PersonaChatBench 用同一批 806 个任务配不同人设卡片的模拟用户，在健康咨询、编程、数学辅导等六个领域评测 20 个语言模型，把任务完成度、人设需求满足度与模拟器保真度拆开独立打分。**</p>
+ **PsyInterviewee: Informational Invariance and Relational Adaptivity in Mental Health Interview Simulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41289)
![architecture](https://img.shields.io/badge/PsyInterviewee_DualChannel_Asymmetric_Write-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/BeIn-Lab/pdm-interviewer)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PsyInterviewee 用双通道与非对称写权限约束心理健康访谈模拟：受保护的事实通道只允许档案授权的临床事实，交互通道只更新披露与行为状态，并以档案核验生成的临床断言，分别度量信息不变性与关系适应性。**</p>
