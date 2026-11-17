<!-- direction: duplex_speech_core -->

+ **Latency, Speech Recognition and Turn-Taking in Voice Agents for Spanish Phone Negotiation: An Externally Measured Comparison of Pipecat, LiveKit and GPT-Live**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19118)
![architecture](https://img.shields.io/badge/Three_Way_Voice_Agent_Comparison-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/AI_Lab_Freight_Technologies_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**统一外部实测下比较 Pipecat、LiveKit 与 GPT-Live 三种语音代理：每架构 77 通西班牙语谈判电话的内容响应中位延迟为 2616.0、3090.0、2444.8 ms，差异置信区间含 0；真正的短板是金额识别错误率 13.01%、12.61% 对 2.86%，以及插话的 ok 被当成成交。**</p>

+ **FEND: Far-End Detection in Outbound Voice AI Calls**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18050)
![architecture](https://img.shields.io/badge/Four_Class_Far_End_Detector-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Observe.AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AILabFr8tech/voice-negotiation-agents)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**外呼语音 agent 的远端判定从传统 AMD 的一位标签改成四分类：1,000 通自有外呼中真人 48.1%、语音信箱 44.6%、AI 代接 6.9%、IVR 0.4%；信箱组件 100% 准确且不误伤真人，Asterisk app_amd 默认把 65.8% 真人判成机器；AI 代接靠语音节奏达 0.952 AUC。**</p>

+ **FineSpeaker: Reliable Speaker Representation Learning at Fine Temporal Resolution**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15288)
![architecture](https://img.shields.io/badge/FineSpeaker_Frame_Level_Speaker_Encoder-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用可调 n 帧窗池化做成分辨率可控的逐帧说话人向量，再用 MSC+TCN 局部时序建模与 VAE+flow matching 解耦：VoxCeleb1-O 上 0.5 秒短语音 EER 9.12%、帧级 2f EER 4.74%，优于 ReDimNet-B4 的 11.25% 与 ERes2NetV2 的 18.10%。**</p>

+ **Marimba: A System One Model for Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18330)
![architecture](https://img.shields.io/badge/Marimba_Typed_Speech_Decision_Interface-red)
![task](https://img.shields.io/badge/Turn_Taking-magenta)
![organization](https://img.shields.io/badge/charcot.ai-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Charcot-AI/marimba-api)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用冻结的 Qwen3-ASR 0.6B 特征做成统一 typed decision 接口：词条走零样本打分、非词条走条件头、turn-end 另设 layer-18 读出。turn-end 读出在 Smart Turn 上 AUROC 0.930 对 0.982，在 ICSI 1,728 窗上 0.716 对 0.712 持平。**</p>

+ **A Systematic Study of Cross-Token Transfer for Data-Efficient Non-Verbal Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19145)
![architecture](https://img.shields.io/badge/CosyVoice_Cross_Token_Transfer_Study-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/Meta_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在固定 CosyVoice 2 配方下研究非言语语音事件之间的跨 token 迁移：只有 200 条笑声时加入 3,200 条咳嗽样本，波形级 laughter F1 从 0.170 升到 0.529，胜过单用 1,600 条笑声的 0.495；1,600 条锚点时咳嗽达 0.695，接近 6,400 条笑声的 0.697。**</p>

+ **Beyond Controllability: Speaker Diversity in Instruction-Guided Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19030)
![architecture](https://img.shields.io/badge/ITTS_Speaker_Diversity_Audit-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dlion168/ITTS-Speaker-Diversity)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首次把指令引导 TTS 的说话人多样性与真实语音对照：7 个开源系统用 Vendi 与 MPCD 测得的说话人分布全部窄于真实语音（基线 68.3），Qwen3-TTS 的女性提示多样性只有男性的 59%（16.6 对 28.1），但 6/7 系统性别控制召回仍高于 0.88。**</p>

+ **Why Do Low-Activity Speakers Disappear in Speaker Diarization? Decomposing Lost Speakers and What Training-Free Fixes Can Recover**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19160)
![architecture](https://img.shields.io/badge/Global_Assignment_Windowed_ReInference-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/panchorange/voxmap)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**拆解端到端 diarization 里丢失的说话人：Nemotron-3 八槽模型 990 条录音上的 485 个丢失者中 425 人（88%）总发言不足 10 s。≥9 人录音用窗口重跑加全局分配把丢失从 228 降到 101、DER 从 20.10% 降到 14.99%，但多余说话人从 5 涨到 50。**</p>

+ **Scaffolding Self-Transduction with Alignment Attention Mask for Aligner-Encoder ASR**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15087)
![architecture](https://img.shields.io/badge/Alignment_Attention_Mask_Scaffold-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/NTT_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把外部强制对齐路径做成编码器自注意力掩码，给 Aligner-Encoder 的自转导过程搭脚手架：掩码在训练中淡出后 LibriSpeech test-clean/test-other WER 从 3.9/6.4 降到 3.5/5.9，长句（>17 s）桶从 11.7% 降到 9.3%；oracle 掩码可达 1.2/2.9。**</p>

+ **Convolutional VocalTrax: Replacing Backpropagation Through Time with Convolution in Differentiable Articulatory Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17181)
![architecture](https://img.shields.io/badge/Convolution_Replaces_Waveguide_BPTT-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Smule_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 Pink Trombone 声道的精确频响算成因果卷积，替掉逐样本 BPTT：梯度只经 FFT 与 43 步声道递归，A100 上声道前反向快 47–63 倍。600 条 AudioMNIST 上只训真人语音的分类器对其重建识别率 14.5%（原版 10.0%），代价是 log-mel 距离高 11%。**</p>

+ **eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18529)
![architecture](https://img.shields.io/badge/Slot_Splitting_With_E_Means-red)
![task](https://img.shields.io/badge/Real_Time_Speech-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://kyudan1.github.io/eDIAR/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不改训模型，只在槽位用尽后用 e-means 拆分槽位，把流式 diarization 变成开放说话人：1.04 s 流式下 VoxConverse DER 5.8%（八槽头 6.4%、四槽 Sortformer 14.1%），20 人时错误约为头的三分之二；45 分钟会议里 Sortformer 从 23% 崩到 57%。**</p>

+ **Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16051)
![architecture](https://img.shields.io/badge/Human_Likeness_vs_Conversational_Preference-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Fluid_Concepts_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 120 条客服转写、6 个商用 TTS 系统各 8 个音色的配对选择实验里对比像真人与更愿意聊两种判断：系统被真人选中的比例从 19% 升到 36%，Cartesia 以 49% 与真人持平；两种判断的系统排名会互换（Rime 68%→49%、Google 33%→49%），三个自动自然度分数都预测不了后者。**</p>

<!-- direction: speech_rl -->

+ **Low-Latency LLM-Based Streaming Multi-Talker ASR with Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19136)
![architecture](https://img.shields.io/badge/RLVR_SA_WER_Onset_Delay-red)
![task](https://img.shields.io/badge/RLVR_Speech-magenta)
![organization](https://img.shields.io/badge/Meta_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 RLVR 后训练流式多说话人 ASR：固定角色 SA-WER 评分器把 SFT 的 20.51% 降到 13.14%，角色互换错误由 3.2%/5.0% 降到 0.5%/0.3%；叠加 onset 延迟奖励后 p50 从 0.918 s 降到 0.320 s、p90 降到 0.780 s，SA-WER 12.70%。**</p>

