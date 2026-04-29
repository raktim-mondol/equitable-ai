<!-- Page 1 -->

nature communications

8

Article

[https://doi.org/10.1038/s41467-025-66300-y](https://doi.org/10.1038/s41467-025-66300-y)

# Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness

Received: 3 March 2025

Accepted: 4 November 2025

Published online: 12 December 2025

 Check for updates

  Yanyan Huang 
^1^
, Weiqin Zhao 
^1^
, Zhengyu Zhang
^1^
, Yihang Chen 
^1^
, Yu Fu
^2^
, Feng Wu 
^3^
, Yuming Jiang 
^4^
, Li Liang 
^5,6^
, Shujun Wang 
^1,4^
 & Lequan Yu 
^1,5^

Foundation models in computational pathology suffer from site-specific and demographic biases, which compromise their generalizability and fairness. We introduce FLEX, a framework that employs a task-specific information bottleneck, guided by visual and textual domain knowledge, to disentangle robust pathological features from these artifacts. Using three large cohorts (The Cancer Genome Atlas, Clinical Proteomic Tumor Analysis Consortium, and an in-house dataset) across 16 clinical tasks, totaling over 9,900 slides, we demonstrate that FLEX achieves superior zero-shot generalization to unseen external cohorts, significantly outperforming baselines and narrowing the performance gap between seen and unseen domains. A comprehensive fairness analysis confirms that FLEX also effectively mitigates disparities across demographic groups. Furthermore, its versatility and scalability are proven through compatibility with various foundation models and multiple-instance learning architectures. Our work establishes FLEX as a promising solution for developing more generalizable and equitable pathology AI for diverse clinical settings.

Histopathology remains the gold standard for cancer diagnosis and treatment planning, yet its traditional manual analysis faces challenges of subjectivity and limited scalability1,2. Recent advances in artificial intelligence (AI) have revolutionized computational pathology, enabling the automated extraction of complex patterns from histopathology images with high accuracy and efficiency3–5. These advancements have paved the way for clinical applications such as automated cancer diagnosis, molecular biomarker prediction, and

treatment response assessment6–10. A pivotal development in this field is the emergence of pathology foundation models11–13, which are pre-trained on large-scale pathology datasets via self-supervised learning (SSL)14,15,16,18,20–24. These models act as powerful image feature extractors, acquiring transferable representations from whole slide images (WSI) patches and enabling accurate predictions for various clinical tasks by integrating multiple-instance learning (MIL) models25–28.

1School of Computing and Data Science, The University of Hong Kong, Hong Kong SAR, China. 2Department of Pathology, Nanfang Hospital, School of Basic Medical Sciences, Southern Medical University, Guangzhou, China. 3School of Information Science and Engineering, Lanzhou University, Lanzhou, Gansu, China. 4School of Medicine, Wake Forest University, Winston-Salem, North Carolina, USA. 5Guangdong Provincial Key Laboratory of Molecular Tumor Pathology, Guangzhou, China. 6Jinteng Laboratory, Chongqing, China. 7Department of Biomedical Engineering, The Hong Kong Polytechnic University, Hong Kong SAR, China. 8Research Institute for Smart Ageing, The Hong Kong Polytechnic University, Hong Kong SAR, China.  e-mail: li@emu.edu.cn; jyq@polyu.edu.hk; lyu@hku.hk

Nature Communications | (2025)16:11485

1

---

<!-- Page 2 -->

Article
https://doi.org/10.1038/s41467-025-66300-y

Despite these advancements, a critical limitation persists: features extracted by pathology foundation models exhibit significant site-specific signatures. These signatures, which stem from operational site preparation, staining protocols, and scanning equipment across different clinical centers (e.g., hospitals or research institutions) where samples are processed (Fig. 1a), directly impede cross-domain generalization. Specifically, they foster shortcut learning12 (Fig. 1b), where models learn superficial site-specific patterns rather than the underlying pathological features essential for robust diagnosis. As a result, these models often perform well on in-domain (IND) testing data but fail to generalize to out-of-domain (OOD) data. This can exhibit drastically reduced accuracy and unreliable predictions on out-of-domain (OOD) testing data (i.e., data from different sites with distinct site-specific patterns), compromising diagnostic reliability and robustness across risk of disease stratification data. Therefore, effective clinical practice. Although stain normalization13,14,15 has been proposed as a potential solution16, our findings demonstrate its ineffectiveness in eliminating site-specific signatures. Furthermore, the challenges of cross-site generalization, recent studies have highlighted a concerning lack of demographic fairness in pathology foundation models17, arising from variations in tissue appearance across demographic groups and their subsequent deployment. Therefore, effectively mitigating site-specific biases and demographic disparities is paramount for the responsible and reliable deployment of pathology foundation models in diverse clinical settings.

In this work, we propose a novel, two-Level Enhancement from Cross-domain generalization), an approach that leverages domain knowledge to address the intertwined challenges of cross-domain generalization and demographic fairness. Our foundation models, FLEX enhances the model's focus on generic pathological patterns by employing an information bottleneck. This bottleneck is guided by visual and textual concepts enriched with domain-specific pathology knowledge. The information bottleneck features with task-specific textual concepts. These textual concepts are generated by the text encoder of pathology foundation models, and thus, originating from the text domain, they are not directly free from site-specific signatures. These signatures are present in the images. As a result, pathology images from diverse source sites and demographic groups, which exhibit distinct feature distributions, are effectively aligned to a unified feature space through alignment modules to generalize across heterogeneous sites and demographic groups, while enhancing the discriminativeness and expressiveness of encoded patch features (Supplementary Figs. 1 and 2). This alignment module mitigates the presence of confounding site-specific signatures and demographic biases in existing foundation models. We then assess FLEX across 16 diverse clinical tasks using a rigorous two-stage evaluation. This involves a Site-Preserved Monte Carlo Cross-Validation (SP-MCCV) within The Cancer Genome Atlas (TCGA) cohort and a zero-shot external validation on two independent cohorts: the public Clinical Proteomic Tumor Analysis Consortium (CPTAC; n = 1738) and our private Nanfang Hospital (NFH; n = 5318). This comprehensive evaluation demonstrates three key strengths of FLEX. First, it yields an improvement in cross-domain generalization, with performance improvements of 1.2–1.5% over the state-of-the-art external CPTAC and NFH cohorts. Second, it promotes demographic fairness by reducing performance disparities across demographic groups. Third, FLEX shows practical versatility in pathology foundation models, demonstrating superior performance across models (VLMs) and downstream MIL architectures, and maintains effectiveness across different data scales. These findings establish FLEX as a promising solution for improving the generalizability and fairness of pathology AI. By addressing the critical barriers of domain shift and bias, it offers a robust pathway for the reliable,

responsible, and equitable deployment of foundation models in clinical settings.

## Results

We first systematically evaluated the persistence of site-specific signatures and demographic biases in representations from pathology foundation models, and their negative impact on cross-domain generalization and fairness. We then demonstrate that our proposed FLEX framework mitigates these issues. As outlined in Fig. 1d, FLEX leverages visual and textual prior knowledge to enhance the discriminability and robustness of patch features. Our results are presented in three parts. First, we show that FLEX improves cross-domain generalization within the TCGA cohort and in zero-shot validation on external CPTAC and in-house cohorts. Second, we assess its impact on demographic fairness, revealing a marked reduction in performance disparities across race and ancestry groups. Finally, we establish the practical versatility of FLEX by confirming its compatibility with various foundation models and its effectiveness across different data scales. These findings highlight FLEX as a robust solution for developing more generalizable and equitable pathology AI models.

### FLEX improves cross-domain generalization and facilitates accurate clinical usage of pathology foundation models

This section evaluates how site-specific patterns in feature representations extracted by pathology foundation models affect cross-site generalization and fairness. To this end, we first evaluate the impact of site-specific signatures. TCGA is a cornerstone resource for cancer research, which includes WES from multiple contributing sites and introducing site-specific signatures across different relationships. Clinical applications. TCGA cohort comprises WES from 66 sites, breast carcinoma (BRCA) from 36 sites, stomach adenocarcinoma (STAD) from 22 sites, and colorectal adenocarcinoma (CRC) from 37 sites (Fig. 1c). To further investigate the impact of site-specific signatures, we first extract by the CONCH18 image encoder from the BRCA cohort (Fig. 2a, middle). Patches were color-coded by the substituting site (left panel) and diagnostic class (right panel). The clear clustering by site-specific signatures is evident. The color-coded signatures indicate that it is robust to UNAP hyperparameter variations (Supplementary Fig. 1). These patterns serve as problematic shortcuts, enabling models to predict clinical labels without learning meaningful task-relevant features and thereby compromising cross-domain generalization, as illustrated in Fig. 1b.

We first quantified this issue across 16 pathology tasks using an SP-MCCV. We then evaluate the impact of site-specific signatures on “Methods” within TCGA, where test data were split into IND and OOD subsets based on substituting sites (Fig. 2b). Patch features were extracted using CONCH18 and aggregated with an AMPIL model19. The results showed a significant drop in area under the receiver operating characteristic curve (AUROC) performance for OOD data compared to IND data across all task categories (Fig. 2c). Specifically, the average AUROC for IND was 0.918, 0.754, and 0.651 for morphology, molecular biomarker, and gene mutation tasks, respectively. In contrast, the average AUROC dropped to 0.853, 0.721, and 0.628. This performance decline illustrates the substantial impact of domain shift, a challenge that persists in performance across different foundation models.

A common method for addressing domain shift is stain normalization, such as the Reinhard method20–22, which aligns the color distribution of WES to a reference template. While this approach can be effective for simple color shifts, it often fails to color correct OOD often insufficient for more complex biases. As shown in Fig. 2a (right panel), features after Reinhard normalization remain strongly clustered by site. Consequently, this method yielded minimal and inconsistent performance gains, and in some cases, even reduced performance (Fig. 2d, Supplementary Table 1).

Nature Communications | (2025) 16:11485
2

---

<!-- Page 3 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

a

WSI processing pipeline

Step 1: Tumor Sectioning → Different Thickness

Step 2: Staining → Different Stain

Step 3: Scanning → Different Scanner

WSIs with different site-specific signatures

Different Thickness, Different Stain, Different Scanner

b

Shortcut learning via signature

Training

- Task-related Information
- Site-specific Information
- Feature Extractor
- Utilize Task-related Information
- Shortcut prediction
- Desired vs site-specific signature
- Site-specific signatures as shortcut

IND Testing (From same source sites with learning loss) → Good IND performance

OOD Testing (From different source sites with learning loss) → Poor OOD performance

c

Datasets and tasks

SP-MCCV training & test

