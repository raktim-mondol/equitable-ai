<!-- Page 1 -->

arXiv:2507.21912v1 [cs.CV] 29 Jul 2025

# PREDICTING PATIENT SELF-REPORTED RACE FROM SKIN HISTOLOGICAL IMAGES WITH DEEP LEARNING *

Shengjia Chen, Ruchika Verma, Jannes Jegminat, Thomas Fuchs, Gabriele Campanella*

Windreich Department of Artificial Intelligence and Human Health,

Icahn School of Medicine at Mount Sinai, New York, USA

Hasco Plattner Institute for Digital Health at Mount Sinai,

Icahn School of Medicine at Mount Sinai, New York, USA

Corresponding author: gabriele.campanella@mssm.edu

Kuan-lin Huang

Windreich Department of Artificial Intelligence and Human Health,

Icahn School of Medicine at Mount Sinai, New York, USA

Mount Sinai Center for Transformative Disease Modeling,

Icahn School of Medicine at Mount Sinai, New York, USA

Kevin Clare, Brandon Veremis

Department of Pathology, Molecular and Cell-Based Medicine,

Mount Sinai Health System, New York, USA

## ABSTRACT

Artificial Intelligence (AI) has demonstrated success in computational pathology (CPath) for disease detection, biomarker classification, and prognosis prediction. However, its potential to learn unintended demographic biases, particularly those related to social determinants of health, remains understudied. This study investigates whether deep learning models can predict self-reported race from digitized dermatopathology slides and identifies potential morphological shortcuts. Using a multisite dataset with a racially diverse population, we apply an attention-based mechanism to uncover race-associated morphological features. After evaluating three dataset curation strategies to control for confounding factors, the final experiment showed that White and Black demographic groups retained high prediction performance (AUC: 0.799, 0.762), while overall performance dropped to 0.663. Attention analysis revealed the epidermis as a key predictive feature, with significant performance declines when these regions were removed. These findings highlight the need for careful data curation and bias mitigation to ensure equitable AI deployment in pathology. Code available at: https://github.com/sinai-computational-pathology/CPath_SAF

Keywords Computational Pathology · AI Fairness · Dermatopathology

## 1 Introduction

Bias and disparities in Machine Learning (ML)-based biomedical and healthcare applications have been widely studied by stratifying model performance across demographic groups [1]. Recent studies have shown that ML models can propagate or even exacerbate existing healthcare inequalities due to dataset bias, arising from differences in disease prevalence, clinical presentation, and annotation inconsistencies across demographic groups [2, 3]. While algorithmic fairness techniques have been explored to mitigate bias [4], several studies have also demonstrated

*Citation: Accepted to the MICCAI Workshop on Fairness of AI in Medical Imaging (FAIMI), 2025. Full citation will be provided after final publication.

---

<!-- Page 2 -->

Predict Patient Self-reported Race from Skin Histological Images
Chen et al.

that feature-confounder correlations, such as the presence of treatment artifacts or institution-specific markers, can undermine model generalizability and fairness [5, 6, 7].

In computational pathology (CPath), deep learning (DL) models have shown promise in disease detection [8], biomarker classification [9], and prognosis prediction [10], but demographic disparities in performance have also been reported, in recent studies [11]. While biases and demographic shortcuts are well-studied in medical imaging [12], particularly radiology [13, 14], similar investigations in histopathology remain limited. Histological slides capture complex tissue morphology, cellular structures, and microenvironmental characteristics, but it is unclear whether these reflect demographic variations. Identifying such associations is crucial to understand confounders that may influence differential model performance in CPath [15].

In this study, we investigate whether the DL models can infer self-reported race from histological images using skin histology data collected across multiple sites within a health system, without specific curatorial. Skin histology provides a unique opportunity for this analysis, as characteristics related to melanin and pigmentation—while visibly distinct in clinical dermatology [16]—are not readily apparent in histological images, making it unclear whether DL models can still capture race-associated patterns. By focusing on a single organ system, we effectively control for potential confounding variables that would present greater challenges in a more heterogeneous dataset. Using widely validated tile-level foundation models (FMs) in CPath [17] combined with explainable attention-based model AB-MIL [19], we examine whether cellular and cellular features can predict self-reported race. Furthermore, we implement a histomorphological phenotype learning framework [20] to identify morphologies associated with high attention regions, providing biological insights into model behavior.

