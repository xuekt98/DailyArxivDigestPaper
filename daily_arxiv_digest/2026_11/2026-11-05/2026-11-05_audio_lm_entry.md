# 2026-11-05 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06083)
![architecture](https://img.shields.io/badge/SleuthVLM-red)
![task](https://img.shields.io/badge/Omni_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Bristol-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从不直接听音频，只用 ASR 转写加强制对齐把语音变成带时间戳文本，再交给 VLM 自主推理；在四个全模态基准上平均准确率 75.0%，比 Gemini 3.8 Flash 高 2.6 分，Video-MME-v2 达 77.8%。**</p>
+ **CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06501)
![architecture](https://img.shields.io/badge/CRESiST-red)
![task](https://img.shields.io/badge/Simultaneous_Speech_Translation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 400 毫秒声学块上交错读写语音与文本，实现全 KV cache 复用与免切分的无限长流式翻译；ACL 60/60 英德方向无分段时 COMET 85.59、LongYAAL 1.08，优于 AlignATT 的 80.83 与 1.57。**</p>
+ **Speaker-Consistent Grounding for Confusion-Resilient LLM-Based Target Speech Extraction**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06297)
![architecture](https://img.shields.io/badge/Repair_Before_Grounding-red)
![task](https://img.shields.io/badge/Target_Speech_Extraction-magenta)
![organization](https://img.shields.io/badge/UNSW_Sydney_Australia-green)
[![project](https://img.shields.io/badge/project-blue)](https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**先修证据再接地：CDCS-5 从五路冻结确定性 TSE 输出中挑出说话人一致的证据，再用代码空间接地约束 LLM 解码；干净混合下错说话人抽取率从 6.87% 降到 0.75%，噪声下从 18.95% 降到 10.46%。**</p>
+ **LibriSpeech-Real-QA: A Benchmark for Streaming Question Answering**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06496)
![architecture](https://img.shields.io/badge/LibriSpeech_Real_QA-red)
![task](https://img.shields.io/badge/Audio_QA-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 LibriSpeech 构造流式问答基准，覆盖词法与语义各自的检测和计数四类任务；词法检测上商业实时 API 平均启动延迟 4.35 到 6.52 秒、词法计数达 10.03 秒，而 400 毫秒分块流式基线 F1 达 0.993 与 0.978、延迟仅 0.661 秒。**</p>
+ **Holistic Parallel Supervision for Expressive Speech to Speech Translation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06010)
![architecture](https://img.shields.io/badge/DirectS2ST-red)
![task](https://img.shields.io/badge/Speech_to_Speech-magenta)
![organization](https://img.shields.io/badge/Center_for_Language_and_Speech_Processing_Johns_Hopkins_University_MD_USA-green)
[![project](https://img.shields.io/badge/project-blue)](https://hzted.github.io/truly-e2e-expressive-s2st-demo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把专业配音与多语种音色转换拼成内容、韵律、时间、说话人四维对齐的平行监督，并训练端到端的 DirectS2ST；英德方向 ASR-BLEU 从 6.01 升到 10.52，韵律相似从 2.162 升到 2.905，打乱配对则 BLASER 崩到 2.285。**</p>
+ **Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06043)
![architecture](https://img.shields.io/badge/Confucius4_R2T2-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/NetEase_Youdao_Beijing_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/netease-youdao/Confucius4-R2T2)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出最长稳定前缀标签，把全上下文 Qwen3-ASR-1.7B 后训练成输出永不回改的流式 ASR；使用 1,500 小时中英音频并冻结音频编码器，块长可在 80 毫秒到 2 秒间配置，在 1,860 条 Buckeye 语料上评测。**</p>
+ **Phonological Knowledge of Chinese Characters in Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05803)
![architecture](https://img.shields.io/badge/PinyinBench-red)
![task](https://img.shields.io/badge/Phonological_Knowledge-magenta)
![organization](https://img.shields.io/badge/School_of_Foreign_Languages_and_Literature_Beijing_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PinyinBench 用 38,183 个最小对比对考察模型的中文音系知识，覆盖同音判断、音素特征与多音字；17 个文本与多模态模型中前沿模型同音判断 90% 以上，仅差声调时骤降到 72%，且声调难以被激活操纵。**</p>
+ **SAUCE: Summary Analysis Using Conversation Entailment**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06812)
![architecture](https://img.shields.io/badge/SAUCE-red)
![task](https://img.shields.io/badge/Conversation_Evaluation-magenta)
![organization](https://img.shields.io/badge/RTX_BBN_Technologies_Cambridge_MA_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用对话与文本之间的蕴含关系给跨语言口语摘要做免参考评测，同时给出忠实度与覆盖率；阈值 0.9 时蕴含判定准确率 77.0%，覆盖率与真实对话质量的 Kendall 秩相关 0.677，远高于 SummaCConv 的 -0.266。**</p>
+ **Text-Only Domain Adaptation for Low-Resource Medical ASR: Shallow Fusion and Density Ratio Rescoring for Hausa**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05744)
![architecture](https://img.shields.io/badge/Shallow_Fusion_DRA-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/RUZIVO_Research_Lab_African_Leadership_University_Kigali_Rwanda-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**固定 MMS-1B-FL102 声学模型，只靠文本做低资源医疗 ASR 域适配：19,421 句 Hausa 医疗文本训练 4-gram KenLM，250 条录音跨 10 位说话人；五折交叉验证下 WER 从 29.56% 降到 23.55% 与 23.33%。**</p>
+ **Contextual Pictograms for Repairing Multilingual ASR Errors**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05637)
![architecture](https://img.shields.io/badge/Contextual_Pictogram_Repair-red)
![task](https://img.shields.io/badge/ASR_Error_Repair-magenta)
![organization](https://img.shields.io/badge/Department_Signal_Theory_Telematics_and_Communications_University_of_Granada-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向法语与西班牙语的 ASR 纠错界面提案：对低置信片段给出备选转写、局部回放与经上下文校验的象形图，对比 top-one 等三种显示条件，用最小对比对构造测试集，并按语义错配与额外交互耗时分别计数。**</p>
