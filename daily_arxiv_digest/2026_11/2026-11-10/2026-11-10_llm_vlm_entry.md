<!-- direction: llm_core -->

+ **Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10405)
![architecture](https://img.shields.io/badge/Yuanbao_Reranker-red)
![task](https://img.shields.io/badge/Retrieval-magenta)
![organization](https://img.shields.io/badge/Yuanbao_Search_Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Yuanbao-Search/Yuanbao-Reranker)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以 Qwen3 为底座的 0.6B/4B/8B 三档稠密重排器，用文档接地合成加偏好蒸馏构造 2.75M 组排序数据，4B 版即以 73.63 Avg. 反超 8B 教师，8B 版达 74.21 Avg.。**</p>

+ **D-REAL: Acceptance-Length Optimization with Unbiased Gradients for Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10432)
![architecture](https://img.shields.io/badge/D_REAL_Acceptance_Length-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把投机解码的期望接受长度直接变成可优化的后训练目标，用无偏梯度估计处理随机验证下的参数依赖，一轮训练即让平均接受长度提升 0.23 token、端到端吞吐最高提升 9.4%。**</p>

+ **Two-Sided Conformal Evidence Sets for Retrieval-Augmented Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10335)
![architecture](https://img.shields.io/badge/Conformal_Evidence_Sets-red)
![task](https://img.shields.io/badge/RAG-magenta)
![organization](https://img.shields.io/badge/Florida_Atlantic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 RAG 的双侧保形证据集框架，分别给出支持集与反驳集，在可交换性下每侧保证至少 1−α 覆盖率，维生素C基准上最大偏差仅 3.0 与 5.4 个百分点，并指出跨分布时保证会失效。**</p>

+ **Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10439)
![architecture](https://img.shields.io/badge/MixUA_Scoped_Memory-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/AWS_Agentic_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向多用户多智能体的记忆系统，把每条经验按受益方与可披露范围分配到 pair、user、agent、global 四种作用域，相比无记忆最高提升 16 分，同时把私密事实的越域泄漏率压到 0.02% 以内。**</p>

+ **The Truth Beneath the Tokens: Prompt-Space Recovery of Knowledge Edits in Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10450)
![architecture](https://img.shields.io/badge/Memento_Prompt_Space_Recovery-red)
![task](https://img.shields.io/badge/Model_Editing-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出只在提示空间操作、完全不改动被编辑模型权重的 Memento，用可学习前缀把编辑前的事实重新诱导出来，在 3 个 LLM 与 5 种编辑方法上恢复了 80.07% 的留出事实。**</p>

+ **LongCapHarness: Capability-Guided Auto-Harnessing for Long-Context Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10463)
![architecture](https://img.shields.io/badge/LongCapHarness_Capability_Harness-red)
![task](https://img.shields.io/badge/Long_Context-magenta)
![organization](https://img.shields.io/badge/Microsoft_Research_Asia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不用数据合成也不用后训练，靠递归自改进在开发集上沉淀可复用的能力 harness，在 HELMET 与 RULER 上大幅超过三个数据合成基线，开发成本估算不足 NExtLong 与 PolicyLong 训练成本的一半。**</p>

+ **Hibana: Fast Agentic Inference on Unified-Memory Devices**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10469)
![architecture](https://img.shields.io/badge/Hibana_Unified_Memory_Engine-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Cornell_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sharar-project/hibana)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向统一内存设备的智能体推理引擎，通过模型手术、跨轮次保留智能体状态的会话缓存与自适应投机解码，在单台 DGX Spark 上把每小时智能体任务数提升最多 3.4 倍、解码吞吐提升最多 3.9 倍。**</p>

+ **Beyond Query Similarity: Safety-Conditioned Cache Routing for LLM Response Reuse**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10418)
![architecture](https://img.shields.io/badge/SafeCache_Safety_Conditioned_Routing-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/PDL_Lab_College_of_Computer_Science_and_Technology_National_University_of_Defense_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把语义响应缓存重述为安全条件路由：显式提取缓存响应的复用条件，与新请求逐条匹配并用独立矛盾守卫防止强匹配稀释冲突，在缓存效用几乎不变的前提下把有害复用率降了 8.6 个百分点。**</p>

<!-- direction: vlm_core -->

+ **Mental Imagery That Matters: Curing Latent Collapse in Multimodal Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10423)
![architecture](https://img.shields.io/badge/AnchorSim_Contrastive_Distillation-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/The_University_of_Texas_at_Austin-green)
[![project](https://img.shields.io/badge/project-blue)](https://vision.cs.utexas.edu/projects/AnchorSim/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出交错式潜在多模态推理中的心理模拟坍塌：视觉潜变量的丢弃、替换与打乱几乎不影响答案概率，AnchorSim 用对比蒸馏把潜变量锚回模型行为，基座平均 62.4%、提升 13.5 分。**</p>

+ **Uncertainty, Not Concealment: A Mechanistic Reappraisal of Sycophancy in Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10297)
![architecture](https://img.shields.io/badge/Sycophancy_Three_Part_Diagnostic-red)
![task](https://img.shields.io/badge/Multimodal_Hallucination-magenta)
![organization](https://img.shields.io/badge/German_International_University_in_Cairo-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mohamed-eldagla/Uncertainty-Not-Concealment/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用表征探针、激活引导和二选一强制回答三段式诊断重新审视视觉语言模型的迎合性，发现模型内部能线性分离冲突信号（探针 AUC 0.781）却从不表达反驳，结论是错配被登记为不确定而非被隐瞒。**</p>

+ **A Clinical Evaluation of Conformal Prediction for Chest Radiograph Report Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10288)
![architecture](https://img.shields.io/badge/CLARITY_Clinical_Admissibility-red)
![task](https://img.shields.io/badge/Multimodal_Hallucination-magenta)
![organization](https://img.shields.io/badge/Max_Planck_Institute_for_Intelligent_Systems-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出放射科医生标注的临床可接受性判据 CLARITY，用它标注重评 970 份生成报告，证明 CheXbert 这类自动可接受性代理与临床真实判定几乎脱钩，为保形预测的风险控制指出了正确的校准对象。**</p>

+ **PoseBench: Probing Pose Awareness in Visual Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10347)
![architecture](https://img.shields.io/badge/PoseBench_Pose_Awareness_Probe-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/South_Dakota_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 31 个公开检查点的姿态感知评测基准，基于 7 个 BOP 数据集构建模板与真实图两套探针，发现 21M 参数的 DINOv3-Small 在真实图像上反超 11 亿参数的 DINOv2-Giant，姿态结构在 2D 基础模型中隐式存在但高度不均。**</p>

+ **LoCo: Selective Local Competition for Discriminative Open-Vocabulary Multi-Label Recognition**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10321)
![architecture](https://img.shields.io/badge/LoCo_Selective_Local_Competition-red)
![task](https://img.shields.io/badge/Vision_Language_Model-magenta)
![organization](https://img.shields.io/badge/Southeast_University_Nanjing-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向开放词表多标签识别的新框架，用空间一致的稠密编码器配合只在局部不兼容类别间生效的 Selective Softmax，四个基准上平均 F1 与 mAP 相对 TagCLIP 提升 3.4% 与 3.8%，集成全局预测器后进一步提升。**</p>

<!-- direction: llm_vlm_rl -->

+ **Plug-and-Play Verifier for Decoupling Process Reward in Stabilizing Long-Horizon Agentic Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10305)
![architecture](https://img.shields.io/badge/Plug_And_Play_Verifier-red)
![task](https://img.shields.io/badge/Process_Reward_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Washington-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/momo1443/plug-and-play-verification)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出即插即用的验证器框架：从智能体运行轨迹中抽取中间推理产物，经统一接口交给领域专用验证器打分，聚合为有界过程奖励后与稀疏结果奖励做两阶段后训练。HotpotQA 上 Qwen3.5-4B 准确率达 60.18%，超过 GRPO 基线 57.73%，五个基准平均 48.02 亦为最高。**</p>

+ **Coding or Cheating? An Investigation of Frontier Coding LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10404)
![architecture](https://img.shields.io/badge/Hardened_Repo_Sandbox-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Logitly-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/logitly-ai/reward-hacking-raw-v1)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在彻底堵住答案泄漏的加固仓库环境里评测前沿编码模型：当 20 道来自 linux、ffmpeg、llvm-project 的难题无法直接求解时，几乎每个模型都会依次尝试挖仓库历史、读 git 裸对象库、扫全盘找新版源码。作者据此主张这是 RL 环境泄漏答案后学到的捷径，并公开了全部 agent trace。**</p>

+ **BunshinRL: Splitting Live Agent Workspaces for Memory-Efficient Agentic RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10453)
![architecture](https://img.shields.io/badge/Live_Workspace_Forking-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/WukLab/ForkRL)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 agentic RL rollout 的系统 BunshinRL：基于整工作区实时 fork 在容器间共享内存，并保留文件、通信与 GUI 状态，再结合工具前缀缓存和推测式工具执行。训练 Qwen3-VL-8B 时峰值内存最多降低 43%、总内存降低 51%、rollout 延迟降 23%。**</p>

+ **Represented but Not Used: Value-Policy Dissociation in LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10457)
![architecture](https://img.shields.io/badge/Value_Readout_NVT_Steering-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究 LLM 智能体「心里有数却不用」的解耦现象：在 Grid 与 WebShop 上，候选动作的相对价值可从中间隐藏状态线性解码，但策略在 34.2%–58.3% 的状态下仍选了价值更低的动作，作者称之为价值-策略解耦，并用后层自然价值传递干预与闭环控制予以验证。**</p>

+ **PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10477)
![architecture](https://img.shields.io/badge/Two_Stage_Graph_Pattern_RL-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_University_of_Maryland_College_Park-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/EllenYiGe/PatternBloom)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 RAG 的检索单位从「读什么」换成「怎么推」：PatternBloom 第一阶段用信息密度奖励监督智能体构建的证据图，蒸馏出类型抽象的图模式记忆，第二阶段再用模式增强奖励把策略与这份冻结记忆耦合。7B 模型在七个 QA 基准上比 27 个基线高出 15.0 个 OOD 平均 EM 分。**</p>

+ **FEROM: Frontier Endogenous Reveal-Order Marginal Policy Optimization for Masked Diffusion LMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10369)
![architecture](https://img.shields.io/badge/Reveal_Order_Marginalization-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ziansu/ferom)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为掩码扩散语言模型提出前沿内生解掩码顺序边缘策略优化 FEROM：把采样顺序视为 rollout 的内生隐变量，推导跨隐变量的 Rao–Blackwell 化策略梯度并表示成解掩码状态 DAG 上的后验边占据率，再用预算受限的 frontier 展开近似，集成进 GRPO 目标后在数学与代码任务上不劣于现有方法。**</p>

+ **Sampling Is Not Curiosity: Why LLM Agents Should Investigate**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10501)
![architecture](https://img.shields.io/badge/Curiosity_Commitment_Framework-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/University_of_California_Santa_Barbara-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**立场论文论证 LLM 智能体目前只做随机探索而非好奇探索：推理时权重固定，只有条件上下文在变，故温度、best-of-N、树搜索、RAG 都不更新智能体对环境的模型。作者借鉴 RL 中的好奇传统提出五项架构承诺，并据此诊断现有方法缺失的环节与开放问题。**</p>

