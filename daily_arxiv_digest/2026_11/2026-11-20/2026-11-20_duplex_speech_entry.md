<!-- direction: duplex_speech_core -->

+ **Can Omni-modal LLMs Understand Spoken Intentions?**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24706)
![architecture](https://img.shields.io/badge/O_IN_Bench-red)
![task](https://img.shields.io/badge/Turn_Taking-magenta)
![organization](https://img.shields.io/badge/Renmin_University_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://xxayt.github.io/O-IN-Bench)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**O-IN-Bench 用 1000 条中英原生音视频样本评测全模态助手是否听懂口语意图：30 组配置最佳总分仅 59.6，意图判断通过率 74.4%，而内容判断只有 42.6%，多诉求场景最好仅 25.9。**</p>

+ **21Codec: Decoder-side Speaker Control for Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24094)
![architecture](https://img.shields.io/badge/21Codec-red)
![task](https://img.shields.io/badge/Neural_Audio_Codec-magenta)
![organization](https://img.shields.io/badge/Leiden_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dcze4/21Codec)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**21Codec 是一种 0.80 kbps、50 Hz 帧率的流式神经音频编解码器，用对抗说话人分类器与 NANSY 共振峰增强从码流剥离身份，再在解码端以 ECAPA 嵌入控制音色，分块解码不再出现说话人漂移。**</p>

+ **Label-Free Role-Aware Segmentation of Classroom Recordings: Recovering the Teacher from Transferable Structure**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23609)
![architecture](https://img.shields.io/badge/Session_Relative_Role_Segmentation-red)
![task](https://img.shields.io/badge/Speech_Embedding-magenta)
![organization](https://img.shields.io/badge/University_of_Tübingen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该课堂录音教师-学生分割流水线推理端完全无标注、可跑在手机且无需逐场校准，292 段 63 位教师上教师 F1 达英文 0.81、德文 0.87，手机端实时因子约 0.18、比 pyannote 快 4.8 倍。**</p>

+ **Personalized Causal Low-Bitrate Coded Speech Restoration with Speaker Embeddings**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22620)
![architecture](https://img.shields.io/badge/Speaker_Conditioned_UBGAN-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/Fraunhofer_IDMT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在因果低复杂度 UBGAN 基础上系统考察低码率编码语音修复的个性化：嵌入条件化把 ViSQOL 从 2.80/2.92 提到 2.92/2.97、WB-PESQ 从 2.36/2.28 提到 2.47/2.34，而按聚类选模型并不稳定。**</p>

+ **Beyond Intelligibility: Fine-Grained Perceptual Assessment of Dysarthric Speech with Auditory Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23768)
![architecture](https://img.shields.io/badge/ALLM_Prompt_Conditioned_Assessment-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文首次把听觉大模型用于构音障碍语音的五维临床感知评估：Qwen2.5-Omni 自然度 ρ 达 0.828，video-SALMONN 2 Plus 清晰度 ρ 0.635、辅音精确度 0.738，通用 MOS 预训练无法替代域内临床适配。**</p>

+ **Great Listeners, Poor Decision-Makers: Rethinking Agentic Audio AI**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23847)
![architecture](https://img.shields.io/badge/Fuzzy_Decision_Gating_Layer-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇立场文章指出音频代理的瓶颈已从识别转向决策，提出独立于感知与推理的动作门控层：在真实录音上把被执行的环境对话从 41% 压到 7–10%，同时仍服务 83–85% 的有效请求。**</p>

+ **Gaspard: Expressive unified speech and gesture synthesis with continuous autoregressive flow-matching and decoupled classifier-free guidance**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24862)
![architecture](https://img.shields.io/badge/Gaspard_Unified_Speech_Gesture-red)
![task](https://img.shields.io/badge/Expressive_TTS-magenta)
![organization](https://img.shields.io/badge/Sorbonne_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tguichoux.github.io/papers/Gaspard)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Gaspard 用连续自回归加逐步流匹配统一生成语音与共语手势，并以解耦分类器自由引导重平衡两条流，在 Genea-95 上 FGD 6.56、BC 0.67，同步 MOS 3.70 已接近人类的 3.75。**</p>

