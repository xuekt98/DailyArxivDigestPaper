<!-- direction: llm_core -->

+ **Scaling Looped MoE Language Models under Matched Budgets: Information Flow and Parameter Allocation**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34276)
![architecture](https://img.shields.io/badge/Looped_MoE_Architecture-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/Meituan-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lxi01766/Scaling-Looped-MoE-Language-Models-under-Matched-Budgets-Information-Flow-and-Parameter-Allocation)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在等参数等 FLOP 约束下系统研究循环式 MoE：用门控内环状态更新加跨阶段残差改善信息流，把 Core 单次通过设为展开总深度的 25%-35%，省下的参数回填为每层额外路由专家，1T token 后 69B 与 51B 两版分别比非循环基线高 1.16 与 2.29 个百分点。**</p>

+ **Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31638)
![architecture](https://img.shields.io/badge/Wavefront_Low_Rank_Drafter-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/University_of_Oregon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**解码方法 Wavefront：将目标模型 4096×V lm_head（bf16 约 1.2 GB）换成低秩基座，修正头改为在草稿块内读取整段前缀并用并行 Jacobi 遍精修，固定遍数让草稿步无数据相关控制流、可捕获为单个 CUDA graph，Qwen3-8B 上吞吐超过 xPress、DSpark 与 DFlash。**</p>

+ **Factorized Context Attention: From Emulated to Native Grid Probing**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32423)
![architecture](https://img.shields.io/badge/Factorized_Context_Attention-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/King_Abdullah_University_of_Science_and_Technology_KAUST-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mohammad2012191/FCA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「网格探测」重解释为从模型外部模拟的注意力，并给出原生版本 FCA：训练无关的块稀疏注意力把输入只编码一次进 KV cache，再在模型内部按 12×12 网格批量读取局部与跨步跨度，长视频与超长文本上追平网格探测的准确率，耗时降到其零头。**</p>

+ **Rethinking Knowledge Distillation for Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33670)
![architecture](https://img.shields.io/badge/Trajectory_Consistent_Distillation-red)
![task](https://img.shields.io/badge/Distillation-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个扩散语言模型蒸馏的系统性研究，指出经典 forward-KL 的两个反直觉失效：学生困惑度随教师数据量非单调、同一语料下 FKL 蒸馏反而不如直接用 DLM 去噪目标；提出免数据的轨迹损失加置信度重加权加信赖域锚框架，MDLM 学生困惑度 24.75 反超教师 27.04。**</p>

+ **When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33893)
![architecture](https://img.shields.io/badge/Parallel_Subagent_Coding-red)
![task](https://img.shields.io/badge/Multi_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/cogito233/subagent-study)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**实证研究并行子智能体在写代码上到底何时有用：在 NL2Repo 与 ProgramBench 上对照单智能体，随机任务仅提升约 1 到 5 个百分点却要付最多 3.8 倍成本；硬任务收益更大，并把机制拆成自我检查、新鲜上下文与模块化三条，给出可操作的替代做法。**</p>

+ **Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34051)
![architecture](https://img.shields.io/badge/Stable_Gated_DeltaNet2-red)
![task](https://img.shields.io/badge/State_Space_Model-magenta)
![organization](https://img.shields.io/badge/MemTensor-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**定位 Gated DeltaNet-2 长上下文训练崩溃的根因：擦除算子读写不对称导致方向增益跨 token 累积，即使没有新写入也会让状态指数增长；改用对称擦除加衰减调节的残差写入后建立 O(√T) 状态增长上界，约 1.6B 模型在 128K 上的 RULER 均分比原版高 6.80 点。**</p>

+ **Improving Tail-Augmented Speculative Drafting with Hidden State Mixing and Gradient Detach**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34092)
![architecture](https://img.shields.io/badge/Hidden_State_Mixing_Drafter-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对自回归 MTP 与 EAGLE 草稿器的训练-推理错配，提出两个纯训练期方法：隐状态混合在同一预测目标下混合主干与 MTP 隐状态，隐状态梯度截断随机阻断梯度通路，二者都不增加推理开销；冻结主干下平均接受长度最高提升 52.2%，EAGLE-3 场景峰值训练显存比 TTT 低 48%。**</p>

+ **DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34776)
![architecture](https://img.shields.io/badge/DFly2_Shared_Sparsity_Drafter-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tencent/AngelSpec)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**原生稀疏目标模型的推测解码方法 DFly2：草稿层直接读配对目标层缓存的 KV，复用该层 indexer 选中的位置，不另建 cache；在 DS-V4.1-Flash、GLM-5.3-Flash 与 Hy4 flash 上接受长度超过 DFlash 与 DSpark，长上下文负载上领先 10.0% 到 31.5%。**</p>

<!-- direction: vlm_core -->

+ **Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31576)
![architecture](https://img.shields.io/badge/Scoped_Lesion_Probe-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/Rice_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/gezhixuan/moedep)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「激活图不等于必要性地图」引入多模态 MoE：对 Qwen3-VL-30B-A3B、Kimi-VL-A3B 与 Gemma-4-26B-A4B 找出 3% 到 12% 的视觉专属专家，Qwen3-VL 中它们承接四分之一图像 token 路由，但整体切除只掉不到 1 个百分点，真正的依赖在文本位置的双用途专家上。**</p>

+ **ViDM: Efficient and Order-Robust Parallel Visual Decision Making**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32461)
![architecture](https://img.shields.io/badge/ViDM_Parallel_Decision_Mask-red)
![task](https://img.shields.io/badge/VQA-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把共享视觉输入的多问推理从自回归逐 token 生成改造成单次前向的并行决策：把共享上下文、多个问题与决策槽编排进一条序列，用 Decision-Query Mask 对齐决策读出与问题，并叠加用例均衡的多顺序训练；Qwen3.5-4B 准确率由 73.49% 升到 77.55%，吞吐达基线 8.4 倍。**</p>

+ **STAR: Counterfactual Dual-World Rollouts and Spatial Target Adaptive Reconstruction for Visual On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32472)
![architecture](https://img.shields.io/badge/STAR_Dual_World_Distillation-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对视觉语言模型靠全局上下文与语言先验、忽略决定答案的局部细节，先用跨尺度诊断证明遮蔽局部证据后模型仍保留过半全图准确率，再提出 STAR：反事实双世界 rollout 暴露上下文捷径，教师在真实与均值色裁剪间的对比给出修正方向，配合空间注意力引导的逐 token 目标重建，六个细粒度基准上最多提升 8.04 个百分点。**</p>

+ **Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34036)
![architecture](https://img.shields.io/badge/Agentic_Model_Editing-red)
![task](https://img.shields.io/badge/Test_Time_Adaptation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把少样本适应流程本身交给 LLM 智能体设计：AME 让智能体联合设计输入变换、编码器编辑、特征计算与分类器拟合，输出可执行的领域定制适应程序，在支持集内用交叉验证诊断、独立验证集上打分选优；11 个数据集上以 CLIP ViT-B/16 取得无反向传播 81.2%、有反向传播 81.9% 的最高平均准确率。**</p>

+ **Rethinking Video Agents: When and Why Video Harnesses Work**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31883)
![architecture](https://img.shields.io/badge/Video_Relook_Harness-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/KlingAI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究视频智能体外壳何时有效：Video-Relook 让模型从默认时空采样出发自主调整观察，五个模型在 FastAct 细粒度动作理解上提升 3.0 到 14.2 个百分点；但同一接口下模型差异巨大，Qwen 3.7 Flash 纠正 250 个错误同时推翻 250 个正确答案，说明收益取决于模型把交互转成可靠修订的能力。**</p>

<!-- direction: llm_vlm_rl -->

+ **Rethinking Reasoning Effort Training in Large Language Models: On-Policy Distillation or Reinforcement Learning?**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32131)
![architecture](https://img.shields.io/badge/Dense_Anchor_Reasoning_Effort_RL-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/ERNIE_Team_Baidu-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/baidu/ERNIE-5.5-Flash-Preview)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统对比序列级奖励的强化学习与 token 级 on-policy 蒸馏：前者能把 AIME25 思考长度压缩 70%，后者在 33 个基准上分出 low/medium/high 三档，并让 high 档比参考策略高 3.1 分。**</p>

+ **AdProducer: Towards Agentic Advertising Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31466)
![architecture](https://img.shields.io/badge/Product_Research_Storyboard_Agent-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Institute_of_Artificial_Intelligence_University_of_Central_Florida-green)
[![project](https://img.shields.io/badge/project-blue)](https://lky-ang.github.io/AdProducer-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个端到端的广告视频生成 agent：自主检索产品并写卖点分镜，用 GRPO 联合分镜级与视频级奖励，在 305 条 brief 的 AdCreation-Bench 上把 MiniMax H3 的 PG-Score 从 17.3 拉到 51.3。**</p>

+ **NOBODY Was There: Bridging the Human-VLM Gap in Unwarranted Person Attribution Bias**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31714)
![architecture](https://img.shields.io/badge/Self_Judged_Caption_Preference_DPO-red)
![task](https://img.shields.io/badge/Multimodal_DPO-magenta)
![organization](https://img.shields.io/badge/UC_SANTA_BARBARA-green)
[![project](https://img.shields.io/badge/project-blue)](https://pmadinei.github.io/NOBODY/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**量化并修正「无人场景凭空归因到人」的偏差：25 个 SOTA VLM 的 caption 提及人眼是人类的四倍，用 5,844 对自偏好数据做 DPO 后，22 个模型与人类的一致率从 55.3% 升到 84.7%。**</p>

+ **Open-OmniCoach: Evidence-Enhanced Trajectory Learning for Omni Video Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31891)
![architecture](https://img.shields.io/badge/Step_Level_Evidence_Guided_SEPO-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/ByteDance_OmniCoach_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://open-omnicoach.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向全模态视频 agent 的证据导向框架：248.2K 条交互轨迹加上按证据增量分配信用的 SEPO，让 Open OmniAgent-30B 在 9 个基准上比 Qwen3-Omni 平均高 6.3 个点，LVOmniBench 与 LVBench 分别高 12.2 和 13.3 分。**</p>

+ **More Powerful, Less Verifiable? Mitigating Hard-to-Verify Hallucinations in MLLM's Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32055)
![architecture](https://img.shields.io/badge/Verifiability_Aware_Risk_Constrained_DAPO-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Institute_of_Trustworthy_Embodied_AI_Fudan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/pang-jh/RL-Verifiability)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现纯精度奖励会让模型剩下的错误更难被人发现：ITHV 用 2,728 条样本区分明显与难察觉幻觉，DAPO-V 在风险预算下加强低验证难度样本的惩罚，三个基座上难察觉幻觉准确率比只按精度训的 DAPO 高 5.78 到 9.72 个点。**</p>

+ **ARS-VLM: Visually Aligned Augmented Random Search for Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32147)
![architecture](https://img.shields.io/badge/Visual_Aligned_Zero_Order_Search-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/The_University_of_Melbourne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把前向零阶随机搜索引入 VLM 后训练：8B 上 20 步达到 61.0% 验证精度（GRPO 需 150 步），7 个 OOD 基准 micro 精度 75.41% 追平全参数 GRPO 的 75.31%，静态显存约 16.5 GB 而 GRPO 约需 64 GB。**</p>

+ **Avalon-M1: Reinforcement Learning from Collective Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32539)
![architecture](https://img.shields.io/badge/Shared_Advantage_Agent_Organisation-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/General_Reasoning_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用同一个 outcome 派生优势同时训练一整个 agent 组织：CEO 加最多 8 名专家共享策略，147 个环境上训出的 120B 模型在八人组织下把 IMO-ProofBench-Advanced 从 23.8% 提到 39.0%，同时推导延迟约为单 agent 的三分之一。**</p>

