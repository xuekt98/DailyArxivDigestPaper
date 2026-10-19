+ **Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.23678)
![architecture](https://img.shields.io/badge/TTS_Conditioning_Failure_Characterization-red)
![task](https://img.shields.io/badge/Zero_Shot_Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/1Univ_Toulon,_Aix_Marseille_Univ,_LIS,_CNRS,_France;_2Mila_–_Quebec_AI_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Qwen3-TTS 报告了 SOTA 的零声纹克隆，但其技术报告留下了几个未回答的问题：模型**应当如何被条件化**、在朗读语音之外表现如何、以及如何失败。作者刻画其两种克隆接口（ICL 与 X-Vector），并与 Chatterbox、XTTS-v2、F5-TTS 对比（摘要在此处截断）。**</p>

+ **DriftTTS: One-stage Single Step Text-to-Speech via Generative Drifting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22960)
![architecture](https://img.shields.io/badge/Generative_Drifting_OneStep-red)
![task](https://img.shields.io/badge/Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/Department_of_AI,_University_of_Seoul,_Seoul,_South_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于得分匹配与流匹配的文本到语音模型能产生自然语音，但只能通过**多次调用解码器**做到，这使合成缓慢。减少调用次数的既有做法要么从多步教师蒸馏，要么在预训练模型之上加一个阶段（摘要在此处截断）。**</p>

+ **Semantic-Critical Regions for Video-to-Audio Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.23021)
![architecture](https://img.shields.io/badge/Semantic_Critical_Region_Conditioning-red)
![task](https://img.shields.io/badge/Video_To_Audio_Generation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在真实视频中，声音事件常与**局部化、细粒度**的视觉线索相关联，如物体运动、物体部件动态、接触事件与物体间交互。既有视频到音频（V2A）方法使用基于全局视觉表示的隐式条件或显式……（后续详见正文）。**</p>

+ **Bridge, Distill, Refine: High-Fidelity One-Step Generation for Multi-Bandwidth Speech Extension**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22910)
![architecture](https://img.shields.io/badge/Bridge_Distill_Refine_BWE-red)
![task](https://img.shields.io/badge/Speech_Bandwidth_Extension-magenta)
![organization](https://img.shields.io/badge/1Shanghai_University,_Shanghai,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音带宽扩展（BWE）旨在从带限语音中恢复缺失的频谱内容。然而多数生成式 BWE 方法为固定输入带宽设计，且依赖迭代采样，限制了其灵活性与效率（摘要在此处截断）。**</p>

+ **MUB: An Identity-Masked Benchmark for Music Understanding in Multimodal Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22989)
![architecture](https://img.shields.io/badge/Identity_Masked_Benchmark-red)
![task](https://img.shields.io/badge/Music_Understanding_Evaluation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**评估多模态语言模型的音乐感知，需要把**音频证据**与可从元数据或外部工具恢复的答案分离。作者提出音乐理解基准（MUB）——一个本地组装的 500 条**身份遮蔽**录音集合，带有速度等既有标注（摘要在此处截断）。**</p>

+ **Too Emotional to Be Fake? Intra-Utterance Emotion Shifts Expose Failure Modes in Speech Deepfake Detectors**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22832)
![architecture](https://img.shields.io/badge/Emotion_Shift_Deepfake_Audit-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**富有表现力的语音合成现在能在**单条话语内部**改变情绪，但其对深伪检测的影响仍不清楚。作者引入 EmoShift 基准，比较情绪稳定（AA）与情绪变化（AB）的语音，同时控制静态情绪身份与声学……（摘要在此处截断）。**</p>

+ **Rethinking Magnitude Compression in Spectral Losses for DDSP Parameter Estimation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22962)
![architecture](https://img.shields.io/badge/Spectral_Loss_Magnitude_Compression-red)
![task](https://img.shields.io/badge/DDSP_Parameter_Estimation-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign,_Siebel_School_of_Computing_and_Data_Science,_USA_61801-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可微数字信号处理（DDSP）的谱损失常压缩幅度，例如使用对数幅度项。这种压缩模仿人类感知，但它是否**有助于优化**并不清楚，且通常只能通过比较训练好的模型才发现（摘要在此处截断）。**</p>

+ **Interpreting SSL Representations for Spoof Detection: a WavLM Study**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.23526)
![architecture](https://img.shields.io/badge/SSL_Layer_Interpretability-red)
![task](https://img.shields.io/badge/Spoof_Detection-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WavLM 等自监督语音模型在伪造检测上表现强劲，但哪些层编码了最多与伪造相关的信息、它们捕获何种声学性质仍不透明。作者在 ASVspoof 5 数据库上做逐层可解释性研究（摘要在此处截断）。**</p>

+ **Known Music, Unknown Response: Leakage-Audited Dynamic Arousal Forecasting With Scheduled Future Music** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.23063)
![architecture](https://img.shields.io/badge/Leakage_Audited_Arousal_Forecasting-red)
![task](https://img.shields.io/badge/Music_Emotion_Recognition-magenta)
![organization](https://img.shields.io/badge/1School_of_Computer_Sciences,_Universiti_Sains_Malaysia,_11800,_Pulau_Pinang,_Malaysia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**动态音乐情感识别通常从**已观测**的音频估计同时或滞后对齐的标签。我们改为预测**未来音乐已被排定但后续情感标签仍隐藏**时共识唤醒度的变化。评测按完整歌曲留出（摘要在此处截断）。**</p>

+ **Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.23409)
![architecture](https://img.shields.io/badge/Memory_Efficient_RNN_T-red)
![task](https://img.shields.io/badge/Streaming_ASR_Training-magenta)
![organization](https://img.shields.io/badge/95%_of_its_peak_throughput.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**循环神经网络 transducer（RNN-T）仍是流式语音识别的实用选择，但训练需要巨大的中间张量。本文提出 Flash RNN-T，结合专用内核与可选的分块重计算（摘要在此处截断）。**</p>

