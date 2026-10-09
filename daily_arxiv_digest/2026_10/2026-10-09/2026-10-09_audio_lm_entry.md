+ **DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11299)
![architecture](https://img.shields.io/badge/Recursive_Harness_Improvement-red)
![task](https://img.shields.io/badge/Full_Duplex_Voice_Agent-magenta)
![organization](https://img.shields.io/badge/⋆The_Chinese_University_of_Hong_Kong,_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音智能体正在收敛到一种协作范式：全双工交互模型留在实时通道上作为对话入口，检索、推理与编码则通过异步委派处理。双工模型支持持续听说，但复杂推理与工具使用可能超出其能力；编码智能体可以规划并执行扩展任务。**</p>

+ **Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11196)
![architecture](https://img.shields.io/badge/Paired_Drift_Analysis-red)
![task](https://img.shields.io/badge/Audio_Language_Model-magenta)
![organization](https://img.shields.io/badge/1College_of_Computer_Science_and_Technology,_National_University_of_Defense_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大型音频语言模型会利用多模态证据，但当不需要听的时候，与任务无关的音频仍可能改变文本推理决策。聚合准确率会掩盖这种成对漂移，因为音频带来的修复与损害可能互相抵消。作者用成对漂移分析与定向干预，定位出架构特定、可干预的晚期音频通路。**</p>

+ **DiffuPlex: Accelerating Full-Duplex Spoken Dialog Models via Rolling Masked Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12214)
![architecture](https://img.shields.io/badge/Rolling_Masked_Diffusion-red)
![task](https://img.shields.io/badge/Full_Duplex_Spoken_Dialog-magenta)
![organization](https://img.shields.io/badge/University_of_Seoul-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期的全双工口语对话模型实现了边听边说，但细粒度模型仍在每个交互帧上自回归推进其骨干。DiffuPlex 提出滚动掩码扩散框架，在单次骨干唤醒中预测多个未来的用户与助手帧，从而减少这类串行计算。**</p>

+ **SteerablePlex: Can We Steer Full-Duplex Models?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12201)
![architecture](https://img.shields.io/badge/Simulator_Instruction_Following_Benchmark-red)
![task](https://img.shields.io/badge/Full_Duplex_Steerability-magenta)
![organization](https://img.shields.io/badge/1University_of_Illinois_Urbana-Champaign,_2Karlsruhe_Institute_of_Technology,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工语音模型可以边听边说，交互自然，但随着对话历史增长会变得**越来越难以控制**。当它们被用作用户模拟器时，这种失控会让它们偏离规定场景并产生不可靠的评测结果。作者提出 SimIF-Bench 来评测指令遵循。**</p>

+ **Gated Memory: Admission-Controlled Memory Formation for Conversational AI**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11270)
![architecture](https://img.shields.io/badge/Admission_Controlled_Memory-red)
![task](https://img.shields.io/badge/Conversational_Memory-magenta)
![organization](https://img.shields.io/badge/Samsung_Research_America,_Mountain_View,_CA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**个性化对话 AI 依赖从用户话语中抽取事实并存入持久向量库的长期记忆系统。尽管检索、去重与生命周期管理都有进展，**形成阶段**——事实首次被写入存储的那一刻——几乎没得到原则性的关注。作者把它识别为记忆中质量的绑定约束。**</p>

+ **Local Prototype Reconstruction for Text-Compatible Speech-to-LLM Bridge Pretraining**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11159)
![architecture](https://img.shields.io/badge/Local_Prototype_Reconstruction-red)
![task](https://img.shields.io/badge/Speech_To_LLM_Bridge-magenta)
![organization](https://img.shields.io/badge/†Institute_of_Information_Science,_Academia_Sinica,_Taiwan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音到 LLM 系统通常用一个小的可训练桥接模块连接冻结的语音编码器与冻结的大语言模型。这个桥通常被当作管道，但它实际上定义了语音到 LLM 接口的几何，而预训练目标决定了这个接口是否为下游任务提供可复用的初始化。**</p>

+ **SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11150)
![architecture](https://img.shields.io/badge/Conversational_Speech_Corpora-red)
![task](https://img.shields.io/badge/Multi_Party_Conversation-magenta)
![organization](https://img.shields.io/badge/ASLP_NPU-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大音频语言模型的进展推动了自然智能语音交互系统的发展，这类系统需要建模复杂对话行为，包括话轮转换、重叠语音与说话者协调。多方对话为研究这些行为提供了现实设定，但既有普通话对话语料往往……**</p>

+ **STEMMA: Song-to-Stem Multi-Audio Reasoning for Large Audio Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11884)
![architecture](https://img.shields.io/badge/Multi_Audio_Reasoning_Framework-red)
![task](https://img.shields.io/badge/Music_Understanding-magenta)
![organization](https://img.shields.io/badge/1_Graduate_School_of_Culture_Technology,_KAIST,_Daejeon,_Republic_of_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**音乐理解常需比较片段并推理歌曲、段落与音轨之间的关系。但现有大型音频语言模型与音乐问答数据集通常基于单条录音，或比较独立采样的曲目而没有已知的制作关系。作者提出多音频音乐问答框架。**</p>

+ **MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11156)
![architecture](https://img.shields.io/badge/Unified_Spatial_Audio_LM-red)
![task](https://img.shields.io/badge/Spatial_Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Xiaomi_Inc.,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**大型音频语言模型在通用音频理解上表现强，但多数为单声道输入设计，丢弃了空间感知所必需的通道间线索；而既有的空间音频语言模型是为空间任务专门设计的，无法利用单声道 LALM 的通用理解能力。**</p>

+ **EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12248)
![architecture](https://img.shields.io/badge/Proactive_Spoken_Assistance-red)
![task](https://img.shields.io/badge/Egocentric_Speech_Assistance-magenta)
![organization](https://img.shields.io/badge/Department_of_AI,_University_of_Seoul-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可穿戴 AR 助手正走向持续的真实世界交互：它们通过第一人称视频与音频感知用户活动，并在用户未明确询问时提供及时的口头指导。主动式视频助手、口语对话系统与第一人称任务理解各自进展迅速，但现有系统未处理联合问题。**</p>

