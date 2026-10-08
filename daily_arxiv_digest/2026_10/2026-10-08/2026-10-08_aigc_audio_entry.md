+ **MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10355)
![architecture](https://img.shields.io/badge/Agentic_Intent_Refinement-red)
![task](https://img.shields.io/badge/Text_To_Music_Generation-magenta)
![organization](https://img.shields.io/badge/1Shandong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文生音乐系统产出的音频越来越可信，但评测几乎看不出结果是否匹配用户意图。单一的文本-音频全局相关性分数会忽略欠指定提示里的隐含意图，也会掩盖配器、结构、节奏或情绪走向等具体要求的失败。作者把意图对齐形式化为逐请求满足。**</p>

+ **Beyond Token Revision: Investigating Mask-and-Replace Diffusion for Zero-Shot Text-to-Speech**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09448)
![architecture](https://img.shields.io/badge/Mask_And_Replace_Diffusion-red)
![task](https://img.shields.io/badge/Zero_Shot_Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/1KAIST,_Republic_of_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**与自回归模型不同，离散扩散的零样本 TTS 并行生成语音 token 并可回看早先预测。mask-and-replace 训练在 mask-only 训练之上随机替换部分 token，其增益通常被归因于自我纠错（能修订已生成的 token）。本文指出，训练中暴露于随机扰动上下文可能才是真正原因。**</p>

+ **Tracing Inputs, Verifying Outputs: Validating Attribution in Music Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09637)
![architecture](https://img.shields.io/badge/Input_Attribution_Tracing-red)
![task](https://img.shields.io/badge/Music_Generation_Verification-magenta)
![organization](https://img.shields.io/badge/1Neutune,_Seoul,_South_Korea_2KAIST,_Daejeon,_South_Korea.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**如何验证谁的音乐贡献了一段 AI 生成输出？作者演示输入溯源如何提供可核验的证据，说明哪些音频源被用于生成以及它们是否塑造了输出。做法是仅以音频为条件生成（不给文本输入），再追溯每个输出背后的输入并确立其音乐效果。**</p>

+ **Steerspeech: Activation Steering For Emotion Control In Generated Speech**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10415)
![architecture](https://img.shields.io/badge/Activation_Steering-red)
![task](https://img.shields.io/badge/Emotional_Speech_Synthesis-magenta)
![organization](https://img.shields.io/badge/2Netflix,_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**预训练 TTS 能生成富有表现力的语音，但可靠的推理时情感控制仍困难：提示与参考音频提供的控制粗糙且不一致，而专门条件与模型适配又需要昂贵训练。SteerSpeech 是轻量的激活引导框架，通过向隐层激活注入引导向量控制情感。**</p>

+ **Training-Free Instruction TTS Gender Bias Calibration Using Model-Adaptive Steering**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09831)
![architecture](https://img.shields.io/badge/Model_Adaptive_Steering-red)
![task](https://img.shields.io/badge/Instruction_Text_To_Speech-magenta)
![organization](https://img.shields.io/badge/1AI_Research_Center,_Inventec_Corporation,_Taiwan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指令式 TTS 系统会从职业、人设等描述性风格提示中系统性地编码声学性别偏差，即便人口统计属性未被显式指定。作者提出免训练的指令 TTS 性别偏差校准，用模型自适应引导跨异构架构校准合成语音的隐式性别分布，且不覆盖显式指定。**</p>

+ **Toward Part-Aware Choral Transcription with singing voice assignment** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09861)
![architecture](https://img.shields.io/badge/Part_Aware_Choral_Transcription-red)
![task](https://img.shields.io/badge/Choral_Music_Transcription-magenta)
![organization](https://img.shields.io/badge/1_The_University_of_New_South_Wales,_Sydney,_Australia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**单乐器自动音乐转录进展显著，但合唱场景需要把女高音、女低音、男高音、男低音转录为独立声部。近期的音符级合唱转录反而产出单条合并的音符轨，限制了排练、教育与总谱重建。**</p>

+ **LIFT-SE: Linguistic Inference Followed by Flow Transformation for Generative Speech Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09963)
![architecture](https://img.shields.io/badge/Two_Stage_Generative_SE-red)
![task](https://img.shields.io/badge/Speech_Enhancement-magenta)
![organization](https://img.shields.io/badge/Qwen_Business_Unit_of_Alibaba-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**生成式语音增强在严重噪声与混响下语义约束不可靠时容易产生语言幻觉；而生成离散 codec token 的方法受限于 codec 解码器的量化误差，与 token 预测准确率无关。LIFT-SE 提出两阶段生成框架。**</p>

+ **CrossEdit: Cross-Modal Training Enables Rich Audio-Visual Editing** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10264)
![architecture](https://img.shields.io/badge/Cross_Modal_Training-red)
![task](https://img.shields.io/badge/Audio_Visual_Editing-magenta)
![organization](https://img.shields.io/badge/Adobe_Research1-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多模态编辑要求生成模型理解复杂组合指令并只修改目标元素，而现有系统大多局限于单一模态内的单属性编辑，因为高质量多模态编辑对难以获得。CrossEdit 用跨模态训练获得更丰富的音视频编辑能力。**</p>

+ **A Study on Improving Multi-class Audio Source Separation Via Decoupled CLAP Query Optimization and an Automated Data Engine** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10025)
![architecture](https://img.shields.io/badge/Decoupled_CLAP_Query_Optimization-red)
![task](https://img.shields.io/badge/Audio_Source_Separation-magenta)
![organization](https://img.shields.io/badge/Noah’s_Ark_Lab,_Huawei_Technologies_Canada_co.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**语言查询的音频源分离（LASS）可用自然语言抽取任意声源，但适配到应用特定声源类别很困难：训练数据噪声大，且基于 CLAP 的控制信号语义覆盖有限。作者提出解耦的 CLAP 查询优化加自动化数据引擎。**</p>

+ **VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterior Sampling for Unsupervised Blind Speech Separation** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09334)
![architecture](https://img.shields.io/badge/Virtual_Microphone_Diffusion-red)
![task](https://img.shields.io/badge/Blind_Speech_Separation-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology,_Shenzhen,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**盲源分离要在没有任何先验知识的情况下从混合中分离多个源。传统方法如独立矢量分析利用源的统计独立性，近期基于扩散的方法成为可能。VM-ARRAYDPS 用虚拟麦克风增广的扩散后验采样做无监督盲语音分离。**</p>

