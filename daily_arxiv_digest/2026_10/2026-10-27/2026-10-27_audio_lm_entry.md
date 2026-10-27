# 2026-10-27 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34653)
![architecture](https://img.shields.io/badge/Early_Actionable_Point-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Heard Enough to Act 把「听到多少才够行动」变成可标注的 earliest-actionable-point 监督，构建 26,694 段、786 小时、48 领域的合成口语对话语料并训练 omni-modal 模型做因果 chunk 级决策，正确调用相对整轮级联平均提前 1.8–2.0 秒。**</p>
+ **Diagnosing and Mitigating Long-Session Degradation in Full-Duplex Speech Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34991)
![architecture](https://img.shields.io/badge/TRC_Long_Session_Duplex-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为全双工语音模型建立闭环长会话稳定性评测，揭示响应性、内容质量与声音一致性随时间退化；用自蒸馏 LoRA 加双分辨率上下文 TRC（近期交互全保留、旧历史压缩为 KV）缓解，KV-cache 增长降低 90% 以上。**</p>
+ **Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35846)
![architecture](https://img.shields.io/badge/Preserve_to_Expand-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/University_of_Essex-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在连接器式 Speech LLM 上系统比较多语种扩展：单目标下只训目标语言与标准 TIES 合并都会严重遗忘源语言，SSU-Wanda+TIES 保持最好；多目标下更新合并最稳，而递归扩展对顺序极其敏感。**</p>
+ **DecisionTraceBench: Tracking Decision-Critical Information in Multi-Party Spoken Conversations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34746)
![architecture](https://img.shields.io/badge/DecisionTraceBench-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Qifu_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DecisionTraceBench 评测多方口语对话中决策关键信息的轨迹级还原：中文金融对话（100.39 小时合成 + 8.61 小时真人录音）上，五个级联系统与两个直接音频模型的 DCIST 分数仅 5.73%–21.35%，即使给参考脚本也最高只有 38.72%。**</p>
+ **One Mean Log-Mel Vector per Phoneme: Simple and Fast Text Injection for Speech Recognition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34623)
![architecture](https://img.shields.io/badge/Phoneme_Mean_LogMel-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/RWTH_Aachen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ASR 文本注入不再依赖冻结 TTS：改为每个音素一个平均 log-mel 向量的查表、按对齐统计采样时长，训练快 1.8 倍而 WER 相当，配合外部语言模型在 LibriSpeech clean/other 测试集上达 1.36/2.90% 与 1.52/3.24% WER。**</p>
+ **Probing the phon* representations of the Mimi codebooks**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35432)
![architecture](https://img.shields.io/badge/Mimi_Codebook_Phonetics-red)
![task](https://img.shields.io/badge/Speech_LM-magenta)
![organization](https://img.shields.io/badge/Universite_Paris_Cite-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用强制对齐、熵分析与音素归一化互信息替代不适配 80 ms 固定窗口的 ABX 评测，量化 Mimi 编解码器第一层码本的音素表征：单个 token 与特定音素强相关（PNMI 0.84），但一个音素由多个竞争 token 共同实现，并非一对一映射。**</p>
+ **S2SND-v2: Unified Online and Offline Speaker Diarization with Speaker-Adapted w2v-BERT 2.0**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34707)
![architecture](https://img.shields.io/badge/S2SND_v2_Diarization-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**S2SND-v2 用说话人自适应的 w2v-BERT 2.0 前端、重叠感知 activity-query 掩码与晚说话人训练统一在线/离线说话人分离，剪枝系统仍在八个测试集上取得在线 14.52%、离线 12.03% 的平均 DER。**</p>
+ **Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35694)
![architecture](https://img.shields.io/badge/Not_One_Belief-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/Hanoi_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把口语 QA 的追问拆成话语行为与答案载荷两轴后实测发现：只有用户给出答案串时错误才被修复（正确载荷转换的错误数至少是重问的四倍），而四种置信度信号互相不一致，冻结探针在 Qwen2.5-7B 上随答案顽固程度而非真实性上升。**</p>
+ **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35029)
![architecture](https://img.shields.io/badge/Synthetic_Child_Adult_Dialogue-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Bielefeld_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在一整套语言学度量上对比合成 TinyDialogues 与自然对话后发现：合成数据在词汇层面与自然数据匹配，却严重低估了口语交互本身的破碎与碎片化特征；作者用真实对话构造数据做指令微调可部分矫正该偏差。**</p>
+ **When Fusion Order Matters: Insights on Progressive Multimodal Representation Learning for Cross-modal Retrieval**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35125)
![architecture](https://img.shields.io/badge/UniPRO_Fusion_Order-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UniPRO 用可配置融合调度研究多模态检索的融合顺序：逐个引入优于堆叠融合，且在 R@1 上文本与音频检索都偏好把匹配查询的模态放在最后；受控的语音缺失会反转这一偏好顺序，并据此预测的 visual-last 调度在 MSR-VTT-9k 拿到 97.9 R@1。**</p>