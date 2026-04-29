

<!-- PAGE 1 -->

Frontiers | Frontiers in Cardiovascular Medicine

ORIGINAL RESEARCH

published: 07 April 2022

doi: 10.3389/fcm.2022.899310

# Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation

Esther Puyol-Antón
^1^
*, Bram Ruijsink
^1,2,3^
, Jorge Mariscal Harane
^1^
, Stefan K. Piechnik
^4^
, Stefan Neubauer
^4^
, Steffen E. Petersen
^5,6,7,8^
, Reza Razavi
^1,2^
, Phil Chowwicznyk
^9,10^
 and Andrew P. King
^1^

OPEN ACCESS

**Edited by:**
Chayakorn Kettrawong,
NYU Grossman School of Medicine,
United States

**Reviewed by:**
Eline Pinael Jan,
The Johns Hopkins Hospital, Johns
Hopkins Medicine, United States
Feng Yang,
National Institute of Health (NIH),
United States
Anna Barbuscia,
University of Padua, Italy
Yuli Miron,
University of Copenhagen, Denmark

***Correspondence:**
Esther Puyol-Antón
esther.puyol-anton@ki.se

**School of Biomedical Engineering and Imaging Sciences, King's College London, London, United Kingdom**

**Department of Adult and Paediatric Cardiology, Guy's and St Thomas' NHS Foundation Trust, London, United Kingdom**

**Division of Heart and Lung, Department of Cardiology, University Medical Centre Utrecht, Utrecht, Netherlands**

**Division of Cardiovascular Medicine, Ruskin Department of Medicine, University of Oxford, Oxford, United Kingdom**

**National Institute for Health Research (NIHR) Biobank Biomedical Research Centre, William Harvey Research Institute, Queen Mary University of London, London, United Kingdom**

**Biarts Heart Centre, St Bartholomew's Hospital, Barts Health NHS Trust, London, United Kingdom**

**Health Data Research UK, London, United Kingdom**

**“Alan Turing Institute, London, United Kingdom**

**“British Heart Foundation Centre, King's College London, London, United Kingdom**

**Specialty section:**
This article was submitted to
Cardiovascular Imaging,
a section of the journal
Frontiers in Cardiovascular Medicine

**Received:**
 21 January 2022
**Accepted:**
 02 March 2022
**Published:**
 07 April 2022

**Citation:**
Puyol-Antón E, Ruijsink B,
Mariscal Harane J, Piechnik SK,
Neubauer S, Petersen SE, Razavi R,
Chowwicznyk P and King AP (2022)
Fairness in Cardiac Magnetic
Resonance Imaging: Assessing Sex
and Racial Bias in Deep
Learning-Based Segmentation.
Front. Cardiovasc. Med. 9:899310.
doi: 10.3389/fcm.2022.899310

**Results:**
 Results on the overall population showed an excellent agreement between the manual and automatic segmentations. We found statistically significant differences in Dice scores between races (white ~94% vs. minority ethnic groups 86–89%) as well as in absolute/relative errors in volumetric and functional measures, showing that the AI model was biased against minority racial groups, even after correction for possible confounders. The results of a multivariate linear regression analysis showed that no covariate could explain the Dice score bias between racial groups. However, for the Mixed and Black race groups, sex showed a weak positive association with the Dice

**Frontiers in Cardiovascular Medicine**
 | www.frontiersin.org

1

April 2022 | Volume 9 | Article 899310

<!-- PAGE 2 -->

Proctor et al.

Farness in Deep Learning-Based CMR Segmentation

score. The results of an ANCOVA analysis showed that race was the main factor that can explain the overall difference in Dice scores between racial groups.

**Conclusion:**
 We have shown that racial bias can exist in DL-based cine CMR segmentation models when training with a database that is sex-balanced but not race-balanced such as the UK Biobank.

**Keywords:**
 cardiac magnetic resonance, deep learning, far AI, segmentation, inequality, fairness in deep learning-based CMR segmentation

## INTRODUCTION

Artificial intelligence (AI) is a rapidly evolving field in medicine, especially in cardiology. AI is the potential to aid cardiologists in making better decisions, improving workflows, productivity, cost-effectiveness, and ultimately patient outcomes (1). Deep learning (DL) is a recent advance in AI which allows computers to learn a task using data instead of being explicitly programmed. Several studies in cardiology and other applications have shown that DL methods can match or even exceed human experts in tasks such as identifying and classifying disease (2–4).

Cardiac magnetic resonance imaging is a pivotal role in diagnostic decision making. Cardiac magnetic resonance (CMR) is the established non-invasive gold-standard modality for quantification of cardiac volumes and ejection fraction (EF). For decades, clinicians have been relying on manual or semi-automated segmentation approaches to trace the cardiac chamber contours. However, manual expert segmentation of CMR images is tedious, time-consuming and prone to subjective errors. Recently, DL models have shown remarkable success in automating many image segmentation tasks. In cardiology, human-level performance in segmenting the main structures of the heart has been reported (5, 6), and researchers have proposed to use these models for tasks such as automating cardiac functional quantification (7). These methods are now starting to move toward broader clinical translation.

In the vast majority of cardiovascular diseases (CVDs), there are known associations between sex and epidemiology, pathophysiology, clinical manifestations, effects of therapy, and outcomes (8–10). Furthermore, in clinically asymptomatic individuals the Multi-Ethnic Study of Atherosclerosis (MESA) study showed that men had greater right ventricular (RV) mass and larger RV volumes than women, but had lower RV ejection fraction. African-Americans had lower RV mass than whites, whereas Hispanics had higher RV mass (11), and the LV was more trabeculated in African-American and Hispanic participants than white participants, and smoother in Chinese-American participants (12), but the greater extent of LV trabeculation was not associated with a absolute decline in LVEF during the approximately 10 years of the MESA study. Similarly, the Coronary Artery Risk Development in Young Adults (CARDIA) study (13) showed differences between race (African American and white) and sexes in LV systolic and diastolic function, which persist after adjustment for established cardiovascular risk factors.