- Lung: TCGA-NSCLC (n = 658, White 88.0%, Black 11.7%, Asian 0.3%)
- Breast: TCGA-BRCA (n = 937, White 75.6%, Black 21.3%, Asian 2.0%)
- Stomach: TCGA-STAD (n = 22, White 90.9%, Black 7.3%, Asian 1.8%)
- Colonorectal: TCGA-CRC (n = 606, White 77.7%, Black 21.3%, Asian 1.0%)

External test

- CPTAC: CPTAC-NSCLC (n = 1188), CPTAC-BRCA (n = 22), CPTAC-COAD (n = 247)
- NFH: NFH-NSCLC (n = 249), NFH-BRCA (n = 187), NFH-STAD (n = 598), NFH-CRC (n = 1346)

Tasks

- Morphology Classification: NSCLC subtyping, BRCA subtyping, STAD Lauren Prediction
- Molecular Biomarker Status Prediction: HER2 ER PR EYB VEGF Status Prediction
- Gene Mutation Prediction: TP53 NRAS KRAS KRAS GATA3 Prediction

d

Workflow

Original WSI → Segment → Foreground area → Crop → VLM Image Encoder (CONIC, PatchGAN-CLIP, Gufnet) → Original Patch Features → FLEX → Enhanced Patch Features → ML Model (ASML, PCCM, DMTL, PCCM, DMTL, PCCM, DMTL, PCCM) → Classifier → Quantile

Original Information

- Site-specific signature
- Task-related information
- Demographic info

Others

- Visual Knowledge (Guided by visual and textual domain knowledge)
- Textual Knowledge (Pretrained textual components)

Performance

- More generalizable
- More interpretable
- More fair

Evaluation

- AUROC
- Fairness
- Attention score
- UMAP

Figure 1 Overview of the computational pathology challenge and the proposed FLEX framework. a The WSI processing pipeline highlights variables that contribute to site-specific signatures. b Conceptual illustration of shortcut learning where models exploit spurious correlations from site-specific signatures instead of learning task-related biological features. This leads to high performance on IND data but poor generalization to OOD data from unseen sites. c Datasets and tasks used in this study. A large multi-center TCGA cohort is used for training and cross-validation, with two independent external cohorts (CPTAC and in-house NFH dataset) for zero-shot generalization testing. We address 10 diagnostic tasks across four major cancer types, including NSCLC, BRCA, STAD, and CRC, spanning morphology, molecular biomarker, and gene mutation prediction. d The proposed FLEX workflow. Patch features are extracted using a pre-trained pathology VLM. Guided by visual and textual domain knowledge, FLEX selectively suppresses site-specific and demographic signatures while amplifying task-relevant biological information. The enhanced features are then used by a ML model for slide-level prediction, leading to improved generalizability and fairness. Performance is evaluated using AUROC, fairness metrics, and interpretability methods (UMAP, attention maps). Schematics in panels (a, b), and the organ icons in panel (c) were created with BioRender.com.

Figure 1 Overview of the computational pathology challenge and the proposed FLEX framework. a The WSI processing pipeline highlights variables that contribute to site-specific signatures. b Conceptual illustration of shortcut learning where models exploit spurious correlations from site-specific signatures instead of learning task-related biological features. This leads to high performance on IND data but poor generalization to OOD data from unseen sites. c Datasets and tasks used in this study. A large multi-center TCGA cohort is used for training and cross-validation, with two independent external cohorts (CPTAC and in-house NFH dataset) for zero-shot generalization testing. We address 10 diagnostic tasks across four major cancer types, including NSCLC, BRCA, STAD, and CRC, spanning

Nature Communications | (2025)16:11485

3

---

<!-- Page 4 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

a FLEX Original Reinhard

b Site 1 Site 2 Site 3

c Morphology Classification Biomarker Status Prediction Gene Mutation Prediction CPTAC NFH

d TCGA OOD Testing TCGA IND Testing

e External Testing TCGA

f TCGA OOD Testing

Fig. 2 | FLEX enhances model generalizability and diagnostic performance by mitigating site-specific signatures. a t-SNE visualization of patch features from the TCGA BRCA dataset (BRCA-type task), encoded by a CONCI model. Features are colored by submitting site (left panel) or diagnostic class (right panel). Original features and those after Reinhard normalization show strong clustering by site and poor separation of diagnostic classes, confirmed by low site integration (LSI: 3.03 and 3.29) and class separability (Silhouette Score: 0.15 and 0.14) scores. Callouts highlight patches from the same site with different diagnoses clustering together, indicating that site-specific signals overrule biological ones. In contrast, FLEX processed features show effective removal of site signatures (LSI: 4.18) and improved separation of diagnostic classes (Silhouette Score 0.38). b Schematic of the site-preserved cross-validation setup, defining IND test sets and OOD test sets. c Performance comparison in terms of AUROC across three major task categories and two external datasets (CPTAC, NFH). Red represent mean AUROC for the Original (O), Reinhard-normalized (R), and FLEX (F) models. P-values indicate the statistical significance of the improvement of the over the

best-performing baseline (O or R), calculated using a two-sided paired t-test on the results from 15 cross-validation folds across all tasks within each category (P = 2.688 \times 10^{-10} for OOD and P = 0.003 for IND in morphology classification; P = 3.305 \times 10^{-12} for OOD and P = 0.001 for IND in molecular biomarker prediction; P = 1.010 \times 10^{-10} for OOD and P = 5.764 \times 10^{-10} for IND in gene mutation prediction; P = 9.432 \times 10^{-16} for CPTAC and P = 8.900 \times 10^{-15} for NFH in external validation). d Radar plots comparing model performance (AUROC) on individual tasks for TCGA OOD testing (left) and IND testing (right). e Radar plot of model performance on external validation datasets (CPTAC and NFH). For (d) and (e), asterisks indicate the statistical significance of FLEX compared to the best-performing baseline for each specific task, determined by a two-sided paired t-test across 15 folds (P < 0.05, ^*P < 0.01, ^{**}P < 0.001). f Qualitative examples of attention maps on representative WSI for BRCA-type and STAD-MSI tasks. The color bar indicates attention value. WSI images were obtained from the TCGA gene mutation. Source data are provided as a Source Data file.

Nature Communications | (2025)16:11485

4

---

<!-- Page 5 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

In contrast, FLEX is designed to address a broader spectrum of site-specific signatures, including not only staining variations but also subtle variations from tissue overexpression and scanner artifacts, through its knowledge-guided information bottleneck. When applied within the TCGA cross-validation, FLEX significantly improved model generalizability for both IND and OOD testing (Fig. 2). Specifically, the average OOD AUROC increased by 6.43%, 7.21%, and 4.94% for the three task categories, substantially narrowing the IND-OOD performance gap. UMAP visualizations for the BRCA-TYPE task (Fig. 2a, left panel) further confirmed that FLEX effectively suppressed site-specific features, forcing the model to focus on biologically relevant cohorts rather than their site of origin. Detailed results across all 16 tasks (see ‘Dataset and clinical tasks description’ in ‘Methods’ and Supplementary Table 2) show consistent performance improvements in both IND and OOD settings (Fig. 3). Overall, FLEX outperforms cohorts without OOD AUROC for the STAD-LAUREN task, reducing the IND-OOD gap from 20.59% to 8.64%. This highlights FLEX’s potential to address key bottlenecks in cross-domain generalization.

Furthermore, we conducted a zero-shot evaluation on two independent external cohorts: the public CPTAC dataset and our in-house NFH dataset (see Supplementary Tables 3, 4). Model-trained exclusively on TCGA were unable to generalize to these external cohorts without any fine-tuning. These datasets introduce unique site-specific signatures distinct from TCGA, representing a true out-of-distribution challenge. Across all tasks and both cohorts, the baseline model’s performance was markedly inferior to FLEX, which demonstrated consistent and significant performance uplift, demonstrating its ability to generalize to new clinical environments. The average AUROC for the CPTAC zero-shot improvement was 1.09% (0.8900 × 103), as shown in Fig. 2c. The radar plot in Fig. 2e provides a comprehensive overview, showing that FLEX (pink line) consistently improves performance. Similar results for the NFH dataset are shown in Supplementary Tables 3, 4. These analyses indicate that FLEX learns transferable biological representations rather than memorizing source-domain shortcuts.

Finally, to provide additional insights into FLEX’s mechanism, we visualized attention maps from the ABMIL models (Fig. 2f). Here, noisy regions are defined as visual information irrelevant to the diagnostic task, such as processing artifacts or task-agnostic biological structures (e.g., non-proliferative stroma). The CPTAC-TYPE task (Fig. 2f, top panel), the baseline model’s attention is diffuse, scattered across tumor cells and distracting noisy elements. In contrast, the model with FLEX is tightly focused on the tumor cells, with minimal attention to irregular glandular and ductal formations characteristic of invasive Ductal Carcinoma (IDC) without being distracted by noisy foreground elements. This focused attention provides an intuitive explanation for the quantitative performance gains. Similarly, for the STAD-MSI task, the FLEX-enhanced model successfully identified potential Micro-satellite Instability-High (MSI-H) regions, where tumor cells exhibit greater heterogeneity, whereas the baseline model failed to do so, suggesting incorrect predictions. This suggests that FLEX enhances the model’s focus on salient pathological patterns while suppressing task-agnostic information.

### FLEX effectively improves demographic fairness

Demographic biases within large-scale datasets like the TCGA dataset exacerbate fairness concerns, leading to significant performance disparities in deep learning models, particularly among underrepresented populations from minority demographics31. Because self-reported race may not fully capture complex biological heritage, we also stratified cohorts by genetic ancestry32, which provides a more biologically grounded definition of race. FLEX was conducted across both stratification methods in the TCGA dataset to ensure a comprehensive evaluation. Additionally, we performed a zero-shot

fairness evaluation on the CPTAC dataset, which contains only self-reported race. As baseline experiments confirm (Fig. 3b, c), models trained on original features exhibit notable performance disparities across both stratification methods. Simple stain normalization, while useful for reducing inter-site staining variations, does not effectively address these demographic biases.

By addressing this critical limitation through feature disentanglement, FLEX offers a significant improvement in both demographic fairness and model reliability. We evaluated this using a multi-faceted approach, assessing performance across both self-reported race and genetic ancestry. The results in Supplementary Fig. 3b show that within individual clinical sites (Supplementary Fig. 3).

