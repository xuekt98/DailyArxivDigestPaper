# 2026-10-23 - AIGC 音频生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **HeyGen Voice: Scene-Aware Voice Cloning for Talking Videos**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30470)
![architecture](https://img.shields.io/badge/HeyGen_Voice-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/HeyGen_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://heygen.com/heygen-voice)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HeyGen Voice 把「谁在说」与「在哪儿说」分离：多模态自回归 transformer 同时条件化图像、说话人字幕、场景字幕与原始录音，五阶段训练含强化与偏好优化，在 Artificial Analysis 受控音色 TTS 榜以 Elo 1201 居首。**</p>
+ **EmoFI-TTS: Face-Conditioned Expressive Voice Synthesis with Intensity Modulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30477)
![architecture](https://img.shields.io/badge/EmoFI-TTS-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Mila-Québec_AI_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EmoFI-TTS 从单张人脸推断情绪类别与强度，用跨说话人训练分离情感与声纹身份，并通过插值强度嵌入实现免训练的连续情绪控制，MEAD 上主观强度准确率达 75.2%。**</p>
+ **Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31510)
![architecture](https://img.shields.io/badge/Piano2Pop-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Piano2Pop 提出把钢琴 MIDI 扩展为器乐流行制作的新任务，用音乐生成与多声部转录造出伪配对数据，在无对齐钢琴-流行监督的情况下条件化预训练流匹配模型完成训练。**</p>
+ **CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30854)
![architecture](https://img.shields.io/badge/CAVC-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/State_Key_Lab_of_CAD&CG,_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CAVC 揭示音视频联合扩散的模态不对称可恢复性：中段只缓存音频侧去噪与跨模态注意力，视频侧保持完整精化，末端恢复少数联合步，取得 1.10–1.35× 加速且视觉动态统计反而改善。**</p>
+ **When Do Self-Supervised Representations Help Speech Restoration?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30869)
![architecture](https://img.shields.io/badge/Early_Restoration_Injection-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇系统检验 SSL 特征清洗在语音恢复中的必要性，发现严重退化下存在「感知相关性崩塌」——清洗会与恢复目标错配；并提出 ERI，把恢复骨干中间特征回注进 SSL，在 VoiceFixer 上有竞争力。**</p>
+ **HC-AINet: An Auditory-Inspired Network with Harmonic Compensation for Low-Complexity Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30818)
![architecture](https://img.shields.io/badge/HC-AINet-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Tianjin_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HC-AINet 用三角 ERB 滤波器组与倒残差 / Conformer 轻量骨干，配合谐波位置图把谐波贡献限制在选定频带，在 VoiceBank-DEMAND 上以约 0.27M 参数达到 PESQ 3.20、STOI 0.95。**</p>
+ **Measuring the Verifier's Floor: How Much Apparent Rare-Word Text-to-Speech Error Is ASR Error?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31470)
![architecture](https://img.shields.io/badge/Verifier's_Floor_Audit-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/BitmanagerAI,_Dubai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇量化了 TTS 评测的地板误差：在人类录音上评测识别器仍漏掉 33–67% 的极罕见词，直接掩蔽这些词是有偏的（其他识别器在其上的 TTS 错误率高达 4–6%），结论仍需听辨测试支撑。**</p>
+ **MQAScore: Fine-Grained Text-Music Alignment Evaluation via Large Audio Language Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31083)
![architecture](https://img.shields.io/badge/MQAScore-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MQAScore 用大音频语言模型对二元提问的肯定概率，沿流派 / 配器 / 情绪 / 人声 / 用途五个维度逐原子概念核验 text-to-music 对齐，并提出 Sensitivity-Invariance Ratio 度量评测器对语义替换的敏感性。**</p>
+ **MixJudge: Learning a Language-Queryable Critic for Vocal Mixing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30783)
![architecture](https://img.shields.io/badge/MixJudge-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MixJudge 是语言可查询的人声混音评判器：用 11 类问题、多级严重度的合成课程训练，能检索问题、区分相反问题并排序严重度，其判断还能迁移到处理候选的菜单选择。**</p>
+ **Lip-Focused Audio-Visual Consistency Detects Speech Content Manipulation beyond Coarse Synchronization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30872)
![architecture](https://img.shields.io/badge/C-MIND-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Tianjin_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**C-MIND 用帧级对齐的音频与口型运动一致性做语音内容操纵取证：不用转写或 ASR 特征，在 SyncSpeech 基准上达 95.813% 准确率与 0.9943 AUC，但对未见 Video-Retalking 攻击准确率降至 82.775%。**</p>
