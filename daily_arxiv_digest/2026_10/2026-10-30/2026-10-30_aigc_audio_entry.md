# 2026-10-30 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Discovering Interpretable Acoustic Features in Autoregressive Voice-Cloning TTS Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40505)
![architecture](https://img.shields.io/badge/SAE_Probing_Steering_Framework-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/University_of_Texas_at_Austin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出面向自回归 voice-cloning TTS 的特征级可解释性框架，用 SAE、PCA 与随机方向配合稀疏 probing、steering 和 auto-interpretability，量化了 probing 强度与可 steering 性之间的错位。**</p>
+ **Array-Agnostic High-Order Ambisonics Encoding via Diffusion Posterior Sampling**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39185)
![architecture](https://img.shields.io/badge/ADEUPS_Diffusion_Posterior_Sampling-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Ben-Gurion_University_of_the_Negev-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ADEUPS 把与阵列无关的 Ambisonic 扩散先验与显式物理采集模型在推理阶段耦合，用 order-masking 训练与 score blending 采样，在多种阵列几何上 zero-shot 完成高阶 Ambisonics 的编码与升阶。**</p>
+ **What Makes a Good Audio Prompt for Zero-Shot TTS? Learning Prompt Selection from Synthesis Outcomes**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40372)
![architecture](https://img.shields.io/badge/Prompt_Selector_Network-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/The_Hebrew_University_of_Jerusalem-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文分析了四个零样本 TTS 模型从 YouTube 候选 prompt 合成出的数十万条输出，发现 prompt 选择同时决定可懂度与相似度，并训练出一个只看音频的小网络，把留出集词错误率相对随机选择降低三分之一到五分之二。**</p>
+ **SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40640)
![architecture](https://img.shields.io/badge/SonoWorld4D_Dual_Space_Audio_Diffusion-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland,_College_Park-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SonoWorld4D 提出 Video-to-4DAVScene 任务，从单目视频生成 360 度背景与发声物体的运动轨迹，并用 dual-space audio diffusion synchronization 合成物理可解释的多声源空间声场，支持实时新视角视听渲染。**</p>
+ **AKDQ: Adaptive Key-Delta Quantization for Low-Bitrate RVQ-based Neural Speech Codecs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39885)
![architecture](https://img.shields.io/badge/AKDQ_Key_Delta_Quantization-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AKDQ 把 RVQ 固定的逐帧码本分配换成自适应的 key 或 delta 策略，由带预算的因果调度器经 bit-bank 决策，在 DAC 上以 1.5 kbps 达到基线 2.0 kbps 的重建质量，省下 25% 码率且无需修改编解码器主干。**</p>
+ **Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39168)
![architecture](https://img.shields.io/badge/Reading_Level_CTC_Verifier-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Best_AI_Co.,_Ltd.,_Tokyo,_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文指出用 ASR 转写加假名比对来复检日语 TTS 的做法双向都不可靠，改用 CTC 假名识别器给预期读音及易混淆读音打分，在 540 条注入误读上把误读检出率提到 91.7% 且误报率仅 5.0%。**</p>
+ **Toward Complete Speaker Anonymization: a Streaming Cascaded System for Voice Privacy and PII Removal**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39754)
![architecture](https://img.shields.io/badge/ASR_NLP_TTS_Privacy_Cascade-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/Center_for_Language_and_Speech_Processing,_Johns_Hopkins_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 ASR 加 NLP 加 TTS 的级联流式语音隐私系统，NLP 模块负责删除 PII，端到端延迟 717 ms 时在 Librispeech 上保持 11% WER，PII 检测达到 69% SLU F1，并对半知情攻击者最高取得 47.66% EER。**</p>
+ **Automated Parameter Sensitivity Ranking in Audio Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38740)
![architecture](https://img.shields.io/badge/Sweep_Sobol_Sensitivity_Framework-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Bahçeşehir_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出先测量后验证的两阶段参数敏感度排序框架，用 -23 LUFS 归一化与五种频谱指纹抑制增益干扰，以 101 步扫描和 128 点 Sobol 激励给参数打分，在五个软件合成器上取得 0.82 到 0.96 的排序相关性。**</p>
+ **Personalising Parametric Audio Effect Recommendation for Vocals from Parameter-only Style Priors**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38696)
![architecture](https://img.shields.io/badge/Parameter_Only_Style_Prior_Recommender-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/C4DM,_Queen_Mary_University_of_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把人声效果链中工程师的风格建模为参数分布，在 label-shift 假设下由内容模型、参数总体模型与工程师先验闭式推出个性化推荐，无需配对音频或调权重，14 人听测可区分度达 89.3%。**</p>
+ **Structured Pruning of Feedback Delay Networks**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38768)
![architecture](https://img.shields.io/badge/Staged_FDN_Structured_Pruning-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/AudioLab,_University_of_York-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出面向 FDN 的结构化剪枝，把反馈矩阵换成固定置换加小型正交块的分级结构，导出了精确条件块更新与幅度响应精修，在 Apple M2 上相对稠密 BLAS 取得约三倍到二十倍以上的反馈乘法加速。**</p>
