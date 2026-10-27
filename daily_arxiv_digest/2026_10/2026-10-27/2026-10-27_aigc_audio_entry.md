# 2026-10-27 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ImageTTS: Repurposing Pretrained Image Diffusion Transformers for Speech Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34807)
![architecture](https://img.shields.io/badge/Image_DiT_Flow_Matching-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ImageTTS 把 FLUX.2 的图像 VAE 与 DiT 改造成语音合成器：用冻结图像 VAE 编码伪 RGB log-mel、只微调 DiT 做条件潜空间流匹配；10 万小时数据下 Seed-TTS test-en WER 1.12%，且图像预训练初始化把 WER 从 4.2% 降到 2.7%。**</p>
+ **When the Persona Contradicts the Line: Diagnosing Plan-to-Synthesis Failures in Chain-of-Thought TTS**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35008)
![architecture](https://img.shields.io/badge/CoT_TTS_Failure_Analysis-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Spellbrush-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出日英双语人格-台词冲突基准，沿规划器 delivery phrase、emotion 向量到渲染波形逐级探测，定位到 CoT-TTS 的意图流失发生在 plan-to-synthesis 接口而非规划器本身；学习式 text-to-latent 接口把英语方向正确率提到 89%。**</p>
+ **TIMUSE: Text-Initialized Masked Semantic Token Modeling for Universal Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34814)
![architecture](https://img.shields.io/badge/TIMUSE_Semantic_Restoration-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TIMUSE 用两阶段框架做通用语音增强：先以 LoRA 适配预训练扩散语言模型做掩码语义恢复，再用条件流匹配从恢复出的语义 token 重建 24 kHz 语音，在感知质量与语言/说话人保真之间取得比现有离散方法更好的平衡。**</p>
+ **From Speech Tokens to Stolen Voices: Attacker-Chosen-Text Speaker Impersonation via Representation Inversion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34688)
![architecture](https://img.shields.io/badge/STIA_Speech_Token_Inversion-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**STIA 揭示端到端语音 LM 的前端表示仍泄露说话人身份：用仅 3 秒的 Moshi 表示泄漏、结合公开语音数据训练条件流匹配模型，即可生成攻击者指定文本的受害者语音，CAM++ 说话人余弦相似度达 0.78、目标文本 WER 3.80%。**</p>
+ **Realizing Low-Precision Storage and Sparse Execution in a Folded FPGA Speech Enhancer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35144)
![architecture](https://img.shields.io/badge/Folded_FPGA_Speech_Enhancer-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/GN-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在折叠式 FPGA 语音增强加速器上，混合精度权重降片上存储、结构化通道稀疏直接从调度中移除整块运算：最佳稀疏模型消除 47.3% 卷积 MAC、帧时间 1.86→1.03 ms、动态能耗 83→33 μJ/帧，且语音质量更高。**</p>
+ **The Voice on the Line**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35272)
![architecture](https://img.shields.io/badge/Causal_Voice_Isolator-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Scicom-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/collections/Scicom-intl/voice-isolator)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**训练 20 ms 延迟的因果语音隔离器并从通话本身登记说话人，暴露「久别忘人」与「独处反被伤」两类被短窗口掩盖的失败；用长通话切窗训练把干净通话错误率降到 2.96%，蒸馏后 22.1M 参数可在单 CPU 线程实时运行。**</p>
+ **Graph Neural Network for Wide-Area 6DoF Ambisonic Rendering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35741)
![architecture](https://img.shields.io/badge/GNN_Ambisonic_Rendering-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Politecnico_di_Milano-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对广域 6DoF Ambisonic 渲染，作者只在插值环节加一个轻量 GNN：以已知阵列与查询位置建图、节点携带局部 DirAC 特征，让网络预测查询条件的阵元权重，再交由解析 DirAC 层重建能量、扩散度与到达方向。**</p>
+ **Gangqinpu: A Multi-Genre, Multi-Task Piano Dataset with Aligned Audio, MIDI, and Musical Scores**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34694)
![architecture](https://img.shields.io/badge/Gangqinpu_Piano_Dataset-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/wei-zeng98/gangqinpu)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Gangqinpu 提供 18,786 条乐谱-演奏配对与 1,007 小时钢琴音频，含音符级对齐与节拍标注，并用基于乐谱的分类器滤掉无表现力的演奏；其在节拍跟踪上取得跨数据集增益，数据与代码已公开。**</p>
+ **A Robust, Explainable, and Efficient Deep Metric for Speech and General Audio Quality**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35810)
![architecture](https://img.shields.io/badge/SAQM_Audio_Quality_Metric-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Fraunhofer_Institute_for_Integrated_Circuits_(IIS)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SAQM 用传统质量度量特征加对比学习训练的 CNN 构成无参考语音/音频质量度量，以 PEAQ-2f 或编码模式排序作伪标签预训练，并可通过梯度回传给出显著性归因，在语音上比肩 SOTA 且算力开销低。**</p>
+ **Multimodal Concert Video Editing: System Design and Exploratory Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35816)
![architecture](https://img.shields.io/badge/Concert_Video_Editing-red)
![task](https://img.shields.io/badge/Audio_Editing-magenta)
![organization](https://img.shields.io/badge/Reutlingen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多机位演唱会剪辑框架把多轨音频的乐器活动、可见乐器与画面清晰度配以节拍时间轴，用可解释打分模型在整段镜头区间上做概率化机位选择；一场四机位专家研究给出混合评价，并据此提出扩展到上下文与序列级准则。**</p>