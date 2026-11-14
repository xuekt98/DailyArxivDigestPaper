<!-- direction: duplex_speech_core -->

+ **An LLM Is All You Need: Data-Efficient Adaptation to Full-Duplex, Word-Level Spoken Dialogue**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14774)
![architecture](https://img.shields.io/badge/Thinker_Talker_Cascade-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/AveraLabs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**冻结 Qwen3-Omni-30B-A3B，只训 97.4M 参数的适配器与 17 个时间 token，在 80 ms 帧时钟上用约 30 GPU 小时完成四阶段课程，把只会轮次对话的多模态大模型改造成逐词级全双工语音系统。**</p>

+ **Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16371)
![architecture](https://img.shields.io/badge/Structured_Speaker_Conditioning-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出结构化说话人条件化，把局部活动结构与会话级声学身份拼成条件调制声学编码器，只加 1.46M 参数就让 Qwen3-ASR-0.6B 在四个会议集上相对四状态对角条件平均降 6.23% 的 cpER。**</p>

+ **Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16933)
![architecture](https://img.shields.io/badge/Decide_Then_Separate-red)
![task](https://img.shields.io/badge/Speech_to_Speech-magenta)
![organization](https://img.shields.io/badge/Manifestro-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Manifestro/kezek)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Kezek 把单声道双人对话整段还原成一路一人、时长与时序不变且两轨之和恒等于原音，短回应保留率 0.83 对 0.69、覆盖率 1.000，每 GPU 小时处理 231 小时音频，比基线快 4–5 倍。**</p>

+ **Duo: A Reciprocal World Model for Full-Duplex Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15131)
![architecture](https://img.shields.io/badge/Reciprocal_World_Model-red)
![task](https://img.shields.io/badge/Full_Duplex-magenta)
![organization](https://img.shields.io/badge/Ant_Group_inclusionAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://duo-v1.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ant Group 提出互惠世界模型，把智能与物理现实并列，拆出 Intent 与 Realization 两种能力；Duo v1 以 17 帧为一块（约 0.71 s）推进全双工交互，模块掩码保证因果，双 rollout 蒸馏缓解分布漂移。**</p>

+ **RSE-TTS: Compact Text-to-Speech through Shared Text-Aware Reference Encoding and Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15464)
![architecture](https://img.shields.io/badge/Reconstructive_Speaker_Encoder-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/VoxNexus-green)
[![project](https://img.shields.io/badge/project-blue)](https://voxnexusai.github.io/RSE-TTS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RSE-TTS 让预训练 TTS 骨干兼任参考编码器，把参考文本与语音压成 8 个连续向量，编码加生成的参数从 228.5M 降到 118.2M，在 Seed-TTS、CV3-eval、MiniMax 三个英文基准上同时改善 WER 与说话人相似度。**</p>

+ **Low Language Transfer Speech-to-Text**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16260)
![architecture](https://img.shields.io/badge/Low_Language_Transfer_SFT-red)
![task](https://img.shields.io/badge/Low_Resource_ASR-magenta)
![organization](https://img.shields.io/badge/Scicom_MSC_Berhad_Malaysia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给 28 个多语种开源语音识别模型在 50 种低资源语言上直接打分，再用每语言最多 1,000 段、共 82 小时微调其中 24 个，宏 CER 全线下降 16.6 到 53.1 点、最好 9.5，随机初始化对照组始终落后 60 点以上。**</p>

+ **Beyond Word Error Rate: A Failure Taxonomy of Streaming Dictation ASR**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16919)
![architecture](https://img.shields.io/badge/Streaming_ASR_Failure_Taxonomy-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/HeyLemon_heylemon.ai-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/heylemon-ai/streaming-dictation-asr)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 106 段英语听写流式送给 11 个 ASR 系统，按识别、输出格式、语言处理、模型前丢弃四层归类错误；安静英语 WER 几乎相同的两个系统，耳语下分别是 34.7% 与 8.8%，代码与全部录音已开源。**</p>

<!-- direction: speech_rl -->

+ **JEV-VAD: Efficient Semantic Endpointing via Task-First Conditioning and Decoder-Prefix Pruning**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15362)
![architecture](https://img.shields.io/badge/Task_First_Scalar_Endpointing-red)
![task](https://img.shields.io/badge/RL_for_ASR-magenta)
![organization](https://img.shields.io/badge/Tianjin_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**JEV-VAD 是 ASR-free 的语义端点检测：问题与完成标准前置到音频之前，标量头仅 1025 个参数输出停止概率，先 SFT 再用 RLCD 对 32 个采样动作做策略更新，在 14 语言 EOT-bench 上取得最低的中文 cut@300ms 19.57%。**</p>

+ **DeALR: Decoupled Audio-Latent Optimization with Acoustic Backtracking for Test-Time Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15439)
![architecture](https://img.shields.io/badge/Decoupled_Audio_Latent_Reasoning-red)
![task](https://img.shields.io/badge/Audio_RL-magenta)
![organization](https://img.shields.io/badge/HKUSTGZ-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DeALR 让冻结的音频语言模型在测试时主动回溯关键声学片段：只优化 32 个可学习向量，MMAR 从 57.7 升至 60.3、MMAU 从 70.2 升至 73.1、AudioMCQ 从 83.4 升至 88.4，且合成前复原原始音频嵌入。**</p>

+ **ZONOS3-Mini Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16525)
![architecture](https://img.shields.io/badge/Latent_MoE_TTS_Backbone-red)
![task](https://img.shields.io/badge/GRPO_Speech-magenta)
![organization](https://img.shields.io/badge/Zyphra-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Zyphra/ZONOS3-Mini)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ZONOS3-Mini 用 886M 总参、每 token 只激活 100M 的潜空间 MoE 骨干，配合 44.1 kHz、15 Hz 帧率的 ZAC-1 编解码器，在 55 个语言集上宏平均 WER 6.71%，后训练用 DPO 加 GRPO 修失败模式，可在笔记本与手机上实时零样本克隆。**</p>