First, we examine the Fairness Gap (AUROC gap ratio)33 (in Fig. 3a, which measures the absolute performance difference between the best- and worst-performing racial groups relative to the overall AUROC. On average, FLEX consistently reduces the fairness gap across tasks. For instance, in the NSCLC-TYPE task, FLEX reduces the mean fairness gap from 0.041 (0.041) to 0.016 (0.016) (0.041) (0.041) (from 0.062 to 0.040). For the external CPTAC cohort, the fairness gap for the C-BRCA-TYPE and C-UAD-EGFR tasks decreased from 0.287 and 0.494 to 0.245 and 0.246, respectively. The scatter plots and marginal distributions in Supplementary Fig. 3c show that FLEX’s results are more tightly clustered at lower gap values, indicating improved fairness. Even in cases like CRC-BRAF where an outlier widens the confidence interval, the central tendency of FLEX’s performance remains stable.

For a more robust assessment of model reliability, we analyzed the True Positive Rate (TPR) disparity34 (Fig. 3c), which quantifies the difference in TPR between the best- and worst-performing racial groups overall. The violin plots for FLEX are consistently narrower and more centered around the zero-disparity line for both self-reported race and ancestry stratifications, demonstrating that the model applies its improvements across all groups. This is quantitatively supported by the TPR disparity RMSE values (Fig. 3d). In the challenging C-UAD-EGFR task, for example, FLEX reduces the average RMSE from 0.140 to 0.085, indicating a substantial improvement in fairness. Similarly, for the C-BRCA-TYPE task, Supplementary Fig. 3b show that FLEX yields tighter and more equitable performance curves.

### FLEX is versatile across different pathology VLMs

To further evaluate the effectiveness and adaptability of FLEX across different pathology VLMs, we integrated it with three state-of-the-art pathology VLMs (CONCH35, PathGenCLIP36, and QuliNet37), which are based on the same architecture. We evaluated ABMIL as the down-stream MLL framework, we tested performance on 6 pathology tasks, focusing on the OOD generalization setting.

The results show that FLEX consistently and significantly enhances performance across all three foundational VLMs (Fig. 4a). While the baseline performance varies between VLMs, applying FLEX delivers a robust improvement in nearly all scenarios. For CONCH, FLEX improved OOD performance in all 16 tasks, with significant improvement in 0–10% observed in 14 out of 16 tasks. For PathGenCLIP, FLEX improved performance in all tasks, with significant improvement in 9 out of 16 tasks. For QuliNet, performance improved in 14 out of 16 tasks. These results demonstrate that FLEX is a model-agnostic solution for improving generalization. The varying magnitude of improvement may be attributed to differences in the expressivity and discriminative power of the underlying VLMs, as well as differences in the VLMs. Since FLEX relies on visual and textual knowledge as guidance to enhance the patch features, the quality of this guidance depends on the features extracted by the VLMs. Visual knowledge and textual knowledge are complementary, and the patch image embedding prompts with the image and text encoders of the pathology VLMs. If the VLMs lack expressivity and discriminability, the resulting visual and

Nature Communications | (2025)16:11445

5

---

<!-- Page 6 -->

Article

https://doi.org/10.1038/s41467-025-66330-y

a Fairness gap

| Model | Method | AUROC per ratio | AUROC |
| --- | --- | --- | --- |
| NCDL-TYPE | Original | ~0.35 | ~0.35 |
| NCDL-TYPE | Reimhard | ~0.35 | ~0.35 |
| NCDL-TYPE | FLEX | ~0.35 | ~0.35 |

b Group-wise AUROC

| Model | Method | AUROC |
| --- | --- | --- |
| NCDL-TYPE | Original | ~0.85 |
| NCDL-TYPE | Reimhard | ~0.85 |
| NCDL-TYPE | FLEX | ~0.85 |

c TPR disparity

| Model | Method | TPR disparity | P-value |
| --- | --- | --- | --- |
| NCDL-TYPE | Original | ~0.2 | P=0.001 |
| NCDL-TYPE | Reimhard | ~0.2 | P=0.001 |
| NCDL-TYPE | FLEX | ~0.2 | P=0.001 |

d TPR disparity RMSE

| Model | Method | O | R | F |
| --- | --- | --- | --- | --- |
| NCDL-TYPE | Race EU | 0.001 | 0.070 | 0.075 |
| NCDL-TYPE | Race LUAD | 0.001 | 0.105 | 0.062 |
| NCDL-TYPE | Race LSC | 0.001 | 0.111 | 0.070 |
| NCDL-TYPE | Ancestry EU | 0.004 | 0.079 | 0.079 |
| NCDL-TYPE | Ancestry LUAD | 0.027 | 0.102 | 0.027 |
| NCDL-TYPE | Ancestry LSC | 0.027 | 0.102 | 0.027 |
| **Average** |   | 0.008 | 0.090 | 0.008 |

textual knowledge may be less informative and discriminative, limiting the performance improvement achieved by FLEX.

We further analyzed the mechanism behind this improvement by visualizing the patch feature space for the STAD-BV task using UMAP30 (Fig. 4b). For all three VLMs, the original features show strong clustering by site, with poor separation between BV+ positive and BV- negative classes. This is confirmed by low Local Inverse Simpson's Index (LISI) scores, which measure local data mixing by site, and Silhouette Scores, which measure class separability. After applying FLEX, the feature distributions become more uniform, with site-specific clusters dissolving. This is validated by a significant increase in the LISI score for all three VLMs (e.g., from 2.22 to 3.22 for CONCH), indicating

better integration of features from different sites. Concurrently, the separation between BV classes improves, which affected the LISI score in the Silhouette Score (e.g., from 0.09 to 0.24 for CONCH). These results demonstrate that FLEX mitigates site-specific biases while enhancing the discriminability of task-relevant biological features, a dual benefit that holds across different foundational models.

FLEX is effective with different sizes of training data and flexible with different MLL models

To evaluate the scalability of FLEX with varying training data scales, we conducted additional experiments on the RBCA cohort. The experimental design is illustrated in Fig. 5a. The dataset was partitioned into

---

<!-- Page 7 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

Fig. 3 | Evaluation of FLEX's effectiveness in improving performance. The top three rows (NSCLC-PRCA, BRCA, CRC-BRMA) show fairness when evaluated across self-reported race and ethnicity groups using results from 15-fold 5D-MCV on the TGA-NSCLC (n = 958), TGA-BRCA (n = 937), and TGA-CRC (n = 660) datasets. The remaining two bottom rows (CRCA-CTLA4, CRCA-CTLA4 with self-reported race and ethnicity groups using results from 15-fold 5D-MCV on CPTAC-BRCA (n = 323) and CPTAC-LUAD (n = 815)). For each cross-validation fold, metrics for each demographic-label group were estimated via bootstrapping (see Supplementary Fig. 1). The bottom row shows the linear regression slope ratio in the performance difference between the best- and worst-performing subgroups relative to the overall AUCROC. Smaller dots represent individual folds. Bars indicate size with error bars showing the standard deviation. The bottom row distributions show the distribution of AUCROC gap ratios across folds. Presented P values are from a two-sided Wilcoxon signed-rank test without adjustment, comparing FLEX to the Original Model (P = 0.026 when evaluated on ancestry, for

NSCLC-CTE; P = 0.018 when evaluated on self-reported race for BRCA-PR; P = 0.048 for CRCA-CTLA4; P = 0.004 for CLUAD-EGFR); b AUCROC distribution across subgroups. Bars show the distribution across n = 15 cross-validation folds. The center line represents the median (50th percentile), the box bounds represent the interquartile range (IQR, 25th to 75th percentile), and the whiskers extend to data points within 1.5 times the interquartile range (IQR) and whiskers extending from 1.5x IQR. Distributions centered closer to the zero-disparity line indicate higher fairness. Presented P values are from a two-sided Wilcoxon signed-rank test without adjustment, comparing FLEX to the Original Model across the three methods. d Quantitative summary of TPR disparity, showing the Root Mean Square Error (RMSE) of Original (o), Reinhard (r), and FLEX (f). Lower values indicate better fairness. Source data are provided as a Source Data file.

five site-preserved outer folds, with one fold held out at the OOD test set in each of five outer loop iterations. Training sets of increasing size (1, 2, 3, and 4 folds) were constructed from the remaining four folds to create a learning curve. Three inner MCV runs were performed for each fold to ensure stability. For this analysis, three tasks spanning different domains were selected: BRCA-CTE, BRCA-HER2, and BRCA-PIK3CA. The corresponding training and OOD test set sizes are in Supplementary Table 7. The results shown in Fig. 3b demonstrate that FLEX generally outperforms the Original Model in terms of performance across all tasks and data scales, underlining its ability to generalize effectively even with larger training datasets.

Next, we assessed the performance of FLEX across all MLL models, we integrated it with five state-of-the-art MLL architectures: ABM152, CLAM-SB53, ACML54, DTED-MLI55, and IRLA-MIL56. As shown in Fig. 5c, FLEX consistently improved OOD performance across all models. The average OOD performance gains were 6.05%, 5.55%, 3.52%, 3.93%, and 6.06%, respectively. Additionally, FLEX significantly reduced the performance gap between IND and OOD testing. Specifically, the gap decreased from 0.034, 0.040, 0.041, 0.038, and 0.035 to 0.022, 0.024, 0.023, 0.020, and 0.019, respectively. FLEX also reduced the per-task performance metrics for all combinations of VLM and MLL models evaluated are provided in Supplementary Tables 8–23.

The performance improvement seen in Fig. 5c varies across the 16 pathology tasks due to the varying complexity of each task. The utility of feature refinement for a given task, and the complexity of the MLL model. First, inherent task difficulty sets the upper bound on performance; for example, morphology classification tasks consistently yield higher AUCROCs than most gene mutation prediction tasks. Second, the magnitude of improvement from FLEX depends on task-specific conditions. In the STAD-LAUREN task, for instance, all MLL models show a substantial performance gain. This may be because the TCGA-STAD cohort is relatively small, causing baseline models to overfit to noisy features. FLEX's core mechanism—refining features by filtering task-relevant information—improves the signal-to-noise ratio, which is particularly beneficial when training data is limited. Third, performance gains are more pronounced with simpler MLL models like ABM1 and CLAM-SB compared to more complex architectures like hypernetworks and VLMs. The more complex models like FLEX and the MLL model. A simpler MLL backbone may create a more stable learning environment, allowing gradients to effectively guide the feature refinement process within FLEX. In contrast, with more intricate models, models may struggle with conflicting or interacting components can complicate convergence to an optimal state, potentially limiting the observable performance gain from FLEX.

## Discussion

Foundation models in computational pathology have rapidly advanced, demonstrating impressive capabilities in histopathology

images understanding. Their integration into weakly supervised computational pathology pipelines has yielded strong performance across diverse diagnostic tasks12,13. Despite this progress, significant challenges remain. These include limitations in cross-domain generalization, demographic fairness, and the practical adaptation of these powerful models for specific diagnostic objectives. Our study undertakes a comprehensive analysis and proposes an effective solution to address these critical challenges of cross-domain generalization and demographic fairness. In this cross-domain generalization and demographic systematic investigation, we identified the detrimental impact of site-specific signatures and demographic biases inherent in pathology VLMs. These biases, stemming from the development of FLEX, an approach engineered to enhance both generalization capacity and fairness across a spectrum of diagnostic tasks.