Although these physiological differences are associations and not proven causative links with race/gender, their presence raises a potential concern about the performance of AI models in cardiovascular imaging. Although AI has great potential in this area, no previous work has investigated the fairness of such models. In AI, the concept of “fairness” refers to assessing AI algorithms for potential bias based on demographic characteristics such as race and sex. In general, AI models are trained against demographic characteristics, and they assume that if the model is unaware of these characteristics while making decisions, the decisions will be fair. However, we have recently shown, for the first time, that using the UK Biobank, which exists racial bias in DL-based cine CMR segmentation models when training using racially imbalanced data (14). The previous study aimed to identify the presence of bias and the technical development of different bias mitigation strategies, in order to reduce the bias effect between different racial groups. The object of this study is to investigate in more detail the origin and the effect of this bias on cardiac structure and function and to assess whether the bias could be changed by any confounder and therefore be linked with changes in subject characteristics, anatomy or cardiovascular risk factors.

## MATERIALS AND METHODS

### Participants

The UK Biobank is a prospective cohort study with more than 500,000 participants aged 40–69 years of age conducted in the United Kingdom (15). This study complies with the Declaration of Helsinki; the work was covered by the ethical approval for UK Biobank studies under the NHS National Research Ethics Service on 17th June 2011 (Ref 11/NW/082) and extended on 18th June 2021 (Ref 21/NW/0157) with written informed consent obtained from all participants. The present study was performed using a sub-cohort of the UK Biobank imaging database, for whom CMR imaging and ground truth manual segmentations were available. In this study, in order to minimize the effects of physiological differences due to cardiovascular and other related diseases, we only focus on the healthy population of the UK Biobank database and analyze the confounders that can explain racial and sex bias.

Therefore, we included any subjects with known cardiovascular disease, respiratory disease, hematological disease, renal disease, rheumatic disease, malignancies, symptoms of chest pain, respiratory symptoms or other diseases

Citation: Proctor et al. (2022) Farness in Deep Learning-Based CMR Segmentation. Front. Cardiovasc. Med. 9:106310. doi: 10.3389/fcvm.2022.106310

<!-- PAGE 3 -->

Page 4/20

Printers in Cardiovascular Medicine | www.printers.org

Farness in Deep Learning-Based CMR Segmentation

impacting the cardiovascular system, except for diabetes mellitus, hypercholesterolemia and hypertension (see all exclusion criteria in Supplementary 1a). We included these cardiovascular risk factors to evaluate if or how they affect cardiovascular risk in otherwise healthy patients could explain a potential bias in segmentation performance between the LV and RV and ICDU codes and self-reported detailed health questionnaires and medication history for the selection process.

For each patient, race was recorded in a single with self-reported ethnicity, which was the data collected in the UK Biobank. From the total UK Biobank database (N = 501,643), the race variable was as follows: White 94%, Black 2%, Asian 1%, Other 1%, Black 1.6%, Chinese 0.9%, Other 0.4%. The UK Biobank cohort has a similar ethnic distribution to the national population of the UK in the range of 85% to 90% (10, 11). The UK Biobank cohort used in this study (N = 5,660) has a slightly different racial distribution (White 81%, Mixed 5%, Asian 7%, Black 4%, Chinese 2%, Other 3%), but it is predominantly white race, in line with the full cohort of the UK Biobank database. Imaging centers of the UK Biobank are in Newcastle upon Tyne, London, Reading and Bristol. The imaging protocol was used in all imaging centers and no racial distribution difference was found between them. Moreover, the image acquisition protocol can be found in Petersen et al. (17).

Subject characteristics obtained were age, binary sex category, sex hormone levels (height, weight, body mass index, BMI, and body surface area, BSA), and smoker status (smoker was defined as a subject smoking or smoked daily for over 25 years in the previous 35 years). We also obtained the average heart rate (HR) and brachial systolic and diastolic blood pressure (SBP and DBP) measured during the CMR exam. These subject characteristics were considered as possible confounding factors in the analysis as they are directly or indirectly related to the measurements made and therefore plausibly associated with the accuracy of the measurements.

### Automated Image Analysis

We used the in-house DL based segmentation model, the “mnuNet” framework (18), was used for automatic segmentation of the left ventricle blood pool (LV), left ventricular myocardium (LVmyo) and right ventricle blood pool (RVBP) from cine short-axis CMR slices at end-diastole (ED) and end-systole (ES). This model was chosen as it has been validated well across a range of segmentation challenges and was the top-performing model in the “ACDC” CMR segmentation challenge (6). For training and testing, a segmentation model was used a random split of 4:4:0.12 and 1,250 samples, respectively, each with similar sex and racial distributions. We refer the reader to our previous paper (14) for details of the model architecture and training.

### Evaluation of the Methods

For quantitative assessment of the image segmentation model, we used the Dice similarity coefficient (DSC), which quantifies the overlap between an automated segmentation and a ground truth segmentation. DSC has values between 0 and 100%, where 0 denotes no overlap, and 100% denotes perfect agreement. From the manual and automated image segmentations, we calculated the LV end-diastolic volume (LVEDV) and end-systolic volume (LVESV), and RV end-diastolic volume (RVEDV) and end-systolic volume (RVESV) by summing the number of voxels belonging to the corresponding label classes of the segmentation and multiplying this by the volume per voxel. The LV myocardial mass (LVMM) was calculated by multiplying the LV myocardial volume by a density of 1.05 g/mL. Derived from the LV and RV volumes, we also computed the ejection fraction (EF) and RV ejection fraction (RVEF). We evaluated the accuracy of these volumetric and functional measures by computing the absolute and relative differences between automated and manual measurements to define the absolute and relative error as 
\epsilon_{absolute} = |V_{manual} - V_{auto}|
 and 
\epsilon_{relative}(\%) = 100 \cdot |V_{manual} - V_{auto}| / V_{manual}
, where 
V_{manual}
 and 
V_{auto}
 are the manual and automated volumes, respectively.

### Analysis of the Influence of Confounders

To investigate whether a true difference in racial and/or sex groups exists for automated DL-based cine CMR segmentation, we conducted a statistical analysis to investigate if the observed bias could be explained by the most common confounders. In this study, we use as possible confounders the following body measurements: age, sex, height, weight, SBP, DBP, CMR-derived parameters (LVEDV, LVESV, RVEDV, RVESV, LVMM), cardiovascular risk factors (i.e., hypertension, hypercholesterolemia, diabetes and smoking) and center (i.e., core lab where most of the segmentations were performed vs. additional lab).

### Statistical Analysis

