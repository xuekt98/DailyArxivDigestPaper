+ **Edit Who Speaks, Control How They Speak: Global Timbre Editing and Local Instruction Control for TTS**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11437)
![architecture](https://img.shields.io/badge/Global_Timbre_Local_Instruction_Control-red)
![task](https://img.shields.io/badge/Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/1National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指令式 TTS 通过语音克隆与文本化声音设计提供对声音特征与表达的两种接口：克隆复现参考音色，文本设计从自然语言描述创造声音。但两种接口都不能让你**修改一个给定参考的音色**，并在修改的同时保持局部表达遵循指令。**</p>

+ **Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11461)
![architecture](https://img.shields.io/badge/Speech_Rewarded_Style_Planning-red)
![task](https://img.shields.io/badge/Conversational_Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/Institute_of_Science_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自然语言风格描述为 LLM 与可控 TTS 之间提供了可解释接口。但把描述当作伪标签会把目标声学压缩进文本，且描述的保真度并不蕴含对某个特定合成器的有效控制。作者实证显示：语音-文本对齐只能弱预测下游声学效果。**</p>

+ **SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11361)
![architecture](https://img.shields.io/badge/Unified_Separation_Generation-red)
![task](https://img.shields.io/badge/Audio_Video_Generation-magenta)
![organization](https://img.shields.io/badge/1Tel_Aviv_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**4D 视听场景包含视频、它所描绘的动态几何、以及充满其中的声源，每个声源都有自己的位置与轨迹。从新视角渲染这样的场景，要求每个声源都以独立波形形式可用，以便在场景中定位、传播到观察者，再混合信号。**</p>

+ **Reference-Free Singing Pitch Correction via Music-Constrained Sequence Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11524)
![architecture](https://img.shields.io/badge/Music_Constrained_Sequence_Editing-red)
![task](https://img.shields.io/badge/Singing_Pitch_Correction-magenta)
![organization](https://img.shields.io/badge/1Faculty_of_Computing,_Harbin_Institute_of_Technology,_Harbin,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**既有歌唱音高修正方法依赖目标旋律或伴奏轨，而实践中这些常常不可得。这篇把无参考歌唱音高修正形式化为音乐约束的序列编辑任务：仅从输入演唱本身判断每个音符是否以及如何被修正。**</p>

+ **Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11237)
![architecture](https://img.shields.io/badge/Chain_Of_Dancers-red)
![task](https://img.shields.io/badge/Group_Dance_Generation-magenta)
![organization](https://img.shields.io/badge/Monash_University,_Australia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**群体舞蹈生成要从音乐合成协调的多舞者编舞。该任务需要建模密集的人际依赖以保证空间协调，同时自然保留每位舞者的身份。既有方法用端到端 transformer 联合建模所有舞者，代价随人数增长。**</p>

+ **CloudEar: Integrating Perceptual, Diagnostic, and Cross-Modal Evidence for Music Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11672)
![architecture](https://img.shields.io/badge/Multi_Evidence_Music_Evaluation-red)
![task](https://img.shields.io/badge/Music_Generation_Evaluation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**评估生成音乐需要建模感知质量、技术音频质量与提示对齐。既有方法常忽视信号级缺陷、产出被压缩的质量分数，并遗漏文本提示中细粒度的音乐属性。CloudEar 是一个成对框架，整合感知、诊断与跨模态证据。**</p>

+ **Randomized Scores and Diverse Timbres: Augmenting Automatic Music Transcription with Online-Generated Data**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11197)
![architecture](https://img.shields.io/badge/Online_Generated_AMT_Augmentation-red)
![task](https://img.shields.io/badge/Automatic_Music_Transcription-magenta)
![organization](https://img.shields.io/badge/1Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自动音乐转录受限于「音频 + 精确符号标注」配对数据的稀缺。合成数据可大规模提供监督，但有效迁移究竟依赖真实的乐谱结构还是广泛的音色覆盖仍不清楚。作者通过在线采样器-渲染器流水线把这两个因素分开研究。**</p>

+ **SEER: Source-Conditioned Emotion Enhancement via Retrieval for Cochlear-Implant Speech**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11131)
![architecture](https://img.shields.io/badge/Source_Conditioned_Retrieval-red)
![task](https://img.shields.io/badge/Emotional_Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/1Department_of_Electrical_Engineering,_National_Tsing_Hua_University,_Taiwan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**人工耳蜗恢复语音通路，但削弱了声音情感识别所需的线索。既有面向人工耳蜗的增强方法要求平行的正常/强录音与强度标签。这篇提出基于检索的框架，学习哪个同情感参考能让每个源在人工耳蜗处理后仍可辨识。**</p>

+ **Prosody-to-Text: Predicting text from low-pass filtered speech**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.11544)
![architecture](https://img.shields.io/badge/Prosody_To_Text_Inversion-red)
![task](https://img.shields.io/badge/Speech_Analysis-magenta)
![organization](https://img.shields.io/badge/Faculty_of_Informatics,_Masaryk_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从文本预测韵律是成熟任务，而反方向——预测契合给定韵律模式的文本——基本被忽视。作者认为这个方向被低估，因为反向问题能带来有趣的用例。**</p>

+ **Ambient Discrete Diffusion: Using the Wrong Data at the Right Time for Data Efficient Learning** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.12340)
![architecture](https://img.shields.io/badge/Out_Of_Distribution_Diffusion_Time-red)
![task](https://img.shields.io/badge/Discrete_Diffusion_Learning-magenta)
![organization](https://img.shields.io/badge/1_ETH_Zürich,_2_Harvard_University,_3_MIT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RefineMix 框架在严重数据稀缺下训练离散扩散模型，常见于科学应用。它在选定的扩散时间步上使用分布外数据来改善泛化，同时不使采样分布产生偏置。**</p>

