# 2026-11-06 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07881)
![architecture](https://img.shields.io/badge/TactileLab-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://yijionglin.github.io/tactilelab/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TactileLab 基于 IsaacLab 用刚体仿真而非软体物理估计接触界面的稠密切向运动，提出 simulated tactile flow 与接触深度场互补，配合 PETS-Net 策略架构完成从仿真到真机的迁移，并已在双臂物体跟随与灵巧手内操作上落地。**</p>
+ **La-JEPA: Compact Robot Policies with Latent World Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08156)
![architecture](https://img.shields.io/badge/La_JEPA-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Huawei_Technologies-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mt-clemente/lajepa)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**La-JEPA 把机器人策略 Transformer 直接从零训练在预训练 V-JEPA 2.1 的特征空间里，训练时联合预测未来特征与动作、推理时只生成动作，部署参数量约为次优策略的四分之一，速度最高可达 Fast-WAM 的 5 倍。**</p>
+ **Motion-guided Contrastive Regularization For Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06901)
![architecture](https://img.shields.io/badge/Motion_Guided_Contrastive-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Northeastern_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文指出 JEPA 式潜世界模型存在静态塌缩：编码器保留与回合绑定的静态内容却压掉操作相关的状态变化；所提运动引导对比正则把 OGBench-Cube 随机背景下的规划成功率从 52% 提升到 78%，LIBERO-Object 从 14% 提升到 54%。**</p>
+ **From Pixels to Actions - Towards Native Vision-Language-Action Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06918)
![architecture](https://img.shields.io/badge/NEO_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/S-Lab_Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://www.lmms-lab.com/posts/neo_vla/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NEO-VLA 是结构上无视觉编码器的 VLA 框架，图像由轻量 patch 卷积 token 化后与语言在骨干中共同演化，流匹配动作专家可读取不同深度的视觉表示；只训动作专家时 LIBERO 平均成功率 90.9%，LIBERO-Plus 总分 89.7。**</p>
+ **Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07513)
![architecture](https://img.shields.io/badge/Concertina-red)
![task](https://img.shields.io/badge/Policy_Diffusion-magenta)
![organization](https://img.shields.io/badge/University_of_Sydney-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lose4578/Concertina)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Concertina 把连续轨迹表示、分块生成与物理坐标监督直接放进共享的扩散 VLM 骨干，每个控制步编码成隐空间里的一个连续动作 token，动作投影仅占 4.46B 模型的 0.21%，LIBERO 常规集平均成功率 98.15%。**</p>
+ **AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07712)
![architecture](https://img.shields.io/badge/AffectiveVLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Skolkovo_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AffectiveVLA 在 Unitree G1 人形机器人上部署意图门控的 VLA 流水线，用两路 RGB 相机识别交互意图并转成语言提示，低置信度预测直接抑制动作执行；接入意图模块后 GR00T 的宏 F1 从 0.75 提升到 0.90。**</p>
+ **Learning Robotic World Models with Semantic and Visual Feedback**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07850)
![architecture](https://img.shields.io/badge/RoboImagine-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/The_City_College_of_New_York-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Alexander-wu/RoboImagine)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboImagine 把自回归机器人世界模型的后训练改成候选未来比较：冻结的多模态评价器按两种顺序做成对视频比较给出语义偏好，再叠加像素与感知级一致性反馈，以组相对优势驱动优化，RT-1 上 PSNR 提升 1.26 dB、LPIPS 降低 11.93%。**</p>
+ **MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08372)
![architecture](https://img.shields.io/badge/MOMASPLAT-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Texas_at_Austin-green)
[![project](https://img.shields.io/badge/project-blue)](https://robin-lab.cs.utexas.edu/momasplat)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MOMASPLAT 面向移动操作的新视角演示增强，把静态场景与被操作物体分开重建再渲染出合成轨迹，并用运动学重定向生成配对动作；在 30 厘米底盘偏移处仍有 33% 成功率、40 厘米处 50%，而所有基线在同处已归零。**</p>
+ **LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07515)
![architecture](https://img.shields.io/badge/LMGN-red)
![task](https://img.shields.io/badge/Loco_Manipulation-magenta)
![organization](https://img.shields.io/badge/Hubei_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LMGN 把腿式机器人的最后一公里抓取导航作为统一建模问题，用 ED-DR 表示显式刻画可抓取的底盘位姿与接近方向，配合分阶段的层次化混合专家策略，Habitat 上注视成功率 73.9%、抓取成功率 74.8%，相对 VBC 分别提高 4.9 与 22 个百分点。**</p>
+ **GPWM: Modeling the World as 3D Particle Motion**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08338)
![architecture](https://img.shields.io/badge/GPWM-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://robertren1122.github.io/gpwm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GPWM 直接在三维物理空间里生成粒子与刚体运动，用流匹配与 diffusion forcing 组合出对象感知的多分辨率 Transformer，一套架构与一套权重覆盖刚体、变形体、布料与颗粒介质，在 2550 万帧语料上六个物理域平均预测误差降低 31%。**</p>
