+ **S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06847)
![architecture](https://img.shields.io/badge/Serial_To_Parallel_Diffusion-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Names the failure precisely - bidirectional video diffusion transformers violate physical laws and simple symbolic rules even when trained on effectively unlimited procedurally generated data, so physical accuracy does not emerge from data scaling alone. The proposed cause is sequential depth: diffusion models stay in TC0, so structure that needs serial computation is never supplied.**</p>

+ **Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05608)
![architecture](https://img.shields.io/badge/Dual_Stream_CrossDiT-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Kandinsky_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**A family of two fully open foundation models - Kandinsky 6.0 Video Lite (3B) and Pro (29B) - each generating 5-second clips with synchronized 44 kHz audio including lip-sync, in both text-to-audio-video and image-to-audio-video modes, with a built-in super-resolution model lifting output to Full-HD (1920x1080).**</p>

+ **Level-of-Token Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05816)
![architecture](https://img.shields.io/badge/Level_Of_Token_Asymmetric_Flow_DiT-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Up to 2.04x speedup for images and 3.53x for videos on average versus full-resolution pretrained models, with the speedup set by the layout's token budget. On FLUX.2-klein-base-4B at 2.040x compression it reaches 1.32-2.04x and beats ToMe-SD, DDiT and Foveated Diffusion on most metrics at every token budget.**</p>

+ **PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05233)
![architecture](https://img.shields.io/badge/Pixel_Conditioned_Causal_Video_DiT-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**On a purpose-built 68-pair extreme-condition benchmark (CelebV-HQ drivers with extreme poses and occlusions, FFHQ references) PixReenact lifts AdaFace identity similarity from PersonaLive's 0.472 to 0.727 and lowers expression deviation from 1.295 to 1.135, at equal temporal LPIPS (1.853 vs 1.866).**</p>

+ **SPIN: Image Immunization Against Diffusion Editing via Single-Step Projection in Stochastic Neighborhoods**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06334)
![architecture](https://img.shields.io/badge/Single_Step_Projection_Stochastic_Neighborhood-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/School_of_Advanced_Interdisciplinary-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Immunization success reaches 90% on SD3 and 94% on InstructPix2Pix under the instructions used to build the perturbation, against 84-85% for the best baseline (AdvDM / MIST), with the largest margin on SD3 where protected-image PSNR drops to 11.20 versus AdvDM's 13.54 and LPIPS rises to 0.6730 versus 0.5391.**</p>

+ **How Does Geometry Enter Generated Motion?**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05135)
![architecture](https://img.shields.io/badge/Controlled_Geometry_Intervention_Benchmark-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Across nine image-to-video models (six open-weight, three closed) and more than 5,000 generated videos, geometry genuinely shapes motion but the *state* does not evolve by the physical law: the ball rises above its release height in 63 of 72 videos and crosses 43 of 49 physically impassable barriers, and with three deflectors the correct physical contact order appears in at most a quarter of a model's videos.**</p>

+ **UniSlider: Perceptually Uniform Sliders for Continuous Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06831)
![architecture](https://img.shields.io/badge/Perceptual_Uniformity_LoRA_Reparam-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Computer_Vision_Center-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**The core objective is stated as a constraint rather than a heuristic - perceptual distance from the input must grow linearly with the slider, D(x_src, x_s) = s*D(x_src, x_edit), while the trajectory stays on the perceptual path, D(x_src,x_s) + D(x_s,x_edit) = D(x_src,x_edit). Current sliders (adapter coefficient, prompt weight, interpolation factor) fail this, producing dead zones, jumps and reversals.**</p>

+ **Geometry-Aware Preference Optimization for Text-to-Image Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.04980)
![architecture](https://img.shields.io/badge/Anisotropic_Jacobian_Metric_Preference_Opt-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/aSun_Yat_Sen_University_Guangzhou_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Identifies a named geometric failure mode of DPO-style diffusion alignment - off-manifold drift. Standard Diffusion-DPO measures the noise-prediction residual under an isotropic Euclidean metric, which over-regularizes manifold-tangent directions and under-constrains geometry-sensitive normal directions, degrading image quality and diversity as training proceeds.**</p>

+ **Keepsake: Selective Spatial Memory for Long-Horizon Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06588)
![architecture](https://img.shields.io/badge/Pose_Appearance_Graph_Memory_Controller-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Institute_of_Artificial_Intelligence-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**On 180-second MemCam trajectories Keepsake retains only 32 of 5,397 frames and reduces FVD from 734.2 to 476.6 (-35.1%), while cutting CPU lookup time per query from 3,077.6 ms to 43.8 ms. On 60-second WorldMem it improves both FVD (1,116.9) and LPIPS (0.534) over full retention.**</p>

+ **DynaMesh: Dynamic 3D Texture Generation** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05529)
![architecture](https://img.shields.io/badge/Temporal_Blend_PerShape_LoRA_ImageTo3D-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Chicago-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Over 42 objects and effects and all 150 frames, DynaMesh reaches flicker 0.005 and acceleration 0.005 (per-step temporal errors), beating the frozen per-frame image-to-3D generator (0.023 / 0.035) and video-to-4D baselines (SV4D 2.0 at 0.074 / 0.142, MeshNCA 0.007 / 0.011), at PSNR 24.9 / SSIM 0.798 fidelity to the reference video.**</p>

