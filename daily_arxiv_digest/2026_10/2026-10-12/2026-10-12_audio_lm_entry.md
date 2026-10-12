+ **Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio Grounding in LALM Hallucination**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13112)
![architecture](https://img.shields.io/badge/Black_Box_Causal_Audit-red)
![task](https://img.shields.io/badge/Audio_Language_Model_Hallucination-magenta)
![organization](https://img.shields.io/badge/1Sharif_University_of_Technology,_Iran-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大型音频语言模型经常出现物体幻觉，肯定并不存在的声音。主要缓解手段 Audio-Aware Decoding 通过对比真实音频与全零「空白」波形下的 logits 运作，而此前评审已标记该空白波形为分布外。本文提出黑盒因果测试来隔离幻觉的实际来源。**</p>

+ **AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13600)
![architecture](https://img.shields.io/badge/Transitional_Importance_Token_Elimination-red)
![task](https://img.shields.io/badge/Efficient_Audio_LLM-magenta)
![organization](https://img.shields.io/badge/Eindhoven_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大音频语言模型在语音-文本任务上表现强，但标准音频编码器即使对短音频片段也产生数百个 token。由于自注意力按序列长度平方增长，这显著抬高了推理期计算量。**</p>

+ **Phonology-Aware Speaker Extraction Frontend for Audio LLMs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13500)
![architecture](https://img.shields.io/badge/Phonology_Aware_Speaker_Frontend-red)
![task](https://img.shields.io/badge/Target_Speaker_Extraction-magenta)
![organization](https://img.shields.io/badge/1Sun_Yat-Sen_University,_Zhuhai,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**目标说话人提取（TSE）是让音频大语言模型在重叠语音中识别并理解指定说话人的关键前端。然而多语混合的提取需求异质，固定深度的系统要么对困难输入处理不足，要么浪费算力。**</p>

+ **SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13081)
![architecture](https://img.shields.io/badge/Self_Rated_Difficulty_Reasoning-red)
![task](https://img.shields.io/badge/Audio_Reasoning-magenta)
![organization](https://img.shields.io/badge/1_MoE_Key_Lab_of_Artificial_Intelligence,_X-LANCE_Lab,_Shanghai_Jiao_Tong_University,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期关于大型音频语言模型的工作探索自适应推理以平衡精度与效率，但现有方法常依赖**粗粒度**难度估计，忽略了决定推理投入的多样因素。SWEAR 导出五维难度刻画。**</p>

+ **Lossless Inference Acceleration for ASR via EAGLE-Style Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13506)
![architecture](https://img.shields.io/badge/Eagle_Style_Speculative_Decoding-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/lege_of_Intelligence_and_Computing,_Tianjin_University,_Tianjin_300350,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归 Transformer 与 Conformer 在 ASR 上达到最优性能，但其逐 token 生成的机制在解码期造成显著延迟瓶颈。推测解码是应对该问题的方案之一，本文将其引入 ASR。**</p>

+ **Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13807)
![architecture](https://img.shields.io/badge/Augmentation_Cost_Audit-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/University_of_Notre_Dame-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**数据增强是低资源 ASR 的标准做法，但其收益几乎总是以聚合错误率报告，留下「为什么以及何时某方法有帮助」未答。该文在四种低资源语言与英语、五种数据规模上交叉两种修改已有音频的增强方法。**</p>

+ **Revisiting Accent Classification with DistilHuBERT: Speaker-Disjoint Evaluation and Cross-Corpus Generalization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13440)
![architecture](https://img.shields.io/badge/Speaker_Disjoint_Reevaluation-red)
![task](https://img.shields.io/badge/Accent_Classification-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期口音分类系统在标准同语料评测中可达高准确率。但当训练集与测试集的说话人重叠时，这类结果可能**高估**模型相对真实部署场景的鲁棒性。该文以说话人不重叠的评测与跨语料泛化重新检视 DistilHuBERT。**</p>

+ **VoxAnon: A balanced dataset for a fair evaluation of speech anonymization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13313)
![architecture](https://img.shields.io/badge/Balanced_Anonymization_Benchmark-red)
![task](https://img.shields.io/badge/Speech_Anonymization_Evaluation-magenta)
![organization](https://img.shields.io/badge/Universit´e_de_Lorraine,_CNRS-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音匿名化用自动说话人验证攻击者评估，而攻击者性能取决于其训练与评测数据的属性分布，这可能对某些说话人群体偏置隐私估计。VoxAnon 从 VoxCeleb1 与 2 构建带平衡属性的数据集。**</p>

+ **Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13277)
![architecture](https://img.shields.io/badge/Token_Level_Evidence_Retrieval-red)
![task](https://img.shields.io/badge/Conversational_Memory_Retrieval-magenta)
![organization](https://img.shields.io/badge/1Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**带记忆增强的助手从存储的对话与文档中检索证据来回答查询。多数基于嵌入的检索器比较查询与记忆的单向量表示，即使相关性只取决于内容的一小部分。这些局部证据可以用上下文 token 匹配。**</p>

+ **Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.13282)
![architecture](https://img.shields.io/badge/Multimodal_LALM_ASR_System-red)
![task](https://img.shields.io/badge/Timestamped_Speaker_Attributed_ASR-magenta)
![organization](https://img.shields.io/badge/1Key_Laboratory_of_Modern_Acoustics,_Nanjing_University,_Nanjing,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文描述 SLT2026 智能眼镜挑战赛 Track 1（带时间戳的说话人归属 ASR）的系统。为处理两人对话中的重叠语音、背景噪声与远场条件，使用 SoulX-Transcriber 这一接受全长音频输入的多模态大语言模型。**</p>

