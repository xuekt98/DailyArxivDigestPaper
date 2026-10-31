# 2026-10-29 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **A Tutorial on Generative Models for Music Audio**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38252)
![architecture](https://img.shields.io/badge/Music_Audio_Generative_Models_Tutorial-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Warsaw_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一本 132 页的音乐生成专著，用统一记号梳理 neural audio codec、自回归与 masked token 模型、diffusion 与 flow matching、采样加速与 preference optimization，并覆盖评测、听测设计与版权争议。**</p>
+ **Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38384)
![architecture](https://img.shields.io/badge/Qwen3_TTS_Pronunciation_Supervision-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Laneguage-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 12.8 小时 Common Voice 语音把 Qwen3-TTS 适配爱尔兰语，跨语料 CER 0.225，优于从零训练与 zero-shot cloning；把 Wiktionary 记录做成 phoneme critic 作 verifier 做 rejection fine-tuning，CER 降到 0.159。**</p>
+ **DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38316)
![architecture](https://img.shields.io/badge/DRC_TTS_Dual_Resolution_Codec-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Universiti_Sains_Malaysia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DRC-TTS 针对低帧率离散 codec 下字符时长被量化成 0 帧、导致发音遗漏的问题，先在 50 Hz 展开字符表征再降采样到 12.5 Hz 做 token 预测，把马来语语音合成 CER 从 27.11% 降到 21.86%，MOS 由 4.12 升到 4.30。**</p>
+ **Beyond Utterance-Level Speaker Similarity: Perception-Aligned Segmental Evaluation of Accent in Speech Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37912)
![architecture](https://img.shields.io/badge/Segmental_Accent_Evaluation_Protocol-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/Centre_for_Speech_Technology_Research,_University_of_Edinburgh-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/BytedanceSpeech/seed-tts-eva)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**作者提出分段式口音评测协议，把相似度评分与目标地区听者给出的 subword 级差异标注结合，在 200 对样本上验证了 subword 标注会给出不同于相似度评分的系统排序，同时发现七种客观距离与该标注的相关性最高仅 0.22。**</p>
+ **MiDiff: MIDI-Conditioned Diffusion Models for Drum Audio Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38619)
![architecture](https://img.shields.io/badge/MiDiff_MIDI_Conditioned_Diffusion-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Bar-Ilan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MiDiff 在复数 STFT 域用 MIDI piano roll 条件化扩散反向过程修复鼓组，结合预训练 MIDI encoder 与 early injection、FiLM、cross-attention 三种条件方式，证明只用 classifier guidance 的符号先验无增益，混合调度再降 47% FAD。**</p>
+ **SelectSep: Target-Selective Video Queries for Audio Source Separation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38624)
![architecture](https://img.shields.io/badge/SelectSep_Text_Click_Conditioned_Separation-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Korea_Advanced_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SelectSep 用文本加单次点击坐标共同指定目标声源与实例，推理时无需分割掩码：先以 target-feature distillation 适配视觉编码器，再微调分离器，并在新增的 on-screen interference 设定下验证语义相近声源的选择性提升。**</p>
+ **Who Called? V33DA: A Physically Verified Multimodal Benchmark for Vocal Attribution in Zebra Finch Groups**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38109)
![architecture](https://img.shields.io/badge/V33DA_Accelerometer_Verified_Attribution-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Institute_of_Neuroinformatics,_University_of_Zurich_and_ETH_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**V33DA 是面向社交斑胸草雀叫声归属的多模态基准，含 33625 个经加速度计振动信号核验的事件，耦合 5 通道音频、三机位与 3D 位姿，评测显示依赖熟悉嗓音身份的方法在换到未见个体时急剧退化。**</p>
+ **ODAQ-Collection: Expanding the Open Dataset of Audio Quality with a Focus on Spatial Distortions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37959)
![architecture](https://img.shields.io/badge/ODAQ_Spatial_Distortion_Subset-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Netflix-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ODAQ 新增空间失真子集，用 148 对高质量音乐与语音立体声样本做受控双耳线索失真与对白增强，使数据集扩到 688 对、覆盖 17 类处理方法并附 18984 条主观评分，为客观音质指标研究提供开放资源。**</p>
+ **Universal Short-Time Fourier Transform: Data-Adaptive Window-Length Selection for Time-Frequency Analysis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37795)
![architecture](https://img.shields.io/badge/U_STFT_Window_Length_Trellis-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Stony_Brook_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**U-STFT 把 STFT 的时频分辨率折中建成序列决策问题，用归一化三阶 Rényi entropy 逐帧给候选窗打分，并由 window length trellis 以每帧线性复杂度聚合出指数级的候选调度，兼顾自适应分辨率跟踪与精确 overlap-add 重构。**</p>
+ **Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37906)
![architecture](https://img.shields.io/badge/HRF_Res_Harmonic_Resonate_Fire_Reservoir-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Delft_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HRF-Res 把 liquid state machine 中的 LIF 神经元换成具备内禀振荡的 Harmonic Resonate-and-Fire 神经元群，让储备池具备频率选择性表征，在时间序列、序列图像、音频脉冲列等十个基准上领先脉冲储备池方法，能耗最多降低 19 倍。**</p>