Data analysis was performed using SPSS Statistics (version 26, IBM, United States). Continuous variables are reported as mean 
\pm
 standard deviation (SD) and tested for normal distributions with the Shapiro-Wilk test. Log transformations were applied to the LVEDV and LVMM to obtain an approximate normal distribution. After transformation, all continuous variables were normally distributed. Categorical variables are presented as absolute counts and percentages. Comparison of variables between groups (i.e., races and sexes) was carried out using an independent Student’s t-test.

Independent association between log-transformed DSC values and race was performed using univariate linear regression followed by multivariable linear regression for all variables in the regression models were standardized by computing the z-score for individual data points.

Finally, the differences in DSC values among different racial groups were initially assessed by a 1-way ANOVA (Model 4) followed by an analysis of covariance—ANCOVA (Model 5) to statistically control the effect of covariates. In addition, we checked the assumption concerning regression residuals (19) as follows: (1) Homoscedasticity tested by a Levene’s Test of quality of error (2) Normality of residuals was tested by the Kolmogorov-Smirnov and Shapiro-Wilk test. (3) Multicollinearity tested by the Durbin-Watson test. (4) All statistical tests were set at a threshold for statistical significance was 
p < 0.01
 and confidence intervals (95%) were calculated by non-parametric bootstrapping with 1,000 resamples.

<!-- PAGE 4 -->

**RESULTS**

## Deep Learning-Based Image Segmentation Pipeline

**Table 2**
 reports the DSC values between manual and automated segmentations evaluated on the test set of 1,250 subjects which the segmentation model had never seen before. The table shows the mean DSC for LVBB, LVMyo and RVBP for both the full test set and stratified by sex and race. Overall, the average (AVG) DSC was 93.03 ± 3.83% (94.04 ± 2.61% for the LVBP, 88.78 ± 3.08% for the LVMyo and 90.77 ± 3.96% for the RVBP). 
**Table 2**
 shows that the CMR segmentation model had a racial bias for all comparisons but no sex bias (independent Student’s 
*t*
-test between each racial group and rest of the population; 
*p*
 < 0.001 for LVBP, LVMyo, RVBP and AVG for all races). 
**Supplementary Figure 2**
 shows in the first row visual examples of frames from a cine CMR sequence and their associated ground truth segmentations, on the two last rows some sample segmentation results (on different frames) for different racial groups with both high and low DSC.

Next, we evaluate the accuracy of the volumetric and functional measures (LVEDV, LVESV, LVEF, LVMA, RVESV, RVEDV, RVEF). 
**Table 3A**
 reports the mean values based on the manual segmentations and 
**Tables 3B,C**
 report the mean absolute differences and relative differences between automated and manual measurements, respectively. The Bland-Altman plots for agreement between the pipeline and manual analysis are shown in 
**Supplementary Figure 3**
. For the overall population, all results are in line with previous reported values (5, 22) and within the inter-observability range (20).

These results show that for sex there is a statistically significant difference in the absolute error for LVEF, LVMA and RVF.

**Table 2**
 differs from 
**Table 1**
 of our previous work (14), as in the present study we have excluded any case with cardiovascular disease.

**PAIRWISE POST HOC TESTING**

Pairwise post hoc testing was carried out using Bonferroni correction and Scheffé correction for multiple comparisons on the 
*t*
-test and ANOVA analysis, respectively.

## MATERIALS

### Subject Characteristics

The dataset used consisted of ED and ES short-axis cine CMR images of 5,660 healthy subjects (with or without cardiovascular risk factors). Subject characteristics for all participants were obtained from the UK Biobank database and are provided in 
**Table 1**
.

For all subjects, the LV endocardial and epicardial borders and the RV endocardial border were manually traced at ED and ES frames using the cv42 software (version 5.11, Circle Cardiovascular Imaging Inc., Calgary, Alberta, Canada). 4,975 subjects were previously analyzed by two core laboratories based in London and Oxford (20), the remaining 685 subjects were analyzed by two experienced CMR cardiologists at Guy’s and St. Thomas’ Hospital following the same standard operating procedures described in Petersen et al. (20). For all CMR examinations that underwent manual image analysis, any case with insufficient quality (i.e., presence of artifacts or slice location problems, operator error or evidence of pathology, such as significant shunt or valve regurgitation) were rejected (21). All experts performing the segmentations were blinded to subject characteristics such as race and sex. From our database, 4,410 images were used to train and validate the DL-based CMR segmentation model, and 1,250 subjects were used as a test set for the validation of the model and the statistical analysis (split 70/10/20 for training/validation/test set). The train and test sets were stratified to contain approximately the same percentage of samples for each racial group and sex. 
**Supplementary Figure 1**
 shows the flow chart for selection of cases for this study.

**TABLE 1**
 | Population characteristics for the train/validation and test sets.

|  |  | Train/validation | Test |
| --- | --- | --- | --- |
| Continuous variables | Patients, n | 4,410 | 1,250 |
| Age (years; mean, SD) | 62 (8) | 61 (8) |
| Height (cm; mean, SD) | 169 (8) | 169 (8) |
| Weight (kg; mean, SD) | 76 (15) | 75 (14) |
| BMI (kg/m^2^; mean, SD) | 27 (6) | 26 (6) |
| BSA (m^2^; mean, SD) | 1.80 (0.23) | 1.80 (0.23) |
| Systolic blood pressure (mmHg; mean, SD) |  | 136 (26) | 136 (18) |
|  | 79 (11) | 80 (10) |
|  | 65 (8) | 65 (10) |
| Categorical variables | Sex (males, n, %) | 2,299 (52) | 665 (52) |
| Race group |  |  |
| White, n, % | 3,670 (83) | 1,025 (81) |
|  | Mixed (n, %) | 156 (3) | 34 (3) |
|  | Asian, n, % | 313 (7) | 87 (7) |
|  | Black, n, % | 190 (4) | 47 (4) |
|  | Chinese, n, % | 87 (2) | 22 (2) |
|  | Other, n, % | 144 (3) | 34 (3) |

All continuous values are reported as mean(SD), while categorical variables are reported as number (percentage), SD, standard deviation.

Frontiers in Cardiovascular Medicine | www.frontiersin.org

4

April 2022 | Volume 9 | Article 859310

<!-- PAGE 5 -->

TABLE 2 | Dice similarity coefficient (DSC) values for the overall test set and by sex and race.

