+ **EchoChat: Structured Cognitive Reasoning in Empathetic Spoken Dialogue**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.04826)
![architecture](https://img.shields.io/badge/SpeechLLM_SFT_Acoustic_Anchored_Attention_RL_SDCA-red)
![task](https://img.shields.io/badge/Spoken_Dialogue-magenta)
![organization](https://img.shields.io/badge/The_Chinese_University_of_Hong_Kong_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dingdongwang/EchoChat)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Reframes empathetic spoken dialogue as structured cognitive reasoning - perception, then latent mental-state reasoning, then response - rather than a direct input-to-response mapping. The diagnosis is that the simplified formulation produces "superficially warm" interactions and lets errors at any stage cascade untracked.**</p>

+ **TS-SP: Learning Speaker-Preserving Representations in Audio Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.04887)
![architecture](https://img.shields.io/badge/Two_Stage_LoRA_Speaker_Supervision-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Department_of_Electrical_and_Electronic-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TS-SP (Two-Stage Speaker Preservation) addresses a specific and underexamined gap: audio LLMs understand speech content but cannot use speaker identity for verification. It learns speaker-preserving representations and exposes them to the LM's computation without retraining the backbone.**</p>

+ **SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05610)
![architecture](https://img.shields.io/badge/FoACoder_Spatial_Encoder_MLLM_Dual_Pathway-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland_College_Park-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SEA-LM handles egocentric spatial audio understanding for wearable microphone arrays, cutting azimuth mean absolute error from 80.6 to 14.9 degrees and elevation error from 27.4 to 12.8 degrees, while raising location-bin accuracy from 42.0% to 84.1%.**</p>

+ **Mind the Accent Gap: British Accent Robustness in Speech-Driven Financial Voice Assistants**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06587)
![architecture](https://img.shields.io/badge/Cascaded_ASR_LLM_Accent_Benchmark-red)
![task](https://img.shields.io/badge/Voice_Assistant-magenta)
![organization](https://img.shields.io/badge/Within_British_English-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Measures accent robustness in speech-driven financial voice assistants and shows that ASR trained predominantly on American English carries errors through to the LLM reasoning stage for Scottish, Irish and Welsh accents - the failure is in the cascade, not only the recognizer.**</p>

+ **Transferable Adversarial Robustness for Speech Foundation Models via Hierarchical Stabilization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05310)
![architecture](https://img.shields.io/badge/Hierarchical_Adversarial_Robustification_Margin_Refinement-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Sharif_University_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/arefmousavi/hierarchical-robust-sfm)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Shows robustness against adversarial audio can be learned *before* future downstream tasks are known: across 12 backbone-task pairs on Wav2Vec2, HuBERT and WavLM Large under adaptive 30 dB attacks, hierarchical robustification improves robust accuracy by 46.4 percentage points.**</p>

+ **UltraM2M: Leveraging Text Transcripts and Mixture Constraints for Weakly-Supervised Speech Enhancement** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05155)
![architecture](https://img.shields.io/badge/M2M_Mixture_Constraint_Plus_ASR_Loss-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UltraM2M extends the unsupervised mixture-to-mixture speech enhancement idea with two weak-supervision signals - text transcripts and mixture constraints - so target speech need not be perfectly separated.**</p>

+ **Character Identity is not Speaker Identity: KyaraBench and KyaraEmbed for Character Verification** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06013)
![architecture](https://img.shields.io/badge/Character_Supervised_Compact_Audio_Encoder-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Spellbrush_CA_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Separates character identity from speaker identity - a dubbed character keeps its identity while the voice actor changes, so speaker verification measures only one of the two properties that actually matter for verification in dubbed or synthetic media.**</p>

+ **Revisiting Label-Free Speaker Embedding Enhancement with vMF Profile Likelihood** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06691)
![architecture](https://img.shields.io/badge/vMF_Profile_Likelihood_Embedding_Enhancement-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Shows that for label-free speaker embedding enhancement with a frozen backbone, a simple direct matching objective on the unit hypersphere is already competitive - modelling the clean target with a von Mises-Fisher likelihood and profiling out a sample-wise concentration parameter yields a closed-form loss with adaptive reweighting.**</p>

+ **Revisiting Frame-Wise Saliency for Audio Moment Retrieval** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05737)
![architecture](https://img.shields.io/badge/Frame_Wise_Saliency_Parameter_Free_Segmentation-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/LY_Corporation_Tokyo_Japan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Shows the frame-wise saliency sequence - conventionally only an auxiliary output in DETR-based audio moment retrieval - can itself be the prediction source, converted to ranked moments by a parameter-free SED-inspired segmentation rule.**</p>

+ **AraYoungVoices: A Diverse L1/L2 Corpus of Arabic Child and Adolescent Speech** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05044)
![architecture](https://img.shields.io/badge/Age_Nativity_Aware_ASR_Corpus-red)
![task](https://img.shields.io/badge/Audio_Understanding-magenta)
![organization](https://img.shields.io/badge/Qatar_Computing_Research_Institute_Qatar-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Releases AraYoungVoices, a 151.72-hour Arabic read-speech corpus of 86,471 utterances from 286 speakers aged 7-18, split into AraKids (7-12) and AraTeens (13-18), with 146 L1 and 140 L2 speakers spanning Egyptian, Gulf, Levantine and North African dialects.**</p>

