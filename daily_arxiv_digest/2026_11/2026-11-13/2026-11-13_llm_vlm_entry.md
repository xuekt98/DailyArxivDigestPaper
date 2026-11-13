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

+ **Edge-Native Multimodal RAG: Hardware-Aware Quantization and Architectural Optimization for Consumer GPUs**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14924)
![architecture](https://img.shields.io/badge/Edge_Native_Multimodal_RAG-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Egypt-Japan_University_of_Science_and_Technology_E-JUST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向消费级 Turing GPU 的多模态 RAG：NF4 长上下文稳定、延迟 81 ms/tok，整套占 8.37 GB，结构化提示再降 47% 延迟，200 次试验里数学准确率从 35.0% 修回 92.0%。**</p>

+ **MuEdit: An efficient multi-task editing method towards inter-domain knowledge conflicts**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14910)
![architecture](https://img.shields.io/badge/Mu_Edit_Framework-red)
![task](https://img.shields.io/badge/Model_Editing-magenta)
![organization](https://img.shields.io/badge/Gaoling_School_of_Artificial_Intelligence_Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MuEdit 把多任务模型编辑崩溃归因于跨域零空间错位，用 0 到 1 的 Conflict Index 排序任务并动态降秩扩空间，ZsRE 特异性从 0.7098 提到 0.8845。**</p>

+ **Termination Lag: Coding Agents Solve Early but Stop Late**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14960)
![architecture](https://img.shields.io/badge/Termination_Lag_Analysis-red)
![task](https://img.shields.io/badge/Code_Agent-magenta)
![organization](https://img.shields.io/badge/The_Pennsylvania_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文发现代码 agent 普遍解得早停得晚：38%–82% 的成功运行首次改码即正确，后续步骤仍占成功运行的 35%–60%，还有 1%–8% 最终把正确补丁改坏。**</p>

+ **CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14980)
![architecture](https://img.shields.io/badge/CoLFA_Attribution-red)
![task](https://img.shields.io/badge/Multi_Agent-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/luoyufeihaha/CoLFA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoLFA 借多智能体的交接痕迹重排失败归因输入，五个设置三个骨干上精确步骤定位准确率最多提升 37.50%，token 消耗最多减少 97.6%，小模型也能替代全量轨迹审查。**</p>

+ **Same Task, Different Statement: When and How Reformulation Helps LLM Problem Solving**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14997)
![architecture](https://img.shields.io/badge/Problem_Reformulation-red)
![task](https://img.shields.io/badge/Reasoning-magenta)
![organization](https://img.shields.io/badge/Northwestern_Polytechnical_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文检验 LLM 的先改写再求解习惯：oracle 改写平均提分 27.6%，固定规则只赚 11.0% 而盲改亏 5.6%，收益取决于问题类型而非改写本身。**</p>

+ **EvoX: Rethinking the Agent Harness as a Runtime Policy**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15006)
![architecture](https://img.shields.io/badge/EvoX_Agent_Runtime-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/Infinite_Evolution_Lab_EvoMap-green)
[![project](https://img.shields.io/badge/project-blue)](https://evomap.ai/evox)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EvoX 用 Rust 写的多模型 agent runtime 把外壳当作操作策略层，在 691 个任务-模型对上取得最高 56.2% 成功率，比其余五个外壳均值高约 3.0 个点。**</p>

+ **AutoAssumption: Searching over Assumptions Discovers ML-Systems Algorithms**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14844)
![architecture](https://img.shields.io/badge/AutoAssumption_Search-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AutoAssumption 把 89 个 ML 系统算法改写成 Lean 证明图并搜索其假设，搜出的 KV 缓存驱逐算法 RULER-4K 得 75.7 分，高于最好已发表方法的 74.1。**</p>

<!-- direction: vlm_core -->

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

+ **Hint-Informed Self-Distillation for Reasoning Segmentation**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14931)
![architecture](https://img.shields.io/badge/Hint_Informed_Self_Distillation-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HISD 用离线目标消歧提示驱动 EMA 教师给学生轨迹做 token 级信用分配，ReasonSeg 的 gIoU/cIoU 比 DPAD 高 3.00/3.55 点，有效推理 token 少 80% 以上。**</p>

+ **Poison-then-Hide: Finetuning-Activated Backdoor Attack on Pretrained Vision Encoders**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14970)
![architecture](https://img.shields.io/badge/Poison_Then_Hide-red)
![task](https://img.shields.io/badge/Vision_Language_Model-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/QixuanJin99/poison-then-hide)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Poison-then-Hide 把休眠后门植入预训练视觉编码器、等干净下游微调才激活，6 个数据集上攻击成功率最高 97%，且 Neural Cleanse 等七种防御都无法彻底清除它。**</p>

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

+ **Is Jev a Good Multilingual Judge?**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14861)
![architecture](https://img.shields.io/badge/Multilingual_Judge_Evaluation-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Heidelberg_Institute_for_Theoretical_Studies-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文在 4 个多语基准、最多 47 个语言变体上评估 Jev 作为多语言裁判的能力：成本仅为 GPT-6.1 的 1/31–1/61，但知识密集答案核验准确率低 6.5 个百分点，且低资源语言更易误接受错误答案，建议英文指令加置信度筛选与路由。**</p>

