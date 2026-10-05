+ **Rubric-Based Optimization for Text-to-Music Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03589)
![architecture](https://img.shields.io/badge/Rubric_Reward_DPO-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Paul_G._Allen_School_of_Computer_Science_-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Uses pretrained audio-language models (ALMs) as rubric-based reward scorers for music generation: an ALM scores each generated clip against the rubric, candidates for the same text prompt are ranked by score, and rankings are converted into preference pairs for DPO on MusicGen-small and ACE-Step-v1.**</p>

+ **DriftTTS: Few-Step Text-to-Speech Without Distillation via Distribution-Matching Drift**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03390)
![architecture](https://img.shields.io/badge/Distribution_Matching_Drift-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/University_of_Massachusetts_Amherst_MA_USA-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/BASHLab/driftTTS)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DriftTTS is a few-step mel-spectrogram generator trained without a generative teacher, without distillation and without adversarial discrimination - avoiding the dependencies that dominate few-step TTS.**</p>

+ **Refinement Buys Intelligibility, Search Buys Identity: What Test-Time Compute Buys in Masked-Diffusion TTS**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03320)
![architecture](https://img.shields.io/badge/Masked_Diffusion_Codec_TTS-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Work_done_outside_of_Blackstar_Inc-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Trains 15 masked-diffusion codec TTS models (19-133M parameters, 3 seeds) on 2,000 hours of speech and sweeps refinement steps T in [1,16], measuring zero-shot synthesis via ASR word error rate (intelligibility) and speaker verification (identity) on 174 held-out speakers.**</p>

+ **Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.01012)
![architecture](https://img.shields.io/badge/Conditional_Flow_Matching-red)
![task](https://img.shields.io/badge/Speech_Synthesis-magenta)
![organization](https://img.shields.io/badge/Department_of_Information_and-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/gunwoo5034/Watch-your-Speech)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Identifies the one-to-many mapping problem in video-to-speech synthesis - visual dynamics often lack sufficient information to uniquely determine the utterance.**</p>

+ **Shared-State Local Translations for Training-Free Voice Conversion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.01952)
![architecture](https://img.shields.io/badge/Gaussian_Mixture_State_Transfer-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/Shared_GMM-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**In one-shot training-free voice conversion, source and reference utterances may contain different linguistic content, so reliable frame-level correspondence cannot be assumed.**</p>

+ **Q-SPT: Learnable Query-Based Compression for Low-Frame-Rate Speech Tokenization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.01492)
![architecture](https://img.shields.io/badge/Dual_Stream_Query_Compressor-red)
![task](https://img.shields.io/badge/TTS-magenta)
![organization](https://img.shields.io/badge/Korea_University_Seoul_Republic_of_Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Lowering speech-codec frame rate cuts SLM compute and memory but makes it hard to preserve both linguistic information and acoustic detail. Rule-based compression fails asymmetrically: average pooling discards linguistic information, while similarity-based merging uses a fixed threshold on adjacent-frame similarity and applies those boundaries to the acoustic stream too.**</p>

+ **Multi-sample Synthetic Supervision for Accent Conversion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.01961)
![architecture](https://img.shields.io/badge/Discrete_Speech_Code_Adaptation-red)
![task](https://img.shields.io/badge/Voice_Conversion-magenta)
![organization](https://img.shields.io/badge/Stage1_Synthetic_Training_Data-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Accent conversion must change accent while preserving speaker identity and linguistic content, but parallel recordings are scarce and synthesized targets vary in accent realization and source preservation.**</p>

+ **Learning Jazz Pianist Style with Cross-Attention Conditioning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02918)
![architecture](https://img.shields.io/badge/Cross_Attention_Conditioning-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Centre_for_Digital_Music-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Shows a pretrained symbolic music transformer's learned representations already encode pianist identity well enough for highly accurate classification across two benchmarks.**</p>

+ **From Isolated Feature to Orbits: Discovering Music Concepts via Multi-SAE Alignment**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.01864)
![architecture](https://img.shields.io/badge/Sparse_Autoencoder_Alignment-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Computer_Science_Department_NYU_Shanghai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Argues many music concepts are better understood as structured relations rather than isolated features - chords and keys are naturally expressed as structured sets (12 transpositions of a chord, the diatonic system within a key) rather than single features.**</p>

+ **How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02837)
![architecture](https://img.shields.io/badge/Causal_Transformer_Analysis-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/Department_of_Computing_Science-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Trains a small causal Transformer separately at each context length T in {6, 18, 48, 96, 192, 336} over symbolic music and evaluates on the same target positions, over raw tokens and over non-overlapping binary latent codes.**</p>

