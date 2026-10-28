# 2026-10-28 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Expressive Guitar Synthesis via Controllable Latent Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36786)
![architecture](https://img.shields.io/badge/Ctrl_LFM_Guitar_Two_Stage-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://weifu3024.github.io/ctrl-lfm-guitar-synth/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对吉他的「弹什么」与「怎么弹」分离：两阶段框架先由性能预测器从定时 MIDI 推断逐弦 f0 与幅度轨迹，再由潜空间流匹配合成器渲染为音频，并用伪速度预测器降低用户调节负担，在控制保真度与听感上优于单阶段对照与 DDSP-Guitar。**</p>
+ **StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37024)
![architecture](https://img.shields.io/badge/StreamSE_Codec_Latent_Regression-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Sungkyunkwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**2000 万参数的流式生成式语音增强：在冻结神经音频编解码器的连续潜空间里，每帧直接从带噪潜变量单次回归干净潜变量并条件于自身历史预测，无需迭代采样与前瞻；截断残差量化器到粗层级后每帧 token 减半，在单颗手机 CPU 核上实时运行且感知质量持平离线生成式基线。**</p>
+ **SMEBENCH: Benchmarking Neural Music Editing with Synthetized MIDI Edits**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36715)
![architecture](https://img.shields.io/badge/SMEBench_MIDI_Edit_Pairs-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Mila_-_Quebec_Artificial_Intelligence_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**通过改符号化 MIDI 演奏并渲染配对源/目标音频，构造 11,160 条配对样本的受控音乐编辑基准 SMEBench，覆盖十二类操作，配对目标让源保持、目标一致、文本兼容三维度可独立评测；用它诊断常见编辑指标并发现指标选择会实质改变六个系统的排名结论。**</p>
+ **Partially Edited Audio: Generation, Defense, and Open Problems**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37640)
![architecture](https://img.shields.io/badge/Partially_Edited_Audio_Taxonomy-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**综述「partially edited audio」范式：只有真实录音的部分被编辑而非整段重生成；论文主张「是否算伪造、有害与否取决于应用场景而非编辑的固定属性」，并分别从生成与防御视角给出分类、评测方法与基准工具包。**</p>
+ **TAC2: Timestamped Audio Captioning as composable functions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36568)
![architecture](https://img.shields.io/badge/TAC2_Composable_IIO_Functions-red)
![task](https://img.shields.io/badge/Text_to_Audio-magenta)
![organization](https://img.shields.io/badge/University_of_Surrey-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把带时间戳的音频描述重写为可组合函数的基础模型 TAC2：用时间对齐 IoU 融合事件检测、分离与字幕三个弱教师造结构化监督，以 IIO 格式一次调用解码完整声学时间线；作为成对监督用于文本到音频生成时，可对事件时序、说话人属性与词级重音做零样本控制。**</p>
+ **The Content Leash: Mitigating Degenerate Solutions in Invertible Speaker Anonymization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36768)
![architecture](https://img.shields.io/badge/Content_Leash_Constraint_Anonymization-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/Islamic_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对可逆语音匿名化的退化解——三元组损失可通过严重破坏频谱来满足，作者引入内容保持训练约束堵住该捷径，并用验证器泛化策略在训练中引入更强说话人验证表征；在 38 个未见说话人上把攻击者 EER 从 2.8% 抬到 26.3%，同时保持 11.8% 词错误率与 94.9% 说话人相似度。**</p>
+ **ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36126)
![architecture](https://img.shields.io/badge/ConformalMOS_Ordinal_Head-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Michigan_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把共形预测套到 MOS 预测上，在可交换性假设下给出有覆盖率保证的区间并保留点估计；训练时把 MOS 标签以序数感知方式建模为高斯平滑分布以保留分数次序，在 BVCC 上 MSE 0.08，且改善了分布外语音上 softmax 过度自信导致的不确定性校准。**</p>
+ **Physiology-Informed Audio Quality and Listening Effort Estimation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36865)
![architecture](https://img.shields.io/badge/Physiology_Informed_Quality_Effort-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Strathclyde-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 30 名听众上同时记录 32 通道实验室 EEG、可穿戴 EEG、fNIRS 与眼动，检验消费级设备能否解码音频质量并逐听众恢复听觉努力；结果显示商用可穿戴与光学传感可统计显著地解码质量并还原个体努力，把主观 MOS 从「慢且贵」推向实时、个体化的方向。**</p>
+ **Perceptual Differences and Preferences in Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36892)
![architecture](https://img.shields.io/badge/Discriminability_Preference_SE_Evaluation-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Aalborg_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「可辨别性」与「偏好」作为语音增强评价的两个互补维度：通过众包三角测试与成对偏好测试覆盖四个系统与干净参考，发现听众辨别能力与系统性偏好随系统及声学条件显著变化，且客观指标与两者的相关性并不稳定。**</p>
+ **EEG-Based Decoding of Musical Mode and Melodic Direction Using Empirical Mode Decomposition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37148)
![architecture](https://img.shields.io/badge/EMD_EEG_Musical_Mode_Decoding-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Universidad_de_Malaga-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以经验模态分解把主动钢琴演奏的 EEG 分解为四个固有模态函数，用能量描述子加宽网络判别音乐调式与旋律走向，被试内/跨被试平均准确率约 84%/81%、AUC-ROC 约 0.9；属音乐感知方向，非音乐生成。**</p>