## 2 Related Work

Recent studies have shown that DL models can predict self-reported race with high accuracy across medical imaging modalities, particularly in radiology [21]. Adleberg et al. [14] reported an AUC of 0.911 for race prediction using chest radiographs, a capability that persists across modalities even when undetectable to human experts [13]. Beyond classification, race-related feature encodings have been observed in chest X-ray foundation models [22] and brain age prediction models trained on MRI, with both showing performance disparities and statistically significant distribution shifts across demographic subgroups [23]. In histopathology, stain variability and site-specific digital signatures can correlate with ethnicity and inflate model performance [6, 24]. Additionally, models trained for diagnostic tasks can encode racial information, with diagnostic accuracy positively associated with race prediction performance, even after mitigation efforts [11]. Extending these findings to CPath, our work investigates histomorphological features associated with self-reported race in dermatopathology, aiming to identify potential biological confounders and assess their influence on model predictions.

## 3 Methods

### 3.1 Dataset

A self-reported, a social construct with known correlations to differential health outcomes and a widely recognized social determinant of health, was collected from patient records and questionnaires at Mount Sinai health system. Patients with self-reported race equal to “unknown” or “not reported” were removed. Our private dataset consists of digitized slides from all available skin specimens, assembled from multiple sites in New York city, with all slides scanned on a Philips Ultrafast scanner. The dataset exhibits a diverse racial distribution with the overall patient population at Mount Sinai health system, closely matching the city’s demographics. Although the White group is slightly overrepresented (39.3%), this imbalance is relatively minor compared to other widely used histological datasets, such as TCGA, where 73.7% of samples are from White patients. Self-reported race data are provided for comparison in Table 1.

The dataset was generated from all available dermatopathology specimens within the health system, rather than being curated for a specific disease or prediction task. This includes a wide range of skin conditions such as hemangiomas, melanoma, basal cell carcinoma (BCC), seborrheic keratosis, squamous cell carcinoma (SCC), and various types of inflammatory and infectious dermatoses. Additionally, the potential site-specific signature, as suggested in [6], has been controlled for since all slides collected from different sites were stained and digitized in a central laboratory within the health system.

2

---

<!-- Page 3 -->

Predict Patient Self-reported Race from Skin Histological Images

Chen et al.

Table 1: Summary of the skin dataset by self-reported race compared with Mount Sinai healthcare system, New York city population, and public source (TCGA).

| Self-reported | Skin Cohort | Skin Cohort | Health System | City | TCGA |
| --- | --- | --- | --- | --- | --- |
| Race | # Slides (%) | Patients % |   | Population % |   |
| White | 1,351 (40.6%) | 30.3 | 45.1 | 31.2 | 73.9 |
| Black | 1,015 (19.3%) | 19.0 | 21.7 | 29.9 | 10.3 |
| Hispanic/Latino | 868 (16.5%) | 16.8 | 18.5 | 21.0 | 8.5 |
| Asian | 687 (13.1%) | 15.7 | 16.1 | 5.7 | 7.1 |
| Other | 543 (10.3%) | 9.3 | 6.4 | 4.5 | 1.8 |
| Total Number | 5,266 | 2,471 | 114,947 | 8M | 23,276 |

### 3.2 Experimental Setup

To investigate the capability of DL models to classify self-reported race from histological images, we implemented a classification pipeline leveraging FM for feature extraction. Each slide was assigned a label corresponding to the self-reported race of the patient. The dataset was split 80/20 for training and validation at the patient level, with no separate test set allocated since generalization was not the focus. Tissue tiles were extracted at 20x magnification, and tile-level embeddings were generated using four pretrained FMs. SP22M [25], UNI [26], GigaPath [27], and Virchow [28], followed by an attention-based MIL (AB-MIL) model [18] for slide-level aggregation. We selected AB-MIL due to its ability to efficiently learn informative tile-level attention scores that highlight discriminative regions within a slide while maintaining interpretability. The attention mechanism allows the model to quantitatively assess each tile’s contribution to the slide-level racial prediction. These models are specified by the count of skin slides utilized in their pretraining and their model size: SP22M (1426 slides, 22M) [25], UNI (3653 slides, 303M) [26], GigaPath (2243 slides, 1135M) [27], and Virchow (273,893 slides, 1.488M) [28].

