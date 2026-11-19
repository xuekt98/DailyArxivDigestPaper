<!-- direction: world_model -->

+ **Distilling World Action Models for Efficient Bimanual Manipulation via Anchored Path Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22592)
![architecture](https://img.shields.io/badge/Anchored_Path_Matching-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Astribot-green)
[![project](https://img.shields.io/badge/project-blue)](https://jialonglong.github.io/Anchored-Path-Matching/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**APM 用锚点路径匹配把世界动作模型蒸馏成单个 checkpoint，同时支持 1、2、4 步生成：RoboTwin 2.0 上一步平均成功率 80.9%、比同预算续训基线高 1.7 个点，视频 PSNR 从 30.169 升到 32.317 dB，真机控制周期从 4323.6 ms 降到 203.1 ms。**</p>

+ **SpikWM: Efficient End-to-End Spiking World Modeling for Visual Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22981)
![architecture](https://img.shields.io/badge/Spiking_Latent_World_Model-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ShawnYE618/SpikWM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SpikWM 是端到端脉冲化的 JEPA 世界模型，每张图一次仿真步即可完成目标条件规划：Push-T / Two-Room / Reacher / OGBench-Cube 成功率 88.67% / 97.33% / 99.33% / 86.67%，同规划预算下估计算术能耗比 LeWM 低 75.6%，部署参数 16.81M。**</p>

+ **Risk-Triggered Search: Behavior-Preserving Safe Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24409)
![architecture](https://img.shields.io/badge/Risk_Triggered_Search-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RTS 在冻结的 JEPA 世界模型上用预测潜前缀估计过程风险，把同一判据同时用作搜索触发门与可行性门：五个任务的安全到达率比 Direct 基线高 12.67–41.67 个点，1,968 条配对轨迹的动作与逐步搜索完全一致，却省下 17.71%–70.41% 控制时间。**</p>

+ **Counterfactual World Models: JEPAs That Reason About "What If"**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24778)
![architecture](https://img.shields.io/badge/Counterfactual_World_Model-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Brown_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/galilai-group/counterfactual-WM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文证明只靠事实转移训练的世界模型无法识别个体反事实，并给出零反事实数据、零额外参数、零重训的残差复用解法：四个模拟器上反事实 R² 从 38–46% 提到 86–96%，后见规划找到可达目标动作的比例 35–69%，高于不知结果的 oracle 规划器。**</p>

+ **Phoenix: Learning Scene Structure Representations for Generalizable World-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24938)
![architecture](https://img.shields.io/badge/Phoenix_Scene_Structure_WAM-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Phoenix 用双教师蒸馏 DINOv3 学场景结构表示，再用 CS-VAE 压缩成生成潜变量驱动世界动作模型：39306 小时数据下 LIBERO-Plus 94.8%、RoboTwin 2.0 C2R 72.4%，预训练数据从 25% 增到 100% 涨 27.0 点。**</p>

+ **Perception into Imagination: Executable Memory for World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22294)
![architecture](https://img.shields.io/badge/Executable_Perceptual_Memory-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EPM 让显式感知状态在想象过程中与神经潜动力学同步演化，并把读出接到奖励、价值与策略三个环节：Memory Maze 13×13 达 30.37 回报，比只接策略与价值高 7.00、比仅观测访问高 16.19，记住目标的奖励预期从 0.154 升到 0.587。**</p>

+ **CaFe: Causally Faithful Conditional Traffic Scenario Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22855)
![architecture](https://img.shields.io/badge/CaFe_Causal_Faithful_Traffic_Simulator-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/CARIAD_SE-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CaFe 用双流扩散强制模拟器把「意图泄漏」变成可测量指标：固定被指令车辆的执行动作、只改私有指令时，现有条件设计让 23–83% 的邻近车辆提前反应，CaFe 降到 0.0%，同时 WOSAC 真实度保持 0.763、碰撞率从 5.82% 降到 4.81%。**</p>

<!-- direction: embodied_ai -->

+ **Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22713)
![architecture](https://img.shields.io/badge/Body_Schema_Policy-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://www.lechen-zhang.com/BSP/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BSP 把关节与连杆 token 放到机器人运动学树上，用螺旋运动在连杆间传递特征，每个身体部位只取自己那部分视觉证据再条件化动作去噪：35.0M 参数在九个 Unitree G1 全身任务上总分 221，与 2.63B 的 Ψ0 打平，每个动作块只要 13.9 ms。**</p>

+ **Homeward: No Place Like the Training View**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24455)
![architecture](https://img.shields.io/badge/Homeward-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Homeward 是训练无关的观测适配器：把未知的相机参数与静态场景深度交给冻结 VGGT，把已知的机器人几何交给正运动学渲染再合成回训练视角，使四个冻结 VLA 在 1,599 个 LIBERO-Plus 相机变体上的成功率从 62.5%/76.5%/68.0%/3.6% 升到 77.6%/95.1%/91.2%/26.4%。**</p>

+ **ALOHA Lightning: Learning Fast and Precise Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21919)
![architecture](https://img.shields.io/badge/ALOHA_Lightning-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://flash-aloha.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ALOHA Lightning 用动觉示教在可反驱双臂平台上采集近人手速演示，再用测试时动作平滑与按执行器位置实时更新的掩码对齐训练与部署的视觉分布：每任务 50 条演示下叠杯 3.97 秒、抛接 1.85 秒，成功率超 80%，整体耗时比遥操作基线低 50% 以上。**</p>

+ **Making Future-Predictive Representations Actionable**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22994)
![architecture](https://img.shields.io/badge/RelayWAM-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Xinjiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RelayWAM 在视频骨干与动作骨干之间插入显式 transition 空间，把深层才出现的未来预测线索按当前动作步与流时间转成动作可读表示：LIBERO-Plus 成功率从 51.50% 提到 72.03%、标准 LIBERO 均值 98.2%，额外参数仅 34.96M、不到 6.02B 主干的 0.6%。**</p>

+ **TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23143)
![architecture](https://img.shields.io/badge/TCP4D-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://livioni.github.io/TCP4D/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TCP4D 用同一份 4D 场景表示既跟踪单目视频中的 TCP 位姿与夹爪状态，又生成未来 TCP 轨迹：DROID 与 RoboLab 的绝对轨迹误差 7.60 与 16.07 mm、跟踪成功率 100%，生成器在 RoboTwin 上 69.19% 均值成功率，跨本体增广数据联合训练再提升 41.5%。**</p>

+ **BiCAT: Bimanual Coordination Action Tokenization**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23499)
![architecture](https://img.shields.io/badge/BiCAT-red)
![task](https://img.shields.io/badge/Action_Chunking-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://magiclab-nus.github.io/BiCAT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BiCAT 用共享运动表示加对称跨臂注意力与联合解码，把双臂动作块编成两路互相可参考的离散 token：RoboTwin 2.0 十个任务平均成功率 69.3%、比八个基线里最强的 NAC 高 17.6 点，耦合越紧增益越大（紧耦合 +21.3），每动作块仅 40.5 ms。**</p>

+ **SPICE: Stochastic Policy for Interaction in Cluttered Environments**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23585)
![architecture](https://img.shields.io/badge/SPICE-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPICE 是首个以触觉为唯一环境反馈的扩散策略，用空间 taxel 编码加显式接触信号在视觉遮挡的植物冠层中伸臂取目标：绕枝 19/20（95%）对最强触觉基线的 8/20（40%），图像条件 DP 为 0/20，换到未见植株 40 次零样本成功 87.5%。**</p>

+ **RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23855)
![architecture](https://img.shields.io/badge/RoboBuilder-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://ghadinehme.com/robobuilder.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboBuilder 让编码智能体从标准零件、电机与一个自制 3D 打印件出发协同设计机器人硬件与程序，通过仿真的设计全部被真的造出来跑过：16,427 次仿真、12,774 个机器人、135 台真机下仿真通过率只有 66%，看到真实失败视频后智能体消掉了 72% 的一二级失败。**</p>

+ **GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23926)
![architecture](https://img.shields.io/badge/GTI-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GTI 用当前观测与执行历史定位活跃子任务及其阶段，为同一子任务生成相位条件的 K1 接触态与 K2 完成态两类视觉目标共同条件化 VLA：RoboCasa365 复合任务 14.6% 升到 31.8%，VLA-Arena 总体 47.6%，真机全任务从 21.7% 升到 59.2%。**</p>

+ **3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23961)
![architecture](https://img.shields.io/badge/3DTouch-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**3DTouch 把 RGB-D 场景点与五指密集触觉统一表达在机器人基座坐标系里，并用手-物、物-物的相对位移与距离 token 显式描述几何关系：UR7e 加 XHand 上五个接触密集真机任务平均成功率 65.0%，比对应 VLA 基线高 42 点、比最强触觉 VLA 高 20 点。**</p>

+ **WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24011)
![architecture](https://img.shields.io/badge/WAM_Policy-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Australian_Centre_for_Robotics_University_of_Sydney-green)
[![project](https://img.shields.io/badge/project-blue)](https://aigeeksgroup.github.io/WAM-Policy/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WAM-Policy 把为手臂预训练的世界动作模型改造成无臂四足腿-臂操作策略：先只替换视觉与动作接口（30 维双臂指令换成 9 维）保住通用性，再用在线自蒸馏把采样压到 1/2 NFE、生成时间从 2.226 秒降到 0.159 秒而成功率只由 77.0% 掉到 76.7%，最终经 RL 与多教师合并升到 85.0%。**</p>

+ **AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24077)
![architecture](https://img.shields.io/badge/AeroRSI-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University_SIGS-green)
[![project](https://img.shields.io/badge/project-blue)](https://starsholic.github.io/AeroRSI/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AeroRSI 让失败的航拍导航策略靠继续飞行来自行验证修复：自适应失败锚定、续飞验证与保留式蒸馏构成三轮递归自改进，TravelUAV 上 2B 策略成功率从 46.4% 升到 67.5%、碰撞率减半、比同初始化的前 SOTA 高 10.6 点，且无需人工标注与额外推理开销。**</p>

+ **Ego2X: Contact-aware Transfer from Egocentric Human Data to Any Robot**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24138)
![architecture](https://img.shields.io/badge/Ego2X-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/BUPT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ego2X 以物体坐标系中的接触为核心，用 CORE 记录每次接触的表面锚点、外法线、相对力、握持模式与交互状态，把单目第一人称视频转成机器人数据：EgoDex 上 62.9% 的标注接触对官方 HuRo 的 27.9%，X-VLA 后训即把 RoboTwin 2.0 成功率从 40.5% 升到 67.0%。**</p>