| N = 1,250 | LVEF | LVMi | FVBP | RVPB | AVG |
| --- | --- | --- | --- | --- | --- |
| Total | 94.39 (2.61) | 88.68 (6.06) | 90.77 (7.89) | 90.77 (7.89) | 91.28 (5.18) |
| Male | 94.35 (2.55) | 88.10 (6.24) | 90.81 (7.93) | 90.81 (7.93) | 91.35 (5.12) |
| Female | 94.44 (2.67) | 89.29 (5.28) | 90.74 (8.34) | 90.74 (8.34) | 91.32 (5.29) |
| White | 95.13 (1.98)* | 89.63 (4.14)* | 92.24 (2.11)* | 92.24 (2.11)* | 92.39 (1.66)* |
| Black | 94.76 (3.96)* | 88.19 (6.06)* | 82.48 (10.33)* | 82.48 (10.33)* | 86.49 (8.19)* |
| Asian | 92.15 (4.48)* | 86.46 (4.18)* | 96.27 (2.65)* | 96.27 (2.65)* | 94.28 (3.43)* |
| Other | 91.41 (5.53)* | 85.76 (7.71)* | 80.66 (8.19)* | 80.66 (8.19)* | 86.02 (7.78)* |
| Chinese | 94.76 (3.96)* | 79.16 (7.41)* | 82.48 (10.33)* | 82.48 (10.33)* | 86.12 (8.37)* |
| Others | 90.46 (5.53)* | 82.64 (4.44)* | 84.74 (7.41)* | 84.74 (7.41)* | 85.56 (5.81)* |

DSC reported for the LV blood pool (LVEF), LV myocardium (LVMi), and RV blood pool (FVBP), and average DSC values across LVEF, LVMi and FVBP (AVG column). *Indicates a significant difference (DSC values) between the groups (p < 0.001). †Indicates a significant difference (DSC values) between the groups (p < 0.001). ‡Indicates a significant difference (DSC values) between the groups (p < 0.001). §Indicates a significant difference (DSC values) between the groups (p < 0.001). ¶Indicates a significant difference (DSC values) between the groups (p < 0.001). ||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). ||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups (p < 0.001). |||||||||||||||||||||||||||||||||||||||||||||||||||Indicates a significant difference (DSC values) between the groups

<!-- PAGE 6 -->

TABLE 3 | Manual clinical measurements (top table) and absolute (middle table) and relative (bottom table) differences in volumetric and functional measures between automated and manual segmentations, overall and by sex and race.

