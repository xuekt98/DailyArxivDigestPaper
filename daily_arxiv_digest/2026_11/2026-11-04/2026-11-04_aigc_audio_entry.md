# 2026-11-04 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **TTSonic: A Unified Framework for Composable and Controllable Speech Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04282)
![architecture](https://img.shields.io/badge/Semantic_Acoustic_Disentangled_TTS-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/ByteDance_Douyin_Content_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://bytedance.github.io/TTSonic/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**统一可控语音生成框架 TTSonic：语义-声学解耦 tokenizer 加 Text-to-Semantic 自回归与声学流匹配渲染，重组模块即覆盖零样本 TTS、克隆、指令跟随与音色设计，零样本 test-zh 达 0.78% CER 与 0.784 SIM，中文指令跟随 APS 88.8。**</p>
+ **Detector-Guided Vocoder Training for Adversarial Text-to-Speech Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04511)
![architecture](https://img.shields.io/badge/Detector_Guided_Adversarial_Vocoder-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Dipartimento_di_Elettronica_Informazione_e_Bioingegneria_DEIB_Politecnico_di_Milano-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/polimi-ispl/adversarial-tts/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把检测器拉进训练回路的对抗 TTS 框架：不做后处理而直接微调声码器，针对 RawNet2 优化使其 EER 从 5.8% 升到 39.1%、未优化的 AASIST 也升到 21.1%，同时 FAD 由 31.25 降至 17.81，主观听感不降反升。**</p>
+ **ScrambleMark: Zero-Query Watermark-Agnostic Black-Box Evasion of Modern Speech Watermarking**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04122)
![architecture](https://img.shields.io/badge/Harmonic_Scrambling_Watermark_Evasion-red)
![task](https://img.shields.io/badge/Neural_Audio_Watermarking-magenta)
![organization](https://img.shields.io/badge/University_of_Missouri-Kansas_City-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**零查询黑盒语音水印规避攻击 ScrambleMark：论证绕过检测不必抹除水印、只需破坏其嵌入图案的结构一致性，用谐波乱序实现，在 Google SynthID、Resemble AI 与 TrustedAudio 上取得近 97% 规避率与 4.2/5 人评，并能抵抗自适应恢复。**</p>
+ **Averaging Collusion Breaks Traceability in Personalized Neural Audio Watermarking**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04400)
![architecture](https://img.shields.io/badge/Collusion_Attack_On_Personalized_Watermark-red)
![task](https://img.shields.io/badge/Neural_Audio_Watermarking-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University_Shenzhen_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Silwan5z/neural-audio-watermark-collusion-attack)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**个性化神经音频水印的串谋攻击研究：仅把两份拷贝做样本级平均，就在五个系统上造成 87.7% 到 99.7% 的追踪失败率且几乎不损音质；载荷感知混合还能把解码指向指定非成员，在 TimbreWM 上达成 92.3% 成功率。**</p>
+ **Cross-Codec Robustness in Speech Watermarking**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04716)
![architecture](https://img.shields.io/badge/Channel_Augmented_Speech_Watermarking-red)
![task](https://img.shields.io/badge/Neural_Audio_Watermarking-magenta)
![organization](https://img.shields.io/badge/Department_of_Information_and_Communications_Engineering_Aalto_University_Espoo_Finland-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ljuvela/DAREA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语音水印跨编解码器鲁棒性研究：用 Mimi（1.1 kbps）与 SNAC（0.98 kbps）做通道增广，对未见神经编解码器与传统 DSP 攻击泛化最好，但二者相互泛化很差，混响与多次重合成仍难，并提出以 DAC 为生成器的零比特水印系统。**</p>
+ **KeyWise: Efficient Video-Only Piano Transcription with a Lightweight Per-Key Architecture**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04476)
![architecture](https://img.shields.io/badge/Per_Key_Recurrent_Piano_Transcription-red)
![task](https://img.shields.io/badge/Piano_Transcription-magenta)
![organization](https://img.shields.io/badge/Department_of_Informatics_and_Telecommunications_University_of_Thessaly_Lamia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**纯视频钢琴转写的轻量逐键架构 KeyWise：利用键盘已知几何把画面切成 88 个键 ROI、由全键共享的小型循环网络逐键预测 onset、按键状态与力度，PianoVAM 上 onset F1 达 95.0% 与 97.8%，参数量 1.3M 对 28.2M 且快 4.7 倍。**</p>
+ **DGC-Net: Cross-Modal Dynamic Routing with Global-Guided Compensation in Multimodal Sentiment Analysis**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04841)
![architecture](https://img.shields.io/badge/Dynamic_Expert_Routing_MSA-red)
![task](https://img.shields.io/badge/Audio_Visual_Scene_Understanding-magenta)
![organization](https://img.shields.io/badge/College_of_Computer_Science_and_Technology_Zhejiang_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多模态情感分析框架 DGC-Net：用跨模态贡献感知的动态专家路由与全局引导的动态补偿融合，缓解情感线索不一致与全局-局部失衡，在 CMU-MOSI 上取得最佳 MAE 与 Corr、CMU-MOSEI 上 Acc-7 与 F1 领先。**</p>
+ **Therapy-FIS: A Dataset for Assessing Facilitative Interpersonal Skills in Psychotherapeutic Setting**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04645)
![architecture](https://img.shields.io/badge/Dyadic_FIS_Assessment_Benchmark-red)
![task](https://img.shields.io/badge/Audio_Evaluation-magenta)
![organization](https://img.shields.io/badge/College_of_Computer_Science_and_Artificial_Intelligence_Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**心理治疗助人技能评估数据集 Therapy-FIS：该领域首个公开专业数据，基于 890 段治疗师录像与 8 段标准化来访者片段，含面部、声学与文本信号及 8 个 FIS 分量标注，并建立两个下游任务与宏 CCC 0.2807 与 0.3299 的基线 DyadicFIS。**</p>
+ **Hybrid acoustic and pretrained embedding feature fusion for unmanned aerial vehicle detection using stacking ensemble learning under a leakage-aware evaluation protocol**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04714)
![architecture](https://img.shields.io/badge/Leakage_Aware_Drone_Audio_Detection-red)
![task](https://img.shields.io/badge/Sound_Event_Localization-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_Faculty_of_Computing_and_Information_Technology_University_of_Gujrat-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向公共无人机声学基准的泄漏感知评测工作：在 11,704 段一秒片段上用来源不相交划分评估双视图堆叠集成，平均准确率 95.29%、AUC 0.990，并指出随机划分会把准确率高估 1.89 到 3.22 个百分点，是各类声学事件基准都应自查的问题。**</p>
+ **Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04692)
![architecture](https://img.shields.io/badge/Wearable_Mediated_Discreet_Interaction-red)
![task](https://img.shields.io/badge/Audio_Effects_Design-magenta)
![organization](https://img.shields.io/badge/Universität_Siegen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可穿戴介导的隐蔽人机交互研究：用耳内音频配合有意向右歪头作为回应，在 20 对 40 人的 Wizard-of-Oz 牌局中 39/40 次信道回合按预期完成，佩戴者感知压力无显著差异，但非佩戴者的察觉与公平感反馈并不一致。**</p>
