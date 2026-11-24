<!-- direction: aigc_generation -->

+ **HorizonFlow: Few-Step Video Distillation in 600 Iterations**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29431)
![architecture](https://img.shields.io/badge/HorizonFlow-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/XIANGLONGGUO/HorizonFlow-repo)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**仅用 600 次迭代与 8.4k 样本把 Wan2.1-T2V-1.3B 蒸馏成 4 步视频模型，VBench 总分 85.64，样本量比 rCM 少 304 倍。**</p>

+ **Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29618)
![architecture](https://img.shields.io/badge/Mass_Forcing-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/City_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 DMD 监督从整段视频下沉到单个状态，按师生概率质量比重加权更新，训练 1,000 步后 Dynamic Degree 仍有 83%，基线仅 12–32%。**</p>

+ **Constrained Diffusion from Binary Evaluations via Learned Doob h-Functions**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29779)
![architecture](https://img.shields.io/badge/Doob_H_Transform_Guidance-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Pennsylvania-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 Doob h 变换把约束生成化成学一个二值标签函数，基座扩散模型冻结不需重训，QM9 类 Lipinski 性质过滤通过率由 54.3% 提到 96.8%。**</p>

+ **Same Seed, Different Picture? Deciding Early at Low Resolution for Seed-Faithful Few-Step Flow Sampling**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30728)
![architecture](https://img.shields.io/badge/Decide_then_Render-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/The_City_University_of_New_York-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**定位到构图在噪声水平高于 0.9 时就已决定，先半分辨率决策再全分辨率渲染，训练-free 采样在 4 个大模型上快 11–25 倍且更贴近 50 步参考。**</p>

+ **DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30844)
![architecture](https://img.shields.io/badge/DyLoMo_DiT-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://oneboxcream.github.io/DyLoMo-DiT/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以权重共享循环层加深网络、稀疏专家分配参数容量，等预算下 ImageNet FID 相对 DiT 降 11–24%，GenEval 0.714 超过 FLUX.1。**</p>

+ **Demystifying Classifier-Free Guidance for Auto-Regressive Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29002)
![architecture](https://img.shields.io/badge/AttnReuse-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Yale_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**实证拆解自回归图像生成中 CFG 的机制：纹理只存在于条件与无条件 logit 之差，二者共享的重复语义使注意力复用可行，AttnReuse 可省约 25% 注意力算力。**</p>

+ **Hindsight Forcing: Learning Better History from the Future in Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27074)
![architecture](https://img.shields.io/badge/Hindsight_Forcing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/City_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/haonanAN309/Hindsight-Forcing)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 latent 直通桥让历史 chunk 直接从未来结果学习，不增参数不改架构，VBench 总分 85.74，Dynamic Degree 从 73.33 提到 92.22。**</p>

+ **Beyond Prompt Imitation: Capability-Aware Video Generation with Smaller Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27252)
![architecture](https://img.shields.io/badge/Oracle_Control_Ladder-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_New_South_Wales-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出神谕控制阶梯，逐级给固定学生模型喂稠密描述、首帧、深度视频等控制，量出每级控制能闭合多少保真度差距，为小模型追平大模型提供可量化的 headroom 基准。**</p>

+ **Budgeted Safety Verification for Streaming Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27268)
![architecture](https://img.shields.io/badge/Budgeted_Safety_Guard-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把流式视频安全判定建模为按预算排序的停止问题，用生成器隐状态做廉价排序再升级到视频模型判定，599 条流上的有害暴露帧从 46.25 降到 2.35 帧。**</p>

+ **Scalable Beckmann Maps Improve One-step Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28286)
![architecture](https://img.shields.io/badge/Scalable_Beckmann_Map-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Harvard_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tullebulle.github.io/projects/sbm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给 Beckmann 传输模型补上 CFG 与可扩展训练配方，保持单次网络前向的一步生成，ImageNet 一步 FID 1.6、文本生成 GenEval 0.86。**</p>

<!-- direction: aigc_editing -->

+ **TOGO: Take One Image Editor, Get One Video Editor for Free**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28397)
![architecture](https://img.shields.io/badge/TOGO-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Chicago-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**利用图像编辑器与视频模型共享潜空间，把编辑速度零训练叠加到视频采样器上，FiVE-Bench 成功率从 47.0% 提到 65.6%，超过最佳已发表方法 6.4 个点。**</p>

+ **LiveMirror: Real-Time Diffusion Virtual Try-On on a Consumer GPU and Its Self-Supervised Adaptation to Indian Ethnic Wear**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30461)
![architecture](https://img.shields.io/badge/LiveMirror-red)
![task](https://img.shields.io/badge/Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/School_of_Electronics_Engineering_KIIT_Deemed_to_be_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**单张 16GB 消费级 GPU 上用异步关键帧实现实时试穿镜像，720p 稳定 25 FPS，并用 24.9k 自监督照片把民族服装 LPIPS 从 0.137 降到 0.077。**</p>

+ **Borrow the Style, Follow the Prompt: Progressive Reference-Guided Stylization**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27360)
![architecture](https://img.shields.io/badge/ProStyle-red)
![task](https://img.shields.io/badge/Style_Transfer-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**学习内容抑制的风格先验再渐进拟合全参考残差，配 134K 跨内容训练对，ReConStyle-Full 上七项标准平均排名 1.86，用户研究文本对齐选择率 84.36%。**</p>

+ **ReCoRain: Reliability-Coupled Content and Noise Conditioning for Event-Guided Video Deraining**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28717)
![architecture](https://img.shields.io/badge/ReCoRain-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以 RGB 外观、事件证据与前后向运动一致性共同估计对应可靠性，耦合内容搬运与噪声关联，NTURain-Syn 达 32.09 dB，门控使 warp 误差降 33.0%。**</p>

<!-- direction: aigc_rl -->

+ **DeFlowCritic: Dense Latent Reward Alignment for Text-to-Image Flow Matching Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28265)
![architecture](https://img.shields.io/badge/DeFlowCritic-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Inria-green)
[![project](https://img.shields.io/badge/project-blue)](https://zeeshank95.github.io/deflowcritic/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用扩散模型自身特征训内部 critic 给中间潜变量打密集奖励，GenEval2 的 HPSv3 从 7.13 提到 8.07，训练比 Flow-GRPO 快约 10 倍。**</p>

+ **Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30986)
![architecture](https://img.shields.io/badge/iTDM-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Luo-Yihong/iTDM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示前向扩散 RL 的基线假设在 CFG rollout 与离线更新下失效，用瞬时轨迹分布匹配锚定梯度，GenEval2 近 3 倍更快收敛并稳定涨到 0.87。**</p>

+ **Preserving Pretrained CFG Structure in RL for Diffusion Models with Conditional Contrast Regularization**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27288)
![architecture](https://img.shields.io/badge/Conditional_Contrast_Regularization-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现 RL 学到的修正与预训练 CFG 修正平均夹角约 93.5 度，用冻结模型的条件对比作结构先验，GenEval 设定下 Laplacian 方差由 208 提到 841。**</p>

