# 2026-11-02 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **MFlowAudio: Efficient Text-to-Audio Synthesis via Mamba-based Stateful Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41852)
![architecture](https://img.shields.io/badge/MFlowAudio_TCMamba_Stateful_Flow_Matching-red)
![task](https://img.shields.io/badge/Text_to_Audio-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MFlowAudio 把 Mamba 的线性复杂度骨干 TCMamba 塞进 flow matching，用 TimeMamba 与 ChannelMamba 双扫描同时建模时间因果与跨通道谐波结构，并以 Stateful Flow Matching 实现 O(1) 缓存的分块训练与流式生成。**</p>
+ **Scalable Audio-LLM System for Speech MOS Evaluation: A Diagnostic Case Study and Adaptation Roadmap**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41539)
![architecture](https://img.shields.io/badge/AudioLLM_MOS_Eval_LoRA_Cascade-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Samsung_Electronics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文以企业语音系统的批量质检为场景，先验证 Qwen2-Audio-7B-Instruct 零样本 MOS 打分与人类评分几乎无关，再经 LoRA 微调把与 MOS 的 Pearson 相关推到 0.65 并优于 UTMOSv2，给出可离线批量跑的语音质量评测蓝图。**</p>
+ **Nedimo: An Evidence-Grounded Multilingual Pipeline for AI-Generated Sleep Stories**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40970)
![architecture](https://img.shields.io/badge/Nedimo_Guardrail_TTS_Pipeline-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/University_of_Piraeus-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Nedimo 把证据不足的助眠音频诉求翻译成保守工程要求，用确定性规划加 LLM 生成、多阶段注意力衰减、约束校验与隔离机制产出低唤醒度多语种睡前故事，并在发布门前按响度、响度范围与真峰值限值复测文件。**</p>
+ **From prediction error to sparse events: Biologically inspired signed-dyadic coding for Mandarin keyword spotting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41381)
![architecture](https://img.shields.io/badge/Predictive_Signed_Dyadic_Coding-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把预测编码与感官适应机制搬到声学前端，提出 Predictive Signed-Dyadic Coding，只在残差超过可学习阈值时才发出带符号与二进制幂幅度的事件，在普通话关键词 spotting 上以 90% 准确率换来约三分之一的存储与推理开销下降。**</p>
+ **Self-Supervised Object-Centric Representation for Multi-Task Audio Analysis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41870)
![architecture](https://img.shields.io/badge/SlotAttention_Object_Centric_Audio-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Tampere_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用 slot attention 自监督地从合成混合音频的 AST patch embedding 重建对象中心槽位表示，一个共享表示同时支撑声音事件分类、检测与分离，检测宏 F1 达 0.7、分离 SI-SDRi 达 18.4 dB、zero-shot 分离仍有 14.5 dB。**</p>
+ **ARPEGE: Dataset and Methods to Estimate Acoustic and Geometric Parameters of Rooms from Sound**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41543)
![architecture](https://img.shields.io/badge/ARPEGE_Ambisonic_RIR_Dataset-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Univ._Gustave_Eiffel-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ARPEGE 发布 6 个空房间内用球形阵列采集的 248 条 ambisonic 房间脉冲响应，标注声源、麦克风与全部反射体的相对位置，并演示图像声源定位与盲房间参数估计两种方法，同时给出基于 Pyroomacoustics 的可复现仿真代码。**</p>
+ **Self-Localization of Distributed Microphone Arrays Using One Source and Acoustic Reflections**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41547)
![architecture](https://img.shields.io/badge/ARCTIC_ImageSource_PointCloud_Registration-red)
![task](https://img.shields.io/badge/Sound_Synthesis-magenta)
![organization](https://img.shields.io/badge/Univ._Strasbourg,_CNRS_UMR_7501-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ARCTIC 用单个声源的房间脉冲响应做分布式麦克风阵列自定位，把每个阵列的早期反射转成三维图像声源点云，再以锚定于真实声源的相似三角形排序搜索对齐，6 个房间 36 条实测脉冲响应上角度误差小于 5 度、径向误差小于 10 厘米。**</p>
+ **A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42042)
![architecture](https://img.shields.io/badge/ABI_E_Species_Level_Biodiversity_Index-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Abu_Dhabi_Maritime_Academy-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文改用物种级检出而非声能统计量构建声学生物多样性指数，先在带强标注数据上比较四个分类器并指出随机帧级切分会虚高，再用地点与季节过滤加事后过滤剔除 517 条误报，等努力量下与物种丰富度的 Spearman 相关达到 0.93。**</p>
+ **A General Theoretical Framework for Transformed Geometric Pattern Matching in Music**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42095)
![architecture](https://img.shields.io/badge/TransformationClass_GeometricPattern_Framework-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Aalborg_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇 61 页长文为音乐中的几何模式匹配建立统一的概念、术语与记号体系，以变换类为核心形式化定义匹配、出现、最大匹配与异质出现集，并讨论变换等价性与变换群，可作为音乐模式发现的理论基础。**</p>
+ **MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41127)
![architecture](https://img.shields.io/badge/MotorSense_Video_EMG_CrossModal_Pretraining-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland,_College_Park-green)
[![project](https://img.shields.io/badge/project-blue)](https://www.cs.umd.edu/~edessale/motorsense/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MotorSense 发布首个大规模配对的自我中心视频与表面肌电数据集，覆盖 100 小时无脚本操作并同步双侧 EMG、IMU 与音频，用视频—EMG 跨模态预训练学到的感知—运动对齐在四类动作理解任务上全面超过自监督视频基线。**</p>
