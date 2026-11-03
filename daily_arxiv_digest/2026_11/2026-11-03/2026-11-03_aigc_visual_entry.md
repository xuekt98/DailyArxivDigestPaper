# 2026-11-03 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **MoviEdit: Long-form Multi-Shot Video Editing Made Easy**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02737)
![architecture](https://img.shields.io/badge/Cascaded_Bidirectional_Autoregressive_Video_Editor-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Adobe-green)
[![project](https://img.shields.io/badge/project-blue)](https://multi-shot-edit.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MoviEdit 用三条自动流水线合成 87K 条无标注配对编辑视频，训练出级联双向—自回归长视频编辑器：先在时空压缩表示上生成全局编辑草稿，再自回归渲染全分辨率，并发布含 64 段多镜头视频、128 个编辑场景的 MoviEdit-Bench。**</p>
+ **SeMo3D: Unifying 3D Generation, Editing, and Completion via Selective Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02568)
![architecture](https://img.shields.io/badge/Selective_Modeling_Multi_Condition_3D_DiT-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://xiaokunsun.github.io/SeMo3D.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SeMo3D 提出 Selective Modeling 范式，把 3D 生成、编辑、补全统一为只合成选定区域，用 region-selective denoising 无需配对数据联合训练，并以多条件 3D DiT 在 Toys4K 上取得 LPIPS 0.079、FID 4.99、CD 0.0118 的最佳结果。**</p>
+ **TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03394)
![architecture](https://img.shields.io/badge/Progressive_Resolution_Autoregressive_AudioVideo_Generator-red)
![task](https://img.shields.io/badge/Joint_Audio_Video_Generation-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://taoliveaigc.github.io/TaoMate-HD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TaoMate-HD 用渐进分辨率的自回归音视频生成应对流式数字人：每个 chunk 先两步低分辨率去噪定结构、再一步高分辨率精修，配合阶段并行部署，相对直接高分辨率生成提速 1.6 倍再叠加 1.9 倍，并把文本续写带来的字错率降低 11.18 个百分点。**</p>
+ **UniCross3D: Unified Cross-View and Cross-Domain Diffusion for Consistent Single-Image 3D Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02631)
![architecture](https://img.shields.io/badge/Cross_View_Cross_Domain_3D_Diffusion-red)
![task](https://img.shields.io/badge/Single_Image_3D_Generation-magenta)
![organization](https://img.shields.io/badge/Sookmyung_Womens_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UniCross3D 用跨视角潜变量正则与跨域互信息目标，把单图 3D 生成中的视角几何一致性和颜色—法线语义对齐统一到一个扩散框架，在 2D-to-3D 对比中以 PSNR 21.84、CD 0.0125、IoU 0.6125 全面领先 Wonder3D、CRM 等基线。**</p>
+ **VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03043)
![architecture](https://img.shields.io/badge/MoE_Attention_Video_Editing_Backbone-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Tencent-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VideoEditor-MoE 是首个开源视频编辑混合专家框架，用 MoE-Attention 把稀疏专家容量扩进注意力层，从 5B 初始化扩到 14B/56B，Edit Execution 与 Edit Fulfillment 均达 94.70、视频质量 77.27，优于全部 MLP-MoE 与显式专家基线。**</p>
+ **Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02822)
![architecture](https://img.shields.io/badge/Disentangled_Context_Routing_AR_Video_Diffusion-red)
![task](https://img.shields.io/badge/Autoregressive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/Australian_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://disen-forcing.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Disen-Forcing 指出自回归视频扩散中的初始帧并非 LLM 式注意力汇，而是由稀疏的 anchor heads 负责语义锚定，据此提出解耦上下文路由与运动解耦正则，在 30 秒/1 分钟长视频上把 Dynamic Degree 从 35.66 拉到 73.12，同时把漂移从 7.23 降到 4.03。**</p>
+ **When Optimization Meets Human Intent: Human-Centered Diffusion Model Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03140)
![architecture](https://img.shields.io/badge/Human_Centered_Diffusion_Optimization_Framework-red)
![task](https://img.shields.io/badge/Personalized_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇综述不再按算法罗列扩散模型优化，而是提出以人本视角重构该领域的四个维度：意图表示、优化机制、失效模式与权衡、以人为中心的验证，并用三个相互关联的挑战解释为什么自动指标涨分未必等于更贴合用户意图。**</p>
+ **OctreeSplat: Hierarchical Octree-Guided Feed-Forward Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02658)
![architecture](https://img.shields.io/badge/Hierarchical_Octree_Guided_Feed_Forward_3DGS-red)
![task](https://img.shields.io/badge/3D_Gaussian_Splatting_Rendering-magenta)
![organization](https://img.shields.io/badge/East_China_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OctreeSplat 用冻结视觉基础模型的多视角特征与几何先验构建分层八叉树，由预测的致密化分数决定高斯原语的疏密，训练只增加 76M 参数、耗时 35 GPU 小时，在 Replica、TUM、Tanks and Temples、DTU 上用更少原语达到有竞争力的重建质量。**</p>
+ **One Image Is Enough: Self-Generated Supervision for Personalizing Human Video Diffusion at Test Time**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02964)
![architecture](https://img.shields.io/badge/Pseudo_Supervision_Test_Time_Personalization-red)
![task](https://img.shields.io/badge/Personalized_Image_Generation-magenta)
![organization](https://img.shields.io/badge/Concordia_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/SadmanPinon/one-image-is-enough)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**One Image Is Enough 用姿态条件生成器为单个参考图合成伪真值帧，再以低秩适配器做测试期人物视频个性化，无需任何主体视频；其在 TikTok 与 UBC Fashion 上把基线 FVD 从 402.14 降到 133.5，并追平甚至超过用 5 帧真实素材的适配效果。**</p>
+ **Intent2CAD: How Semantic-Parametric Supervision Shapes Text-to-CAD Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03449)
![architecture](https://img.shields.io/badge/Semantic_Parametric_Lifting_Text_To_CAD-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/JinboYang94/Intent2CAD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Intent2CAD 研究监督表示粒度对文本到 CAD 生成的影响，构建 10 万对的 IntentCAD-100K 与 IntentCAD-Edit-1K；不做架构改动，仅靠语义提升把无效程序率从 2.39% 降到 0.22%、API 恢复率达 99.96%，参数化提升再改善零样本意图保持编辑。**</p>
