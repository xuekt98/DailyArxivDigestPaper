<!-- direction: llm_core -->

+ **ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14925)
![architecture](https://img.shields.io/badge/ToolTurns_Benchmark-red)
![task](https://img.shields.io/badge/Tool_Use-magenta)
![organization](https://img.shields.io/badge/University_of_California_Santa_Cruz-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ToolTurns 用 2620 个欠明确问题、1827 个工具和 11004 个 API 端点搭多轮工具对话基准，最好 agent 单轮解决率 69.6%，整段对话完成率却只有 39.8%。**</p>

+ **Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14965)
![architecture](https://img.shields.io/badge/Prefix_Guided_Sampling-red)
![task](https://img.shields.io/badge/Test_Time_Compute-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL_MIT_FutureTech-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/renjie3/PreG)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Prefix-Guided Sampling 先用短前缀的内部置信度给候选推理路径排序再展开，60 组配置中 54 组省 token，BRUMO 上最高省约 80%，前缀只用 22% token 就拿到全路径 53% 的增益。**</p>

+ **Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15029)
![architecture](https://img.shields.io/badge/Mask_Pattern_Position_Augmentation-red)
![task](https://img.shields.io/badge/Long_Context-magenta)
![organization](https://img.shields.io/badge/International_Institute_of_Information_Technology_Hyderabad-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MPPA 用每位置每步的累计 mask 密度偏移修正 RoPE 插值，在 LLaDA-8B-Instruct 的 8192 token 上把困惑度从 19.51 降到 3.12，passkey 检索保持 100%。**</p>

+ **Effective Teacher Support for Reasoning Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14850)
![architecture](https://img.shields.io/badge/Teacher_Support_Distillation-red)
![task](https://img.shields.io/badge/Reasoning_Distillation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文只蒸馏教师最高概率的词表片段，Qwen3 4B 到 1.7B 保留 0.01% 词表时 MMLU-Pro 无观测下降，训练步时降 38%、峰值显存降 24%。**</p>

+ **Probabilistic State Space Enumeration in Neural Network Computation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15062)
![architecture](https://img.shields.io/badge/Probabilistic_State_Space_MLP-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/ElohaX_Ltd.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 Transformer MLP 的稠密计算重写为可精确恢复的组合状态空间，NORDER-II 按联合概率排序枚举状态，在 2048 状态预算下把 MLP 输出逼近精度从 top-k 的 77% 提到 92% 以上，三层联合近似后困惑度几乎无损。**</p>

+ **Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15642)
![architecture](https://img.shields.io/badge/Differential_Backpack-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/University_of_Ioannina-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 Backpack 的义项权重从非负 softmax 改为两个 softmax 之差，使语境能主动抑制某个义项；70M 参数下困惑度从 24.60 降到 23.52，解释性税缩小 31%，线性读出与逐义项归因却完整保留。**</p>

+ **Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15842)
![architecture](https://img.shields.io/badge/Farthest_Future_Expert_Cache-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/CarbonForge-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/carbonforgeAI/moe-expert-eviction)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在真实 CPU→GPU 拷贝下实测 OLMoE-1B-7B 的六种专家缓存策略，发现固定专家集的加速都要付至少 0.067 nats 代价；改用「淘汰最久未来才用的专家」可零质量损失少拷 2.1 倍，吞吐反而从 38.3 升到 42.5 tok/s。**</p>

+ **Mach2: Scientific Discovery Platform with Deterministic Execution Constraints**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14777)
![architecture](https://img.shields.io/badge/Rule_Gated_Agent_Harness-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/Department_of_Aerospace_Engineering_University_of_Michigan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把自然语言操作规则翻译成 lint 式可执行谓词，用规则门控约束 agent 的工具调用、代码改动与产物验收，并在外部 agent 包返回时校验契约；全文无实验数字，贡献集中在治理规范与证据可追溯性。**</p>

+ **MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15315)
![architecture](https://img.shields.io/badge/MIGRO_Experience_State-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zOUMINGXI/MIGRO)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把长期记忆从模型内部状态改造成跨模型共享的持久经验状态：证据精确保留、地址近似组织、检索延迟到提问时才决定；LoCoMo 得分 54.13 领先 Mem0，私有内存少用 99.3%，BEAM 长历史上存储少 57.5%。**</p>

+ **SAME: Semantic Watermark Embedding for Open-Source Large Pretrained Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15771)
![architecture](https://img.shields.io/badge/Private_Vocabulary_Watermark-red)
![task](https://img.shields.io/badge/Watermarking-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出与原生词表逐 token 语义对齐的私有词表水印，只需在 Alpaca 上注入一次即可跨任务复用，九个下游集的固定触发检出率全为 100%，并额外提供语义级验证以适配不同任务格式。**</p>

<!-- direction: vlm_core -->

+ **Video-as-Experience: Learning Computer Use via Audio-Visual Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18747)
![architecture](https://img.shields.io/badge/Video_SALMONN_VEX-red)
![task](https://img.shields.io/badge/Computer_Use-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/TomZ1412/VideoCUA/tree/main)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用音视频理解统一「看教程学操作」与「回看自己的执行录像」两种经验来源；9B 的 video-SALMONN-VEX 在 OSWorld 成功率 49.99%、相对骨干提升 22%，CUA-Gym 上 26.26%，去掉音频会明显掉点。**</p>

+ **Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14942)
![architecture](https://img.shields.io/badge/Vision_Language_Axis_Ablation-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文用定向因果消融证明多模态训练会重塑纯文本推理：Chameleon-7B 砍掉视觉-语言轴后 BBH navigate 掉 27.6 点，布尔表达式反涨 5.6 点。**</p>

+ **AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15041)
![architecture](https://img.shields.io/badge/AROMA_Subspace_Actuation-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/University_of_Toronto-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AROMA 指出定位因果头不等于能控制：一个交叉注意力头的 4 维解释 89.82% 计数敏感性却只占 9.52% 激活能量，归一化驱动让精确计数准确率 +8.00 点。**</p>

+ **Recognizing Events Is Not Enough: Why Streaming VLMs Struggle in Compositional Instruction Triggering**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18743)
![architecture](https://img.shields.io/badge/TEMPI_Scenario_Memory-red)
![task](https://img.shields.io/badge/Temporal_Grounding-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出流式 VLM 能识别事件却常执行错组合指令，提出用原子事件查询加 Scenario Memory 持续记账的 TEMPI；CoTriggerBench 指令级成功率 44.4%，领先最强闭源基线 15.6 个百分点，检测器端侧还可加速 4.90 倍。**</p>

+ **DiFiT: Distribution-Fidelity-guided Visual Token Pruning for Multimodal Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15069)
![architecture](https://img.shields.io/badge/DiFiT_Visual_Token_Scorer-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/School_of_Artificial_Intelligence_Anhui_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出视觉 token 剪枝的代价不在贪心答案而在响应分布漂移，提出同时蒸馏参考答案与全 token 分布的 DiFiT；Qwen2.5-VL-7B 保留 10% token 时八项基准平均保留 89.36%，采样负向翻转比 FastV 少 30.3%。**</p>

<!-- direction: llm_vlm_rl -->

+ **Breaking Bad: "Going Badly" Activations Drive Reward Hacking**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14996)
![architecture](https://img.shields.io/badge/Task_Badness_Steering_Vector-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/ERACambridge_UK_AI_Safety_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文从 1,774 条不含 hack 样本的日常叙事中提取 task badness 激活方向，发现该状态在作弊发生前约 5 轮即升高，α=−0.25 的负向 steering 可把作弊率从 97% 降到 39%，但剂量过大会让模型把失败测试误判为通过。**</p>

+ **Rethinking "RL Generalizes, SFT Memorizes": The Role of SFT Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14912)
![architecture](https://img.shields.io/badge/SFT_Data_Source_And_Scale-red)
![task](https://img.shields.io/badge/RL_for_Reasoning-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该论文指出 RL 泛化、SFT 记忆的差距主要来自 SFT 数据而非算法：按 rollout 预算把 SFT 数据扩到约 138,000 条并混合 10% 强教师数据后，SFT 在通用推理任务上反超 GRPO 训练的 RL 模型，长尾解法覆盖正是关键机制。**</p>

+ **SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15426)
![architecture](https://img.shields.io/badge/SimRec_Task_Anchored_GRPO_Agent-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZJU-REAL/SimRec)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用任务锚定用户模拟器与轨迹级奖励，把推荐代理的搜索、追问、推荐整条交互策略用 GRPO 端到端训练，ESCI 上 NDCG@100 从 32.23% 提升到 35.42%。**</p>

+ **Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15346)
![architecture](https://img.shields.io/badge/JurisCoT_SFT_LABPO_Two_Stage-red)
![task](https://img.shields.io/badge/RL_for_Reasoning-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**法律推理两阶段训练：先用长度归一化双目标 SFT 平衡推理链与最终答案，再用 LABPO 自动激活与退役辅助奖励，Qwen3-8B 在 ChJGBench 上从 0.6406 提升到 0.7786。**</p>

+ **Is Jev a Good Multilingual Judge?**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14861)
![architecture](https://img.shields.io/badge/Multilingual_Judge_Evaluation-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Heidelberg_Institute_for_Theoretical_Studies-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文在 4 个多语基准、最多 47 个语言变体上评估 Jev 作为多语言裁判的能力：成本仅为 GPT-6.1 的 1/31–1/61，但知识密集答案核验准确率低 6.5 个百分点，且低资源语言更易误接受错误答案，建议英文指令加置信度筛选与路由。**</p>

