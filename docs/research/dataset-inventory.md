# Deepfake Dataset Inventory & Classification Matrix

This inventory categorizes benchmark datasets used for training and evaluating Deepfake generation and detection algorithms. Datasets are organized by "Generation" eras, reflecting the evolution of manipulation complexity.

---

## 1. Generation 1: Standard Visual Manipulations
*Focus: Face-swapping and basic facial expression manipulation using early autoencoder architectures or traditional computer vision graphics.*

### UADFV (University at Albany DeepFake Video)
* **Description:** A localized dataset targeting physiological signals (specifically, unnatural blinking rates).
* **Composition:** 49 real videos, 49 fake videos.
* **Primary Utility:** Benchmark for early, artifact-based detection algorithms.
* **License:** Custom Academic/Research Use Only.
* **Access Link:** [Official UADFV Repository via kaggle](https://www.kaggle.com/datasets/adityakeshri9234/uadfv-dataset)

### DeepFakeTIMIT
* **Description:** Generated using an open-source autoencoder framework based on the Faceswap GitHub repository, manipulating the VidTIMIT database.
* **Composition:** 620 fake videos split across low-quality (`64×64`) and high-quality (`128×128`) resolutions.
* **Primary Utility:** Evaluating basic GAN and autoencoder face-swaps under controlled lighting.
* **License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
* **Access Link:** [IDIAP Research Institute DeepFakeTIMIT Portal](https://www.idiap.ch/en/dataset/deepfaketimit)

---

## 2. Generation 2: Large-Scale & Real-World Forgery Benchmarks
*Focus: Scaling data volume, tracking diverse generation networks, and introducing real-world environmental diversity (lighting, compression, angles, internet artifacts).*

### FaceForensics++ (FF++)
* **Description:** An industry-standard benchmark featuring thousands of video clips manipulated by four distinct automated techniques (Deepfakes, Face2Face, FaceSwap, and NeuralTextures).
* **Composition:** 1,000 pristine source videos, 4,000 manipulated videos across 3 compression levels (Raw, HQ, LQ).
* **Primary Utility:** Evaluating detection model robustness against real-world video compression and post-processing.
* **License:** FaceForensics Terms of Use (Strictly Non-Commercial / Academic Research Only via signed agreement).
* **Access Link:** [Official FaceForensics GitHub](https://github.com/ondyari/FaceForensics)

### Celeb-DF (v2)
* **Description:** A high-quality dataset specifically designed to reduce standard visual artifacts (such as boundary blending issues and low-resolution face ghosting) seen in earlier datasets.
* **Composition:** 590 original celebrity videos, 5,639 high-quality synthesized deepfakes, and 300 additional YouTube-real videos.
* **Primary Utility:** Training models on seamless, modern visual fakes with minimized color mismatching.
* **License:** Custom Academic Research License Agreement.
* **Access Link:** [Celeb-DF via github](https://github.com/yuezunli/celeb-deepfakeforensics)

### WildDeepFake
* **Description:** A dataset harvested entirely from real-world internet sources rather than synthesized in a controlled lab environment. It features a vast diversity of expressions, angles, lighting conditions, and unknown baseline generation algorithms.
* **Composition:** 7,314 face sequences extracted from 707 internet-sourced deepfake videos, intentionally containing diverse synthesis anomalies.
* **Primary Utility:** Testing the generalization of detection models against practical, uncontrolled "wild" internet deepfakes and multi-person frames.
* **License:** Custom Research Use License.
* **Access Link:** [WildDeepFake Repository on GitHub](https://github.com/OpenTAI/wild-deepfake)

---

## 3. Generation 3: Hyper-Realistic & Audio-Visual Forgeries
*Focus: Multi-modal fakes (synchronized audio-to-video manipulation) and large demographic diversity to eliminate model bias.*

### DFDC (DeepFake Detection Challenge)
* **Description:** Created by Facebook AI (now Meta) to incentivize global detection pipelines. Features diverse actors, varied lighting, shadows, and synthetic audio tracks. Includes consenting paid actors and multiple manipulation methods.
* **Composition:** 128,154 total videos (104,500 unique fake videos) generated using eight facial modification algorithms, sourced from 3,426 paid actors.
* **Primary Utility:** Global benchmark for commercial-grade detection software and multi-modal audio-visual evaluation.
* **License:** CC BY-NC 4.0 (Non-Commercial Research and Development).
* **Access Link:** [AI Commons / Kaggle DFDC Portal](https://ai.meta.com/datasets/dfdc/)

### FakeAVCeleb
* **Description:** A novel audio-visual deepfake dataset introducing deepfake audio synced with manipulated facial videos across a multicultural demographic.
* **Composition:** Over 20,000 video clips utilizing methods like Wav2Lip, Faceswap, and SV2TTS.
* **Primary Utility:** Advancing multimodal (audio + video) deepfake tracking and reducing demographic bias in detection models.
* **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
* **Access Link:** [FakeAVCeleb Project Platform via GitHub](https://sites.google.com/view/fakeavcelebdash-lab/)

---

## 4. Comprehensive Technical Matrix

| Dataset | Version / Compression | Frame Sampling Method | Split Logic | License Type | Official Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UADFV** | v1.0 / Uncompressed (Raw) | Complete Sequence / Fixed Frame Window | Fixed Subject-based Split (Targeted Identities) | Custom Academic | [UADFV Source](https://www.kaggle.com/datasets/adityakeshri9234/uadfv-dataset) |
| **DeepFakeTIMIT** | v1.0 / Low-Q ($64^2$) & High-Q ($128^2$) | Full Sequence Tracking | Subject-Independent Split (VidTIMIT ID isolation) | CC BY-NC-SA 4.0 | [IDIAP Portal](https://www.idiap.ch/en/dataset/deepfaketimit) |
| **FaceForensics++** | v1.0 / Raw (c0), HQ (c23), LQ (c40) | Evenly Spaced Intermittent Frame Extraction | 720 Train / 140 Validation / 140 Test (Videos) | Custom Restrictive | [FF++ Source](https://github.com/ondyari/FaceForensics) |
| **Celeb-DF v2** | v2.0 / Standard MP4 Broadcast Compression | Face-Detection Anchored Sampling | Identity Cut-off (Diverse subjects isolated to Test set) | Custom Research | [Celeb-DF Project](https://github.com/yuezunli/celeb-deepfakeforensics) |
| **WildDeepFake** | v1.0 / Variable Native Web Compression | Extracted Facial Crop Sequences (No-drop tracking) | 80% Train / 20% Test (Randomly split by sequence) | Research Only | [WildDF Repository](https://github.com/OpenTAI/wild-deepfake) |
| **DFDC** | Final Production / Variable (Simulated Augmentation) | Randomized Stratified Chunk Selection | Strict Actor-Independent Split (No overlap across sets) | CC BY-NC 4.0 | [Meta AI Dataset](https://ai.meta.com/datasets/dfdc/) |
| **FakeAVCeleb** | v1.0 / Standardized H.264 Web Compression | Audio-Frame Boundary Coordinated Extraction | 70% Train / 15% Validation / 15% Test (Demographic) | CC BY 4.0 | [FakeAVCeleb Source](https://sites.google.com/view/fakeavcelebdash-lab/) |