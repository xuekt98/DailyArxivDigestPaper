+ **Full-duplex Spoken Language Modeling with Discrete Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17780)
![architecture](https://img.shields.io/badge/Discrete_Diffusion_Full_Duplex-red)
![task](https://img.shields.io/badge/Full_Duplex_Spoken_Language_Model-magenta)
![organization](https://img.shields.io/badge/NVIDIA_GB300_GPU._More_decoding_speed_results_on_different_GPUs_are_provided_at_Appendix_A.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Diffuplex 是基于离散扩散的全双工口语语言模型，在语言智能与响应效率之间取得了前所未有的平衡。开启思考模式时每次前向产出 13.0 个 token，平均 1872 token/秒，解码速度显著超过前沿自回归模型。**</p>

+ **DuplexAct: How Interactive Are Frontier Full-Duplex Spoken Language Models?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17738)
![architecture](https://img.shields.io/badge/Action_Level_Duplex_Evaluation-red)
![task](https://img.shields.io/badge/Full_Duplex_Evaluation-magenta)
![organization](https://img.shields.io/badge/1The_University_of_Melbourne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**端到端全双工口语模型支持持续听说，需要随对话展开采取恰当的交互动作。但现有基准缺少结构化的动作级形式化，往往只评估动作是否发生而非是否成功，且对多样真实对话的覆盖有限。**</p>

+ **D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17124)
![architecture](https://img.shields.io/badge/Half_To_Full_Duplex_Conversion-red)
![task](https://img.shields.io/badge/Full_Duplex_Spoken_Language_Model-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**全双工口语模型支持同时听说，但在通用能力上常落后于半双工模型。D2（Dialogue-to-Duplex）提出一个框架，在细时间粒度上把预训练的半双工模型转换为高能力全双工模型。**</p>

+ **Distilling Text LMs into Speech-to-Speech LMs by Matching Internal Text Predictions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17461)
![architecture](https://img.shields.io/badge/Internal_Text_Prediction_Matching-red)
![task](https://img.shields.io/badge/Speech_To_Speech_Language_Model-magenta)
![organization](https://img.shields.io/badge/2_Stony_Brook_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文本语言模型通过大规模预训练获得广泛的语言与事实能力，而从语音单独学习这些能力仍很困难。近期工作显示从预训练文本 LM 蒸馏是转移其语言与事实能力到语音模型的有前景路径，但既有蒸馏方法存在局限。**</p>

+ **PhonoVoxtLM: Exploring Single-Codebook Phonological Tokens for Speech Understanding and Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.18469)
![architecture](https://img.shields.io/badge/Single_Codebook_Phonological_Tokens-red)
![task](https://img.shields.io/badge/Speech_Understanding_and_Generation-magenta)
![organization](https://img.shields.io/badge/Johns_Hopkins_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文研究语音 token 表示如何在一个统一的语音语言模型内同时支撑理解与生成。PhonoVoxtLM 基于 VoxtLM 框架，使用旨在保留语言内容与韵律信息的音系 token。现有 tokenizer 为语音识别与重合成联合训练。**</p>

+ **What Matters in Preference Post-Training of Continuous Autoregressive Speech Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.16276)
![architecture](https://img.shields.io/badge/Controlled_Intervention_Preference_Tuning-red)
![task](https://img.shields.io/badge/Speech_Language_Model_Preference_Tuning-magenta)
![organization](https://img.shields.io/badge/†_The_Chinese_University_of_Hong_Kong,_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**连续自回归语音语言模型把自回归骨干与扩散或流匹配头结合。偏好后训练需要选择如何构造偏好对以及更新哪些模块。受控干预显示：扰动一段声学 patch 会改变后续骨干状态，但更大的表示变化并不必然降低语音质量。**</p>

+ **Collapse, Repair, and Drift: Dissecting Fine Tuning Dynamics in Speech Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.18192)
![architecture](https://img.shields.io/badge/Lossless_Dynamics_Dissection-red)
![task](https://img.shields.io/badge/Speech_Language_Model_Fine_Tuning-magenta)
![organization](https://img.shields.io/badge/1Department_of_Intelligence_Science_and_Technology,_Kyoto_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**监督微调通常通过训练与评估损失来监控，但损失并不能完整刻画模型功能如何沿同一轨迹演化。作者研究这一落差：对 Qwen3-ASR、MiMo-Audio、FireRed-LLM 做方言适配，在 1e-5 到 1e-3 的学习率范围内观察。**</p>

+ **What Do Deepfake Audio Detectors Hear? From Self-Supervised Models to Audio LLMs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17617)
![architecture](https://img.shields.io/badge/Attention_Attribution_Audit-red)
![task](https://img.shields.io/badge/Deepfake_Audio_Detection-magenta)
![organization](https://img.shields.io/badge/National_Institute_of_Informatics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真实世界的深伪检测录音很少只有语音，它们常是语音与背景事件的混合，而背景事件本身也可能是合成的。处理这些混合时，检测器究竟关注语音还是背景事件、其频谱证据在哪里，并不清楚。**</p>

+ **When Does an ASR Error Matter? Task-Role Diagnostics for Tool-Using Voice Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.17619)
![architecture](https://img.shields.io/badge/Task_Role_ASR_Error_Diagnostic-red)
![task](https://img.shields.io/badge/Tool_Using_Voice_Agent-magenta)
![organization](https://img.shields.io/badge/Leibniz_University_Hannover,_Hannover,_Germany-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在级联语音智能体中，ASR 错误的下游后果差异极大：一个小转写错误可能让工具调用保持不变，也可能改变其意图或参数。而常规的词错误率捕捉不到这些差异。**</p>

+ **RefTAG: Reflection-aware Temporal Audio Grounding in Large Audio Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.16217)
![architecture](https://img.shields.io/badge/Reflection_Chain_Of_Thought_Grounding-red)
![task](https://img.shields.io/badge/Temporal_Audio_Grounding-magenta)
![organization](https://img.shields.io/badge/Northwestern_Polytechnical_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**时序音频定位需要找出被查询目标的**每一次**出现，因此出现次数与区间边界都至关重要。RefTAG 是一个面向可验证时序自我纠正的后训练框架。**</p>

