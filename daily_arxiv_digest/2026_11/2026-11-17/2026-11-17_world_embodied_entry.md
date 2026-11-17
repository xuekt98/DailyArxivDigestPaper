<!-- direction: world_model -->

+ **Rethinking Actions: Continuity-Aware Priors for World-Model Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16645)
![architecture](https://img.shields.io/badge/LG_DKGP_Action_Prior-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/oliverstack-byte/LG-DKGP)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把专家动作的时序连续性做成 LG-DKGP 先验：局部门控深核 GP 预测动作续接，配合冻结的世界模型在五个任务上取得 87.07% 宏平均成功率，优于 INTACT 的 71.03%。**</p>

+ **Frame First, Decode Once: Object-Centric Coordinates and Single-Pass Decoding for System-1 World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18761)
![architecture](https://img.shields.io/badge/Procrustes_FPD_Decoder-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/Sigmind.ai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**单次前向解码的动作条件预测器：用物体初始位姿的 SE(2) 坐标系把决策后悔降低 1.9–2.2 倍，单次解码每次决策仅 1.6–1.8 ms，比 10 步 DDIM 快 6–8 倍。**</p>

+ **Latent Imagination for Parameterized Action Spaces**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15744)
![architecture](https://img.shields.io/badge/HyLI_Hybrid_Latent_Imagination-red)
![task](https://img.shields.io/badge/Dreamer-magenta)
![organization](https://img.shields.io/badge/Turkish_Aerospace-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HyLI 把混合动作策略完全放进 DreamerV3 世界模型的潜空间想象里训练，靠反事实模式评估与成功窗口回放解决模式稀疏问题，7 个基准上环境步数少 2.4 倍、决策比 DLPA 快 67 倍。**</p>

+ **Bind-WAM: Binding-Uncertainty-Guided Selective Future Imagination in World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15368)
![architecture](https://img.shields.io/badge/Bind_WAM_Selective_Imagination-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Bind-WAM 用语言-对象绑定不确定性决定何时启动未来想象：6.65M 参数的路由器在 LIBERO 上只用 40.58% 的联合去噪就拿到 98.60% 成功率，完成时间比始终想象降低 25.6%。**</p>

+ **Probing Where Surprise Happens: Localized Violation-of-Expectation Evaluation of Video World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18979)
![architecture](https://img.shields.io/badge/Localized_VOE_Evaluation-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/University_of_Miami-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给 VOE 基准补上时空违规证据标注后，作者发现全局与局部惊讶分数在 28.7% 的样本上给出互相矛盾的判定，说明聚合预测误差并不代表模型真的在违规处感到惊讶。**</p>

+ **WeatherDreamer: Learning a World Model from Multimodal Earth Observations**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18393)
![architecture](https://img.shields.io/badge/WeatherDreamer_State_Space-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Zeus_AI_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WeatherDreamer 从 18 个全球观测系统端到端学出观测-校正-再预报循环，一小时全球分析单卡约 1.5 分钟，留出站点集合预报 12 小时内优于 NOAA GEFS，但没有动作条件。**</p>

+ **Marginal-Preserving Coupled Diffusion Composition for Long-Horizon Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15585)
![architecture](https://img.shields.io/badge/MCDC_Coupled_Noise_Init-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/China_University_of_Mining_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MCDC 不重训模型，只把相邻轨迹 chunk 的初始高斯噪声耦合成正相关，同时严格保持每个 chunk 的标准高斯边缘分布，在 OGBench 长程任务上把 AntMaze-Large 成功率从 83.6% 提到 96.0%。**</p>

<!-- direction: embodied_ai -->

+ **Training Reasoning Models in Simulation to Natively Use Real Robots**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18562)
![architecture](https://img.shields.io/badge/RURL_Robot_Use_RL-red)
![task](https://img.shields.io/badge/Computer_Use_Embodied-magenta)
![organization](https://img.shields.io/badge/MIT-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mit-han-lab/pear)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MIT 等团队用 robot-use 强化学习在纯仿真中、无示教无 harness 地把 27B 开源推理模型训成原生机器人使用者，LIBERO 成功率 1.6% 升到 74.4%，并在未训练过的双臂真机上完成 60% 的试验。**</p>

+ **TMA: Sim-to-Real Forceful Humanoid Manipulation via Tactile-Driven Motor Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18976)
![architecture](https://img.shields.io/badge/TMA_Tactile_Motor_Adaptation-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![project](https://img.shields.io/badge/project-blue)](https://humanoid-tma.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TMA 用锥坐标触觉信号与约 2 秒交互历史在线修正电机行为，在四种商用圆门把手上零样本实机开门成功与抓取成功为 8/9、6/8、6/7、7/8，而 RMA 全部失败。**</p>

+ **ActionCodec2: A Streaming Action Tokenizer**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15490)
![architecture](https://img.shields.io/badge/ActionCodec2_Streaming_Tokenizer-red)
![task](https://img.shields.io/badge/Action_Chunking-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://zibindong.github.io/actioncodec2-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ActionCodec2 把动作分词改成流式释放：相对解码器重建状态做量化以抑制误差累积，LIBERO 回放漂移压到 5 mm 内、成功率 97%，通用版 15 Hz 末端控制仅需 8.8 token/s。**</p>

+ **STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16589)
![architecture](https://img.shields.io/badge/STVLA_Spatial_Temporal_Memory-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/AgiBot-green)
[![project](https://img.shields.io/badge/project-blue)](https://stvla.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**STVLA 把冻结几何基础模型的空间 token 与视觉 token 一起写入有界记忆库并用相关性-非冗余打分检索，LIBERO 五套件均值 97.8%，真机叠块 60 次全部成功。**</p>

+ **EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16728)
![architecture](https://img.shields.io/badge/MXT_Plus_Embodiment_Dreaming-red)
![task](https://img.shields.io/badge/Robot_Foundation_Pretraining-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://egox-dream.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EgoX 的 MXT+ 按模态而非按本体划分 tokenizer 与动作专家、共享 Transformer 骨干跨本体预训练，13 个任务-本体对上平均任务进度从 0.63 升到 0.80，OOD 条件从 0.53 升到 0.77。**</p>

+ **ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16872)
![architecture](https://img.shields.io/badge/ACE_CaP0_Agentic_Recipe-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/ACE_Robotics-green)
[![project](https://img.shields.io/badge/project-blue)](https://acerobotics2025.github.io/ACE-CaP/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ACE-CaP-0 把代码即策略做成按需索要机器人示教加按需用仿真验证的配方，八个真实操作任务的冻结程序在 240 次试验中成功 221 次（92.1%），平均执行 0.97 到 2.27 分钟。**</p>

+ **UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17163)
![architecture](https://img.shields.io/badge/FlowVLA_Tail_Aware_GRPO-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://prince687028.github.io/UAV-Flow)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UAV-Flow++ 提出 Flying-on-a-Word 任务并给出 30,692 条真机专家轨迹与 10,109 条仿真轨迹的数据集，FlowVLA 预训练成功率 75.58%，经尾部感知 GRPO 后训练提升到 93.16%。**</p>

+ **Certify, Then Select: Viability-Aware Runtime Steering of Frozen Diffusion Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19047)
![architecture](https://img.shields.io/badge/CAST_Certified_Action_Selection-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/SUPSI-IDSIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://clmoro.github.io/cast)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CAST 对冻结扩散策略的动作块先做屏障认证、再用价值集成排序执行，robomimic Can 五类请求上联合成功率 0.70–0.89，最大违规率降到 0.5%，并用可行动性估计避开死路。**</p>

