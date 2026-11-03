# 2026-11-03 - 生成式内容模型的 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02366)
![architecture](https://img.shields.io/badge/Quantile_Utility_Policy_Optimization-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/ByteDance_Seed-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/austin-k-wang/QUPO)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统诊断视觉 RL 后训练在 Best-of-N 推理期扩展下的收益转移失效：GenEval2 上后训练模型优势随采样预算增大反被基座反超，上尾奖励分位甚至为负。提出 QUPO，把标量 advantage 换成可控分位数效用混合，Best-of-1 达 0.2287 且 Best-of-128 仍高于基座。**</p>
+ **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02803)
![architecture](https://img.shields.io/badge/Modality_Wise_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把专用音频与视频 RL 教师的能力蒸馏进单个学生模型，用非对称噪声调度、分组多噪声采样和时间步重要性加权解决音视频 token 失衡导致的稀疏音频监督。JavisBench 上 VQ 3.347、AQ 5.449，三项消融各自贡献可测。**</p>
+ **Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03017)
![architecture](https://img.shields.io/badge/Efficient_Adversarial_Score_Distillation-red)
![task](https://img.shields.io/badge/Adversarial_Diffusion_Training-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/pf0607/EASD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示 Score 蒸馏与对抗蒸馏在噪声区间上互补而非重叠，用 regime-adaptive 采样把两者分配到各自生效区间。SiT-XL/2+REPA 上 ImageNet 256×256 一步生成 FID 1.39，64×64 上 100K 步达 1.46，收敛快于 DMD2 一倍。**</p>
+ **Latent Diffusion-GAN: Adversarial Learning in the Autoencoded Latent Space**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02625)
![architecture](https://img.shields.io/badge/VAE_Energy_Discriminator-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Sookmyung_Womens_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 latent diffusion 自带的 VAE 编解码器改造成能量判别器，不新增判别器参数就把对抗训练并入原有扩散管线，并用结构一致性能量稳住潜空间结构。SD-2.1 上 FID 13.79→9.42、CLIP 0.3098→0.3428，SD-3.5-M 上 7.983→6.732。**</p>
+ **Utility-Aware Generative Recommendation: Utility-Enriched Semantic Codes and Utility-Guided Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02981)
![architecture](https://img.shields.io/badge/Utility_Enriched_SID_With_Guided_Decoding-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Kuaishou_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从语义 ID 构造与自回归解码两端对齐下游多目标效用：末层编码塞入离散效用位，beam 打分融合多后验行为效用估计，不改动主干训练。已在快手全量部署，线上视频观看时长 +0.206%、播放量 +0.164%，离线 NDCG@3 相对最强基线提升 16.52%。**</p>
+ **Balancing Representations by Identifying and Generating Under-represented Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02952)
![architecture](https://img.shields.io/badge/Label_Free_Repair_Loop-red)
![task](https://img.shields.io/badge/Generative_Data_Augmentation-magenta)
![organization](https://img.shields.io/badge/Humboldt-Universitat_zu_Berlin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**无标签的表示平衡反馈环：编码器用平均 kNN 距离定位稀疏样本，在可忠实变化的分数带里用冻结图生图扩散模型补局部变体后重做预训练。五种源上 linear-probe 平均提升 2.4–10.6 分，修复效果达到补真实 withheld 图像 oracle 的水平。**</p>
+ **Probing Local Conditional Fit for Diffusion Model Membership Inference**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02578)
![architecture](https://img.shields.io/badge/Local_Conditional_Fit_Score-red)
![task](https://img.shields.io/badge/Diffusion_Privacy_Audit-magenta)
![organization](https://img.shields.io/badge/Sony_Group_Corporation-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 LoFIT 成员推断分数：在固定噪声输入上测量条件预测偏移引发的一阶去噪损失响应，只用前向查询、不需要目标模型梯度。微调 SD v1.4 上 AUROC 达 0.935/0.954/0.896，优于 CLiD 与 PFAMI，能在微调早期识别成员。**</p>
+ **Unlocking the Potential of Contrastive Regularization for Diffusion Transformer Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02921)
![architecture](https://img.shields.io/badge/Clean_Anchored_Contrastive_Regularizer-red)
![task](https://img.shields.io/badge/Contrastive_Diffusion_Training-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断出 InfoNCE 在扩散训练中失效的原因：输入噪声的近正交分量提供了撑开负样本距离的捷径，反而削弱正样本对齐。CRAN 用干净样本表示距离锚定对比分散，SiT-B/2 的 FID-50K 从 33.0 降到 26.3，追平依赖外部 DINO 特征的 REPA。**</p>
+ **LAND: Learning an Adaptive Number of Draws for Bayesian Best-of-N Selection**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03388)
![architecture](https://img.shields.io/badge/Adaptive_Draw_Allocation-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Aleph_Alpha_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 Best-of-N 的固定预算改成按期望边际收益动态分配：学出源条件的分数分布混合，用后验边际改进对比全局算力价格决定是否继续采样。机器翻译上同等平均算力下 MetricX 优于固定 Bo-N，同等质量下少生成约 20-40% 候选。**</p>
+ **GEAR: Generative Editing for Scene-Conditioned Outfit Retrieval for VR Travel**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02363)
![architecture](https://img.shields.io/badge/Generative_Editing_For_Retrieval-red)
![task](https://img.shields.io/badge/Generative_Editing_For_Retrieval-magenta)
![organization](https://img.shields.io/badge/University_of_Science_Ho_Chi_Minh_City-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 VR 场景条件化服装检索，用 VLM 描述服装、指令引导扩散模型渲染到参考角色、裁剪服装区检索的三段式管线合成中间视觉查询，绕开 3D 环境视图与商品图的跨域差距。受控数据集 top-1 平均 Elo@5 1012.75，20 场景用户研究视觉与适配偏好均居首。**</p>
