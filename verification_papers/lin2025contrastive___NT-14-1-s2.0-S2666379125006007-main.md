

<!-- PAGE 1 -->

# Cell Reports Medicine

Article

## Contrastive learning enhances fairness in pathology artificial intelligence systems

### Graphical abstract

### Authors

Shih-Yen Lin, Pei-Chen Tsai, Fang-Yi Su, ..., Sabina Signoretti, Jung-Hsien Chiang, Kun-Hsing Yu

### Correspondence

jhchang@mail.ncku.edu.tw (J.-H.C.), kun-hsing_yu@hms.harvard.edu (K.-H.Y.)

### In brief

Standard AI systems for cancer pathology interpretation exhibit differential performance across demographic groups. Lin et al. address this critical challenge by establishing the FAIR-Path framework, which substantially reduces diagnostic disparities and enhances model fairness. This work represents a crucial step toward ensuring effective AI-assisted cancer evaluation for all populations.

### Highlights

- Standard pathology AI systems show performance disparities across demographic groups
- Our FAIR-Path framework mitigates 88.5% of these disparities
- External validation demonstrates a 91.1% reduction in diagnostic performance gaps
- Population-level somatic mutation variations contribute to AI model bias

Lin et al., 2025. Cell Reports Medicine 6, 102527
December 16, 2025 © 2025 The Author(s). Published by Elsevier Inc.
https://doi.org/10.1016/j.xcrm.2025.102527

Cell Press

<!-- PAGE 2 -->

# Cell Reports Medicine

OPEN ACCESS

## Article

# Contrastive learning enhances fairness in pathology artificial intelligence systems

Shih-Yen Lin,
^1,2,3^
 Pei-Chen Tsai,
^1,2,3^
 Fang-Yi Su,
^1,2,3,4^
 Chun-Yen Cheng,
^1^
 Fuchen Li,
^1^
 Junhan Zhao,
^1,2,3^
 Yuk Yeung Ho,
^1,4^
 Tsung-Li Michael Lee,
^1^
 Elizabeth Heeley,
^1^
 Po-Jen Lin,
^1,2,3^
 Ting-Wan Kao,
^1^
 Dmitry Vremenko,
^1,2,3^
 Thomas Roetzer-Pajvinszky,
^1,2^
 Lynette Shull,
^1,2,3^
 Deborah Dillon,
^1,2^
 Nancy Li Lin,
^1,2^
 David Maretzki,
^1,2^
 Keith L. Ligon,
^1,2,3,4^
 Ying-Chun Lo,
^1,2^
 Nhon Chaisawat,
^1,2,3,4^
 David J. Cook,
^1,2,3^
 Adelheid Woerker,
^1,2,3^
 Jeffrey Meyerhardt,
^1,2^
 Shih-Orjen Ma,
^1,2,3^
 Madh Lee P. Nasrallah,
^1,2^
 Jeffrey A. Golden,
^1,2^
 Sabino Moroetti,
^1,2,3^
 Jang-Hsien Chiang,
^1,2,3^
 and Kun-Hsing Yeh,
^1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925^

<!-- PAGE 3 -->

OPEN ACCESS

## Cell Reports Medicine

article

**Cancer subtypes**
^7,8,9^
 predicting cancer-related genomic profiles
^10,11^
 and estimating patient survival outcomes.
^12,13,14,15^
 These findings point to a promising future where data-driven algorithms could significantly enhance diagnostic accuracy and patient care. In addition, AI has been shown to alleviate clinicians' workload by automating repetitive tasks by enabling them to focus more on patient-specific care.
^13,14^
 For example, AI applications in pathology aid in timely detection and treatment by predicting prognostic factors, allowing early interventions. Computational pathology shows the potential for intraoperative diagnostics and decisions using frozen sections, such as determining the extent of malignant tissue removal to prevent over/under-treatment.

However, algorithmic bias remains a significant challenge in developing AI models for pathology research.
^16^
 Large-scale genomic pathology datasets, such as The Cancer Genome Atlas Program
^17^
 (TCGA) and the Clinical Proteomic Tumor Analysis Consortium
^18^
 (CPTAC), predominantly consist of Caucasian patients, with African Americans, Asians, and other minority racial groups accounting for only 17.4% of patients. This imbalance may result in biases into AI-driven pathology diagnosis models, as these systems often reflect the bias present in their training data.
^19^
 When combined with racial disparities in cancer risk factors
^20,21^
 and societal determinants of health,
^22^
 using biased datasets without caution could result in underdiagnosis and exacerbate health inequities in underrepresented groups. In addition, previous studies have shown that pathology images contain features that correlate with race
^23^
 and hospital site,
^24^
 which may lead to short-sighted learning
^25^
 during model training. These issues can result in unequal diagnostic performance and perpetuate disparities in healthcare outcomes.
^26^
 Therefore, auditing AI models for bias has become a critical prerequisite of clinical deployment.
^27^

Several bias mitigation strategies have been proposed in the deep learning literature. For example, some studies address data imbalances between demographic groups through reweighting, resampling,
^28^
 or generative augmentation
^29^
 of underrepresented minority group data.
^30^
 Others have sought to learn fair representations by suppressing information related to demographic attributes or other confounding factors (e.g., tissue source site) using contrastive learning,
^31^
 feature disentanglement,
^32^
 domain generalization,
^33^
 or generative models.
^34,35^
 In addition, pruning
^36^
 or adversarial learning.
^36,37^
 Additional studies attempted to validate the efficacy of bias mitigation methods in various disease diagnosis models.
^38,39^

In cancer pathology, several studies have attempted to address biases in AI-based diagnostic models. For example, Kien et al. demonstrated that generative models can reduce performance disparities between tissue source sites in pathology classification models while preserving overall performance. Hosseini et al. proposed proportionally fair federated learning
^40^
 to improve fairness among different models. Li et al. investigated how data preprocessing methods, model architectures, and bias mitigation methods affect racial disparities in subtyping breast and lung carcinomas using whole slide images (WSIs).
^41^
 Other studies have also revealed that state-of-the-art models for lung cancer subtyping exhibited significant biases related to attributes such as insurance type and age.
^42^
 These studies provide valuable insights into understanding bias in computational pathology while underscoring the need for continued efforts in bias mitigation. Despite these efforts, fairness analysis and bias mitigation in computational pathology remain limited to small datasets and selected cancer types. A systematic analysis of demographic biases and bias mitigation without a priori cancer diagnosis tasks remains lacking.

In this study, we present a comprehensive analysis of computational pathology, evaluating critical cancer detection and classification tasks across 20 cancer types and eight datasets. Our analysis revealed that standard deep learning models exhibited biases and performance disparities against underrepresented demographic subgroups defined by race, gender, and age. To address these issues, we introduce Fairness-aware Artificial Intelligence Review for Pathology (FAIR-Path), a multi-modal learning framework that mitigates bias through a fairness-aware contrastive learning process. Our pan-cancer evaluation, conducted across diverse cancer types and diagnostic tasks using multiple cancer cohorts from seven institutions or study populations, shows that FAIR-Path reduces bias to 88.5% of the baseline model's baseline performance. Our approach lays the foundation for developing unbiased AI systems for cancer pathology, advancing equity in cancer risk.

## RESULTS

### Study cohort summary

We collected 28,732 whole-slide cancer pathology images (WSIs) from 14,456 cancer patients, encompassing 20 cancer types across five medical centers and three nationwide study cohorts. These digital pathology images include 5,044 hematoxylin-eosin (H&E) slides and 15,320 frozen section slides from the TCGA dataset, 6,866 slides from the 1,248 frozen section slides from CPTAC-3 studies
^43^
 from 1,367 patients, 1,573 FFPE slides from the Prostate, Lung, Colorectal, and Ovarian (PLCO) Cancer Screening Trial
^44^
 (PLCO), 759 FFPE slides from the Medical University of Vienna (MUV), and 1,019 FFPE slides from the Data-Farber Cancer Institute (DFCI; from 3,160 patients), 166 FFPE slides from Mayo Clinic (Mayo; from 166 patients), 166 FFPE and 166 frozen section slides from the University of Pennsylvania (UPenn; from 164 patients), and 121 FFPE and 122 frozen section slides from Mass General Brigham (MGB; from 154 patients). Detailed patient demographics are summarized in Table S1.

### Overview of FAIR-Path

Figure 1 illustrates the overall workflow of the FAIR-Path system. First, we established a pan-cancer WSIs patchset and removed those containing mostly blank backgrounds based on their color distribution. Our model employs a contrastive learning architecture
^45^
 with a two-stage training pipeline to ensure fairness in the learned image representations. In the first stage, we pre-trained the MIL feature extractor with our proposed contrastive learning objective, enhancing the similarity between features from images with the same ground-truth labels. A non-discriminative loss was incorporated to mitigate demographic-related but diagnostic-irrelevant attributes by penalizing similarities between samples sharing demographic

<!-- PAGE 4 -->

**Cell Reports Medicine**

**Article**

Cell Press
OPEN ACCESS

**A The informatics workflow of FAIR-Path**

**B Pan-cancer fairness analysis across 20 cancer types and eight patient cohorts**

**C FAIR-Path mitigated up to 88.5% of disparities observed in standard AI models**

**Figure 1. The Fairness-Aware Artificial Intelligence Review for Pathology (FAIR-Path) framework**

(A) The workflow of FAIR-Path. We first tessellated whole-slide pathology images (WSIs) into patches and removed those with predominantly blank backgrounds. FAIR-Path employs a two-stage training pipeline with multiple-contrastive learning to extract diagnostic signals irrespective of demographic blind signals. In the first stage, supervised contrastive learning identifies diagnosis-related features independent of demographic-related imaging signals. In the second stage, we froze the pretrained feature extractor and fine-tuned the multilayer perceptron (MLP) classifier.

(B) Patient cohorts. We collected 28,782 WSIs from 14,456 cancer patients and evaluated FAIR-Path across 82 classification scenarios, encompassing 27 diagnostic tasks, 20 cancer types, and eight cohorts. To assess internal validity, we quantified performance across patient subgroups defined by self-reported race, gender, and age using cohorts from The Cancer Genome Atlas (TCGA). To evaluate the generalizability of FAIR-Path, we employed 15 independent cohorts from the National Cancer Institute’s NCIC Clinical Proteomic Tumor Analysis Consortium (CPTAC), the Prostate, Lung, Colorectal and Ovarian (PACO) screening trials, the Medical University of Vienna, Austria (MCG), and institutional cohorts from Dana-Farber Cancer Institute (DFCI), Mass General Brigham (MGB), Mayo Clinic (MCG), and the Hospital of the University of Pennsylvania (UPenn).

