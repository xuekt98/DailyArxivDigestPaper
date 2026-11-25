<!-- direction: llm_core -->

+ **PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30205)
![architecture](https://img.shields.io/badge/Row_Packed_Self_Speculation-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把推测位置打包进本来就要读取的 KV 行，PackLoop 在 164 个并发负载点的 161 个上快于逐点最优调度，中位加速 1.25 倍、最高 1.76 倍，且 FP32 输出与自回归解码逐 token 相同。**</p>

+ **ModernELECTRA: Replaced-Token Detection with Boundary-Window Reconstruction for Compact Encoders that Classify and Embed**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31495)
![architecture](https://img.shields.io/badge/Boundary_Window_RTD_Encoder-red)
![task](https://img.shields.io/badge/Pretraining-magenta)
![organization](https://img.shields.io/badge/Knowledgator_Engineering-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Knowledgator/FlashDeBERTa)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 ELECTRA 的替换检测主目标上只加一个训练期即丢弃的边界窗口重建任务，31M 英文编码器 GLUE 达 86.0、61M 多语言模型 85.1，超越同规模 Ettin-Enc-32m 的 83.5 与 MiniLM-L12 的 84.6。**</p>

+ **Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30554)
![architecture](https://img.shields.io/badge/Near_Far_Sparse_Attention-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近远分离的区域感知稀疏注意力 NFA 先在 prefill 判定可跳过的区域，再对远近页面差异化打分排序，在 Qwen3-8B、512K 上下文下相对 FlashInfer 取得最高 5.49 倍算子加速与 2.97 倍整模解码加速。**</p>

+ **Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30587)
![architecture](https://img.shields.io/badge/Commitment_Risk_Calibrated_Quant-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在带缓存的真实解码器下重估 dLLM 的 W4A4 量化：强制提交只占 16.5% 至 29.2% 的提交却承担 88.8% 至 97.1% 的永久翻转，DECAL 据此重加权层校准，并用保 argmax 的提交温度抵消最多 13.3% 的额外前向。**</p>

+ **Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31094)
![architecture](https://img.shields.io/badge/Loop_Residual_Attention-red)
![task](https://img.shields.io/badge/Test_Time_Compute-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/NUS-HPC-AI-Lab/LoopRes)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让循环层直接关注更早循环的输出、给每个循环配可训练的 loop-aware key 并只保留最近 W 个循环的残差窗口，LoopRes 在 6 个预训练模型、9 个基准上于 2 倍算力把 Qwen3-1.7B-Base 相对 SFT 提升 29.1%。**</p>

+ **Look Back, Draft Ahead: Corrective Prefix Attention for Parallel Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31112)
![architecture](https://img.shields.io/badge/Corrective_Prefix_Attention-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Ascend_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/MohammadMahdi1375/vLLM_NPU)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让并行草稿块内的每个候选关注块内更早的选择、并用辅助自回归损失监督共享骨干，CPA 在 8 个数学、代码与对话基准上每轮提交 token 比 DSpark 多 13% 至 15%、比 DFlash 多 25% 至 26%，贪心解码加速 3.35 倍与 3.37 倍。**</p>

+ **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32954)
![architecture](https://img.shields.io/badge/Lossless_KV_Cache_Compression-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/East_China_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以每头两级 3-bit 无损码压缩 KV 高字节，LoomKV 把 BF16 KV 压到原体积 0.71、FP8 压到 0.85 至 0.87，在未改动的引擎上让分层等效 1.4 倍原始容量，LRU 断崖处 goodput 达原方案 2.7 至 3.6 倍。**</p>

+ **VADE: A Verifiable Agent Data Engine from Professional Sources**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30202)
![architecture](https://img.shields.io/badge/Verified_Agent_Data_Engine-red)
![task](https://img.shields.io/badge/Data_Curation-magenta)
![organization](https://img.shields.io/badge/University_of_Waterloo-green)
[![project](https://img.shields.io/badge/project-blue)](https://tiger-ai-lab.github.io/VADE/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**数据引擎 VADE 用「参考分析加独立代理复现验证加条目级评分契约」自动构造可验证的专业分析任务，覆盖金融、法律、医学与能源四域，金融 1000 题、法律 372 题，186 道金融任务的专家评审有 93.5% 无需实质修改。**</p>

<!-- direction: vlm_core -->

+ **PixelOne: From Options to Pixels in a Single Forward for GUI Grounding**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30235)
![architecture](https://img.shields.io/badge/Pixel_Level_GUI_Grounding-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GUI 定位从固定全局分桶改为原生分辨率下的单次前向预测：教师用搜索逐步放大候选区域，学生继承其参数并做空间蒸馏，PixelOne-Pro-35B-A3B 在 4 个基准上均值 83.8%、每目标 0.43 秒，为所测单次前向方案最高。**</p>

+ **S1Arena-MM: Which Multimodal Decisions Can Be Left to System 1?**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29773)
![architecture](https://img.shields.io/badge/System1_Multimodal_Arena-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/The_University_of_Texas_at_Austin-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zhaoyang02/S1Arena-MM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多模态决策基准 S1Arena-MM 用同一批决策请求评测 33 个开源模型（12 个 System-1 加 21 个 MLLM）并对概率打分，含 51,060 道题、94 个任务与 102 个闭环游戏环境；图像上最佳 System-1 模型领先最佳 MLLM 4.9 个百分点，BALROG 进度 22.0% 对 9.7%。**</p>

+ **Replay Before You Reply: Second-Look Prompting for Unified Multimodal Encoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30909)
![architecture](https://img.shields.io/badge/Second_Look_Prompting-red)
![task](https://img.shields.io/badge/Vision_Language_Model-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在因果注意力下把图像与问题对在输入中重复一遍形成 ⟨V,T,V,T⟩，训练零成本的 Second-Look Prompting 在 12 个基准上提升了全部 9 个开源模型与 3 个闭源模型的平均分，Gemini 3 Flash 在 MATH-Vision 上最高涨 5.6 分。**</p>

+ **One Step, Four Clocks: How GUI Agents Fall Out of Step**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31522)
![architecture](https://img.shields.io/badge/Chronotope_GUI_Controller-red)
![task](https://img.shields.io/badge/GUI_Agent-magenta)
![organization](https://img.shields.io/badge/Hadron-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用环境变化、观测可用、决策提交、动作接收四事件解释 GUI 代理为何选对动作仍失败，并在 Paused、Replay、Live 三种执行下对比；仅更新待提交点击就把 Moving Balloon 成功率从 0% 提到 100%，Chronotope 中位延迟再降 85.5%。**</p>

+ **RVLM-X: Towards a Universal VLM Harness**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31755)
![architecture](https://img.shields.io/badge/Recursive_VLM_REPL_Harness-red)
![task](https://img.shields.io/badge/Computer_Use-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让 VLM 在持有全分辨率图像的持久化代码 REPL 中自行递归选区放大，RVLM-X 在 7 个公开基准上全部优于单次调用并取得 77.5% 最高合并精度，程序生成的 MapGenBench 留出集答对 71.4%，最强基线 55.5%。**</p>

<!-- direction: llm_vlm_rl -->

+ **Online Environment Repair for Coding Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32037)
![architecture](https://img.shields.io/badge/OER_Gate_Verified_Verifier_Repair-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Hunyuan_Team_Tencent-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在线环境修复把 coding agent 的 reward hacking 从惩罚策略转成修补验证器：20 次受控 GRPO 实验中累计漏洞率从 36.9% 降到 0.06%，未打补丁的 held-out Pass@8 从 21.7% 提升到 46.7%。**</p>

+ **ASTERISM: Do Multimodal LLMs Actually Look at All the Images?**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32316)
![architecture](https://img.shields.io/badge/ASTERISM_CICA_Credit_Assignment-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Machine_Intelligence_Lab_University_of_Seoul-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/chanseul01/ASTERISM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ASTERISM 审计 19 个多图基准的 32,688 条题目，发现 24.2% 只需一张图即可作答；作者据此建 18.7k 题的干净基准与 49k 训练集，并用跨图信用分配 CICA 在三个开源 MLLM 上把分数提高 2.6 到 6.0 分。**</p>

+ **VenusOCR2.0: Towards Efficient and Effective Document Parsing**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32617)
![architecture](https://img.shields.io/badge/VenusOCR_Compact_OTSL_Recognizer-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/VenusOCR_Team_Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/flow3rdown/VenusOCR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VenusOCR2.0 用 1B 参数解析文本、表格与公式：指标对齐 RLVR 把 OmniDocBench v1.6 总分从预训练 94.96 推到 96.24，配 Tele-layout 达 96.45、公式 CDM 98.57，PTPv2 另给 2.96 倍单请求无损加速。**</p>

+ **Accuracy Is Not Evidence: Measuring and Training Evidence Dependence in Video Temporal Grounding**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30320)
![architecture](https://img.shields.io/badge/Evidence_Dependence_Placebo_Audit-red)
![task](https://img.shields.io/badge/GRPO_Video-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![project](https://img.shields.io/badge/project-blue)](https://jinzijie-bupt.github.io/Accuracy-Is-Not-Evidence/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇论文指出视频时序定位的 IoU 奖励可以盲拿：三个用 IoU 奖励 RL 的公开 checkpoint 把 Qwen2.5-VL-7B 准确率抬高 9 到 20 点却没提升证据依赖，作者用安慰剂对照的证据依赖目标在五个基座上修好了这一点。**</p>

+ **Auxiliary Clues Aware's Geometry Problem Solving**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30617)
![architecture](https://img.shields.io/badge/AuxCA_Clue_Dependency_GRPO-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fukua23/AuxCA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AuxCA 用辅助线索依赖度给 GRPO 的 token 优势加权，教模型隐式构造辅助线：8B 模型在辅助依赖平面几何上完整准确率从 18.4 提到 31.7、加权从 24.6 提到 44.6，并零样本迁移到 MathVista 提升 2.9 点。**</p>

+ **From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30627)
![architecture](https://img.shields.io/badge/APRM_Attention_Process_Reward-red)
![task](https://img.shields.io/badge/Process_Reward_Model-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**APRM 用隐藏状态与注意力图构造内部过程奖励，只有约 46M 参数，作为插件接入 GRPO 等 RL 方法后跨模型与算法平均 pass@8 提升 2.88%，同时让模型的推理轨迹趋于更短。**</p>

+ **WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30662)
![architecture](https://img.shields.io/badge/WeMM_Ecom_OPD_Merge_GRPO-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/WeChat_Vision_Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tencent/WeMM-Ecom)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WeMM-Ecom 用两阶段继续预训练加混合思考的 OPD、参数合并与 GRPO 后训练，在覆盖 8 个场景 207,117 条样本的 28 个电商基准上，35B-A3B 以 74.35 分居首，超过 5 到 22 倍大的开源旗舰模型。**</p>

