# 2026-11-03 - LLM 后训练 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Controlling Sharpening in LLM Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03146)
![architecture](https://img.shields.io/badge/AtK_Adaptive_Pressure_Policy_Optimization-red)
![task](https://img.shields.io/badge/PPO_RLHF-magenta)
![organization](https://img.shields.io/badge/EPFL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**推导 KL 正则下 pass@k 与 max@k 的闭式最优策略，证明 @k 压力可由 @1 目标经提示自适应正则或奖励变换得到，提出 KAPPO 把 A*PO、GRPO、DPO 改造成 @k 优化器，在 AIME 2026 上与需多条 rollout 的 PKPO 持平而校准开销不超过 5%。**</p>
+ **Order-Only On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02112)
![architecture](https://img.shields.io/badge/Ordinal_TopK_Distillation_Loss-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Memphis-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 on-policy 蒸馏匹配教师 token 概率时把教师的自信度也当作信号、导致对温度敏感，这篇只让学生复现教师 top-K token 的排序而不对齐概率值，在六组师生配对上相对 OPD 平均最多提升 2.9 个点、AIME25 上最多 5.6 个点。**</p>
+ **Bernoulli On-Policy Distillation: Don't Ignore High-Confidence Student Tokens**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02093)
![architecture](https://img.shields.io/badge/Bernoulli_Probability_Matching_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Surrey-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/duterscmy/Bernoulli-OPD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**证明采样式 reverse-KL 的 OPD 梯度带 1−p_S 因子、会系统性压制高置信 token 的更新，提出直接匹配师生伯努利概率差的 Bernoulli OPD，在 Qwen3-1.7B 配 Qwen3-4B-Instruct-2507 的主设置中把五基准平均从 44.38 提到 51.76。**</p>
+ **Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03133)
![architecture](https://img.shields.io/badge/Student_Prefix_Conditioned_Teacher_Adaptation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Beijing_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出学生生成前缀会让教师监督可靠性下降且随前缀变长而加剧，提出在蒸馏前用前缀条件化的 RLVR 先把教师适配到学生实际访问的状态上，在三组师生配对上分别把五基准平均提升 3.78、3.03 与 0.82 个点。**</p>
+ **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02846)
![architecture](https://img.shields.io/badge/Branch_Parallel_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Qwen_Business_Unit_of_Alibaba-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出投机解码的 draft 监督不必继承 draft-and-verify 的顺序依赖，提出在参考锚点处并行采样多分支并打包成 proposal tree 的 SpecOPD，覆盖 8B/27B/125B 三类目标模型与三种 draft 架构，平均接受长度最高提升 41.45%、监督吞吐 16.09 倍。**</p>
+ **Chain of Faith: Policy-Internal Rewards for Reasoning Reliance**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02672)
![architecture](https://img.shields.io/badge/Policy_Internal_Reliance_Rewards-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/University_of_California_Davis-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「答案是否真的依赖自己生成的推理」做成可训练目标，提出只用策略自身信号的梯度敏感度、置信度差、渐进置信增益与推理-提示互换四种奖励加入 GRPO，在 GSM8K/StrategyQA 上显示依赖度可提升但准确率常下降，高权重下还会出现答案复制。**</p>
+ **What Drives the Zero-to-One Jump? Diagnosing and Steering Hard-Prompt Learning in RLVR**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02747)
![architecture](https://img.shields.io/badge/Negative_Augmented_Policy_Optimization-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/jameszhu-pixel-time/Z2O)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用首次命中正样本时间的事件分析发现成功跃迁前的负样本 rollout 早期保留更高生成熵，据此提出在 GRPO 内对未解出组的负样本排序并分配分级优势的 NAPO，在固定 rollout 预算下把 AIME24 的 Pass@256 提升 10.0 个点、AIME2025 提升 6.6 个点。**</p>
+ **Hindsight Credit Assignment over Trees for Agentic RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02706)
![architecture](https://img.shields.io/badge/Tree_Rollout_Hindsight_Credit_Assignment-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Alibaba_Cloud_Computing-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对长程 agentic RL 里成功样本稀缺的问题，提出以前缀共享 rollout 树加事后引导分支把稀缺成功转化为树内与树间信号的 TriGRPO，在 ALFWorld 上三个 Qwen2.5 尺度峰值成功率达 88.3%、93.8%、93.8%，比 root-only GRPO 高 15.5–20.9 个点。**</p>
+ **Whitened Advantage Summation Policy Optimization: Correlation-Aware Aggregation for Multi-Reward Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02609)
![architecture](https://img.shields.io/badge/Whitened_Advantage_Summation_Policy_Optimization-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/ProofMed_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出多奖励归一化加权求和在 ZCA 去相关基下实际施加 Σ^{1/2}w 而非选定权重，提出用 Σ^{-1/2} 白化优势后再加权的 WAS-PO，工具调用上三奖励训练奖励高 GDPO 3.8%，但增益未传导到留出准确率。**</p>
+ **RLVR Sharpens the Pencil, Not the Mind**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02574)
![architecture](https://img.shields.io/badge/Probe_Based_Internal_Representation_Analysis-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Technology_Roorkee-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**沿着 OLMo-2-1B 在 GSM8K 上的全部 13 个 checkpoint 追踪 RLVR 的内部变化：首答准确率 58.0% 升到 61.3% 而 256 次采样覆盖率仅 94.5% 升到 96.9%，错误探针 AUROC 恒在 0.798–0.840，唯一真实变化出现在最终答案 token（AUROC 0.93）。**</p>
