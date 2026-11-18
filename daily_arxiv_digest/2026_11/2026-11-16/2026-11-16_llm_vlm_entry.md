<!-- direction: llm_core -->

+ **Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17696)
![architecture](https://img.shields.io/badge/Co_Sight_Harness-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/ZTE_Corporation-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZTE-AICloud/Co-Sight/tree/master/Co-Sight%20Harness)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Co-Sight 把长程业务 agent 的工作流定义、状态与领域知识外置为版本化控制资产，用状态机与可机器校验的验收门强制执行：120 例评测中无人值守完成率由 50% 升至 100%，检索召回 56% 升至 91.67%，延迟从 440 分钟降到 159 分钟。**</p>

+ **CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17808)
![architecture](https://img.shields.io/badge/CarryOn_Context_Manager-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/University_of_New_South_Wales-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CarryOn 用紧凑执行状态加细粒度可溯源证据管理长程 agent 上下文，学习式选择器无需额外 LLM 调用即可完成取舍；三 benchmark 三 Actor 上宏平均成功率 75.7%，比最强基线高 6.7 个百分点，同时平均每成功任务的归一化开销最低。**</p>

+ **Disentangling Forgetting from Utility: Lightweight LLM Unlearning via Orthogonal Null-Space Projection**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17864)
![architecture](https://img.shields.io/badge/UUE_Null_Space_Projection_Unlearning-red)
![task](https://img.shields.io/badge/Model_Editing-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UUE 把大模型遗忘重述为可控的模型编辑：把参数更新投影到保留知识表征的左零空间，并推导出把遗忘集嵌入推向对跖点的凸无目标闭式解，在 TOFU forget01 上把 ROUGE-L 遗忘分从 0.9530 压到 0.3178 而保留分仅从 0.9290 降到 0.9228。**</p>

+ **Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17880)
![architecture](https://img.shields.io/badge/Soteria_Verified_Hierarchical_Planning-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Soteria 在任何工具调用前先形式验证分层计划，再在运行期强制执行规格，在三个基准 207 个任务上对四个模型全部达成 100% 一致性与零规格违反，任务成功率平均为最强基线的 1.7 倍，并靠可复用子计划把计划中位长度从 11 个状态压到 8 个。**</p>

+ **LACCO: Local Accumulation with Computation--Communication Overlap**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17991)
![architecture](https://img.shields.io/badge/LACCO_Local_Accumulation_Overlap-red)
![task](https://img.shields.io/badge/Training_Infrastructure-magenta)
![organization](https://img.shields.io/badge/Sorbonne_Université_ISIR-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LACCO 用前瞻加主两阶段把全局通信与本地计算重叠，同时让所有副本共享全局聚合更新而不引入外层陈旧性，在 FineWeb 上预训练 134M 至 500M 模型时与 DDP 的差距不超过 1.77%，0.5B 模型在 0.5 Gbps 带宽下端到端加速最高 1.89 倍。**</p>

+ **VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18392)
![architecture](https://img.shields.io/badge/VelServe_Tail_Calibrated_Scheduling-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Microsoft-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VelServe 用自身迭代延迟的实测尾部校准每步解码可承担的预填充预算，把解码抖动转成可控裕量，在 Qwen3-8B 与 DeepSeek-V4-Flash 上把 SLO goodput 提到最强基线的 2.4–2.9 倍，在 DeepSeek-V2-Lite 上至少 4.4 倍。**</p>

+ **Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18459)
![architecture](https://img.shields.io/badge/Callo_Invalidated_KV_Speculation-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Callo 在预填充-解码分离部署下复用被上下文编辑作废的 KV 做推测草稿，提交前再用精确 KV 校验：草稿下一 token 与精确 KV 在 98.3% 的位置一致，32 token 窗口在 65% 的 miss 请求中整窗接受，双 GPU 上全请求加速 1.05–1.19 倍。**</p>

+ **Alignment with Reflect-Reasoning: Learning How To Follow Principles**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17398)
![architecture](https://img.shields.io/badge/Reflect_Reasoning-red)
![task](https://img.shields.io/badge/Safety_Alignment-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Reflect-Reasoning 用 SFT 加 GRPO 两阶段训练模型「如何对原则做反思推理」，无需人工标注数据；五个模型在留出原则上的成对胜率达 82.5%–94.7%，并泛化到医疗与金融两个分布外领域，同时降低罕见严重违规且不损伤原有安全工程。**</p>

<!-- direction: vlm_core -->

+ **DoubleTake: Focused Verification of Visual Evidence for Long-Document Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17853)
![architecture](https://img.shields.io/badge/Double_Take-red)
![task](https://img.shields.io/badge/Document_Understanding-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/small-code-cat/double_take)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DoubleTake 用「两次阅读加一次聚焦核验」在冻结 Qwen3-VL-8B-Instruct 上免训练地提升长文档问答：四个 benchmark 共 4,816 题的微平均准确率 66.76%，高于 MDocAgent 的 65.16%，且同页面同调用次数下问聚焦事实优于重复原问题。**</p>

+ **MMFlash: Faster Speculative Decoding for Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18482)
![architecture](https://img.shields.io/badge/MMFlash_Visual_Dependence_Drafter-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://fscdc.github.io/MMFlash/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MMFlash 面向视觉语言模型提出扩散草稿器，用有与无视觉输入的 next-token 分布 KL 度量视觉依赖度并对草稿器预测差的视觉相关 token 加权，配合稀疏注意力把长视频上下文压到约 1.6K，实现最高 3.58 倍无损解码加速。**</p>

+ **ParseBench-2: Severity-Aware Evaluation of Document Parsing**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17400)
![architecture](https://img.shields.io/badge/Parse_Bench_2-red)
![task](https://img.shields.io/badge/Document_Understanding-magenta)
![organization](https://img.shields.io/badge/LlamaIndex-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ParseBench-2 从专家严重度策略出发校准文档解析指标：覆盖 4,317 页与文本、格式、表格、图表、视觉定位、表单 6 个维度，评分取内容恢复分与严重度上限的较小值，六个严重度套件上更贴近专家判断且最多只惩罚 3.4% 的良性变体。**</p>

+ **Towards Seconds-level Video Representation: Quadratically Gated Feature Grid with Adaptive, Prediction-free Sampling**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17786)
![architecture](https://img.shields.io/badge/Q_GAS-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/MillenRosen/Q-GAS)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Q-GAS 用多分辨率显式 3D 特征网格配二次门控解码器与免预测的误差感知采样器，坐标可查询地表示视频：UVG 完整序列上单卡拟合加量化不到 50 秒、混合精度解码超 370 FPS，比 Instant-NGP 快 5.5–7.2 倍。**</p>

+ **Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17797)
![architecture](https://img.shields.io/badge/Vision_As_A_Tool-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://vision-as-a-tool.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Vision-as-a-Tool 把通用 MLLM 重构为 coding agent 可调用的外部视觉工具，用 transcribe、grep、inspect、align、diff 五个原子动作覆盖 Image-to-HTML、SVG、3D 三类任务，让纯文本 agent 也能外放视觉推理并提升保真度与几何精度。**</p>

+ **Zoom In, Scale Out: Metric Depth Models Mistake Digital Zoom for Moving Closer**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17903)
![architecture](https://img.shields.io/badge/Digital_Zoom_Invariance-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Daffodil_International_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用数字变焦给度量深度模型做免标签体检：每个模型 800 张 KITTI、NYUv2、DIODE 图上 Depth Anything V2 的深度指数 α=0.95，把裁剪放大当成相机靠近；按预测焦距或真实相机换算即可让误差回到接近 0，且无需任何标签。**</p>

<!-- direction: llm_vlm_rl -->

+ **Benchmarks Don't Talk Back: Learning Through Self-Disagreement**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17563)
![architecture](https://img.shields.io/badge/Self_Disagreement_GRPO-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Microsoft_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**单策略同时扮演正题、反题与综合裁决三个角色，用同一个精确匹配验证器同时给答案和裁决打分，GRPO 训练下 Qwen3-8B 九基准综合准确率由 50.0% 提到 55.9%，全程不需要奖励模型或偏好数据。**</p>

+ **See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17754)
![architecture](https://img.shields.io/badge/Full_Block_Estimator-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Kyoto_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/githubhyz/See_Every_Block_Once)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在掩码扩散语言模型后训练中，把 blockwise 代理目标的蒙特卡洛估计换成每个 block 恰好评一次的全块估计，保持代理目标与 GRPO 更新不变，五个基准上平均比随机采样高 12.79 分。**</p>

+ **Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17539)
![architecture](https://img.shields.io/badge/Reflexive_Evolution_Agent-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sache07/verifiable-pxrd)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把粉末 X 射线衍射结构测定写成可验证的智能体搜索问题，用前向模拟残差与结构匹配充当验证器，在 200 题基准上把精确结构恢复率从 27% 推到 69%，并支持推理期扩展。**</p>

+ **AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17790)
![architecture](https://img.shields.io/badge/Multi_Agent_RL_Supervisor-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Meituan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用感知器、提案器与编排器组成的多智能体系统接管 GRPO 训练的过程级监督，在 Qwen3-4B 上九个基准全面超过静态配方，AIME 2024 提升 20.00 个百分点，并支撑起 14.7 天无人值守训练。**</p>

+ **G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17814)
![architecture](https://img.shields.io/badge/GCAST_Governed_Continual_Self_Training-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![project](https://img.shields.io/badge/project-blue)](http://cai.1688.com/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**G-CAST 把部署电商 agent 的每日生产证据按奖励路由成 SFT、RL 与回归监控三条分支，用 token 级熵做组内优先级，并配上受治理的奖励演化与累积评估闸门，第 4 轮累积奖励做到 0.8078，高于 AutoTrainess 的 0.7911 且保留期奖励不降反升。**</p>

+ **PaperCritic: Training AI Reviewers to Assess the Soundness of Papers**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17834)
![architecture](https://img.shields.io/badge/Review_Point_F1_Reward-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 AI 审稿目标改为最大化审查点的精确率与召回率 F1，用两个奖励模型加一个覆盖率匹配器合成整篇评审级奖励并用 GRPO 训练，4B 模型在自建测试集上 F1 达 45.1，比最强 4B 训练基线高 21.4 个百分点。**</p>