During training, a weighted loss function was applied to ensure class balance, and models were trained for 40 epochs using the AdamW optimizer [29] with an initial learning rate of 0.0005, a 5-epoch warm-up, and a cosine decay schedule. A batch size of 512 was employed, and the final model checkpoint was evaluated on the validation set for performance and attention analysis. To ensure reproducibility and stability, Xavier initialization [30] was applied with three fixed random seeds (0, 42, 2025), and output probabilities and attention scores were averaged across these runs. All training was conducted on a single H100 GPU.

### 3.3 UMAP Visualization

To better understand the histological patterns that are important for the self-reported race prediction task, we utilized a histomorphological phenotype learning framework [20] to efficiently analyze regions of high attention. This tool also enables the efficient visualization of high histological structures, allowing us to study the relative attention given to different tissue compartments. Instead of training a segmentation model from scratch, we leveraged SP22M [25] to extract tile features, which were then projected into a 2D UMAP space [31] for visualization. Pathologists annotated a few landmark tiles to identify key tissue structures, allowing us to locate similar tiles in the UMAP space. Through iterative refinement, a Random Forest classifier was trained to segment regions of interest (ROI) based on UMAP-embedded tile features, defining ROIs as areas where at least 20% of pixels corresponded to a given morphological class. Representative morphological classes identified in the UMAP space included epidermis, inflammation, gastrointestinal (GI) tissue, bone, adipose tissue (fat), blood, smooth muscle, skeletal muscle, ducts, and oncocytes, as well as common artifacts such as ink, cautery, and coverslip edges. Two pathologists validated these annotations before proceeding with stratified attention analysis.

### 3.4 Attention Scores and Distribution Analysis

The attention score for each self-reported race class was obtained from AB-MIL [18], incorporating a multi-head mechanism similar to CLAM [32] to output distinct attention scores for each race groups. Each tile within a slide received an attention score corresponding to the race prediction head, indicating its contribution to the model’s classification decision. To enable cross-slide comparisons, attention scores were normalized across all tiles in the validation dataset to a [0,1] range. We then compared mean attention scores between ROI and non-ROI areas to assess the relationship between attention and tissue morphology, investigating whether specific tissue types contributed more significantly to the model’s decision-making process.

3

---

<!-- Page 4 -->

Predict Patient Self-reported Race from Skin Histological Images

Chen et al.

## 4 Results

To evaluate the potential bias of disease distribution on race prediction, we curated three versions of datasets. Model performance was evaluated using one-vs-rest (O/R) area under the curve (AUC), and results are summarized in Table 2. For each row, the mean area under the curve (AUC) score is reported based on 1000 bootstrap iterations. On average, 9,647 tiles were extracted at 20x magnification per slide (min: 46, median: 8,067, max: 45,172), depending on the size of the main tissue area.

Table 2: Model performance across three dataset curations. AUC is one-vs-all, accuracy is balanced accuracy.