Our investigation yielded key insights into the nature of these challenges. UMAP visualizations of feature embeddings from FLEX, coupled with the stark performance decline observed in OOD testing, clearly demonstrated the presence of site-specific signatures impeding cross-site generalization. Furthermore, our fairness gap analysis revealed that FLEX, despite its demographic awareness, still compellingly highlighted inherent biases within current pathology foundation models. Crucially, we demonstrated that standard stain normalization is insufficient to mitigate these deeper biases. It particularly addresses pixel-level color variations and fails to account for the broader spectrum of site-specific signatures, including subtle variations from tissue preparation and scanner artifacts. To overcome these challenges, we propose a two-pronged approach: teaching the visual and textual prior knowledge to strategically suppresses site-specific patterns and demographic bias while amplifying task-relevant feature discriminability, thereby facilitating effective task-specific adaptation. Visual concepts, consisting of representative patch images for target classes (Supplementary Fig. 4), guide the retrieval of task-relevant patches from WSI, facilitating information bottleneck training. Complementing visual concepts, we incorporated domain expertise to create learnable textual concepts. These textual concepts guide an information bottleneck mechanism within FLEX. This mechanism enhances task-related information within patch features and guides the model to focus on learning out-of-domain task-specific biasing information. This ultimately leads to significant improvements in both cross-site generalization and demographic fairness. The ablation study on visual prompts and textual prompt length is presented in Supplementary Fig. 5.

FLEX represents a significant step in adapting foundation models for computational pathology. It effectively mitigates the negative impacts of site-specific signatures and demographic biases while maintaining the core strengths of foundation models. The core mechanism of FLEX uses an information bottleneck guided by textual pathological concepts to disentangle task-relevant features from

Nature Communications | (2025)16:11485

7

---

<!-- Page 8 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

a

Different pathology VLMs

Overall

BRCA-TYPE NSCLC-TYPE STAD-LAUREN BRCA-HER2

BRCA-ER BRCA-PR STAD-EBV STAD-MSI BRCA-PJ3C4 BRCA-COH1

LIAD-EGFR LIAD-STK11 STAD-TPS3 STAD-MUC16 CRC-BRAF CRC-TPS3

b

CONCH UMAP visualization PathGen-CLIP QuilNet

Original FLEX

EBV Positive EBV Negative

Fig. 4 | Performance evaluation of FLEX when incorporated with different pathology VLMs. a Comparison of AUROC performance between original pathology vision-language models (VLMs) and their counterparts enhanced with FLEX. The 16 tasks span four datasets: TCGA-BRCA (n = 937), TCGA-NSCLC (n = 958), TCGA-STAD (n = 414), and TCGA-CRC (n = 606). Each box plot summarizes results from n = 15 independent cross-validation folds derived from SP-MCVC. Box plots display the median (center line), interquartile range (IQR; box limits from 25th to 75th percentiles), and whiskers extending to 1.5 \times IQR; individual data points for each fold are overlaid. Indicated P-values were calculated using a

two-sided paired-samples t-test with multiple hypothesis correction. C, P, and Q correspond to CONCH, PathGen-CLIP, and QuilNet, respectively. b UMAP visualizations illustrating the effect of FLEX on the patch feature space for the STAD-EBV task. For each VLM, parallel subplots are colored by site (left) to visualize batch effect mitigation, and by EBV status (right) to visualize class separability. The LSI for site integration (higher is better) and the Silhouette Score for class separation (higher is better) provide quantitative evidence. The visualizations and scores demonstrate that FLEX reduces site-specific clustering while improving the discriminability of task-relevant classes. Source data are provided as a Source Data file.

Nature Communications | (2025)16:11485

8

---

<!-- Page 9 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

a Different scales of training data

Site-preserved Split

Outer Fold1: 1 IND Split, 2 IND Splits, 3 IND Splits, 4 IND Splits, 1 OOD Split

Outer Fold2: IND Splits, OOD Split

Outer Fold3: IND Splits, OOD Split

Legend: Label A (dark grey), Label B (light grey)

b

BRCA-TYPE: P = 0.001, P = 0.004, P = 0.002, P = 0.003

BRCA-HER2: P = 0.001, P = 0.022, P = 0.019, P = 0.005

BRCA-PWCA: P = 0.020, P = 0.002, P = 0.001, P = 0.001

AUCROC vs. Number of IND Splits (1, 2, 3, 4)

Legend: FLEX (pink), Original (blue)

c Different MIL models

AUCROC vs. Number of IND Splits (1, 2, 3, 4)

Legend: ABML, ACML, CLAM-SB, DTTM-MIL, EDN-MIL, Original, FLEX

Significance levels (P) for each task: ABML, ACML, CLAM-SB, DTTM-MIL, EDN-MIL, Original, FLEX.

Tasks: BRCA-TYPE, NSCLC-TYPE, STAD-ALPHA, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER2, BRCA-HER

---

<!-- Page 10 -->

Article

https://doi.org/10.1371/journal.pmed.0266300-y

spurious variations. Because these textual concepts are inherently free of site or demographic information, this process forces the model to extract extraneous signals, including complex site and demographic signatures. The efficacy of FLEX was validated through extensive evaluations across 16 pathology tasks, using various pathology VLMs and MIL frameworks. These consistent results, obtained via a step-preserved cross-validation strategy and supported by fairness analyses, underscore the method's robustness. Beyond performance improvements, FLEX offers insights into the strategic use of multi-modal prior knowledge for task-specific adaptation of foundation models, contributing to the development of more effective and equitable diagnostic tools.

While FLEX leverages the inherent alignment between visual and textual embedding spaces of pathology VLMs, its current reliance on textual-only limits its applicability to tasks requiring cross-modal interaction. To address this, future work could explore cross-modal distillation techniques or develop a vision-only adaptation module, enabling FLEX to operate as a broader range of architectures. Moreover, the current FLEX is primarily optimized for classification tasks, such as cancer subtyping and biomarker prediction. However, complex diagnostic tasks like prognosis in computational pathology are crucial for personalized medicine and pathobiology research. To address this, we may extend FLEX to incorporate prognostic-specific textual prompts to guide the model towards relevant features for predicting patient outcomes. Future research will focus on expanding FLEX's versatility. Key areas include: 1) exploring the model's applicability to foundation models and extending its application to a wider range of tasks, including regression and prognosis. We will also explore its integration with vision-language models for tasks requiring multimodal interpretability and adaptability of these models. This effort includes the quantitative validation of attention mechanisms against expert-annotated regions by pathologists, which would provide an objective confirmation of the model's focus. Such work will be crucial for translating these advancements into clinically impactful and trustworthy tools.

## Methods

This retrospective study was conducted in compliance with all relevant ethical regulations. The research utilized publicly accessible data from the TCGA and the CPTAC cohorts, which were originally collected under approved protocols and informed consent from all participants. Information regarding participant compensation for these public cohorts was not available to the authors. The in-house NHF dataset was collected with the informed approval of the Medical Ethics Committee of Nanfang Hospital of Southern Medical University (approval number: NFE-C-2025-419), which granted a waiver of informed consent due to the retrospective nature of the study and the use of de-identified data, posing minimal risk to participants. No compensation was provided for the retrospective collection of NHF data. All data were handled with a strict commitment to patient privacy, fairness, and transparency.

The demographic characteristics of the patient cohorts, including sex and age, are detailed in the subsequent dataset descriptions. For all cohorts, participant sex and race were determined from self-reported information available in the pathology reports. The TCGA cohort ancestry was derived from genomic data as established by the TCGA Pan-Cancer Atlas project42. Patient sex was not considered in the study design. Our fairness analysis focused primarily on self-reported race and gender ancestry to directly address significant disparities previously reported in the literature for these groups in computational pathology.

### Dataset and clinical tasks description

