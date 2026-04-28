

<!-- PAGE 1 -->

## ARTICLES

https://doi.org/10.1038/s41467-021-05950-6

natu
medicine

Check for updates

# OPEN

## Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations

Laleh Seyyed-Kalantari
^1,2,3,5^
, Haoran Zhang
^2^
, Matthew B. A. McDermott
^1^
, Irene Y. Chen
^1^
 and Marzyeh Ghassemi
^1,4^

Artificial intelligence (AI) systems have increasingly affected expert-level performance in medical imaging applications. However, there is growing concern that such AI systems may reflect and amplify human bias, and reduce the quality of their performance in historical or sensitive populations such as female patients, Black patients, or patients of low-income or low-status. Such biases are especially troubling in the context of underdiagnosis, whereby the AI algorithm would inaccuracy label an individual with a disease that the population is known to be under-represented for. We apply the concept of underdiagnosis in chest X-ray pathology classification across three large chest X-ray datasets, as well as one multi-source dataset. We find that classifiers produced using state-of-the-art computer vision techniques consistently and selectively underdiagnosed under-represented patient populations and that the underdiagnosis rate was higher for intersectional under-represented subpopulations, for example, Hispanic female patients. Deployment of AI systems using medical imaging for disease diagnosis with such biases can result in extension of existing health biases and can potentially lead to unequal access to medical treatment, thereby raising ethical concerns for the use of these models in the clinic.

A artificial intelligence (AI) algorithms increasingly affect expert-level performance in medical imaging applications. However, there is growing concern that such AI systems may reflect and amplify human bias, and reduce the quality of their performance in historical or sensitive populations such as female patients, Black patients, or patients of low-income or low-status. Such biases are especially troubling in the context of underdiagnosis, whereby the AI algorithm would inaccuracy label an individual with a disease that the population is known to be under-represented for. We apply the concept of underdiagnosis in chest X-ray pathology classification across three large chest X-ray datasets, as well as one multi-source dataset. We find that classifiers produced using state-of-the-art computer vision techniques consistently and selectively underdiagnosed under-represented patient populations and that the underdiagnosis rate was higher for intersectional under-represented subpopulations, for example, Hispanic female patients. Deployment of AI systems using medical imaging for disease diagnosis with such biases can result in extension of existing health biases and can potentially lead to unequal access to medical treatment, thereby raising ethical concerns for the use of these models in the clinic.

In a review of AI algorithms in specific circumstances, different performance on disease diagnosis in Black compared with white patients
^1^
. Although AI algorithms in specific circumstances can potentially reduce bias
^2^
, direct application of AI has also been shown to systematize biases in a range of settings
^3–11^
. This tension is particularly pressing in healthcare, where AI systems can improve patient health
^12^
 but can also exhibit biases
^13^
. Motivated by the racial underdiagnosis shortage
^14–16^
, we demonstrate that AI algorithms can match specialist performance particularly in medical settings, but biased diagnostic tools present a clear incentive for real-world deployment.

Although much work has been done in algorithmic bias
^17^
 and bias in health
^18^
, the topic of AI underdiagnosis has been relatively unexplored. Crucially, underdiagnosis, defined as falsely claiming that the patient is healthy, leads to no clinical treatment when a patient needs it most, and could be harmful in radiology specifically
^19^
. Given that automatic screening tools are actively being developed in research
^20–22^
 and have been shown to match specialist performance
^23^
, underdiagnosis in AI-based diagnostic algorithms can be a crucial concern if used in the clinical pipeline for patient triage. Triage is an important diagnostic first step in which patients with no falsely diagnosed as healthy are given lower priority for a clinician visit. As a result, the patient will not receive much-needed attention in a timely manner. Underdiagnosis is potentially worse than overdiagnosis, because in the latter case, the patient still receives clinical care, and the clinician can use other symptoms and data sources to clarify the mistake. Initial results have demonstrated that AI can reduce underdiagnosis in general
^24,25^
 but these studies do not deeply consider the existing clinical image classification against under-served subpopulations. For example, Black patients tend to be more underdiagnosed in chronic obstructive pulmonary disease than non-Hispanic white patients
^26^
.

Here, we perform a systematic study of underdiagnosis bias in the AI-based chest X-ray (CXR) prediction models, designed to predict diagnostic labels from X-ray images, in three large public biology datasets: ChestX-ray14 (CXR14), CheXpert (CXP)
^27^
 and ChestX-ray15 (US National Institutes of Health (NIH)
^28^
), as well as a multi-source dataset combining all three on shared diseases. We focus our analysis on three intersectional and intersectional subgroups spanning race, socioeconomic status (as assessed via the proxy of insurance type), sex and age. The choice of these subgroups is motivated by the clear history, in both traditional medicine and AI algorithms, of bias for subgroups on these axes
^29–31^
. An illustration of our model pipeline is presented in Fig. 1.

**Results**

A standard practice among the AI-based medical image classifiers is to train a model and report the model performance on the overall population regardless of the patient membership to sub-populations
^32–34^
. Motivated by known differences in disease manifestations in patients by sex
^35^
, race/ethnicity
^36^
 and the effect of insurance type in quality of received care
^37^
, we report results for all of these factors. We use insurance type as an indicator of socioeconomic status because, for example, patients with Medicaid insurance are often in the low income bracket. Given that bimodal predictions are often required for clinical decision-making at the individual level, we define and quantify the underdiagnosis rate based on the bimodal model predictions. To assess model decision