| Experiment | Encoder | AUCs by Racial Groups | AUCs by Racial Groups | AUCs by Racial Groups | AUCs by Racial Groups | AUCs by Racial Groups | Overall Metrics | Overall Metrics |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Experiment | Encoder | White | Black | Hispanic | Asian | Other | AUC | Accuracy |
| Exp1 Uncurated | SP22M | 0.772 | 0.785 | 0.586 | 0.805 | 0.547 | 0.699 | 0.395 |
| Exp1 Uncurated | UNI | 0.791 | 0.791 | 0.607 | 0.791 | 0.603 | **0.718** | **0.400** |
| Exp1 Uncurated | GigaPath | 0.801 | 0.753 | 0.598 | 0.801 | 0.522 | 0.695 | 0.388 |
| Exp1 Uncurated | Vischew | 0.784 | 0.749 | 0.591 | 0.783 | 0.579 | 0.697 | 0.392 |
| Exp1 Uncurated | Average | **0.789** | 0.770 | 0.596 | **0.795** | 0.563 | 0.702 | 0.394 |
| Exp2 Balance Disease | SP22M | 0.744 | 0.751 | 0.569 | 0.701 | 0.577 | 0.668 | 0.368 |
| Exp2 Balance Disease | UNI | 0.760 | 0.773 | 0.560 | 0.715 | 0.560 | **0.676** | **0.380** |
| Exp2 Balance Disease | GigaPath | 0.734 | 0.739 | 0.581 | 0.753 | 0.559 | 0.673 | 0.372 |
| Exp2 Balance Disease | Vischew | 0.728 | 0.735 | 0.528 | 0.726 | 0.590 | 0.665 | 0.354 |
| Exp2 Balance Disease | Average | **0.754** | 0.757 | 0.560 | 0.732 | 0.564 | 0.671 | 0.364 |
| Exp3 Strict ICD code | SP22M | 0.788 | 0.773 | 0.584 | 0.841 | 0.534 | 0.632 | 0.287 |
| Exp3 Strict ICD code | UNI | 0.819 | 0.766 | 0.654 | 0.856 | 0.594 | 0.678 | 0.296 |
| Exp3 Strict ICD code | GigaPath | 0.791 | 0.766 | 0.664 | 0.650 | 0.631 | 0.661 | **0.533** |
| Exp3 Strict ICD code | Vischew | 0.796 | 0.742 | 0.656 | 0.592 | 0.613 | **0.680** | 0.293 |
| Exp3 Strict ICD code | Average | **0.799** | **0.762** | 0.660 | 0.570 | 0.543 | 0.663 | 0.302 |

Exp1 (Uncurated) included all available dermatopathology specimens and yielded the highest overall O/R AUC (0.702), with particularly strong performance in the Asian group (AUC = 0.795). This was attributed to a disproportionately high prevalence of hemorrhoid cases (61%) among Asian patients due to site-specific sampling biases (160 out of 312 Asian patients treated at one site). Exp2 (Balance Disease) mitigated disease-related confounding by rebalancing hemorrhoid cases and removing gangrene and sun damage-related conditions disproportionately prevalent in Black and White patients but had low overall occurrence (e.g., melanoma, basal cell carcinoma, squamous cell carcinoma, actinic keratosis, and seborrheic keratosis), resulting in 2,032 patients (W 37.5%, B 19.8%, H/L 17.3%, A 15.1%, O 10.2%). This adjustment led to a decline in overall O/R AUC (0.671), with the Asian group experiencing the largest drop (AUC: 0.795 → 0.724). In Exp3 (Strict ICD Code), we further restricted the dataset to classical dermatopathology cases (ICD-10 code, L: inflammatory skin diseases, C: skin cancers, D: benign skin growths and disorders), fully removing hemorrhoids (ICD-10 K), and reducing dataset to 800 patients (W 46.9%, B 19.9%, H/L 19.6%, A 7.2%, O 6.5%). This further reduced the overall O/R AUC to 0.663, with the Asian group showing the most pronounced decline (0.570), whereas the White group maintained consistently high performance (0.799).

### 4.1 UMAP Visualization of Attention and Morphological Patterns

Visual inspection of attention scores suggested a spatial association between high attention and tissue morphology across racial groups. To investigate this, we projected attention scores into a lower-dimensional UMAP space using SP22M encoder due to its lightweight architecture (22M parameters) and comparable performance. For UMAP generation, 20 slides per racial group were randomly sampled from Exp3, with 10,000 tiles per slide. Figure 1A presents the UMAP projection, where a grayscale kernel density estimation (KDE) background shows the overall data distribution, and colored contour lines highlight regions with the top 10% of attention scores for each racial group. White and Black groups exhibit more concentrated attention clusters, whereas the Hispanic/Latino, Asian, and Other groups display more dispersed attention distributions, suggesting potential histomorphological differences. To further examine morphological differences in model attention, Figure 1B visualizes pathologist-annotated tissue types (epidermis, inflammation, blood, and dermis) with UMAP. The UMAP projection shows that inflammation is influenced by the distinct histological structures. Figure 1C and D zoom into two high-attention regions identified in the KDE plot. Figure 1C includes diverse histomorphological types (oncocytes, ducts, inflammation), but high attention in this region lacks a clear structural association. In contrast, Figure 1D corresponds specifically to epidermis, aligning with the strong epidermal attention observed in the White and Black groups.