| (A) Manual | LIVEDV(mL/min) | LIVEDV(mL/min^2^) | LVEF (%) | LVmass(g/min) | RVEDV(mL/min) | RVEDV(mL/min^2^) | RVEF (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total | 79 (23) | 33 (13) | 60 (7) | 51 (14) | 86 (22) | 38 (13) | 57 (7) |
| Male | 82 (20)^a^ | 36 (12) | 59 (7)^a^ | 50 (12)^a^ | 95 (21)^a^ | 45 (13)^a^ | 54 (7)^a^ |
| Female | 72 (18)^a^ | 29 (8) | 61 (7) | 48 (9) | 77 (14)^a^ | 32 (11) | 58 (8)^a^ |
| White | 83 (20) | 35 (12) | 59 (8) | 51 (14)^a^ | 87 (20)^a^ | 39 (13)^a^ | 56 (8) |
| Mixed | 76 (20)^a^ | 37 (9)^a^ | 64 (8)^a^ | 47 (14) | 83 (20)^a^ | 35 (10)^a^ | 58 (8)^a^ |
| Asian | 76 (19)^a^ | 35 (10)^a^ | 65 (8)^a^ | 50 (12)^a^ | 79 (19)^a^ | 35 (11)^a^ | 56 (8)^a^ |
| Black | 87 (21)^a^ | 33 (11)^a^ | 63 (8) | 59 (13) | 94 (27)^a^ | 41 (14) | 56 (8) |
| Chinese | 66 (12)^a^ | 22 (7) | 66 (7)^a^ | 46 (11)^a^ | 75 (18) | 32 (8) | 58 (8) |
| Others | 78 (18) | 28 (8) | 64 (7) | 50 (13) | 90 (23) | 38 (13) | 56 (8) |

| (B) Absolute difference | LIVEDV(mL/min) | LIVEDV(mL/min^2^) | LVEF (%) | LVmass(g/min) | RVEDV(mL/min) | RVEDV(mL/min^2^) | RVEF (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total | 2.6 (1.7) | 2.1 (1.8) | 2.5 (2.4) | 3.8 (5.9) | 3.5 (2.6) | 3.0 (2.2) | 3.6 (3.5) |
| Male | 2.7 (1.7) | 2.1 (1.7) | 2.1 (1.9)^a^ | 4.1 (4.2) | 3.4 (2.6) | 3.0 (2.1) | 3.1 (2.7) |
| Female | 2.6 (1.7) | 2.1 (1.8) | 2.9 (2.8)^a^ | 3.5 (5.4) | 3.5 (2.6) | 4.6 (2.2) | 4.1 (3.3)^a^ |
| White | 2.3 (1.6) | 1.8 (1.2)^a^ | 2.1 (2.1)^a^ | 4.0 (3.2)^a^ | 3.3 (2.6)^a^ | 3.6 (2.3)^a^ | 3.0 (3.6) |
| Mixed | 3.9 (2.1)^a^ | 3.4 (1.7)^a^ | 4.1 (2.7) | 1.9 (1.7)^a^ | 4.6 (1.8)^a^ | 3.9 (1.8)^a^ | 4.9 (2.5)^a^ |
| Asian | 3.4 (1.9)^a^ | 2.8 (2.3)^a^ | 4.0 (2.8)^a^ | 2.0 (3.7)^a^ | 4.4 (2.4)^a^ | 3.4 (1.9) | 4.4 (3.3) |
| Black | 5.6 (1.9)^a^ | 2.9 (2.8)^a^ | 3.3 (1.6)^a^ | 2.0 (2.8)^a^ | 4.4 (1.6)^a^ | 3.5 (1.5)^a^ | 3.0 (3.6) |
| Chinese | 4.4 (2.2)^a^ | 3.4 (2.1)^a^ | 4.7 (2.8)^a^ | 4.1 (5.6)^a^ | 4.8 (2.4) | 4.0 (2.9)^a^ | 6.4 (4.7)^a^ |
| Others | 3.1 (1.8) | 3.1 (2.0)^a^ | 4.3 (3.3)^a^ | 2.3 (3.5)^a^ | 4.6 (3.6) | 3.4 (1.9)^a^ | 4.3 (3.8)^a^ |

| (C) Relative difference | LIVEDV(mL/min) | LIVEDV(mL/min^2^) | LVEF (%) | LVmass(g/min) | RVEDV(mL/min) | RVEDV(mL/min^2^) | RVEF (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total | 3.4 (2.6) | 7.1 (7.4) | 4.1 (5.8) | 4.3 (5.4) | 4.3 (5.7) | 8.4 (7.5) | 6.4 (5.2) |
| Male | 3.0 (2.0)^a^ | 6.2 (6.7)^a^ | 3.6 (3.1)^a^ | 7.8 (8.5)^a^ | 3.3 (3.0)^a^ | 7.3 (5.9)^a^ | 5.8 (5.0)^a^ |
| Female | 3.7 (2.7)^a^ | 7.0 (8.2)^a^ | 4.6 (4.4)^a^ | 9.6 (6.6)^a^ | 4.9 (3.7)^a^ | 10.2 (8.4)^a^ | 7.0 (5.4)^a^ |
| White | 3.0 (2.1)^a^ | 6.0 (6.1)^a^ | 3.7 (3.6)^a^ | 8.4 (8.7)^a^ | 4.0 (3.4)^a^ | 8.2 (7.3)^a^ | 6.0 (5.1)^a^ |
| Mixed | 6.2 (3.8)^a^ | 14.1 (8.2)^a^ | 6.8 (4.4)^a^ | 10.3 (6.4)^a^ | 6.2 (4.4)^a^ | 13.3 (8.4)^a^ | 9.2 (4.7)^a^ |
| Asian | 5.1 (2.2)^a^ | 11.8 (11.6)^a^ | 5.8 (4.2)^a^ | 10.5 (4.4)^a^ | 6.1 (4.0)^a^ | 11.5 (6.8)^a^ | 7.2 (4.9)^a^ |
| Black | 4.1 (3.8)^a^ | 7.7 (8.8)^a^ | 7.3 (6.1)^a^ | 7.6 (5.1)^a^ | 5.3 (3.2)^a^ | 7.5 (5.2)^a^ | 7.0 (4.4)^a^ |
| Chinese | 7.0 (4.3)^a^ | 16.5 (10.6)^a^ | 6.9 (3.7)^a^ | 13.6 (7.1)^a^ | 6.2 (3.3)^a^ | 13.4 (11.4)^a^ | 10.4 (9.4)^a^ |
| Others | 5.0 (2.9)^a^ | 12.6 (12.1)^a^ | 7.7 (6.5)^a^ | 8.9 (4.2)^a^ | 5.2 (3.9) | 11.9 (7.0)^a^ | 8.1 (4.9) |

Clinical measurements for the LV (LVEDV and absolute volume, LVEF) and systolic volume (ESV, suction fraction, EF) and left ventricular mass (LVmass, LV cardiac volumes) were indexed to body surface area using the Dubois and Dubois formula (23). We define the absolute and relative errors as follows: 
	ext{Absolute error} = 	ext{Manual} - 	ext{Automated}
 and 
	ext{Relative error} = 	ext{Absolute error}/	ext{Manual}
. 
	ext{Absolute error}
 (in mL/min) = 100% 
	ext{Absolute error}
 (in mL/min) / 
	ext{Manual}
 (in mL/min). 
	ext{Relative error}
 (in %) = 100% 
	ext{Relative error}
 (in %) / 
	ext{Manual}
 (in %). 
	ext{Absolute error}
 (in mL/min
^2^
) = 100% 
	ext{Absolute error}
 (in mL/min
^2^
) / 
	ext{Manual}
 (in mL/min
^2^
). 
	ext{Relative error}
 (in %) = 100% 
	ext{Relative error}
 (in %) / 
	ext{Manual}
 (in %). 
	ext{Absolute error}
 (in %) = 100% 
	ext{Absolute error}
 (in %) / 
	ext{Manual}
 (in %). 
	ext{Relative error}
 (in %) = 100% 
	ext{Relative error}
 (in %) / 
	ext{Manual}
 (in %). 
	ext{Absolute error}
 (in g/min) = 100% 
	ext{Absolute error}
 (in g/min) / 
	ext{Manual}
 (in g/min). 
	ext{Relative error}
 (in %) = 100% 
	ext{Relative error}
 (in %) / 
	ext{Manual}
 (in %). 
	ext{Absolute error}
 (in mL/min
^2^
) = 100% 
	ext{Absolute error}
 (in mL/min
^2^
) / 
	ext{Manual}
 (in mL/min
^2^
). 
	ext{Relative error}
 (in %) = 100% 
	ext{Relative error}
 (in %) / <

<!-- PAGE 7 -->

Puglisi-Atkins et al. Fairness in Deep Learning-Based CMR Segmentation
**TABLE 4**
 Associations between average DSC and racial group.
**(A) Univariate linear regression**
Standardized Beta-coefficients (95% CI)

| N | Model 1 | p-value |
| --- | --- | --- |
| Mean | 0.34 (0.30, 0.38)* | 6.35e-16 |
| Black | 0.33 (0.29, 0.37)* | 1.30E-16 |
| Asian | 0.36 (0.32, 0.40)* | 1.35E-19 |
| Chinese | 0.32 (0.28, 0.36)* | 1.06E-8 |
| Other | 0.30 (0.26, 0.34)* | 4.43E-14 |

**(B) Multivariate linear regression**
Standardized Beta-coefficients (95% CI)

| N | Model 2 | p-value |
| --- | --- | --- |
| Mean | 0.32 (0.28, 0.36) | 0.210 |
| Black | 0.31 (0.27, 0.35) | 0.364 |
| Asian | 0.35 (0.31, 0.39) | 0.099 |
| Chinese | 0.31 (0.27, 0.35) | 0.379 |
| Other | 0.30 (0.26, 0.34) | 0.114 |
| Sex | 0.01 (0.00, 0.02) | 0.000 |
| Age | 0.01 (0.00, 0.02) | 0.000 |
| BMI | 0.02 (-0.06, 0.36) | 0.944 |
| Hb | 0.03 (0.01, 0.05) | 0.114 |
| SBP | 0.01 (0.00, 0.02) | 0.000 |
| DBP | 0.04 (-0.06, 0.01) | 0.114 |
| LDL | -0.03 (-0.21, 0.17) | 0.885 |
| LVEF | -0.07 (-0.09, 0.06) | 0.284 |
| RVEF | 0.12 (0.06, 0.31) | 0.235 |
| RVEF | -0.11 (0.24, 0.04) | 0.127 |
| Lumens | -0.04 (-0.11, 0.02) | 0.174 |
| Diabetes | 0.10 (0.07, 0.27) | 0.273 |
| Hypertension | 0.02 (0.00, 0.19) | 0.080 |
| Hyper | 0.00 (-0.04, 0.05) | 0.860 |
| Cholesterol |  |  |
| Smoking |  |  |
| Center | 0.15 (0.09, 0.21) | 9.99E-02 |
| Mean | 0.38 (0.36, 0.41)* | 8.99E-04 |
| Asian | 0.37 (0.34, 0.41)* | 8.99E-04 |
| Black | 0.40 (0.38, 0.43)* | 8.99E-04 |
| Other | 0.36 (0.34, 0.38)* | 8.99E-04 |
| Other | 0.34 (0.30, 0.38)* | 8.99E-04 |

Standardized regression beta-coefficients and CI are shown, representing the average change in variables with increasing DSC. The White racial group was selected as control. LV left ventricle, EDV end-diastolic volume, ESV end-diastolic volume, SBP systolic blood pressure, DBP diastolic blood pressure, CI confidence interval. Model 1 is unadjusted. Model 2 is adjusted for sex, height, weight, blood pressure at scan-time, heart rate at scan-time, LVEF, RVEF, LDL, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF, RVEF,

<!-- PAGE 8 -->

TABLE 1 | Misclassification rate for Hf diagnosis.

|  | HfEF | HfNEF | HfPEF |
| --- | --- | --- | --- |
| LVEF < 40% | LVEF 40-49% | LVEF 40-49% | LVEF 40-49% | LVEF > 50% | LVEF > 50% |
| n | 107 | 465 | 97 | 440 | 8 | 23 |
| White | 107 | 0 | 97 | 0 | 8 | 0 |
| Mixed | 11 | 0 | 46 | 0 | 0 | 0 |
| Black | 0 | 0 | 0 | 0 | 0 | 0 |
| Asian | 14 | 0 | 2 | 0 | 0 | 0 |
| Chinese | 0 | 0 | 0 | 0 | 0 | 0 |
| Other | 0 | 0 | 0 | 0 | 0 | 0 |
| Minority groups | 43 | 8 | 23 | 20 | 9 | 23 |

The table summarizes numbers of subjects in each racial group and Hf diagnosis (i.e., HfEF, HfNEF and HfPEF), as well as the misclassification rate (MCR%) for each racial group and Hf diagnosis. The row 'Minority groups' combines data from the Mixed, Black, Asian, Chinese and Other groups. The left column is overall above the number of subjects for each racial group used to compute the MCRs. For each Hf diagnosis, the first column shows the number of ground truth positive subjects in that group, the second column shows the number of subjects crossing the MCRs, the ground truth negative subjects are in the third column, and the fourth column is the misclassification rate. HfEF, HF with mildly reduced EF; HfNEF, HF with preserved EF; Blank cells show regions with missing data.

The potential shortcomings of AI at this stage before AI models become more widely deployed in clinical practice.

For these reasons, we believe that it is necessary that new standards are established to ensure equality between demographic groups in AI model performance, and that there is consistent and rigorous reporting of performance for new AI models that are intended to be integrated into clinical practice. Similar to Noseworthy et al. (30), we would recommend that any new AI-based publication include a report of performance across a range of demographic subgroups, particularly race/sex.

## Strategies to Reduce Racial Bias

The obvious way to mitigate bias due to imbalanced datasets (whether in current clinical guidelines or AI models) is to use more balanced datasets. However, this is a multibarrier problem and is associated with many challenges, such as historical discrimination, research design and accessibility (22). We note that AI has the potential to mitigate bias without requiring such balanced datasets. A range of bias mitigation strategies have been proposed that either pre-process the dataset (e.g., it is less imbalanced, after the training procedure or post-process the model outputs to reduce bias (31). We have recently proposed three algorithms to mitigate bias in CMB image segmentation: (1) train a CMB segmentation algorithm that ensures racial balance during training (12) and an AI race classifier that has the segmentation and feature racial variations; and (3) train a different CMB segmentation model for each racial group. For more detail of these models, we refer to the reader to our previous work (4). All three proposed algorithms result in a fairer segmentation model that aims to ensure that no racial group will be disadvantaged when segmentations of their CMB data are used to inform clinical management. Note that, compared to our previous work (4), in this paper we have excluded all subjects with cardiovascular disease to ensure that racial bias was not influenced by this factor.

## Limitations

This study utilizes the imaging cohort from the UK Biobank. UK Biobank is a long-term prospective epidemiology study of over 500,000 persons aged 40–69 years across England, Scotland, and Wales. Therefore, the data are geographically limited to the UK population, which might not reflect geographic, socioeconomic or healthcare differences among other populations. This work uses the UK Biobank participants' self-reported ethnicity, which corresponds to them self-identifying as belonging to ethnic groups based on shared culture and heritage. A possible limitation is that ethnic groups are socially constructed and thus may not serve as reliable proxies for analysis. Future work should aim to perform a similar analysis using genetic ancestry data, which will make the analysis more generalizable. In addition, Mixed Race was considered to be a single category, whereas in reality this encompasses many different subcategories.

Manual analysis of CMB scans was performed by three independent centers using the same operating procedures for analysis. For the three centers, inter- and intra-observer variability between analysts was assessed by analysis of fifty, randomly selected CMB examinations (20). However, one limitation of this study is the center- and observer variability was not assessed individually by race and sex. Also, this study is limited by the lack of diversity and relatively small sample sizes for certain racial groups by the exclusion criteria for comorbid and pre-morbid conditions. The study only includes the most common cardiovascular risk factors as confounders: hypertension, hypercholesterolemia, diabetes and smoking. However, there are other clinically relevant risk factors such as sedentary lifestyle, alcohol consumption or stress that could potentially explain the bias found in our study. For instance, a previous study showed an association between RV size and living in a high traffic location (32). Another limitation is that current analysis does not adjust for any measures of ventricular function, which could explain the structural differences. Future work will aim to extract echocardiographic measures of relaxation and whether the current bias could be explained by changes in subclinical diastolic dysfunction.

## CONCLUSION

We have demonstrated that a DL-based CMB segmentation model derived from an imbalanced database has poor

<!-- PAGE 9 -->

generalizability across racial groups and has the potential to lead to inequalities in early diagnosis, treatments and outcomes. Therefore, for best practice, we recommend reporting of performance among diverse groups such as those based on sex and race for all new AI tools to ensure responsible use of AI technology in cardiology.

## DATA AVAILABILITY STATEMENT

The data analyzed in this study is subject to the following license restrictions: The UK Biobank datasets are publicly available for approved research projects. Requests to access these datasets should be directed to 
[https://www.ukbiobank.ac.uk/](https://www.ukbiobank.ac.uk/)
.

## ETHICS STATEMENT

The studies involving human participants were reviewed and approved by the NHS National Research Ethics Service on 17th June 2011 (Ref 11/NO/0882). The patients/participants provided their written informed consent to participate in this study.

## AUTHOR CONTRIBUTIONS

EP-A designed, developed the method, and analyzed the data. AK, RR, BR, HM, PC, and EP-A conceived the study. BR, SKP, SN, and SEP provided the manual segmentation used for the implementation of the method. PC, RR, and AK were part of the supervision of EP-A. AK and EP-A wrote the manuscript with input from all authors.

## FUNDING

EP-A and AK were supported by the EPSRC (EP/R005516/1) and by core funding from the Wellcome/EPSPS Centre for Medical Engineering (WT203480/Z/16Z). This research was funded in part, in part, by the Wellcome Trust (WT203480/Z/16Z). For the purpose of open access, the author has applied a CC-BY public copyright license to any author accepted manuscript version arising from this submission. SEP, AK, and RR acknowledge funding from the EPSRC through the Smart Heart Programme grant (EP/P001009/1). EA, BR, IM,

AK, and RR acknowledged support from the Wellcome/EPSPS Centre for Medical Engineering at King's College London (WT 203480/Z/16Z), the NIHR Cardiovascular MedTech Cooperative award to the Guy's and St Thomas' NHS Foundation Trust and the Department of Health National Institute for Health Research (NIHR) Biomedical Research Centre award to Guy's & St Thomas' NHS Foundation Trust in partnership with King's College London. SEP, SN, and SKP acknowledged the British Heart Foundation for funding the manual analysis to create a cardiovascular magnetic resonance imaging reference standard for the UK Biobank imaging resource in 5,000 CMR scans (www.bhf.org.uk/research). SEP acknowledged support from the National Institute for Health Research (NIHR) Biomedical Research Centre at Barts. SEP received funding from the European Union Horizon 2020 Research and Innovation Programme under grant agreement No 825903 (euCanCARE project). SEP also acknowledged support from the CAP-AL Programme, London. EHT AI Enabling Programme focused on stimulating growth in the capital's AI Sector. CAP-AI was led by Capital Enterprise in partnership with Barts Health NHS Trust and Digital Catapult and was funded by the European Regional Development Fund and Barts Health NHS. SEP acknowledges support from the Health Data Research UK, an initiative funded by UK Research and Innovation, Department of Health and Social Care (England) and the devolved administrations, and leading medical research charities. SN and SKP were supported by the Oxford NIHR Biomedical Research Centre and the Oxford British Heart Foundation Centre of Research Excellence.

## ACKNOWLEDGMENTS

This research has been conducted using the UK Biobank Resource (application numbers 17,806 and 2,964) on a GPU generically donated by NVIDIA Corporation. The UK Biobank data are available for approved projects from 
[https://www.ukbiobank.ac.uk/](https://www.ukbiobank.ac.uk/)
.

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: 
[https://www.frontiersin.org/article/10.3389/fcm.2022.859310/full#supplementary-material](https://www.frontiersin.org/article/10.3389/fcm.2022.859310/full#supplementary-material)

## REFERENCES

1. Constantinides B, Fitzmaurice DA. Artificial intelligence in cardiology: applications, benefits and challenges.*Br J Cardiol*. (2018) 7:25–86.
2. Lalonde JP, Javel D, Novoa RA, Xu L, Suetter SK, Bao HQ, et al. Dermatologic facial classification of skin cancer with deep neural networks.*Nature*. (2017) 542:115–8. doi: 10.1038/nature21080
3. Goulden N, Ocampo PA, Sakala-Okogun T, Novoa N, Sneddon M, Ferro D. Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning.*Nat Med*. (2018) 24:1559–67. doi: 10.1038/nm.4188-0777-5
4. Johnson KW, Torres Soto I, Glickberg BS, Shumate K, Montie R, Ali M, et al. Artificial intelligence in cardiology.*J Am Coll Cardiol*. (2018) 71:2048–75.
5. Bai W, Sinclair M, Tierney O, Okoye O, Rajdip M, Vulliamy G, et al. Automated cardiovascular magnetic resonance image analysis with fully convolutional networks.*J Cardiovasc Magn Reson*. (2018) 20:65. doi: 10.1186/s12968-018-0471-x
6. Bersani O, Lalonde A, Zotti C, Cervenansky Y, Yang X, Heng P, et al. Deep learning techniques for automatic CMR cardiac multi-structure segmentation and diagnosis: is the problem solved?*IEEE Trans Med Imaging*. (2018) 37:215–24. doi: 10.1109/TMI.2017.287502

<!-- PAGE 10 -->

Yonezawa K, Venkatesh BA, Bhanuka DA, McClelland RL, Lima JAC. Cardiovascular magnetic resonance in an adult human population: serial observations from the multi-ethnic study of atherosclerosis (Cardiovascular Magnetic Resonance, 2007) 19:52. doi: 10.1186/12968016-007-13627-1

Holmes MD. Basal recapitulation in the use of procedures for ischemic heart disease. JAMA. (1989) 261:2342–5. doi: 10.1001/jama.1989.0342020502414

Begley-Zagorodny V, Oerlebke-Pignone S, Prescott E, Francou F, Gervais E, Peyret-Lodding A, et al. Gender in cardiovascular diseases: impact on clinical manifestations, management, and outcomes. Eur Heart J. (2016) 37:518–34. doi: 10.1093/eurheartj/ehv398

Oerlebke-Pignone S, Begley-Zagorodny V. Sex and Gender Aspects in Clinical Medicine. London: Springer (2017).

Kawai SM, Lima JAC, Barr RG, Chalal H, Jain A, Tendril A, et al. Sex and gender differences in right ventricular function in hypertension. Circulation. (2011) 123:2542–51. doi: 10.1161/CIRCULATIONAHA.111.083515

Capraro G, Zemelka M, Mathuranga V, Pereira SE, L.C. Daoust P, et al. Facial analysis of myocardial trabeculations in 2547 study participants: multi-ethnic study of atherosclerosis. Radiology. (2015) 276:104–11. doi: 10.1148/radiol.2015147033

2013.42958

Kuhn J, Pott P, Venkatesh BA, Gidding SS, Armstrong AC, Jacobs DR, et al. Race-ethnic and sex differences in left ventricular structure and function: the coronary artery risk development study (CARDIA) study. J Am Heart Assoc. (2015) 4:e001254. doi: 10.1161/JAHA.114.001254

Proctor S, Raisin J, Raisin B, Proctor S, Noubiak S, Pereira SE, et al. Sex differences in deep learning based segmentation: An investigation of bias due to data imbalance in deep learning based segmentation. In: Proceedings of the International Conference on Medical Image Computing and Computer-Assisted Intervention – MICCAI 2022. Cham: Springer (2022) p. 413–23.

Sadler J, Schiller J, Allen B, Bierman R, Dandale S, et al. UK biobanks: an open access resource for identifying the causes of a wide range of complex diseases of middle age. PLoS Med. (2013) 10:e1001779. doi: 10.1371/journal.pmed.1001779

International Statistical Institute. Cross-Risks of Scotland, Northern Ireland Statistics and Research Agency. 2017 Census Aggregate Data (Edition: February 2017). UK Data Service (2017). doi: 10.5255/2776/aggregates_2017_1

Peterson SE, Matthews PM, Francis JM, Robson MD, Zemelka B, Bodenbarker R, et al. Sex-specific cardiovascular magnetic resonance protocol. J Cardiovascular Magnetic Resonance. (2018) 18:68. doi: 10.1186/s12968-018-0227-4

Isensee J, Jaeger PF, Kohl SA, Petersen J, Maier-Hein KH, et al. Net: a self-configuring deep learning method for biomedical image segmentation. Nat Methods. (2020) 17:1820–11. doi: 10.1038/s41592-020-01006-9

Wang L, Shao K. Fast bin-leaf-based tree-structure: checking unsupervised coregistration predictions. Ann Clin Transl. (2023) 10:533–53. doi: 10.1002/ctn.1589

Peterson SE, Augs N, Smajlov TM, Zemelka B, Fung K, Pava JM, et al. Refinement for cardiac structure and function using cardiovascular magnetic resonance (CMR) in Caucasians from the UK biobank population cohort. J Cardiovascular Magnetic Resonance. (2021) 23:19. doi: 10.1186/s12968-021-00272-9

Wang L, Matthews PM, Isensee J, Augs N, Fung K, Pava J, et al. Towards the semantic enrichment of free-text annotation of image quality and UK biobank radiological data. In: Proceedings of the German Conference on Pattern Recognition (ICPR). Berlin: Springer (2021). p. 107–17. doi: 10.1007/978-3-662-63055-0_12

Wang L, Pava J, Augs N, Matthews PM, Isensee J, Smajlov TM, et al. Fully automated, quality-controlled cardiac analysis from CMR. IEEE Trans Biomed Imaging. (2020) 13:648–65. doi: 10.1109/tbi.2019.2955030

Borkert R, Coato A, Trautel H, Abidullah M, Adamopoulos S, Albert N, et al. Universal definition and classification of heart failure. J Card Fail. (2021) 27:30–41.

Perdikouli P, Vouros AA, Akerlof S, Berris J, Cleland JFC, Pau A, et al. 2016 ESC guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. (2016) 37:2120–200.

Buschmann J, Geltay T. Gender studies: international accuracy disparities in commercial gender classification. In: Friede S, Wilson C. editors. Proceedings of the 1st Conference on Fairness, Accountability and Transparency. New York (NY, USA): 77–91.

Seyyedi Kalantarati L, Liu G, McClelland M, Chen TC, Chassman M, ChChelouche. Fairness Gaps in Deep Credit Risk Classifiers. Singapore: World Scientific (2020).

Larranzola AJ, Nieto N, Peterson V, Milner DH, Ferrante E. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis. Pre-Print arXiv:2005.01239. doi: 10.1037/bul0012117

World Health Organization (WHO). Committee on Understanding and Eliminating Racial and Ethnic Disparities in Health Care. Unequal Treatment: Confronting Racial and Ethnic Disparities in Health Care. Washington, DC: National Academies Press (2001).

Smith T, Taylor E. Understanding gender bias in computer vision: problems and promise. Health Care Women J. (2011) 32:555–65. doi: 10.12220/HCW.32.555

Noserworthy PA, Attia ZI, Brewer LC, Hayne SN, Yao X, Kapa S, et al. Assessing and mitigating bias in medical artificial intelligence. Circ Arrhythm Electrophysiol. (2020) 13:e008798. doi: 10.1161/CIRC:ARR.119.008798

Nah B, Kim J, Moortimer E, Saxena N, Lerman K, Galbany A. A survey on bias and fairness in machine learning. In: Proceedings of the ACM Computing Survey (CSUR). Vol. 54. New York, NY: Association for Computing Machinery (2019): 1–35. doi: 10.1145/3456767

De Bias D, Du Bois D. Standards for the measurement of the approximate surface area of height and weight for known. Arch Intern Med. (1916) 17:865–71. doi: 10.1001/archinte.1916.0001002100010021

**Author Disclaimer:**
 The views expressed are those of the author(s) and not necessarily those of the NHS, the NHS, NHSR, or the Department of Health

**Conflict of Interest:**
 SEP provided consultancy to and a shareholder of Circle Cardiovascular Imaging Inc., Calgary, Alberta, Canada.

The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a conflict of interest.

**Publisher's Note:**
 All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2023 Poyap-Antiby, Smajlov, Marciali, Hawana, Pacholski, Noubiak, Petersen, Berris, Chassman and King. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forms is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction in other forms is permitted, provided that the original