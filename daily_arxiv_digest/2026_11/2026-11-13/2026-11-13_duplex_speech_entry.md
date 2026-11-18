<!-- direction: duplex_speech_core -->

+ **Hy ASR 3.0 Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14908)
![architecture](https://img.shields.io/badge/Hy_ASR_3_0-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Hy_ASR_team_Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**腾讯混元 Hy ASR 3.0 是基于 Hy3 大模型的 LLM 式 ASR 系统，支持普通话、英语与 13 个汉语方言群；公开基准聚合中文 CER 4.64%、英文 WER 5.22%、方言 4.80%，可用热词、问答对话与摘要做外部上下文偏置，并能在句内消解同音关键词。**</p>

+ **Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15691)
![architecture](https://img.shields.io/badge/Dynamic_Block_Online_Paraformer-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Apurba_NSU_R&D_Lab_North_South_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/King-Rafat/Dynamic_Streaming_ASR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向孟加拉语—英语句内切换的流式 ASR：用 VAD 触发的动态块在线推理加全局注意力保住黏着后缀，Eroot 与 Emorph 分别比 3 秒因果流式低 6 和 7 个点。**</p>

+ **Distributionally Robust BEST-RQ For Speech Representation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14801)
![architecture](https://img.shields.io/badge/DRO_BEST_RQ_KL_Regularized-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/Rensselaer_Polytechnic_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把随机量化目标按码本分成 group 做分布鲁棒优化并加 KL 正则，让 BEST-RQ 不再押注单一次随机抽样：在 Multilingual LibriSpeech 五语种上平均 WER 从均匀多码本的 8.9% 降到 λ=1.0 时的 8.4%，葡萄牙语等低资源语种收益最大。**</p>

+ **Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14929)
![architecture](https://img.shields.io/badge/T_SemAttack_ROSETok_Pipeline-red)
![task](https://img.shields.io/badge/Speech_Tokenization-magenta)
![organization](https://img.shields.io/badge/Shenzhen_International_Graduate_School_Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://wxzyd123.github.io/t-semattack)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现语音 tokenizer 在语义层极其脆弱：T-SemAttack 联合四个代理编码器做语义漂移，把 LibriTTS 上 7 个目标 ASR 的平均 WER 从 2.503% 抬到 61.348%；对应的 ROSETok 用带噪训练加鲁棒语义蒸馏，把受攻击后的下游 FSC 分数从基线最高的 35.0 提升到 77.9。**</p>

+ **Harmony: Bridging Audio Understanding and Editing through Agentic Collaboration**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14724)
![architecture](https://img.shields.io/badge/Harmony_Agentic_Audio_Editor-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Worcester_Polytechnic_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://christong9.github.io/harmony/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把音频理解与编辑接起来的智能体框架：LLM 规划器协同 Qwen3-Omni 与分析工具定位声源与时间窗，执行阶段依据中间音频做有界修正，420 条 MMAE 上精确匹配率 22.62%。**</p>

+ **Can Music Generation Models Tap Along? Evaluating Generative Approaches to Beat Tracking**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14971)
![architecture](https://img.shields.io/badge/MusicGen_Audio_Conditioning_Adapter-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Schulich_School_of_Music_McGill_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://kunfang98927.github.io/generative-beat-tracking/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把节拍跟踪改写成生成任务：给冻结的 MusicGen 加 10.4M 参数音频条件适配器生成同步打击乐轨再抽拍点，GTZAN 上 F-measure 达 0.851 且去鼓轨后掉分最少。**</p>

+ **Right Answers, Inconsistent Evidence: Source-Level Counterfactual Auditing of Large Audio-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15463)
![architecture](https://img.shields.io/badge/TRACE_Source_Level_Counterfactual_Audit-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_and_Technology_Harbin_Institute_of_Technology_Shenzhen-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yikise/TRACE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TRACE 用逐声源删除构造序数反事实检验：8 个音频语言模型在 3456 个受控混合上，18911 个正确答案中有 6.3% 存在无法用共享阈值修复的排序冲突。**</p>

+ **Evaluating AI Musical Creativity: Towards a Quantitative Multi-Dimensional Framework Based on Value, Novelty, and Surprise**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14634)
![architecture](https://img.shields.io/badge/Value_Novelty_Surprise_Metric_Ensemble-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Department_of_Arts_and_Sciences_University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 Boden 的价值、新颖、惊奇三要素操作化到音乐领域，提出一组互补的量化指标集而非单一总分，并明确这是尚待与人类判断做实证校验的概念性框架，不含实验验证结果。**</p>