(C) Performance comparison. Standard deep learning models showed significant performance disparities (one-sided bootstrap test, 
p
 value < 0.05) across race, gender, and age groups, as measured by the equal opportunity metric. These disparities affected 8.75% of cancer detection, 12.1% of histological type classification, and 10.25% of subtype classification tasks (top left). FAIR-Path mitigated these biases in 88.5% of affected tasks, achieving 100% resolution in cancer detection and subtype classification, and 80.0% in histological type classification (top right). Bottom row: percentage of biased tasks in standard models and resolution rates by FAIR-Path, stratified by self-reported sex, gender, and age groups.

See also Table S1.

**Pan-cancer AI fairness analysis revealed demographic biases in AI-driven cancer pathology diagnosis**

We conducted a pan-cancer fairness analysis to quantify demographic bias in baseline AI models across 82 classification scenarios, including 17 tumor detection tasks, 6 cancer

Cell Reports Medicine 6, 102527, December 16, 2025 3

<!-- PAGE 5 -->

OPEN ACCESS

Article

**Figure 2.**
 Standard AI models showed significant performance disparities in cancer diagnosis tasks across population groups

Each fairness metric is represented by a different color, with higher values indicating greater disparity. Data are represented as micro-averaged metrics. Asterisks denote statistically significant tests.

(A) Cancer-type classification (FFPE) sampled. We observed significant racial and gender disparities for LUAD vs. LUAD classification.

(B) Subtype classification (FFPE). We identified significant racial disparities in classifying IDC and related ductal carcinomas vs. ILC and age disparities in the IDC vs. ILC classification.

(C) Cancer-type classification (frozen section). We found significant racial disparities in the classification of GBM vs. LGG, KIRC vs. LGG, KIRC vs. KIRP, and KIRC vs. HCC.

(D) Subtype classification (frozen section). No significant disparities were observed.

(E) Tumor detection (frozen section). We found significant racial disparities in BRCA detection; significant gender disparities in KIRP and THCA detection; and significant age disparities in KIRP and STAD detection.

