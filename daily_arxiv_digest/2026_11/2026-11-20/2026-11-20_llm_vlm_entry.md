<!-- direction: llm_core -->

+ **Lost in a Few Heads: Diagnosing and Repairing Block Selection in Sparse Attention**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21917)
![architecture](https://img.shields.io/badge/Blind_Head_Full_Attention_Repair-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Yale_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zhangwenhe1007/blind-attention-heads)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用精确注意力质量作 oracle，定位稀疏注意力里把 needle 排低的少数盲头，在 MiniCPM4.1-8B 的 64K 上把多键检索从 54.1% 修到 97.5%，全程无需训练。**</p>

+ **RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22179)
![architecture](https://img.shields.io/badge/Chained_Observation_Note_Memory-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/University_of_Chicago-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Jingyu6/rag-in-a-trenchcoat)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BRIDGE 用链式观察笔记加 BM25/余弦混合检索与时序渲染，在 LongMemEval-S 和 BEAM 上打平此前 SOTA，EverMemBench 反超最好记忆基线 5.7–6.3 分，并用 5 个对抗探针说明记忆设计各有所长。**</p>

+ **Toaster: Nonlinear Memory from Cascaded Linear Memories and Target Propagation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23648)
![architecture](https://img.shields.io/badge/Cascaded_Linear_Memory_Target_Propagation-red)
![task](https://img.shields.io/badge/State_Space_Model-magenta)
![organization](https://img.shields.io/badge/Google_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Toaster 用逐点激活串联两层线性记忆并靠 target propagation 训练隐藏层，每层仍走 delta-rule kernel，五个规模上 loss 全线低于 KDA，13 任务 three-shot 均值 51.84%，且比 Titans 快 2.8–5.5 倍。**</p>

+ **Long-Context Generation Is a Sampling Problem (When You Turn Up the Heat)**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22148)
![architecture](https://img.shields.io/badge/Sampler_Pool_Size_Control-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Thoughtworks-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**29 个开源权重模型、10 个基准与百万 token needle 检索显示长文本退化源于采样器：温度 2 时 top-p 类 coding agent 解决 0/100 个 SWE-bench 问题，top-nσ 解决 46–62 个，池大小与质量相关 −0.77。**</p>

+ **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22191)
![architecture](https://img.shields.io/badge/Shared_Read_Plan_Block_Diffusion-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Rice_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RISA 为 block-wise 扩散语言模型提出可恢复稀疏注意力，把历史保存与读取计划分离并在块内复用一份有界计划，32K 注意力加速 2.67×、128K 达 5.53×，任务精度与 dense 持平。**</p>

+ **XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22280)
![architecture](https://img.shields.io/badge/Scaleup_Memory_Sparse_Offload-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/Netpreme-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**XM-Sparse 面向 scale-up 内存池做稀疏注意力卸载：分析发现吞吐仍受 HBM 中常驻的热 KV 与 K-index 缓存限制，遂按访问模式分别用 TMA 融合检索与 GPU 发起 DMA 预取，DeepSeek-V3.2 上解码吞吐最高提升 4.98×。**</p>

<!-- direction: vlm_core -->

+ **Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24267)
![architecture](https://img.shields.io/badge/Active_Forager_Evidence_Routing-red)
![task](https://img.shields.io/badge/Video_QA-magenta)
![organization](https://img.shields.io/badge/Xian_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/TiezMind/ActiveForager)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ActiveForager 是流式视频取证 agent，只保留 4 帧干净工作窗口并按 Answer/ZoomIn/Recall/Wait 四路按需取证，用反事实信息增益训练防止工具坍缩，OVO-Bench 上 Qwen3-VL-8B 整体从 47.6% 提到 65.9%。**</p>

+ **SpatialMind: Adaptive Multi-Level Geometric Fusion for Spatial Reasoning in Multimodal Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22415)
![architecture](https://img.shields.io/badge/GeoFus_Adaptive_Geometric_Fusion-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/School_of_Advanced_Interdisciplinary_Sciences_University_of_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zhaosb-star/SpatialMind)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SpatialMind 用三路条件门控 GeoFus 自适应融合 VGGT 的浅/中/深几何特征，并用负熵正则防门控坍缩，VSI-Bench 取得 72.3 的 SOTA，验证几何粒度需随任务认知层次切换。**</p>

+ **Semantic-Guided Geometric Decoding for Token-Efficient Visual Grounding**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22577)
![architecture](https://img.shields.io/badge/Grid_Token_Geometric_Decoder-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/Huawei_Technologies_Co._Ltd.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SemGeo 为每个实例只生成一个网格 token 做粗定位，再由 11.02M 参数的几何解码器并行回归 1000 档离散框坐标，8 个基准中 6 个 F1@mIoU 最高，vLLM 下框生成吞吐达基线 2.07×。**</p>

+ **NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22790)
![architecture](https://img.shields.io/badge/SightForge_Verifiable_Task_Pipeline-red)
![task](https://img.shields.io/badge/Temporal_Grounding-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NexSight 用答案隐藏的验证器与反例检查筛出 108 段长视频上的 310 个可溯源任务，最强模型只有 54.52%、给标注证据即到 79.35%，不足 6K 样本后训练把交互准确率从 21.29% 翻倍到 42.26%。**</p>

+ **Visual Harness Scales General VLMs to Medical Images**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22815)
![architecture](https://img.shields.io/badge/VERA_Medical_Visual_Harness-red)
![task](https://img.shields.io/badge/VQA-magenta)
![organization](https://img.shields.io/badge/New_Jersey_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VERA 是面向医学影像的视觉 harness，用工具化探查、无损证据记忆与证据验证器补强通用 VLM，Qwen3.8-27B 在 11 个任务上全部提升，脾脏测量 63.3%→98.3%、GPT-6.1 Sol 肺结节检出 10.8%→69.2%。**</p>

+ **Learning Grounded Reasoning from Human Gaze**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23209)
![architecture](https://img.shields.io/badge/Gaze_Prior_Grounded_Reasoner-red)
![task](https://img.shields.io/badge/Grounding_Accuracy-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究收集 7,109 次人类眼动试次训练有依据的推理模型，发现眼动作先验优于监督完整注视序列：准确率 55.9%→62.8%，而完整序列虽对齐更高（1.04 对 0.82 bits/fix）却在 RL 后陷入重复检视。**</p>

+ **Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23228)
![architecture](https://img.shields.io/badge/Affine_Transition_State_Spool-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spool 利用线性循环层更新对状态仿射的性质，缓存每帧的状态变换并用段树组合，无需重放帧即可淘汰过期帧，20 项模型-基准测试 p95 首 token 延迟全部最低，几何均值比 vLLM 基线快 6.6×。**</p>

+ **SpecLook: Speculating Where to Look for Fast and Reliable Agentic MLLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23483)
![architecture](https://img.shields.io/badge/Speculative_Observation_Draft_Verify-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/University_of_Wisconsin-Madison-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SpecLook 训练免用地投机 agent 的下一次观察而非答案：小模型起草 glimpse 并重答，答案一致且置信度达到 98% 即退出，否则由大模型核验纠正，V*/HR-Bench/POPE 上每个 split 都最准，相对 DeepEyes-7B 快 7.7×。**</p>

+ **Read Together, Answer Apart: How Earlier Questions Help Vision-Language Models Look**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24785)
![architecture](https://img.shields.io/badge/Read_Together_Answer_Apart_Mask-red)
![task](https://img.shields.io/badge/VQA-magenta)
![organization](https://img.shields.io/badge/South_China_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 22 个 1B–35B 开源 VLM 上配对分析发现共问同时带来 15.4%–29.8% 的纠错和随能力上升的答案损坏，Read Together, Answer Apart 用免训练解码掩码保留共享 prefill、隔离答案，DCI 上 12/14 模型最多提升 4.71 分。**</p>

+ **The Elephant in the Question: Unified Models Picture the Concepts Behind Their Answers**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24793)
![architecture](https://img.shields.io/badge/V_Lens_Visual_Concept_Decoder-red)
![task](https://img.shields.io/badge/Omni_Model-magenta)
![organization](https://img.shields.io/badge/Technische_Universität_Darmstadt-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/multimodal-ai-lab/V-lens)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**V-LENS 借用统一多模态模型自带的图像生成器可视化任意 token 的隐状态，无需训练解码器；lens tuning 后 BAGEL、SenseNova-U1、HunyuanImage-3.0 正确可视化代词指代对象的比例从 2%–11% 提升到 86%–94%。**</p>

+ **Ultimate3D: Teaching Multimodal LLMs 3D Camera-Object Relations by Large-Scale Visual Instruction Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24795)
![architecture](https://img.shields.io/badge/Render_ControlNet_Instruction_Pipeline-red)
![task](https://img.shields.io/badge/Visual_Instruction_Tuning-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ultimate3D 用开源 3D 资产渲染深度/边缘/分割先验再经 ControlNet 生成保留精确相机-物体关系的照片级图像，配 240K 条带标注 VQA 与 8K 条基准，微调后开源 MLLM 在关系识别上平均比商用模型高 29.7%。**</p>

<!-- direction: llm_vlm_rl -->

+ **ViStep-RL: Stepwise Reinforcement Learning for Long-Horizon Visual Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24170)
![architecture](https://img.shields.io/badge/Evidence_Graph_Verifier_RL-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把长程视觉任务拆成带依赖的证据子目标图，验证器用图势增量发放净进展奖励、主动记忆跨轮保留证据，Qwen2.5-VL-7B 在 ViInteract 严格完成率达 60.0%，比同预算标准 GRPO 高 11.5 个百分点。**</p>

