<!-- direction: llm_core -->

+ **Rethinking MoE Load Balancing as Feedback Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09252)
![architecture](https://img.shields.io/badge/PID_Balancer-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/Umea_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 MoE 负载均衡重述为 PID 反馈控制问题，证明只有积分项既消除持续不均衡又抑制逐步抖动，并在 OLMoE 16-64 专家的混合切换实验中以 0.30 的 postMV 优于辅助损失基线。**</p>

+ **Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09598)
![architecture](https://img.shields.io/badge/Transformer_FSQ-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/University_of_Edinburgh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用有限标量量化瓶颈替换常规 K/V 投影，实现每 token 只存打包整数码的极端 KV 压缩：在 0.6B-8B 模型上 RULER 从 12× 到 97.5× 压缩比均为最准，97.5× 时解码吞吐为原生 SDPA 的 1.54 倍。**</p>

+ **Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09700)
![architecture](https://img.shields.io/badge/HASA-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/University_of_Houston-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**头自适应稀疏注意力 HASA 不做训练，改用每个注意力头 query-key 算子的奇异谱决定特征维度有效秩、按响应方向一致性合并相邻序列区域，捕获 88.1% 稠密注意力质量并把长上下文速度提升最多 14.07 倍。**</p>

+ **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09722)
![architecture](https://img.shields.io/badge/FOSCAR-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Together_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/FutureMLS-Lab/FOSCAR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FOSCAR 用仿射折叠替代逐元素反量化，把 2/4 位 KV cache 解码的 scale/offset 操作减少最多两个数量级，H100 上 INT2 相对 FlashInfer BF16 加速 3.36 倍，接入 SGLang 后长上下文服务吞吐最高提升 170%。**</p>

+ **Intent-Aware Caching for Efficient LLM Serving**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09715)
![architecture](https://img.shields.io/badge/Intent_Aware_Caching-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/Virginia_Tech-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/hasanar1f/intent-aware-caching)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向多轮对话服务的意图感知缓存策略 IAC，用请求意图分类加在线复用统计指导前缀缓存驱逐，在 WildChat 与 ShareChat 真实负载上把命中率提到 34.6%，远高于学习类方法的 18.8% 与 LRU 的 12.2%。**</p>

+ **Test-Time Compute Scales Better with Parallel Agent Teams**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09798)
![architecture](https://img.shields.io/badge/Parallel_Agent_Teams-red)
![task](https://img.shields.io/badge/Test_Time_Compute-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/modal-projects/parallel-agent-teams-scaling)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**并行 agent 团队把测试时计算扩展到协作式采样：在 12 个长程任务上，十人小队在 100 agent 预算下有 10 个胜过并行单 agent、在 4 个任务上胜过单个百人团队，同等美元成本下半数任务超过前沿模型。**</p>

+ **RPEG: Training Reasoning Language Models Scalably and Cost-Effectively**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09207)
![architecture](https://img.shields.io/badge/RPEG-red)
![task](https://img.shields.io/badge/Training_Infrastructure-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/spcl/RPEG)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RPEG 用数据中心的图中间表示统一表达推理语言模型 RL 训练管线的结构选择与执行优化，在最多 256 张 GH200 上相对 ReaL 性能最高提升 2 倍、相对 verl 步延迟最多降低 2.48 倍，硬件利用率提升最高 30%。**</p>

+ **MINE: Entropy-coded Memory-efficient Inference for Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09424)
![architecture](https://img.shields.io/badge/MINE-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://doi.org/10.5281/zenodo.23885927)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MINE 用改造自 dtANS 的 GPU 熵编码方案 dtANS-LLM 做无损权重压缩，自动为每个张量与 GPU 调出码率-延迟 Pareto 前沿，在 Llama 3.1 8B 的 2.1 位检查点上比最快基线快 2.52 倍与 1.48 倍。**</p>

+ **Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09554)
![architecture](https://img.shields.io/badge/QGPM-red)
![task](https://img.shields.io/badge/Long_Context-magenta)
![organization](https://img.shields.io/badge/USC-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/iZHpy/QGPM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**QGPM 用模型自身注意力头的 query 相关度重塑 RoPE 位置，低相关 token 在快旋转平面上前进不足一个位置、慢旋转平面保持原布局，免训练即在 NoLiMa 与 RULER 上把五任务平均分提升 2.4 至 8.9 分。**</p>

<!-- direction: vlm_core -->

+ **AtariBench: Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08755)
![architecture](https://img.shields.io/badge/AtariBench-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/UC_San_Diego-green)
[![project](https://img.shields.io/badge/project-blue)](https://mignonjia.github.io/AtariBench/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AtariBench 在 20 个 Atari 2600 游戏上用高时间分辨率画面流考察 VLM 的时空推理，每种设置跑 10 次 30 秒闭环回合并解耦游戏内动态与推理速度，暴露出模型在运动方向判断与序贯决策上的持续短板。**</p>

+ **Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08998)
![architecture](https://img.shields.io/badge/Complexity_Twins-red)
![task](https://img.shields.io/badge/Chart_Understanding-magenta)
![organization](https://img.shields.io/badge/Google-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**复杂孪生问题把同一张图的计数题配成不同复杂度类，用转写探针与纯文本对照分离多模态 LLM 的看错与算错：答案每增一个数量级命中概率降 2.38 倍，而二次换视角读取能把大图读对率从 57/96 提到 86/96。**</p>

+ **Training-Free Active Test-Time Adaptation for Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09084)
![architecture](https://img.shields.io/badge/ACTOR-red)
![task](https://img.shields.io/badge/Test_Time_Adaptation-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/kaist-dmlab/ACTOR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**主动视觉语言测试时适配 ACTOR 是免训练插件，在当前样本必须先出预测、标签只能事后使用的约束下，用一致性与可靠性判据复用稀疏标注：跨域与 OOD 基准上一致提升 CLIP 与 TDA，开销不到 1 毫秒。**</p>

+ **AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09092)
![architecture](https://img.shields.io/badge/AdaAlloc-red)
![task](https://img.shields.io/badge/Video_QA-magenta)
![organization](https://img.shields.io/badge/UT_Austin-green)
[![project](https://img.shields.io/badge/project-blue)](https://vision.cs.utexas.edu/projects/adaalloc)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AdaAlloc 把长视频问答当作视觉 token 分配问题，先规划全局低分辨率与局部高分辨率的预算切分，再用时序定位挑出证据片段，在 LVBench、MLVU、VideoMME、LongVideoBench 上比均匀采样最多高 10.5 个百分点。**</p>

+ **Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09655)
![architecture](https://img.shields.io/badge/DMC-red)
![task](https://img.shields.io/badge/Vision_Language_Model-magenta)
![organization](https://img.shields.io/badge/Telecom_Paris-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/IemProg/DMC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**解耦模式连通 DMC 指出 CLIP 提示学习的基类特化与新类泛化梯度冲突，改为两个提示分别承载两个目标、在文本特征空间按固定系数插值，11 个数据集上把基类新类调和平均相对 MergeTune 提升 0.78 与 0.33。**</p>

<!-- direction: llm_vlm_rl -->

+ **RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09597)
![architecture](https://img.shields.io/badge/RuACT-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZJU-REAL/RuACT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 rubric-based GRPO 中 60.88% 的 query-rubric 观测失活（25.19% 不可达、35.69% 饱和），RuACT 让不可达 rubric 当特权教师做奖励门控自蒸馏，让饱和 rubric 拆出子 rubric 恢复组内对比度，在四个医学与科学基准上全面超过 GRPO 与重加权基线。**</p>

+ **Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09828)
![architecture](https://img.shields.io/badge/MonitorInterventionDesign-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Google_DeepMind-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ariahw/rl-rewardhacking-ext)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文开源三个自然出现奖励黑客的环境（代码改测试、医患谄媚、传记幻觉），用 GRPO 训练 Qwen3-4B 后发现模型先语义规避再表征规避，并量化了监控信号强度与规避风险的权衡，给出可迁移到新环境的监控器干预设计。**</p>

+ **Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09448)
![architecture](https://img.shields.io/badge/Reward_Conditioned_Entropy_Allocation-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_and_Information_Science_Southwest_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 RLVR 里常记的全局 token 熵拆成验证成功与失败的分层、再拆成语义解模式层：配对分析显示 12 个端点的失败轨迹熵一律更高，44 次相邻检查点转移中协方差近似 42 次正确预测熵变化方向，说明熵塌缩要按被移除的是哪种不确定性来诊断。**</p>

+ **Alignment by Confident Debate: Preference Learning from Multi-Agent Debate**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09568)
![architecture](https://img.shields.io/badge/Confidence_Weighted_Debate_Oracle-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Upwork_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把多智能体辩论转成无金标偏好数据：五个温度多样代理辩论后按答案等价聚类，用答案跨度置信度选出获胜簇来构造偏好对；跨 5 个模型族 4 个数据集，12 组里 9 组由 DPO 最优，最大提升 21.5 个百分点。**</p>

+ **Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09634)
![architecture](https://img.shields.io/badge/LambdaMix-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_University_of_Sheffield-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ckarouzos/lambdamix)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LambdaMix 为每个目标训练一个低秩适配器，用同一个偏好向量同时决定适配器混合与归一化后奖励的权重，单次训练即得到可在推理期调节的多目标策略族；四个基座上超体积优于全部条件化与策略合并基线，两个适配器即胜过十组 GRPO 专家。**</p>

+ **On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09872)
![architecture](https://img.shields.io/badge/Prompt_Conditional_Dr_DPO-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 TTRL 中多数投票伪标签的误差拆成总体多数偏置与有限 rollout 波动，前者不可辨识、后者随采样数指数衰减；PC-Dr.DPO 用 prompt 级众数占比条件化 Dr.DPO 温度并加缓存回放，在 6 个基准 5 个骨干的 30 组设置中 24 组持平或优于最强基线。**</p>