University of Toronto, Toronto, Ontario, Canada; Vector Institute, Toronto, Ontario, Canada. Massachusetts Institute of Technology, Cambridge, MA, USA. 
^4^
email: 
[laleh@cs.toronto.edu](#)

NATURE MEDICINE | VOL 27 | DECEMBER 2021 | 2706–2782 | 
[www.nature.com/naturemedicine](#)

<!-- PAGE 2 -->

**NATURE MEDICINE**

**ADVERTISEMENT**

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

**Fig. 1**
 The model pipeline. a. We examine chest radiographs across several subpopulations with diverse diagnoses. b. A deep learning model is then trained from these data (training across all patients simultaneously) to predict the presence of the no finding label, which indicates that the algorithm did not detect disease for the image. c. The underdiagnosis rate (that is, the false-positive rate (FP) of the no finding label) of this model is then compared in different subpopulations (see Methods). d. The age and insurance status of patients in the no finding subpopulation are then analyzed. e. FN, false negative; TN, true negative; TP, true positive. Symbol colors indicate different races of male and female patients.

<div style="display: flex;

<!-- PAGE 3 -->

## ARTICLES

## NATURE MEDICINE

| Subgroup | Attribute | CXR | CPR | NH | ALL |
| --- | --- | --- | --- | --- | --- |
| Sex (%) | Male | 371,858 | 223,648 | 112,02 | 707,626 |
| Female | 52,17 | 38,36 | 19,98 | 110,515 |
| Other | 4783 | 40,64 | 43,51 | 44,87 |
| Age (%) | 0–20 years | 2,20 | 0,87 | 6,09 | 2,40 |
| 20–40 years | 19,51 | 13,18 | 25,96 | 18,55 |
| 40–60 years | 37,12 | 27,83 | 24,83 | 26,24 |
| Race/Ethnicity (%) | >80 years | 3,96 | 38,94 | 23,11 | 39,90 |
| Asian | 3,24 | 16,01 | 1,01 | 8,88 |
| Black | 18,59 |  |  |  |
| Insurance (%) | Hispanic | 6,41 |  |  |  |
| Native | 0,29 |  |  |  |
| White | 67,64 |  |  |  |
|  | Other | 3,83 |  |  |  |
| Medicaid | 46,07 |  |  |  |
| Medicare | 8,98 |  |  |  |
|  | Other | 44,95 |  |  |  |
| ALICE | 2,97% |  |  |  |
| Other | 0,84±0,001 |  |  |  |

The datasets studied are MIMIC-CXR (CXR), CheXpert (CXR), ChestX-ray14 (CXR) and a multi-source dataset (ALL) comprised of aggregated data from the CXR, CPR and NH datasets using the clinical notes (disease labels) and the radiology reports. The table showing results is limited to the first 10 rows of the CXR, CPR and ALL datasets. The models (AUC) are then evaluated for each of the labels in the CXR (A1–A10), CPR (A11–A15), and NH (A16–A20) datasets, and an averaged over all of the labels for each dataset. The reported AUCs (95% confidence interval (CI)) for each dataset is from the average of the AUCs for the five random models with different random seeds using the same train-validation-test split.

overall and interclassical FPR and FNR in Extended Data Figs. 1–3, except for the age >80 years and >20 years subgroups in the NIH dataset, which may again be due to the small number of samples in the >80 years subgroups or to potential dataset selection bias (Methods). The fact that FPR and FNR show an inverse relationship, rather than an increase for both FPR and FNR, suggests that under-served subpopulations are undergoing flagging erroneously as healthy by the algorithm, without a corresponding increase of instances of erroneous diagnoses of disease by the algorithm. This is consistent only with selective underdiagnosis of a condition, rather than a single, undirected errors that could arise from a higher rate of noise alone. Using Fig. 2c–d and Extended Data Figs. 1b,d,2b,d,3b,d we summarize subpopulations with the lowest overdiagnosis rates (lowest FNR for no finding) across the datasets in Table 2.

### Likelihood of underdiagnosis in specific diseases.

The distribution of prevalence in the underdiagnosed patient population is significantly different to that in the general patient population. We compare the disease prevalence in the unhealthy population and the underdiagnosed population for the intersections of race/ethnicity and sex in Supplementary Table 4. For example, underdiagnosed populations are proportionally more likely to have a positive label for lung lesion and less likely to have a positive label for pleural effusion. This suggests that the task of disease detection is more difficult for some diseases than others.

### Fairness definitions in a healthcare context.

Our study considers underdiagnosis as the main fairness concern, due to its potentially harmful impact on patients, such as causing a delay in receiving treatment (for example, assigning lower priority to the underdiagnosed population in a triage use case). We acknowledge that depending on the use case of the algorithm there are many other fairness definitions one may consider. One such definition is predictive parity, which implies equal positive predictive value, or equivalently, false discovery rate (FDR) between the groups
^1^
.

In Supplementary Table 6 we report the additional data for FDR of a no disease diagnosis (that is, the likelihood that the patient is ill given that the classifier predicts no finding). We observe that, similar to FPR and FNR, significant gaps exist across many protected attributes. In particular, the disparities tend to follow a different pattern of that seen for FPR, favoring, for example, female people over male people and younger people over older people. The underlying cause is the difference in prevalence between groups—that is, given that there are far fewer sick people in the b-20 year old group (Supplementary Table 4) we will have relatively fewer false positives and true negatives, which, keeping all else constant, will cause a decrease in the FDR.

### Discussion

We have shown consistent underdiagnosis in three large, public datasets in the chest X-ray domain. The algorithms trained on all settings exhibit systematic underdiagnosis biases in under-served subpopulations, such as female patients, Black patients, Hispanic patients, younger patients and patients of lower socioeconomic status (with Medicaid insurance). We found that these effects persist for interclassical subgroups (for example, Black female patients) but are not consistently worse in the smallest interclassical groups. The specific subpopulations most affected vary in the NIH dataset, specifically male patients and patients aged >80 years, which should be explored further. Beyond these immediate take-aways, there are several topics for further discussion and investigation.

First, we highlight that automatic labeling from notes should be carefully audited. We note that in chest X-ray datasets, there has been a general shift in machine learning from manual image labeling to automatic labeling, with natural language processing (NLP)-based methods used to generate the labels in radiology reports. This has resulted in large annotated chest X-ray datasets
^10–12^
 that are widely used for training deep learning models and for providing AI solutions
^13–15^
. Although automatic labeling has been validated for labeling quality
^16,17^
 and adapted as reliable ground truth, the

<!-- PAGE 4 -->

**Figure 2**
 | Analysis of underdiagnosis across subgroups of sex, age, race/ethnicity and insurance type in the MIMIC-CXR (CXR) dataset. a. The underdiagnosis rate, as measured by the no finding FPR, in the indicated patient subpopulations. b. Intersectional underdiagnosis rates for female patients (b(i)), patients aged 0–20 years (b(ii)), Black patients (b(iii)), and patients with Medicaid (b(iv)), c. The overdiagnosis rate, as measured by the no finding FNR in the same patient subpopulations as in a and b. The results are averaged over five trained models with different random seeds on the same train-validation-test splits. 95% confidence intervals are shown. Subgroups with too few members to be studied reliably (
\le 15
) are labeled in gray text and the results for these subgroups are omitted. Data for the Medicare subgroup are also omitted, given that data for this subgroup are highly confounded by patient age.

<!-- PAGE 5 -->

## ARTICLES

## NATURE MEDICINE

**Table 2**
 | Age and sex subgroups for all four datasets

| Subpopulation | NR | CXP | NH | ALI |
| --- | --- | --- | --- | --- |
| Most underdiagnosed subgroup |  |  |  |  |
| Sex | Female | Female | Female | Female |
| Age (years) | 20–40 | 20–40 | 20–40 | 20–40 |
| Female underdiagnosed group |  |  |  |  |
| Sex | Female | Female | Female | Female |
| Age (years) | 20–40 | 20–40 | 20–40 | 20–40 |
| Male underdiagnosed group |  |  |  |  |
| Sex | Male | Male | Male | Male |
| Age (years) | 20–40 | 20–40 | 20–40 | 20–40 |

inconsistent and may vary based on individual factors such as age, socioeconomic level or the local availability of care. This heterogeneity in self-identification may result in lower model performance for patients of groups for which self-identification criteria are more complex. Finally, this solution is ideal only in the case in which the per-group ROC curves have intersections. In cases in which the ROC curves do not intersect, we would require the FPR combination not corresponding to an intersection between curves, resulting equal FNR for all groups. This would require that the model is that, systematic worsening of the model performance in particular subgroup
^10^
. It is unclear whether worsening the overall model performance for one subgroup to achieve equality is ethically desirable. This is especially relevant in the medical context, in which we often expect that subgroups would have similar areas under the ROC curves (AUCs), given that the difficulty of the problem often varies with the protected group, for example, with women. We do not think that equal FPR alone is thus achievable through threshold adjustments if the underdiagnosis is the main fairness concern; however, such a solution may be useful for other fairness diagnoses (FNR) disparities, in addition to requiring knowledge of the “genuine” group membership
^10^
.

Fourth, despite the fact that we do not have the same disease prevalence between subgroups based on real data
^10,11^
, and our choice of disease metrics is not based on the prevalence of the subgroups, we stress that equal underdiagnosis rates between subgroups of age and sex are not the same as equal FPR. For example, deployed in a clinical pipeline mistakenly underdiagnosed a certain subgroup (for example, Black patients) more than others due to the lower prevalence of the disease, this is not a disadvantage for members of that group and could lead to serious ethical concerns
^10^
. Fifth, we note that fairness definitions are not necessarily in a healthcare context, given that many definitions are not concurrently satisfiable as shown through fairness impossibility theorems
^10,11^
. For example, given that the base rates of the two groups are different, it is impossible for them to have equal FNR, FPR and FDR, unless the classification is completely random
^10^
.

Last, regulatory and policy decision-makers must consider underdiagnosis as a fairness diagnosis in the context of the evaluation of medical algorithms, even those that are built with seemingly robust model pipelines. Given that medical algorithms are increasingly deployed in clinical settings, and that these metrics such as differences in underdiagnosis rates and other health outcomes are not always captured in the current regulatory and deployment. Furthermore, the clinical application and historical performance have been sources of underdiagnosis concerns
^10^
. Patients with low socioeconomic status may have fewer interactions with the healthcare system, or they may be more likely to visit a primary care physician, and therefore may not be aware of treatment plans may be different
^10^
. Our results may not be replicable in health settings in which the dynamics of sex or racial identity are different, or in which the health insurance system operates differently.

Third, although there are possible post-hoc technical solutions for improving fairness, it may not be the best approach. One simple post-processing method for achieving equal FNR and FPR across subgroups is selection of a threshold for all subgroups that groups corresponding to the intersection of their receiver operating characteristic (ROC) curves
^10^
. This means that we are mainly involved in using a different threshold for each group. For example, for interactional subgroups with small populations, an accurate approximation of the threshold might be difficult to obtain because of the large degree of uncertainty. The number of thresholds that can be computed is limited by the number of subgroups, the number of protected attributes, which makes it largely infeasible for interactions of three or more protected attributes. Additionally, race and ethnicity are proxy variables for socioeconomic boundaries. As a result, self-reported race and ethnicity may be

performance of these labelers in different subpopulations has not been investigated. Given that NLP and computer vision have shown biases against under-represented subpopulations in both medical
^10^
 and non-medical domains, the automatic labeler could potentially be a large source of bias.

Second, bias amplification is likely to be generalizable. The prevalence results are consistent in the context of losing biases in clinical care itself, in which under-served subpopulations are often underdiagnosed by doctors without a significant increase in privileged group underdiagnosis
^10^
. Our prediction labels are extracted from clinical records, and are therefore not an unbiased ground truth in our words, our labels may already contain the same bias that our model is then additionally demonstrating. This is a form of bias amplification, where a model predicted outputs amplify a known source of error in the process of data generation
^10^
 or data distribution
^10^
. This is an especially dangerous outcome for machine learning models in healthcare, given that existing biases in health practice risk being magnified, rather than moderated, by algorithmic decisions based on large (707,626 images), multi-source datasets.

We note that some of our observed differences in underdiagnosis have been established in other areas in clinical care, such as underdiagnosis of female patients
^10^
. Black patients
^10,11^
 and patients with low socioeconomic status
^10^
. Therefore, we would expect our results to hold regardless of the algorithm used, given that the disparities we have observed from the data. Moreover, missing data, small sample size and the consistently suboptimal care delivered to some subpopulations have been sources of underdiagnosis concerns
^10^
. Patients with low socioeconomic status may have fewer interactions with the healthcare system, or they may be more likely to visit a primary care physician, and therefore may not be aware of treatment plans may be different
^10^
. Our results may not be replicable in health settings in which the dynamics of sex or racial identity are different, or in which the health insurance system operates differently.

Third, although there are possible post-hoc technical solutions for improving fairness, it may not be the best approach. One simple post-processing method for achieving equal FNR and FPR across subgroups is selection of a threshold for all subgroups that groups corresponding to the intersection of their receiver operating characteristic (ROC) curves
^10^
. This means that we are mainly involved in using a different threshold for each group. For example, for interactional subgroups with small populations, an accurate approximation of the threshold might be difficult to obtain because of the large degree of uncertainty. The number of thresholds that can be computed is limited by the number of subgroups, the number of protected attributes, which makes it largely infeasible for interactions of three or more protected attributes. Additionally, race and ethnicity are proxy variables for socioeconomic boundaries. As a result, self-reported race and ethnicity may be

inconsistent and may vary based on individual factors such as age, socioeconomic level or the local availability of care. This heterogeneity in self-identification may result in lower model performance for patients of groups for which self-identification criteria are more complex. Finally, this solution is ideal only in the case in which the per-group ROC curves have intersections. In cases in which the ROC curves do not intersect, we would require the FPR combination not corresponding to an intersection between curves, resulting equal FNR for all groups. This would require that the model is that, systematic worsening of the model performance in particular subgroup
^10^
. It is unclear whether worsening the overall model performance for one subgroup to achieve equality is ethically desirable. This is especially relevant in the medical context, in which we often expect that subgroups would have similar areas under the ROC curves (AUCs), given that the difficulty of the problem often varies with the protected group, for example, with women. We do not think that equal FPR alone is thus achievable through threshold adjustments if the underdiagnosis is the main fairness concern; however, such a solution may be useful for other fairness diagnoses (FNR) disparities, in addition to requiring knowledge of the “genuine” group membership
^10^
.

Fourth, despite the fact that we do not have the same disease prevalence between subgroups based on real data
^10,11^
, and our choice of disease metrics is not based on the prevalence of the subgroups, we stress that equal underdiagnosis rates between subgroups of age and sex are not the same as equal FPR. For example, deployed in a clinical pipeline mistakenly underdiagnosed a certain subgroup (for example, Black patients) more than others due to the lower prevalence of the disease, this is not a disadvantage for members of that group and could lead to serious ethical concerns
^10^
. Fifth, we note that fairness definitions are not necessarily in a healthcare context, given that many definitions are not concurrently satisfiable as shown through fairness impossibility theorems
^10,11^
. For example, given that the base rates of the two groups are different, it is impossible for them to have equal FNR, FPR and FDR, unless the classification is completely random
^10^
.

Last, regulatory and policy decision-makers must consider underdiagnosis as a fairness diagnosis in the context of the evaluation of medical algorithms, even those that are built with seemingly robust model pipelines. Given that medical algorithms are increasingly deployed in clinical settings, and that these metrics such as differences in underdiagnosis rates and other health outcomes are not always captured in the current regulatory and deployment. Furthermore, the clinical application and historical performance have been sources of underdiagnosis concerns
^10^
. Patients with low socioeconomic status may have fewer interactions with the healthcare system, or they may be more likely to visit a primary care physician, and therefore may not be aware of treatment plans may be different
^10^
. Our results may not be replicable in health settings in which the dynamics of sex or racial identity are different, or in which the health insurance system operates differently.

Third, although there are possible post-hoc technical solutions for improving fairness, it may not be the best approach. One simple post-processing method for achieving equal FNR and FPR across subgroups is selection of a threshold for all subgroups that groups corresponding to the intersection of their receiver operating characteristic (ROC) curves
^10^
. This means that we are mainly involved in using a different threshold for each group. For example, for interactional subgroups with small populations, an accurate approximation of the threshold might be difficult to obtain because of the large degree of uncertainty. The number of thresholds that can be computed is limited by the number of subgroups, the number of protected attributes, which makes it largely infeasible for interactions of three or more protected attributes. Additionally, race and ethnicity are proxy variables for socioeconomic boundaries. As a result, self-reported race and ethnicity may be

inconsistent and may vary based on individual factors such as age, socioeconomic level or the local availability of care. This heterogeneity in self-identification may result in lower model performance for patients of groups for which self-identification criteria are more complex. Finally, this solution is ideal only in the case in which the per-group ROC curves have intersections. In cases in which the ROC curves do not intersect, we would require the FPR combination not corresponding to an intersection between curves, resulting equal FNR for all groups. This would require that the model is that, systematic worsening of the model performance in particular subgroup
^10^
. It is unclear whether worsening the overall model performance for one subgroup to achieve equality is ethically desirable. This is especially relevant in the medical context, in which we often expect that subgroups would have similar areas under the ROC curves (AUCs), given that the difficulty of the problem often varies with the protected group, for example, with women. We do not think that equal FPR alone is thus achievable through threshold adjustments if the underdiagnosis is the main fairness concern; however, such a solution may be useful for other fairness diagnoses (FNR) disparities, in addition to requiring knowledge of the “genuine” group membership
^10^
.

Fourth, despite the fact that we do not have the same disease prevalence between subgroups based on real data
^10,11^
, and our choice of disease metrics is not based on the prevalence of the subgroups, we stress that equal underdiagnosis rates between subgroups of age and sex are not the same as equal FPR. For example, deployed in a clinical pipeline mistakenly underdiagnosed a certain subgroup (for example, Black patients) more than others due to the lower prevalence of the disease, this is not a disadvantage for members of that group and could lead to serious ethical concerns
^10^
. Fifth, we note that fairness definitions are not necessarily in a healthcare context, given that many definitions are not concurrently satisfiable as shown through fairness impossibility theorems
^10,11^
. For example, given that the base rates of the two groups are different, it is impossible for them to have equal FNR, FPR and FDR, unless the classification is completely random
^10^
.

Last, regulatory and policy decision-makers must consider underdiagnosis as a fairness diagnosis in the context of the evaluation of medical algorithms, even those that are built with seemingly robust model pipelines. Given that medical algorithms are increasingly deployed in clinical settings, and that these metrics such as differences in underdiagnosis rates and other health outcomes are not always captured in the current regulatory and deployment. Furthermore, the clinical application and historical performance have been sources of underdiagnosis concerns
^10^
. Patients with low socioeconomic status may have fewer interactions with the healthcare system, or they may be more likely to visit a primary care physician, and therefore may not be aware of treatment plans may be different
^10^
. Our results may not be replicable in health settings in which the dynamics of sex or racial identity are different, or in which the health insurance system operates differently.

Third, although there are possible post-hoc technical solutions for improving fairness, it may not be the best approach. One simple post-processing method for achieving equal FNR and FPR across subgroups is selection of a threshold for all subgroups that groups corresponding to the intersection of their receiver operating characteristic (ROC) curves
^10^
. This means that we are mainly involved in using a different threshold for each group. For example, for interactional subgroups with small populations, an accurate approximation of the threshold might be difficult to obtain because of the large degree of uncertainty. The number of thresholds that can be computed is limited by the number of subgroups, the number of protected attributes, which makes it largely infeasible for interactions of three or more protected attributes. Additionally, race and ethnicity are proxy variables for socioeconomic boundaries. As a result, self-reported race and ethnicity may be

inconsistent and may vary based on individual factors such as age, socioeconomic level or the local availability of care. This heterogeneity in self-identification may result in lower model performance for patients of groups for which self-identification criteria are more complex. Finally, this solution is ideal only in the case in which the per-group ROC curves have intersections. In cases in which the ROC curves do not intersect, we would require the FPR combination not corresponding to an intersection between curves, resulting equal FNR for all groups. This would require that the model is that, systematic worsening of the model performance in particular subgroup
^10^
. It is unclear whether worsening the overall model performance for one subgroup to achieve equality is ethically desirable. This is especially relevant in the medical context, in which we often expect that subgroups would have similar areas under the ROC curves (AUCs), given that the difficulty of the problem often varies with the protected group, for example, with women. We do not think that equal FPR alone is thus achievable through threshold

<!-- PAGE 6 -->

NATURE MEDICINE

ARTICLES

In conclusion, we demonstrate evidence of AI-based underdiagnosis under severe underdiagnosis in diagnostic algorithms trained on chest X-rays. Clinically, underdiagnosis is key importance because undiagnosed patients incorrectly receive no care. We observe, across a large-scale dataset, that combined multi-source dataset, which under-served subpopulations are prominently at significant risk of algorithmic underdiagnosis. Additionally, patients in interventional subgroups (for example, female patients) are particularly susceptible to algorithmic underdiagnosis. Our findings demonstrate a concrete way that deployed algorithms (for example, 
[https://model.ai/ct.org](#)
) could be improved by existing systems and institutions if they consider audit of performance disparities across subpopulations. As algorithm developers from the AI and health care fields consider the ethical concerns regarding the accessibility of medical treatment for underdiagnosed subpopulations and the effective and ethical deployment of these algorithms.

### Online content

Any methods, additional references, Nature Research report- ing statement, source data, extended data, supplementary infor- mation, acknowledgements, peer review information, details of author contributions and competing interests, and statements of data availability are available at 
[https://doi.org/10.1038/s41591-021-01595-0](#)
.

Received 20 January 2021; Accepted: 28 October 2021; Published online: 10 December 2021

### References

1. Hajblum, M., Barocas, S., Kibriya, J. & Levy, K. Mitigating bias in algorithms hiring evaluating claims and practices. In 
*FAIT: Proceedings of the Conference on Fairness, Accountability, and Transparency*
 460–469 (Association for Computing Machinery, 2020).

2. Wurzel, I. et al. Do we have a roadmap for responsible machine learning for health care? 
*Med. J. Aust.*
 214, 10–11 (2021).

3. Chai, D. S., Elaswad, I. G. & Jones, D. S. Implementing machine learning in health care: addressing ethical challenges. 
*N. Engl. J. Med.*
 378, 981–983 (2018).

4. Chai, D. S., Elaswad, I. G. & Jones, D. S. Health training algorithms with artificial intelligence. 
*Nat. Med.*
 26, 16–17 (2020).

5. Oremus, S., Powers, B. W. & Dillenbeck, S. Disclosing bias in AI in algorithm used to manage the health of populations. 
*Science*
 366, 447–448 (2019).

6. Larrazabal, A. J. et al. Gender imbalance in medical imaging datasets. 
*IEEE Open J. Biomed. Eng.*
 2, 106–112 (2021).

7. Sadek, S., Liao, C., Lin, C., McDermott, M., Chen, J. Y. & Ghassemi, M. CheckX-ray: fairness gaps in deep chest X-ray classifiers. In 
*Neural Information Processing Systems*
 12925–12934 (2020).

8. Sadek, S., Liao, C., Lin, C., McDermott, M., Chen, J. Y. & Ghassemi, M. CheckX-ray: fairness gaps in deep chest X-ray classifiers. In 
*Neural Information Processing Systems*
 12925–12934 (2020).

9. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

10. Manzur, A. I. et al. Race and gender disparities are evident in COVID-19 mortality across all severities of measured airflow obstruction. 
*Chest*
 158, 157–164 (2020).

11. Jan, T. Y., Chen, Y.-H., Wu, D. J. Y., Chen, L. J., Reyes Nava, H. & Elbaiby, N. Exploring gender disparities in time to diagnosis. In 
*Machine Learning for Health: 2nd Workshop on Machine Learning for Health Care*
 1–8 (2019).

12. Sadek, S., Gaskin, D. J. & Roberts, T. E. The quality of care delivered to patients within the same hospital varies by insurance type. 
*Health Aff.*
 39, 1714–1720 (2020).

13. Campbell, J. et al. Gender disparities in breast and bladder cancer screening and journal articles 1930–98. 
*W. J. Urology Institute for Employment and Training Research*
 (2019).

14. Dwork, C., Hardt, M., Pitassi, T., Reingold, O. & Zemel, R. Fairness through awareness. In 
*Proceedings of the 32nd International Conference on Machine Learning - Conference Proceedings Track*
 214–224 (Association for Computing Machinery, 2015).

15. Bouziane, J. & Gubin, T. Gender shades: Intersectional accuracy disparities in commercial gender classification. 
*Proc. Mach. Learn. Res.*
 81, 77–91 (2018).

16. Bimrot, A. Radiologist shortage leaves patient care at risk, warns report. 
*College BMJ*
 359, p.g5956 (2019).

17. Rajpurkar, P. et al. CheXNet: radiologist-level pneumonia detection on chest X-rays with deep learning. 
*IEEE Trans. Med. Imaging*
 39, 2011–2021 (2020).

18. Tjandra, T. J. A new evidence-based estimate of patient harms associated with hospital care. 
*J. Patient Saf.*
 12, 122–128 (2016).

19. Whang, J. S., Baker, S. L., Park, S., & Carrillo, A. H. The causes of death in the United States, 2013. 
*N. Engl. J. Med.*
 370, 1265–1271 (2014).

20. Whang, J. S., Baker, S. L., Park, S., & Carrillo, A. H. The causes of death in the United States, 2013. 
*N. Engl. J. Med.*
 370, 1265–1271 (2014).

21. Learning from noise labs to regularized estimation of attention confusion. In 
*IEEE International Conference on Computer Vision and Pattern Recognition (CVPR) 11345–11354*
 (IEEE, 2019).

22. Cohen, J. D., Hashmi, M., Brooks, K. & Berrant, D. On the limits of classification models. Preprint at 
[https://arxiv.org/abs/2009.10252v1](#)
 (2020).

23. Cohen, J. D., Hashmi, M., Brooks, K. & Berrant, D. On the limits of classification models. Preprint at 
[https://arxiv.org/abs/2009.10252v1](#)
 (2020).

24. Cohen, J. D., Hashmi, M., Brooks, K. & Berrant, D. On the limits of classification models. Preprint at 
[https://arxiv.org/abs/2009.10252v1](#)
 (2020).

25. Alon, J., Ben-Aharon, M. A. novel approach for multi-label heart X-ray classification. In 
*IEEE International Conference on Computer Vision and Pattern Recognition (CVPR) 2944–2957*
 (IEEE, 2017). 
[https://doi.org/10.1109/CVPR.2017.302](#)

26. Alkhatib, S., Seyed-Kalantari, L., Khatib, A. & Dabouil, E. Evaluating knowledge in neural networks for chest X-ray classification based software improves radiologist detection of malignant lung nodules on chest radiographs. 
*Radiology*
 294, 144–151 (2020).

27. Rao, S. R. et al. Utility of artificial intelligence tool as a prospective radiology decision support system for lung nodule detection. 
*Invest. Radiol.*
 55, 88–93 (2020).

28. Johnson, A. B. W. et al. MIMIC-CXR: a de-identified publicly available database of chest radiographs with free text reports. 
*Sci. Data*
 6, 317 (2019).

29. Irvin, J. et al. CheXpert: a large-scale chest radiograph dataset with uncertainty labels and expert comparison. 
*Proc. AAAI Conf. Artif. Intell.*
 33, 1861–1868 (2019).

30. Wang, X. et al. ChestX-ray14: hospital-scale chest X-ray database and benchmarks for learning to detect pneumonia from radiographs. In 
*IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 1702–1711*
 (IEEE, 2017). 
[https://doi.org/10.1109/CVPR.2017.302](#)

31. Shen, M. T., Bao, X., & Shukla, R. Pulmonary tuberculosis in differential diagnosis of pneumonia on chest radiographs. 
*Respir. Med.*
 110, 105–110 (2013).

32. Shen, M. T., Bao, X., & Shukla, R. Pulmonary tuberculosis in differential diagnosis of pneumonia on chest radiographs. 
*Respir. Med.*
 110, 105–110 (2013).

33. Zhang, H. et al. An empirical framework for domain generalization in clinical settings. In 
*CHI '21: Proceedings of the Conference on Human Factors in Computing Systems*
 179–296 (Association for Computing Machinery, 2021).

34. Zhang, H., Liu, C., Shukla, M. & Li, Y. A framework for domain generalization: quantifying biases in clinical contextual word embeddings. In 
*CHI '21: Proceedings of ACM Conference on Human Factors in Computing Systems*
 110–120 (Association for Computing Machinery, 2020).

35. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

36. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

37. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

38. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

39. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

40. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

41. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

42. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

43. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

44. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

45. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

46. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

47. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

48. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

49. Sadek, S., Elaswad, I. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. 
*N. Engl. J. Med.*
 385, 1874–1876 (2021).

50. Sadek, S., Elaswad, I. G. & Jones, D

<!-- PAGE 7 -->

**Publisher's note**
 Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

**Open Access**
 This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit 
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)
.

© The Author(s) 2021

<!-- PAGE 8 -->

NATURE MEDICINE

ARTICLES

LETTER

OPEN

## Method

Dataset collection and inclusion criteria. Because of the size of these large datasets, we have not included a complete description of the datasets in the main description, we do not anticipate any issues with selection bias and assume that the collected datasets are representative of patients at these hospitals over the specified years. Only the Chest-x-ray dataset is gathered from the NIH Clinical Center (NIH-CCX-R). In short, we have collected these images from patients who selected based on whether they belong to a disease studied by the Institute.

Image acquisition. We have collected the images from the same pathologist and from both frontal and lateral view images. We include all of the images of each dataset regardless of the time in the medical record. In addition, the two chest-x-ray datasets and six data sets are self-reported in the MMIC-CXR dataset and age is reported at the time of the exam. In the case of the NIH-CCX-R dataset, the other data sets are reported at the time of the examination. In the Chest-x-ray dataset, we have collected the frontal and the lateral view images of the patients. In the NIH-CCX-R dataset, the chest-x-ray images were collected from the patients who were reported >100,000 X-rays for which we do not have these data (there are X-rays from Africa/African Americans, and some from Indian/Alaska Natives, and in the study we have used the shorter terminology white, other, Hispanic, Black and Native American, respectively).

## Definitions and quantification of the fairness metrics. Commonly used fairness definitions such as equality of odds and equality of opportunity10 rely on equalized odds and equalized error rates across groups. However, the fairness of models in binarized fairness metrics because binarized prediction is most often required in applications of medicine. We have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}.
For the NIH-CCX-R dataset, we have used the following definitions to assess fairness in undiagnosed patients we compare undiagnosed rates across classes. In addition, we define the undiagnosed rate of the i-th class of the binarized model prediction for the n-th finding label at the levels of the subgroup i, j, that is, U_{i,j} = \frac{\sum_{n=1}^{N} \mathbb{I}(y_n = i, \hat{y}_n = j)}{\sum_{n=1}^{N} \mathbb{I}(y_n = i)}, where \mathbb{I}(\cdot) denotes the indicator function, y_n is the true class, \hat{y}_n is the predicted class, i is the class, j is the predicted class, N is the total number of patients, and U_{i,j} is the undiagnosed rate of the i-th class of the binar

<!-- PAGE 9 -->

## ARTICLES

## NATURE MEDICINE

### Code availability

The code for training the models on the MIMIC-CXR (CXR)⁴⁰, CheXpert (CXP)⁴¹ and labels is identical to that in 
[https://github.com/LabStryd/ChexLabels](https://github.com/LabStryd/ChexLabels)
. The code for training the CheXNet, res44 (CHEX)⁴² dataset on 15 labels as well as the code for all of the analyses in this paper is presented in 
[https://github.com/LabStryd/VideoAnalysis_NatMed](https://github.com/LabStryd/VideoAnalysis_NatMed)
. We have provided the Code environment in the same repository for the purpose of reproducibility. We are not able to share the trained model and the true labels and predicted labels CSV files of the test set due to the data-sharing agreement. However, we have provided the patient ID per test split, random seed and the code. The true label and predicted label CSV files and trained models can then be generated by users who have downloaded the data from the original source following the procedure described in the Data Availability section.

### References

1. Ramakrishna, O. et al. ImageNet large scale visual recognition challenge.*Int. J. Comput. Vis.***118**, 211–252 (2015).
2. Landrieu, F. et al. DenseNet: implementing efficient ConvNet descriptor pyramids.*Preprint at*[https://arxiv.org/abs/1608.04471](https://arxiv.org/abs/1608.04471)(2016).
3. Goldberger, A. L. et al. PhysioNet, PhysioToolkit, and PhysioBank: components of a new research resource for complex physiologic signals.*Circulation***100**, e21–e27 (2000).
4. Johnson, A., Pollard, T., Mark, R., Berkowitz, S. & Hriog, S. MIMIC-CXR database.*PhysioNet*[https://physionet.org/](https://physionet.org/)10.13026/c2m-0g95 (2020).
5. Johnson, A. et al. MIMIC-IV (version 0.4).*PhysioNet*[https://doi.org/10.13026/c2m-0g95](https://doi.org/10.13026/c2m-0g95)(2020).

### Acknowledgements

The authors thank M. Linder for helpful discussions and acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC) grant FDP-519886 to L.S., K.C. (Microsoft Research (M-L) Canadian Institute for Advanced Research (CIFAR) (M-L) and an NSERC Discovery Grant (to M.G.). The authors also thank Vector Institute for providing high-performance computing platforms.

### Autor contributions

L.S., K.H., M.R.A.M., J.Y.C. and M.G. have substantially contributed to the underlying research and drafting of the paper.

### Competing interests

The authors declare no competing interests.

### Additional information

**Extended data**
 are available for this paper at 
[https://doi.org/10.1038/s41591-021-01595-0](https://doi.org/10.1038/s41591-021-01595-0)
.

**Supplementary information**
 The online version contains supplementary material available at 
[https://doi.org/10.1038/s41591-021-01595-0](https://doi.org/10.1038/s41591-021-01595-0)
.

**Correspondence and requests for materials**
 should be addressed to Labh Seysid Kalantri.

**Peer review information**
 Nature Machine Intelligence thanks Oded Golden-Bayer and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Michael Bause was the primary editor on this article and managed its editorial process and peer review in collaboration with the rest of the editorial team.

**Reprints and permissions information**
 is available at 
[www.nature.com/reprints](www.nature.com/reprints)
.

NATURE MEDICINE | 
[www.nature.com/naturemedicine](www.nature.com/naturemedicine)

<!-- PAGE 10 -->

**A**

**B**

**C**

**D**

**Extended Data Fig. 1**
 Analyzing underdiagnoses over subgroups of sex, age, within ALL dataset (combined CXR, CXP and NIH dataset on shared labels). Fig. S1. Analyzing underdiagnoses over subgroups of sex, age, within ALL dataset (combined CXR, CXP and NIH dataset on shared labels). The results are averaged over 5 trained model with different random seed ± 95% confidence interval (CI). A. The underdiagnosis rate (measured by 'No Finding' FNR). B. The overdiagnosis rate ('No Finding' False Negative Rate (FNR)) over subgroups of sex, age. C. The intersectional underdiagnosis rates within only female patients. D. Examining the overdiagnosis rate for the intersectional identities. The number of images with actual 0 or 1 'No Finding' label in the age - sex intersections in the test dataset is presented in Supplementary Table 1.

<!-- PAGE 11 -->

**ARTICLES**

**NATURE MEDICINE**

**A**

Subgroups FPR

**B**

Subgroups FNR

**C**

Intersectional FPR

**D**

Intersectional FNR

**Extended Data Fig. 2 |**
 Analyzing underdiagnoses over subgroups of sex, age, within CheXpert (CXP) dataset. Fig. S2. Analyzing underdiagnoses over subgroups of sex, age, within CheXpert (CXP) dataset. The results are averaged over 5 trained model with different random seed ± 95% CI. A. The underdiagnosis rate is FPR in No Finding. B. Examining the overdiagnosis rate (No Finding FNR) over sex and age subgroups. C. The intersectional underdiagnosis rates within only female patients, and D. measure the overdiagnosis rate for the intersectional identities. The subgroups labeled in gray text, with results omitted, indicate the subgroup has too few members (<=15) to be used reliably. The number of images with actual 0 or 1 No Finding label in the age-sex intersections in the test dataset is presented in Supplementary Table 1.

**NATURE MEDICINE**
 | www.nature.com/naturemedicine

<!-- PAGE 12 -->

**A**

Subgroups FPR

MALE FEMALE

80 60-80 40-60 20-40 0-20

**B**

Subgroups FNR

MALE FEMALE

80 60-80 40-60 20-40 0-20

**C**

Intersectional FPR

FEMALE

80 60-80 40-60 20-40 0-20

**D**

Intersectional FNR

FEMALE

80 60-80 40-60 20-40 0-20

**Extended Data Fig. 3 | Analyzing underdiagnoses over subgroups of sex, age, within ChestX-ray14 (NH) dataset.**
 Fig. 53. Analyzing underdiagnoses over subgroups of sex, age, within ChestX-ray14 (NH) dataset. The results are averaged over 5 trained model with different random seed ± 95% confidence interval (CI). A. The underdiagnosis rate ('No Finding' FPR). B. The over diagnosis rate ('No Finding' FNR) over subgroups of sex and age. C. The intersectional underdiagnosis rates within only female patients. D. The over diagnosis rate for the intersectional identities. The subgroups labeled in gray first, with results omitted, indicate the subgroup has too few members (<= 10) to be used reliably. The number of images with actual 0 or 1 'No Finding' label in the age - sex intersections in the test dataset is presented in Supplementary Table 1.

<!-- PAGE 13 -->

# nature research

Corresponding author(s): Laleh Seyyed-Kalantari

Last updated by author(s): Oct. 22, 2021

## Reporting Summary

Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Research policies, see our Editorial Policies and the Editorial Policy Checklists.

### Statistics

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.

n/a

✓ Confirmed

☐ The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement

☐ A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly

☐ The statistical test(s) used AND whether they are one- or two-sided

☐ Only common tests should be described solely by name; describe more complex techniques in the Methods section.

☐ A description of all covariates tested

☐ A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons

☐ A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)

☐ For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted

☐ Only P values are exact values whenever suitable

☐ For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings

☐ For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes

☐ Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated

(Our web collection on 
[statistics for biologists](#)
 contains articles on many of the points above.

### Software and code

Policy information about availability of computer code

| Data collection | Data was publicly available. We have not collected the data and no software was used in our side to collect data. We have provided a full reference on data availability session. |
| --- | --- |
| Data analysis | The code for training the models on MMIC-CXR (XR) [26], CheXpert (XRP) [27], and All datasets is identical in ([https://github.com/LalehSeyyed-Kalantari](https://github.com/LalehSeyyed-Kalantari)). The code for training ChestX-ray4 (Mx) [26] datasets on 10 labels as well as the code for all the analyses in this paper is presented in ([https://github.com/LalehSeyyed-Kalantari/diagnosis_NetMed](https://github.com/LalehSeyyed-Kalantari/diagnosis_NetMed)). We have provided the yml Conda environment in the same repository for reproducibility purposes. We are not able to share the trained model and the true label and predicted label CSV file of the test set due to the data-sharing agreement. But we have provided the patient ID per test splits, random seed, and the code. Then the true label and predicted label CSV files and trained models can be generated by users who have downloaded the data from the original source following the procedure that is described in "Data availability" session. |

channels:

- pytorch
- conda-forge
- anaconda
- defaults

dependencies:

- blazr>1.0=0
- ca-certificates=2018.5.14=0
- certifi=2019.3.9=py36_0
- cffi=1.12.3=py36h9c24a2b_0
- cudatoolkit=10.0=1=0
- cycler=0.10.0=py_1

<!-- PAGE 14 -->

-dhost:1.13.3.144&31_3
 -rpost:2.5.1.4=04&43a_1002
 -fortunelg:2.13.1=04&13&7_1000
 -freenyge:2.0.1=04&88&6_1
 -gettax:13.8.1=1=04&58&4_1002
 -gfb:7.56.2=04&26&2_1001
 -gpl-galigis-base:1.14.0=04&88&0_1
 -gpt-gateway:1.14.0=04&88&0_1
 -icu:58.2.0=04&48&5e_1000
 -intel-asmeng:1010=4=433
 -jdbb:0.13.2=04&95_0
 -jpeglib:0=02&4e1a_2
 -krasovsk:1.1.0=04&39&55&8a2_0
 -libd:3.1.3=01&129=04&5&8e_0
 -libffi:3.2.1=04&85&5_4
 -libgcrypt:2.0=04&65&5_0
 -libgfortran-ng:7.3.0=04&35&0_0
 -libiconv:1.15.4=03&09&9a_1005
 -libpng:1.6.37=04&83&047_0
 -libtiff:0.8.2.0=04&03&0_1
 -libtiff:4.0.13&n=731037_2
 -libuuid:2.32.1=1=14&3975_1000
 -libxcb:1.13=14&3767_1002
 -libxml2:2.9.9=1=13577&0_0
 -matplotlib:1.1.0=04&9_1
 -matplotlib-base:3.1.0=04&39&68&1e_1
 -mkl:2019.4=4243
 -mkl-service:2.0.2=04&39&764&7c_0
 -mkl:10.1=12=04&38&44&87c_0
 -mkl_random:1.0.2=04&39&81&0a3_0
 -ncurses:6.1=04&71&0_1
 -ninja:1.9.0=04&81&6&8e_0
 -numpy:1.16.4=04&9=04&9e_0
 -numpy-base:1.16.4=04&39&04&8d_0
 -openssl:1.0.2p_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0.4=04&7c_0
 -openssl:1.1.1=04&47c_0
 -openssl:1.0

<!-- PAGE 15 -->

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research 
[guidelines for submitting code & software](#)
 for further information.

## Data

**Policy information about availability of data**

All manuscripts must include a 
**data availability statement**
. This statement should provide the following information, where applicable:

- Access codes, unique identifiers, or web links for publicly available datasets
- A list of figures that have associated raw data
- A description of any restrictions on data availability

All three datasets that we have used for this work are public and under data use agreements, and the experiments are based on observational, retrospective data. The datasets are all well-referenced in the paper. Here is the link to each of the datasets:

- MMIC-CXR [2] dataset is available at:[https://physionet.org/content/mmic-cxr/2.0.0/](https://physionet.org/content/mmic-cxr/2.0.0/)
- CheXpert [27] dataset is available at:[https://stanfordmlgroup.github.io/competitions/chexpert/](https://stanfordmlgroup.github.io/competitions/chexpert/)
- Chest-Xray14 [28] dataset is available at:[https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community)

Access to all three datasets requires user registration and the signing of a data use agreement. Thus access is provided in a timely manner. Only the MMIC-CXR dataset also requires the completion of a credentialing process, that takes a few hours to be completed. After following this procedure the MMIC-CXR data is available through Physionet [42]. The MMIC-CXR project page on Physionet describes the data access procedure [43]. The raw/credentials and insurance type of the patients are not provided naturally with the download of the MMIC-CXR dataset. However, this data is available through merging the patient IDs in MMIC-CXR with subject ID in MMIC-W [44] using the patient and admissions tables. Access to MMIC-W requires a similar procedure as MMIC-CXR and the same credentialing process is applicable for access to both datasets.

## Field-specific reporting

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.

 Life sciences 
 Behavioural & social sciences 
 Ecological, evolutionary & environmental sciences

For a reference copy of the document with all sections, see 
[nature.com/documents/reporting_summary-flat.pdf](#)

## Life sciences study design

All studies must disclose on these points even when the disclosure is negative.

**Sample size**
 In total, we use over 98,000 chest x-ray images for model training, with specific ablations for subgroups and dataset source. While there is no definitive threshold set for convergence of deep neural network model training, the machine learning literature generally suggests that over 50,000 samples is appropriate for convolutional neural network convergence in fine-tuning of natural and medical images. We have randomly sampled 10%, 10%, and 60% of the patients of each whole dataset for train, validation and test set, such that each patient medical images belongs to only one of the train, test and validation sets. We have not done any other sampling from the whole dataset in our model development. The details on the number of images per dataset (sample size) and where they have been collected are presented in Human research participant session in this document (next page).

**Data exclusions**
 No data was excluded.

**Replication**
 To ensure reproducibility, we save all model random seeds, and have released the source code for model training upon acceptance.

**Randomization**
 As no human subject evaluation was performed, we did not require randomization groups.

**Binding**
 As this study contained no human evaluation or intervention, and only profiles computational models on a fixed dataset, no blinding was necessary.

## Reporting for specific materials, systems and methods

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.

<!-- PAGE 16 -->

## Materials & experimental systems

| n/a | Involved in the study | n/a | Involved in the study |
| --- | --- | --- | --- |
|  | Antibodies |  | CHIP-seq |
|  | Eskeptic cell lines |  | Flow-cytometry |
|  | Palaeontology and archaeology |  | MR-based neuroimaging |
|  | Animals and other organisms |  |  |
|  | Human research participants |  |  |
|  | Clinical data |  |  |
|  | Dual use research of concern |  |  |

## Methods

### Human research participants

Policy information about studies involving human research participants

We have used already existing public data on human Chest X-rays and we have not collect them. The distribution of age data over sex and age is provided in table 2. One one of the datasets has the race and insurance type of the patients where we have reported in the Table 2.

| Images | OR: 373,858 |
| --- | --- |
|  | OP: 223,648 |
|  | NH: 112,120 |
| Sex |  |
| OR-Male: 52.17% |  |
| OR-Female: 47.83% |  |
| OP-Male: 59.36% |  |
| OP-Female: 40.64% |  |
| NH-Male: 56.49% |  |
| NH-Female: 43.51% |  |
| Age | OR |
| 0-20 | 3.20% |
| 20-40 | 19.51% |
| 40-60 | 37.20% |
| 60-80 | 34.17% |
| 80+ | 6.96% |
| Age | OP |
| 0-20 | 0.87% |
| 20-40 | 13.18% |
| 40-60 | 31.00% |
| 60-80 | 38.94% |
| 80+ | 16.01% |
| Age | NH |
| 0-20 | 6.09% |
| 20-40 | 25.96% |
| 40-60 | 43.83% |
| 60-80 | 38.94% |
| 80+ | 1.12% |
| OR: Race/Ethnicity |  |
| Asian | 3.24% |
| Black | 38.52% |
| Hispanic | 6.41% |
| Native | 0.29% |
| White | 67.64% |
| Other | 3.83% |
| OR: Insurance |  |
| Medicare | 46.07% |
| Medicaid | 8.98% |
| Other | 44.95% |

### Recruitment

Because of the size of these large datasets, and the fact that no exclusionary criteria are mentioned in the dataset descriptions, we do not anticipate any issues with selection bias and assume that the collected datasets are representative of patients at these hospitals over the specified years. Only the ChestX-ray4 dataset is gathered from the NIH clinical research dedicated hospital where patients are treated without charge, unlike most hospitals, the Clinical Center does not routinely

<!-- PAGE 17 -->

provide standard diagnostic and treatment services. Admission is selective: patients are chosen by Institute physicians solely because they have an illness being studied by those Institutes
^1^
, as mentioned in their website (
[https://clinicalcenter.nih.gov/about/welcome/faq.html](https://clinicalcenter.nih.gov/about/welcome/faq.html)
)

NIH dataset has only frontal view images where the other datasets have both frontal and lateral view images. We include all the images of each dataset regardless of their view in the model training and evaluation.

The race/ethnicity and sex data are self-reported in the MMIC-COR dataset and age is reported at a patient's first admission. In the CheXpert dataset, sex is assigned by clinicians and the age is at the time of the examination. In the ChestX-ray14 dataset, the sex is self-identified and the age corresponds to the time of the examination. In the MMIC-COR dataset, we only have the race/ethnicity and insurance type data of a patient if the patient was admitted to an ICU, so there are around ~100,000 cases where we do not have this data (there are x-rays done for patients who were only admitted to the emergency department. The reported race/ethnicities in MMIC-COR dataset are WHITE, OTHER, HISPANIC/LATINO, BLACK/AFRICAN AMERICAN, AMERICAN INDIAN/ALASKA NATIVE, where in this study we have used shorter terminology White, Other, Hispanic, Black, and Native for each group, respectively.

| Ethics oversight | Since we have worked on public, anonymized, retrospectively collected data, and we have not collected any human data ourselves we did not get any organizational/IRB approval. These public datasets are largely and commonly used in the machine learning medical imaging literature. |
| --- | --- |

Note that full information on the approval of the study protocol must also be provided in the manuscript.