4

---

<!-- Page 5 -->

Predict Patient Self-reported Race from Skin Histological Images

Chen et al.

Figure 1: UMAP visualization of attention scores. (A) Density plot with a grayscale KDE background representing the overall distribution. Contour lines were generated for high-attention tiles within each racial group. (B) Grid plot visualizing representative samples from different UMAP regions. (C, D) Zoomed-in grid plots highlighting regions that received high model attention. GI: gastrointestinal tract.

#### 4.2 Attention Distribution Analysis

Figure 2 presents whole-slide attention maps from examples in Exp3. In (A), attention to White maps strongly to the epidermis, whereas in (B), attention to Black highlights the epidermis but also extends to other regions. In (C), attention to Hispanic is predominantly observed in non-epidermis regions. To compare attention distribution, we performed a one-sided paired t test to assess whether epidermal regions received higher attention than non-epidermis regions. Figure 3A presents the median attention score per slide including only slides with more than 15 epidermis tiles were to reduce noise. Across all three experiments, epidermal regions consistently received higher attention than non-epidermis regions, but the magnitude of this difference decreased from Exp1 to Exp3. In Exp3, the effect was significant only for the White and Black groups, while the Asian group exhibited lower attention in epidermis than non-epidermis regions. Figure 3B further

5

---

<!-- Page 6 -->

Predict Patient Self-reported Race from Skin Histological Images

Chen et al.

Figure 2 displays whole-slide attention maps for three racial groups (White, Black, and Hispanic/Latino) across three stages: (1) Thumbnail, (2) Epidermis, and (3) Attention Score. The figure is organized into a 3x3 grid. The rows are labeled A: White, B: Black, and C: Hispanic/Latino. The columns are labeled (1) Thumbnail, (2) Epidermis, and (3) Attention Score. A color scale on the right indicates the Attention Score, ranging from 0.2 (blue) to 0.9 (yellow). The attention maps show the distribution of attention across the whole slide, with the epidermis layer being a key focus for all groups.

Figure 2: Whole-slide attention maps for selected examples from Exp3. Rows correspond to three selected slides, with columns showing: (1) Whole-slide thumbnail, (2) Binary mask of epidermis detection, and (3) Attention score from a specific racial group. (A) Attention to White, (B) Attention to Black, (C) Attention to Hispanic/Latino.

highlights the importance of epidermis in self-reported race prediction. When epidermis tiles were completely removed in validation data, model performance dropped by approximately 0.05 across all racial groups and experiments. When only epidermis tiles were retained—with 85% of slides in validation set containing less than 20% epidermis tiles—the model maintained comparable or even improved performance in some racial groups.

## 5 Discussion

In this study, we examined whether DL models can predict self-reported race from digitized dermatopathology slides, independent of pathology task. Unlike previous studies on reporting the differential performance of task-specific models, we explored whether biological correlates of race could be identified in histology images. This is important because task-specific models could exploit these features as shortcuts, leading to unintended biases and disparities in clinical predictions. Our results (Exp3) show that self-reported race can be predicted with moderate accuracy (AUC = 0.7), particularly for White (0.80) and Black (0.76) patients. Across four encoders used, UNI consistently captured race-related information, despite Virchow being pretrained on the largest number of skin slides (18%, 273,893 slides).

We identified epidermis, which typically constitute 10%–20% of tissue in skin histology slides, as the strongest predictive histological component, consistent with the role of melanocytes in skin tone [15]. Across all experiments, White and Black groups consistently had higher prediction performance than Hispanic/Latino and Asian groups, possibly due to more distinct epidermal features in White and Black patients, whereas Hispanic and Asian groups exhibit greater morphological variation, making classification more challenging. Confounding variables in patient sampling and disease presentation also inflated prediction performance. In Exp1, the overrepresentation of hemorrhoid cases in Asian patients (61%) likely caused the model to associate race with disease prevalence rather than intrinsic histological differences. Exp2 rebalanced disease distribution, resulting in a performance drop, suggesting that race labels acted as unintended shortcuts for disease classification. Exp3, which applied ICD-10 coding to focus on skin disease cases, was chosen for further investigation.

