# 2026-10-26 - AIGC 音频生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Melody Guidance for Audio Diffusion Models Without Retraining**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32211)
![architecture](https://img.shields.io/badge/Inference_Time_Melody_Guidance-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Friedrich-Alexander-Universitaet_Erlangen-Nuernberg-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用可微音高检测器在推理期引导一个完全无旋律条件的音频扩散模型，并从合成旋律起步以稳定采样；钢琴、吉他、人声上的旋律准确率与专用条件模型相当，且无需配对数据或重训。**</p>
+ **X-Dubbing: Speech-to-Speech Translation under Temporal and Visual Constraints**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32042)
![architecture](https://img.shields.io/badge/Translator_Plus_Voice_Actor-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把跨语种配音拆成时间感知的语音到文本翻译与视频感知的 TTS，两者共用语言无关的时间预算；再用合成语音反馈反哺翻译器，无需成对配音数据即可在等时性与音视频对应上超过基线。**</p>
+ **MI-MIDI 2: From Observation to Control with Sparse Autoencoders in Text-to-MIDI Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32007)
![architecture](https://img.shields.io/badge/SAE_Feature_Atlas-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Institute_of_Computer_Science_Warsaw_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首次在文生 MIDI 上系统检验 SAE 特征的「可解释性是否等于可控性」：密度校正相关性选出的特征能小幅推动目标指标，原始相关性选出的则完全无效；并附完整特征图谱。**</p>
+ **DRAMA-Eval: A Benchmark for Context-Aware, Multi-Turn, Multi-Speaker Speech Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31796)
![architecture](https://img.shields.io/badge/LLM_As_Judge_Benchmark-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Northwestern_Polytechnical_University_ASLP-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向上下文感知、多轮、多说话人的语音生成统一基准，用 LLM-as-a-Judge 从客观/局部/全局三层评估；结果显示长程说话人一致性与隐式指令遵循是当前两大短板。**</p>
+ **MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32161)
![architecture](https://img.shields.io/badge/Multi_Granularity_REPA-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 REPA 的对齐拆成帧级 SSL 与句级说话人验证两支，并对帧级目标做时间归一化以剥离句级统计；在 Libri2Mix 上以 1/3 与 1/2 的轮数达到 MeanFlow-TSE 基线的 OVRL 与 PESQ。**</p>
+ **Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32749)
![architecture](https://img.shields.io/badge/Causal_Multi_Scale_TF_Separator-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发布真实场景视听目标说话人提取基准 RealSSA，并提出单次编解码前向完成多尺度时频分离的因果方法 Falcon：参数减 91.9%、计算减 20.2 倍、延迟降 11.1 倍，同时提取质量 SOTA。**</p>
+ **NECTAR: Automatic Negative Clue Estimation via Centroid-Space Mapping for Target Speaker Extraction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32133)
![architecture](https://img.shields.io/badge/Centroid_Space_Mapper-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现混合语音的说话人质心接近其成分说话人质心的中点，据此自动反推干扰者的负线索并估计所需质心；Libri2Mix 上取得 16.18 dB SI-SDRi。**</p>
+ **SEMAC: Spherical Energy Matching Ambisonics Codec for Efficient Higher-Order Ambisonics Compression**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32981)
![architecture](https://img.shields.io/badge/Directional_Energy_Envelope_Codec-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Google-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**高阶 Ambisonics 不再逐通道编码：只传全阶方向性能量包络加少数 CELT 传输通道，码率不再随阶数平方增长；MUSHRA 显示 36 个通道中的 16 个在两个码率下都优于全阶 CMF 3。**</p>
+ **Noisy Target Training Meets Drifting for Weakly-Supervised Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32870)
![architecture](https://img.shields.io/badge/Sinkhorn_Drifting_Loss-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Mitsubishi_Electric_Research_Laboratories-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对弱监督语音增强中「训练目标本身带噪」会留下残余噪声的问题，引入 Sinkhorn 漂移损失，把增强语音分布匹配到非配对干净语音的高密度区域，同时保持弱监督性质。**</p>
+ **ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32202)
![architecture](https://img.shields.io/badge/Radar_Vibrometry_Benchmark-red)
![task](https://img.shields.io/badge/Audio_Super_Resolution-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个毫米波雷达语音增强社区挑战赛：面向麦克风失效的透玻璃场景，提供成对雷达/干净语音数据、标准化预处理、基线系统与基于 Codabench 的统一客观评测。**</p>
