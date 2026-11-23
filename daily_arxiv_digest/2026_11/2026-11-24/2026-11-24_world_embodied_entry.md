<!-- direction: world_model -->

+ **Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25594)
![architecture](https://img.shields.io/badge/Bradley_Terry_Language_World_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示用 Bradley-Terry 目标做比较反馈训练会把原本准确的语言世界模型概率推向不可能结局：仿真推杆任务上原本 2.4 个百分点的危险误差，变成 33 到 43 个百分点的概率错配。**</p>

+ **Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25626)
![architecture](https://img.shields.io/badge/Dual_Conditioned_Forced_Response-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用双重视觉-数值条件改造 6 个图像到视频骨干，仅靠 flow-matching 损失就能复现线性响应与共振、5 个模型捕获非线性软化，而软化在训练数据中仅占 0.74%，是视频世界模型真学到物理的细致证据。**</p>

+ **Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25980)
![architecture](https://img.shields.io/badge/Action_Effect_Matching-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 AFFECT 辅助训练目标：向遥操作动作注入时间相关噪声，教世界模型学会动作扰动如何改变未来画面，DROID 上策略成功率的相关系数从 0.47 升到 0.79、FVD 最多降 23%。**</p>

+ **LATER: Learning Action-Conditioned Temporal Evidence Retrieval for Predictive World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25671)
![architecture](https://img.shields.io/badge/Temporal_Evidence_Retrieval_Bridge-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 CF-JEPA 之上加入响应桥与分区记忆，把早期交互揭示、后期观测不再显示的物理属性按动作条件化检索回来：受干扰推杆任务终局成功率由 15.5% 提升到 25.0%，读出误差降 20.2%。**</p>

+ **Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25927)
![architecture](https://img.shields.io/badge/Fast_JEPA_Planning-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Sofilyzia/Fast-JEPA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**重组潜空间世界模型的预测计算方式，用目标导向方案引导搜索并直接预测完整候选终态，四个基准上平均成功率 96.50%、规划快 2.41 倍，并在 DynaGoal 上验证动态偏移与截止条件。**</p>

+ **Point Dynamics as Proxy for Robotic World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25946)
![architecture](https://img.shields.io/badge/Point_Dynamics_Proxy-red)
![task](https://img.shields.io/badge/Learned_Simulator-magenta)
![organization](https://img.shields.io/badge/Institute_of_Foundation_Models-green)
[![project](https://img.shields.io/badge/project-blue)](https://marsaki.github.io/point-dynamics-proxy/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 3D 点动力学作为机器人世界模型与视频渲染之间的代理：首帧抬升成点后由学到的动力学模型模拟响应再渲染回像素，DROID 上物体运动误差降 8.6% 与 6.2%、真机双臂降 8.1%。**</p>

+ **Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26825)
![architecture](https://img.shields.io/badge/Skill_JEPA-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Centro_Nacional_De_Inteligencia_Artificial-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/tcouso/Skill-JEPA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出规划器从高斯采样候选、世界模型却只见过结构化动作这一错配，用条件 VAE 学出与规划器对齐的技能空间：80 步远目标成功率由 42% 升至 62%，AntMaze 由 0.4% 升至 38%。**</p>

+ **LoCo-WAM: Test-Time Training as Long Context for World-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26853)
![architecture](https://img.shields.io/badge/LoCo_WAM-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Amazon_AGI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把测试时训练当作长上下文：保持短历史窗口不变，用新观测帧更新视频专家的低秩适配器，RoboCasa GR-1 上 2.4 秒历史追平 9.6 秒基线、4.8 秒历史再高出 4.8 个百分点。**</p>

+ **ViewDreamer: A Robot World Model beyond Fixed Camera Setups**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26981)
![architecture](https://img.shields.io/badge/ViewDreamer_Cross_View_Slots-red)
![task](https://img.shields.io/badge/Video_Prediction-magenta)
![organization](https://img.shields.io/badge/Meta_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://matchlab-imperial.github.io/ViewDreamer/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向相机数量、位置与顺序都随本体变化的机器人视频生成，把逐视角生成与跨视角交互解耦、只用共享 slot token 传信息，在覆盖 1 到 4 相机的 RoboView-Bench 上生成质量最佳并改善跨视角一致性。**</p>

+ **A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27124)
![architecture](https://img.shields.io/badge/Round_Trip_Plan_Check-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出潜空间世界模型的规划结果可能只是对抗样本：CEM 迭代越多会丢掉近半已解问题而模型自身毫无察觉，round-trip check 以 0.2% 到 3.1% 的额外规划时间把 Wall 成功率从 0.39 提到 0.76。**</p>

<!-- direction: embodied_ai -->

+ **ActMem: From Latent Memory Reasoning to Grounded Robotic Action**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25461)
![architecture](https://img.shields.io/badge/ActMem_Memory_CoT-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/LigphiDonk/ActMem)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把记忆推理与感知接地解耦：用带时间戳的历史推断子任务并保留潜空间记忆思维链去条件化 flow-matching 动作专家，RoboMemArena 任务成功率 71.1%、真机三类记忆任务平均 68.8%。**</p>

+ **A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25656)
![architecture](https://img.shields.io/badge/A2_VLA_Affordance_Agent-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让智能体把工具可供性当作可构建、检验、修正的假设，在重建的仿真场景中自主找出功能区域及关键几何属性并沉淀技能库，再条件化 π0.5：跨工具重定向 86.1%、真机高出 30.7 个百分点。**</p>

+ **One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26161)
![architecture](https://img.shields.io/badge/OVOA_VLA_Cross_Graph-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让每个相机视角都预测自己坐标系下的动作，并用基座专家与视角专家的两个互补有向注意力图加跨图一致性训练同一目标：LIBERO-Plus 全视角 88.1%、真机空间偏移下从 π0.5 的 28.3% 提升到 58.3%。**</p>

+ **EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26196)
![architecture](https://img.shields.io/badge/EmbodyAgent_Post_Training-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给出开源 VLM 变闭环机器人代理的完整后训练栈：黑盒教师合成数据、SFT 蒸馏、在线 RL 三段共用一个 Python 执行工具，LIBERO Spatial 留出成功率由 0/100 提升到 84/100。**</p>

+ **TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26405)
![architecture](https://img.shields.io/badge/TacInno_Tokenizer-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/ShanghaiTech_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tacinno.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出触觉变化大多可由视觉与动作推出、导致模型忽略触觉，TacInno 只把视觉与动作解释不了的接触动力学压成 16 位离散码作为训练目标：仿真 87.5%、真机 70.5%，部署不增模块。**</p>

+ **One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26617)
![architecture](https://img.shields.io/badge/O2LaF_Two_Dynamics-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Show_Lab_National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://showlab.github.io/o2laf)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用同一个预训练视频 DiT 同时初始化逆向与前向动力学，靠紧凑瓶颈端到端学出可迁移潜动作：GR-1 上 EEF R² 达 0.277（DreamDojo 为 0.149），跨上下文导航平移 NRMSE 降到 1.289。**</p>

+ **FlowScope: 3D Scene Flow Pretraining Improves Surgical Robot Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26865)
![architecture](https://img.shields.io/badge/FlowScope_Scene_Flow_Pretrain-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Vanderbilt_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用立体深度与光流构造场景流伪标签来预训练手术策略主干，预训练后丢弃流头使部署仍是标准 ACT：1,149 例手术、135 万片段，真机取针成功率由 54% 升至 90%、换手再抓针由 4% 升至 52%。**</p>

+ **BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27047)
![architecture](https://img.shields.io/badge/BeyondEgo_Dual_View_Foresight-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用同步外部视角的冻结 DINOv3 特征扩展人形 VLA 的空间感知，并用双视角 0.6 秒前瞻做特权监督训练 4.2M 参数残差适配器：HELM 同分布成功率 48.0% 升到 92.0%、留出场景 23.5% 升到 65.0%。**</p>

+ **ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization in Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27305)
![architecture](https://img.shields.io/badge/ManipScope_Diagnostic_Benchmark-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/USTC-AIR-Lab/ManiScope)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出操作成功并不等于遵循指令：基于 RoboTwin 2.0 构造 48 个留出场景、6 个任务族，12 个策略检查点在 13200 个回合中 84.6% 的失败是抓错目标，目标重指派后跟随指令的比例仅 3.9%。**</p>

+ **GenPA: Image Generators as Efficient Robot Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27446)
![architecture](https://img.shields.io/badge/GenPA_Action_Adapter-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://deng-zian.github.io/GenPA-website/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**主张图像生成预训练的能力不必经由预测未来画面兑现：GenPA 在 FLUX.2 klein Base 4B 上加 19M 参数动作回归适配器并复用生成目标做感知协同训练，LIBERO 99.10%、每动作块 20.9 毫秒。**</p>