6

---

<!-- Page 7 -->

Predict Patient Self-reported Race from Skin Histological Images

Chen et al.

Figure 3: Attention and ablation analysis across racial groups and experiments. (A) Boxplots comparing the median attention score per slide between epidermis and non-epidermis regions (B) AUCs with epidermis tiles removed (orange), kept only (blue), and compared to original model (green). One-sided paired t-test significance: *, p < 0.05, **, p < 0.01, ***, p < 0.001, n.s./unlabeled if not significant.

Our study raises key concerns about demographic shortcuts in CPath but also has several limitations. Self-reported race is a socioeconomic determinant that while identifying potential confounders, also introduces noise. The heterogeneity of the Hispanic/Latino group further complicates isolating specific biological or morphological patterns. Integrating genetic ancestry data alongside self-reported race may provide a more comprehensive understanding of demographic influences in histological analysis. This study focused on skin histology for better control over confounders, but future work should extend to other specimen/organs to determine whether race-associated patterns emerge in other tissues or if skin remains unique due to its link to pigmentation. Additionally, ICD-10 coding has inherent limitations, as it reflects clinical suspicion rather than definitive histological diagnosis. In addition, while we focused on removing high-attention epidermal tiles during validation, further investigation into secondary high-attention regions with more heterogeneous morphologies would be valuable. Furthermore, our study used AB-MIL, a spatially-unaware aggregation model, meaning it analyzes each tile independently without considering spatial interactions across the slide. Evaluating on a more sophisticated slide-level aggregator that accounts for tile-to-tile spatial relationships could offer deeper insights into how histological structures collectively contribute to racial classification.

## 6 conclusion

While histological images may not encode demographic signals as strongly as radiological images [13, 14], DL models can still predict self-reported race, likely by leveraging morphological shortcuts such as epidermal structures in skin slides. These findings highlight the need to consider demographic biases in CPath models and the impact of dataset curation on model fairness. Developing bias mitigation methods to address model reliance on demographic shortcuts is crucial for ensuring fairness in CPath applications, and we encourage researchers to carefully account for disease distribution and remain mindful of how AI models may inadvertently learn and exploit sensitive demographic information rather than focusing on disease-related histological features.

## Acknowledgments

This work is supported in part through the use of research platform AI-Ready Mount Sinai (AIR.MS) and the expertise provided by the team at the Haso Plattner Institute for Digital Health at Mount Sinai (HPLMS). This work was supported in part through the computational and data resources and staff expertise provided by Scientific Computing and Data at the Icahn School of Medicine at Mount Sinai and supported by the Clinical and Translational Science Awards (CTSA) grant UL1TR004419 from the National Center for Advancing Translational Sciences.

7

---

<!-- Page 8 -->

Predict Patient Self-reported Race from Skin Histological Images
Chen et al.
References

[1] Laleh Seyyed-Kalatari, Haoran Zhang, Matthew BA McDermott, Irene Y Chen, and Marzyeh Ghassemi. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature medicine, 27(12):2176–2182, 2021.

[2] Lama H Nazer, Nazare Zatarah, Shah Waldrip, Janny Xue Chen Ke, Mira Moukheiber, Ashish K Khanna, Rachel S Hicklen, Lama Moukheiber, Dana Moukheiber, Haobo Ma, et al. Bias in artificial intelligence algorithms and recommendations for mitigation. PLoS Digital Health, 2(6):e0000278, 2023.

[3] Charles Jones, Daniel C Castro, Fabio De Sousa Ribeiro, Ozan Oktay, Melissa McCradden, and Ben Glocker. A causal perspective on dataset bias in machine learning for medical imaging. Nature Machine Intelligence, 6(2):138–146, 2024.

[4] Jenny Yang, Andrew AS Soltan, David W Eyre, Yang Yang, and David A Clifton. An adversarial training framework for mitigating algorithmic biases in clinical machine learning. NPJ digital medicine, 6(1):55, 2023.