This study utilized datasets from the TCGA cohort, including data from breast invasive carcinoma (BRCA), non-small cell lung cancer (NSCLC,

encompassing lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (USC), stomach adenocarcinoma (STAD), and colorectal carcinoma (CRC), endometrial cancer, adenocarcinoma (AD), and rectum adenocarcinoma (READ). The original WSIs were collected from the publicly available TCGA program (https://www.cancer.gov/cg/research/genome-sequencing/tcga), and corresponding clinical, molecular, and gene mutation information was obtained from the cBioPortal database (https://www.cbioportal.org). In this study, we conducted 16 WSI analysis tasks to comprehensively evaluate the effectiveness of FLEX across different task types. These tasks include: three-class classification across three organs, three organ-specific cellular biomarker status prediction tasks across two organs, and eight gene mutation prediction tasks across four organs. This diverse range of tasks ensures a robust assessment of FLEX in various computational pathology applications. A detailed breakdown of patient and cohort counts for each task in the TCGA cohort is provided in Supplementary Table 2.

The demographic and clinical characteristics of the primary TCGA cohorts are as follows: the TCGA-BRCA cohort included 876 female (98.8%) and 11 male (1.2%) patients, with a median age of 58 years (range: 26–90). The TCGA-NSCLC cohort comprised 341 female (40.4%) and 503 male (59.6%) patients, with a median age of 67 years (range: 30–90). The TCGA-STAD cohort included 132 female (34.0%) and 256 male (66.0%) patients, with a median age of 67 years (range: 30–90). The TCGA-CRC cohort consisted of 225 female (48.2%) and 296 male (51.8%) patients, with a median age of 67 years (range: 31–90).

Morphology classification. For the morphology classification tasks, we used the same demographic and histopathology images into distinct subtypes of the same cancer type:

- • BRCA-TYPE: This binary classification task involves classifying histopathology images from the TCGA-BRCA cohort into invasive carcinoma (1) and non-invasive carcinoma (0).
- • NSCLC-TYPE: This two-class classification task categorizes histopathology images from the TCGA-NSCLC cohort into lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (USC).
- • STAD-LAUREN: This task focuses on the Lauren classification of histopathology images from the TCGA-STAD cohort, distinguishing between the intestinal type and diffuse type43.

Molecular biomarker status prediction. The molecular biomarker status prediction tasks aim to identify clinically relevant biomarker status from histopathology images, leveraging specific morphological correlations:

- • BRCA-HER2, BRCA-ER, and BRCA-PR: These binary classification tasks predict the human epidermal growth factor receptor 2 (HER2), estrogen receptor (ER), and progesterone receptor (PR) statuses of breast cancer using histopathology images from the TCGA-BRCA cohort44–47.
- • STAD-EBV and STAD-MSI: These binary classification tasks predict the Epstein-Barr virus (EBV) and Microsatellite Instability (MSI) statuses of stomach cancer using histopathology images from the TCGA-STAD cohort48,49.

Gene mutation prediction. Gene mutation prediction tasks aim to predict the mutation status of specific genes in cancer using histopathology images. In this study, the following binary classification tasks were conducted:

- • BRCA-PKMC3 and BRCA-CDH1: These tasks predict the PKMC3 and CDH1 gene mutation statuses in breast cancer using histopathology images from the TCGA-BRCA cohort50,51.
- • STAD-EGFR and LUAD-TP53: These tasks predict the EGFR and STKJ1 gene mutation statuses in lung adenocarcinoma using histopathology images from the TCGA-LUAD cohort52,53.

Nature Communications | (2025)16:11485

10

---

<!-- Page 11 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

- • STAD-TP53 and STAD-MUC6/C6: These tasks predict the TP53 and MUC6 gene mutation statuses in stomach adenocarcinoma using histopathology images from the TCGA cohort under NFH.
- • CRC-BRAF and CRC-TP53: These tasks predict the BRAF and TP53 gene mutation statuses in colorectal carcinoma using histopathology images from the TCGA-CRC cohort6,59.

By targeting tasks of varying complexity and clinical significance, we aimed to comprehensively assess the effectiveness of FLEX across a diverse range of WSI analysis applications.

## External Validation Datasets

To evaluate the zero-shot generalization capability of models trained on TCGA, we used two independent external cohorts for testing: the overall CPTAC dataset and a large in-house STAD cohort. These datasets introduce significant domain shifts, including different patient populations, slide preparation protocols, and scanning equipment, providing a more realistic test of real-world applicability. Detailed statistics for the tasks performed on these external cohorts are available in Supplementary Table 3 for CPTAC and Supplementary Table 4 for NFH. The specific tasks for external validation were selected based on data availability and their overlap with the TCGA tasks.

CPTAC Dataset. The CPTAC collections are a publicly available resource (https://portal.gdc.cancer.gov/projects/CPTAC-2, https://portal.gdc.cancer.gov/projects/CPTAC-3) that includes proteomic data along with corresponding WSIs. For our external validation, we selected a subset of tasks that mirror those in our primary TCGA cohort. The CPTAC STAD cohort was used in this study were as follows: the CPTAC-BRCA cohort included 116 female patients with a median age of 59 years (range: 30–89). The CPTAC-NSCLC cohort included 82 female (30.9%) and 183 male (69.1%) patients with a median age of 65 years (range: 36–88). The CPTAC-COAD cohort consisted of 61 female (58.7%) and 43 male (41.4%) patients with a median age of 65 years (range: 35–93). The specific tasks covered three cancer types.

- • BRCA: C-BRCA-TYPE, C-BRCA-PIK3CA, C-BRCA-CODH: Including subtype classification (IDC vs. ILC) and prediction of PIK3CA and CDHI gene mutations using histopathology images from the CPTAC-BRCA cohort.
- • NSCLC: C-NSCLC-TYPE, C-UADU-EGRF, C-UADU-STK11: Including subtype classification between UADU and LUSD, and prediction of EGRF and STK11 gene mutations in LUAD using histopathology images from the CPTAC-NSCLC cohort.
- • COAD: C-COAD-BRAF, C-COAD-TP53: Including prediction of BRAF and TP53 gene mutations in COAD using histopathology images from the CPTAC-COAD cohort.

Nanfang Hospital of Southern Medical University (NFH) in-house Dataset. The NFH dataset is a large-scale, retrospectively collected in-house cohort from Nanfang Hospital of Southern Medical University, Guangzhou, China. The NFH STAD cohort contains 37,636 WSIs to its distinct technical and demographic characteristics compared to the Western-centric TCGA cohort. The demographic breakdown for the cohort is as follows: 26,161 (69.6%) patients with a median age of 76.1 years (99.9%) and 1 male (0.1%) patient, with a median age of 52 years (range: 17–89). The NFH-NSCLC cohort included 910 female (46.7%) and 1037 male (53.3%) patients with a median age of 59 years (range: 24–87). The NFH-BRCA cohort contained 1,040 patients with 249 male (63.0%) patients with a median age of 60 years (range: 20–89). The NFH-CRC cohort included 482 female (41.6%) and 678 male (58.4%) patients with a median age of 62 years (range: 21–93). The additional tasks on the in-house cohort cover four major cancer types: • BRCA (N-BRCA-TYPE, N-BRCA-HER2, N-BRCA-ER, N-BRCA-PR): Including subtype classification (IDC vs. ILC) and prediction of

HER2, ER, and PR biomarker statuses using histopathology images from the NFH-BRCA cohort.

• NSCLC: C-NSCLC-TYPE, N-UADU-EGRF: Subtype classification between LUAD and LUSD and prediction of EGRF gene mutation status in LUAD using histopathology images from the NFH-NSCLC cohort.

• STAD: C-STAD-LAUREN: Lauren classification between Intestinal and Diffuse type in STAD using histopathology images from the NFH-STAD cohort.

• CRC (N-CRC-BRAF): Prediction of BRAF gene mutation status in CRC using histopathology images from the NFH-CRC cohort.

By evaluating model performance on these diverse external datasets without any fine-tuning, we assess the effectiveness of FLEX in overcoming domain-specific biases and generalizing to unseen clinical environments.

## Preprocessing of histopathology images

Segmentation and patching. We adopted the preprocessing steps outlined in CLAM7, which involve segmenting and cropping tissue regions from each WSI and extracting instance features from each patch using a feature extractor. Specifically, each WSI is first loaded into memory at a downscaled resolution (i.e., 32 × downscale) and converted from RGB to HSV color space to facilitate tissue segmentation. A binary mask for the foreground is then computed by thresholding the histology channel after applying median blurring to smooth edges. Morphological closing operations are subsequently performed to fill small gaps and holes within the tissue regions. The segmented tissue regions are further cropped into 212 × 512 patches within the foreground contours at 20 × magnification for each slide.

Feature extraction. Due to the potentially vast size of the patch bag for each WSI (e.g., exceeding 10,000 patches), each patch was transformed into a compact feature representation using the pretrained feature extractor neural network. In this study, the feature extractor was implemented using the ViT backbone of pathology VLMs, including CONCH4, PathGen-CLIP8, and QiniNet11.

Slide normalization. For slide normalization, we employed the Reinhard method60 and the Macenko normalization61 to standardize the color distribution of the histopathology images. For implementation, we utilized the torch-standard package for efficient normalization (https://github.com/CeLA/torch-standardols).

## Pathology vision-language foundation models

With the advancement of large-scale pre-trained VLMs in computer vision and natural language processing, several pathology-specific VLMs have been developed to integrate histopathology images and textual concepts. Compared to vision-only foundation models, pathology VLMs better capture the intricate relationships between histopathology images and textual data. This alignment enhances the generalizability and robustness of image features62. The proposed FLEX is designed to seamlessly integrate the performance of VLMs in pathology, enabling the performance of WSI analysis tasks. In this study, we employed three state-of-the-art pathology VLMs:

CONCH4. CONCH is a visual-language foundation model pre-trained on over 1.17 million image-caption pairs, leveraging diverse histopathology images and biomedical text. It supports versatile applications in histopathology with minimal or no supervised fine-tuning, addressing the challenges of adapting adaptability across diseases and tasks. The CONCH model is publicly available on GitHub: https://github.com/mahmoodlab/CONCH.

Nature Communications | (2025)16:11485

11

---

<!-- Page 12 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

PathGen-CLIP®. PathGen-CLIP is a pathology-specific VLM trained using PathGen-1.6M®, a dataset containing 1.6 million high-quality image-caption pairs generated from large-scale WSI datasets such as TCGA. The PathGen-CLIP model is publicly available on GitHub: https://github.com/PathGen-1.6M/PathGen-1.6M.

QuiltNet®. QuiltNet is a visual-language model for histopathology trained on Quilt-IM®, a dataset of 1 million image-caption pairs curated from sources such as YouTube, Twitter, and research papers. QuiltNet is publicly available on GitHub: https://github.com/wisdommekogowo/quiltnet.

### Multiple instance learning methods

MIL®. is the predominant, widely supervised learning paradigm in computational pathology. In MIL, each WSI is treated as a bag of patch instances, and the models predict the bag-level label based on aggregated instance features. To demonstrate the adaptability and generalizability of FLEX, we integrated it with five state-of-the-art MIL methods in our experimental comparisons. The selected MIL methods are as follows:

ABMIL®. ABMIL models the Bernoulli distribution of a bag and parameterizes the aggregation operator using an attention mechanism. We used the original implementation available on GitHub: https://github.com/AMLab-Amsterdam/AttentionDeepMIL.

ACMIL®. ACMIL mitigates overfitting by introducing multi-batch attention and stochastic Top-k instance masking, addressing attention over-concentration. The original implementation was used from GitHub: https://github.com/dazhangyou22/ACMIL.

CLAM-SB®. CLAM-SB identifies diagnostically relevant sub-regions and refines the feature space through instance-level clustering of these regions. The implementation from the original GitHub repository was followed: https://github.com/mahmoodibad/CLAM.

DTFD-MIL®. DTFD-MIL addresses WSI classification challenges with small sample sizes by using pseudo-bags to expand training data and a double-tier MIL framework for better feature utilization. The original implementation was used from GitHub: https://github.com/hrzhang123/DTFD-MIL.

ILRA-MIL®. ILRA-MIL employs a low-rank constraint to group similar patches and separates different ones, utilizing low-rank latent vectors for efficient global interaction modeling. The original GitHub implementation was used: https://github.com/jimixiang/low_rank_wsi.

### Site-preserved Monte Carlo cross-validation

Histopathology images within the TCGA cohort originate from diverse source sites (e.g., hospitals, research institutions), often exhibiting site-specific features. To mitigate such biases, we induce models to learn spurious correlations, hindering their ability to generalize to new, unseen sites. To rigorously evaluate the generalizability and effectiveness of FLEX and other state-of-the-art MCCV strategies from novel source sites, we implemented an MCP-MCCV strategy. This approach is specifically designed to ensure models are tested on completely independent source sites not encountered during training, as illustrated in Fig. 2d. The proposed MCP-MCCV strategy is conceptually inspired by the Preserved-Site Cross-Validation method4 and includes outer and inner cross-validation loops.

Outer loop: site-preserved partitioning. Our strategy treats each Tissue Source Site (TSS) as an independent entity, representing a unique source of protocols and potentially biases. We do not group sites

based on known factors (e.g., scanner type), as this would fail to capture the full complexity of site-specific artifacts and would represent a lossy process for generalization. Also, we partition the entire pool of TSS codes (see https://gdc.cancer.gov/resources/tcga-users/tcga-code-tables/tissue-source-site-codes-for-site-TSS mapping) into K_t mutually exclusive site-folds using convex optimization to ensure that each site-fold contains a balanced proportion of patients from the diagnostic labels of interest4. In each outer loop of the cross-validation, one of these site-folds is designated as the IND dataset, while the remaining K_t - 1 site-folds are aggregated to form the OOD test set, simulating a deployment to unseen medical centers.

Inner fold: Monte Carlo cross-validation within IND dataset. Within each site-preserved outer loop, the IND dataset (comprised of all samples from a single TSS) is further partitioned into Validation (VAL) and Specifying, the IND data was randomly divided into training and IND test subsets at a 7/3 ratio. The OOD dataset from the held-out site-fold is used to evaluate and use exclusively for the final OOD performance evaluation.

This nested SP-MCCV procedure guarantees that model training and validation occur on data originating from distinct, site-specific datasets. For each iteration, we train the model, we encode K_t - 5 site-preserved splits, with each IND fold undergoing 3 MCCV iterations, resulting in a total of 15 evaluation folds. For datasets with fewer source sites and WSIs, we reduced K_t to 3 to maintain sufficient training data for validation, increasing MCCV iterations to 5 per IND fold, also yielding a total of 15 folds. This adjustment ensures robust statistical evaluation across datasets of varying sizes and site diversity. In summary, we train the model using 15 folds and conduct 15 rounds of evaluation of model performance, specifically across unseen source sites. By strictly separating training and testing data at the source site level, SP-MCCV allows for a robust and reliable assessment of FLEX's generalizability and effectiveness in mitigating site-specific biases.

### FLEX architecture

As illustrated in Fig. 1d, the proposed FLEX is a flexible and adaptable learning framework for histopathology, leveraging existing workflows for WSI analysis tasks. For clarity, we denote the input histopathology dataset as D = \{p_i, y_i\}, where P = \{p_1, p_2, \dots, p_n\} is a set of N patches cropped from the WSI and y is the corresponding label. The traditional WSI analysis pipeline comprises two stages: feature extraction and MIL-based classification. In the feature extraction stage, the image encoder E of pathology VLMs is employed to extract patch-level features X = \{x_1, x_2, \dots, x_n\}, where x_i is the extracted original patch-level features with dimension of D. In the MIL-based classification stage, MIL models aggregate the patch-level features into a comprehensive representation, upon which a classifier is trained to predict the bag-level label y = \text{CLS}(\text{MIL}(X)), where CLS and MIL are the classifier and the MIL model, respectively. The objective of FLEX is to enhance the original patch-level features X by leveraging the knowledge from visual concepts V and textual concepts T. This process filters out site-specific signatures and task-agnostic. The result, resulting in enhanced features that are subsequently fed into the MIL model for generalizable and robust WSI analysis. Z = \text{FLEX}(X, V, T). CLS and FLEX are the classifier and the MIL model, respectively. The patch-level features, each with a dimension of D. Specifically, the visual concepts V consist of representative patch images for the target class, which are used to retrieve important patches from the source sites to predict the bag-level label y = \text{CLS}(\text{MIL}(X)), where CLS and MIL are the classifier and the MIL model, respectively. The result, resulting in enhanced features that are subsequently fed into the MIL model for generalizable and robust WSI analysis.

Nature Communications | (2025) 16:11485

12

---

<!-- Page 13 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

a Visual Concept Generation

Q: Can I be deceived from this image? What features distinguish this image from the others? (invasive ductal carcinoma)

A: This image demonstrates strong histological features that could be indicative of Invasive Ductal Carcinoma.

Q: What types of tissue or cells are present in this whole image of breast tissue?

A: 1. Tumor Tissue2. Normal Breast Tissue

Visual Concept Generation process: Input images → GPT-4o (Task Prompt) → Representative Patch Image Candidates → Verification by Human Expert → Representative Patch Images → VLM Image Encoder → Visual Concepts (Class 1, Class 2).

b Textual Concept Generation

Representative Text Prompt: (Invasive ductal carcinoma) (Invasive breast tissue) (Normal breast tissue)

Textual Concept Generation process: Input text prompt → GPT-4o (Task Prompt) → Representative Text Prompts with Learned Context (Invasive ductal carcinoma) (Invasive breast tissue) (Normal breast tissue) → Verification by Human Expert → Textual Concepts (Class 1, Class 2) → Task-relevant.

c Architecture of FLEX

Inference Phase: Input images (Class 1, Class 2) → VLM Image Encoder → Task-related Information (Task-specific Signature, Task-specific Information) → Encoder → q(x|z) → MIL Model → Selected Top-k.

Training Phase: Textual Concept Guided Feature Calibration. Textual Concepts (Class 1, Class 2) → MIL Model → Textual Concepts. Arrows indicate Minimize Distance (red) and Maximize Distance (blue).

Visual Concept Guided Patch Selection: Visual Concept (Class 1) → Visual Concept Guided Patch Selection → Selected Top-k.

d Site-preserved Monte Carlo Cross-Validation

Outer Fold: Site-preserved Split (Site 1, Site 2, Site 3, Site 4, Site 5). Inner Fold: Random Split.

Validation Matrix:

| Outer Fold | Inner Fold | Training | IND Testing | OOD Testing |
| --- | --- | --- | --- | --- |
| 1 | 1 | IND | IND | IND |
| 1 | 2 | IND | IND | IND |
| 2 | 1 | IND | IND | IND |
| 2 | 2 | IND | IND | IND |

Legend: Label A (light blue), Label B (light green).

Visual concept generation. The process of visual concept generation is illustrated in Fig. 6a. First, an ABMIL model was trained on the training data, and patches with high attention scores were randomly selected from the training set. However, due to potential overfitting, these high-attention patches may not be representative of the target class. To mitigate this issue, a multimodal large language model (e.g., GPT-4o) was employed to filter out task-irrelevant and noisy patches. This was achieved by prompting GPT-4o with queries such as whether the input patch could reliably indicate its belonging to the target class.

This step served as a preliminary screening to identify representative patches. To further ensure task relevance, a human expert manually verified the selected patch candidates. Finally, the visual concept for each target class was generated by averaging the features of the selected patches, which were extracted using the image encoder of the pathology VLMs.

Textual concept generation. The process of textual concept generation is illustrated in Fig. 6b. It involves creating task-specific

Nature Communications | (2025)16:11485

13

---

<!-- Page 14 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

Fig. 6 | Overview of the proposed framework and experimental setup. A visual knowledge generation pipeline. This is a one-time offline procedure during training. ABM identifies high-frequency patches, followed by GPT-4o-based filtering, and human expert verification to select representative patches. Class-specific visual concepts are generated by averaging features from representative patches using the ABM-defined knowledge encoder. B pipeline for textual knowledge generation, also a one-time offline procedure. GPT-4o is prompted to create representative text prompts (both task-specific and task-agnostic). After expert verification, these prompts are extracted and stored. C pipeline for textual knowledge generation, also a one-time offline procedure. GPT-4o is prompted to create representative text prompts (both task-specific and task-agnostic). After expert verification, these prompts are extracted and stored. D pipeline for textual knowledge generation, also a one-time offline procedure. GPT-4o is prompted to create representative text prompts (both task-specific and task-agnostic). After the architecture of FLEX, during inference, original patch features are extracted by the VLM image encoder; a variational encoder then generates parameters for a Gaussian distribution for each patch, from

which enhanced features are sampled and aggregated by the MIL model. During training, a Visual Concept Guided Pilot Patch Selection module uses the pre-trained ABM to identify high-frequency patches for relevant enhanced features. These selected patches are then used in the Textual Concept Guided Feature Calibration process, where an InForce loss aligns the features with the textual concepts by minimizing the cosine similarity between the enhanced features and the variational posterior of FLEX. d Schematic of the SP-MCCW strategy. The dataset is non-negative, we have \hat{y} = \text{logit}(p(x|z)) and \hat{y} = \text{logit}(p(x|z)) for inference training and OOD test sets. Inner folds are then used to randomly split the training data for IND evaluation. Some illustrations were created by BioRender.com.

and task-agnostic prompts for each case as positive and negative supervision signals. Recognizing the need for accuracy in medical applications, our methodology incorporates an expert validation protocol. First, the generated prompts are compared to prompts from descriptive labels grounded in established oncologic terminology (e.g., “invasive ductal carcinoma”, “connective tissue”), which minimizes the risk of factual inaccuracies. Second, and most critically, as the impacts of other tissue types on loop export is unknown, we employ a process. All textual concepts, whether initially derived from established class names or drafted with assistance from GPT-4o, were rigorously reviewed, edited for clinical precision, and for readability, followed by expert verification. This two-step oversight ensures that every prompt used is medically accurate and relevant to the prediction task. The specific task-specific and task-agnostic prompts provided for each case type are detailed in Supplementary Tables 24–29. With these controls, prompts were defined as follows: for tasks with clear class boundaries, such as BRCA subtyping, task-specific prompts are the class names themselves, following previous studies22,23. However, for more complex tasks with vague class boundaries, high complexity, or limited data, class names alone may be insufficient. To address this, we propose using the same class names as task-specific prompts are attached to the original image. This enables us to effectively capture task-specific information from the images during training, enhancing the prompts’ effectiveness. Task-agnostic prompts consist of general descriptions irrelevant to the task, such as the names of other tissue types (e.g., “connective tissue” or “normal tissue”). These prompts guide the feature enhancement process to filter out task-agnostic information. These are generated by leveraging the embeddings of these prompts in filtering out irrelevant features. Finally, textual concepts are generated by averaging the embeddings of these prompts (with their learnable contexts) produced by the VLM’s text encoder.

Knowledge-guided feature enhancement. The feature enhancement process, illustrated in Fig. 6c, is guided by visual and textual knowledge and comprises three main steps: visual concept-guided pilot patch selection, textual concept-guided feature calibration, and feature enhancement using a variational information bottleneck. To enhance the original patch-level features, we leverage the information bottleneck, which filters out site-specific signatures and task-agnostic information while preserving task-related information. The information bottleneck principle seeks a compressed representation of the input data that maximizes the mutual information between the compressed representation and maximizes the mutual information between the compressed representation and the target output.

First, we crop patches from WSIs are processed through the frozen image encoder of the pathology VLMs to extract the original patch-level features \mathbf{X}. For each original feature \mathbf{x} and its corresponding

enhanced feature \mathbf{z}, we define the mutual information between them as:

I(\mathbf{x}, \mathbf{z}) = \int p(\mathbf{x}, \mathbf{z}) \log \frac{p(\mathbf{x}, \mathbf{z})}{p(\mathbf{x})} d\mathbf{x}, \quad (1)

= \int p(\mathbf{x}, \mathbf{z}) \log p(\mathbf{x}|\mathbf{z}) d\mathbf{x} - \int p(\mathbf{x}) \log p(\mathbf{x}, \mathbf{z}) d\mathbf{x}, \quad (2)

where p(\mathbf{x}, \mathbf{z}) represents the joint distribution of the original and enhanced features, p(\mathbf{x}) and p(\mathbf{x}, \mathbf{z}) are the marginal distributions, and p(\mathbf{x}|\mathbf{z}) is the conditional distribution of the enhanced features given the original features. However, the computing of p(\mathbf{z}) = p(\mathbf{x}|\mathbf{z})p(\mathbf{x}) is intractable. To address this issue, we let the Gaussian distribution of the enhanced features \mathbf{z}, p(\mathbf{z}), be a variational approximation of the true marginal distribution p(\mathbf{z}). Since the KL divergence between the variational posterior p(\mathbf{z}) and the true posterior p(\mathbf{z}) is non-negative, we have p(\mathbf{z}) \log p(\mathbf{z}) \leq p(\mathbf{x}) \log p(\mathbf{x}, \mathbf{z}). Therefore, we derive an upper bound for the mutual information: I(\mathbf{x}, \mathbf{z}) \leq I(\mathbf{x}, \mathbf{z}) + p(\mathbf{x}) \log \frac{p(\mathbf{x}, \mathbf{z})}{p(\mathbf{x})} d\mathbf{x}.

We further utilize a variational distribution q(\mathbf{z}|\mathbf{x}) to approximate the true posterior p(\mathbf{z}|\mathbf{x}), which was implemented by a neural network with the original features \mathbf{x} as input and the mean and variance of the Gaussian distribution of the enhanced features \mathbf{z} as output. After that, we can sample the enhanced features \mathbf{z} from the variational distribution: \mathbf{z} \sim N(\text{NN}^{\mathbf{x}}(\mathbf{x}), \text{NN}^{\mathbf{v}}(\mathbf{x})), where \text{NN}^{\mathbf{x}} and \text{NN}^{\mathbf{v}} are the neural networks for the mean and variance of the Gaussian distribution of the enhanced features, respectively, which enable flexible parameterization, we apply the reparameterization trick24, which provides an unbiased gradient estimate to optimize the objective25. Using this approach, the upper bound of the mutual information I(\mathbf{x}, \mathbf{z}) can be computed as: I(\mathbf{x}, \mathbf{z}) \leq p(\mathbf{x}) \log \frac{p(\mathbf{x}, \mathbf{z})}{p(\mathbf{x})} d\mathbf{x} = \mathbb{E}_{\mathbf{z} \sim q(\mathbf{z}|\mathbf{x})} [\log \frac{p(\mathbf{x}, \mathbf{z})}{p(\mathbf{x})}], which can be optimized by minimizing the Kullback-Leibler (KL) divergence between the variational posterior q(\mathbf{z}|\mathbf{x}) and the Gaussian distribution p(\mathbf{z}): \mathcal{L}_{KL} = \mathbb{E}_{\mathbf{z} \sim q(\mathbf{z}|\mathbf{x})} [\log p(\mathbf{z}|\mathbf{x})]. Traditionally, the mean and variance of mutual to guide the enhancement features and the target output is achieved by minimizing the cross-entropy loss between the bag-level predictions and the ground truth labels. However, we observed that supervised loss often fail to provide accurate supervision signals for optimizing the variational information bottleneck, which operates at the patch level. To address this challenge, we propose leveraging a variational information bottleneck to guide the feature enhancement process, offering more accurate patch-level supervision signals.

Specifically, as only a subset of patches contains task-related information, we select pilot patches \mathbf{z}^{\text{pilot}} to guide the feature enhancement process. We first identify the pilot patches by calculating the cosine similarity between the original patch features and the visual concept of the target class. Patches with high similarity scores are

Nature Communications | (2025)16:11485

14

---

<!-- Page 15 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

designated as pilot patches, ensuring they contain relevant task-related information to effectively drive feature refinement.

Following the selection of pilot patches, textual concepts are employed to guide the feature enhancement process. Given that the text encoder of pathology VLMs is inherently general due to pre-training on large-scale, diverse pathology datasets with domain-aggregated learning objectives, we post that textual concepts are robust and generalizable. These concepts can effectively filter out site-specific signatures, while task-specific textual concepts provide relevant information for the target class. This enables the enhancement process to preserve the task-related information and eliminate task-agnostic noise. Consequently, the task-specific textual concept for the target class is treated as the positive supervision signal \mathbf{c}_{\text{task}}, whereas other task-specific and task-agnostic textual concepts are treated as negative supervision signals \mathbf{c}_{\text{neg}}. To implement this guidance, we utilize the InfoNCE loss30, which minimizes the distance between the enhanced features and the positive supervision signal while maximizing the distance between the enhanced features and the negative supervision signals:

\mathcal{L}_{\text{InfoNCE}}^{\text{task}} = -\frac{1}{M} \sum_{j=1}^M \log \left( \frac{\exp \left( \frac{\mathbf{c}_{\text{task}}^T \mathbf{e}_{\text{task}}}{\tau} \right)}{\exp \left( \frac{\mathbf{c}_{\text{task}}^T \mathbf{e}_{\text{neg}}}{\tau} \right) + \sum_{k=1}^K \exp \left( \frac{\mathbf{c}_{\text{neg}}^T \mathbf{e}_{\text{neg}}}{\tau} \right)} \right) \quad (3)

where M represents the number of pilot patches, \mathbf{c}_{\text{task}} denotes the number of negative supervision signals, and \tau is the temperature parameter. To further enhance the distinction between task-specific textual concepts and task-agnostic concepts, we ensure task-specific textual concepts from different classes are more distinguishable, we propose an additional optimization strategy. In this approach, the corresponding task-specific textual concept of the target class serves as the optimization target, the other textual concepts are treated as positive samples, and the other task-specific textual concepts and task-agnostic textual concepts are treated as negative samples:

\mathcal{L}_{\text{InfoNCE}}^{\text{task}} = -\log \left( \frac{\exp \left( \frac{\mathbf{c}_{\text{task}}^T \mathbf{e}_{\text{task}}}{\tau} \right)}{\exp \left( \frac{\mathbf{c}_{\text{task}}^T \mathbf{e}_{\text{neg}}}{\tau} \right) + \sum_{k=1}^K \exp \left( \frac{\mathbf{c}_{\text{neg}}^T \mathbf{e}_{\text{neg}}}{\tau} \right)} \right) \quad (4)

The enhanced patch-level features are obtained by inputting the original patch-level features into the information bottleneck. These features are then aggregated by the MaxPool to produce the bag-level features, denoted as \mathbf{z}^{\text{bag}} \in \text{ML}(Z). Subsequently, we propose further enhancing the aggregated bag-level features through a contrastive learning process, leveraging the positive supervision signals \mathbf{c}_{\text{task}} and negative supervision signals \mathbf{c}_{\text{neg}}, similar to the feature enhancement process applied to the patch-level features. It is important to note that the textual concepts used for patch-level (\mathbf{c}_{\text{task}}^{\text{bag}} and \mathbf{c}_{\text{neg}}^{\text{bag}}) and slide-level (\mathbf{c}_{\text{task}}^{\text{slide}} and \mathbf{c}_{\text{neg}}^{\text{slide}}) feature enhancement share the same initialization but are optimized independently. The resulting InfoNCE losses for the slide-level feature enhancement are defined as:

\mathcal{L}_{\text{InfoNCE}}^{\text{task}} = -\log \left( \frac{\exp \left( \frac{\mathbf{c}_{\text{task}}^{\text{bag}} \mathbf{e}_{\text{task}}}{\tau} \right)}{\exp \left( \frac{\mathbf{c}_{\text{task}}^{\text{bag}} \mathbf{e}_{\text{neg}}}{\tau} \right) + \sum_{k=1}^K \exp \left( \frac{\mathbf{c}_{\text{neg}}^{\text{bag}} \mathbf{e}_{\text{neg}}}{\tau} \right)} \right) \quad (5)

\mathcal{L}_{\text{InfoNCE}}^{\text{task}} = -\log \left( \frac{\exp \left( \frac{\mathbf{c}_{\text{task}}^{\text{slide}} \mathbf{e}_{\text{task}}}{\tau} \right)}{\exp \left( \frac{\mathbf{c}_{\text{task}}^{\text{slide}} \mathbf{e}_{\text{neg}}}{\tau} \right) + \sum_{k=1}^K \exp \left( \frac{\mathbf{c}_{\text{neg}}^{\text{slide}} \mathbf{e}_{\text{neg}}}{\tau} \right)} \right) \quad (6)

The final prediction of the bag-level labels is obtained by feeding the enhanced bag-level features into the classifier y = \text{CLS}(z^{\text{bag}}). The

prediction loss is then optimized with the ground-truth label by minimizing the cross-entropy loss \mathcal{L}_{\text{CE}}.

\mathcal{L}_{\text{FLEX}} = \mathcal{L}_{\text{CE}} + \lambda_1 \mathbf{c}_{\text{B}} \mathbf{b}_{\text{B}} + \lambda_2 \mathbf{c}_{\text{S}} \mathbf{b}_{\text{S}} + \mathbf{c}_{\text{M}} \mathbf{b}_{\text{M}} + \lambda_3 (\mathbf{c}_{\text{TC}_1} \mathbf{b}_{\text{TC}_1} + \mathbf{c}_{\text{TC}_2} \mathbf{b}_{\text{TC}_2}) \quad (7)

where \lambda_1, \lambda_2, \lambda_3 and \mathbf{b}_{\text{B}} are the hyperparameters to balance the different components of the loss function.

## Training details

All experiments were conducted on a server with 8 NVIDIA A40 GPUs. The length of the learnable context was set to 40 tokens for morphology classification, 100 tokens for pathology classification, and 200 tokens for gene mutation prediction tasks. An ablation study was performed to evaluate the impact of the learnable context length by varying the context length from 40 to 200 tokens. The average performance for each task type is reported in the supplementary material. During training, all weights of the pathology VLMs were frozen, and only the learnable context, the weights of the variational information bottleneck, and the weights of the ML models were optimized. For optimization, the Adam optimizer was used with a learning rate of 0.00001 for ABMIL, ACMIL, and CLAM-SB, and 0.00001 for DTFD-MIL and IRLA-MIL. The batch size was set to 1, and all tasks were trained for 20 epochs. For evaluation, the F1 score and the F1 score were adopted as metrics. Results for all models are reported as the mean and standard deviation over 15 folds of SP-MCCV for both OOD and IND testing data.

## Evaluation metrics

To comprehensively assess the efficacy of FLEX, we evaluated its performance across two key dimensions: standard performance metrics and demographic fairness metrics.

Performance metrics. Given the inherent class imbalance often encountered in WSI analysis tasks, we employed the AUROC and the F1 score as primary performance metrics. These metrics are well-suited for evaluating model performance in imbalanced classification scenarios. The Receiver Operating Characteristic (ROC) curve graphically depicts the trade-off between the True Positive Rate (TPR) and the False Positive Rate (FPR) across varying classification thresholds. AUROC, representing the area under this curve, provides a threshold-independent measure of model performance that is robust to imbalanced and negative instances. Its robustness to class imbalance makes AUROC particularly appropriate for our evaluation. Complementing AUROC, the F1 score offers a balanced measure of precision and recall, providing a more granular perspective on classification accuracy. Defined as the harmonic mean of precision and recall, the F1 score is calculated as follows:

F_1 = \frac{2 \times \text{TP}}{2 \times \text{TP} + \text{FP} + \text{FN}} \quad (8)

where True Positives (TP), False Positives (FP), and False Negatives (FN) denote the number of true positives, false positives, and false negatives, respectively. The F1 score penalizes models that disproportionately favor either precision or recall, rewarding those with balanced performance.

Fairness metrics. To evaluate FLEX's impact on demographic fairness, we adopted a suite of fairness metrics: AUROC gap ratio31, TPR disparity32, and demographic parity33. These metrics collectively quantify and characterize potential performance disparities across different demographic groups, offering a multi-faceted assessment of fairness.

Nature Communications | (2025)16:11485

15

---

<!-- Page 16 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

The AUROC gap ratio, as defined in14, quantifies the relative AUROC performance disparity between the best-performing and worst-performing demographic groups, normalized by the overall AUROC. A smaller AUROC gap ratio indicates improved fairness. TPR disparity, as introduced in14, measures the difference between the overall TPR and the TPR for each demographic group. TPR disparity values closer to zero suggest greater fairness, indicating that the model's true positive detection rate is more consistent across demographic groups and less biased towards any particular group. Furthermore, race-wise AUROC provides a granular view of performance by calculating the AUROC separately for each race group. Consistent AUROC values across different demographic groups are indicative of a fairer model, demonstrating that the model's discriminatory power is not significantly influenced by demographic factors.

## Ethics declarations

TCGA dataset and the CPTAC dataset are publicly accessible with appropriate protocol approval. The NCI-NCI-HCC-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

---

<!-- Page 17 -->

Article

https://doi.org/10.1038/s41467-025-66300-y

30. Xiang, J., Zhang, J. Exploring low-rank property in multiple instance learning for whole slide image classification. In: The Eleventh International Conference on Learning Representations. (2022).

31. Huang, Y., Zhao, W., Fu, Y., Zhu, L., Yu, L. Unleash the power of state space model for whole slide image with local aware scanning and importance resampling. IEEE Transactions on Medical Imaging. (2023).

32. Ong, Ly, C. et al. Shortcut learning in medical AI hinders generalization: method for estimating AI model generalization without external data. NPJ Digit. Med. 7, 124 (2024).

33. Chawla, N. J. et al. Challenges in artificial intelligence for medical and healthcare. Nature. 10, 696 (2023).

34. Geirhos, R. et al. Shortcut learning in deep neural networks. Nat. Mach. Intell. 2, 665–673 (2020).

35. Vaidya, A. et al. Demographic bias in misdiagnosis by computational pathology models. Nat. Med. 30, 1174–1180 (2024).

36. Salehi, P., Chalechane, A. Pix2pix-based stain-to-stain translation: a solution for robust histopathology image segmentation and image analysis. In: 2022 International Conference on Machine Vision and Image Processing (MVIP), 1–7 (IEEE, 2022).

37. Howard, F. M. et al. The impact of site-specific digital histology signatures on deep learning model accuracy and bias. Nat. Commun. 12, 4423 (2021).

38. Healy, J. & McInnes, L. Uniform manifold approximation and projection. Nat. Rev. Methods Primers 4, 82 (2022).

39. MacIsaac, M. et al. A method for normalizing histology slides for quantitative analysis. In: 2009 IEEE International Symposium on Biomedical Imaging: from Nano to Macro, 1107–1110 (IEEE, 2009).

40. Tello, J. et al. Quantitative analysis of histological features and stain color normalization in convolutional neural networks for computational pathology. Med. image Anal. 58, 101544 (2019).

41. Bejndor, B. E. et al. Stain-specific standardization of whole-slide histological images. IEEE Trans. Med. Imaging 35, 404–415 (2015).

42. Carrot-Jiang, J. et al. Comprehensive analysis of genetic ancestry and their molecular correlates in cancer. Cancer Cell 37, 899–914 (2020).

43. Ktena, J. et al. Generative models improve the fairness of medical classifiers under distribution shifts. Nat. Med. 30, 1166–1173 (2024).

44. Bernardo-Sousa, R. & Metzger-Filho, O. Differences between invasive lobular and invasive ductal carcinoma of the breast: results and therapeutic implications. Ther. Adv. Med. Oncol. 8, 261–266 (2019).

45. Tang, M. I. et al. The histologic phenotype of lung cancers is associated with transcriptomic features rather than genomic characteristics. Nat. Commun. 12, 7081 (2021).

46. Chen, Y.-C. et al. Clinicopathological variation of the Lauren classification in gastric cancer. Pathol. Oncol. Res. 22, 197–202 (2016).

47. Lobl, S. & Gianni, L. Her-2-positive breast cancer. Lancet 389, 2415–2429 (2017).

48. Sommer, S., Fuqua, S.A. Estrogen receptor and breast cancer. In: Seminars in Cancer Biology, 11, 339–352 (Elsevier, 2001).

49. Kato, A. & Rhiolais, D. Estrogen and progesterone receptors in breast cancer. Future Oncol. 10, 2393–2301 (2014).

50. Fukuyama, M. Epstein-barr virus and gastric carcinoma. Pathol. Int. 60, 357–360 (2010).

51. Lee, W. K., Kim, J., Kim, J. G., Graham, D. Y. & Sepulveda, A. R. Microsatellite instability in gastric intestinal metaplasia in patients with and without gastric cancer. Am. J. Pathol. 156, 537–543 (2000).

52. Zardis, D., Phillips, W. A. & Lo, S. P. Kic3a mutations in breast cancer: reconciling findings from preclinical and clinical data. Breast Cancer Res. 16, 1–10 (2014).

53. Sarrio, D. et al. Epigenetic and genetic alterations of APC and CDH1 genes in lobular breast cancer: relationships with abnormal α-catenin expression, histology and microsatellite instability. Int. J. Cancer 108, 208–215 (2003).

54. Cunha Santos, G., Shephard, F. A. & Tsao, M. S. Efr mutations and lung cancer. Annu. Rev. Pathol. Mech. Dis. 6, 49–69 (2011).

55. Facchinetti, A. et al. L919/4K1 mutations in non-small cell lung cancer patients: descriptive analysis and prognostic value. Lung Cancer 12, 62–68 (2017).

56. Fengilho-Preiser, C., Wang, J., Stemmermann, G. & Nofflinger, A. T. and the European carcinoma: a review. Hum. Mutat. 21, 258–270 (2003).

57. Jonchere, N. & Van Seuningen, I. Integrative analysis of the Cancer Genome Atlas and cancer cell line HIF1α encodes a large genomic deletion. Cell 140, MuC4/6muC20 signature is associated with poor survival in human carcinoma cells. J. Transl. Med. 16, 1–22 (2018).

58. Serrano, J. J., Ibarra, I. & Punt, C. J. Brf1 mutation in metastatic colorectal cancer. N. Engl. J. Med. 361, 98–99 (2009).

59. Iacopetta, B. Tp53 mutation in colorectal cancer. Hum. Mutat. 21, 271–276 (2003).

60. Reinhard, E. & Adhikmin, M., Gooch, B. & Shirley, P. Color transfer between images. IEEE Comput. Graph. Appl. 21, 34–41 (2001).

61. Maron, O., Lozano-Pérez, T. A framework for multiple-instance learning. Advances in neural information processing systems 10 (2017).

62. Huang, Y., Zhao, W., Chen, Y., Fu, Y., & Yu, L. Free lunch in pathology foundation model: Task-specific model adaptation with concept-driven data augmentation. Adv. Neural Inf. Process. Syst. 37, 7963–7965 (2024).

63. Tishby, N., Zaslavsky, N. Deep learning and the information bottleneck principle. In: 2015 IEEE Information Theory Workshop (ITW), 1–5 (IEEE, 2015).

64. Tishby, N., Pereira, F. C., Bialek, W. The information bottleneck method. arXiv Preprint at https://arxiv.org/10.48550/arXiv.physics/0004005v0 (2000).

65. Kolesnikov, A. & Helling, M. Auto-Encoding Variational Bayes. In: 2nd International Conference on Learning Representations. (2014).

66. Alemi, A. A., Fischer, I., Dillon, J. V. & Murphy, K. Deep variational information Bottleneck. In: International Conference on Learning Representations. (2017).

67. Oord, A. v. d., Li, Y., Vinyals, O. Representation learning with contrastive predictive coding. arXiv Preprint at https://doi.org/10.48550/arXiv.1607.08638 (2016).

68. Huang, Y. et al. Knowledge-Guided Adaptation of Pathology Foundation Models Effectively Improves Cross-domain Generalization and Demographic Fairness. Code Repository for FLEX. https://doi.org/10.5328/zemodo.7374304 (2025).

## Acknowledgments

This work was supported in part by the Research Grants Council of Hong Kong (Nos. 27062013, 12200125, C5055-14-C, and T45-401/22-N) and the Hong Kong Innovation and Technology Fund (Nos. ITS/274/22 and GHP/318/22GD) awarded to LY, and by the RGC Collaborative Research Fund (No. 1410121917) and the Hong Kong Polytechnic University (Nos. PQ045998), the Seed Fund of the Research Institute for Smart Ageing (No. PQ005946), the TangYau-PolyU Joint Research Initiative Fund (No. PQ056509), and PolyU's UGC funding (No. PQ053716) awarded to SW.

## Author contributions

Y.H., W.Z., and L.Y. conceived the study and designed the experiments. Y.H., W.Z., Z.Z., Y.-F., W.L., and S.H. contributed to data analysis and manuscript writing. Z.Z., Y.-F., and L.L. provided expert opinions on pathology concepts and data interpretation for model development.

Nature Communications | (2025)16:11485

17

---

<!-- Page 18 -->

Article
[https://doi.org/10.1038/s41467-025-66300-y](https://doi.org/10.1038/s41467-025-66300-y)

L.Y., S.W., and L.L. supervised the study. All authors reviewed and approved the final paper.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-66300-y.

Correspondence and requests for materials should be addressed to Li Liang, Shujun Wang or Lequan Yu.

Peer review information Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025

Nature Communications | (2025)16:11485
18