Abbreviations: BAC vs. LUAD, bronchioalveolar carcinoma vs. other lung adenocarcinoma subtypes; AUCROC vs. mAUROC, serious vs. non-serious derma corpus endometrioid carcinoma; IDC vs. ILC, invasive ductal carcinoma vs. invasive lobular carcinoma; IDC vs. ILC, invasive ductal carcinoma vs. invasive ductal carcinoma mixed with lobular carcinoma vs. invasive lobular carcinoma. 
^**^
bootstrap test p value < 0.05. See also 
[Figure S1](#)
 and 
[Table S1](#)
 and 
[S2](#)
.

type classification tasks, and 4 cancer subtype classification tasks, using TCGA datasets (see 
[Table S2](#)
 for the list of classification scenarios). For each task, we trained a standard AI model
^10^
 with the same architecture as Fair-Path but without incorporating demographic fairness considerations. We developed separate models for FFPE and frozen section slides due to their intrinsic differences and distinct clinical utility. We evaluated fairness with respect to self-reported race, gender, and age. We measured performance disparities using equal opportunity (EOPp; disparity in recall) and equal balanced accuracy (EBAcc). We compared Fair-Path against existing fairness correction methods, including demographic-balanced reweighting
^11^
 (DBR), adaptive sensitive reweighting (ASR)
^12^
, learning fair representations (LFR)
^13^
, AdaFair,
^14^
 and synthetic minority over-sampling technique (SMOTE).

Standard AI models show significant race, gender, or age bias in 29.93% (11 out of 37) of cancer diagnostic tasks (
[Figure 2](#)
). In FFPE-based models for assisting final cancer diagnosis, baseline models showed significant demographic disparities in three cancer classification tasks for at least one fairness measure (Figures 2A and 2B). For instance, in classifying lung adenocarcinoma (LUAD) vs. lung squamous cell carcinoma (LUSC), we observed significant racial disparity in equal opportunity for LUAD (EOPp (LUAD); bootstrap test p value = 0.048), along with gender disparities in EOPp (LUAD; p < 0.0001) and EBAcc (p = 0.0059). In differentiating invasive ductal carcinoma (IDC) from invasive lobular carcinoma (ILC) of the breast, the baseline model showed significant age disparities in EOPp
^ILC^
 (p = 0.038) and EBAcc (p = 0.044). Additionally, the IDC/mixed IDC (IDC
^mix^
) vs. ILC task showed significant racial disparities in EOPp
^IDCmix^
 (p = 0.043) and EOPp
^ILC^
 (p = 0.043).

Frozen section-based models for intraoperative decision support revealed significant disparities in four classification tasks (Figures 2C and 2D). We observed significant racial disparities in the classification of glioblastoma multiforme (GBM) vs. low-grade glioma (LGG; EOPp
^GBM^
, p = 0.025), renal clear cell

<!-- PAGE 6 -->

# Cell Reports Medicine

## Article

OPEN ACCESS

carcinoma (KRCP), kidney chromophobe (KICH; 
EPF^{imm} = 0.001
), KIRC vs renal papillary cell carcinoma (KIRP; 
EPF^{imm} = 0.040
), and KIRP vs KICH (
EPF^{imm} = 0.05
). Across the 17 tumor types detected, tasks using frozen section slides from the TCGA cohorts, baseline models showed significant diagnostic disparity (Table S3). Specifically, we identified racial disparities in breast cancer (BRCA) detection (
EPF^{imm} = 0.021
; 
EBACC = 0.025
), the KIRP detection task showed gender (
EPF^{imm} = 0.026
) and age-related disparities (
EPF^{imm} = 0.029
; 
EBACC = 0.025
). In addition, the thyroid carcinoma (THCA) detection task exhibited gender-related disparity (
EPF^{imm} = 0.040
), while the stomach adenocarcinoma (STAD) detection task showed age-related disparity (
EPF^{imm} = 0.048
).

We found performance disparities mostly in underrepresented groups defined in medical studies,
^44,45^
 including racial minorities, females, or older age groups. Interestingly, 3 tasks showed lower performance in groups not underrepresented in the training cohorts. For example, we found lower performance for male patients in LUAD vs. LUSC classification using FFPE samples. Younger age groups also showed lower performance in IDC vs. ILC classification using FFPE samples and in the detection of KIRP and STAD (Figure S1A). Pairwise analysis between each self-reported race group revealed that most of the significant racial disparities were against American patients. Racial disparities against Asian patients were observed in only one task (IDC/mixed IDC vs. ILC using FFPE), likely due to insufficient statistical power from smaller sample sizes (Figure S1B).

Additionally, these biases could not be fully explained by tissue procurement site, scanner type, magnification, patient stage, or patch selection strategies (Figure S3). These results suggest a more complex role of model bias beyond technical factors and differences in healthcare access.

**Data imbalances, genomic variations, and morphological differences contributed to the demographic biases of stratified pathology AI models**

We further investigated sampling and molecular factors contributing to demographic biases in baseline models. Many TCGA cohorts have demographic imbalances (Table S1), and stratified diagnostic tasks show different demographic compositions between diagnostic classes (Table S3). We conducted subsample analysis by varying group imbalances in baseline models and discovered that imbalanced sample sizes between demographic subgroups significantly correlated with large biases (Figure 3A; Figure S3A). Furthermore, discrepancies in diagnosis prevalence between demographic groups, even with balanced sample sizes, contributed to demographic disparities (Figure S3B).

We further examined the relationship between the observed performance biases and the incidence of genomic mutations (see Methods for details). We found that differential incidence of genomic mutations correlated with performance gaps between groups. For example, variations in TP53 mutation rates are associated with differential error rates in IDC/mixed IDC vs. ILC, LUAD vs. LUSC, and GBM classification. Similar differences in CDH1 mutation rates were linked to significant racial disparity in IDC/mixed IDC vs. ILC and age discrepancy

in IDC vs. ILC classification. These genetic mutations have significantly different prevalences in patient groups defined by age, gender, and self-reported race (Wald test 
p
 value < 0.05) and are significantly associated with prediction errors in paired AI baseline models (Wald test 
p
 value < 0.05; Figure 3C). However, these same demographic factors are uncorrelated by AI models with significant accuracy (AUROCs = 0.556–0.769), bootstrap test 
p
 value < 0.05; see Table S3), a finding consistent with our results.

In addition, many cancer types associated with demographic bias showed demographic distinct imaging characteristics. Supervised machine learning analysis using pathology imaging features in lung cancer patients revealed significant distinctions in gene (AUROC = 0.659; DeLong test 
p
 value < 0.001) and gender (AUROC = 0.629; 
p
 value < 0.001). For breast cancer patients, imaging characteristics are significantly predictive of race (AUROC = 0.641; 
p
 value < 0.001) and age (AUROC = 0.571; 
p
 value < 0.001). We found significant racial distinctions across gender and cancer subtypes (AUROC = 0.690; 
p
 value < 0.001; 0.683, 
p
 value < 0.001), and KIRC vs. KICH (AUROC = 0.745, 
p
 value < 0.001). Stratification by cancer subtype reduced the significance of demographic differences in lung cancer (AUROC = 0.544; 
p
 value < 0.001) and age (AUROC = 0.544; 
p
 value < 0.001). For breast cancer, however, morphological patterns associated with race and age persisted within ductal and lobular subtypes (AUROC = 0.545–0.631; 
p
 < 0.05; Table S4). Stratified analyses showed that such distinctions in imaging characteristics remain significant after controlling for other demographic attributes as prevalent somatic mutations (Figure S4).

We next investigated the cellular basis for these demographic distinctions and found significant differences in tumor composition (Figure 2D). We observed consistent racial differences in tumor composition (Figure 2D; Table S5) between American patients had lower inflammatory and connective cell densities and higher overall and neoplastic cellularity than tumors from Caucasian patients (Mann-Whitney test 
p
 value < 0.001). Epithelial cell density was lower for African American patients than IDC/mixed IDC overall (Mann-Whitney test 
p
 value < 0.001). Age correlated with distinct morphological profiles across breast cancer subtypes: tumors from elderly patients contained higher overall and neoplastic cellularity, connective, and epithelial cell densities, but a higher neoplastic cell density (age < 0.001). Our findings are consistent with existing evidence that as a subset of Alzheimer’s disease pathology, strongly associated with demographic variables.
^46^

**FAIR-Path framework mitigates demographic biases in cancer pathology diagnosis**

We employed FAIR-Path to mitigate the fairness issues discovered by our systematic fairness evaluation. For each task where demographic models showed significant demographic bias, we use a same model architecture and trained it with FAIR-Path’s fairness-aware contrastive learning approach (Figure 1). We also reported the stratified and non-stratified models trained using a diverse set of performance metrics (see Table S2).

For FFPE-based tasks, FAIR-Path successfully mitigated all significant biases in the baseline models (Figure 4). We used existing fairness correction methods demonstrated resolution rates of up to 80% for EOPs, while one computing method (SMOTE)

ORCID: 0000-0002-1234-5678

ORCID: 0000-0003-9876-5432

ORCID: 0000-0001-2345-6789

Cell Reports Medicine 6, 102527, December 16, 2025

5

<!-- PAGE 7 -->

**Figure 3.**
 Data imbalances and morphological differences contributed to performance disparities among demographic groups in cancer diagnostic tasks

(A) A subsample analysis shows that performance differences between majority and minority populations increased as the sample size imbalance across demographic groups enlarged. The Spearman correlation between farness metrics and sample size balance is shown.

(B) A subsample analysis shows greater performance disparities as differences in diagnostic category distribution between majority and minority populations in the training set widened. The Spearman correlation between farness metrics and class balance in the minority groups is shown.

(C) Variations in somatic mutation rates partially explained performance discrepancies in baseline models across patient groups. We summarized the tasks where baseline models exhibited significant performance differences between patient groups, alongside covariates that simultaneously showed significant differences between demographic groups and significant association with predictive errors in baseline models. Whiskers in box plots indicate 1.5 × the interquartile range. “Wild” test 
*p*
 value < 0.05. “Wild” test 
*p*
 value < 0.01.

(D) Demographically distinct imaging features correspond to differences in cellular composition, including neoplastic, inflammatory, connective, and epithelial cell densities. Data are represented as mean ± SEM. Statistical comparisons between demographic subgroups were performed using the Mann-Whitney U test. BRCA: breast invasive carcinoma; LUAD: lung squamous cell carcinoma; LUAD: lung adenocarcinoma. “Mann-Whitney U test 
*p*
 < 0.05,” “
*p*
 < 10
^-3^
,” “
*p*
 < 10
^-5^
.” See also Figures S3 and S4, Tables S3-S6.

<!-- PAGE 8 -->

## Cell Reports Medicine

### Article

Cell Press

OPEN ACCESS

also achieved a 100% resolution rate for EBACs. For frozen section diagnostic tasks, FAIR-Patch mitigated 77.8% of the significant EOP biases and 75% of the EBACs biases (Figure 4B). This substantially outperformed the other competing methods. ASR and DBR, which achieved mitigation rates of 55.6% for EOPs and 65% for EBACs. Notably, the correction by FAIR-Patch exhibited no significant decrease in overall performance in nearly all tasks (bootstrap test p value > 0.05). The only exception was the race correction for LIAD vs. LUSC classification (p value < 0.001). In this case, the leading competing methods (ASR and DBR) failed to mitigate the bias and exacerbated the disparities (Figure 4C and 4D).

Furthermore, bias mitigation by FAIR-Patch preserved pathological variants for clinically relevant biomarkers with high diagnostic variations in prevalence (Table S3). In addition, FAIR-Patch model ensembles can achieve enhanced fairness across multiple demographic attributes (Figure S5A). In scenarios where FAIR-Patch successfully mitigated baseline biases, intersectional fairness analyses revealed no significant bias across subgroups (Figure S5B). We project that fairness improvements by FAIR-Patch could prevent thousands of misdiagnoses among female patients in the U.S. with underrepresented racial groups. For example, in classifying IDC-invasive IDC, ILC among African American female patients, the fairness improvement of FAIR-Patch will prevent the misdiagnosis of approximately 5,092 African American female patients each year (Table S3). However, some biases persisted after mitigation through FAIR-Patch, occurring exclusively in frozen section evaluation tasks (EBM vs. LGG classification and KIRC vs. KIRP classification).

We further conducted ablation studies to validate the efficacy of our framework (see Methods). First, an otherwise identical supportive contrastive learning model without the proposed fairness objective exhibited significant demographic bias in 4 of 8 tasks, demonstrating that contrastive learning alone is insufficient to ensure fairness (Figure 4E). Second, we tested whether demographic bias is a proxy for site-related factors by adapting FAIR-Patch to correct site-related bias. Consequently, site-related bias did not eliminate demographic disparities, as 9 (out of 12 tasks retained persistent demographic bias after site correction (Figure 4F and Figure S5C). This indicates that demographic bias arises from mechanisms more complex than site-specific variations, reinforcing the need for our explicit fairness approach. Lastly, we assessed the reliability of FAIR-Patch in low-data regimes by training it on progressively smaller subsets of the training data. We found that FAIR-Patch's ability to mitigate bias was preserved under reduced training sample sizes, demonstrating its robustness (Figure S5C).

**Independent validation demonstrated the generalizability of fairness enhancement by FAIR-Patch.**

We tested the generalizability of FAIR-Patch on FFPE and frozen section slides from 15 independent validation cohorts not involved in model development. After training on the FFPE cohort with 10,000 group samples, we evaluated 39 classification settings across all diagnostic tasks, tissue sources, and demographic attributes (Table S3).

We found that standard pathology AI models exhibited significant biases in 60% of tumor detection tasks, 40% of cancer type classification tasks, and half of cancer subtype classification tasks across independent validation cohorts (Figure 5). In particular, we observed significant gender disparities in GBM vs. LGG classification in the DFCI FFPE cohort and gender disparities in both the MGB and DFCI FFPE cohorts. For KIRC vs. KIRP classification, we found significant disparities in the age of the cohort. The LIAD vs. LUSC classification models showed significant age bias in the CPTAC cohort, along with both gender and age bias in the TCGA cohort. In the COAD vs. READ classification, the standard model demonstrated significant age and gender disparities in the DFCI cohort. For bronchial/pleural carcinoma detection from other LIAD in the PCLO cohort, the baseline model showed significant age bias. In tumor detection tasks across the CPTAC and TCGA cohorts, we observed significant age disparities for detecting both KIRC and LIAD. In addition, only 3 out of 9 tasks that showed significant bias in independent cohorts also demonstrated significant bias in the COAD vs. READ cohorts. These differences highlight distributional shifts between cohorts and the robustness of FAIR-Patch.

Among the biased diagnostic tasks in external FFPE cohorts, FAIR-Patch successfully mitigated 88.9% of the observed EOP disparities and 100% of the observed EBAC disparities. Other methods were less effective: LFR achieved the next highest resolution rates, resolving 55.6% of EOP bias and 100% of EBAC bias, while other methods ranged from 44.4 to 55.6% for EOP and up to 66.7% for EBACs. The only instance where FAIR-Patch did not fully mitigate bias was in the COAD vs. READ classification in the DFCI dataset. Notably, none of the other methods succeeded in this task. All FAIR-Patch-corrected tasks in the independent FFPE cohorts showed no significant drop in overall AUROC performance (one-sided bootstrap test p value > 0.05) (Figure 5B and Figure S6). This demonstrates that FAIR-Patch also showed no significant AUROC drop. AdFair and SMOTE caused significant AUROC declines in 30% and 10% of tasks, respectively.

In the frozen section cohorts, FAIR-Patch eliminated all significant biases (Figure 5C and Figure S6). In contrast, other methods exhibited complete bias mitigation, while other fairness correction methods showed slightly lower resolution rates: ASR and DBR resolved 10% of EOP biases and 10% of EBAC disparities. AdFair and SMOTE achieved 100% resolution for EOPs and 66.7% for EBACs. Notably, FAIR-Patch showed a significant AUROC drop in the LIAD detection task, which was observed in the substantial performance-fairness trade-offs with AdFair and LFR (Figure 4D).

**FAIR-Patch enhanced fairness in pathology foundation models.**

Pathology foundation models
^31–34^
—large models pretrained on pathology slides using self-supervised learning—have great translational interest for their strong performance and generalizability. However, prior studies have shown that these models exhibit demographic disparities, which are often not explicitly addressed during downstream training.
^35^
 To demonstrate the utility of FAIR-Patch in this context, we evaluated fairness metrics on three state-of-the-art pathology foundation models (CHEF
^36^
, UNI
^37^
, and GigaPath
^38^
) in cancer classification tasks across TCGA cohorts. Our result showed that, without a fairness

<!-- PAGE 9 -->

**Figure 4.**
 FAIR-Path more effectively mitigated biases in critical cancer diagnostic tasks compared to existing methods

Cases are represented as micro-averaged metrics.

(A) Bias mitigation in diagnostic tasks using FFPE samples. FAIR-Path (red bars) eliminated significant biases in both equal opportunity and equal balanced accuracy across all tasks. In contrast, success rates for other methods ranged from 33.4% to 86.7%. Red asterisks indicate significant disparities.

(B) Bias mitigation in diagnostic tasks using frozen section samples. FAIR-Path mitigated biases in 75% of tasks with equal balanced accuracy bias and 77.8% of those with equal opportunity bias, respectively. This surpassed other fairness correction methods, which corrected only 31.3%–53.6% of such tasks.

(C) FAIR-Path improves both fairness and performance in FFPE-based pathology evaluation. For tasks with significant bias in baseline models (black dots), FAIR-Path (red crosses) consistently reduced bias while increasing overall AUCROC.

(D) We observed similar gains by FAIR-Path in frozen section samples. Among tasks showing performance disparities, FAIR-Path (red crosses) consistently reduced bias in baseline models (black dots) and enhanced overall AUCROC.

ASF: adaptive sensitive reweighting; LPR: learning for representation; SMOTE: synthetic minority over-sampling technique. *bootstrap test p-value < 0.05. See also Figures S5 and S6, Tables S1, S2, S6, and S7.

<!-- PAGE 10 -->

# Cell Reports Medicine

## Article

OPEN ACCESS

**Figure 5.**
 Baseline models showed significant performance disparities in cancer diagnosis tasks across population groups in external validation cohorts

Higher value reflect greater disparity. Significant bases are marked with asterisks.

(A) Cancer-type classification (FPPE) analyzed. Baseline models showed significant performance disparities between demographic groups in 41.7% of these tasks, including GCAD vs. READ in the DFCI cohort, GBM vs. LGG in the DFCI and UPenn cohorts, KIRC vs. KIRP in the DFCI cohort, and LUAD vs. LUSC in the PDC cohort.

(B) Subtype classification (FPPE). BAC vs. LUAD classification showed significant age disparity in the PDC cohort.

(C) Cancer-type classification (tumor sections). LUAD vs. LUSC classification showed significant age disparity in the CPTAC cohort.

(D) Tumor detection (tumor sections). 50% of these tasks showed significant age disparity, including the detection of KIRC and LUAD in the CPTAC cohort.

*bootstrap test p value <0.05. See also Tables S1 and S2.

constraint, foundation model-based diagnostic classifiers displayed significant performance disparities by age, gender, and self-reported race, with CHIEF exhibiting the highest bias rate (77.8%), followed by UAI (66.7%) and GigaPath (66.7%; see Figure 7A). Applying FAIR-Path successfully mitigated these disparities in 73.7%, 66.7%, and 57.1% of tasks for CHIEF, GigaPath, and UAI, respectively (Figure 7B). These findings demonstrate the effectiveness of FAIR-Path in enhancing fairness in both standard end-to-end training pipelines and state-of-the-art foundation models. Notably, the racial bias in KIRC vs. KIRP classification, which was observed consistently across all foundation models, remained significant after applying FAIR-Path. Our analysis revealed a notable difference between this task and those where bias was consistently mitigated (IOC vs. ILC and SUEC vs. nsLUCEC). In the latter cases, we found significant racial disparities in the prevalence of common mutations, whereas no such disparities were observed in KIRC or KIRP (Table S7). These findings suggest that FAIR-Path is more effective when demographic bias is linked to differences in genomic profiles but may be less so when disparities originate from non-mutational factors.

### DISCUSSION

Despite rapid advancements in AI, fairness issues in real-world medical diagnostic tasks remain a pressing concern. Our pan-

cancer fairness analysis demonstrated that standard AI diagnostic models and advanced pathology foundation models can inadvertently discriminate against patients from underrepresented subpopulations, even when overall performance appears strong. AI models can encode representation biases from demographically imbalanced pre-training datasets, and their downstream training is vulnerable to shortcut learning—a risk that persists regardless of the feature encoder’s representational power unless fairness constraints are explicitly applied. These findings highlight the importance of fairness evaluation and the urgent need for equitable frameworks in AI pathology to prevent perpetuating health disparities. To address this, we introduce FAIR-Path, a fairness-aware contrastive learning framework designed to enhance fairness in AI-empowered pathology image evaluation. Through extensive experiments across multiple cancer types and external validation involving five medical centers and three nationwide study cohorts, we demonstrated that FAIR-Path, coupled with fairness auditing, successfully reduced performance disparities across demographic subgroups in both standard AI diagnostic models and pathology foundation models. This framework represents a promising step forward in addressing the ethical and fairness challenges in pathology AI diagnosis.

We found that demographic attributes are associated with tumor histology differences detectable by AI models. In older patients, tumors consistently exhibit increased stromal volume and diminished inflammatory infiltration compared to younger

Cell Reports Medicine 6, 102527, December 16, 2025 9

<!-- PAGE 11 -->

**Figure 6. FAB-Path mitigated biases in cancer diagnostic tasks across 15 external validation cohorts, outperforming existing methods**

(A) FFPE-based diagnostic tasks. FAB-Path (red bars) is compared to standard deep learning models (black bars) and other correction methods. Red asterisks indicate significant bias. FAB-Path resolved 89.9% of significant baseline biases in equal opportunity and 100% in equal balanced accuracy. LFR achieved the second-highest resolution rates, resolving 56.6% and 100% for equal opportunity and equal balanced accuracy, respectively.

(B) Diagnostic tasks using frozen sections. FAB-Path corrected all significant baseline biases, whereas other methods achieved resolution rates of 80%-100% for equal opportunity and 75%-100% for equal balanced accuracy, respectively.

(C) Fames vs. performance in FFPE-based tasks with significant baseline bias. FAB-Path (red markers) reduced bias without compromising AURCC, outperforming baseline models (black dots) and other methods. Stars indicate no significant bias or AURCC drops. Arrows indicate significant change from baseline. A downward arrow indicates significant bias, a leftward arrow indicates a drop in AURCC, and an upper-left arrow indicates both.

(D) Fames vs. performance in frozen section diagnostic tasks with significant baseline bias. FAB-Path resolved biases without significantly reducing overall AURCC or tasks including LUSD vs. LUSD classification and KIRC detection. In the LUSD detection task, AdFair, SMOTE, and FAB-Path all exhibited significant AURCC drops compared to the baseline model.

ADB: adaptive sensitive reweighting; LFR: learning fair representation; SMOTE: synthetic minority over-sampling technique. *Bootstrap test p-value < 0.05. See also Tables S1 and S2.

<!-- PAGE 12 -->

Cell Reports Medicine

Article

Cell Press

OPEN ACCESS

A

B

Figure 7. FAIR-Path mitigates bias in pathology foundation models

Data are represented as micro-averaged metrics.

(A) Pathology foundation models exhibited sex, gender, and age bias in classifying cancer types and subtypes. When trained without demographic bias correction, all evaluated foundation models (CHEF, GigaPath, and LUN) exhibited significant performance disparity in 66.7%–77.8% of the classification tasks. Asterisks indicate statistically significant disparities between demographic subgroups.

(B) In tasks where stratified pathology foundation models (CHEF, GigaPath, and LUN) exhibited significant performance disparities (black bars), FAIR-Path (red bars) eliminated these biases in 73.7%, 66.7%, and 57.1% of tasks for each model, respectively.

*Bootstrap test p value < 0.05. See also Tables S1 and S2.

patients. This pattern aligns with established features of aging tissues, including fibroblast senescence, extracellular matrix accumulation, and immune exclusion.
^104^
 Similarly, tumors from African American patients show a higher density of neoplastic cells and a lower presence of immune and stromal components compared to those from Caucasian patients. This histologic profile is consistent with prior reports of elevated levels of CD163
^105^
 tumor-associated macrophages
^106^
 and exhausted CDB
^107^
 T cells
^108^
 in tumors from individuals of African ancestry, both of which are linked to impaired immune surveillance. Higher

Cell Reports Medicine 6, 102527, December 16, 2025 11

<!-- PAGE 13 -->

CELL PRESS
OPEN ACCESS

Cell Reports Medicine
Article

microvesSEL density has also been reported in tumors from African American patients, suggesting enhanced angiogenesis and stromal remodeling.
^10^
 Collectively, these observations indicate that morphological variations in tumors with demographic differences are embedded in tissue architecture and can be inadvertently overlooked by AI models.

Our analyses revealed that differences in sample sizes, class distribution, and morphological variations between demographic groups contributed to disparities in performance in pathology diagnosis. The significant demographic biases we identified align with well-documented demographic differences in disease prevalence for several cancer subtypes, including renal,
^11^
 lung,
^12^
 brain,
^13^
 breast,
^14^
 and stomach cancers.
^15^
 In addition, we showed that disparities in mutation prevalence (particularly for TP53 and CDH1), partially explain performance disparities in baseline models across several diagnostic tasks. For example, TP53, the most commonly mutated gene in solid-organ cancers,
^16^
 has shown significant differences in mutation rates across races and gender based on the TCGA.
^17^
 Conversely, CDH1 mutations are important markers for invasive lobular carcinoma (ILC),
^18^
 are more prevalent in late-onset breast cancer,
^19^
 and are more common in Caucasian populations (breast, gastric, and colorectal cancers).
^20^
 Pathology AI can identify cell morphology associated with genetic aberrations,
^21^
 which is also further confirmed by our experimental results. Disparities in gene mutation incidence across populations may contribute to subtle morphological differences, leading to variations in AI model performance across demographic groups that are not fully attributable to technical factors.
^22^
 This is supported by our analyses, where demographic factors played after accounting for technical variables. Thus, AI-based cancer diagnostic tools should account for these morphological consequences to minimize bias. This underscores the importance of implementing fairness-aware data collection processes and training strategies.

We observed that FAIR-Path’s efficacy is consistently lower for frozen section samples. This reduced efficacy may arise from the greater variability in staining inherent to frozen section slides,
^23^
 attributable to variable staining profiles, inconsistent artifacts, and thicker samples. To address these limitations, additional solutions to improve quality-control pipelines, advanced data preprocessing, and domain adaptation techniques.
^24^
 Ultimately, building a large, multi-institutional repository of standardized frozen section slides will improve these technical solutions and further reduce biases. These strategies chart a path toward enhanced fairness and reliability for intra-operative diagnostic assessment.

In summary, our systematic pan-cancer analysis revealed that standard computational paradigms frequently exhibit significant demographic biases, disproportionately affecting underrepresented racial groups, and leading to disparities and other inconsistencies. In addition, we identified the molecular and sampling factors contributing to these disparities. By incorporating fairness-aware generative learning into our framework, we successfully mitigated these performance gaps across a wide range of pathology evaluation tasks in diverse external cohorts. These enhancements in AI-driven diagnostic models will enable more equitable diagnostic assessments, reducing the risk of misdiagnosis and enhancing patient outcomes.

### Limitations of the study

Our study has a few limitations. First, our racial group investigation was limited to Caucasian, African American, and Asian patients. Biases against other racial groups, such as Hispanic Native Americans, Alaska Natives, or Pacific Islanders, could not be reliably evaluated due to the limited sample sizes of these non-cancer patient populations. These populations were limited to individual data distributions. Understanding how multiple demographic factors interact could provide further insights into the complex mechanisms of algorithmic bias, but interventional analysis
^25,26^
 is particularly challenging due to the limited sample sizes of interventional subgroups examined by multiple demographic factors. Furthermore, although we explained some performance disparities through differences in gene mutation prevalence, gene distribution, and genomic profiles, other potential explanations of bias—such as disparities in socioeconomic status,
^27^
 population differences between regions, areas, or different racial or comorbidities
^28,29^
—remain to be explored. Finally, systematic fairness evaluation of AI models for cancer and AI diagnostic language models
^30,31^
 is needed to further examine their performance in diverse populations.

### RESOURCE AVAILABILITY

**Lead contact**
Data access requests should be directed to the lead contact, Kun-Heng Yu (kun-heng_yu@hsph.harvard.edu), and will be forwarded to the managers of the various internal databases. These data are strictly only for non-commercial academic use.

**Materials availability**
This study did not generate new unique reagents.

**Data and code availability**

- The digital pathology slides, summarized clinical data, and biospecimen information for The Cancer Genome Atlas (TCGA) and Clinical Proteomic Tumor Analysis Consortium (CPTAC) cohorts are available through the National Cancer Institute’s Data Commons (https://datacommons.cancer.gov/cancer). Summarized molecular data for these cohorts are available from dbGaP (https://www.ncbi.nlm.nih.gov/gap). Data from the Proteintum, Lung, Colorectal and Ovarian (PCO) Cancer Screening Trials can be obtained from the NCCTG Data Commons (https://datacommons.cancer.gov/cancer). Data from the Medical University of Vienna can be available through the EMBL-EBI (https://www.ebi.ac.uk/). Datasets from Mayo Clinic, Dana-Farber Cancer Institute (DFCI), University of Pennsylvania (UPenn), and Mass General Brigham (MGB) are not publicly available due to patient privacy concerns and data use agreement requirements. To request access to these data, please contact the lead contact, Kun-Heng Yu (kun-heng_yu@hsph.harvard.edu). This request must describe the objectives of the research project for which the data will be used. We aim to forward all requests to the managers of these institutional datasets within 2 weeks, and these requests will be evaluated according to institutional policies. Data access will be considered for research purposes and non-commercial use only. In order to ensure data privacy, access to potentially identifiable information or sensitive clinical information will not be provided, and requests for access should not specifically adhere to the consent agreements established with study participants.
- All original code and data used to develop GATBUD and G publicly available as of the date of publication. The code for our model and data analysis can be found at https://github.com/hsph-ai/GATBUD.
- Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request.

12 Cell Reports Medicine 6, 102527, December 16, 2025

<!-- PAGE 14 -->

# Cell Reports Medicine

## Article

OPEN ACCESS

### ACKNOWLEDGMENTS

We thank Alesia Hughes, Faith McDonald, Catherine Burnham, and Mariam Kepafora for their administrative support. We thank Sunyi Lin for her technical assistance and Dr. Mckinley Tate for her help in grouping pathology subtypes. K.-H.Y. is partially supported by the National Institute of General Medical Sciences grant R01GM100949 (to Drs. David Hauss, and David Gilbert) and the National Institute of General Medical Sciences grant R01HL174679, the Department of Defense Peer Reviewed Cancer Research Grant Award (to Drs. David Hauss, and David Gilbert) (DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81XWH-13-1-0033) (grant DOD W81XWH-13-1-0032 and W81

<!-- PAGE 15 -->

**CellPress**

OPEN ACCESS

**Cell Reports Medicine**

Article

11. Yu, K.H., Wu, Y., Wang, F., Matushko, I.A., Muller, G.L., Golden, J.A., and Kohnen, E.S. (2020). Deep-learning versus ovarian carcinoma histopathology and pathogen response by convolutional neural networks. 
*BMC Med. Res. Meth.*
 16, 238. 
[https://doi.org/10.1186/s12874-020-01064-0](https://doi.org/10.1186/s12874-020-01064-0)

12. Yu, K.H., Zhang, C., Berry, D.J., Althaus, R.R., Ito, K., Rubin, D.L., and Kohnen, E.S. (2019). Predicting tumor response using deep learning in automated microscopic pathology image features. 
*Nat. Commun.*
 7, 12474. 
[https://doi.org/10.1038/s41467-019-10747-7](https://doi.org/10.1038/s41467-019-10747-7)

13. Fogle, A.L., and Kveher, J.C. (2018). Artificial intelligence powers digital pathology. 
*Diagn. Pathol.*
 13, 1. 
[https://doi.org/10.1186/s13000-018-0712-2](https://doi.org/10.1186/s13000-018-0712-2)

14. Alwaisi, A.S., Alghamdi, S.S., Alsubaheeh, N., Alghamdi, T., Althaya, A.I., Almohareb, S.N., Aldaheri, A., Alnashed, M., and Saini, K., Buchholz, N.A., and Kohnen, E.S. (2023). Revolutionizing healthcare with artificial intelligence in clinical practice. 
*BMC Med. Res. Meth.*
 23, 689. 
[https://doi.org/10.1186/s12874-023-01608-0](https://doi.org/10.1186/s12874-023-01608-0)

15. Ouyoude, K.B., Can, S., Daraba, B., Bagale, K., Derry, D., Gokeler, G.I., Serr, G., Iacchetti, L., and Kohnen, E.S., Liu, M.Y., et al. (2020). A deep-learning model for transforming the style of tissue images from cryosections to formalin-fixed and paraffin-embedded. 
*Nat. Biomed. Eng.*
 4, 1407–1419. 
[https://doi.org/10.1038/s41551-022-00902-9](https://doi.org/10.1038/s41551-022-00902-9)

16. Yu, K.H., Healey, E., Leong, T.Y., Kohnen, I.S., and Maresca, A.K. (2024). Artificial intelligence and pathology. 
*Cell Rep. Med.*
 5, 101749. 
[https://doi.org/10.1016/j.xcrm.2024.101749](https://doi.org/10.1016/j.xcrm.2024.101749)

17. Zhang, T., and Kveher, J.C. (2020). Artificial Intelligence. 
*Cell Rep. Med.*
 1, 100044. 
[https://doi.org/10.1016/j.xcrm.2020.100044](https://doi.org/10.1016/j.xcrm.2020.100044)

18. Cancer Genome Atlas (TCGA): an immensurable source of knowledge. 
*Cortisep. Oncol.*
 19, 488–497. 
[https://doi.org/10.1186/s12874-018-0518-0](https://doi.org/10.1186/s12874-018-0518-0)

19. Edwards, N.J., Oberb, M., Thanapudi, R.R., Cai, S., McEvoy, P.B., Jacobs, S., Madsen, W., and Kothapalli, K.A. (2015). The CPTAC Data Portal: A Resource for Cancer Proteomics Research. 
*J. Proteome Res.*
 14, 2700–2713. 
[https://doi.org/10.1021/pr501254a](https://doi.org/10.1021/pr501254a)

20. Kohnen, D.F. (2018). Are we inadvertently widening the disparity gap in pursuit of precision oncology? 
*Br. J. Cancer.*
 119, 783–784. 
[https://doi.org/10.1038/s41416-018-02216-0](https://doi.org/10.1038/s41416-018-02216-0)

21. Chen, R.J., Wang, J.J., Williamson, D.F.K., Chen, T.Y., Liskevicius, J., Liu, M.Y., Sahu, S., and Mahmood, F. (2023). Algorithmic fairness in artificial intelligence for medicine and healthcare. 
*Nat. Biomed. Eng.*
 7, 719–732. 
[https://doi.org/10.1038/s41551-023-00918-8](https://doi.org/10.1038/s41551-023-00918-8)

22. Ashktorab, H., Kugler, S.S., and Kohnen, E.S., and Malmstrom, J.M. (2017). Racial Disparity in Gastrointestinal Cancer Risk. 
*Gastroenterology*
 153, 1536–1544.e1. 
[https://doi.org/10.1053/j.gastro.2017.07.018](https://doi.org/10.1053/j.gastro.2017.07.018)

23. Crockett, B.C., and Soto, G.P. (2017). Racial Differences in Cancer Susceptibility and Survival: More than the Color of the Skin? 
*Trends Cancer*
 3, 198–204. 
[https://doi.org/10.1016/j.trecan.2017.02.002](https://doi.org/10.1016/j.trecan.2017.02.002)

24. Du, X.L., Li, C.C., Johnson, N.J., and Althaus, S. (2011). Effects of individual socioeconomic factors on racial disparities in cancer incidence and survival. 
*Cancer*
 117, 2542–2551. 
[https://doi.org/10.1002/cncr.26450](https://doi.org/10.1002/cncr.26450)

25. Vaidya, A., Chen, R.J., Williamson, D.F.K., Song, A.H., Jauma, G., Yang, Y., Hanington, T., Dyer, E.C., Liu, M.Y., Liskevicius, J., et al. (2024). Demographic bias in misdiagnosis by commercial pathology algorithms. 
*Nat. Med.*
 30, 1174–1193. 
[https://doi.org/10.1038/s41591-024-02898-2](https://doi.org/10.1038/s41591-024-02898-2)

26. Chen, M., Dossai, J., Bhandari, A., and White, J., Chen, T.Y., He, L., Huo, D., Nanda, R., Olopade, O.I., Kather, J.N., et al. (2023). The impact of phenotypic digital pathology signatures on deep learning model accuracy and bias. 
*Nat. Commun.*
 12, 4423. 
[https://doi.org/10.1038/s41467-023-36589-0](https://doi.org/10.1038/s41467-023-36589-0)

27. Gerber, R., Jacobsen, J.H., Michaels, G., Zemel, R., Brändel, W., Bethge, M., and Wichmann, F.A. (2020). Shortest learning in deep neural networks. 
*Nat. Mach. Intell.*
 2, 665–674. 
[https://doi.org/10.1038/s42256-020-00237-0](https://doi.org/10.1038/s42256-020-00237-0)

28. Yu, K.H., Marm, A.L., and Kohnen, E.S. (2018). Artificial intelligence in healthcare. 
*Nat. Biomed. Eng.*
 2, 719–723. 
[https://doi.org/10.1038/s41551-018-0303-0](https://doi.org/10.1038/s41551-018-0303-0)

29. Administration, F.A.D. (2018). Proposed regulatory framework for modifications to artificial intelligence/machine learning (AI/ML)-based software as a medical device (SaMD). 
[https://www.fda.gov/media/130388/download](https://www.fda.gov/media/130388/download)

30. Kamran, F., and Caiden, J. (2015). Data preprocessing techniques for classification without dimensionality. 
*Knowl. Inf. Syst.*
 53, 1–33. 
[https://doi.org/10.1007/s10115-015-0807-0](https://doi.org/10.1007/s10115-015-0807-0)

31. Franchet, C., Schwab, R., Batalion, G., Synytskiy, C., Freyssinet, S., Frenou, F., Xu, Benabid, A.L., and Benabid, A.L. (2019). Deep learning in Parkinson’s disease: Bias reduction using combined stain normalization and augmentation by a based classification of histological images. 
*Comput. Biol. Med.*
 107, 103810. 
[https://doi.org/10.1016/j.compbiomed.2019.103810](https://doi.org/10.1016/j.compbiomed.2019.103810)

32. Khan, I., Wiles, D., Abubakar, I., Neufeld, S.A., Tanno, R., Roy, A.G., Alizai, S., Belagundu, S., and Cottam, C. (2020). ePathAI: the ePathAI AI for image classification of medical specimens under distribution shifts. 
*Nat. Med.*
 26, 1166–1172. 
[https://doi.org/10.1038/s41591-020-0900-0](https://doi.org/10.1038/s41591-020-0900-0)

33. Shen, A., Itoh, Y., Cohn, T., Baldwin, T., and Freeman, L. (2023). Contrasting learning for medical image classification. 
*Preprints*
 at arXiv. 
[https://doi.org/10.20944/preprints202305.0065.v1](https://doi.org/10.20944/preprints202305.0065.v1)

34. Thanapudi, E., Barbano, C.A., and Grangier, M. (2021). End-Enabling and disentangling deep learning for medical image classification. 
*arXiv*
 arXiv:2106.04850v1 [cs.CV]. 20210330.

35. Zhang, T., and Zhang, X. (2023). Deep Learning in Cancer and Accuracy of Digital Histopathology. 
*Preprints*
 at arXiv. 
[https://doi.org/10.20944/preprints202301.0201.v1](https://doi.org/10.20944/preprints202301.0201.v1)

36. Wu, Y., Zeng, X., Xu, S., Xie, Y., and Hu, L. (2023). FairPine: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis. 
*arXiv*
 arXiv:2301.00000v1 [cs.CV]. 20230101.

37. Zhang, B.H., Lennox, B., and Mitchell, M. (2018). Mitigating Unwanted Biases in Deep Learning. In 
*Proceedings of the 2018 AAAI Conference on AI, Ethics, and Society (Association for Computing Machinery)*
.

38. Madras, D., Creager, E., Pitassi, T., and Zemel, R. (2018). Learning Adversarially Fair and Transferable Representations. In 
*Proceedings of Machine Learning Research*
, D. Levine, ed. (PMLR), pp. 539–555.

39. Zong, Y., Yang, Y., and Hospedales, T. (2023). MEDFair: Benchmarking Fairness in Medical Imaging. 
*Preprint*
 at arXiv. 
[https://doi.org/10.48550/arXiv.2310.01722](https://doi.org/10.48550/arXiv.2310.01722)

40. Hossein, S.M., Skarzadeh, M., Babaei, M., and Tchoupo, H.R. (2023). Prognostic factors for hepatocellular carcinoma: a systematic review of prognostic images. 
*IEEE Trans. Med. Imaging*
 42, 1982–1996. <a href="https://doi.org/10.1109/tmi.202

<!-- PAGE 16 -->

# Cell Reports Medicine

Article

OPEN ACCESS

https://doi.org/10.1016/j.xcrm.2025.03.019

Cell Reports Medicine 6, 100257, March 25, 2025

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1–15

100257

1

<!-- PAGE 17 -->

OPEN ACCESS

## Cell Reports Medicine

Article

75. Ho, M.M., Dubey, K., Chong, Y., Knudsen, B., and Tazdzien, T. (2023). F2PLM: Latest Diffusion Models with Histopathology Pre-Trained Embeddings for Unpaired Frozen Section Section to FFPE Translation. 
*IEEE*
, pp. 4382–4391.

76. Fairbanks-Kok, K., Guo, T., Huang, M., Tertool, P., Wood, C.D., Keren, J.A., Serac, I., and Bhargava, R. (2023). A generative adversarial approach to facilitate artificial-intelligence diagnostics from frozen tissue sections. 
*Lab. Invest.*
 102, 564–586. 
[https://doi.org/10.1038/s41374-023-00718-7](https://doi.org/10.1038/s41374-023-00718-7)
.

77. Nakhli, R., Rich, K., Zhang, L., Dantanaray, A., Shrestha, E., Hajizadeh, A., Thessen, S., Mina, K., Jones, S.I.M., McAlpine, J.N., et al. (2024). VOLTA: an environment-aware Contrastive cell representation learning for histopathology. 
*Nat. Commun.*
 15, 3942. 
[https://doi.org/10.1038/s41467-024-48062-7](https://doi.org/10.1038/s41467-024-48062-7)
.

78. Havelka, D., Doyal, L., Erozan, G., Kelly, U., Stein, J., Weder, L., and Reetz, R. (2017). The odd couple: using biomedical and informational approaches to address health inequities. 
*Global Health Action*
 10, 1326898. 
[https://doi.org/10.1080/16549716.2017.1326898](https://doi.org/10.1080/16549716.2017.1326898)
.

79. Tuzun, J.M., Batra, M.A., Lopé, C.H., Bank, S., Tuan, N., Crockett, K.B., Pencovich, B., and Murray, S.M. (2018). Challenges and opportunities in examining and addressing informational stigma and health. 
*BMC Med.*
 17, 7. 
[https://doi.org/10.1186/s12916-018-1246-6](https://doi.org/10.1186/s12916-018-1246-6)
.

80. Duffy, G., Clarke, S.L., Christensen, M., He, B., Yuan, N., Cheng, S., and Ouyang, D. (2023). Confounders mediate AI prediction of demographics in medical imaging. 
*Int. Org. Med. S.*
 188. 
[https://doi.org/10.1038/s41774-023-00720-3](https://doi.org/10.1038/s41774-023-00720-3)
.

81. Wang, X., Yang, S., Zhang, J., Wang, M., Zhang, J., Yang, W., Huang, J., and Han, X. (2023). Transformer-based unsupervised contrastive learning for histopathological image classification. 
*Med. Image Anal.*
 81, 102559. 
[https://doi.org/10.1016/j.medica.2022.102559](https://doi.org/10.1016/j.medica.2022.102559)
.

82. Kung, M., Song, H., Park, S., Yoo, D., and Rivera, S. (2023). Benchmarking self-supervised learning on diverse pathology datasets. In 
*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*
, pp. 3344–3354.

83. He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. In 
*Proceedings of the IEEE conference on computer vision and pattern recognition*
, pp. 770–778.

84. Khosla, P., Teterwak, P., Wang, C., Sarna, A., Tian, Y., Isola, P., Maschler, A., Liu, C., and Krishnan, D. (2020). In supervised contrastive learning. 
*H. Larochelle, M. Ranzato, R. Hadsell, M.F. Batacan, and H. Lin*
, eds. Curran Associates, Inc., pp. 1461–1467.

85. Nar, V., and Hinton, G.E. (2010). Rectified linear units improve restricted boltzmann machines. In 
*Proceedings of the 27th International Conference on Machine Learning (ICML-10)*
, pp. 807–814.

86. Mackinnon, J.G. (2008). Bootstrap hypothesis testing. In 
*Handbook of Computational Econometrics*
 (Wiley), pp. 185–215. 
[https://doi.org/10.1002/9780470274816](https://doi.org/10.1002/9780470274816)
.

87. Hörst, F., Hengst, M., Harsa, L., Saboci, C., Keyl, J., Biedler, D., Ugiara, S., Svele, J., Grönwall, E., Egger, J., and Hessele, J. (2024). Gohr: Vision transformers for precise cell segmentation and classification. 
*Med. Image Anal.*
 84, 102143. 
[https://doi.org/10.1016/j.medica.2024.102143](https://doi.org/10.1016/j.medica.2024.102143)
.

88. Verwe, J., Plaisance, A., Bousquet, G., Lehmann-Cha, J., de Bazelaire, C., Soufir, N., and Mongiart-Artus, P. (2019). Hereditary Renal Cancer Syndromes: An Update of a Systematic Review. 
*Eur. Urol.*
 86, 701–710. 
[https://doi.org/10.1016/j.eururo.2019.08.031](https://doi.org/10.1016/j.eururo.2019.08.031)
.

89. Orphanet (2022). Hereditary papillary renal cell carcinoma. 
[https://www.orpha.net/consor/cgi-bin/OC_0004744.php](https://www.orpha.net/consor/cgi-bin/OC_0004744.php)
.

90. Jacaba, I.M., and Lu, Z. (2024). Hereditary papillary renal cell carcinoma. 
*Semin. Diagn. Pathol.*
 41, 28–31. 
[https://doi.org/10.1053/j.sempd.2023.12.002](https://doi.org/10.1053/j.sempd.2023.12.002)
.

16

Cell Reports Medicine 6, 102527, December 16, 2025

<!-- PAGE 18 -->

# Cell Reports Medicine

## Article

### STAR+METHODS

#### KEY RESOURCES TABLE

| REAGENT OR RESOURCE | SOURCE | IDENTIFIER |
| --- | --- | --- |
| Deposited data |  |  |
| Digital pathology slides and summarized clinical data (TCGA) | National Cancer Institute - Genomic Data Commons (GDC) | [https://portal.gdc.cancer.gov](https://portal.gdc.cancer.gov) |
| Digital pathology slides (CPTAC-3) | National Cancer Institute/GDC | [https://portal.gdc.cancer.gov](https://portal.gdc.cancer.gov) |
| Summarized molecular profiles (TCGA/CPTAC) | cBioPortal | [https://cBioPortal.org](https://cBioPortal.org) |
| PLOO Cancer Screening Trial data | NCI Cancer Data Access System (CDAS) | [https://cdas.cancer.gov/plooo](https://cdas.cancer.gov/plooo) |
| Medical University of Vienna cohort portal | EBI/EnAble | [https://ebi-via.ebi.ac.uk](https://ebi-via.ebi.ac.uk) |
| Software and algorithms |  |  |
| FAIR/Patch source code (model and analysis) | GitHub | [https://github.com/hms-dbmi/fairpatch](https://github.com/hms-dbmi/fairpatch) |
| NOIA-NCC-PyTorch tissue sticker image (development environment) | NOIA-NCC | 22.03 |
| Python (main program language) | Python | 3.8 |
| PyTorch (internal validation) | PyTorch | 2.0.0 |
| Numpy (numerical operations) | Numpy | 1.22.4 |
| Scikit-learn (metric calculation) | Scikit-learn | 1.1.2 |
| SciPy (Mean-Wilcoxon U-test, Spearman rank correlation test, bootstraping) | SciPy | 1.76.1 |
| WORC (DeLong test) | WORC | 3.7.0 |
| statmodels (GLM) | statmodels | 0.14.2 |

#### EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS

##### Human participants

All patients provided written informed consent at the time of enrollment. Our multi-center study was approved by the Harvard Medical School Institutional Review Board (IRB25-0188 for the SmartPath Research Network and IRB 20-1509). We obtained digital hematoxylin and eosin (H&E)-stained pathology slides from the National Cancer Institute-sponsored TCGA, CPTAC-3, and PLOO Cancer Screening Trials. In addition, we digitized 4,747 slides from the Mayo Clinic, MGB, UPenn, DFCI, and the Medical University of Vienna, Austria. Digital slides from the TCGA, CPTAC-3, and PLOO cohorts were scanned at 40X or 20X magnification. We scanned pathology slides from the Mayo Clinic at 40X with Aperio S7450 scanners, with pixel widths of 0.263 microns per pixel. We digitized slides from MGB and UPenn by Hamamatsu S210 scanners at 40X magnification, with pixel widths ranging from 0.221 to 0.253 microns per pixel. All WSIs used in this study were derived from pre-treatment tumor samples, and thus the potential differential access to treatments will not affect our analyses. We digitized slides from the Medical University of Vienna with a Hamamatsu NanoZoomer 2.0 HT slide scanner at 40X magnification with a pixel width of 0.228 microns per pixel. We scanned slides from DFCI using Aperio ScanScope scanners at 40X (0.248 microns per pixel) or 20X (0.496 microns per pixel). Participant age, gender, and race distributions for TCGA cohorts are summarized in Table S1 of the main text; demographics for external validation cohorts are summarized in the “Patient demographics for external cohorts” table. Analysis in this study explicitly evaluate performance across demographic attributes (age, gender, self-reported race) and include site-, scanner-, and magnification-stratified assessments reported in the Results and Table S3.

#### METHOD DETAILS

##### Whole-slide preprocessing and patch sampling

We preprocessed the whole-slide images (WSIs) by tiling each image into non-overlapping patches of 512 × 512 pixels at 20X magnification. To separate tissue regions from the background, we converted the WSIs to grayscale and excluded pixels with intensity values greater than 225 via foreground filtering. We removed patches with an insufficient size (<0.12 × 512 pixels) or low tissue content in foreground ratio <0.1. This filtering strategy effectively eliminates regions with minimal biological signal without selectively eroding any specific microenvironment. We then divided the list of image patches into equal-length segments and evenly sampled 200 patches per patient from these segments. This strategy ensures a balanced representation, preventing the model

<!-- PAGE 19 -->

OPEN ACCESS

# Cell Reports Medicine

Article

## from overexpressing high-tumor regions while retaining potential morphological patterns relevant to demographic factors.

### Fairness-aware contrastive pretraining

FaRP-Path employs a multi-instance learning (MIL) architecture with ResNet
^44^
 as the tile-level feature extractor, which aligns with standard pathology AI frameworks such as CLAM
^45^
 and MOIA
^46^
 that employed ResNet as the backbone for image feature extraction. We trained ResNet-18 to balance computational efficiency and performance during the contrastive learning phase of our fairness-enhancement framework. Following tile-level encoding, a MIL module aggregates features across all tiles, which are then processed by a two-layer multilayer perceptron (MLP) projector.

During the pretraining process, we trained the side-side encoder, along with a two-layer multilayer perceptron (MLP) projector, using supervised contrastive loss and non-discrimination loss. The pretraining was performed in an end-to-end manner, where all parameters were trained during the process. After training the FaRP-Path side-side encoder, we froze its parameters and trained a three-layer MLP for cancer diagnostic tasks using a graph-balanced reweighting approach.
^47^

For randomly sampled data triplets, 
(D_i, y_i, s_i)
, 
x_i
 in a batch, where 
y_i, y_j
, and 
s_i
 denotes the bag of the input samples, target label, and demographic attribute labels, respectively, with an equal number of samples drawn from each demographic group and random sampling performed within each group. After augmentation, we obtained 2N data triplets in a batch, 
(D_i, y_i, s_i)
, 
x_i
. The feature extractor encodes patches into tile-level features, which are grouped into bags corresponding to the original slides and input into the attention-based MLP module. The MLP module computes attention weights, which are multiplied by their respective embeddings and then summed to form the bag representations, 
z_i
, 
i=1, \dots, 2N
. We then projected these representations into another feature space, where we compute the fairness-aware supervised contrastive loss using supervised contrastive loss and non-discrimination loss.

The non-discrimination loss (
L_{CNDL}
) extends supervised contrastive learning
^48^
 by addressing the fairness constraint. Mathematically,

L_{CNDL} = \sum_{i=1}^{2N} \log \left[ \frac{\exp\left(\frac{z_i z_i^T}{\tau}\right)}{\sum_{j \neq i} \exp\left(\frac{z_i z_j^T}{\tau}\right)} \right]

where the set of representations that share the same demographic category but have different demographic attributes from 
z_i
 is denoted as 
Z_{D_i} = \{z_j \in Z_{D_i} : y_j = y_i \land s_j \neq s_i\}
. Similarly, the set of representations with both different demographic categories and demographic attributes from 
z_i
 is denoted as 
Z_{D_i} = \{z_j \in Z_{D_i} : y_j \neq y_i \land s_j \neq s_i\}
.

We incorporated the non-discrimination loss 
L_{CNDL}
 into the training process to mitigate the model's tendency to encode imaging features associated with demographic attributes rather than diagnostic categories, which could lead to performance differences across population groups. By pushing apart representations of the same demographic attribute but different diagnostic labels, our model learns to focus on diagnosis-related features instead of demographic characteristics. This enhances the model's fairness by reducing the risk of bias related to these demographic attributes. As a result, the model becomes less likely to unfairly favor or penalize certain population groups, thereby achieving more equitable outcomes across different demographic groups.

Our model training process is guided by a loss function, denoted as 
L_{CNDL}
, which combines both the supervised contrastive loss and the non-discrimination loss. i.e.,

L_{CNDL} = L_{sup} + L_{CNDL}

We trained our contrastive learning models with SGD using a learning rate of 
5 \times 10^{-3}
, a batch size of 8, and 100 epochs with a cosine annealing learning rate scheduler.

### Classifier training

We conducted pretraining in an end-to-end manner, with all model parameters optimized during the process. In the second stage, we froze the parameters of the pretrained encoder and trained a three-layer MLP for cancer diagnosis using a simple group-balanced reweighting approach.
^49^
 We trained the classifier with an SGD using a learning rate of 
10^{-3}
, a batch size of 8, and 50 epochs with a cosine annealing learning rate scheduler. In our experiments, the hyperparameters were set as above across all tasks, and no hyperparameter tuning was required.

### Sample size and allocation to analyzing groups

We included all pathology diagnostic tasks with sufficient sample sizes (>8 patients) in each diagnostic category and demographic subgroups for performance and fairness evaluation. This resulted in 27 classification scenarios, including 17 tumor detection tasks, 6 cancer type diagnostic tasks, and 4 cancer subtype diagnostic tasks across 20 cancer types. We repeated the process independently for FFPE and frozen section samples. For each task, we employed a 4-fold cross-validation (CV) to train the model, with a training-validation-test split ratio of 2:1:1 for each fold. There was no patient overlap among training, validation, and testing sets. We selected the number of epochs with the highest AUROC in the validation set. After finalizing the model, test set metrics for each fold were aggregated to provide the final evaluation results for our developmental cohorts.

<!-- PAGE 20 -->

# Cell Reports Medicine

Article

Cell Press
OPEN ACCESS

To evaluate the generalizability of our framework, we performed external validation on patient cohorts from CPTAC-3, PLCO, DFCI, Mayo Clinic, UPenn, MQB, and the Medical University of Vienna. For the external validation experiments, we only included tasks with baseline results from the TCGA cohort and sufficient sample sizes for each cancer type in each demographic subgroup (N > 8). We listed all tasks included in our validation study in Table S2.

### Baseline training details

In the baseline model, we adopted ResNet-18 as the feature extractor and replaced the last fully connected layer with a linear layer and a rectified linear unit (ReLU).
^10^
 We employed gated attention-based multiple instance learning to aggregate patches from the same slides.
^11^
 For more efficient training, we used a ResNet-18 backbone pretrained on ImageNet and subsequently fine-tuned it using pathology images during model training. We trained the baseline models using stochastic gradient descent (SGD) with a learning rate of 5 × 10
^-5^
 and a batch size of 8. Because the supervised contrastive learning framework mitigated bias for one demographic attribute at a time, we trained separate Fair-Path models for each demographic characteristic.

### External validation of FAIR-Path

To evaluate the generalizability of our framework, we performed external validation on patient cohorts from CPTAC-3, PLCO, DFCI, Mayo Clinic, UPenn, MQB, and the Medical University of Vienna. For the external validation experiments, we only included tasks with baseline results from the TCGA cohort and sufficient sample sizes for each cancer type in each demographic subgroup (N > 8). We listed all tasks included in our validation study in Table S2.

Based on the slide presentation method (frozen section or FFPE), demographic attributes (race, age, or gender), and the type of diagnostic tasks (tumor detection, cancer type classification, or subtype classification), we selected the corresponding baseline and FAIR-Path models trained on the TCGA dataset. For each model, we fixed the embeddings extracted by the slide-level encoder and retrained only the subsequent classification layers. To account for domain differences, we re-estimated the normalization statistics (i.e., mean and variance) of all batch normalization layers in the model using data from the external cohorts. We implemented our methods using PyTorch 2.0.0.

### Patch selection

To assess the potential impact of patch selection on the demographic bias in standard AI models, we compared the resulting fairness from our patch selection method with that of two alternative patch selection strategies. The first strategy is a random selection approach, where 200 patches were randomly selected from each WSI during each iteration of the training process. The second patch selection strategy involves random sampling of 200 patches in a demographic-balanced manner, where the samples were drawn from each patient group with equal sampling probabilities. As a representative example, we compared the racial biases from these patch selection strategies on cancer type and subtype classification tasks using FFPE cohorts.

### Evaluation metrics of model fairness

We evaluated the fairness of our models' performance metrics, including recall, balanced accuracy, accuracy, and AUROC. We focus on the two standard fairness measures, including equal opportunity (EOp) and equal balanced accuracy (EBAcc), given their clinical significance. We also provide additional fairness measurements in Table S4, including equalized odds (EOEq), difference of accuracy (AccDiff), and difference of AUROC (AUcDiff).

For a class in a binary classification task, we defined its EOp (denoted as EOp
g
) as the difference between the highest and lowest recall values for class across subgroups defined by a demographic attribute (S):

EOp_g = \max_{s \in S} (\text{Recall}_g(s)) - \min_{s \in S} (\text{Recall}_g(s))

EBAcc quantifies the maximum between-group discrepancy in balanced accuracy (BA), where BA is the macro-average of recalls for all ground truth classes:

EBAcc = \max_{s \in S} (\text{BA}_g(s)) - \min_{s \in S} (\text{BA}_g(s))

where:

BA = \frac{1}{|C|} \sum_{c \in C} \text{Recall}_c

Equalized Odds quantifies the bias through the maximum absolute between-group disparity across true positive rate (TPR) and false positive rate (FPR), thereby promoting fairness across both positive and negative categories:

EOEq = \max_{s \in S} (|\text{TPR}_{\text{grouped}}(s) - \text{FPR}_{\text{grouped}}(s)|, |\text{TPR}_{\text{grouped}}(s) - \text{TPR}_{\text{grouped}}(s)|)

EBAcc = \max_{s \in S} (\text{BA}_g(s)) - \min_{s \in S} (\text{BA}_g(s))

BA = \frac{1}{|C|} \sum_{c \in C} \text{Recall}_c

<!-- PAGE 21 -->

OPEN ACCESS

## Cell Reports Medicine

Article

Similarly, we defined AccDiff and AUCDiff as the maximum between-group discrepancies in overall accuracy and AUC, respectively:

AccDiff = max(Acc_{1,1} - min(Acc_{1,2}))

and

AUCDiff = max(AUC_{1,1} - min(AUC_{1,2}))

The performance and fairness metrics listed above were estimated based on model predictions for each individual. To assess performance disparities measured by each fairness metric, we employed non-parametric, one-sided bootstrap hypothesis testing
^10^
 to evaluate the significance of the observed bias. For each task, we first aggregated the labels and predictive scores from the test set across all 4-tasks. Subsequently, for each demographic group, we resampled the label-score pairs with replacement from the combined testing dataset. We then averaged fairness metrics from these resamples for each demographic group and generated 10,000 bootstrap samples for each metric. For a given fairness metric, the P-value was defined as the percentage of bootstrap samples that exhibited greater bias than the observed fairness metric. A model was considered significantly biased for a given fairness metric if the P-value was less than 0.05.

### Subsampling analyses for imbalance and shifts

We quantified how sample size imbalance and shifts in class distribution between demographic groups affect performance disparities in a deep learning model for common pathology diagnostic tasks through a series of subsample analyses. We focused on 13 cancer diagnostic tasks from the NIH ChestX-ray14 dataset that contain four samples for each cancer type across all demographic groups. To ensure sufficient sample sizes across all demographic strata, we employed a stratified random split where the testing partition in each stratum was set to be at least half of the size of the smallest stratum defined by the targeted demographic attribute (e.g., age, gender, or self-reported race). The training dataset was then sampled from the remaining data in each stratum. There was no patient overlap between the training and testing sets.

That, we investigated the impact of sample size balance on model fairness. To achieve this goal, we varied the number of samples for the majority and minority groups while keeping the total dataset size at 200 samples. The balance between the minority and majority groups ranged from being completely balanced (100 majority and 100 minority) to only including data from the majority group (majority and 0 minority).

Next, we examined the impact of distribution shifts in diagnostic categories within each demographic group while maintaining overall sample size balance across groups (e.g., 100 majority and 100 minority patients). In the majority group, sample sizes for each cancer type were perfectly balanced (e.g., 50% for each cancer type), while we introduced various degrees of diagnostic category imbalance in the minority group (from 100:0 to 50:50).

In the sample size balance evaluation experiment, we excluded tasks in which the minority group's training sample size was less than 100. In the distribution shift experiment, we excluded tasks where the minority group sample size was fewer than 50 across both classes or fewer than 25 within a single class. We excluded the COAD vs. READ classification task from both experiments due to a consistently low AUC. For each experiment, we repeated the training and evaluation processes 20 times with different balance ratios, and we used two-sided Spearman correlation tests to examine the relationships between sample size imbalance, category imbalance, and performance disparities between majority and minority groups. The Spearman correlation test assumes ordinal or continuous data, monotonic relationships, paired observations, and independence of observations.

### Demographic separability

We evaluated the extent to which pathology image representation contained information related to demographic attributes by conducting supervised machine learning analyses. For cancer types where baseline AI models for cancer diagnosis showed significant demographic bias, we extracted slide-level WSIs features using the trained baseline AI models. We then built logistic regression models to classify patients' race, gender, or age using the extracted features and 4-told cross-validation. We reported the AUCROC of demographic attribute classification and employed the one-sided DeLong test to determine if the AUCROC is significantly greater than 0.5.

For cancer types showing significant distinction between demographic groups in their image features (Delong test P-value < 0.05), we further investigated their cellular attributes contributing to demographic separability. For each patient, we selected up to 500 of the most accurately predicted patches by the demographic attribute classification model. Subsequently, we applied CellTITV
^11^
 to segment and classify the cells into four primary cell types: neoplastic, inflammatory, epithelial, and connective or soft tissue cells. Neoplastic cells were excluded from the analysis, as it was our goal to select cells in 0.22% of the selected patches. We reported the density of each cell type and assessed the differences in cell-type distributions across demographic groups using the Mann-Whitney U test. These analyses collectively assess how demographic information is encoded in tissue morphology and identify cellular correlates underlying such signals.

e4 Cell Reports Medicine 6, 102527, December 16, 2025

<!-- PAGE 22 -->

# Cell Reports Medicine

## Article

Cell Press
OPEN ACCESS

### GLM analyses for tissue/genomic factors

We further examined the relationships between performance disparities and tissue or genomic characteristics in our pathology samples. For each WSI, we obtained the percentages of eight tissue types (tissues with lymphocyte infiltration, monocyte infiltration, necrosis, multinuclear infiltration, normal cells, tumor cells, and tumor nuclei) curated by the TCGA study consortium from GDC. In addition, we retrieved mutational profiles for the five genes with the highest mutation prevalence and those related to FDA-approved targeted therapies from cBioPortal. The genomic features were investigated in our model framework as described in Table S1. Our analysis included genomic mutations both related and unrelated to the cancer type in question, allowing us to investigate the influence of potential disease-independent factors. We investigated germline MET mutation in KIRP, which is characteristic of the familial KIRP variant.
^48^
 but found no significant performance disparity due to limited sample size (
N = 3
 in TCGA cohort; Mann-Whitney 
U
-test 
P
-value = 0.96).

We focused on cancer type or subtype classification tasks where the baseline models exhibited significant performance disparity. We excluded tissue percentage analyses for FFPE samples because fewer than 1% of them contain such information. Among the classification scenarios showing significant performance bias in the baseline model, we employed generalized linear models to quantify tasks that showed both tissue or genomic associations between tissue or genomic features and demographic attributes of interest and 2) significant associations between each tissue or genomic factor and the model's predictive errors. For this purpose, we employed generalized linear models (GLM), with the assumptions of independent observations, linearity in parameters, binomial distribution for demographic attributes and genomic mutations, Gaussian distributions for predictive error and tissue percentages, and no perfect multicollinearity. For variables modeled with a Gaussian distribution, we employed an identity link function, whereas for those modeled with a binomial distribution, a logit link function was used. We used two-sided 
P
-values from Wald tests to determine statistical significance.

### Fairness analysis accounting for technical factors

We conducted stratified bootstrap tests to evaluate whether patient path and technical heterogeneity contributes to demographic disparities in model performance. Factors examined included patient stage as well as technical factors such as tissue procurement sites, scanner types, and scanning magnification. For each factor, the dataset was stratified to preserve the internal structure of that variable. Within each stratum, 1000 random samples via bootstrapped resampling were used to generate a null distribution of fairness metrics under the assumption that the stratification factor remained fixed. The observed fairness metrics can then compared against their respective null distributions to determine whether the observed disparities could be explained by patient stage or technical variability alone.

### Ablation studies

We conducted three ablation analyses to demonstrate the efficacy of our model design.

1. FAIR-Path versus Supervised Contrastive Learning: While supervised contrastive learning has shown promise in improving generalization, its ability to mitigate demographic bias remains unquantified. To investigate this, we compared the racial fairness of FAIR-Path to an otherwise identical model trained without the non-discrimination objective, using only the supervised contrastive loss. We evaluated and compared these models across all cancer type and subtype classification tasks using FFPE cohorts.
2. Hospital-Clinic-Related Bias: To investigate whether the observed demographic bias can be mitigated by addressing the representation disparity between hospital sites, we trained a variant of FAIR-Path that aims to correct the hospital-related bias. For this purpose, the hospital sites are treated as demographic attributes during the fairness-aware contrastive learning and the downstream training process. Hospital sites with two or fewer samples were excluded from the analysis. We selected 12 tasks in which the baseline models exhibited demographic biases. After correction for hospital sites, we then evaluated the bias related to the demographic attributes (race, gender, and age) on these site-corrected classification models.
3. Impact of Training Sample Size: To investigate the robustness of our fairness-aware contrastive learning framework under varying amounts of training data, we conducted an experiment to assess how the amount of training data affects its fairness performance. Using the ULMFiT and BERT classification models in this study, we trained models with different proportions of the training data (20%, 40%, 60%, 80%, and 100%) in the contrastive learning stage. Subsequently, all samples were used to fine-tune the downstream classification task.

### QUANTIFICATION AND STATISTICAL ANALYSIS

All statistical analyses were performed in Python 3.8 (NGC PyTorch 2.0.2 base docker image uses Python 3.8) using NumPy 1.22.4 and scikit-learn 1.1.2. Mann-Whitney 
U
 tests and Spearman rank correlation tests were conducted with SciPy 1.16.1. Generalized linear model analyses were conducted using statsmodels 0.14.2. The bootstrapping tests were conducted using the resampling package from the WORC 3.7.0 package. Bootstrap significance tests were performed via our Python implementation provided in the repository (see 
[key resources table](#)
) with results computed on pooled per-patient predictions. Unless otherwise specified, it denotes the number of patients (per-patient predictions aggregated across slides) per statistical significance was assessed at 
\alpha = 0.05
.

Cell Reports Medicine 6, 102527, December 16, 2025 e5