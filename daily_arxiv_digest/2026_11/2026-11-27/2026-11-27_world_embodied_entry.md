<!-- direction: world_model -->

+ **A Mesh to Remember: Persistent Appearance for Interactive Video Worlds**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32445)
![architecture](https://img.shields.io/badge/Mesh_Surface_Memory_Renderer-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research.nvidia.com/labs/sil/projects/m2r/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把网格当成渲染器的地址：M2R 把生成的特征写回物体自身坐标系下的表面，物体移动或重新入镜时外观随之重现，记忆随已见表面而非帧数增长，720p 实时渲染达 40 FPS。**</p>

+ **CodeWAM: A Code World Action Model for End-to-End Autonomous Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32483)
![architecture](https://img.shields.io/badge/Executable_Code_Ego_Dynamics-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CodeWAM 把可执行代码引入驾驶世界模型表示自车动力学：代码执行给出候选计划下的精确运动序列，再与既有计划和历史运动比对，NAVSIM v1 navtest 达 93.6 PDMS，NAVHARD 达 50.6 EPDMS。**</p>

+ **Simulator-as-Proxy World Model for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32786)
![architecture](https://img.shields.io/badge/Simulator_As_Proxy_World_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://sim-pwm.pages.dev)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SimPWM 用无训练参数的规则模拟器代理机器人与物体的显式状态，视频模型只负责渲染；冻结代理物体可检验基座模型是否真的遵守模拟状态，漏抓率从 54% 降到 38%。**</p>

+ **SplatWAM: Splatting World Action Models for Real-Time 3D Imagination**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33467)
![architecture](https://img.shields.io/badge/Gaussian_Token_Dynamics_Model-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/CVSSP_University_of_Surrey-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SplatWAM 直接在紧凑 3D 高斯图元上学习动作条件动力学，tokenizer 把不定数量无位姿视图压成固定预算的高斯 token，动态模型每个动作一次前向；新视角渲染快 12 倍、约 80 FPS。**</p>

+ **$\mathrm{M}^{2}$-WAM: Efficient Hierarchical Memory Across Modalities and Timescales for World-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33710)
![architecture](https://img.shields.io/badge/Hierarchical_Visual_Interaction_Memory-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**M2-WAM 给世界动作模型配上层次化的视觉与交互记忆：稠密短期窗口加定长联想式长期记忆，门控增量更新迁移被淘汰条目，在线开销与回合长度无关，比 Fast-WAM 高 53.2 与 61.2 个百分点。**</p>

+ **Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33925)
![architecture](https://img.shields.io/badge/Reforge_Failure_Post_Training-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://aim-uofa.github.io/WorldReforge/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WorldReforge 靠 62k 条人为扰动抓取得到的仿真失败轨迹补世界模型的短板，让它学会物体被推、滑、掉落时的物理；在 Cosmos3 Nano 上轨迹误差降 28.2%，未见物体降 35.0%。**</p>

+ **Long-Horizon Planning with Latent World Models via Graph Anchors**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34509)
![architecture](https://img.shields.io/badge/Sparse_Graph_Anchor_Planner-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Robotics_and_Mechatronics_Engineering_University_of_Dhaka-green)
[![project](https://img.shields.io/badge/project-blue)](https://syed-nazmus-sakib.github.io/graph-anchors/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Graph Anchors 指出潜空间目标距离会同时丢掉方向性并压过被操作物体，改为瞄准录制轨迹上沿最短路前移几跳的锚点，免训练即把 400 步外远目标成功率从 13% 提到 85%。**</p>

<!-- direction: embodied_ai -->

+ **HoloBrain-0.5 Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34449)
![architecture](https://img.shields.io/badge/URDF_Standardized_VLA_Policy-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/Horizon_Robotics_HoloBrain_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://horizonrobotics.github.io/robot_lab/holobrain_0_5/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HoloBrain-0.5 先用 URDF 标准化统一关节轴、坐标框架与工具中心点，再在超过 10,000 小时、15 类本体数据上预训练连续与离散两版 VLA，离散版六个闭环仿真设定平均成功率 56.77%，七个真机任务免后训练达 87.76%。**</p>

+ **Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31452)
![architecture](https://img.shields.io/badge/Selective_MFM_VLA_Collaboration-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://tom-zgt.github.io/MFM-VLA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MFM-VLA 让多模态基础模型只做目标定位与空间引导、VLA 保留精细操作控制，并用能力路由避免无谓介入；在 LIBERO-PRO 与 ALOHA-Sim-PRO 上分别带来 14.9 与 74.0 个百分点的成功率提升。**</p>

+ **RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31894)
![architecture](https://img.shields.io/badge/Verified_World_Skill_Transfer-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RESET 用一段真实演示同时确定场景几何、终止判据与参考轨迹，重建可交互世界后让编码智能体自举技能代码，再零 LLM 调用部署到真机；8 个任务上未见布局平均成功率 97%，真机 280 次试验成功 80%。**</p>

+ **VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32245)
![architecture](https://img.shields.io/badge/Policy_Measured_Skill_Envelope-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Skill Envelope 用策略实测的 3D 扫掠体积作为可组合技能的前置条件，暴露成几何检查与安全放置两个工具，让 VLA 执行、代码修复；碰撞预测 AUROC 0.946，三四步抽屉链成功率从 29.7% 升到 93.8%。**</p>

+ **EgoLoAF: Learning Humanoid Loco-Manipulation from Egocentric Demonstrations with Hand-Object Affordances**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32260)
![architecture](https://img.shields.io/badge/Egocentric_Affordance_Retargeting-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Xian_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://egoloaf.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EgoLoAF 不依赖穿戴式动捕，只用第一视角视频重建躯干与双手轨迹并显式表示手物可供性，通过交叉注意力注入动作专家；发布 128,400 段演示共 1,000 小时，四个真机任务进度分 73.1 对遥操作 74.4。**</p>

+ **Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32353)
![architecture](https://img.shields.io/badge/Embodiment_Grounded_Representation-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://any2act.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Any2Act 把演示统一表达在执行者机器人的相机布局与动作空间里，在 1.2M 条真实轨迹、10K 个任务上学会跟随，再用每个仅几百对的源路由适配器接入人类视频、仿真与 UMI；单条演示未见任务成功率 57.5%。**</p>

+ **ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32476)
![architecture](https://img.shields.io/badge/Contact_Solver_Anchored_Tactile_Sim-red)
![task](https://img.shields.io/badge/Physics_Simulator-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ViTacLab 把锚定 PhysX 接触求解器的三模态触觉原语做成可并行的 GPU 模拟器，并配基准与双流 VQ-VAE 策略；法向与切向力 RMSE 从 2.31 与 1.85 N 降到 0.42 与 0.53 N，256 并行下 2,482.9 FPS。**</p>

+ **GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32510)
![architecture](https://img.shields.io/badge/Gated_Geometry_Grounded_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Xiaomi_Corporation-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GeoVLDrive 用 3D 基础模型的多层特征经门控交叉注意力注入视觉语言骨干，并把未来几何、关键智能体运动与元动作编进结构化潜思维链；NAVSIM v1 达 91.8 PDMS，NAVSIM 3DQA 总体 89.2%。**</p>

+ **DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32665)
![architecture](https://img.shields.io/badge/Execution_Aware_Differentiable_Training-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Department_of_Automation_Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DiffGR00T 用可学习的动作条件世界模型替换不可微模拟器，让多步身体执行损失经冻结的全身控制器与流匹配采样器回传进 VLA 动作头；四个 HumanoidArena 任务平均成功率从 59.2% 升到 71.7%。**</p>

+ **Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32797)
![architecture](https://img.shields.io/badge/Screw_Axis_Attention_Policy-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_University_of_Nottingham-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Screw Attention Policy 把几何显式供给策略、只学执行，仅 30K 个可学习参数；LIBERO 96%、换布局 85.8%、跨五种未见机械臂 80.2%（此前最好 33.0%），真机 24 次试验成功 21 次。**</p>

+ **RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33390)
![architecture](https://img.shields.io/badge/Spatial_Constraint_Puzzle_Benchmark-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Northwestern_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://roboarc.embodied-first-exam.ai)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboARC 用 90 个空间约束谜题检验机器人能否推理出正确动作：最强编码智能体在特权设定解 86%、标准设定只剩 43%，而补充物体位姿与零件几何可让失败显著减少，四个零样本 VLA 全军覆没。**</p>

+ **DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33579)
![architecture](https://img.shields.io/badge/Physics_Corrected_Retargeting_Pipeline-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/POSTECH-green)
[![project](https://img.shields.io/badge/project-blue)](https://wongyun-yu.github.io/dexengine/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexEngine 把人手物演示放到机械臂够得到的位置，再用残差强化学习在物理仿真中修正成可执行的整臂轨迹；九个人类数据集产出 65,000 条轨迹与 325,000 段回放，每片段 3.9 GPU 分钟，比基于 RL 的方法快 10 倍以上。**</p>

+ **FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33635)
![architecture](https://img.shields.io/badge/Hierarchical_Continuous_Latent_Actions-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![project](https://img.shields.io/badge/project-blue)](https://freshvla.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FreshVLA 用高频先验把视觉变化编码推向动态区域，并把隐动作拆成粗粒度任务进展与细粒度执行残差，冻结编码器后做潜动作与机器人动作的联合流匹配；LIBERO 98.2%、LIBERO-Long 98.0%，真机比 π0.5 高 7.5%。**</p>

