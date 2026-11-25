<!-- direction: duplex_speech_core -->

+ **LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30714)
![architecture](https://img.shields.io/badge/Block_Causal_Streaming_DiT-red)
![task](https://img.shields.io/badge/Real_Time_Speech-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://streamaudio.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把双向视频转音频扩散模型改造成实时流式生成器：分块因果 DiT 加同步对齐视频条件，经 ODE 蒸馏与非对称 DMD 四阶段训练后四步免 CFG 出声，单卡 A100 上 RTF 0.79、TTFF 143 毫秒，同步误差 0.395 反超教师模型。**</p>

+ **BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30723)
![architecture](https://img.shields.io/badge/BiSAT_Shared_Index_SVQ-red)
![task](https://img.shields.io/badge/Speech_Tokenization-magenta)
![organization](https://img.shields.io/badge/Japan_Advanced_Institute_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://seekmind-lab.github.io/bisat-demo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**声学与语义双分支各自独立编码、只靠共享索引向量量化器耦合的语音分词器，25 Hz 单码流 375 bps 下重建 WER 2.15、冻结码英文 ASR WER 37.71，优于 CosyVoice 3，且仅用 12.2 万小时数据就能训出零样本 TTS。**</p>

+ **Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30106)
![architecture](https://img.shields.io/badge/Ultrasound_Guided_FiLM_Watermark-red)
![task](https://img.shields.io/badge/Real_Time_Speech-magenta)
![organization](https://img.shields.io/badge/Bloomberg_L.P.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用手机自带扬声器与麦克风捕捉的超声反射，把说话人口部运动与语音实时绑定成动态水印，iOS 与 Android 端侧运行、延迟开销小于 200 毫秒；六类攻击平均 AUC 0.95，对同步伪造成攻击最弱时降至 0.84。**</p>

