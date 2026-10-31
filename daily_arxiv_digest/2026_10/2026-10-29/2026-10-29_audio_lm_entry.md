# 2026-10-29 - 音频与语音语言模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Beyond Aggregate WER: In-domain Adaptation, Learner Speech, Code-Switching, and Speaker Attribution in Online Spanish Learning Classrooms**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38016)
![architecture](https://img.shields.io/badge/Condition_Aware_ASR_Evaluation-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Arizona_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把在线 L2 西班牙语课堂的 ASR 评测按说话人角色与语言上下文拆开，比较平台集成、开放权重、适配与商业四类系统，结论是域匹配比数据量更关键，且 LoRA 适配的 MOSS 在 WER 与 CER 上与商业系统相当并取得更低 DER。**</p>
+ **Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38570)
![architecture](https://img.shields.io/badge/HEAR_Acoustic_Evidence_Probing-red)
![task](https://img.shields.io/badge/Audio_Reasoning-magenta)
![organization](https://img.shields.io/badge/Microsoft-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HEAR 用疼痛切片检验音频大模型能否利用副语言线索：在只能从声音推断疼痛的 Harvard 句子上七个模型全部处于随机水平，但分层 probing 显示疼痛可从早期音频表征解码，把线索改写成文本回注 prompt 又能让成对预测提升 32 点。**</p>
+ **Depth through Recurrence: Towards Ultra-Efficient On-Device ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37833)
![architecture](https://img.shields.io/badge/Block_Recurrent_ASR-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Qualcomm_AI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**作者发现大型 ASR 模型多数层学到功能相似的变换，据此提出 block-recurrent 架构，用少量权重共享的循环块取代参数化深度，经表征引导分组与蒸馏后参数量少一个数量级，两个共享块即可平均恢复大型模型 97.4% 的准确率，并支持轻量 MoE-LoRA 端侧个性化。**</p>
+ **"It Would Make a Geordie Feel at Home": Regional Accent Perceptions and Speech Accommodation in Voice AI**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38005)
![architecture](https://img.shields.io/badge/Wizard_of_Oz_Accent_Accommodation_Study-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Heinrich_Heine_University_Düsseldorf-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究让纽卡斯尔英语使用者与说 Newcastle English 或标准南英英语的模拟语音助手交互并做半结构化访谈，发现地域音色虽带来温暖与归属感却折损权威感，用户在识别失败时会主动改用主流口音，暴露双向的语音偏置。**</p>
+ **MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38276)
![architecture](https://img.shields.io/badge/MixCardBench_Structured_Captioning-red)
![task](https://img.shields.io/badge/Audio_Captioning-magenta)
![organization](https://img.shields.io/badge/New_Jersey_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://mixcards-anon.github.io/mixcards-demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MixCardBench 用 4884 个最多九源重叠的合成声景评测复音音频的结构化描述，要求模型先定位声源再逐源生成语义、时间与声学属性卡片，六个大型音频语言模型中最强者的平均字段分仅约 60%。**</p>
+ **Improving the Dependency on Fine-Tuning Data in Transfer Learning for Speech Emotion Recognition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38050)
![architecture](https://img.shields.io/badge/fMLLR_Autoencoder_Compensation-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Chile-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用 fMLLR 构造补偿机制，在 encoder latent space 上以仿射变换刻画旋转与平移来缓解声学环境造成的训练测试错配，在人机交互的语音情感识别任务上仅用 12.9% 训练集就带来平均 CCC 16.8% 的提升。**</p>
+ **QMUL_AK at AISA-ArabicFC: Schema-Constrained Function Calling with ALLaM**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37995)
![architecture](https://img.shields.io/badge/ALLaM_LoRA_Schema_Constrained_Calling-red)
![task](https://img.shields.io/badge/Audio_LM-magenta)
![organization](https://img.shields.io/badge/Queen_Mary_University_of_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**QMUL_AK 用 LoRA 把 ALLaM-7B-Instruct 适配到阿拉伯语 function calling，配合 schema-aware prompt、方言与 no-call 重采样和确定性校验，盲测总分 A、B 各为 0.9253 与 0.9380，并在 21 队中拿下方言鲁棒性诊断第一。**</p>
+ **Implicit Minor Detection from Multi-Turn Dialogue in High-Risk AI Interactions: A Constrained Self-Evolving LLM Harness**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38546)
![architecture](https://img.shields.io/badge/Maker_Checker_Harness_Implicit_Minor_Detection-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把弱身份条件下判断对话者是否为未成年人形式化为高风险用户属性推断，用 LLM 加 Harness 与 Maker-Checker 协议控制触发时机并要求结构化证据，在 8328 段多轮中文对话上把平均精确率与未成年人类 F1 提升 7.60 与 6.37 个百分点。**</p>
+ **Effects of Deep Learning Architecture and Pretraining on Automated Vocal Fold Segmentation in Ex Vivo High-Speed Phonation Images**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37860)
![architecture](https://img.shields.io/badge/Pretrained_Transformer_Segmentation_Benchmark-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Cincinnati-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在离体犬喉高速成像的二维喉内粒子图像测速上比较 UNet、UNet++、TransUNet 与 Swin-UNet，六条流水线用 16344 张标注图训练，平均 Dice 仅在 0.9734 至 0.9764 之间，差异主要体现在 ImageNet 预训练带来的边界保真度提升。**</p>
+ **The Artificial Personality Model: Theory, Implementation, Measurement and Experimental Validation in Conversational Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38608)
![architecture](https://img.shields.io/badge/APM_Artificial_Personality_Questionnaire-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Karlsruhe_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文改进并实证评估融合人本与机器专属维度的 Artificial Personality Model，在三个实验共 395 人条件下用自建 APQ 问卷测量，识别出额外机器人格维度，并验证人工人格对满意度、持续使用意愿与社会临场感有显著影响。**</p>
