<!-- direction: llm_core -->

+ **Multi-Branch Transformer**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19800)
![architecture](https://img.shields.io/badge/Multi_Branch_Transformer-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/GaotangLi/Multi-Branch-Transformer)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把完整 Transformer 块并行组成分支再融合输出：在 0.8B–2.1B 四个 MoE 规模上 2 分支 Wide-Shallow 在同等参数量与算力下优于顺序模型，Joint-KV 共享缓存后 KV 占用最多降 34%、单卡 H200 解码吞吐最高提升 51.4%。**</p>

+ **K2-Horizon: A Frontier Fleet of Open Source Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21003)
![architecture](https://img.shields.io/badge/Mixture_of_Value_Attention-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/Institute_of_Foundation_Models-green)
[![project](https://img.shields.io/badge/project-blue)](https://ifm.ai/k2/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以舰队形式开源 6 个模型（0.9B 稠密到 375B-A23B MoE），结构新意是 MoVA 把 MoE 下探到注意力 value 投影加 softplus 门控：36B-A4B 用七分之一激活参数逼近 32B 稠密模型，Uno 扩散适配器免草稿模型加速解码 2.2 倍。**</p>

+ **Superfluid: Local AI Server for Distributed LLM Inference**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17753)
![architecture](https://img.shields.io/badge/Superfluid-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Base_Compute-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/basecompute/superfluid)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本地/跨机 LLM 推理服务器，把交互式对话与 agent 批量任务的调度拆开：M5 Pro 上插在 8 个忙 agent 后的聊天首 token 仅 1.5 s（llama-server 等要 291–612 s），6 机 64 用户一小时吞吐 112→534 tok/s。**</p>

+ **Architectures and KV Replay for Depth-Recurrent Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19446)
![architecture](https://img.shields.io/badge/Recurrent_KV_Replay-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/NXAI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统研究深度循环语言模型的缓存账：共享注意力并不共享各次迭代的 KV 状态，缓存随循环深度增长；论文用 mLSTM/Gated DeltaNet 加周期锚点、PARCAE 工作区与「循环 KV 重放」三条路线比较，并把推理时的共享拓扑直接写进训练。**</p>

<!-- direction: vlm_core -->

+ **Glance, then Select: Evidence-Tempered Visual Token Selection for Extremely Compressed Multimodal LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20006)
![architecture](https://img.shields.io/badge/Glance_ETD-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视觉 token 压到 5% 的两阶段方案：低分辨率扫视后只对问题相关区域原分辨率重编码，再用证据加多样性的选择器挑 token；Qwen3.5-4B 保留全量性能的 91.6%（14 个基准），比 LT-OPD 高 17.3 分，4K 首 token 快 3.1 倍。**</p>

+ **Seen but Unsaid: Locating and Repairing Cross-Image Comparison in Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21539)
![architecture](https://img.shields.io/badge/Attention_Head_Repair-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/University_of_Toronto-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**定位并修复 VLM 跨图比较失效：重分配 16–32 个头的跨图注意力会掉 17–32 分准确率（随机头最多 7 分），只训练这些头的 query/key 投影（约 0.02% 参数）即让 SPair-71k 提升 28.3 与 25.1 分，并迁移到 HPatches 与 BLINK。**</p>

+ **Visual Marking as a Native Reasoning Capability for Multimodal LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20278)
![architecture](https://img.shields.io/badge/SelfMark-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视觉 token 网格当画布，让 MLLM 在原生视觉特征空间用 locate–mark–read 写与图像空间对齐的标记：单模型联合训练四类任务、6 个基准上超过专用方法，换更强 backbone 后连线追踪从 71.8% 升到 82.2%。**</p>

<!-- direction: llm_vlm_rl -->

+ **ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18533)
![architecture](https://img.shields.io/badge/ModHarness_RL-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/The_Pennsylvania_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 agentic RL 的 harness 改写成可从数据学习、随模型演化的程序，用 Compression 重组历史、Steering 在行为偏离时纠偏；CodeSearch 上比固定 harness 平均提升 19%，比最强可学习基线高 5%–12%。**</p>

+ **SARGO: Agreement-Gated Reinforcement and Suppression via On-Policy Self-Guidance for Visual Hallucination Mitigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19388)
![architecture](https://img.shields.io/badge/SARGO-red)
![task](https://img.shields.io/badge/Multimodal_RLHF-magenta)
![organization](https://img.shields.io/badge/Tsinghua_Shenzhen_International_Graduate_School_Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 on-policy 自引导把 response 级优势拆到 token 级：按教师 grounding 支持度做直接与互反加权，并以整体优势与幻觉专项优势的符号一致性做路由门控，三个 VLM backbone 上 CHAIRi 相对基线下降 40.6%–49.1%。**</p>

+ **GEM-MM: Reducing VLM Hallucination with Entropy-Guided Preference Alignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20016)
![architecture](https://img.shields.io/badge/GEM_MM-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/SNOWTEAM2023/GEM-MM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把熵引导偏好建模用于 VLM：on-policy 采样候选、奖励高熵推理分叉、惩罚不确定答案，再用组归一化策略梯度更新；3000 条 prompt 预算下熵深度偏好 61.7%，AMBER 幻觉 23.4→20.6、CHAIR 5.0→4.6。**</p>

+ **GPRM: Global Perspective Process Reward Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20755)
![architecture](https://img.shields.io/badge/GPRM-red)
![task](https://img.shields.io/badge/Process_Reward_Model-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**联合建模问题、历史步骤及其评估、当前步与未来步做全局过程奖励，并聚合 look-back、look-ahead、self-check、problem-alignment 四个诊断维度；4B 模型在 PRMBench/ProcessBench 得 73.9/74.3，超过 GPT-4o 与 o1-mini。**</p>

+ **ALIVE: Making Streaming Video Models Interactive**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21366)
![architecture](https://img.shields.io/badge/ALIVE-red)
![task](https://img.shields.io/badge/GRPO_Video-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://lijinzhao30.github.io/ALIVE/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让流式视频模型学会交互：用 ALIVE-SFT-288K 做对比式 SFT，再用 ALIVE-RL-3K 配合 BACA 的轨迹级与局部优势做 RL；IPIBench 总分从基座 24.0 升到 46.4，ProactiveVideoQA 的 PAUC 从 43.0 升到 51.6。**</p>

+ **Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21538)
![architecture](https://img.shields.io/badge/Verifier_Gap_Audit-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Anna_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在过程奖励可精确计算的授权策略设定下，沿七个现实轴退化 verifier 并观察 reward hacking：sufficiency 代理奖励停在 0.940，真实保真度却从 0.731 跌到 0.667；论文同时给出可预判表型的 model-free 审计流程。**</p>

+ **ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21605)
![architecture](https://img.shields.io/badge/CrossRPO-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Rochester_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/huawei-lin/ViRA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CrossRPO，在一组只差一个小物体的图像变体上做集合级奖励并证明不会奖励靠常识猜出的解；仅用约 3,500 条训练数据，ViRA-Bench 最高分辨率下集合准确率 63.3%，高于 GRPO 的 59.3%。**</p>

+ **ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18494)
![architecture](https://img.shields.io/badge/ARCHER-red)
![task](https://img.shields.io/badge/RL_for_Reasoning-magenta)
![organization](https://img.shields.io/badge/Stevens_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把自由 CoT 编译成含计算器调用与确定性观测的类型化动作轨迹，再用非对称分层 RL 强化小模型；五个标准 backbone 上宏平均比最强工具增强基线高 5.51 分，40 个模型-基准组合全部最优或并列最优。**</p>

+ **Fine-Grained RLAIF for Visual Safety: Learning to Zoom into Hazards for Multimodal Safety Alignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19786)
![architecture](https://img.shields.io/badge/FGR-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把图像 zoom-in 变成可学习的感知策略，用视觉证据、工具格式与安全推理三段分解奖励做 RLAIF；在 1,200 样本四域安全基准上准确率 86.71%–93.00%，同 backbone 下全面超过 SAFER-style 与 GPT-o3。**</p>

+ **Interactive Structured Environment Scaling for Large Language Model Agentic Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19871)
![architecture](https://img.shields.io/badge/RISE-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出结构化 RL 的预过滤子图把候选空间压缩 2.16×10^5 倍，问题盲的度数启发式即可 33.27% 命中 top-10；RISE 改用完整 Freebase 交互环境与自演化能力前沿 bandit，覆盖 19 个基准与三个 backbone。**</p>

+ **SpeCal: Spectral Calibration for Unsupervised RLVR**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20691)
![architecture](https://img.shields.io/badge/SpeCal-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用隐状态谱做双层校准改造无监督 RLVR：组级以谱质量与有效秩带通门控加权，rollout 级以留一子空间谱支撑度量；在 Qwen3-8B-Base 上把平均准确率从 42.7 提到 45.6，域外也提升 1.1 分。**</p>