[5] Luke Oakden-Rayner, Jared Dunmonn, Gustavo Carneiro, and Christopher Ré. Hidden stratification causes clinically meaningful failures in machine learning for medical imaging. In Proceedings of the ACM conference on health, inference, and learning, pages 151–159, 2020.

[6] Frederick M Howard, James Dolezal, Sara Kochany, Jefree Schulte, Heather Chen, Lara Heij, Dezheng Huo, Rita Nanda, Olufunmiyao I Olopade, Jakub N Kather, et al. The impact of site-specific digital histology signatures on deep learning model accuracy and bias. Nature communications, 12(1):4423, 2021.

[7] Brandon G Hill, Frances L Koback, and Peter L Schilling. The risk of shortcutting in deep learning algorithms for medical imaging research. Scientific reports, 14(1):29224, 2024.

[8] Mahdi S Hosseini, Babak Ehteshami Bejnordi, Vincent Quey-Hoy Trinh, Lyndon Chan, Daniel Hasan, Xingwen Li, Stephen Yang, Tachyo Kim, Haochen Zhang, Theodore Wu, et al. Computational pathology: a survey review and the way forward. Journal of Pathology Informatics, page 100357, 2024.

[9] Omar SM El Nahhas, Marko van Treeck, Georg Wölflin, Michaela Unger, Marta Ligerio, Tim Lenz, Sophia J Wagner, Katherine J Hewitt, Firas Khader, Sebastian Foersch, et al. From whole-slide image to biomarker prediction: end-to-end weakly supervised deep learning in computational pathology. Nature Protocols, 20(1):293–316, 2025.

[10] Andrew H Song, Guillaume Jaume, Drew FK Williamson, Ming Y Lu, Anurag Vaidya, Tiffany R Miller, and Faisal Mahmood. Artificial intelligence for digital and computational pathology. Nature Reviews Bioengineering, 1(12):930–949, 2023.

[11] Anurag Vaidya, Richard J Chen, Drew FK Williamson, Andrew H Song, Guillaume Jaume, Yuzhe Yang, Thomas Hartvigsen, Emma C Dyer, Ming Y Lu, Jana Lipkova, et al. Demographic bias in misdiagnosis by computational pathology models. Nature Medicine, 30(4):1174–1190, 2024.

[12] Yuzhe Yang, Haoran Zhang, Judy W Gichoya, Dina Katabi, and Marzyeh Ghassemi. The limits of fair medical imaging ai in real-world generalization. Nature Medicine, 30(10):2838–2848, 2024.

[13] Judy Wawira Gichoya, Imon Banerjee, Ananth Reddy Bhimireddy, John L Burns, Leo Anthony Celi, Li-Ching Chen, Ramon Correa, Natalie Dullerud, Marzyeh Ghassemi, Shih-Cheng Huang, et al. Ai recognition of patient race in medical imaging: a modelling study. The Lancet Digital Health, 4(6):e406–e414, 2022.

[14] Jason Adleberg, Ann Wardel, Florence X Doo, Brett Marinelli, Tessa S Cook, David S Mendelson, and Alexander Kagen. Predicting patient demographics from chest radiographs with deep learning. Journal of the American College of Radiology, 19(10):1151–1161, 2022.

[15] Kyle A Williams, Bitania Wondimu, Ayodeji M Ajayi, and Olayemi Sokumbi. Skin of color in dermatopathology: does color matter? Human Pathology, 140:240–266, 2023.

[16] Valérie M Harvey, Andrew Alexis, Chidubem AV Okeke, Lynn McKinley-Grant, Susan C Taylor, Seemal R Desai, Tarannum Jaleel, Candrice R Heath, Sewon Kang, Neelam Vashi, et al. Integrating skin color assessments into clinical practice and research: a review of current approaches. Journal of the American Academy of Dermatology, 2024.

[17] Gabriele Campanella, Shengjia Chen, Ruchika Verma, Jennifer Zeng, Aryeh Stock, Matt Croken, Brandon Veremis, Abdulkadir Elmas, Kuan-lin Huang, Ricky Kwan, et al. A clinical benchmark of public self-supervised pathology foundation models. arXiv preprint arXiv:2407.06508, 2024.

