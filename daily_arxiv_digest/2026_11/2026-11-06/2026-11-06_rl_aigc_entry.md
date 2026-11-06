# 2026-11-06 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07301)
![architecture](https://img.shields.io/badge/Artifact_As_Rubric_RM-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视频生成的伪影本身当作可核验的评分标准，先列出结构化伪影清单再打分，让奖励可解释也便于优化；该视频奖励模型在三个域外基准上成对偏好准确率领先，并能反过来优化 Wan2.1 扩散模型与闭源 Veo-3.1。**</p>
+ **Generator-Aligned Reward Modeling with Target-Aware Bounded Optimization for Visual Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07648)
![architecture](https://img.shields.io/badge/Generator_Aligned_Reward_Model-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Institute_of_Artificial_Intelligence_China_Telecom_TeleAI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对奖励引导的视觉生成后训练，提出生成器对齐的奖励建模与目标感知的有界优化两件套，再改造出目标感知 GRPO，让目标属性增强的同时保住通用生成质量，并抑制中性提示词上的属性泄漏。**</p>
+ **FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08240)
![architecture](https://img.shields.io/badge/FewStep_RL_Adaptation-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把已有的扩散强化学习目标系统性地改造成少步模型可用版本：先统一到 x 空间，再把梯度拆成自回归项与奖励增强项，最后在少步模型上重算锚点与权重，一套代码覆盖五种主流目标并给出可比的横向结论。**</p>
+ **PBPO: Prefix-Block Policy Optimization for Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07783)
![architecture](https://img.shields.io/badge/Prefix_Block_Policy_Optimization-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Meta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对扩散语言模型的块级解码，构造出可解析的单步块似然代理并对块内每个 token 单独加权与裁剪，避免块乘积权重放大梯度方差，在两个 LLaDA 初始化、六个基准与三种生成长度上取得稳定的竞争性表现。**</p>
+ **Expanding the Quality-Coverage Frontier with Competitive Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07055)
![architecture](https://img.shields.io/badge/Competitive_Flow_Matching-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Cornell_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://lilydaytoy.github.io/CFM/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出流匹配回归只能输出一个平均速度、由此产生质量与覆盖率的取舍，转而在训练中让多个带随机条件码的候选速度竞争、只对最优匹配者施加损失，从而把质量—覆盖率前沿整体推向高覆盖高质区。**</p>
+ **Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07566)
![architecture](https://img.shields.io/badge/Interval_Integrated_CFG-red)
![task](https://img.shields.io/badge/Classifier_Guidance-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/YMlinfeng/AGAVE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对一步 MeanFlow 生成器只能用一个标量做分类器自由引导的问题，证明任意引导场都可被吸收进区间积分目标并编译成一次前向，据此提出只加十个标量的 AGAVE，在 VBench、UCF-101 与 MSR-VTT 上追平多步引导质量。**</p>
+ **FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07604)
![architecture](https://img.shields.io/badge/Closed_Form_Fisher_Critic-red)
![task](https://img.shields.io/badge/Few_Step_Distillation-magenta)
![organization](https://img.shields.io/badge/University_at_Buffalo_SUNY-green)
[![project](https://img.shields.io/badge/project-blue)](https://bhosalems.github.io/FisherDistill/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用闭式 Fisher 线性判别方向替代学出来的对抗判别器来精修少步扩散生成器：从冻结教师特征估计真实与生成样本的统计量，直接给出最大分离二者的方向，在 DMD2 与 SiD 上稳定降低 FID 并同时改善精确率或召回率。**</p>
+ **Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08249)
![architecture](https://img.shields.io/badge/Focused_Docking_Supervision-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/University_of_Central_Florida-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在分子对接扩散模型上做固定预算对照，比较宽覆盖续训与聚焦到扭转结构后果的监督：五个 epoch 内聚焦监督并无一致优势，说明几何后果更严重的修正并不自动带来更好的最终对接成功率。**</p>
+ **A Proxy-Based Method for Measuring Racial Disparities in~Text-to-Image~Generators**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07132)
![architecture](https://img.shields.io/badge/Proxy_Based_Bias_Audit-red)
![task](https://img.shields.io/badge/T2I_Evaluation-magenta)
![organization](https://img.shields.io/badge/University_of_Virginia-green)
[![project](https://img.shields.io/badge/project-blue)](https://proxyaudit.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把美国反歧视法中的种族代理变量转化为文生图生成器的自动化偏差审计流程：逐图分类种族后与人口普查数据用总变差距离比对，再用 CIELAB 肤色与嵌入余弦相似度补充人口统计数字看不见的质量差异。**</p>
+ **OptIMerge: Optimization-Based Merging of Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07543)
![architecture](https://img.shields.io/badge/Architecture_Aware_Merge_Coefficients-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Google-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对图像到图像扩散专家在卷积核里编码了冲突空间先验、朴素权重汤必然出伪影的问题，用按层设计的低秩与 Cayley 参数化在百余张图上学合并系数，以不到 0.4% 的可训练参数逼近联合多任务训练的效果。**</p>
