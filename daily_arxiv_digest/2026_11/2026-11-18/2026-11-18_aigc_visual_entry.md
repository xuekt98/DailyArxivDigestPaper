<!-- direction: aigc_generation -->

+ **TetraCoder: Adaptive Tetrahedral Encoding for Neural Fields**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18267)
![architecture](https://img.shields.io/badge/TetraCoder_Adaptive_Tetrahedral_Encoding-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Trento-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TetraCoder 用单分辨率、无哈希的自适应四面体编码把隐式 SDF 与显式网格一一对应：Stanford 重建 Chamfer 距离 1.611×10⁻³ 对 1.718×10⁻³，解析提取 0.446 s 对 2.859 s，参数量 5.22 M 对 16.78 M，并支持直接在四面体骨架上改几何与外观。**</p>

+ **LongCat-Video-Avatar 1.6 Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18822)
![architecture](https://img.shields.io/badge/Dual_Branch_GRPO_OPSD_Pipeline-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Meituan-green)
[![project](https://img.shields.io/badge/project-blue)](https://meigen-ai.github.io/LongCat-Video-Avatar-1.6-Page)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LongCat-Video-Avatar 1.6 用 GRPO 与 on-policy 自蒸馏两条 LoRA 分支改造音频驱动数字人的后训练，采样从 50 步压到 8 步并可生成超过 10 分钟视频；在 33,051 票人类偏好 Arena 中 Elo 1068.1 位列六模型第二，仅次于闭源 OmniHuman-2.0。**</p>

+ **MORE: Merge Once, Route Early for Training-Free Multi-Subject Composition from Large LoRA Pools**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21077)
![architecture](https://img.shields.io/badge/Merge_Once_Route_Early-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sumorday/MORE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MORE 用 SSR-Merge 把 K=10/20 个主体 LoRA 一次性压成单个 rank-8/16 适配器，再在前 30% 去噪步门控到各自区域：留出种子上双主体共存率 94.2%/78.3%，对照 FreeFuse 的 50.8%/35.8%，ImageReward 1.32 对最好基线 0.07。**</p>

+ **Reference Forcing: Long Video Generation with Region-Guided Drift Correction**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21559)
![architecture](https://img.shields.io/badge/Region_Guided_Anchor_Distillation-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Rochester-green)
[![project](https://img.shields.io/badge/project-blue)](https://zhaosheng-thu.github.io/reference-force/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Reference Forcing 用首帧作外观参考，教师以注意力掩码强制新帧各区域只关注首帧同区域，再蒸馏进学生的独立注意力通路并对 KV 缓存做免训练的值修正：MovieGenBench 30 秒主体一致性 97.55、背景 96.70，平均排名第一，可一次生成两小时视频。**</p>

+ **Découpage: Directorial Audio-Visual Control for Long Multi-Shot Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18866)
![architecture](https://img.shields.io/badge/Dual_Schedule_Temporal_Cross_Attention-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://wyf0824.github.io/decoupage/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Découpage 用剧本驱动长多镜头音视频生成，把视觉与声学两条轨道解耦并各自定时，配双调度时间交叉注意力与按可见性门控的 directorial Lip-sync：15 秒 Cut F1 0.99、WER 4.59%，60 秒仍有 0.76 Cut F1、91.12% 对话 containment。**</p>

+ **Few-Shot Visual Concept Extraction for Steering Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19440)
![architecture](https://img.shields.io/badge/Masked_Difference_Of_Means_Steering-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Inria_Centre_at_Université_Côte_d’Azur-green)
[![project](https://img.shields.io/badge/project-blue)](https://newbyl.github.io/few_shot_project_page)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练地从 DiT 图像侧激活里抽概念方向：全局概念用全局差分均值、局部概念用掩码差分均值，5 对提示就够。FLUX.1-schnell 上 ∆VQA 0.32、LPIPS 0.29，优于 SAEdit 的 0.19 与 FluxSpace 的 0.17，已接近需训练的编辑模型。**</p>

+ **FastGRN: Few-Step Generative Refinement Networks**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20021)
![architecture](https://img.shields.io/badge/Few_Step_Generative_Refinement_Network-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Ritsumeikan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FastGRN 让离散潜变量生成器在自己的样本分布上做分布匹配蒸馏，把 50 步压到 2–4 步：ImageNet 256 上 2 步学生 FID 3.73 与教师持平且每图从 835 ms 降到 66 ms，3 步降到 FID 3.42，2B 文本到图像 4 步 GenEval 0.69 接近教师 0.695。**</p>

+ **GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20192)
![architecture](https://img.shields.io/badge/Glyph_Atlas_Anchored_Attention-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Xiamen_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://fr0zencrane.github.io/project-glyphatlas/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GlyphAtlas 把场景文字合成的两个职责解耦：glyph image 只做空间锚点，独立的 glyph atlas 每格渲染字符提供笔画参考，再用 atlas-anchored attention 绑定回布局。AnyText 基准英文句子准确率 88.68%、中文 77.92%，TextOCR 编辑准确率 33.15%。**</p>

+ **MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21339)
![architecture](https://img.shields.io/badge/Window_Wise_Teacher_Forcing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://Tencent-Hunyuan.github.io/MovieRoll/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MovieRoll 是流式长视频的「基座到蒸馏」框架：WinTF 并行窗口监督、CuLT-DMD 在长自 rollout 上训少步生成器、HieraKV 分层压缩缓存使 KV 显存最多降 78%，再用 KV 重计算与引导退火突破训练时序；HeliosBench 上蒸馏版在 10/30/60 s 单事件与多事件评测中总分最高。**</p>

<!-- direction: aigc_editing -->

+ **VIVID: A Visual Harness for Agentic Video Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20688)
![architecture](https://img.shields.io/badge/VIVID_Visual_Harness-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yuwenhan07/VIVID)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VIVID 是给通用编码 agent 用的视频编辑视觉 harness，不训任何模型，只加按需视听检查、带版本与时间坐标的持久证据记忆检索、以及渲染结果复检返修三件套：AgenticVBench 100 题上 Codex 平均 58.6%，比原生 Codex 高 20.2 个点。**</p>

+ **RAGE: Residual-Adaptive Gating for Flow-Based Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21177)
![architecture](https://img.shields.io/badge/Residual_Adaptive_Gating-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Xi’an_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RAGE 把流式图像编辑的源保真控制写成随机最优控制问题，解出残差门控原理：潜变量按局部残差幅度指数衰减的增益拉回源图，小偏差被压住、大改动照过。PIE-Bench 上在 17 个方法中整体排名最好，FLUX 与 SD3 背景保真都提升，每图只多 0.03 s。**</p>

+ **SearchChord: Prompt Preselection and Field Recomposition for One-Step Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19076)
![architecture](https://img.shields.io/badge/Prompt_Preselection_Field_Recomposition-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Michigan_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SearchChord 是免训练的一步图像编辑搜索框架：文本相似度从 100 个 prompt-种子候选里预筛 10 个，再用验证分数加权重组潜变量场。PIE-Bench 上 Best-of-10 把 CLIP-Edited 从 22.58 提到 23.14，加权重组把 PSNR 从 22.44 提到 24.13，二者存在权衡。**</p>

<!-- direction: aigc_rl -->

+ **BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20351)
![architecture](https://img.shields.io/badge/Block_Aligned_Preference_Optimization-red)
![task](https://img.shields.io/badge/Preference_Optimization_Visual-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BlockAlign 解决轨迹蒸馏视频生成的偏好后训练接口错配：在合法块边界构造状态、查询融合块级速度头并监督跨度归一化的转移残差，兼容 DPO/NFT/rollout 目标。RefVid-V4 自动评分均值 3.71 对 3.67，人工偏好 54.0% 对 33.3%，并让 PDD 的 5 倍少步加速换来 3 倍在线训练提速。**</p>