[18] Maximilian Ise, Jakub Tomczak, and Max Welling. Attention-based deep multiple instance learning. In International conference on machine learning, pages 2127–2136. PMLR, 2018.

8

---

<!-- Page 9 -->

Predict Patient Self-reported Race from Skin Histological Images
Chen et al.

[19] Shengjia Chen, Gabriele Campanella, Abdulkadir Elmas, Aryeh Stock, Jennifer Zeng, Alexandros D Polydorides, Adam J Schoenfeld, Kuan-lin Huang, Jane Houldsworth, Chad Vanderbilt, et al. Benchmarking embedding aggregation methods in computational pathology: A clinical data perspective. arXiv preprint arXiv:2407.07841, 2024.

[20] Adalberto Claudio Quiros, Nicolas Coudray, Anna Yeaton, Xinyu Yang, Bojing Liu, Hortense Le, Luis Chiriboga, Afreen Karimkhan, Navneet Narula, David A Moore, et al. Mapping the landscape of histomorphological cancer phenotypes using self-supervised learning on unannotated pathology slides. Nature Communications, 15(1):4596, 2024.

[21] James Zou, Judy Wawira Gichoya, Daniel E Ho, and Ziad Obermeyer. Implications of predicting race variables from medical images. Science, 381(6654):149–150, 2023.

[22] Ben Glocker, Charles Jones, Mélanie Roschechwitz, and Stefan Winzcke. Risk of bias in chest radiography deep learning foundation models. Radiology: Artificial Intelligence, 5(6):e230060, 2023.

[23] Carolina Picarra and Ben Glocker. Analysing race and sex bias in brain age prediction. In Workshop on Clinical Image-Based Procedures, pages 194–204. Springer, 2023.

[24] F Kheiri, S Rahnamayan, M Makrechi, and AA Bidgoli. Bias in histopathology datasets: A comprehensive investigation on possible factors. 2024.

[25] Gabriele Campanella, Ricky Kwan, Eugene Fluder, Jennifer Zeng, Aryeh Stock, Brandon Veremis, Alexandros D Polydorides, Cyrus Hedvat, Adam Schoenfeld, Chad Vanderbilt, et al. Computational pathology at health system scale-self-supervised foundation models from three billion images. arXiv preprint arXiv:2310.07033, 2023.

[26] Richard J Chen, Tong Ding, Ming Y Lu, Drew FK Williamson, Guillaume Jaume, Andrew H Song, Bowen Chen, Andrew Zhang, Daniel Shao, Muhammad Shaban, et al. Towards a general-purpose foundation model for computational pathology. Nature Medicine, 30(3):850–862, 2024.

[27] Hanwen Xu, Naoto Usuyama, Jaspreet Bagga, Sheng Zhang, Rajesh Rao, Tristan Naumann, Cliff Wong, Zelalem Gero, Javier González, Yu Gu, et al. A whole-slide foundation model for digital pathology from real-world data. Nature, pages 1–8, 2024.

[28] Eugene Vorontsov, Alican Bozkurt, Adam Casson, George Shaikovski, Michal Zelechowski, Kristen Severson, Eric Zimmermann, James Hall, Neil Tenenholz, Nicolo Fusi, et al. A foundation model for clinical-grade computational pathology and rare cancers detection. Nature medicine, pages 1–12, 2024.

[29] Ilya Loschilov, Frank Hutter, et al. Fixing weight decay regularization in adam. arXiv preprint arXiv:1711.05101, 5, 2017.

[30] Xavier Glorot and Yoshua Bengio. Understanding the difficulty of training deep feedforward neural networks. In Proceedings of the thirteenth international conference on artificial intelligence and statistics, pages 249–256. JMLR Workshop and Conference Proceedings, 2010.

[31] Leland McInnes, John Healy, and James Melville. Umap: Uniform manifold approximation and projection for dimension reduction. arXiv preprint arXiv:1802.03426, 2018.

[32] Ming Y Lu, Drew FK Williamson, Tiffany Y Chen, Richard J Chen, Matteo Barbieri, and Faisal Mahmood. Data-efficient and weakly supervised computational pathology on whole-slide images. Nature biomedical engineering, 5(6):555–570, 2021.

9