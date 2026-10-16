+ **VoxTurn: Answering Several Turn-Taking Questions in One Pass with One Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21150)
![architecture](https://img.shields.io/badge/Unified_Turn_Taking_Decision-red)
![task](https://img.shields.io/badge/Turn_Taking_In_Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/The_University_of_Melbourne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**级联语音智能体必须在用户的每次静默中判断用户是否说完：答得太早会打断用户，答得太晚会让智能体变慢。它往往还需要相关的判断——用户是否会继续说、自己说话期间的声音是打断还是附和、那声音到底是不是语音。用开放的检测器（摘要在此处截断）。**</p>

+ **Full-Duplex Interaction with Speech, Expressions and Gestures**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21452)
![architecture](https://img.shields.io/badge/Multimodal_Full_Duplex_Dialogue-red)
![task](https://img.shields.io/badge/Full_Duplex_Interaction-magenta)
![organization](https://img.shields.io/badge/1Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**人类面对面对话需要在说话与倾听两侧同时协调语音、手势与表情。ELLSA 2 是一个端到端全双工对话模型，联合优化语音交互与流式的手势-表情生成。自回归的块式合成器把预训练声学特征与独特的倾听……（摘要在此处截断）。**</p>

+ **CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21143)
![architecture](https://img.shields.io/badge/Compressed_Speech_Token_Adaptation-red)
![task](https://img.shields.io/badge/Spoken_Dialogue_Models-magenta)
![organization](https://img.shields.io/badge/1Institute_of_Automation,_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**口语对话模型通常为生成与合成**共享同一个语音 token 空间**，导致自回归序列长、推理昂贵。低码率语音 tokenizer 可缩短序列，但可能引入压缩质量权衡与高昂的替换代价，且不解除这一耦合。CoSTA 提出一个兼容……（摘要在此处截断）的方案。**</p>

+ **Qwen-Audio-Jev: A Unified Interface for Audio Decisions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21614)
![architecture](https://img.shields.io/badge/Unified_Audio_Decision_Interface-red)
![task](https://img.shields.io/badge/Large_Audio_Language_Model-magenta)
![organization](https://img.shields.io/badge/Token_Foundry,_Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大型音频语言模型在音频理解上进展显著。但在需要频繁选择、判断与评分的高吞吐应用中，自回归文本生成引入额外计算开销与响应延迟。Qwen-Audio-Jev 通过增强 Qwen-Audio-3.1-ASR（摘要在此处截断）解决该问题。**</p>

+ **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22196)
![architecture](https://img.shields.io/badge/Attributed_Memory_Writing-red)
![task](https://img.shields.io/badge/Long_Term_Memory-magenta)
![organization](https://img.shields.io/badge/Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**外部记忆系统把语言模型应用扩展到上下文窗口之外，但其质量关键取决于执行**写入路径**的模型：决定保留什么、如何精确表示它、新证据如何更新持久状态。既有框架通常把一个通用大语言模型放在框架特定……（摘要在此处截断）之后。**</p>

+ **MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21405)
![architecture](https://img.shields.io/badge/Forgetting_Benchmark-red)
![task](https://img.shields.io/badge/Long_Term_Memory-magenta)
![organization](https://img.shields.io/badge/1The_Hong_Kong_University_of_Science_and_Technology_(Guangzhou)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长期记忆已成为大语言模型智能体的关键组件，多数研究聚焦于准确高效地检索信息。然而一个**可靠**的记忆系统还必须在被要求时**遗忘**敏感用户数据。为评估该能力，作者引入 MemCut——一个面向用户请求遗忘的系统性基准。**</p>

+ **From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21165)
![architecture](https://img.shields.io/badge/Memory_Centric_Compression_Survey-red)
![task](https://img.shields.io/badge/LLM_Compression_Survey-magenta)
![organization](https://img.shields.io/badge/tokens_(Google,_2026;_OpenAI,_2026;_Xu_et_al.,_2026a),_long-document_understanding,_codebase_analysis,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长上下文能力已成为大语言模型处理复杂任务的必要条件，但**持续扩展上下文窗口并不能消除**推理时的计算、存储与信息选择压力。既有工作已涵盖提示压缩、KV 缓存管理、高效服务、检索增强与智能体记忆。**</p>

+ **Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21126)
![architecture](https://img.shields.io/badge/Post_Selection_Positional_Geometry-red)
![task](https://img.shields.io/badge/Sparse_KV_Cache-magenta)
![organization](https://img.shields.io/badge/National_Key_Laboratory_of_Parallel_and_Distributed_Computing-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**稀疏 KV 压缩通过保留选中的历史状态降低长上下文推理成本，但这些状态通常**保留其在完整历史中的坐标**。在 RoPE 下，被驱逐 token 留下的空隙会继续影响 query-key 匹配，可能限制已保留证据的使用。作者研究选择性之后的位置几何。**</p>

+ **Co2In: a Bi-level Memory Incremental Learning Framework with Knowledge Encoding, Consolidation, and Integration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21804)
![architecture](https://img.shields.io/badge/Bi_Level_Memory_Incremental_Learning-red)
![task](https://img.shields.io/badge/Continual_Learning-magenta)
![organization](https://img.shields.io/badge/are_with_Key_Laboratory_of_Big_Data_&_Artificial_Intelligence_in-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**增量学习旨在持续获取新知识（可塑性）同时保留既有信息（稳定性），而平衡二者仍是智能系统的重大挑战。人脑通过多种记忆单元协同编码与存储取得出色平衡（摘要在此处截断）。**</p>

+ **Federated Art Chase: Privacy Leakage and Data Poisoning in Federated Fine-Tuning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21547)
![architecture](https://img.shields.io/badge/Federated_Privacy_Audit-red)
![task](https://img.shields.io/badge/Federated_Fine_Tuning_Security-magenta)
![organization](https://img.shields.io/badge/https://github.com/Indigma-Innovations/fl-summer-school_and_run_on_Google_Colab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**联邦学习日益被用于把一个预训练、集中微调过的模型适配到留在用户设备上的数据，而非从零训练模型。该报告（为第 4 届联邦机器学习国际暑期学校准备）以可复现管线研究这一做法的隐私与完整性（摘要在此处截断）。**</p>

