# 2026-11-06 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08092)
![architecture](https://img.shields.io/badge/E_Gaborformer-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Deepdub-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**E-Gaborformer 是严格因果的流式语音识别器，用 Gated DeltaNet-2 递归层配滑动窗口注意力、按固定因果 Gabor 原子字典构建全部时间卷积，流式状态恒定约 19MB，0.6B 模型在英语语音代理流量上 WER 比同规模 Nemotron 3.5 低 28%-31%。**</p>
+ **Fine-Tuning a Transducer for Impaired Speech: Where the Gains Appear and What They Mean for Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07587)
![architecture](https://img.shields.io/badge/Parakeet_TDT_Finetuned-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/Eloky-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在受损语音识别挑战赛 SAPC2 中，作者用公开的 Parakeet TDT 1.1B 在约 950 小时、1100 多位说话人的数据上全模型微调并做模型平均，隐藏测试集 Test1 上字符错误率 7.81%，相对官方基线 15.26% 几近减半，CPU 实时版中位延迟约 0.9 秒。**</p>
+ **THG-Omni: Traceable Human-Centric Graph Supervision for Video Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07836)
![architecture](https://img.shields.io/badge/THG_Omni-red)
![task](https://img.shields.io/badge/Omni_Understanding-magenta)
![organization](https://img.shields.io/badge/Lanzhou_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://anonymous.4open.science/r/review-n94hhfcwp5666/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**THG-Omni 用 SAM3 的人物轨迹配合带时间定位的 Qwen3-VL 标注构造可追溯的图监督，候选语义声明在用于造训练问题前会对照源视频与可用音轨核验；NExT-QA 上配对图输入比无图输入高 4.44 个百分点，紧凑图甚至略优于完整图。**</p>
+ **Where Do Reported Long-Video QA Gains Come From? A Controlled Audit of Frame Selection, Evidence Injection, and Expert Routing**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07329)
![architecture](https://img.shields.io/badge/VideoRouteAudit-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mikeslin-ir/long-video-qa-audit)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VideoRouteAudit 固定骨干、帧预算、解码与评分器，只改动一个决策来审计长视频问答：n=900、K=8 的 Video-MME 长桶上帧选择器最大收益仅 +1.9 点，与均匀采样无法区分，而 ASR 转写注入的方向性影响最大可达 -13.0 点。**</p>
+ **A Unified Multi-Encoder Framework for Music Lyric Intelligibility Assessment: Bridging Invasive and Non-Invasive Paradigms**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07485)
![architecture](https://img.shields.io/badge/Multi_Encoder_Lyric_Scoring-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向音乐歌词可懂度评估的统一多编码器框架同时支持有参考与无参考两种建模路径，组合 WavLM 的声学-语义对齐、MuQ 的全局音乐结构与 Whisper 转写文本线索，在 ICASSP 2026 Cadenza 上取得 26.61 RMSE，比基线改进 9.2%。**</p>
+ **Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07718)
![architecture](https://img.shields.io/badge/MIIB-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Southwestern_University_of_Finance_and_Economics-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/wanglingzaishi/MIIB)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MIIB 以部分信息分解为基础，显式编码多模态交互中的冗余、独有与协同信息，用变分界与基于分数的熵估计构造可优化的代理目标，平均准确率 66.73% 对基线 64.45%，在 MOSI 等四个数据集上分别提升 3.7 至 1.6 个百分点。**</p>
+ **Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07755)
![architecture](https://img.shields.io/badge/Video_To_QA_Pipeline-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/Sardar_Vallabhbhai_National_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频转问答的自动化流水线用 Whisper 转写、BART 分段摘要与 Llama-3.1-8B-Instruct 自校验生成候选问答，只保留通过校验的对再用 LoRA 微调；LoRA 把可训练参数降到最多万分之一，但人工评测仅抽取了 25 对样本。**</p>
+ **Automatic keyphrase extraction and annotation: modern theoretical approaches and practical solutions for text and speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08006)
![architecture](https://img.shields.io/badge/Keyphrase_Extraction_Survey-red)
![task](https://img.shields.io/badge/Speech_Summarization-magenta)
![organization](https://img.shields.io/badge/Saint-Petersburg_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇综述系统梳理文本与语音的关键短语抽取路线，从统计、混合、机器学习、结构化方法一路讲到 LLM 生成式抽取，并对比语音场景下转写式与端到端声学两条路线，把低资源语言数据稀缺与生成式抽取评测列为主要瓶颈。**</p>
+ **Linguistic boundaries emerge from pressure-constrained processing dynamics**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08085)
![architecture](https://img.shields.io/badge/Pressure_Constrained_Boundary_Model-red)
![task](https://img.shields.io/badge/Phonological_Knowledge-magenta)
![organization](https://img.shields.io/badge/Universitat_Pompeu_Fabra-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文主张语言边界由维持未决依赖、整合已完成关系与更新语境三种压力的相互作用涌现：不含预置边界的生成式模拟自发产生句子级片段长度分布，50 名听者在 5140 个候选词位上的边界选择与这些压力显著相关。**</p>
+ **Improving the Clinical Generalizability of Machine Learning-Based Alzheimer's Disease Detection Across Domains and Modalities: A Comprehensive Review**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08188)
![architecture](https://img.shields.io/badge/AD_Detection_DA_DG_Review-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Alberta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**阿尔茨海默病检测的域适应与域泛化综述最终纳入 83 项研究，分为神经影像 31 项、眼动 15 项、语音与文本 14 项、EEG 10 项与多模态 13 项；语音方向因跨数据集与跨语言迁移困难成为泛化瓶颈。**</p>
