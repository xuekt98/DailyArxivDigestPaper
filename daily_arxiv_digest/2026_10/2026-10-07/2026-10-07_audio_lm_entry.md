+ **PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07725)
![architecture](https://img.shields.io/badge/Who_What_When_Memory-red)
![task](https://img.shields.io/badge/Full_Duplex_Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/1Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音助手常被多人共用，需要回答'我原本打算什么时候离开'这类问题。这超出检索一段主题相似的文本：助手必须识别当前说话人、恢复相关的历史状态，并把它与后来的修正区分开。PERSIST 用 Who-What-When 记忆来做这件事。**</p>

+ **HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07727)
![architecture](https://img.shields.io/badge/Hierarchical_Policy_Factorization-red)
![task](https://img.shields.io/badge/Full_Duplex_Speech_Language_Model-magenta)
![organization](https://img.shields.io/badge/1Qualcomm_AI_Research,_2KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工语音语言模型除了生成得体回应，还必须实时协调话轮转换、附和（backchanneling）与话语权管理。强化学习可以细化这些行为，但现有方法要么只对 token 策略施加时序反馈，要么只优化语义。HiPLEX 做层次化策略分解。**</p>

+ **Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08125)
![architecture](https://img.shields.io/badge/Dyadic_Evaluation_Protocol-red)
![task](https://img.shields.io/badge/Full_Duplex_Dialogue_Evaluation-magenta)
![organization](https://img.shields.io/badge/1Korea_Advanced_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工对话模型边听边说，能实现轮次制做不到的自然低延迟交互。但它们普遍对着单边对手评测：预录音频不会反应，或自动考官实时反应却只按固定顺序出题、自身从不被评分。作者指出这只评了'双体问题'的一半。**</p>

+ **Coupled but Late: Turn-Taking Between Full-Duplex Speech Models in Unscripted Dialogue**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08683)
![architecture](https://img.shields.io/badge/Shared_Clock_Turn_Taking-red)
![task](https://img.shields.io/badge/Full_Duplex_Speech_Evaluation-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工语音模型越来越多地被用来互相对话——自生成play 数据、智能体社会、基于模型的评测。在这个环路里没有人类吸收时序误差，每个模型的话轮转换就是对方的输入。这篇问：环路最终稳定在什么时序上。**</p>

+ **Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07641)
![architecture](https://img.shields.io/badge/Speculative_Tool_Execution-red)
![task](https://img.shields.io/badge/Voice_Agent_Systems-magenta)
![organization](https://img.shields.io/badge/1Qualcomm_AI_Research,_2KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**工具增强的语音助手通常把 ASR、LLM 推理与外部工具执行串行化，于是工具延迟只在用户说完话、LLM 判定需要调用之后才发生。这篇提出推测式工具执行：从部分 ASR 结果预测工具请求，在语音仍在接收时就启动工具。**</p>

+ **Towards an Extensible Benchmark for Spoken Dialogue with Social Robots**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08733)
![architecture](https://img.shields.io/badge/Spoken_Dialogue_Benchmark-red)
![task](https://img.shields.io/badge/Social_Robot_Dialogue-magenta)
![organization](https://img.shields.io/badge/Boise_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语言模型为人与机器人之间提供了即插即用的接口，但在需要语音、对话、快速交互与协作时仍有明显缺口。这篇提出一个面向社区的基准，专门考察机器人与人类对话中的常见伪影：请求澄清、打断、具身信号（点头、面部提示）与时间约束。**</p>

+ **HINTT Submission to the 2nd MLC-SLM Challenge: Comparing Cascaded and Unified Approaches to Diarization and ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08063)
![architecture](https://img.shields.io/badge/Cascaded_And_Unified_Speech_LLM-red)
![task](https://img.shields.io/badge/Speaker_Attributed_ASR-magenta)
![organization](https://img.shields.io/badge/NTT,_Inc.,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NTT 提交第 2 届 MLC-SLM 挑战赛的系统，处理多语说话人归属 ASR——不仅要说什么、还要谁在什么时候说。作者比较两条建模路线：说话人分离 + 语音 LLM 的级联管线，以及直接生成说话人标签、时间戳与转写的统一语音 LLM。**</p>

+ **SkillFormer: Skill-Decomposed Adaptation for Audio Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07533)
![architecture](https://img.shields.io/badge/Skill_Routed_LoRA-red)
![task](https://img.shields.io/badge/Audio_Language_Model-magenta)
![organization](https://img.shields.io/badge/1Pusan_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**音频语言模型要同时应付音高比较、说话人计数、音乐速度估计、情绪识别等数十种能力，联合训练会产生干扰：一种能力涨了往往牺牲另一种。SkillFormer 把音频理解分解为技能专属低秩适配器，推理时由一个学习型路由器组合。**</p>

+ **AgentMemGate: Addressing Speculation Contamination in Conversational Assistant Memory**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07707)
![architecture](https://img.shields.io/badge/Write_Time_Memory_Gate-red)
![task](https://img.shields.io/badge/Conversational_Memory-magenta)
![organization](https://img.shields.io/badge/Distyl_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**带长期记忆的对话助手会把事实从用户消息中抽取出来存入记忆库供后续对话查询。一句计划可能被当成事实存入——可能搬去西雅图的用户被记成已经住在那儿。作者称之为推测污染。**</p>

+ **Quality-Aware Self-Correcting Speech Translation on an Edge Device**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07545)
![architecture](https://img.shields.io/badge/Quality_Aware_Second_Pass-red)
![task](https://img.shields.io/badge/Speech_To_Speech_Translation-magenta)
![organization](https://img.shields.io/badge/School_of_CS_and_EE-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**完全离线的语音到语音翻译管线跑在 4GB 显存的 Jetson Nano 上：Whisper-tiny 做 ASR、Opus-MT 做翻译，用多语 BERT 余弦相似度作质量估计门控，置信度低于阈值即触发二次修正。本文比较三种修正方式。**</p>

