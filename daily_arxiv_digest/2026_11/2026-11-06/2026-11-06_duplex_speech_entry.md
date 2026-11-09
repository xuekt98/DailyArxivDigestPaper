# 2026-11-06 - 全双工语音与语音 LM 条目目录（7 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08092)
![architecture](https://img.shields.io/badge/E_Gaborformer-red)
![task](https://img.shields.io/badge/Streaming_ASR-magenta)
![organization](https://img.shields.io/badge/Deepdub-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**E-Gaborformer 把 Gated DeltaNet-2 递归层与滑窗注意力按 3:1 混合，所有时间卷积由 16 个固定因果 Gabor 原子线性组合而成，使每路流式状态恒定在约 19 MB；在英文语音代理流量上比同规模 Nemotron 3.5 ASR Streaming 低 28–31% 的 WER。**</p>
+ **Route-DMD: Distribution Matching Distillation with Task-Routed Mechanism for Speech Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08011)
![architecture](https://img.shields.io/badge/Route_DMD-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University_X-LANCE_Lab-green)
[![project](https://img.shields.io/badge/project-blue)](https://route-dmd.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Route-DMD 证明分布匹配目标并非对所有语音任务都成立，把分离任务路由到回归损失后，用两阶段蒸馏把学生压到 4 步且无需 CFG，端到端 RTF 从 0.4333 降到 0.0958，在生成、编辑与处理任务上基本保持 32 步教师的水平。**</p>
+ **VoxCanvas-41M: A Large-Scale Bilingual Dataset for Instruction-Based Speech Editing and Its Learning Dynamics**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08251)
![architecture](https://img.shields.io/badge/VoxCanvas_Edit-red)
![task](https://img.shields.io/badge/Speech_Editing-magenta)
![organization](https://img.shields.io/badge/X-LANCE_Lab_Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://zhikangniu.github.io/voxcanvas/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VoxCanvas-41M 发布约 4100 万条中英双语语音编辑对，覆盖单段、多段、位置指代以及 39 类非语言事件的插入与删除；用 LoRA 只更新约 1.3% 参数即可把 SpeechEditBench 内容编辑平均准确率从 91.05 提到 95.22，并系统梳理了编辑能力的学习动态。**</p>
+ **Adaptive and High-Fidelity Matching Algorithm for Retrieval-Based Accent Conversion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07420)
![architecture](https://img.shields.io/badge/AA_KNN_Accent_Conversion-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/East_China_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://aa-knn-ac.github.io/demo/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AA-kNN-AC 用音素覆盖贪心选池与基于 SVD 各向异性的自适应 k（2–6）改进检索式口音转换，仅用 100 小时 LibriSpeech 训练，在 L2-ARCTIC ASI 上把 WER 从 kNN-AC 的 13.12% 降到 8.35%，VCTK P248 上 WER 5.86%、自然度 MOS 4.16。**</p>
+ **Fine-Tuning a Transducer for Impaired Speech: Where the Gains Appear and What They Mean for Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07587)
![architecture](https://img.shields.io/badge/Fine_Tuned_Parakeet_TDT-red)
![task](https://img.shields.io/badge/Speech_Recognition-magenta)
![organization](https://img.shields.io/badge/Eloky-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇记录了参加 SAPC2 障碍语音识别挑战赛的完整做法与评测反思：微调后的公开识别器在隐藏测试集 Test1 上取得 7.81% 的字符错误率（官方基线 15.26%），CPU 实时条目延迟合计约 0.9 秒，并指出复用训练句子会系统性低估误差。**</p>
+ **Design of a Speech Enhancement-Based Deep Semantic Autoencoder for Wireless Communications**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07361)
![architecture](https://img.shields.io/badge/S_DSA_Semantic_Autoencoder-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/Dalian_Maritime_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**S-DSA 把语音增强与联合信源信道编码结合，用自适应语义噪声解耦模块分离目标语音与噪声表示，AWGN 信道 0 dB 时 PESQ 达 2.05（CNN-AE 与 DeepSC-S 均为 1.73）、STOI 约 0.89，测试时关闭噪声解码分支以降低时延。**</p>
+ **Latent Terrain: Adapting Neural Audio Autoencoders as Design Materials in NIME**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07210)
![architecture](https://img.shields.io/badge/Latent_Terrain-red)
![task](https://img.shields.io/badge/Neural_Audio_Codec-magenta)
![organization](https://img.shields.io/badge/Queen_Mary_University_of_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://jasper-zheng.github.io/nn_terrain/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Latent Terrain 是把神经音频自编码器潜空间改造成可演奏声音空间的 Max/MSP 工具包，支持 RAVE、Stable Audio Open 等模型，把 10 秒音频的 215 个潜码映射成低维控制面，映射网络训练约 1.2 分钟即可收敛，并给出四位 NIME 作者的作品集。**</p>
