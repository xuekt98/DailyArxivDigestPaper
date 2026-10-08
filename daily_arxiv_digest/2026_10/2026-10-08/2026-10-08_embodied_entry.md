+ **Juno: Taming Predictive Latents for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09940)
![architecture](https://img.shields.io/badge/Tamed_Predictive_Latents-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/2Eastern_Institute_of_Technology,_Ningbo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**联合嵌入预测架构（JEPA）在表示空间预测被遮蔽或未来的观测，为 VLA 模型提供天然的预测 latent 来源。但要让这些 latent 在预训练、策略学习与部署三个阶段都有用，必须解决三类失效：与具体本体的控制不匹配、干扰动作学习，以及……**</p>

+ **RoboJEPA: Scaling Robotic Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10515)
![architecture](https://img.shields.io/badge/RoboJEPA-red)
![task](https://img.shields.io/badge/Robotic_Latent_World_Model-magenta)
![organization](https://img.shields.io/badge/1FAIR_at_Meta,_2Chandar_Research_Lab,_3Mila_-_Quebec_AI_Institute,_4Polytechnique_Montréal-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**潜世界模型在预测未来状态与真实世界规划上表现突出，但实践中缺乏一个原则性的方式来估计其能力如何随模型规模、数据与算力扩展——这是拖慢领域进展的开放问题。RoboJEPA 基于 JEPA 训练并研究这种扩展。**</p>

+ **Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09309)
![architecture](https://img.shields.io/badge/Entity_Level_Goal_Readout-red)
![task](https://img.shields.io/badge/Robot_Manipulation-magenta)
![organization](https://img.shields.io/badge/∗National_Yang_Ming_Chiao_Tung_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**生成式世界模型能丰富地预测操作场景如何朝任务目标演化，但这些未来并不直接暴露控制所需的紧凑任务变量。当训练只监督未来预测时，即使几何恢复可得，终极目标精度也不是显式的学习目标。**</p>

+ **ΔWAM: Distilling Action Tangent Fields into World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09734)
![architecture](https://img.shields.io/badge/Action_Tangent_Field_Distillation-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/1Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**世界动作模型（WAM）用稠密未来预测补足稀疏动作监督来改进机器人策略，但可预测的未来中有很大一部分被外观与场景持续性主导，而非动作依赖的动力学。作者观察到光流、运动中心表示、latent action 等若干近期 WAM 设计都可从同一视角理解。**</p>

+ **RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09254)
![architecture](https://img.shields.io/badge/Robot_Oriented_Video_Generation-red)
![task](https://img.shields.io/badge/Visual_Sim_To_Real-magenta)
![organization](https://img.shields.io/badge/1Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**仿真能大规模低成本生成机器人数据，但仿真训练的策略常因视觉 sim-to-real 差距而迁移失败。既有方法常依赖中间表示，这可能丢弃丰富语义信息或在部署时需要额外感知模块。RoboRender 直接处理视觉 sim-to-real 鸿沟。**</p>

+ **Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10479)
![architecture](https://img.shields.io/badge/Agentic_Real_To_Sim_To_Real-red)
![task](https://img.shields.io/badge/Scene_Reconstruction_and_Policy_Development-magenta)
![organization](https://img.shields.io/badge/1Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真实机器人工作空间的仿真必须保留任务相关的交互，而其中开发的策略必须作用于真实机器人可获得的观测。然而场景重建与策略开发通常被分开处理。Agentic RSR 通过场景重建、策略开发与真机执行三者串联来链接它们。**</p>

+ **Sparse Planning in Visual World Models via Cost Gradients**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10274)
![architecture](https://img.shields.io/badge/Cost_Gradient_Token_Selection-red)
![task](https://img.shields.io/badge/Visual_World_Model_Planning-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于 token 的世界模型支持细粒度潜空间规划，但反复处理大块空间 token 网格使动作搜索昂贵。COSTGRAD 是一个免训练、目标条件化的选择器，用规划代价对每个输入 token 的梯度范数给空间 token 排序。**</p>

+ **Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09496)
![architecture](https://img.shields.io/badge/Sparse_Feature_Policy_Unlearning-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/of_Computer_Science_Engineering,_Chung-Ang_University,_Seoul,_06974,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA 模型借助预训练视觉语言模型的丰富表征在操作任务上泛化良好，但部署到真实环境仍受反复出现的不可靠行为限制。作者研究状态幻觉——一种复发性的失效模式：VLA 继续表现得仿佛一个未实现的机器人状态已经存在。**</p>

+ **Factorized Tactile Representation and Control for Sim-to-Real Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10510)
![architecture](https://img.shields.io/badge/Factorized_Tactile_Representation-red)
![task](https://img.shields.io/badge/Sim_To_Real_Manipulation-magenta)
![organization](https://img.shields.io/badge/1_Amazon_Fulfillment_Technologies_&_Robotics,_Westborough,_MA,_USA.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**触觉 sim-to-real 学习必须弥合仿真接触与设备特定传感器响应之间的差距，同时保留控制所需的信息。作者提出因子化的触觉表征与控制框架，把法向力与接触面映射到一个可从传感器读数恢复的有效接触响应。**</p>

+ **OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10384)
![architecture](https://img.shields.io/badge/Unified_Sim_And_Real_Benchmark-red)
![task](https://img.shields.io/badge/Visu_Tactile_Policy-magenta)
![organization](https://img.shields.io/badge/1Fudan_University,_2Shanghai_Key_Laboratory_of_Multimodal_Embodied_AI,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**触觉反馈为具身智能体提供视觉之外的物理信息，使与真实世界的交互更可靠。尽管视觉-触觉-语言-动作（VTLA）策略进展迅速，跨仿真与真实世界评估触觉操作仍缺乏统一基准。**</p>

