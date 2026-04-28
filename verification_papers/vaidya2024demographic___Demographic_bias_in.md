<!-- Page 1 -->

nature medicine

Article

[https://doi.org/10.1038/s41591-024-02885-z](https://doi.org/10.1038/s41591-024-02885-z)

# Demographic bias in misdiagnosis by computational pathology models

Received: 3 September 2023

Accepted: 23 February 2024

Published online: 19 April 2024

 Check for updates

Anurag Vaidya1,2,3,4,5,12, Richard J. Chen1,2,3,4,6,12, Drew F. K. Williamson1,2,12, Andrew H. Song1,2, Guillaume Jaume1,2,3,4, Yuzhe Yang1,2, Thomas Hartvigsen1, Emma C. Dyer10, Ming Y. Lu1,2,3,4,9, Jana Lipkova1,2,3,4, Muhammad Shaban1,2,3,4, Tiffany Y. Chen1,2,3,4 & Faisal Mahmood1,2,3,4,11

Despite increasing numbers of regulatory approvals, deep learning-based computational pathology systems often overlook the impact of demographic factors on performance, potentially leading to biases. This concern is all the more important as computational pathology has leveraged large public datasets that underrepresent certain demographic groups. Using publicly available data from The Cancer Genome Atlas and the EBRAINS brain tumor atlas, as well as internal patient data, we show that whole-slide image classification models display marked performance disparities across different demographic groups when used to subtype breast and lung carcinomas and to predict IDH1 mutations in gliomas. For example, when using common modeling approaches, we observed performance gaps (in area under the receiver operating characteristic curve) between white and Black patients of 3.0% for breast cancer subtyping, 10.9% for lung cancer subtyping and 16.0% for IDH1 mutation prediction in gliomas. We found that richer feature representations obtained from self-supervised vision foundation models reduce performance variations between groups. These representations provide improvements upon weaker models even when those weaker models are combined with state-of-the-art bias mitigation strategies and modeling choices. Nevertheless, self-supervised vision foundation models do not fully eliminate these discrepancies, highlighting the continuing need for bias mitigation efforts in computational pathology. Finally, we demonstrate that our results extend to other demographic factors beyond patient race. Given these findings, we encourage regulatory and policy agencies to integrate demographic-stratified evaluation into their assessment guidelines.

Rapid advancements of artificial intelligence (AI) and deep learning (DL) in computational analysis of digital pathology images—known as computational pathology1—have led to substantial progress across diverse tasks such as cancer subtyping2, prognostication3 and mutation prediction4. Due to the limited availability of large patient cohorts with associated clinical metadata, a common practice in computational

pathology involves training algorithms on publicly available data from consortia such as The Cancer Genome Atlas (TCGA). These algorithms are then often tested in domain test sets from the same consortia5–11 or on smaller, independent cohorts from external institutions12–14. Recent works have shown that DL models can learn dataset-specific bias and artificially inflate performance when trained and tested on

A full list of affiliations appears at the end of the paper. ✉ e-mail: 
[faisal.mahmood@bwh.harvard.edu](mailto:faisal.mahmood@bwh.harvard.edu)

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1174

---

<!-- Page 2 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

public datasets, even with careful dataset-splitting strategies to prevent data leakage14,17. However, it remains largely unexplored whether these strategies work when applied to real-world data. In this study, we used pathology models trained on public data but tested on external cohorts, which likely have different demographic compositions and do not share the same data biases as the training set. With strong evidence from the general machine learning community revealing inadvertent biases of DL models when testing on independent datasets18–22, there is a need to conduct a systematic investigation into this matter.

One prominent form of bias evident within publicly available datasets is found in demographic compositions. For women training of patients from minority demographic groups. For instance, across 8,594 samples from 33 cancer types in TCGA, 82.0% of all patients are white, 10.1% are Black or African American, 7.5% are Asian, and 0.4% are Hispanic. Native American populations are underrepresented in Pacific Islanders (denoted as ‘other’ in TCGA). However, these percentages are quite different from those of the general population in the United States, which are now higher: 62.1% are white, 12.4% are Black, 5.8% of the population23. This disproportional representation is endemic in other public computational pathology datasets24–27, and it is highly probable that the demographic distribution of patients in these public demographic compositions will skew when training datasets. Such disproportionate representation becomes problematic in the context of well-established studies, which demonstrate that ethnicity and race-related risk factors28–31, along with social determinants of health, lead to variable variations in disease presentation32, molecular subtypes33, incidence34, and outcomes between distinct demographic groups35–39.

Therefore, it becomes paramount for stakeholders to carefully assess how different demographic compositions when training datasets and testing cohorts may influence the performance of DL models40–42. Computational pathology study types typically do not evaluate model performance across diverse datasets, but instead use a single dataset (see Data Table 1 for more examples). Although demographic shift and other biases have been extensively studied in radiology40,41 and other medical fields43,44,45, this question has not yet been fully explored in computational pathology. In this study, we highlight that the demographic such as race are generally not incorporated into diagnostic or patient triaging processes in the clinical practice into pathology. Second, existing datasets are not curated in a race-stratified manner, making systematic evaluation more challenging.

To aid the advancement of accurate and fair methods in computational pathology, we here examined demographic disparities in two types of clinically important cancer diagnostic tasks: subtyping and staging. In lung cancer, the most common cause of death from lung cancer. Cancer subtyping is critical for clinical triaging, and errors can result in inappropriate and harmful treatment regimens46. In lung cancer, in lung adenocarcinoma, the most common histological factor, crizotinib bevacizumab benefits only patients with adenocarcinoma and is not recommended for patients with squamous cell carcinoma. Conversely, the anti-epidermal growth factor receptor drug erlotinib is effective for patients with squamous cell carcinoma. We accurately identified IDH1 mutations is essential for diagnosis of gliomas, serving as an important prognostic indicator and informing the treatment strategy47. To assess the utility and equity of models in these tasks in a simulated environment, we used publicly available metrics. To measure performance across demographic groups, we used demographic-stratified area under the receiver operating characteristic curve (ROC AUC) and F-score. To measure fairness under the demographic importance metric, we used the demographic importance rate (DPI) of demographic groups with that of the overall population. Concurrently considering these metrics helped us examine whether model will have disparate results employed clinically. Using these metrics, we investigated the impact of techniques to mitigate image acquisition differences and batch effects on performance and

fairness of downstream tasks. We also explored the consequences of common modeling choices in computational pathology and bias mitigation techniques. We used a simple model architecture (simpleCNN) (ML) classification models. While our experiments focused on fairness in terms of self-reported race, other demographic factors can be used, which we explored in isolation and intersection with self-reported race.

## Results

### Data set and study description

Our investigations considered subtyping breast and lung carcinomas and staging of breast and lung adenocarcinoma. The TCGA dataset contains brain tumor atlas and in-house patient data. For breast subtyping, we trained models on the TCGA breast invasive carcinoma (TCGA-BRCA) cohort (n = 1,049) to differentiate between invasive ductal carcinoma (IDC) and invasive lobular carcinoma (ILC) of the breast. For lung subtyping, models were trained on the TCGA-LUNG cohort (n = 1,043) to distinguish between lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (LUSC). Models were then evaluated on independent test cohorts collected at Mass General Brigham (MGB) (breast, n = 1,265; lung, n = 1,960). For IDH1 mutation prediction, models were trained on the EBRAINS brain tumor atlas (n = 873) to differentiate between gliomas (astrocytoma, oligodendroglioma, mixed glioma, and blastoma (TCGA-GBM) and low-grade glioma (TCGA-LGG) cohorts (collectively called the TCGA-GBLMG cohort) (n = 1,123). TCGA, a publicly available data consortium collecting tissues and clinical metadata for 33 cancer types, has been used extensively in research towards cancer. With few examples from other underrepresented ethnicities (Fig. 1). Numerous clinical sites have contributed to TCGA with site-specific differences in image acquisition, demographics and label distribution48. In contrast, the MGB cohorts, while also having a majority of white people (Supplementary Data Tables 2 and 3), reflect the patient population at Massachusetts General Hospital and Brigham and Women's Hospital in Boston. The base rates of classes differ among cohorts (TCGA-BRCA: MGB and the EBRAINS brain tumor atlas, as well as among races. White and Black patients generally exhibit a skew toward the IDH1 wild type, and IDC and LUAD classes, whereas the class distributions vary for Asian patients (Supplementary Data Tables 2 and 3). Tables 2 and 3 extend to sex, with TCGA-LUNG and TCGA-BGLMG skewed toward male patients, MGB-lung having a majority of female patients, and both the TCGA-BRCA and MGB-breast cohorts including a small number of male patients (Supplementary Data Tables 2 and 3). TCGA-BRCA lacks information on patient insurance or income, whereas only a few MGB cohort patients are uninsured. In our datasets, Black patients are often younger or similar in age to white patients, whereas Asian patients are older (Supplementary Data Tables 2 and 3). In our atlas of lung cancer, also a public dataset collected at the Medical University of Vienna49. No information on patient race, insurance and income is provided. We use sex as patient age, sex, and race as covariates in our models. Further details and the full data collection description are available in Supplementary Data Tables 2–4 and Methods.

Due to the large size of digital histology slides, known as whole slide images (WSIs), we used a simple CNN (the MILS) to predict slide-level labels in a weakly supervised manner. The framework consists of customizable parts (Fig. 1b): segmentation of tissue from background and tessellation into patches; projection of patches onto a 2D grid; and concatenation of patches with enhanced concatenation of patches into slide-level representations, which are classified into the desired labels51. We considered various popular choices for all stages and studied their effects on fairness. For the patch encoder, we used a 100-layer convolutional encoder (100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 100 × 10

---

<!-- Page 3 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

a Training and validation

TCGA-BRCA (n = 1,048)

Asian (5.2%) White (69.5%) Black (16.6%) Nonreporting/other (8.7%)

Site 1 Site 2 Site 3 Site 40

TCGA-Lung (n = 1,043)

Asian (10.0%) White (73.3%) Black (8.9%) Nonreporting/other (8.8%)

Site 1 Site 2 Site 3 Site 73

EBRANS brain tumor atlas (n = 835)

Nonreporting (100%)

Site 1

b WSI

Segment and patch

- Site stratification
- Size normalization
- Text set reampling
- Importance weighting

Patch embeddings

- RealSiDN (RM natural images)
- CLIPaug (ISM history images)
- UKE (DOOM history images)

WSI embedding

- ABM-L
- CLAM
- TransMIL

WSI embedding

Task prediction

- Control batch effects
- Modeling choices
- Bias mitigation strategies

c Original training set

Weighted sampling

Balanced training set

d

Patch aggregator

Race attribute

Task classifier

Task classifier

Task classifier

Minimize loss in task classifier

Maximize loss in task classifier

Debiased task classifier

Fig. 1 | Dataset characteristics, fairness metrics and modeling choices investigated. a, Composition in number of slides for TCGA, cohorts from MGB, and the EBRANS brain tumor atlas, which were used to investigate demographic bias in ML. b, Different stages of the DL pipeline used in MLL, including pathology studies: tissue segmentation and patching, mapping to low-dimensional representation using a patch encoder, and classification. Techniques investigated with respect to fairness are shown (control batch effects and test set bias, modeling choices, and bias mitigation strategies). c, d, Common

bias mitigation strategies investigated in c. d, IV samples patients from racial groups inversely to their population size to ensure equitable representation. d, AR mitigates bias by making embeddings agnostic to race. Loss from a secondary race classifier is maximized to achieve this. Example ROC curves show mean values (n = 10 folds) with 95% CI. Boxes indicate quartile values of TPR discrepancy (n = 10 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5 \times the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. Detailed demographic distributions for each task are available in Supplementary Data Tables 2–4. Some illustrations were created with BioRender.com.

subtype or mutation labeling, which could lead to artificially inflating performance when testing on TCGA12. Next, we considered three common patch aggregator modules that differ in how relations between the

patches are assumed, namely attention-based MIL (ABMIL) (patches are independent)13, clustering-constrained attention MIL (CLAM)14 and transformer-based MIL (TransMIL) (patch interactions learned)15,17.

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1176

---

<!-- Page 4 -->

Article

https://doi.org/10.1038/s41591-024-02985-x

Finally, we investigated two common bias mitigation strategies, namely importance weighting (IW)16–18 (Fig. 1c) and adversarial regularization (AR)19,20 (Fig. 1d,b).

To assess the effect of modeling choices and data processing techniques on the performance and fairness of classification models, we compared a few performance metrics, namely demographic-stratified ROC AUC and F1 score. We also compare TPR disparity between different races and the entire cohort population, under the framework of equalized opportunity21–23, which has been used in other medical fairness and general studies24–26. The AUC reflects the model's ability to discriminate between positive and negative samples, while the F1 score reflects the balance between the model's precision and recall. However, the AUC and F1 score do not show class-specific error rates, which are crucial for understanding model weaknesses. Therefore, we examined TPR disparity to detect performance differences among binary classes (refer to 'Definition and quantification of the fairness metrics' in Methods for more details). A TPR disparity of zero for a demographic group indicates a similar group performance. A TPR disparity of zero for a higher or lower TPR from the population, indicating signs of unfairness. Clinically, sensitivity is paramount as it reflects the model's success in identifying true cases. Thus, TPR disparity provides meaningful clinical insight into potential performance differences between groups. By evaluating race-stratified AUC, F1 scores and TPR disparities, we can understand both the performance and fairness of our model for each race, ensuring the model's utility and equity in clinical settings.

### Baseline race-stratified assessment

A standard study design for model development in computational pathology is randomly splitting a large public dataset (as such TCGA) into training and validation folds, which do not account for different patient demographic subgroups. To understand first to what degree this standard approach affects the subgroup-specific performance of a deep learning model, we trained a baseline model using the TCGA-BRCA, TCGA-lung and EBRAINS brain tumor atlas cohorts into 20 task label-stratified, Monte Carlo cross-validation (CV) folds and trained models using AMBL17—a popular widely supervised slide-level segmentation algorithm. We trained the models using the AMBL algorithm tasks22,24,25. We then assessed the performance on independent test cohorts, namely MGB-breast and MGB-lung for subtyping and TCGA-GBMIG for IDH1 mutation prediction. To establish baselines from the different methods, we trained the models using the AMBL progressively, we trained AMBL with the ResNet5024,25, CTransPath27 and UN28 patch encoders without any bias mitigation strategies.

As measured by 20-fold average AUC on the independent test cohorts, AMBL performed best, followed by CTransPath and paired with self-supervised patch encoders (Fig. 2a and Extended Data Figs. 1 and 2a,e); similar trends extend to IDH1 mutation prediction tasks22,24 and Extended Data Fig. 3a,d,e; however, when using a self-supervised patch encoder for IDH1 mutation prediction, we only observed a performance gap (in ROC AUC) between Black and white patients across all tasks (3.0% for breast subtyping, 10.9% for brain subtyping and 12.3% for IDH1 mutation prediction; Extended Data Figs. 1–3a). This gap was further supported by lower F1 scores, particularly for Black patients in lung subtyping and IDH1 mutation prediction (Fig. 2e,f), whereas the F1 score for white patients was lower in brain subtyping and IDH1 mutation prediction (Extended Data Figs. 1–3a). These results demonstrate that patch encoders were substantially reduced when we used self-supervised patch encoders trained on histology images, such as CTransPath and UNI. For instance, when using UNI, the AUC gap between white and Black patients increased from 0.5% in brain subtyping and to 12.3% for IDH1 mutation prediction (Fig. 2e,f), whereas it remained at 3.8% for breast subtyping (Fig. 2d). However, a closer examination of the high AUC values achieved with UN reveals an imbalance in the F1 score for race groups. Notably, the F1 scores for Black patients in the lung subtyping and IDH1 mutation prediction tasks remained notably lower than those

for white patients (Fig. 2e,f). The AUC and F1 score do not pinpoint the specific error types contributing to lower performance seen among Black patients. However, the performance of the classification models revealed that Black patients with LUAD and LUSC, along with Black patients with an IDH1 mutation, had notably poorer recall rates than the overall population, also evident from their negative TPR disparity values (Fig. 2c and Supplementary Data Tables 6 and 7). Moreover, in breast subtyping, in which AUC remained consistently high with CTransPath across Black, white and Asian patients, the TPR disparity revealed that Black patients with ILC and white patients with IDC underperformed the entire population (Extended Data Fig. 1 and Supplementary Data Table 6). In summary, our analysis highlights racial discrepancies in performance across subtyping and mutation prediction tasks.

### Bias from data characteristics

With our baseline indicating the existence of notable disparities between racial groups, we next investigated how much each encoder assessed whether existing approaches to mitigate variability and bias in the training and testing datasets help reduce the racial disparities. We explored approaches that are not directly race aware (that is, site-stratification and stain normalization) and an approach that is race aware (that is, test set resampling).

Impact of site stratification. The TCGA-BRCA and TCGA-lung cohorts comprise a digitalized collection of tissue samples from multiple hospital sites. Due to differences in tissue preparation protocols and patient demographics across sites, a 'dataset shift' issue inevitably arises, in which models developed and deployed on mismatched data distributions, a common failure mode of machine learning applications in healthcare22,24,25,28,29. Site-stratified CV is a bias mitigation strategy that holds out a subset of sites to prevent models from learning biases from the training data. For instance, when we used the test set whether site-specific demographic variability contributes to the performance disparity, we trained the AMBL model using a tenfold site-stratified CV and various patch encoders (Extended Data Figs. 1 and 2a,e). For the breast subtyping task, we observed robust performance, such as ResNet50, were found to exacerbate existing disparities in lung subtyping. Specifically, as measured by AUC, these splits led to a 5.2% drop for Asian patients, a 2.8% drop for Black patients and a 2.7% drop for white patients (Extended Data Fig. 2b, Corres. Fig. 2b). The F1 scores also decreased across races with the ResNet5024 encoder (Fig. 2e). Using site-stratified splits with self-supervised patch encoders such as UNI and CTransPath showed improvements in subtyping AUC (Extended Data Fig. 2b) and F1 scores (Extended Data Fig. 2f). For example, in breast subtyping, using site-stratified splits with the CTransPath encoder led to equalizing the AUC for white and Black patients (Extended Data Fig. 2b). Despite these improvements, the F1 score for Black patients remained lower than that for the overall population with the UNI encoder in lung subtyping (Fig. 2e). Recall for Black patients with ILC in breast subtyping (Supplementary Data Table 5) and for white patients with IDC in lung subtyping (Supplementary Data Table 6) was also lower. In summary, the effect of site stratification on performance is contingent on the patch encoder used. While it could exacerbate disparities with weaker encoders, it offered some improvement with stronger encoders. Nevertheless, we did not persist in lung subtyping, as measured by AUC, F1 score and TPR disparity. A similar investigation for IDH1 mutation prediction could not be performed as the EBRAINS brain tumor atlas does not provide information on the tissue source site.

Impact of stain normalization. In addition to site-stratified CV, stain normalization is a common stain-adaptation technique for reducing site-specifics in staining variability and is advocated in tandem with site-stratified CV16,24,25,28,29. We thus used stain normalization on both training

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1177

---

<!-- Page 5 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

a IDH1 mutation Lung subtyping Breast subtyping

WhiteBlackBlueOverall

Share-stratified AUC

UNICTransPathResNet50u

b IDH1 mutation

ResNet50uCTransPathUNI

1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W 1W

---

<!-- Page 6 -->

Article

https://doi.org/10.1038/s41591-024-02885-x

and testing cohorts, with the tenfold site-stratified CV, to investigate whether the disparities are reduced. The impact of stain normalization and performance metrics on the disparities between Black and white patients and the disease being investigated (Fig. 2d, f). Using ResNe500 and stain normalization in IDH1 mutation prediction led to increases in the race-stratified and overall AUC (Extended Data Fig. 3B). However, this improvement led to notable drops of 6.1% and 1.9% in Black patients' AUC for breast and lung subtyping, respectively (Extended Data Figs. 1 and 2c). Conversely, stain normalization with stronger encoders did not offer any substantial TPR disparity reduction and also led to performance gains in Black patients' AUC for breast and lung subtyping. The Path encoder, using stain normalization decreased Black patients' AUC by 2.5% and 3.0% in breast and lung subtyping, respectively, while not notably affecting white patients' performance. We note that, even with stain normalization, the performance of the Path encoder was lower than the overall population. For example, when using the UNI encoder, there was a mean TPR disparity of -0.060 (95% confidence interval (CI) -0.080 to -0.020) for IDH1 mutation prediction (Extended Data Table 6) and -0.284 (95% CI -0.482 -0.086) for Black patients with an IDH1 mutation (Supplementary Data Table 7). Demographic gaps also persisted when applying stain normalization without site stratification (Extended Data Fig. 3a) and across encoders (Extended Data Table 8). Overall, depending on the disease being studied, stain normalization may be beneficial when used with less robust patch encoders.

Impact of test set resampling. Lastly, we investigated whether a disproportionate demographic composition in the test cohorts causes performance disparity. To this end, we constructed unbiased test cohorts by resampling with replacement an equal number of patients from each racial group and each class within the test cohorts58. We evaluated the models on resampled test cohorts, with stain normalization and site stratification still in effect. Nonetheless, performance gaps persisted. For example, the ResNe500 encoder with stain normalization (Fig. 2d, f) and Extended Data Figs. 1, 2d, h, and 3c, f, in breast subtyping, a notable 9.2% AUC gap between Black and white patients was evident with the ResNe500 encoder (Fig. 2d). Although the gaps were reduced at 2.8% with the Path encoder (Fig. 2d), the overall TPR disparity persists among Asian and Black patients with ILIC indicating lingering disparities in breast subtyping (Fig. 2c and Supplementary Data Table 5). In lung subtyping, both ResNe500 and UNI showed lower performance in Black patients, with a 10.5% and 10.1% difference in population and white patients, supported by negative TPR disparities among Black patients (Fig. 2e and Supplementary Data Table 6). In the prediction of IDH1 mutations, substantial gaps persisted between Black and white patients, with a 10.5% and 10.1% difference in population and white patients with 14.0% lower than that for white patients, which is reflected in lower F1 scores for Black patients and negative TPR disparities among Black patients with IDH1 mutations (Supplementary Data Table 6). Overall, despite correcting for imbalances in sample size in independent test sets, performance disparities continued to persist.

In summary, performance disparities among different racial groups persist even when correcting for imbalances in sample size and dataset shifts. It is important to recognize that both the site stratification and stain normalization techniques have their pros and cons5. Site-stratified splits can aid in learning features that are specific to site-specific pathology. Stain normalization can enhance performance. However, they may also lead to performance declines, as the exclusion of certain sites could result in the exclusion or underrepresentation of specific demographic groups during training. Likewise, stain normalization can enhance performance but inadvertently remove staining distinctness that arise from the diverse underlying biology of individual patients with cancer. In general, we found that self-supervised patch encoders, such as UNI, tend to remain indifferent to site-specific artifacts and stain normalization, whereas weaker encoders remain more amenable to such techniques.

## Bias from MIL model architectures

The rapid progress in computational pathology has led to the improvement of MIL models for breast subtyping and IDH1 mutation prediction (Fig. 1b). We thus investigated the effect of different modeling choices for patch encoders (ResNe50059, CransPath60 and UNI61) and aggregators (ABMIL62, CLAM63 and TransMIL64) on the disparities between different racial groups for breast subtyping, lung subtyping and IDH1 mutation prediction. We additionally implemented commonly used fairness-aware strategies to study whether these are effective in mitigating demographic biases. Our choice of bias mitigation strategies was guided by the recent literature on fairness in learning from unbalanced DML model embeddings should differ based on protected attributes or remain agnostic to them65,66. Specifically, we used INV67, which emphasizes examples from underrepresented groups in the model's training, and PAV68, which aims to be agnostic to information predictive of protected attributes.

Among all the modeling choices we investigated, the use of a ResNe500 encoder with stain normalization and larger patches in the performance of breast and lung subtyping as well as IDH1 mutation prediction, irrespective of the patch aggregator and bias mitigation strategy used (Fig. 3b, d, f and Supplementary Data Table 9). In general, the use of ResNe500 and ResNe500 with stain in ABMIL, the F1 score for Black patients showed improvements of 2.4% in breast subtyping, 21.6% in lung subtyping and 10.3% in IDH1 mutation prediction (Supplementary Data Tables 9–11). Similarly, the use of CransPath and TransMIL in combination with AUC (Fig. 3b, d, f). Notably, any amount of pretraining on histology images rather than natural images helped improve race-stratified performance (Extended Data Fig. 5a–c). The performance of different patch aggregators exhibited task dependency. For instance, when using the ResNe500 encoder, more complex patch aggregators led to a reduction in overall performance in lung and breast subtyping (Fig. 3b, d). In general, the use of CransPath and TransMIL in predicting IDH1 mutation performance based patch aggregators such as TransMIL64 capture patch relations, whereas ABMIL62 assumes patch independence; such model inductive biases could interact differently with various tasks (Extended Data Fig. 5d).

We observed that IW had an adverse impact on race-stratified performance across different patch encoders and tasks, as evident from reductions in both the AUC (Fig. 3b, d) and F1 score (Supplementary Data Table 9). In general, the use of IW did not show an improvement in TPR disparities with IW, such as ABMIL with CransPath in lung subtyping, this improvement came at the expense of lowering the race-stratified performance (Supplementary Data Table 10). In contrast, the use of INV and PAV led to higher F1 scores for Black and white enhancements in race-stratified performance and reductions in TPR disparities. For instance, in breast subtyping, using CransPath with TransMIL and PAV resulted in high F1 scores for Black and white patients and minimal TPR disparities for Black patients (Fig. 3a, h and Supplementary Data Table 9). However, in lung subtyping, the gains with AR were limited, and the standard ABMIL with the UNI encoder and PAV resulted in a 1.0% improvement as an effective approach for reducing disparities while maintaining high performance (Fig. 3c, d and Supplementary Data Table 10).

Considering TPR disparity and AUC concurrently, we observed that the use of CransPath and TransMIL in combination with AUC for individual racial groups contributed to narrowing the performance gaps between them. This was evidenced by the TPR disparity for Black patients approaching zero with an increase in AUC (Fig. 3b, d, f). In lung subtyping, the mean AUC for Black patients improved from 0.795 (95% CI 0.771, 0.823) for ABMIL with the ResNe500 encoder to 0.954 (95% CI 0.941, 0.967) for ABMIL with CransPath and the F1 score improved from 0.69 (95% CI 0.61–0.77) and 0.62 (95% CI 0.52–0.70) to 0.97 (0.97, 0.99) for Black patients with LUC (Supplementary Data Table 10). However, in IDH1 mutation

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1179

---

<!-- Page 7 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Fig. 3 | Investigating bias from ML model architectures and bias mitigation strategies. a, Combination of patch aggregator (ABML, CLAM, TransML), bias mitigation strategies (no mitigation (No mit.), IW, AR) and patch encoders (ResNet50, CRansPath, UN) were evaluated for breast subtyping (a, b). Lung subtyping (c, d) and IDH1 mutation prediction (e, f). For each task, the TPR disparity for Black patients is visualized in a, c, d, e, whereas shifts in performance due to modeling choices are depicted using the mean race-stratified and overall ROC-AUC (n = 20 folds) in b, d, e, f. For performance from lung subtyping, ABML was trained on the TCGA BRCA (n = 1049 slides) and TCGA lung (n = 1043 slides) cohorts and tested on the respective resampled MGB

cohorts (n_{\text{train}} = n_{\text{train}} = n_{\text{train}} = 1,000, with 500 slides per subtype for each race). For IDH1 mutation prediction, ABML was trained on EBRAINS (n = 873 slides) and tested on the resampled TCGA-GIMMLGG cohort (n_{\text{train}} = n_{\text{train}} = n_{\text{train}} = 1,000, with 500 slides per class for each race). Error bars in bar plots indicate the 95% CI, whereas the center is the mean value (n = 20 folds). Boxes indicate quartile values of TPR disparity (for each fold), with the center being the 50th percentile. Whiskers extend to data points within 1.5 \times the interquartile range. Each task in the box plots represents a unique model trained for one of the folds. Demographic distributions for each task are available in Supplementary Data Tables 2–4.

prediction, increases in AUC for Black patients were not accompanied by large improvements in TPR disparity for Black patients with an IDH1 mutation (Fig. 3e and Supplementary Data Table 11). This suggests that, although more robust patch encoders were used for performance from Black patients in predicting IDH1 mutations, the performance gaps between Black patients and the overall population persist. Hence, concurrently considering fairness and performance metrics provides insights into whether performance gains reduce disparities between race groups.

While numerous sophisticated bias mitigation and patch aggregation methods have been proposed, our findings indicate that, when combined with weak patch encoders such as ResNet503c, these complex methods are not as effective in reducing disparities compared to simpler aggregators paired with strong self-supervised patch encoders. This underscores that, while patch aggregators and bias mitigation strategies have a valuable role, they may not be substituted for robust patch encoders. Instead, they can provide incremental performance enhancements, as evidenced by their successful application in breast

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1180

---

<!-- Page 8 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Fig. 4 | Evaluating race information in embeddings. All combinations of patch encoders (ResNe504, CTRanPath and UN), patch aggregators (ABM, CLAM and TransMIL) and bias mitigation strategies (W and AR) were trained for breast subtyping, lung subtyping and IDH1 mutation prediction using TCGA-BRCA (n = 1409 studies), TCGA-Lung (n = 1043 studies) and the EBRAINS brain tumor atlas (n = 873 studies) in 20 Monte Carlo folds and tested on resampled MGB-BMI. MGB-long and TCGA-MGB-GC, respectively (all resampled sets had n_{\text{train}} = n_{\text{val}} = n_{\text{test}} = 1,000, with 500 slides per class for each case). After freezing the patch aggregators in all trained models, the logistic regression model

was trained to use the slide-level embedding to predict race on the respective resampled test cohorts in fivefold CV studies. a, Overall TALK AUC (n = 20 folds) versus race prediction AUC (n = 5) plotted for breast subtyping (a), lung subtyping (b) and IDH1 mutation prediction (c). Each point corresponds to a combination of patch encoder, patch aggregator and bias mitigation strategy. p is the Spearman correlation coefficient associated with the trend line shown in dashed red and is presented with 95% CI. The error bars indicate the 95% CI, with the center as the mean value. Demographic distributions for each task are available in Supplementary Data Tables 2–4.

subtyping with the CTRanPath encoder and AR. Nevertheless, we note that, even with the UN encoder and ABMIL without bias mitigation strategy, disparities of 4.4% and 9.4% in the F1 score persisted between white and Black patients in lung subtyping and IDH1 mutation prediction, respectively (Supplementary Data Tables 10 and 11). The same observation held true even when performance was assessed by race-stratified AUC (Fig. 3d, j) and TPR disparity (Supplementary Data Tables 10 and 11). Indicating that more work is needed in mitigating demographic disparities in computational pathology.

### Race prediction from pretrained MIL models

We further investigated whether the patients' race can be predicted from the slide-level representation of the models used in subtyping and mutation prediction. Previous works have demonstrated that histology carries information about race in TCGA due to correlations of hematoxylin and eosin stain intensity with hospital site and race. Demographic information10 however is not used for whether slide embeddings used for clinical tasks can also be used for race prediction. We trained models for all possible combinations of patch encoders, patch aggregators and bias mitigation strategies on the TCGA-BRCA, TCGA-lung subtyping and EBRAINS IDH1 mutation prediction tasks; froze the patch aggregators; and used logistic regression to predict race on the task-associated independent test cohort. We found that slide-level representation used for the subtyping and mutation prediction tasks were highly predictive of race and that the race prediction performance was positively correlated with the task performance on the test cohorts (Fig. 4a–c). This is in line with the observation that race predictive information from deep medical imaging modalities20,21. We found that slide representations learned with stronger patch encoders were able to predict race better. For example, in IDH1 mutation prediction, ABMIL with the ResNe504 patch encoder had a mean race prediction AUC of 0.590 (CI 0.539, 0.619), whereas the same patch aggregator with UN features had a mean race prediction AUC of 0.852 (95% CI 0.839, 0.865) (Supplementary Data Table 44). Additionally, we found that models trained with AR, which intends to remove race predictive information from deep embeddings, had a high race prediction AUC. For example, ABMIL

trained with AR on lung subtyping with UN features had a mean race prediction AUC of 0.787 (95% CI 0.773, 0.795), which is comparable to the race prediction AUC with no mitigation strategy (0.784 (95% CI 0.773, 0.794)) (Supplementary Data Table 43). Overall, models showing high performance may be able to more precisely attribute information and popular bias mitigation strategies may not successfully overcome this. We want to emphasize that encoding protected attribute information should not be misconstrued as the information being used for downstream tasks. Our analysis demonstrates that the primary task and the protected attribute information may be related, but it does not establish a causal relation22.

### Bias from training data type, diversity and size

In computational pathology, it is common to train on the multisite TCGA data and test on data from independent institutions10,23. To understand demographic disparities better, we also tried the inverse approach; that is, we trained models on data from breast and lung cancer subtyping and then tested them on TCGA cohorts. We additionally examined the effects of training set diversity and size on performance disparity. We trained models on data from subtyping (mainly, 5 samples per subtyping, referred to as k = 10) and 25 samples per subtyping (referred to as k = 50) and by racial composition (white only, Asian and Black only, and a combination of all races). This approach was also applied reciprocally, with training on TCGA and testing on MGB. For each dataset size and composition, sampling was done ten times to create ten training folds (except for the ‘k = all’ category, in which 20 Monte Carlo folds were used). The UN patch encoder and ABMIL aggregator were used exclusively with training on TCGA and testing on training data, which may lead to data leakage. A similar investigation for IDH1 mutation prediction could not be performed as the EBRAINS brain tumor atlas does not provide patient race information.

Training on MGB and testing on TCGA. Training on the MGB-breast and MGB-lung cohorts and testing on the corresponding TCGA cohorts reveal that, although the ABMIL models discriminate between types of breast and lung carcinomas with high efficiency for both white and Black patients, aligning with prior findings24, the performance

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1181

---

<!-- Page 9 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Fig. 5 | Effect of training set diversity and size on disparities. ABML models with the UN1 patch encoder were trained using different compositions of the training set: white patients only, Asian and Black patients only, and a combination of all racial groups. For each type of composition, the training set's size was increased from 5 samples per subtype (k=10) to 25 samples per subtype (k=50) to training on all patients pertaining to that composition type (k=50) with sampling done ten times to create ten folds. For k=10, 20 Monte Carlo splits were used and actual training dataset size is mentioned. a, c, Race-stratified and macro-averaged overall ROC-AUC (n=10) folds per race for breast subtyping, with training sets derived from MGB-breast and testing done on resampled TCGA-BRCA (a); lung subtyping, with training sets derived from MGB-lung and

testing done on resampled TCGA-lung (b); breast subtyping, with training sets derived from TCGA-BRCA and testing done on resampled MGB-breast (c); and lung subtyping, with training sets derived from TCGA-lung and testing done on resampled MGB-lung (d). All resampled test sets had n_{\text{train}} = n_{\text{test}} = 1,000, with 500 splits per subtype for each race. Boxes indicate quartile values of TPR, disparity is 10 folds for k=10 and k=50 and n=20 folds for k=10, with the center being the 50th percentile. Whiskers extend to data points within 1.5 \times the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. Demographic distributions for each task are available in Supplementary Data Tables 2 and 3.

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1182

---

<!-- Page 10 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Fig. 6 | Investigating lung subsuppling disparities beyond race. TPR disparity was assessed using various demographic subgroups of the MGB-lung test cohort (n = 1,940 slides) for an ABML model trained with UN features on the TCGA lung cohort (n = 1,043 slides) in a 2D-fold study for lung subsuppling. a, TPR disparity for different income groups. b–d, TPR disparity computed for subgroups of LUAD and LUSC patients from low-income postal codes (n = 413 slides), stratified by other demographic variables: racial groups (b), insurance groups (c) and age groups (d). e, TPR disparity for different racial groups. f–h, TPR disparity computed for subgroups of white patients with LUAD and LUSC (n = 1,630 slides), stratified by other demographic variables: insurance groups (f), income groups

inferred from postal code (g) and age groups (h). i–k, TPR disparity computed for subgroups of Black patients with LUAD and LUSC (n = 128 slides), stratified by other demographic variables: insurance groups (i), income groups inferred from postal code (j) and age groups (k). Boxes indicate quartile values of TPR disparity (n = 20 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5 times the interquartile range. Each dot in the plots represents an individual model trained for one of the folds. Preset P values are from a nonparametric two-sided paired permutation test after multiple-hypothesis correction. Demographic distributions for each task are available in Supplementary Data Table 3.

measured by AUC was notably lower for Asian patients. For instance, in lung subsuppling done with all patients from racial races, the mean AUC for TCGA white patients was 0.956 (95% CI 0.945, 0.967) compared to 0.889 (95% CI 0.874, 0.905) for Asian patients (Fig. 5a). Furthermore, in examining recall for each subtype, Asian patients demonstrated lower recall for the ILC subtype in breast subsuppling and the LUSC subtype in lung subsuppling than white patients, corroborated by race-stratified F1 scores and TPR disparities per subtype (Supplementary Data Tables 13 and 15). Despite similar subsuppling AUCs for Asian patients and non-white patients in TCGA lung and TCGA BRCA, this uniformity did not extend to other TCGA cohorts. For instance, Black patients exhibited a lower AUC compared to white patients in the TCGA GBM/CGG cohort for BDH1 and TPH2 prediction, while subsuppling AUCs for Asian patients were all comparable to that for white patients (Fig. 27). Internal TCGA and MGB cohorts also showed demographic disparities (Extended Data Fig. 6 and Supplementary Data Tables 31–34). These results indicate that demographic disparities in computational pathology extend beyond MGB cohorts.

Effect of training dataset size. When expanding the training cohort size from n = 10,000 slides to 100,000 slides, we observed a 0.004 increase in cohort and testing on TCGA data, we observed substantial enhancements in race-stratified AUCs across all racial groups for both subsuppling tasks (Fig. 5b). These improvements in race were consistently mirrored by similar enhancements in race-stratified F1 scores and reductions in TPR disparities (Supplementary Data Tables 13 and 15).

Conversely, models trained on larger TCGA cohorts containing all races and tested on MGB cohorts also exhibited improved race-stratified performance (Fig. 5c,d). Notably, training with smaller cohorts resulted in demographic disparities within the AUC values. For instance, in lung subsuppling trained on TCGA and tested on MGB with k = 10 patients from all races, white patients initially had a mean AUC of 0.840 (95% CI 0.831, 0.850), while Black patients had a lower mean AUC of 0.740 (95% CI 0.724, 0.757). However, after training on all available patients, the AUCs were improved to 0.890 (95% CI 0.890) for white patients and 0.954 (95% CI 0.941, 0.967) for Black patients (Fig. 5d). Similarly, in breast subsuppling, the mean AUC for Black patients improved from 0.636 (95% CI 0.619, 0.653) to 0.944 (95% CI 0.933, 0.944) when training size was increased from 10 patients to 100,000 patients. Similarly, in lung subsuppling, we find F1 scores and reductions in TPR disparities (Supplementary Data Tables 12 and 14). Thus, our findings suggest that training on large datasets is vital for disparity mitigation.

Effect of demographic group diversity in training datasets. Expanding the demographic diversity in large public consortia, typically used as training datasets, results in enhanced race-specific model performance (Extended Data Fig. 6). For example, in breast subsuppling with k = 50, ABML trained on the TCGA dataset that combines white, Asian and Black patients had an improved mean Black AUC of 0.888 (95% CI 0.879, 0.905) compared to 0.850 (95% CI 0.831, 0.869) achieved when training only on white patients (Fig. 5c). These gains are corroborated by similar increases in the F1 score for Black patients in

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1183

---

<!-- Page 11 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

breast subtyping with k = 50 on models trained only on white patients in a similar configuration (Supplementary Data Table 12). Similarly, in a model combining white and black patients, we found that the model combines white, Asian and Black patients saw a higher mean AUC for Black patients (Fig. 5). These improvements in performance also led to reductions in TPR disparity. For example, in breast subtyping with k = 50, ABMIL trained on TCGA white patients had a mean TPR disparity of -0.092 (95% CI -0.124, -0.068) for Black patients with ILC, which decreased to -0.059 (95% CI -0.084, -0.039) when ABMIL was trained on patients from all races (Supplementary Data Table 12). In a model trained in TCGA black patients, we found that the model with k = 50, specifically for Black patients with LUSC (Supplementary Data Table 14). When training for breast and lung subtyping on MGB and testing on TCGA, we observed that the AUC and F1 score improved with more diverse patients (Supplementary Data Table 15). This was compared to training on only white or Asian and Black patients (Fig. 5a,b and Supplementary Data Tables 13 and 15). These enhancements in performance for subtyping were observed for all cancer types in patients with IDC and LUAD in breast and lung subtyping, respectively. Overall, we found that demographic disparities in subtyping exist when training on MGB and testing on TCGA. Further investigations into model performance (TCGA vs. MGB) referred to as income for simplicity and diverse training sets can help alleviate disparities, and efforts should be made to collect and curate demographically diverse public consortia.

### Investigating disparities beyond race

For lung and breast subtyping, we investigated whether computational pathology models perform equally well for subgroups defined by other demographic variables, such as insurance type, postal code or inferred middle socioeconomic income (referred to as income for simplicity) and age groups (refer to 'Forming demographic subgroups' in Methods for further details). In addition, we analyzed disparities within a subgroup by stratifying the cohort by insurance type from other demographic factors, referred to as 'intersectional analysis' (refs. 47,77). Notably, the ABMIL model with UNIf features on 20 MGB Carlo folds and the original test sets were used for this analysis. For IDH1 mutation prediction, such investigations were not performed.

We observed that discrepant performance extends beyond racial subgroups, primarily for postal code income groups in lung subtyping (Supplementary Data Table 21), insurance groups in both lung and breast subtyping (Supplementary Data Table 22), and insurance groups in IDH1 mutation prediction (Supplementary Data Table 27). For example, in lung subtyping on MGB-lung, we found patients from middle- and high-income postal codes to have higher F1 scores than patients from low-income postal codes. In breast subtyping, 2.4% and 2.1% lower than that of patients from middle-income and high-income postal codes, respectively, were observed. Many Data Tables (Supplementary Data Tables 21–27) were also referenced by TPR disparities. Using the F1 score as a measure of performance, we consistently found breast and lung subtyping that patients without Medicare (American federal health insurance program) had higher performance than patients with Medicare, indicating higher misdiagnosis rates (Supplementary Data Tables 22 and 23). In the IDH1 mutation prediction task, we found that patients in the \geq 40 and \leq 60 years age group had higher performance than patients in the middle age group (Supplementary Data Table 27). Overall, we found that demographic disparities in AI models may extend beyond self-reported race, which echoes the findings of numerous previous studies30–32. We also found that performance was lower for minority racial groups in patients in demographic subgroups, even after adjusting for confounding factors such as age. For example, in lung subtyping, when considering patients within the same age group of \geq 70 years, we found that Black patients had worse performance than the overall population (Supplementary Data Table 25). In breast subtyping, we consistently

found white patients to have worse performance in the \leq 62 years age category (Supplementary Data Table 24). In IDH1 mutation prediction, we found that white patients had worse performance than other racial groups \geq 40 and \leq 60 years age groups (Supplementary Data Table 27). A similar analysis can be done for other demographic factors, such as postal code-inferred income. When lung cancer patients from low-income postal codes were stratified by race, we found that Black patients from this subgroup had lower recall for the LUAD subtype than white patients from the same subgroup (Fig. 6b and Supplementary Data Table 21). Differences by insurance type (Fig. 6c) and age (Fig. 6d) were also found for the same patients. These findings are consistent with our previous results29 revealed that aggregating diverse individuals within coarse race groups can mask disparities30,31. For example, when white lung cancer patients (Fig. 6c) are stratified by postal code-inferred income (Fig. 6e) and age (Fig. 6f), we found that disparities in performance are more significant for differences in age when stratifying by insurance type (Fig. 6f). For example, in IDH1 mutation prediction, when white patients from the same postal code were stratified by age, those patients with a worse performance (Extended Data Fig. 7b and Supplementary Data Table 26). This is in contrast to white patients overall having consistently high performance. Such intersectional analysis is not limited to the same racial groups. For example, we found that within Black and insurance, age and postal code income (Fig. 6i–k and Supplementary Data Table 19), which also extended to breast subtyping (Extended Data Fig. 8i–k and Supplementary Data Table 18).

### Analysis of misclassified cases

To understand better the failure modes of one of the models, a board-certified pathologist analyzed misclassified cases. For this, we chose the lung subtyping task trained on TCGA and tested on MGB because (1) large racial disparities in lung subtyping were seen despite using the best data processing and modeling choices, and (2) the morphological features of lung cancer are well understood and well established. The pathologist examined the pathology reports and WSIs used in the study for cases that were misclassified on at least two or more folds for ABMIL with the UNEncoder trained on the TCGA-lung cohort. We found that 10% of the misclassified MGB-lung cases on each slide, the pathologist determined whether the histology on the slide matched that in the corresponding pathology report, what the reported grade of the case was, whether the case was a biopsy or resection, and whether the case was from a primary (nonmetastatic) or secondary (HIC) or special stains were used to make the diagnosis (for example, thyroid transcription factor 1 HIC or microminimae staining to make a diagnosis of LUAD but not HIC for programmed death ligand 1 or programmed death ligand 2 HIC). The morphological features on the slide matched that in the pathology report – no misdiagnoses by the original pathologists were found in the subsequent review. In addition, we found that the cases were not a priori different from each other, as the grade was provided in the report, there was morphological overlap with the other class (for example, solid architectural LUAD), the samples were biopsy specimens (thus had limited tissue area) or resection specimens (thus had more tissue area). The diagnosis of LUAD in these cases were also difficult for the pathologists who originally signed out the cases, corroborating the difficulty for the model. Among these misclassified cases, those from white patients tended to be misclassified more than Black patients (did cases from Black or Black patients (68.4% for white patients versus 50.0% and 42.4% for Asian and Black patients, respectively), although they were less often biopsy specimens (56.5% for white patients versus 63.2% and 72.7% for Asian and Black patients, respectively) (Supplementary Data Table 28). Moreover, within the misclassified cases, Asian and Black patients tended to be younger than white patients. Therefore, the decreased performance on cases from Asian and Black patients in this experiment could be due to the smaller tissue area (and, thus, fewer patches that may be informative for the diagnosis) available to the model, as

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1184

---

<!-- Page 12 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

opposed to differences in grade or morphology, at least as evidenced by similar proportions of cases across grades and lower proportions of patients undergoing radical prostatectomy in the low- and intermediate-grade (resection or biopsy), biopsy specimens generally had lower performance in both subtyping tasks (Supplementary Data Tables 29 and 30). A similar analysis of misclassification of TCGA lung subtyping using ASMIL and the UN encoder also revealed that these cases were usually poorly differentiated; however, they were mainly resection cases and the patient reports did not often describe HCT testing (Supplementary Data Table 28). While such analysis poses one potential limitation, the observations are consistent with the findings reported in IDH1 mutation prediction suggesting that the root causes of these differences are not fully understood and warrant further investigation.

## Discussion

In this study, we assessed the performance of state-of-the-art computational pathology approaches across different demographic subpopulations, including men and women, and across different subtypes of subtypes of breast and lung carcinomas and for predicting IDH1 mutations in gliomas. We observed variations in the performance of current computational pathology methods among different demographic subgroups, even after accounting for statistical differences and using site-specific CV techniques10,12. Notably, these demographic disparities became more pronounced when we used weaker patch encoders, but they were reduced when self-supervised patch encoders were used. Additionally, we found that models trained on data used with self-supervised encoders, effectively mitigating disparities in breast subtyping. Hence, more robust patch encoders offer a promising avenue for mitigating disparities. However, the persistent gaps in lung subtyping and IDH1 mutation prediction, despite the use of state-of-the-art modeling choices, indicate that the issue of demographic disparities remains unresolved10. We additionally observed that mitigating the disparities through the use of a larger training dataset, rather than oversampling from underrepresented groups during training, such as through IW, can help reduce demographic disparities. This underscores the necessity for large and diverse datasets rather than smaller ones to mitigate demographic disparities to address biases. Our findings also indicate that models with higher performance on the test cohort often encode more protected attribute information. This occurred despite the use of AR, a technique known to be relatively robust to demographic biases in patch embeddings. Finally, we also show that demographic gaps can extend beyond racial categories to include variations by postal code income, age and insurance status. Our study, along with a previous work10, demonstrates that conversational AI can mitigate demographic disparities and can exhibit demographic biases on common diagnostic tasks in breast and lung carcinomas and gliomas.

Our findings that our model underperforms the importance of considering fairness and performance simultaneously when assessing algorithms for clinical deployment to avoid prioritizing one over the other, as improving performance at the cost of fairness, or vice versa, raises concerns for clinical use. In a recent study, we found that self-supervised patch encoders improved fairness and performance in subtyping, but we found that IW often reduced TPR disparity in subtyping tasks, but the cost of performance. Similar degradation of performance with the use of algorithmic fairness methods has been noted in other studies of conversational AI13,14. While self-supervised patch encoders increased fairness and performance in subtyping, we found that in predicting IDH1 mutations, increases in overall performance did not lead to large reductions in gaps between white and Black patients. Instead, we observed that the model trained on a larger dataset that might be difficult to identify solely based on overall population performance, which poses a risk of exacerbating existing inequalities in healthcare. Thus, simultaneously measuring bias and performance must become standard practice for medical imaging AI algorithms deployed in clinical settings.

Our finding that AR, the active removal of features predictive of protected attributes, can affect performance in different ways for different tasks, highlights the need to investigate the trade-offs between groups and phenotypic traits15,16. Recently, there has been mounting evidence in population genetics and cancer genomics that genetic ancestry is an important biological determinant in cancer health disparities, which may also manifest as demographic-specific histological phenotypes due to the correlations between ancestry and race16,17. For instance, in breast and lung cancers, innate immune variants and gene mutation frequencies are known to differ across people of European, African, and South Asian descent, which is in contrast to the view in fairness literature, which proposes learning invariant representations to protected attributes such as race18. While our findings suggest that AR combined with self-supervised encoders might reduce disparities, we do not have a clear understanding of which techniques might preclude learning population-specific histological phenotypes in the cancer types we investigated. Nonetheless, further research is required to understand the trade-offs between fairness and diversity.

As the identification and mitigation of bias are known to be difficult, our study has a few limitations. In IDH1 mutation prediction, the EBRAINS brain tumor atlas does not provide site or patient race information, and thus we could not investigate the position of race and ethnicity and its contributions to disparities. Our external test datasets for breast and lung subtyping contain relatively few images, are derived from a single hospital system and mainly include insured patients. Moreover, the test datasets were not specifically collected in the United States and Europe, often excluding geographic regions such as Asia and Africa. Although the slide diagnosis labels in our external test cohort were reviewed by several pathologists, inconsistencies in self-reported race can introduce label noise. Moreover, coarse race groups, such as ‘white’ or ‘African American’, might mask variations within demographic groups19, which can be heterogeneous20. Demographic labels can be influenced by social factors such as age, sex, occupation, education status and levels of cultural assimilation21. Mitigating such label noise remains challenging as traditional strategies of bias mitigation may not provide effective corrections, leading to inherent biases embedded in the data. Finally, the use of a single racial category in our validation set to eliminate label noise remains an ongoing challenge22. Our findings may have implications across multiple healthcare fields, including radiology, dermatology and genome-wide association studies23,24. However, the use of a single racial category in classification problems in this study, caution should be taken when attempting to generalize our findings to other machine learning tasks such as regression25, ranking26 and generative models27.

Our findings that conversational AI has largely been approached using out-of-domain natural image pretrained patch encoders28,29, upgrading to in-domain, histopathology encoders developed using self-supervised patch encoders is a promising direction for improving the performance of pathological AI algorithms. However, although we observed self-supervised pretrained encoders to have a large impact on mitigating disparities, we refrain from suggesting that they are the only solution. We found that self-supervised patch encoders improved encoders on extensive histology data continues to be a rapidly developing area, such models have limited public availability, primarily due to the proprietary patient data used during training. Hence, we recommend that the community invest in a large-scale dataset. Transformer architectures trained on histology images, as these are commonly used and available in the field of computational pathology. We encourage future studies to investigate how convolutional architectures trained on histology images can be trained on histology data affect disparities. Furthermore, the foundation models considered are trained on extensive data from various disease types, as large-scale single-disease data are often limited. Future work should explore the effects of pretraining on large-scale data from a single disease, as opposed to diverse cancer types, on disparities. Finally, as

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1185

---

<!-- Page 13 -->

Article

https://doi.org/10.1038/s41591-024-02885-x

more histology data are collected and organized, the training scale of foundation models considered here will inevitably be eclipsed12,137,138. Furthermore, our focus on the task of predicting disease state, demographic composition (which is often unavailable) and training strategies on disparities in healthcare.

Although our analysis used a variety of performance and fairness metrics to establish disparities, it is important to acknowledge the limitations of using TPR disparity. TPR can be influenced by population and prevalence biases139, and dataset resampling has been suggested to address these issues140,141. Our findings revealed that TPR disparities persist even after performing resampling. For the research study, corroborated by other performance metrics. However, it is essential to recognize that resampling provides only an approximation of ideal data. We performed resampling using patient race, which may not represent other covariates which are relevant for the research study. We explore how a causal understanding of data generation processes and clinical covariates can inform resampling to yield more realistic yet representative dataset. Furthermore, which race for the research study selection has been proposed to reduce TPR differences142,143, especially when dealing with prevalence shifts. However, this technique has notable drawbacks. It requires an intersection between ROC curves between demographic variables, which are not always available, particularly with an increasing number of demographic groups. Furthermore, race is a social construct, and there can be noise in self-reported race and other demographic variables, making it difficult to be between demographic groups. Furthermore, non-biological factors such as race to define clinical thresholds may lead to disparities in healthcare settings12,144–147. With respect to clinical deployment, implementing group-specific thresholds necessitates knowing demographic variables, such as race, for the research study deployment, which may not always be possible. Finally, selecting fairness metrics and definitions is crucial because simultaneously fulfilling them cannot be possible in all cases. For the research study. Nevertheless, we believe that striving for an equally high TPR across groups is essential to ensure that DL-based solutions maintain high clinical sensitivity across all subgroups.

While our study focuses on the performance of AI models across different demographic groups, the exact role of self-reported race as a potential causal factor for these variations is far from definitive. Current research indicates that medical outcomes can be influenced by social factors, such as race, ethnicity, and healthcare access138,148, which have complex interplays with race and other demographic variables such as education level and sex. The independent test cohorts used in our investigation encompass a broad spectrum of demographic variables, including race, ethnicity, income, and race. Performance disparities in such a diverse setting suggest that a complex combination of both social and biological factors, including but not limited to self-reported race, may contribute to the observed differences in model performance. While our intersectional analysis aims to decipher bias from different demographic factors, we currently consider broad demographic groups to ensure sufficiently large sample sizes. However, it is important to note that race may not account for other factors, such as sex. Future research on larger patient cohorts should explore intersectional groups involving multiple specific demographic factors simultaneously. Finally, while our study shows that self-reported race is one factor, such as age, subtyping and ADH1 mutation prediction for Black patients, we caution against generalizing this finding as indicative of a universal trend for a particular group because one must recognize the substantial biological heterogeneity inherent in human populations149,150. While we do not claim that computational pathology systems consistently underperform in any single demographic group, we highlight the existence of notable demographic variances across numerous datasets. Such differences warrant careful reclassification before clinical application to ensure equitable healthcare outcomes.

Recent investigations into demographic disparities within algorithms used in healthcare are more than theoretical inquiries; they carry profound implications for the equitable access and delivery of healthcare equity and quality across all populations151,152,153,154. However, algorithms are currently approved without necessitating the provision of test cohort demographics or the explicit reporting of their performance across different demographic groups (Supplementary Data Table 1). In upcoming years, frameworks for auditing AI algorithms will likely have an important role in clinical deployment155,156. This study, with support from an extensive body of literature157–160, underscores that algorithms do not perform equally well across different demographic categories. If left unchecked, such failure modes may amplify existing healthcare inequities161,162. We encourage medical regulatory agencies to consider these findings and make reporting of demographic stratification a standard practice when evaluating models for clinical deployment and public use. This aligns with reporting guidelines such as CONSORT AI (Consolidated Standards of Reporting for Trials for AI Interventions)163 and STARD AI (specific version) of the Standards for Reporting of Diagnostic Accuracy Studies checklist164, which advocate for transparent reporting of AI performance assessments. Such measures can increase the trust in medical algorithms and their use in clinical practice. Finally, by clinical standards, we hope that our study serves as an entry point for investigations into the complex entanglements between demographic factors, DL and the clinical practice of pathology and for the implementation of policies that enable stakeholders to ensure that AI algorithms are developed to be safe and effective for patients across diverse demographic backgrounds.

## Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, figures, tables or other available content, including details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41591-024-02885-x.

## References

1. Song, A. H. et al. Artificial intelligence for digital and computational pathology.Nat. Rev. Bioeng.1, 930–949 (2023).
2. van der Laak, J., Litjens, G. & Ciampi, F. Deep learning in histopathology: the path to the clinic.Nat. Med.27, 775–784 (2021).
3. Coudray, N. et al. Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning.Nat. Commun.10, 1150 (2019).
4. Lu, M. Y. et al. Data-efficient and weakly supervised computational pathology on whole-slide images.Nat. Biomed. Eng.5, 555–570 (2021).
5. Soudke, O.-J. et al. Deep learning for prediction of colorectal cancer outcome: a discovery and validation study.Lancet395, 350–360 (2020).
6. Chen, R. J. et al. Deep learning-based classification of mesothelioma improves prediction of patient outcome.Nat. Med.25, 1519–1525 (2019).
7. Chen, R. J. et al. Pan-cancer integrative histology—genomic analysis of 1,000,000 cases.Nat. Commun.10, 865–878 (2019).
8. Kather, J. N. et al. Pan-cancer image-based detection of clinically actionable genetic alterations.Nat. Cancer.7, 789–799 (2020).
9. Fu, Y. et al. Pan-cancer computational histopathology reveals novel genomic and epigenetic composition and prognosis.Nat. Cancer.8, 800–810 (2020).
10. Chen, R. J. et al. Scaling vision transformers to gigapixel images via hierarchical self-supervised learning. InProc. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition16144–16155 (IEEE, 2022).

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1186

---

<!-- Page 14 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

1. 11. Shao, Z. et al. TransMIL: transformer-based correlated multiple instance learning for whole slide image classification. InAdvances in Medical Informatics and Computing SystemsVol. 34 (eds. Ranazzo, M. et al.) 2136–2147 (Curran Associates, 2021).
2. 12. Chan, T. H., Cendra, F. J., Ma, L. Y., Gin & Yu, L. H. Histopathology whole slide image analysis with heterogeneous graph representation learning. InProc. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition15661–15670 (IEEE, 2023).
3. 13. Kathir, J. N. et al. Deep learning can predict microsatellite status: instability directly from histology in gastrointestinal cancer.Nat. Med.10, 1054–1058 (2004).
4. 14. Leo, P. et al. Computer extracted gland features from H&E predicts prostate cancer recurrence comparably to a genomic companion diagnostic test: a large multi-site study.NPI Precis. Oncol.5, 35 (2020).
5. 15. Howard, F. M. et al. The impact of site-specific digital histology signatures on deep learning model accuracy and bias.Nat. Commun.12, 4423 (2021).
6. 16. Chatterji, S. et al. Prediction models for hormone receptor status in female breast cancer do not extend to males: further evidence of sex-based disparity in breast cancer.NPI Breast Cancer9, 91 (2023).
7. 17. Dehkharghani, T. et al. Biased data, biased AI: deep networks predict the acquisition site of TCGA images.Diagn. Pathol.18, 67 (2023).
8. 18. Obermayer, Z., Powers, B., Vogeli, C. & Mullainathan, S. Dissecting racial bias in an algorithm used to manage the health of populations.Science366, 447–453 (2019).
9. 19. Mhasawade, V., Zhao, Y. & Chunara, R. Machine learning and algorithmic fairness in public and population health.Nat. Mach. Intell.3, 656–669 (2021).
10. 20. Gichoya, J. W. et al. AI recognition of patient race in medical imaging: a modelling study.Lancet Digit. Health4, e406–e414 (2022).
11. 21. Pierson, E., Cutler, D. M., Leskovec, J., Mullainathan, S. & Obermayer, Z. An algorithmic approach to reducing unexplained disparities in underserved populations.Nat. Med.27, 136–140 (2021).
12. 22. Population Estimates, July 1, 2022 (2022). U.S. Census BureauQuickFactshttps://www.census.gov/quickfacts/table/US/PS12022222(2022).
13. 23. Landry, G. L., Ali, N., Williams, D. R., Rehm, H. L. & Bonham, V. L. Lack of diversity in genomic databases is a barrier to translating precision medicine research into practice.Health Aff. (Millwood)39, 765–768 (2020).
14. 24. Liu, J. J. et al. An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics.Cell173, 400–416 (2018).
15. 25. Spratt, D. E. et al. Racial/ethnic disparities in genomic sequencing.JAMA Oncol.2, 1703–1704 (2016).
16. 26. Khos, S. et al. Racial and ethnic bias in risk prediction models for colorectal cancer: a systematic review.Sci. Rep.12, 10605 are omitted as predictors.JAMA New Open6, e2318495 (2023).
17. 27. van der Burgh, A. C., Hoorn, E. J. & Chaker, L. Removing race from kidney function estimates.JAMA325, 2018 (2021).
18. 28. Duan, E. et al. Clinical implications of removing race from estimates of kidney function.JAMA325, 184–186 (2021).
19. 29. Marmot, M. Social determinants of health inequalities.Lancet396, 1089–1104 (2021).
20. 30. Dietz, E. C., Sitrung, M., Miranda-Carboni, G., O'Reagan, R. & Seewald, V. L. Triple-negative breast cancer in African-American women: disparities versus biology.Nat. Rev. Cancer15, 248–254 (2015).
21. 31. Corner, J. N. et al. Ethnic differences among patients with cutaneous melanoma.Arch. Intern. Med.166, 1907–1914 (2005).
22. 32. Rubin, J. B. The spectrum of sex differences in cancer.Trends Cancer3, 303–315 (2022).
23. 33. Gusap, A. et al. Male breast cancer: clinical and molecular analysis of racial disparities.Cancer126, 800–807 (2020).
24. 34. Heath, E. I. et al. Racial disparities in the molecular landscape of cancer.Anticancer Res.38, 2235–2240 (2018).
25. 35. Gusap, A. et al. Male breast cancer: a disease distinct from female breast cancer.Breast Cancer Res. Treat.173, 37–48 (2019).
26. 36. Dong, M. et al. Sex differences in cancer incidence and survival: a pan-cancer analysis.Cancer Epidemiol. Biomarkers Prev.29, 1195–1207 (2020).
27. 37. Butler, E. N., Kelly, S. P., Coupland, V. H., Rosenberg, P. S. & Cook, M. B. Fatal prostate cancer incidence trends in the United States and England by race, stage, and treatment.Br. J. Cancer123, 123–130 (2020).
28. 38. Zavalie, V. A. et al. Cancer health disparities in racial/ethnic minorities in the United States.Br. J. Cancer124, 315–332 (2021).
29. 39. Ngan, H.-L., Wang, L.-K., Lo, W. & Lui, V. Y. W. Genomic landscapes of EBV-associated nasopharyngeal carcinomas vs. HPV-associated head and neck cancer.Cancers (Basel)10, 210 (2018).
30. 40. Harty, S., Athey, T., Sauer, R. & Chunara, R. A. Fairness violations and mitigation under covariate shift. InProc. 2021 ACM Conference on Fairness, Accountability, and Transparency3–13 (Association for Computing Machinery, 2021).
31. 41. Harty, S., Athey, T., Sauer, R. & Sun, Y. Does enforcing fairness mitigate biases caused by subpopulation shift? InAdvances in Neural Information Processing SystemsVol. 34 (eds. Ranzato, M. et al.) 25773–25784 (Curran Associates, 2021).
32. 42. Giguer, S. et al. Fairness guarantees under demographic shift. InProc. 10th International Conference on Learning Representations(ICLR, 2022).
33. 43. Schroot, J. et al. Diagnosing failures of fairness transfer across demographic shift in real-world medical settings. InAdvances in Neural Information Processing SystemsVol. 35 (eds. Koyejo, S. et al.) 19304–19318 (Curran Associates, 2022).
34. 44. Harty, S. et al. Mitigating fairness-based pathologies may could act as a novel prognostic marker for patients with clear cell renal cell carcinoma.Br. J. Cancer126, 771–777 (2022).
35. 45. US Food and Drug Administration. Evaluation of automatic classification for fair use of race.https://www.accessdata.fda.gov/cdri_docs/reviews/DEN20080.pdf(2021).
36. 46. Seyyed-Kalantari, L., Liu, G., McDermott, M., Chen, L. Y. & Ghassami, M. HeXChou: fairness gaps in deep chest X-ray diagnosis.Proc. Natl. Acad. Sci. U.S.A.119, 232–243 (2022).
37. 47. Seyyed-Kalantari, L., Zhang, H., McDermott, M., Chen, L. Y. & Ghassami, M. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiography in under-served patient populations.Nat. Med.27, 276–282 (2021).
38. 48. Glocker, B., Jones, C., Bernhardt, M. & Winzcke, C. Risk of bias in chest X-ray foundation models. Preprint athttps://arxiv.org/abs/2109.07290(2021).
39. 49. Beheshti, E., Putman, K., Santomartino, S. M., Parekh, V. S. & Yi, P. H. Generalizability and bias in a deep learning pediatric bone age prediction model using hand radiographs.Radiology306, e210000 (2021).
40. 50. Rösli, E., Bozkurt, S. & Hernandez-Boussard, T. Peeking into a black box, the fairness and generalizability of a MMIC-III benchmarking model.Sci. Data9, 24 (2022).
41. 51. Ebert, A. et al. Bias and fairness: potential sources of dataset bias complicate investigation of underrepresentation by machine learning algorithms.Nat. Med.28, 1157–1158 (2022).
42. 52. Mukherjee, P. et al. Confounding factors need to be accounted for in assessing bias by machine learning algorithms.Nat. Med.28, 1159–1160 (2022).

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1187

---

<!-- Page 15 -->

Article

https://doi.org/10.1038/s41591-024-02885-x

53. Meng, C., Trinh, L., Xu, N., Eussen, E. & Liu, Y. Interpretability and fairness evaluation of deep learning models on MIMIC-III dataset. Sci. Data 12, 7165 (2022).

54. Vyas, D. A., Eisenstein, L. G. & Jones, D. S. Hidden in plain sight: reconsidering the use of race correction in clinical algorithms. Neurol. J. Med. 383, 874–882 (2020).

55. Madras, D., Creager, E., Pitts, T. & Zemel, R. Learning adversarially fair and transferable representations. In Proc. 35th International Conference on Machine Learning 3384–3393 (PMLR, 2018).

56. Wang, R., Chaudhari, P. & Davatzikos, C. Bias in machine learning models can be signified by the clinical impact of care. medRxiv (2019).

57. evidence from neuroimaging studies. Proc. Natl Acad. Sci. USA 120, e2211612104 (2023).

58. Yang, J., Soltan, A. A., Eyre, D. W. & Clifton, D. A. Algorithmic fairness and bias mitigation in clinical machine learning with deep reinforcement learning. Nat. Mach. Intell. 5, 884–894 (2023).

59. Larrazabal, A. J., Nieto, N., Peterson, V., Milone, D. H. & Ferrante, E. Gender discrimination in clinical diagnosis: precludes biased classifiers for computer-aided diagnosis. Proc. Natl Acad. Sci. USA 117, 12592–12594 (2020).

60. Burlina, P., Joshi, N., Paul, W., Pacheco, K. D. & Bressler, N. M. Addressing artificial intelligence bias in renal diagnostics. Transf. Vis. Sci. Technol. 10, 13 (2021).

61. Reilly, V., Terrotola, M., Guerra, E. & Alberti, S. Distinct lung cancer subtypes associate to distinct drivers of tumor progression. Cancer Discov. 9, 565–576 (2019).

62. Reilly, V., Terrotola, M., Guerra, E. & Alberti, S. Abandoning the notion of non-small cell lung cancer. Trends Mol. Med. 25, 385–394 (2019).

63. Yan, H. et al. IDH1 and IDH2 mutations in gliomas. N. Engl. J. Med. 360, 765–773 (2009).

64. Hardt, M., Price, E. & Srebro, N. Equality of opportunity in supervised learning. In Advances in Neural Information Processing Systems Vol. 29 (eds. Lee, D. et al.) 3315–3323 (Curran Associates, 2016).

65. Barocas, S., Hardt, M. & Narayanan, A. Fairness and Machine Learning: Limitations, Fairness Definitions, and Mitigations (MIT Press, 2023); fairmlbook.org/fairmlbook.pdf

66. Choulidchova, A. Fair prediction with disparate impact: a study of bias in recidivism prediction instruments. Big Data 5, 153–163 (2017).

67. Wang, X. et al. Characteristics of The Cancer Genome Atlas Cases relative to U.S. general population cancer cases. Br. J. Cancer 119, 885–892 (2018).

68. Rowley, P. & Pejtnikov, V. et al. The Digital Brain Tumour Atlas, an open histopathology resource. Sci. Data 9, 55 (2022).

69. Maron, O. & Lozano-Pérez, T. A framework for multiple-instance learning. In Advances in Neural Information Processing Systems Vol. 10 (eds. Jordan, M. I. et al.) 570–576 (MIT Press, 1998).

70. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In Proc. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 770–778 (IEEE, 2016).

71. Wang, X. et al. Transformer-based unsupervised contrastive learning for histopathology image classification. Med. Image Anal. 81, 102559 (2022).

72. Chawla, N. J. et al. Toward a general-purpose foundation model for computational pathology. Nat. Med. 30, 850–862 (2024).

73. Ise, M., Tomczak, J. & Welting, M. Attention-based deep multiple instance learning. In Proc. 35th International Conference on Machine Learning 7079–7088 (PMLR, 2018).

74. Jaume, G., Song, A. H. & Mahmood, F. Integrating context for superior cancer prognosis. Nat. Biomed. Eng. 6, 1323–1325 (2022).

75. Kamiran, F. & Calders, T. Data preprocessing techniques for classification without discrimination. Knowl. Inf. Syst. 3, 1–13 (2012).

76. Krasanakis, E., Spyromitros-Xiofis, F., Papadopoulos, S. & Kompatsiris, Y. Adaptive sensitive weighting to mitigate bias in deep learning for medical image classification. Proc. 2016 World Wide Web Conference 853–862 (International World Wide Web Conference Steering Committee, 2018).

77. Calmon, F., Wei, D., Vinzambur, B., Ramamurthy, K. N. & Varshney, K. R. Optimized pre-processing for discrimination in medical imaging. In Advances in Neural Information Processing Systems Vol. 30 (eds. Guyon, I. et al.) 3995–4004 (Curran Associates, 2017).

78. Zemel, R., Wu, Y., Swerosky, K., Pittasi, T. & Dwork, C. Learning from diverse data. In Proceedings of the 2016 International Conference on Machine Learning 325–333 (PMLR, 2013).

79. Zafar, M. B., Valera, I., Rodriguez, M. & G. Gummadi, K. P. Machine beyond disparate treatment and disparate impact: learning from diverse data for fair medical treatment. In Proc. 26th International Conference on World Wide Web 117–118 (International World Wide Web Conference Steering Committee, 2017).

80. Cella, L. E. & Kessani, V. Improved adversarial learning for fair classification. Preprint at https://arxiv.org/abs/1910.10434 (2019).

81. Zhong, Y. et al. MEDFAR: benchmarking fairness for medical imaging. In Proceedings of the Conference on Learning Representations (ICLR, 2023).

82. Yang, Y., Zhang, H., Katabi, D. & Ghassami, M. Change is hard: a closer look at subpopulation shift. In International Conference on Computer Vision 1022–1031 (IEEE, 2022).

83. Breen, J. H. et al. Efficient subtyping of ovarian cancer histopathology whole slide images using active sampling in multiple instance learning. In Proc. SPIE 12470 (eds. Tomaszewski, J. E. & Ward, A. J.) 1247010 (Society of Photo-Optical Instrumentation Engineers, 2023).

84. Yao, J., Zhu, X., Jonnagaddala, J., Hawkins, N. & Huang, J. Whole slide images based cancer survival prediction using attention guided deep multiple instance learning networks. Med. Image Anal. 65, 101789 (2020).

85. Rusakovskiy, O. et al. ImageNet large scale visual recognition. arXiv preprint arXiv:1409.1556 (2014).

86. Subbaswamy, A. & Saria, S. From development to deployment: dataset shift, causality, and shift-stable models in health AI. Biostatistics 21, 345–352 (2020).

87. Raghunathan, M. G. et al. Causality and dataset shift in artificial intelligence. N. Engl. J. Med. 385, 288–286 (2021).

88. Castro, D. C., Walker, I. & Glocker, B. Causality matters in medical imaging. Nat. Commun. 11, 3673 (2020).

89. Raghunathan, M. G. et al. Causality in histology slides for quantitative analysis. In Proc. 6th IEEE International Conference on Symposium on Biomedical Imaging: From Nano to Macro 1107–1110 (IEEE, 2008).

90. Raghunathan, A., Basavanthly, A. & Madabhushi, A. Stain Normalization using Sparse AutoEncoders (StaSnAE) application to digital pathology. Comput. Med. Imaging Graph. 57, 50–61 (2019).

91. Ciompi, F. et al. The importance of stain normalization in colorectal tissue classification with convolutional networks. In Proc. 2017 IEEE 14th International Symposium on Biomedical Imaging 1363–1365 (IEEE, 2017).

92. Tellez, D. et al. Quantifying the effects of data augmentation and stain color normalization in convolutional neural networks for computational pathology. Med. Image Anal. 58, 101544 (2019).

93. Raghunathan, M. G. et al. Causality, Imbalance, S. Algorithmic encoding of protected characteristics in chest X-ray disease detection models. EbioMedicine 89, 104467 (2023).

94. Adalegah, J. et al. Predicting patient demographics from chest radiographs with deep learning. J. Am. Coll. Radiol. 19, 151–161 (2022).

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1188

---

<!-- Page 16 -->

Article

https://doi.org/10.1038/s41591-024-02848-x

94. Yi, P. H. & et al. Radiology ‘fornesites’: determination of age and sex from chest radiographs using deep learning. Emerg. Radiol. 28, 1–10 (2021).

95. Lu, M. Y. & et al. A-based pathology predicts origins for cancers of unknown primary. Nature 594, 106–110 (2021).

96. Naik, N. & et al. Deep learning-enabled breast cancer hormonal receptor status determination from base-level H&E stains. Nat. Commun. 11, 5727 (2020).

97. Movva, R. & et al. Coarse race data conceals disparities in clinical risk score performance. In Machine Learning for Healthcare (Springer, 2024) 433–470.

98. Mamary, A. J. & et al. Race and gender disparities are evident in COPD underdiagnoses across all severities of measured airflow obstruction. Chest Obstruct. Pulm. Dis. 5, 177–184 (2018).

99. Sun, T. & et al. Exploring gender disparities in time to diagnosis, in Machine Learning for Healthcare Association (Curren Associates, 2020).

100. Giannaccos, M. A., Tamang, S., Vazquez, J. & Schmaljak, G. Potential biases in machine learning algorithms using electronic health record data. JAMA Intern. Med. 178, 1544–1547 (2018).

101. Gloeckler, B., Jones, C., Roschewitz, M. & Winzke, S. Risk of bias in chest radiography deep learning foundation models. Radiol. Artif. 101, 5, e203060 (2023).

102. Piholi, S. R., Foryczko, A. & Shah, N. H. An empirical characterization of the impact of time for clinical risk prediction. J. Biomed. Inform. 113, 103621 (2021).

103. Borrell, L. N. & et al. Race and genetic ancestry in medicine—a time for reckoning with racism. N. Engl. J. Med. 384, 474–480 (2021).

104. Chen, R. J. & et al. Algorithmic fairness in artificial intelligence for medicine and healthcare. Nat. Biomed. 9, 719–724 (2023).

105. Banda, Y. & et al. Characterizing race/ethnicity and genetic ancestry for 2,000 subjects in the Cancer Epidemiology Research on Adult Health and Aging (GERA) cohort. Genetics 200, 1285–1295 (2015).

106. Bamshad, M., Wooding, S., Salisbury, B. A. & Stephens, J. C. Detecting the relationship between genetics and race. Nat. Rev. Genet. 5, 598–609 (2004).

107. Bhargava, H. K. & et al. Computationally derived image signature of stromal morphology is prognostic of prostate cancer recurrence following prostatectomy in African American patients. Clin. Cancer Res. 26, 1915–1923 (2020).

108. Shi, Y. & et al. A prospective, molecular epidemiology study of EGFR mutations in Asian patients with advanced non-small-cell lung cancer of adenocarcinoma histology (PIONEER). J. Thorac. Oncol. 9, 154–162 (2014).

109. Martini, R. & et al. African ancestry-associated gene expression profiles in triple-negative breast cancer underlie altered tumor biology and clinical outcome in women of African descent. Cancer Discov. 12, 2530–2551 (2022).

110. Zhang, G. & et al. Characterization of frequently mutated cancer genes in Chinese breast cancer patients of Chinese and TCGA cohorts. Ann. Transl. Med. 7, 179 (2019).

111. McCradden, M. D., Joshi, S., Mazwi, M. & Anderson, J. A. Ethical limitations of algorithmic fairness solutions in health care machine learning. Health Affairs 42, e221–e223 (2023).

112. Sung, H., DeSanitis, C. E., Fedewa, S. A., Kantelhardt, E. J. & Lemel, A. Breast cancer subtypes among Eastern-African-born black women and other black women in the United States. Cancer 125, 3401–3410 (2019).

113. Li, X., Wu, P. & Su, J. Accurate fairness-improving individual fairness without trading accuracy. In Proc. 37th AAAI Conference on Artificial Intelligence Vol. 37 (eds. Williams, B. & et al.) 14312–14320 (Association for the Advancement of Artificial Intelligence, 2023).

114. Martin, R. A. & et al. Clinical use of current polygenic risk scores may exacerbate health disparities. Nat. Genet. 51, 584–591 (2019).

115. Hwang, S. H., Kim, D. S., Wang, S. H., Kim, D. S. & Lee, D. S. Delaying deep imbalanced regression. In Proc. 38th International Conference on Machine Learning 11842–11851 (PMLR, 2021).

116. Mokir, M., Singh, A., Hong, J. & Joachims, T. Controlling fairness and bias in dynamic learning-to-rank. In Proc. 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval 429–438 (Association for Computing Machinery, 2020).

117. Liao, Y. & et al. Assessing the potential of GPT-4 to perpetuate racial and gender biases in health care: a model evaluation study. Lancet Digit. Health 6, e12–e22 (2024).

118. Voronov, E. & et al. Virochwa—a million-slide digital pathology foundation model. Preprint at https://arxiv.org/abs/2309.07778 (2023).

119. Dippe, J. & et al. Rudofsky: A foundation model for pathologists for histological diagnosis. Preprint at https://arxiv.org/abs/2401.06705 (2024).

120. Chawda, N., Bowyer, K. W., Hall, L. A. & O’Keefe, M. W. SMOTE: synthetic minority over-sampling technique. J. Artif. Intell. Res. 16, 321–357 (2007).

121. Sheng, S. R. & et al. Understanding subgroup performance differences of fair predictors using causal models. In NeurIPS 2023 Workshop on Distribution Shifts: New Frontiers with Foundation Models (2023).

122. Sheng, S. R. & et al. A Yadvansky: S. Diagnosing model performance under distribution shift. Preprint at https://arxiv.org/abs/2303.02011 (2023).

123. Moriam, A. The racial self-identification of South Asians in the United States. J. Pers. Soc. Psychol. 61, 71–79 (2001).

124. Chadban, S. J. & et al. KDIGO clinical practice guideline in the evaluation and management of candidates for kidney transplantation. Transplantation 91, S10–S103 (2020).

125. Breyer, N. D., Yang, Y. & et al. P: Reconsidering the consequences of using race to estimate kidney function. JAMA 322, 113–114 (2019).

126. Liao, Y., Liao, X., Young, B. & Bansal, N. Association of the estimated glomerular filtration rate with vs without a coefficient for race with time to eligibility for kidney transplant. JAMA Netw. Open 4, e2034004 (2021).

127. Liao, Y., Liao, X., Gort, M. & P. Loubes, J.-M. Review of mathematical frameworks for fairness in machine learning. Preprint at http://arxiv.org/abs/2005.13755 (2020).

128. Binns, R. & on the apparent conflict between individual and group fairness in health care. Health Affairs 40, 1140–1151 (2021).

129. Braveman, P., Egerter, S. & Williams, D. R. The social determinants of health: coming of age. Annu. Rev. Public Health 32, 381–398 (2011).

130. Walker, R. J., Williams, J. S. & Egerton, L. E. Influence of race, gender, and ethnicity on the risk of death from health on diabetes outcomes. Am. J. Med. Sci. 361, 336–373 (2016).

131. Link, B. G. & Phelan, J. Social conditions as fundamental causes of disease. J. Health Soc. Behav. 35, 80–94 (1995).

132. Anderson, N. D. & Norris, M. Access to health and health care: how race and ethnicity matter. Mil. Stat. J. Med. 77, 166–171 (2010).

133. Yearby, R. Racial disparities in health status and access to health care: the continuation of inequality in the United States due to structural racism. Am. J. Econ. Soc. 77, 1113–1152 (2018).

134. van Ryn, M. Research on the provider contribution to racial/ethnicity disparities in medical care. Med. Care 40, 1140–1151 (2002).

Nature Medicine | Volume 30 | April 2024 | 1174–1190

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1189

---

<!-- Page 17 -->

Article
https://doi.org/10.1038/s41591-024-02885-z

135. George, S., Ragin, C. & Ashing, K. T. Black is diverse: the untapped beauty and benefit of cancer genomics and precision medicine. JCO Oncol. Pract. 17, 279–283 (2021).

136. Campbell, M. C. & Tishkoff, S. A. African genetic diversity: implications for human demographic history, modern human origins, and complex disease mapping. Annu. Rev. Genomics Hum. Genet. 9, 403–433 (2008).

137. Bonham, V. L., Green, E. D. & Pérez-Stable, E. J. Examining how race, ethnicity, and ancestry data are used in biomedical research. JAMA 320, 1533–1534 (2018).

138. Daneshjou, R. et al. Disparities in dermatology AI performance on a diverse, curated clinical image set. Sci. Adv. 8, eabq6147 (2022).

139. Zou, J., Gichoya, J. W., Ho, D. E. & Obermeyer, Z. Implications of predicting race variables from medical images. Science 381, 149–150 (2023).

140. Chen, I. Y., Johansson, F. D. & Sontag, D. Why is my classifier discriminatory? In Advances in Neural Information Processing Systems Vol. 31 (Curran Associates, 2018).

141. Puyol-Antón, E. et al. Fairness in cardiac magnetic resonance imaging: assessing sex and racial bias in deep learning-based segmentation. Front. Cardiovasc. Med. 9, 859310 (2022).

142. US Food and Drug Administration. Proposed regulatory framework for modifications to artificial intelligence/machine learning (AI/ML)-based software as a medical device (SaMD). www.fda.gov/files/medical%20devices/published/US-FDA-Artificial-Intelligence-and-Machine-Learning-Discussion-Paper.pdf (2019).

143. Gaube, S. et al. Do as I say: susceptibility in deployment of clinical decision aids. NPJ Digit. Med. 4, 31 (2021).

144. Zhu, S., Gilbert, M., Chetty, J. & Siedlitz, F. The 2021 landscape of FDA-approved artificial intelligence/machine learning-enabled medical devices: an analysis of the characteristics and intended use. Int. J. Med. Inform. 165, 104828 (2022).

145. Liu, X. et al. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Lancet Digit. Health 2, e537–e548 (2020).

146. Sounderajah, V. et al. Developing a reporting guideline for artificial intelligence-centred diagnostic test accuracy studies: the STARD-AI protocol. BMJ Open 11, e047709 (2021).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature America, Inc. 2024

†Department of Pathology, Brigham and Women's Hospital, Harvard Medical School, Boston, MA, USA. ‡Department of Pathology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA. §Cancer Program, Broad Institute of Harvard and MIT, Cambridge, MA, USA. ¶Cancer Data Science Program, Dana-Farber Cancer Institute, Boston, MA, USA. ||Health Sciences and Technology, Harvard-MIT, Cambridge, MA, USA. |||Department of Biomedical Informatics, Harvard Medical School, Boston, MA, USA. |||Department of Pathology and Laboratory Medicine, Emory University School of Medicine, Atlanta, GA, USA. |||Electrical Engineering and Computer Science, MIT, Cambridge, MA, USA. |||School of Data Science, University of Virginia, Charlottesville, VA, USA. |||T.H. Chan School of Public Health, Harvard University, Cambridge, MA, USA. |||Harvard Data Science Institute, Harvard University, Cambridge, MA, USA. |||These authors contributed equally: Anurag Vaidya, Richard J. Chen, Drew F. K. Williamson.

✉ e-mail: faisalmahmood@bwh.harvard.edu

Nature Medicine | Volume 30 | April 2024 | 1174–1190
Content courtesy of Springer Nature, terms of use apply. Rights reserved
1190

---

<!-- Page 18 -->

Articles

(https://doi.org/10.1038/s41591-024-02885-z)

## Methods

### Dataset description

The TCGA dataset is a review board approved retrospective analysis of pathology slides and corresponding pathology reports. Research conducted in this study involved a retrospective analysis of pathology slides, and the participants were not directly involved or recruited for the study. The requirement for informed consent for analyzing archival pathology slides was waived. Before scanning and digitization, all pathology slides were deidentified to ensure anonymity. Likewise, all digital data, which encompassed WSIs, pathology reports and digital medical images, underwent deidentification before being subjected to computational analysis and model development. Sample sizes were determined by data availability, and all in-house data used in the research were dated between 2016 and 2022.

Our archival data consisted of 2,251 WSIs, including both publicly available and in-house datasets, amounting to 8.0 terabytes of raw data. The population demographics of each dataset are provided in Supplementary Data Tables 2–4. Our overall dataset consisted of the following sources.

The Cancer Genome Atlas. The TCGA dataset is a public and comprehensive collection of cancer genomic data across multiple cancer types. In this study, we used the TCGA-BRCA (breast invasive carcinoma collection), TCGA-LUAD, TCGA-LUSC, TCGA-GBM and TCGA-LGG cohorts. We refer to the combined set of TCGA-LUAD and TCGA-LUSC as TCGA-LUNG cohorts, under the deidentification process. We also analyzed TCGA-LGGs as TCGA-GBMLGG cohort. We used 1,049 WSIs from the TCGA-BRCA cohort sourced from 40 different tissue-contributing sites. Of the 1,049 TCGA-BRCA WSIs, 838 are WSIs of IDC and 211 are ILC. The TCGA-lung cohort comprised 1,043 lung WSIs from 73 distinct tissue-contributing sites in the TCGA dataset. The TCGA-lung cohort has 531 cases of LUAD and 512 cases of LUSC. We used 1,123 WSIs from the TCGA-GBM cohort sourced from 40 different tissue-contributing sites. TCGA-GBMLGG comprised 698 WSIs of IDH1 wild-type cancers and 425 WSIs of IDH1 mutant cancers. For TCGA-BRCA, TCGA-lung and TCGA-GBMLGG, only representative formalin-fixed, paraffin-embedded digital pathology slides were used. For TCGA-LGG, we used 1,049 independent test cohorts contributed data to TCGA. The TCGA WSIs and associated clinical data can be accessed through the National Cancer Institute's Genomics Data Commons portal (https://portal.gdc.cancer.gov/) and the Cancer Data Commons portal (https://cancerdatacommons.bioportal.org/). Any clinical data missing on BioPortal were acquired from pathology reports provided by Genomics Data Commons portal.

In-house data. The in-house data collected from MGB consisted of 3,225 WSIs corresponding to the same number of cases. To select patients for the study, we queried our in-house database of pathology slides from patients from a 520 scanner (Nemo = 92, Nemo = 116), within this period with available slides that met the following inclusion criteria: (1) have a lower-magnification downsampling for segmentation and processing the tissue image and (2) have nonzero tumor content. We excluded missing or low-quality images and those that were not rescaned and included in the study. This dataset consists of cases of invasive breast carcinoma, which we call the MGB-breast cohort, and cases of adenocarcinoma and squamous cell carcinoma of the lung, which we call the MGB-lung cohort. We used 1,049 WSIs from the MGB-breast cohort comprised 1,265 invasive breast cancer cases, including 982 cases of IDC (MGB-IDC) and 283 cases of ILC (MGB-ILC). The MGB-lung cohort comprised 2,1960 cases, consisting of 1,626 cases of LUAD (MGB-LUAD) and 534 cases of LUSC (MGB-LUSC). These cases were scanned either at 20× magnification using an Aperio GT450 scanner or at 40× magnification using a Hamamatsu S210 scanner (and included 20× and 40× pyramidal samplings). For MGB-breast, we scanned cases extremely using the Hamamatsu S210 scanner (Nemo = 92, Nemo = 116), whereas 1,057 cases were scanned using the Aperio GT450 scanner

(Nemo = 904, Nemo = 50, Nemo = 48, Nemo = 48, Nemo = 55). For the MGB-lung cohort, 134 cases were scanned with the Hamamatsu S210 scanner and 1,057 cases (Nemo = 60, Nemo = 67, Nemo = 66, Nemo = 66, Nemo = 61). Extended Data Fig. 1 compares the hue and saturation of slides corresponding to different races; we found no statistically significant differences in the hue and saturation between the slides of different races. For in-house patients, the diagnosis assigned was based on a comprehensive review conducted by multiple pathologists. Protected patient information, including self-reported race categories ('white', 'black', 'asian', 'indian', 'hispanic', 'other') and patient ID number type, was collected from electronic medical records. No slides from MGB were contributed to TCGA's data collection initiative. For data availability, refer to 'Data availability'; for institutional review board approval, refer to 'Dataset description' above.

EBRAINS brain tumor atlas. The EBRAINS brain tumor atlas15 is a public and comprehensive collection of brain tumor pathology slides dedicated brain tumor bank based at the Division of Neuropathology and Neurochemistry of the Medical University of Vienna, covering brain tumor cases from 1995 to 2019 (ref. 67). Slides were digitized using a 40× scanner and 40× magnification. There are 40× and 40× magnification. At least two experienced neuropathologists checked each slide scan to ensure conformity of the diagnosis with the current revised 4th edition of the World Health Organization Classification of Tumours of Central Nervous System (WHO 2021) with sufficient accuracy. Ambiguous cases were excluded, and WSIs of inferior quality were rescaned. We selected 873 cases with known IDH1 mutation status. There were 540 IDH1 wild-type cases and 333 IDH1 mutant cases. There were 508 GBM cases and 365 LGG cases. Information about race, insurance and income is provided, whereas the patients' age and sex are known. The EBRAINS brain tumor atlas is available publicly from the official EBRAINS data portal (https://search.ebrains.eu/en/instances/Dataset/S1cBioLab-2024-46ef-8999-60220d41994).

### Processing of digital pathology slides

As WSIs are large images, we downsampled them to 150,000 × 150,000 pixels, it is computationally infeasible to use raw WSIs directly in DL pipelines16. In line with previous work16,17,18, we first segmented the tissue from the background, divided the tissue into smaller nonoverlapping patches and then applied the segmentation patches from WSIs comprise a bag of patches and further downsamplings them using pretrained neural networks. The details of these steps are as follows.

Tissue segmentation. Tissue from WSIs was segmented using the CLAM19 library at 20× magnification for each slide. First, the image was converted from RGB (red, green, blue) to HSV (hue, saturation, value) and then thresholded. The threshold was defined as the saturation channel of the HSV image and then was used as a binary mask for tissue regions. To refine further the segmented tissue contours and address potential artifacts such as small gaps and holes, we used a combination of morphological operations and watershed techniques. To obtain the final tissue segmentation, we subjected the approximated contours of the detected tissue and tissue cavities to a filtering process.

Patching. The segmented tissue was cropped into 256 × 256 patches (no overlap). This was performed at 20 × magnification if available in the image pyramid range; otherwise, 512 × 512 patches were cropped from the 40 × magnification and resized to 256 × 256 (ref. 4L).

Feature extraction. As each bag of patches representing WSIs can be extremely large (for example, >10,000 patches19), we encoded each patch into a compact low-dimensional feature vector using a pretrained neural network, which is referred to as the patch encoder. Because the patch encoder is frozen during training, the choice of pretraining

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 19 -->

ArtiCh

https://doi.org/10.1007/s41591-024-02885-x

data and strategy is essential. In this study, we examined the use of three patch encoders: a ResNet50 convolutional neural network48 pre-training feature extractor, a ViT-1649 pre-training feature extractor, and a patchnet on approximately 1.56 million histograms images from TCGA and PAI (Pathology AI Platform, http://wispiaap.org/pai/) using MoCo v3 (refs. 70, 71), and a ViT-16 transformer49 trained on approximately 100 million histology images using a DINOV2 self-supervised pre-training scheme72. For the ResNet patch encoder, the adaptive mean spatial pooling after the third residual block of the network was used to convert each patch into a compact 1,024-dimensional feature vector. The Swin Transformer48 pre-training encoder, each patch was first resized to a 224 × 224 image and then the provided model weights were loaded in the architecture to convert each patch into a 768-dimensional and 1,024-dimensional feature vector, respectively. The ViT-16 encoder is referred to as ViT-16-Swin. ViT-16 is referred to as CTransPath and the ViT-16 encoder is referred to as UNI. To increase the speed of the feature extraction step, we used three ViT-16 ViT-16GPT architectures to process inputs with a batch size of 384 per GPU. To test the effect of the pretraining scale on demographic disparities, we also used a ViT-16 transformer49 on approximately 1 million and 16 million histology images using a DINOV2 self-supervised pre-training scheme72 and trained the encoder and UNI, respectively. While none of UNI, UNI+ and UNI- was pretrained on any data used in this study, we note that CTransPath was originally pretrained on TCGA (without any subtype or mutation labels). Thus, MIL models using CTransPath trained on TCGA data are expected to generalize histology images inflame performance due to data leakage from pretraining. Finally, the demographic composition of the pretraining datasets for the encoders used is not available and often challenging to collect, as in the case of TCGA trained on public datasets that organize histology images from worldwide institutions where demographic data may not have been collected (http://wispiaap.org/pai/).

Stain normalization. To extract stain-normalized features, we applied Macenko stain normalization to individual image patches before they were input into the patch encoder, using the implementation from https://sliedhoff.de/slide_processing/ (ref. 154).

### Weakly supervised classification

In this study, we trained MIL-based weakly supervised WSI classification models for three cancer types: breast cancer (BC), lung cancer (LC), and prostate cancer (PR) using three datasets: TCGA, PanCancer (PanCA), and ITHI. In this task, as 'breast subtyping' and 'LIDH versus LUSC' (we refer to this task as 'lung subtyping'), and 'IDH1 wild-type versus IDH1 mutant' (we refer to this task as 'IDH1 mutation prediction'), 1D models have been used to perform information extraction from the 1D images. To minimize the need to optimize the models' performance on the classification task and instead allowing to focus on the models' performance within demographic groups. For the breast cancer classification task, 1D models were implemented: ABMIL10, CLAM11, and TransMIL12. These approaches were chosen because they can perform slide-level classification without any region-of-interest extraction or patch-level parameterization, can be trained on a single modality images, and have previously demonstrated strong performance on the TCGA dataset and independent test cohorts10–12. The implementation details of ABMIL, CLAM, and TransMIL are now covered.

ABMIL and CLAM. To learn histology specific feature representations, we passed the patch embeddings extracted by the patch encoder through three fully connected layers. These layers are respectively patch-level, block-level, and whole-slide-level images. These terms are implied and omitted for simplicity. Each fully connected layer is followed by rectified linear unit activation. Thus, each patch embedding z_{i,j} \in \mathbb{R}^{d_{i,j}} is mapped to a feature vector which serves as the input to downstream patch aggregation. ABMIL uses an attention module to learn to rank the relative importance of each image patch to classify

the WSI. The attention module takes in each patch embedding h_{i,j} and learns the weights v_{i,j} \in \mathbb{R}^{d_{i,j}}, u_{i,j} \in \mathbb{R}^{d_{i,j}} and w \in \mathbb{R}^{1 \times d_{i,j}} to score the patch (u_{i,j}):

a_{i,j} = \frac{\exp(W_{i,j}^T (v_{i,j} - h_{i,j})) \otimes \text{sigmoid}(U_{i,j} - h_{i,j})}{\exp(\sum_{i,j} W_{i,j}^T (v_{i,j} - h_{i,j})) \otimes \text{sigmoid}(U_{i,j} - h_{i,j})} \quad (1)

The slide-level representation, h_{slide} \in \mathbb{R}^{1 \times d_{slide}}, is then the sum of the patches weighted by the attention weights:

h_{slide} = \sum_{i,j} a_{i,j} \cdot h_{i,j} \quad (2)

A dropout layer (P=0.25) is used after each layer in the attention backbone for model regularization. The attention module features h_{slide} are then fed to a fully connected layer (defined by W_{fc} \in \mathbb{R}^{1 \times d_{123}}), which is followed by the softmax operator to produce slide-level binary class prediction probabilities. p_{slide} = \text{softmax}(W_{fc} \cdot h_{slide}) (3)

CLAM, in addition to slide-level classification, also performs instance-level clustering as additional supervision to constrain similar diagnostic image regions with similar important weights11.

TransMIL. TransMIL "approximates self-attention with Nystrom attention" to perform self-attention based pooling of individual patches in a WSI. Specifically, TransMIL first squares a sequence of patch embeddings, applies different sized convolutions to encode spatial information, flattens the sequence of patches, applies a class token (called CLAS token) and then uses multilayer self-attention (a linear approximation of self-attention provided by Nystrom attention10) to learn the correlations between patches and the encoded spatial information.

### Data-splitting strategies

Two different strategies were used for creating training and validation cohorts. For the TCGA dataset, we used the Monte Carlo CV, in which the dataset is randomly split into training and validation data in a fixed ratio (stratified by subtype or mutation label); this process is repeated for a fixed number of folds. In our study, we used 90% of the data for training and 10% for validation over 20 folds10–12. Previous work has shown that there are site-specific digital histology signatures in the TCGA dataset14, and different tissue-contributing sites have different racial compositions. Thus, if the submitting sites within a dataset are heterogeneous, the stratification of the dataset into Cardio-CV, which is that a feature of interest would not be evenly represented among these groups, resulting in biased estimates of accuracy. Hence, we used the federated programming solution from Howard et al.21 to generate site-specific stratified splits for the TCGA-BRCA and TCGA-lung cohorts, which led to approximately 90% data for training and 10% for validation. The public Python package for site-stratified splitting generation was accessed from https://github.com/HowardLab/serveTestCV. Ten was the maximum number of folds that the quadratic programming solution provided by Howard et al.21 could converge on for the TCGA-lung cohort. Site-stratified splits could not be made for the EBRAINS brain cohort, as the EBRAINS dataset is not publicly available on tissue-specifics. Multiple training folds are used for all tasks to avoid bias towards certain data. Validation splits are used for saving model checkpoints. Models from all folds are tested on task-specific independent test cohorts using the same metrics are reported. Slices from same case were not distributed between training and validation splits.

### Training details

The training of all models was done using the AdamW optimizer18. Following previous studies9,10,11, we trained the ABMIL and CLAM

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

14

---

<!-- Page 20 -->

Article

https://doi.org/10.1038/s41591-024-02885-x

models using a learning rate of 1 \times 10^{-4} and \lambda_2 weight decay of 0.1 \times 10^{-4}. Following Shao et al.13, we trained TransMIL using a learning rate of 2 \times 10^{-4} and \lambda_2 weight decay of 0.1 \times 10^{-4}. We trained the model by minimizing the cross-entropy loss. CLAM was trained using a weighted loss of the cross-entropy loss for slide classification and the smooth top-1 support vector machine loss44 for distinguishing high- and low-risk patients. In the case of TDMIL and CLAM, the weights were set to 0.7 and 0.3 for the slide-level loss and instance-level loss, respectively, and the temperature scaling parameter and the margin parameter r were both set to 1.0. The weights and parameters of the models were evaluated randomly during training, unless otherwise stated. slides were randomly sampled from the training cohort and provided to the model with a mini-batch size of 1. All models were trained for a maximum of 20 epochs. After the first 10 epochs, the performance of the models was evaluated, and it then decreased for five consecutive epochs, early stopping was triggered and model weights were saved. For each fold, the model checkpoint with the lowest validation loss was used for evaluation on the respective independent test cohort.

### Bias mitigation strategies

Compared to pre-processing bias mitigation strategies were applied to investigate their ability to reduce differences between different demographic groups. These strategies included IV45–47 from preprocessing and AR48 from imputation. While IV tries to remove a group's performance on underrepresented samples by weighted sampling (variably proportional to a group's size), AR encourages the model not to use information correlated with protected attributes. The bias mitigation techniques, which need access to protected attributes, were applied only to the TDMIL and CLAM lung cohorts during the training phase, and no mitigation technique was applied to the MGB independent test set. Both the bias mitigation techniques are model-agnostic and can be applied to any model. The bias applied to the IDH1 mutation prediction problem as race information for the EBRAINS brain tumor atlas is not provided. We now cover their implementation details.

Importance weighting. In IV (Fig. 1c), samples from the underrepresented groups in the dataset are shown more frequently to the model, giving them higher importance and thereby improving the performance of the model. The importance of a sample was calculated the proportions of different races in the overall TCGA lung and TCGA-BCRA datasets. We considered the 'white', 'Asian' and 'Black' race categories. As nonreporting patients account for approximately 10% of all individuals in the dataset, we considered nonreporting groups as a category not to substantially reduce training dataset size. During the training of the subtyping models, each patient from the training dataset was randomly sampled with a probability that was inversely proportional to the representation of the patient's race in the overall dataset. Thus, underrepresented patients, such as 'Black' and 'Asian' patients, were sampled more often and shown more frequently to the model. The overrepresentation of underrepresented groups during sampling was not applied to the validation and test splits; the model was evaluated on each sample from the validation split and independent test dataset only once.

Adversarial regularization. To make the model agnostic to the information related to the sensitive attribute (that is, race), we first passed the slide-level representation (the same representation used to learn the model) of the subtyping models through a connected layer to predict the attribute of the patient (Fig. 1d). Cross-entropy loss was used to calculate the attribute prediction discrepancy. As the aim was to make the model invariant to the sensitive attribute, the negative of the attribute prediction loss was back-propagated, making the model poor in predicting the attribute. The attribute classifier was trained with the same

hyperparameters as the subtyping model, and its weights were updated with the same frequency as the subtyping model. The implementation of adversarial regularization for the subtyping models were available at https://github.com/ShenYanUS/ Multimodal_Fairness. In addition to 'white', 'Asian' and 'Black' race categories, nonreporting group was also considered as not to reduce the training dataset size substantially.

### Evaluation

Evaluation metrics. Subtyping and mutation prediction tasks are binary classification tasks. These tasks were evaluated in both overall and stratified groups. For the subtyping evaluation, the performance of the dataset were considered as patients from nonreporting group make a substantial portion of the dataset and the patient population. In the race-stratified evaluation, metrics for individual races were calculated, while not calculating metrics on the nonreporting group as these patients could be of any demographic. For both the overall and race-stratified settings, we report the ROC AUC. The ROC curve is a plot of the True Positive Rate as the classification threshold is varied. For individual classes, we also report the overall and race-stratified recall, which measures the proportion of positive instances (for example, true positive (TP) and false negative (FN)) that the model correctly identified as positive, indicating the model's ability to find all relevant positive samples:

\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \quad (4)

We also report the macro-averaged F1 score for the overall and race-stratified settings. The macro-averaged F1 score is computed by calculating the F1 score (the harmonic mean of precision and recall, equation (5)) for each class independently. Then, these individual F1 scores are averaged together. Here, 'FP' stands for false positive.

\frac{2 \times \text{TP}}{2 \times \text{TP} + \text{FP} + \text{FN}} \quad (5)

For the classification problem of race prediction, the macro-averaged overall one-versus-rest (OVR) AUC is reported. The macro-averaged OVR AUC generalizes the AUC to the multiclass case by averaging over the ROC AUC of all pairwise combinations of classes.

Selection of cutoffs. When testing a model on any independent test cohort, we used the Youden/ statistic method49 to find the optimal cutoffs. Specifically, for a fold, to convert the model's predicted logits on the test cohort into the true positive and negative classification used the Youden/ statistic from the model's corresponding validation fold. The Youden/ statistic finds the optimal balance between sensitivity and specificity on the validation fold. The same method was applied with subtyping and mutation prediction49. When testing on the internal TCGA and MGB cohorts, we used the validation set to determine the threshold.

Definition and quantification of the fairness metrics. To characterize the fairness of AI oncology models, we followed the group fairness metrics and estimated algorithmic fairness as defined by the separation between the performance of the protected group (equity opportunity)49. Equalized opportunity is a condition for classification parity that suggests that TPR should be equalized across protected subgroups for model fairness and nondiscrimination.

Equity opportunity is the proportion of 'true' or 'negative' classes in the tasks considered, we assessed equalized opportunity for each class. Formally, for a binary prediction \hat{Y} made on a sample X with a protected subgroup G (for example, race) and ground-truth outcome Y, \hat{Y} satisfies equalized opportunity if the TPR is equalized across all protected subgroups.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 21 -->

Articles

https://doi.org/10.1038/s41591-024-02985-x

For example, for subgroups of white, Asian and Black patients in our race-stratified evaluation, equalized opportunity is satisfied if

P(Y = 1 | A = 1, Y = 1) = P(Y = 1 | A = 0, Y = 1),

\forall r, r' \in \{\text{white, Asian, Black}\}, r \neq r'.

With the separation framework, we established our fairness metric as ‘TPR disparity’, which measures the difference in TPR between protected subgroups and the population TPR. Negative TPR disparity in a subgroup indicates that the model misdiagnoses patients in that subgroup at a greater rate than in the overall population. The same definition can be extended to the other protected attributes considered in the study, such as income, insurance and age groups. During intersectional analysis, we compared the sensitivity of the intersectional group to that of the general population.

Test set resampling. The goal of test set resampling is to create an unbalanced test set. To select a test set, we sampled 500 patients from each of the protected attribute subgroups for each subtype of lung and breast cancer. The same method was also used for creating unbiased test sets for the DDH mutation prediction task. Test set resampling was used to create a test set with a balanced distribution of tasks and to none of the training and validation datasets. No considerable effect was found by varying the number of samples sampled per subgroup (Extended Data Fig. 10).

## Review of Food and Drug Administration-approved medical imaging AI algorithms

Documentations (S10(k) and de novo approvals) submitted by companies that develop medical imaging AI algorithms to the US Food and Drug Administration (FDA) between January 2017 and December 2020 were reviewed. Only algorithms that work with medical imaging modalities (computed tomography (CT), positron emission tomography–CT, magnetic resonance imaging, radiography, microscopy, autofluorescence imaging and ultrasonography) were considered. The list of devices and the FDA approval numbers for the algorithms were retrieved at https://www.fda.gov/med-products (ref. 168). For each algorithm, the FDA approval number was used to access the publicly available documentation used for approving the algorithm. The documentation, acquired as a single PDF file, was then reviewed to determine if the algorithm accurately recorded the exact demographics of their test set (age, sex, ethnicity and race). Next, the documentation was reviewed to determine whether the company reported any performance metrics (sensitivity, specificity, AUC or accuracy) that differed from the general population. We also reported that no significant differences were found by demographics, this was considered as reporting demographic-stratified performance metrics. In addition to a machine-readable version of the documentation, the word search was done to make sure that the reporting of demographics or their metrics was not missed. Keywords included the following terms: age, old, young, sex, gender, male, female, race, ethnicity, ancestry, white, Caucasian, Brazilian, Indian, Asian, African, American, demographics and subgroups. Paige AI was approved in 2021. It was included in the analysis because its algorithm is highly relevant to the imaging modality (microscopy/histology) and application domain (oncology) of our study. Our analysis was based only on publicly available documentation that can be accessed at https://www.fda.gov.

## Forming demographic subgroups

We divided patients with lung and breast cancer into subgroups by age at diagnosis, we used the national average age at diagnosis for breast and lung cancer patients. The national average age at diagnosis is 62 years for breast cancer patients and 70 years for lung cancer patients169. To convert postal code information to median household income in the postal code (simply referred to as ‘income’ in the study),

we used the database at https://pyppr.org/project/uzipcode/. Specifically, we used income from the 2010 US census, as this was the most recent census that provided level of detail at the time of the study through the software. To create the three income groups (low, middle and high), we used the 33rd and 66th percentiles to divide the patients into approximately three equal subgroups. Anytime a reference to patients from an income group is made, one must ensure that this is the median household income of the postal code neighbourhood the patient has self-reported and may not be the patient’s actual household income. Regarding insurance, we categorized patients into (1) those with Medicare, (2) those with Medicaid, (3) those on Medicare and those with some form of public insurance, namely Medicare (we call this group ‘on Medicare’). The ‘on Medicare’ group included patients who were on Medicare only and those who were on some private insurance and Medicare. MGB used the same approach to create patients with IDC and one with ILC. MGB lung had ten white patients with unknown insurance (five with UAD and five with LUSC), nine Black patients with unknown insurance (five with UAD and five with LUSC) and 2 Asian patients with unknown insurance (five with UAD and five with LUSC). As the number of patients with unknown insurance was small, this category was not considered. TCGA-GBMLGG provided the age at diagnosis for all patients with lung cancer. In contrast, the Cancer Genome and LGC have different prevalences by age170,171. We used the 33rd and 66th percentiles to divide the patients into approximately three equal subgroups (<40, <40 + 60, >60 years). Any demographic subgroup that had fewer than three patients or had patients from only one subtype or mutation class was excluded.

## Predicting protected attributes from embeddings used for performance tasks

In this study, we predicted protected attributes (that is, race) from the embeddings used for breast and lung subtyping and DDH mutation prediction. We used the embeddings created using the last two layers of the model except the final, fully connected classification layer. We replaced the classification layer with a logistic regression model. Specifically, the slide-level representation from equation (2) was used for the embeddings. The embeddings were used for training a fivefold CV study (folds stratified by race and label), we trained the logistic regression model to predict the protected attribute on the independent test cohort for the task. The logistic regression model and CV study were repeated 100 times. The logistic regression model was trained for 1,000 iterations with lbfis (limited-memory Broyden–Fletcher–Goldfarb–Shanno algorithm) solver, L_2 penalty and 0 < \epsilon (the inverse of regularization strength). Macro-averaged ORs and AUCs were calculated for each of the protected attributes predictions. Note that we did not train wholly supervised AI models to predict race directly from WSIs. Rather, we only investigated whether the race and ethnicity prediction are related by predicting race from the tasks and embeddings learned for subtyping or mutation prediction (Extended Data Fig. 2).

## Analyzing the impact of training dataset size and composition on disparities

To understand the impact of the training dataset size and the demographic subgroups forming it, we systematically varied the dataset size and the demographic subgroups included. We followed this approach to (1) that vary by the number of samples (from 5 per subtype (referred to as k = 10) to 25 per subtype (referred to as k = 50)) and by racial composition (white only, Asian and Black only, and a combination of all races included). We trained the models using the embeddings from the training sets and creating training sets from TCGA and using MGB cohorts as the test sets and (2) creating training sets from MGB and using TCGA cohorts as the test sets. For each dataset size and composition, sampling was done ten times to create training folds, and the LMI patch encoder and ABMLI aggregator were used for all experiments. Samples that

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 22 -->

Bartoli

https://doi.org/10.1038/s41591-024-02885-z

were not sampled for training for a fold were used for validation. When training with all patients of a specific subgroup composition (k=1), we used 20-fold cross-validation. This procedure was repeated to stay consistent with previous experiments using data from all races/groups. To test the demographic disparities in internal TCGA and MGB cohorts, we used the k=50 set composed of all races and reported the disparities on the associated validation set. This was done to ensure that sufficient samples of each subtype from all races were present in the training and validation sets.

## Statistical analysis

Hypothesis testing. To compare the TPR and disparity for different demographic groups within a class for a single experiment, we conducted two-sided paired nonparametric permutation tests14,15. Specifically, we tested the hypothesis that the TPR was equally dispersed. All model performs equally well on demographic group, of a class relative to patients of demographic group, of that class in terms of their TPR disparity. To ensure this, we considered the white and black race groups for the UAD subtype and the ABML aggregator with a UNO encoder trained on TCGA-Lung and tested on MGB-Lung without any bias mitigation strategy. To perform the permutation test, we first pooled the data from the race group composition. We then randomly sampled from the first or second sample. Then, the statistic (difference of means of samples) was calculated. This process was performed repeatedly, n_{permutations}=10,000 times, generating a distribution of the statistic. We then compared the hypothesis distribution with the calculated value compared to this distribution to determine the Pvalue. The raw PValues for comparisons between demographic groups within a class for a single experiment were then corrected for multiple-hypothesis testing using Bonferroni-Hochberg correction16 with a false discovery rate set at 0.05 (ref. 15). Groups varied based on the demographic variable (race, insurance type, income and age) or the intersection of demographic variables being considered. P > 0.05 was considered not significant.

Confidence intervals. While reporting mean metrics, we estimated 95% CIs using all of the folds. To calculate the 95% CI across all folds, we pooled the mean from each fold, resampled the test set with replacement to maintain its original size and evaluated the selected model on the resampled test set, repeating this procedure over all folds. The resulting metrics were averaged to represent one point in the 95% confidence distribution. This process was repeated for 1,000 iterations (that is, 1,000 nonparametric bootstrap iterations), thus defining the bootstrap distribution for the metric. Subsequently, we calculated the 95% CI using this bootstrapped distribution14,15.

Correlation. To calculate correlations between variables, we used Spearman correlation coefficients implemented by scipy.stats.spearmanr17 (https://scipy.org). The Spearman correlation coefficient was calculated by18. The 95% CI for the Spearman correlation coefficient was calculated by converting to z-score using the method outlined by Lane19.

## Computing hardware and software

We used Python (version 3.8.13) and PyTorch100 (version 2.0.0, CUDA 11.7) (pytorch.org) for all experiments and analyses in the study. All downsampled experiments were performed on a 24-core server (64 GB, 390 GPU). All WSI processing was supported by OpenSlide (version 4.3.1), openslide-python (version 1.2.0) and CLAM (https://github.com/mahmoodlab/CLAM). Pillow (version 9.3.0) and OpenCV python were used to perform basic image processing tasks. We used scikit-learn101 (version 1.2.1) for its implementation of logistic regression. We used Scipy102 (version 1.11.4) to calculate correlation coefficients. Implementations of other visual pretrained encoders benchmarked in the study are available at the following links: ResNeST103, with ImageNet transfer (https://github.com/mahmoodlab/CLAM), C-TransPath

(github.com/Xiyue-Wang/TransPath) and UNI (https://arxiv.org/pdf/2308.15474.pdf). For extracting features, multi-GPU code was used to create plots and figures. Apyrx (version 1.2.0) and Pytorch for training weakly supervised ABML models, we adapted the training code from the CLAM codebase (https://github.com/mahmoodlab/CLAM). Matplotlib (version 3.7.1) and Seaborn (version 0.12.2) were used to create plots and figures. Apyrx (version 1.2.0) and Pytorch (version 1.5.3) were used for numerical operations. STAIN normalization was performed using SlideFlow104 (version 2.1.0). The code used for this study has been made publicly available at https://github.com/mahmoodlab/CPTATH. Demographics. Usage of other miscellaneous Python libraries is listed in the Reporting Summary.

## Reporting summary

Full-size Reporting Summary on research design is available in the Nature Portfolio Reporting Summary linked to this article.

## Data availability

Public data from TCGA, including digital histology and the clinical annotations used, are available at https://portal.gdc.cancer.gov/ and https://biocloud.org/. The EBRAINs brain tumor atlas can be accessed at https://www.brain-tumor-atlas-dataset.org/8606-2b34-406f-8999-0262adcf1994. Restrictions apply to the availability of the in-house data, which were used with institutional permission for the current study and are thus not publicly available. We note that these data are not available to the public. All other data, algorithms and code may be addressed to the corresponding author and will be promptly evaluated based on institutional and departmental policies to determine whether the data requested are subject to intellectual property or patentability requirements. Internal data can only be shared for non-commercial, academic purposes and will require a data user agreement.

## Code availability

All code was implemented in Python using PyTorch as the primary deep learning package. Code and scripts to reproduce the training experiments of this paper are available at https://github.com/mahmoodlab/CPTATH.

## References

1. Lipkova, J. et al. Artificial intelligence for multimodal data analysis.Front. Med.9, 1055–1110 (2022).
2. Lipkova, J. et al. Deep learning-enabled assessment of cardiac allograft rejection from endomyocardial biopsies.Nat. Med.28, 875–882 (2022).
3. Smith, E., Herzenn, M., Lesser, E., Ravichandran, D. & Kremers, W. Developing image analysis pipelines of whole-slide images: pre- and post-processing.J. Clin. Transl. Sci.6, e38 (2020).
4. 150. L. Lipkova, J. et al. Transformer-hierarchical vision transformer using shifted windows. InProc. 2021 IEEE/CVF International Conference on Computer Vision (ICCV) 9902–10002 (IEEE, 2021).
5. Chen, X., Xie, S. & He, K. An empirical study of training and evaluation of a self-supervised convolutional neural network.Proc. 2021 IEEE/CVF International Conference on Computer Vision (ICCV) (IEEE, 2021).
6. Dosovitskiy, A. et al. An image is worth 16×16 words: transformers for image recognition at scale. InProc. International Conference on Computer Vision (ICCV) (IEEE, 2020).
7. Oquab, M. et al. DINOv2: Learning robust visual features without supervision. InTransactions on Machine Learning Research 8535–8556 (TMLR, 2024).
8. 185. L. Lipkova, J. et al. Deep learning for digital histopathology with real-time whole-slide visualization. Preprint athttps://arxiv.org/abs/2304.04142(2023).
9. Kriegsmann, M. et al. Deep learning for the classification of small-cell and non-small-cell lung cancer.Cancers (Basel)12, 1604 (2020).

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

12

---

<!-- Page 23 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

156. Janßen, C. et al. Multimodal lung cancer subtyping using deep learning neural networks on whole slide tissue images and MALDI mass images (Basel, Switzerland). Nyctaginia 2023, 12, 1–12.

157. Celik, Y., Tala, M., Yildirim, O., Karatacak, M. & Acharya, U. R. Automated invasive ductal carcinoma detection based using deep transfer learning with whole-slide images. Pattern Recognit. 183, 222–229 (2020).

158. Han, Z. et al. Breast cancer multi-classification from histopathological images with structured deep learning model. Sci. Rep. 7, 4172 (2017).

159. Silek, Murthy, M., M. M. Balasubraman, V.P.S., Dudekula, D.B., Natarajan, S. & Park, J. Classification of benign and malignant subtypes of breast cancer histopathology imaging using hybrid CNN-LSTM based transfer learning. BMC Med. Imaging 23, 19 (2023).

160. Xiong, J. et al. Nystrom-Net: A Nyström-based algorithm for approximating self-attention. In Proc. AAAI Conference on Artificial Intelligence. Vol. 35 14138–14148 (Association for the Advancement of Computing Machinery, 2023).

161. Loshchilov, I. & Hutter, F. Decoupled weight decay regularization. International Conference on Learning Representations (2019).

162. Berrada, L., Zisserman, A. & Kumar, M. F. Smooth loss functions for top-k classification. In International Conference on Learning Representations (ICLR, 2018).

163. Jiang, H. & Nachum, O. Identifying and correcting label bias in machine learning. In Proc. 23rd International Conference on Learning Representations. Vol. 10272 (PMLR, 2020).

164. Chai, X. et al. Unsupervised domain adaptation techniques based on auto-encoder for non-stationary EEG-based emotion recognition. Comput. Biol. Med. 79, 205–214 (2016).

165. Fang, T., Lu, N., Niu, G. & Sugiyama, M. Rethinking importance weighting for deep learning under distribution shift. In Advances in Neural Information Processing Systems. Vol. 33 (eds. Larochelle, H. et al.) 11996–12001 (Curran Associates, 2020).

166. Youden, W. J. Index for rating diagnostic tests. Cancer 3, 32–35 (1950).

167. Ruopp, M. D., Perkins, N. J., Whitcomb, B. W. & Schisterman, E. F. Youden's index and the area under the ROC curve: implications affected by a lower limit of detection. Biom. J. 50, 419–430 (2008).

168. Wu, E. et al. How medical AI devices are evaluated: limitations and recommendations from an analysis of FDA approvals. Nat. Med. 28, 582–594 (2022).

169. American Cancer Society. Key statistics for breast cancer—how common is breast cancer? www.cancer.org/cancer/types/breast-cancer/about/how-common-is-breast-cancer.html (2024).

170. American Cancer Society. Key statistics for lung cancer—how common is lung cancer? www.cancer.org/cancer/types/lung-cancer/about/key-statistics.html (2024).

171. Kim, M. et al. Globlastoma is an age-related neurological disorder in adults. Neurooncol. Adv. 3, vab125 (2021).

172. Cao, J. Y., Wan, Y., Zhan, Z., Hong, X. & Yan, H. Epidemiology and risk stratification of low-grade gliomas in the United States, 2004–2018: a competing risk regression model for survival analysis. Front. Oncol. 13, 1079577 (2023).

173. scikit-learn developers. 1.1. Linear models. scikit-learn scikit-learn.org/stable/modules/linear_model.html (2022).

174. Phipson, B. & Smyth, G. K. Permutation P-values should never be zero: calculating exact P-values when permutations are randomly drawn. Stat. Appl. Gener. Mol. Biol. https://doi.org/10.2202/1544-1515.5185 (2010).

175. Ernst, M. D. Permutation methods: a basis for exact inference. Stat. Sci. 19, 676–685 (2004).

176. Fisher, R. The Design of Experiments Vol. 6 (Hafner, 1951).

177. Benjamin, Y. J. & Hochberg, Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. J. R. Stat. Soc. Ser. B Methodol. 57, 289–300 (1995).

178. Vritsen, P. et al. Soft-PL: A fundamental algorithm for scientific computing in Python. Nat. Methods 17, 261–272 (2020).

179. Lane, D. M. Confidence Interval on Pearson's Correlation (Rice Univ., 2018); onlinestatbook.com/2/estimation/correlation_ci.html

180. Frazzica, A. et al. PyTorch: an imperative style, high-performance deep learning library. In Advances in Neural Information Processing Systems Vol. 32 (eds. Wallach, H. et al.) 8026–8037 (Curran Associates, 2019).

181. Vritsen, P. et al. Scikit-learn: machine learning in Python. J. Mach. Learn. Res. 12, 2825–2830 (2011).

## Acknowledgements

This work was supported in part by the Brigham and Women's Hospital (BWH) Presidents Fund, BWH and Massachusetts General Hospital Pathology, and National Institute of General Medical Sciences R35GM138216 to F.W. R.J.C. was supported by the National Science Foundation Graduate Fellowship. YY was supported by the Takeda Fellowship. M.Y.L. was supported by the Siebel Scholars program. D.F.K.W. was supported by the National Institutes of Health/ National Cancer Institute Lung Cancer National Service Award (T32CA251062). The content is solely the responsibility of the authors and does not reflect the official views of the funding sources.

## Author contributions

A.V., R.J.C. and F.M. conceived the study. All authors designed the experiments. A.V., R.J.C., M.Y.L., D.F.K.W., T.Y.C., J.L. and M.S. performed data collection and cleaning. A.V. and R.J.C. conducted the experimental analysis with assistance from all coauthors. D.F.K.W. analyzed the misclassified cases. A.V., D.F.K.W., R.J.C., A.H.S., G.J., T.H., YY, E.C.D. and F.M. prepared the paper with input from all coauthors. F.M. supervised the research.

## Competing interests

The authors declare no competing interests.

## Additional information

Extended data is available for this paper at

https://doi.org/10.1038/s41591-024-02885-z.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41591-024-02885-z.

Correspondence and request for materials should be addressed to Faissal Mahmood.

Peer review information Nature Medicine thanks Jakob Kather and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Primary Handling Editor: Lorenzo Righetto, in collaboration with the Nature Medicine team.

Reprints and permissions information is available at www.nature.com/reprints.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 24 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Extended Data Fig. 1 | Effects of data processing strategies on disparities in breast subtyping. Race stratified subtyping ROC curves and true positive rate disparity for ABMIL models for breast subtyping trained on TCGA BRCA (n = 1,049 cases) and tested on MGB-breast (n = 1,265 slides) with: A, B. ResNet504 patch encoder; E, F. CTransPath patch encoder; I, J. UN1 patch encoder. In each case, the ABMIL model was trained using different strategies: (i) 20-fold Monte Carlo splits (A, E, I) (ii) 10-fold site-preserving splits (B, F, J) (iii) 10-fold site-preserving splits and stain-normalized features (C, G, K) (iv) With stain normalization and site-preserving folds. ABMIL is tested on unbiased test cohorts (1,000 white, 1,000 Black, and 1,000 Asian slides, with 500 slides per sub-type for each race) (D, H, L). ROC curves show mean curve (n = 10 folds) for site-stratified splits and n = 20 folds for Monte Carlo splits with 95% CIs. Boxes indicate quartile values of True Positive Disparity (n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits) with the center being 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P-value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 2.

Extended Data Fig. 1 | Effects of data processing strategies on disparities in breast subtyping. Race stratified subtyping ROC curves and true positive rate disparity for ABMIL models for breast subtyping trained on TCGA BRCA (n = 1,049 cases) and tested on MGB-breast (n = 1,265 slides) with: A, B. ResNet504 patch encoder; E, F. CTransPath patch encoder; I, J. UN1 patch encoder. In each case, the ABMIL model was trained using different strategies: (i) 20-fold Monte Carlo splits (A, E, I) (ii) 10-fold site-preserving splits (B, F, J) (iii) 10-fold site-preserving splits and stain-normalized features (C, G, K) (iv) With stain normalization and site-preserving folds. ABMIL is tested on unbiased test cohorts

(1,000 white, 1,000 Black, and 1,000 Asian slides, with 500 slides per sub-type for each race) (D, H, L). ROC curves show mean curve (n = 10 folds) for site-stratified splits and n = 20 folds for Monte Carlo splits with 95% CIs. Boxes indicate quartile values of True Positive Disparity (n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits) with the center being 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P-value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 2.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 25 -->

Article

https://doi.org/10.1038/s41591-024-02848-z

Extended Data Fig. 2 | Effects of data processing strategies on disparities in lung subtyping. Rose stratified lung subtyping ROC curves and corresponding PRD plots for ABMIL models for lung subtyping trained on TCCA-lung (n = 1,043 slides) and tested on MGB-lung (n = 1,960 slides) with: A, D, ResNet50, patch encoder for B, E, CTranPath patch encoder F, I, LUN patch encoder. In each case, the ABMIL model was trained using different strategies: (i) 20-fold Monte Carlo splits (A, E, I) (ii) 10-fold site-preserving splits (B, F, J) (iii) 10-fold site-preserving splits and stain-normalized features (C, G, K) (iv) With stain normalization and site-preserving folds, ABMIL is tested on unbiased test cohorts (1,000 white, 1,000 Black, and 1,000 Asian slides, with 500 slides per subtype for each race) (D, H, L). ROC curves show AUC values: n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits with 95% CI. Boxes indicate quartile values of TPDR disparity (n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits) with the center being 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P-value from nonparametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 3.

Extended Data Fig. 2 | Effects of data processing strategies on disparities in lung subtyping. Rose stratified lung subtyping ROC curves and corresponding PRD plots for ABMIL models for lung subtyping trained on TCCA-lung (n = 1,043 slides) and tested on MGB-lung (n = 1,960 slides) with: A, D, ResNet50, patch encoder for B, E, CTranPath patch encoder F, I, LUN patch encoder. In each case, the ABMIL model was trained using different strategies: (i) 20-fold Monte Carlo splits (A, E, I) (ii) 10-fold site-preserving splits (B, F, J) (iii) 10-fold site-preserving splits and stain-normalized features (C, G, K) (iv) With stain normalization and site-preserving folds, ABMIL is tested on unbiased test cohorts (1,000 white,

1,000 Black, and 1,000 Asian slides, with 500 slides per subtype for each race) (D, H, L). ROC curves show AUC values: n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits with 95% CI. Boxes indicate quartile values of TPDR disparity (n = 10 folds for site-stratified splits and n = 20 folds for Monte Carlo splits) with the center being 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P-value from nonparametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 3.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 26 -->

Article

https://doi.org/10.1038/s41591-024-02885-x

Extended Data Fig. 3 Effects of data processing strategies on disparities in IDH1 mutation prediction. Base stratified (A, D, G) and true positive case disparity for ABMIL models for IDH1 mutation prediction trained on EBRANIS brain tumor atlas (n = 873 slides) and tested on TCGA-GMBLLGG cohort (n = 1,123 slides) with A-C, ResNe50 feature encoder D-F. CTransPath patch encoder G-I. UN1 match encoder. In each case, the ABMIL model was trained using different strategies: (I) 20-fold Monte Carlo splits (A, D, G) (ii) ABMIL trained using stain-normalized features (B, E, H) (iii) with stain normalization, ABMIL is tested

on unbiased test cohorts (1,000 white, 1,000 Black, and 1,000 Asian, with 500 slides per class for each case) (C, E, I). Boxes indicate quartile values (n = 20 folds) with 95% CI. Boxes indicate quartile values of TPDR disparity (n = 20 folds) with the center being 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 4.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 27 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Extended Data Fig. 4 | Effect of stain normalization on disparities. Race stratified ROC curves and true positive rate disparity for ABMIL model trained in 20-fold study ResNet50n and UNI patch encoders with Macenkin stain normalization for A, breast subtyping B, lung subtyping C. IDH1 mutation prediction. ABMIL trained on TCGA-BRCA (n = 1,049 slides) and TCGA-lung (n = 1,043 slides) cohorts for breast and lung subtyping and tested on resampled MGB breast lung cohorts. Respectively, for IDH1 mutation prediction, ABMIL trained on EBrains (n = 873 slides) and tested on resampled TCGA-GBMLGG. All

unbiased test cohorts have 1,000 white, 1,000 Black, and 1,000 Asian slides, with 500 slides per class for each race. Boxes indicate quartile values of TPR disparity (n = 20 folds) with the center being 50th percentile. Whiskers extend to data points within 1.5× the interquartile range. Each dot in the box plots represents a unique model trained for one of the cohorts. P-value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Table 2–4.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

2

---

<!-- Page 28 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Extended Data Fig. 5 displays the performance of ABMIL models across three cancer types (Breast, Lung, and BPH) and three tasks (Subtyping, Subtyping, and Mutation prediction). The figure is organized into three panels (A, B, and C), each showing ROC-AUC performance for different models pre-trained on natural images and histology images.

Panel A: Breast subtyping

| Model | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | White | Black | Overall | Asian | White | Black | Overall | Asian |
| ResNet50 10 (10 3 ) | ~0.92 | ~0.85 | ~0.88 | ~0.82 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (10 3 ) | ~0.95 | ~0.92 | ~0.93 | ~0.91 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| CTransPath (15-10 3 ) | ~0.92 | ~0.88 | ~0.90 | ~0.85 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (16-10 3 ) | ~0.95 | ~0.92 | ~0.93 | ~0.91 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni (100-10 3 ) | ~0.98 | ~0.95 | ~0.96 | ~0.94 | ~0.98 | ~0.95 | ~0.96 | ~0.94 |

Panel B: Lung subtyping

| Model | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | White | Black | Overall | Asian | White | Black | Overall | Asian |
| ResNet50 10 (10 3 ) | ~0.92 | ~0.85 | ~0.88 | ~0.82 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (10 3 ) | ~0.95 | ~0.92 | ~0.93 | ~0.91 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| CTransPath (15-10 3 ) | ~0.92 | ~0.88 | ~0.90 | ~0.85 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (16-10 3 ) | ~0.95 | ~0.92 | ~0.93 | ~0.91 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni (100-10 3 ) | ~0.98 | ~0.95 | ~0.96 | ~0.94 | ~0.98 | ~0.95 | ~0.96 | ~0.94 |

Panel C: BPH mutation

| Model | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on natural images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images | Pre-trained on histology images |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | White | Black | Overall | Asian | White | Black | Overall | Asian |
| ResNet50 10 (10 3 ) | ~0.75 | ~0.65 | ~0.70 | ~0.60 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (10 3 ) | ~0.85 | ~0.75 | ~0.80 | ~0.70 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| CTransPath (15-10 3 ) | ~0.85 | ~0.75 | ~0.80 | ~0.70 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni- (16-10 3 ) | ~0.85 | ~0.75 | ~0.80 | ~0.70 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |
| Uni (100-10 3 ) | ~0.95 | ~0.92 | ~0.93 | ~0.91 | ~0.95 | ~0.92 | ~0.93 | ~0.91 |

Extended Data Fig. 5 | Effect of pre-training dataset size on demographic disparities. Race-stratified and overall ROC AUC for ABMIL models with patch encoders pre-trained on natural images and histology image datasets of varying sizes for: A breast subtyping, B lung subtyping, C IDH1 mutation prediction. All models were trained on 20-fold Monte Carlo splits on TCGA-BRCA (n = 1,049 slides), TCGA-Lung (n = 1,043 slides), and EBRAINS brain tumor atlas (n = 873 slides) and tested on resampled MGB-breast, MGB-lung, and TCGA-GBMLGG (1,000 white, 1,000 black, and 1,000 Asian slides, with 500 slides per class for each race) for breast subtyping, lung subtyping, and IDH1 mutation prediction, respectively. The number of images used for pre-training of each encoder is shown in brackets under the encoder name. Refer to Methods for details of each encoder. Error bars in bar plots indicate 95% CI, with the center being the mean value (n = 20 folds).

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 29 -->

Article

[https://doi.org/10.1038/s41591-024-02885-z](https://doi.org/10.1038/s41591-024-02885-z)

Figure 6 displays the demographic stratified performance of internal validation cohorts, showing ROC curves and True Positive Rate (TPR) disparity across different cancer types and subtypes.

Panel A: Breast subtyping (Train set = TCGA, Test set = TCGA). The ROC curve shows an Overall AUC of 0.903 ± 0.009. The TPR disparity box plot shows mean values for IDC (White: 0.900 ± 0.008, Black: 0.911 ± 0.007, Asian: 0.888 ± 0.006) and ILC (White: 0.900 ± 0.008, Black: 0.911 ± 0.007, Asian: 0.888 ± 0.006).

Panel B: Lung subtyping (Train set = TCGA, Test set = TCGA). The ROC curve shows an Overall AUC of 0.956 ± 0.005. The TPR disparity box plot shows mean values for LUAD (White: 0.960 ± 0.004, Black: 0.950 ± 0.004, Asian: 0.916 ± 0.020) and LUSC (White: 0.960 ± 0.004, Black: 0.950 ± 0.004, Asian: 0.916 ± 0.020).

Panel C: Breast subtyping (Train set = MGB, Test set = MGB). The ROC curve shows an Overall AUC of 0.847 ± 0.008. The TPR disparity box plot shows mean values for IDC (White: 0.835 ± 0.006, Black: 0.867 ± 0.004, Asian: 0.971 ± 0.004) and ILC (White: 0.835 ± 0.006, Black: 0.867 ± 0.004, Asian: 0.971 ± 0.004).

Panel D: Lung subtyping (Train set = MGB, Test set = MGB). The ROC curve shows an Overall AUC of 0.956 ± 0.006. The TPR disparity box plot shows mean values for LUAD (White: 0.971 ± 0.004, Black: 0.920 ± 0.006, Asian: 0.965 ± 0.004) and LUSC (White: 0.971 ± 0.004, Black: 0.920 ± 0.006, Asian: 0.965 ± 0.004).

Extended Data Fig. 6 | Demographic stratified performance of internal validation cohorts. Race stratified breast and lung subtyping ROC curves and true positive rate disparity for ABMIL models trained and tested on: (A) TCGA BRCA (B) TCGA lung (C) MGB breast (D) MGB lung. To create training splits, 25 examples from each subtype were sampled 10 times to create 10 folds, and the rest of the data was used for validation. ABMIL with UNIPatch encoder used. ROC curves show mean (n = 10 folds) with 95% CI. Boxes indicate

quartile values of TPR disparity (n = 10 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plot represents a unique model trained for one of the folds. P value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for each task in Supplementary Data Tables 2 and 3.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 30 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Extended Data Fig. 7 | Investigating breast subtyping disparities beyond race. TPR disparity was assessed in various demographic subgroups of the TCGA GBMLGG test cohort (n = 1,123 slides) for ABMIL model trained with UNI features on the EBRAINS brain tumor atlas cohort (n = 873 slides) in a 20-fold study for IDH1 mutation prediction. A. TPR disparity for different race groups. B. The TPR disparity is computed for white IDH1 wild-type (WT) and mutant (MT) patients (n = 983 slides), stratified by age. C. TPR disparity for different age groups (years). D. The TPR disparity is computed for IDH1 wild-type and mutant

patients aged \leq 40 (n = 303 slides), stratified by race. Boxes indicate quartile values of TPR disparity (n = 20 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained in one of the folds. P value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for the task in Supplementary Data Table 4.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 31 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

A Income: Low (blue), Middle (pink), High (yellow). P-values: IDC (Low vs. Middle: P=0.004, Low vs. High: P=0.002), ILC (Middle vs. High: P=0.026, Middle vs. Low: P=0.026).

B Race: White (blue), Asian (pink), Black (yellow). P-values: IDC (White vs. Asian: P=0.001, White vs. Black: P=0.001, Asian vs. Black: P=0.001), ILC (White vs. Asian: P=0.001, White vs. Black: P=0.001, Asian vs. Black: P=0.001).

C Insurance type: On Medicare (blue), Not on Medicare (pink). P-values: IDC (On vs. Not: P=0.001), ILC (On vs. Not: P=0.001).

D Age: < 62 (blue), \geq 62 (pink). P-values: IDC (P=0.001), ILC (P=0.001).

E Race: White (blue), Asian (pink), Black (yellow). P-values: IDC (White vs. Asian: P=0.001, White vs. Black: P=0.001), ILC (Asian vs. Black: P=0.002, White vs. Black: P=0.003, White vs. Asian: P=0.002).

F Insurance type: On Medicare (blue), Not on Medicare (pink). P-values: IDC (On vs. Not: P=0.001), ILC (On vs. Not: P=0.002, P=0.003, P=0.001).

G Income: Low (blue), Middle (pink), High (yellow). P-values: IDC (Low vs. Middle: P=0.001, Low vs. High: P=0.001), ILC (Low vs. Middle: P=0.001, Low vs. High: P=0.001).

H Age: < 62 (blue), \geq 62 (pink). P-values: IDC (P=0.005), ILC (P=0.001).

I Insurance type: On Medicare (blue), Not on Medicare (pink). P-values: IDC (P=0.001), ILC (P=0.001).

J Income: Low (blue), Middle (pink), High (yellow). P-values: IDC (Low vs. Middle: P=0.001, Low vs. High: P=0.001), ILC (Low vs. Middle: P=0.001, Low vs. High: P=0.001).

K Age: < 62 (blue), \geq 62 (pink). P-values: IDC (P=0.001), ILC (P=0.001).

Extended Data Fig. 8 | Investigating IDH1 mutation prediction disparities beyond race. TPR disparity was assessed in various demographic subgroups of the MGB-breast test cohort (n = 1,265 slides) for ABML model trained with UN patch encoder on the TCGA-BRCA cohort (n = 1,049 slides) in a 20-fold study for breast subtyping. A, TPR disparity for different postal code inferred income groups. (B–D) The TPR disparity is computed for subgroups of IDC and ILC patients from low-income postal codes (n = 407 slides), stratified by other demographic variables. B, Racial groups. C, Insurance groups. D, Age groups (years). E, TPR disparity for different racial groups. (F–H) The TPR disparity is computed for subgroups of the white IDC and ILC patients (n = 904 samples),

stratified by other demographic variables. F, Insurance groups. G, Income groups inferred from postal code. H, Age groups. (I–K) The TPR disparity is computed for subgroups of the Black IDC and ILC patients (n = 164 samples), stratified by other demographic variables. I, Insurance groups. J, Income groups inferred from postal code. K, Age groups (years). Boxes indicate quartile values of TPR disparity (n = 20 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. P value from non-parametric two-sided paired permutation test after multiple hypothesis correction presented. Demographic distributions for the task in Supplementary Data Table 2.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

10

---

<!-- Page 32 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Figure 9 displays stain distributions by races for different scanners, comparing Hue and Saturation across three racial groups (White, Asian, Black) using two different scanners (Aperio GT 450 and Hamamatsu S210).

Hue (A, B, C): Hue distributions are shown for the Overall, Aperio GT 450, and Hamamatsu scanners. For each scanner, the distributions are compared across White, Asian, and Black racial groups. The y-axis represents Hue values ranging from 70 to 190.

Saturation (D, E, F): Saturation distributions are shown for the Overall, Aperio GT 450, and Hamamatsu scanners. For each scanner, the distributions are compared across White, Asian, and Black racial groups. The y-axis represents Saturation values ranging from 100 to 220.

In all plots, the box plots represent the median, quartiles, and range of the data, with individual data points (whiskers and outliers) shown. The distributions generally show a shift in hue and saturation values across the racial groups, with the Black group often showing higher values than the White group.

Extended Data Fig. 9 | Stain distributions by races for different scanners. For both the MGB-breast and lung cohorts, we randomly sampled 50 slides per scanner and per race, segmented the tissue from background, and patched the tissue into 256 \times 256 tiles at 20\times magnification. We sampled 1,000 patches from each slide, converted them from RGB to HSV space, and calculated their average hue and saturations. We compare the distributions of hue and saturation by race for A. Overall MGB-breast cohort B. Slides in MGB-breast cohort scanned on Aperio GT 450 scanner C. Slide in MGB-reast cohort scanned on Hamamatsu S210 scanner. We compare the distributions of hue and saturation by race for D.

Overall MGB-lung cohort E. Slides in MGB-lung cohort scanned on Aperio GT 450 scanner F. Slide in MGB-lung cohort scanned on Hamamatsu S210 scanner. We do not find any statistically significant difference in the hues or saturations of whole slide-images by race for both scanners and overall category as compared by two-sided non-parametric paired permutation tests. Boxes indicate quartile values of metric shown by respective axis (n = 50 whole slide images) with the center being the 50th percentile. Whiskers extend to data points within 1.5\times the interquartile range. Each dot represents a unique slide.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 33 -->

Article

https://doi.org/10.1038/s41591-024-02885-z

Extended Data Fig. 10 | Effect of resampling sample size on TPR disparities.

We trained ABMIL models with UNI patch encoder on 20-fold Monte Carlo splits on TCGA BRCA and lung subtyping and EBRADNG/IDH1 mutation prediction and tested them on original and resampled MGB-breast and lung and TCGA GBMLGG cohorts, respectively. We show different resampling variants of the test set (no resampling/ original, 500 and 1,000 slides per class and per race) for A. breast

subtyping B. lung subtyping C. IDH1 mutation prediction. Resampling is done for each disease class and race (See Methods for more details). Boxes indicate quartile values of TPR disparity (n = 20 folds), with the center being the 50th percentile. Whiskers extend to data points within 1.5x the interquartile range. Each dot in the box plots represents a unique model trained for one of the folds. Demographic distributions for the task in Supplementary Data Table 2–4.

Nature Medicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 34 -->

nature portfolio

nature portfolio | reporting summary

Corresponding author(s): Faisal Mahmood

Last updated by author(s): 12/3/2024

## Reporting Summary

Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist.

### Statistics

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.

n/a Confirmed

- The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
- A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
- The statistical test(s) used AND whether they are one- or two-sided
- Only common tests should be described solely by name; describe more complex techniques in the Methods section.
- A description of all covariates tested
- A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
- A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
- For null hypothesis testing, the test statistic (e.g.F,t,r) with confidence intervals, effect sizes, degrees of freedom andPvalue noted
- GivePvalues as exact values whenever suitable.
- For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
- For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
- Estimates of effect sizes (e.g. Cohen'sd, Pearson'sr), indicating how they were calculated

Our web collection on statistics for biologists contains articles on many of the points above.

### Software and code

Policy information about availability of computer code

| Data collection | Packages used for data collection and processing were: Python (version 3.8.13), openSlide-python (version 1.2.0), Pillow (version 9.3.0), scikit-learn (version 1.2.1), and CLAM ( http://github.com/mahmoodlab/CLAM ) for WSI processing. |
| --- | --- |
| Data analysis | We used Python (version 3.8.13) and PyTorch (version 2.0.0, CUDA 11.7) ( pytorch.org ) for all experiments and analyses in the study. All downstream experiments were performed on three 24GB NVIDIA 3090 GPUs. All WSI processing was supported by OpenSlide (version 4.3.1), openSlide-python (version 1.2.0), and CLAM ( github.com/mahmoodlab/CLAM ), Pillow (version 9.3.0) and OpenCV-python (version 4.5.3.56) were used to perform basic image processing tasks. We use Scikit-learn (version 1.2.1) for its implementation of logistic regression. We used Scipy (version 1.11.4) to calculate correlation coefficients. Implementations of other visual pretrained encoders benchmarked in the study are found at the following links: ResNet50In with ImageNet Transfer ( github.com/mahmoodlab/CLAM ), CTranPath ( github.com/Xiyue-Wang/TranPath ) and UNI ( https://arxiv.org/pdf/2308.15474.pdf ). For training weakly-supervised ABML models, we adapted the training code from the CLAM codebase ( github.com/mahmoodlab/CLAM ). Matplotlib (version 3.7.1) and Seaborn (version 0.12.2) were used to create plots and figures. Numpy (version 1.24.4) and pandas (version 1.5.3) were used for numerical operations. Stain normalization was done using slideflow (version 2.1.0). The code used for this study has been made publicly available at: https://github.com/mahmoodlab/path_demographics.git |

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information.

Content courtesy of Springer Nature, terms of use apply. Rights reserved

April 2023

1

---

<!-- Page 35 -->

# Data

## Policy information about availability of data

All manuscript sets must include a data availability statement. This statement should provide the following information, where applicable:

- - Accession codes, unique identifiers, or web links for publicly available datasets
- - A description of any restrictions on data availability
- - For clinical datasets or third party data, please ensure that the statement adheres to ourpolicy

Public data from TCGA including digital histology and the clinical annotations used are available from https://portal.gdc.cancer.gov/ and https://cbioportal.org. EBRAINS Brain Tumor can be accessed from https://search.kg.ebrains.eu/instances/Dataset/8fC108ab-e2b4-406f-8999-60269cd1f994. For academic use of raw and processed in-house MGB data, please email email@taylorandfrancis.com for Restrictions to apply to the availability of the MGB data, which were used with institutional permission for the current study, and are thus not publicly available. All requests will be promptly evaluated based on institutional and departmental policies to determine whether the data requested are subject to intellectual property or patient privacy obligations. Data can only be shared for non-commercial academic purposes and will require a data user agreement.

## Research involving human participants, their data, or biological material

Policy information about studies with human participants or human data. See also policy information about sex, gender (identity/presentation), sexual orientation and race, ethnicity and racism.

### Reporting on sex and gender

Patient sex was not considered in the study design, but for describing the datasets used (both public and private sets), self-reported patient sex (male/female) is disaggregated and presented in Supplementary Data Tables 2–4. No sex-based a priori analysis was done. The terms sex and gender have not been used interchangeably in the study. No individual-level patient sex data has been shared.

### Reporting on race, ethnicity, or other socially relevant groupings

Socially relevant variables were considered in the study to determine whether AI-driven computational pathology algorithms perform well across different demographic groups.

The socially relevant variables considered include:

- - Self-reported patient race: White, Black or African American (abbreviated to Black), Asian, Other/Non-reporting. This information is available for TCGA-Breast, Lung, and GBMLGG datasets (https://www.cbioportal.org) and Mass-General Brigham Breast and Lung sets. EBRAINS Brain Tumor Atlas does not report patient race. Terms race and genetic ancestry are not used interchangeably.
- - Self-reported patient age at the time of diagnosis:- Breast cancer: Patients were grouped into (1) < 62 (2) ≥ 62. This is done because the median age of breast cancer patients is 62 (https://www.cancer.org/cancer/types/breast-cancer/about/how-common-is-breast-cancer.html).- Lung cancer: Patients were grouped into (1) < 70 (2) ≥ 70. This is done because the median age of lung cancer patients is 70 (https://www.cancer.org/cancer/types/lung-cancer/about/key-statistics.html).- Gliomas: Patients were grouped into (1) < 40 (2) ≥ 40 and < 60 (3) ≥ 60. This is done because of the varied age prevalences of Low-Gliomas and Glioblastomas (https://pubmed.ncbi.nlm.nih.gov/34647022/) and (https://pubmed.ncbi.nlm.nih.gov/36937939/)-text#The%20incidence%20rate%20of%20malignant,for%20trafritation%20of%20LowGGs.)- Patient age is available for all datasets considered (TCGA:https://www.cbioportal.org, EBRAINS Brain Tumor Atlas:https://search.kg.ebrains.eu/instances/Dataset/8fC108ab-e2b4-406f-8999-60269cd1f994).- Self-reported patient insurance type: If patients were on Medicare, they were grouped into a category “On Medicare”, otherwise, “Not on Medicare”. This information is only available on the private Mass-General Brigham datasets.- Self-reported postal-code inferred income: Patient reported postal code, in conjunction with US Census data (accessed fromhttps://jpyl.org/project/uspicedoe), is used to infer patient income. The Methods section and the main manuscript clearly identify that postal-code has been used to infer patient income. Patients were grouped into three categories based on the 33rd and 66th percentiles of postal-code inferred income per dataset. This information is only available for the private Mass-General Brigham datasets. We use postal code to infer income because postal code is available via the patient medical data, whereas income is not.
- - Breast cancer: Patients were grouped into (1) < 62 (2) ≥ 62. This is done because the median age of breast cancer patients is 62 (https://www.cancer.org/cancer/types/breast-cancer/about/how-common-is-breast-cancer.html).
- - Lung cancer: Patients were grouped into (1) < 70 (2) ≥ 70. This is done because the median age of lung cancer patients is 70 (https://www.cancer.org/cancer/types/lung-cancer/about/key-statistics.html).
- - Gliomas: Patients were grouped into (1) < 40 (2) ≥ 40 and < 60 (3) ≥ 60. This is done because of the varied age prevalences of Low-Gliomas and Glioblastomas (https://pubmed.ncbi.nlm.nih.gov/34647022/) and (https://pubmed.ncbi.nlm.nih.gov/36937939/)-text#The%20incidence%20rate%20of%20malignant,for%20trafritation%20of%20LowGGs.)
- - Patient age is available for all datasets considered (TCGA:https://www.cbioportal.org, EBRAINS Brain Tumor Atlas:https://search.kg.ebrains.eu/instances/Dataset/8fC108ab-e2b4-406f-8999-60269cd1f994).
- - Self-reported patient insurance type: If patients were on Medicare, they were grouped into a category “On Medicare”, otherwise, “Not on Medicare”. This information is only available on the private Mass-General Brigham datasets.
- - Self-reported postal-code inferred income: Patient reported postal code, in conjunction with US Census data (accessed fromhttps://jpyl.org/project/uspicedoe), is used to infer patient income. The Methods section and the main manuscript clearly identify that postal-code has been used to infer patient income. Patients were grouped into three categories based on the 33rd and 66th percentiles of postal-code inferred income per dataset. This information is only available for the private Mass-General Brigham datasets. We use postal code to infer income because postal code is available via the patient medical data, whereas income is not.

Patients disaggregated into socially relevant groups is presented in Supplementary Data Tables 2–4. Forming of patients groups is described in detail in Methods.

### Population characteristics

Population characteristics for all datasets used in the study are reported in Supplementary Data Tables 2–4.

### Recruitment

No patient recruitment was necessary for using histology whole slide images retrospectively and routine clinical data. No participants received any form of compensation.

### Ethics oversight

Brigham and Women’s Hospital IRB committee approved the study, approval: 2020P000233.

Note that full information on the approval of the study protocol must also be provided in the manuscript.

nature portfolio | reporting summary

April 2023

2

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 36 -->

# Field-specific reporting

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.

 Life sciences  Behavioural & social sciences  Ecological, evolutionary & environmental sciences

For a reference copy of the document with all sections, see nature.com/documents/reporting-summary-flat.pdf

## Life sciences study design

All studies must disclose on these points even when the disclosure is negative.

| Sample size | Public datasets utilized in this study (TCGA and EBRANS Brain Tumor Atlas) have predefined sample sizes. However, for the private Mass-General Brigham cohorts, our sample size was determined based on the availability of high-quality diagnostic histology slides and clinical data. This information was obtained through a query of our entire in-house Mass-General Brigham database of pathology slides, covering the period from 2016 to 2022. As the performance of deep learning models often improves with more data, our goal was to incorporate as many eligible patients as possible. No other statistical sample size calculations were performed. Please refer to Supplementary Data Tables 2-4 for specific sample size details. |
| --- | --- |
| Data exclusions | Data exclusion criteria were: 1. Slides that did not have a lower magnification downsampling for segmenting, processing the tissue image. 2. Slides that did not have any tumor content (as verified by board certified anatomic pathologists). 3. Cases with missing slides were excluded. Cases with blurry scans were not excluded but rescaned. |
| Replication | Our training, test protocols and all code has been made publicly available for additional evaluation and reproducibility and may be accessed at https://github.com/mahmoodlab/CPATH_demographics . UN, CTranPATH weights are publicly available. |
| Randomization | For training models, two strategies were used: 1. Label stratified splits: For subtyping and mutation prediction tasks, we split the training dataset in 20 label-stratified folds (90:10 train-validation splits), to ensure similar distributions of labels in training and validation across folds. This is in line with the community standards of data splitting. 2. Label and site stratified training: For each subtyping task, we split the TCGA datasets while preserving the sites into 10:90 train-validation splits, i.e. cases from one site are not in both training and validation folds. The splits were also stratified by the label. Since EBRANS Brain Tumor Atlas does not provide patient source site, site-stratified training could not be performed. |
| Blinding | All relevant patient data from public and private datasets was collected before training and testing deep learning models, hence blinding was not possible and necessary. Board certified pathologist performing subjective evaluations of mis-classified lung subtyping cases from the Mass-General Brigham cohort was blinded to the patient race and task label and was asked to diagnose the patient following clinical standards and collected routine clinical data such as grade and whether IHC was required for diagnosis. |

## Reporting for specific materials, systems and methods

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.

| Materials & experimental systems | Methods |
| --- | --- |
| n/a | n/a |
| Involved in the study | Involved in the study |
| Antibodies | Chip-seq |
| Eukaryotic cell lines | Flow cytometry |
| Palaeontology and archaeology | MRI-based neuroimaging |
| Animals and other organisms |   |
| Clinical data |   |
| Dual use research of concern |   |
| Plants |   |

nature portfolio | reporting summary

April 2023

3

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 37 -->

## Terms and Conditions

Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH ("Springer Nature").

Springer Nature supports a reasonable amount of sharing of research papers by authors, subscribers and authorised users ("Users"), for small-scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use ("Terms"). For these purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.

These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription (to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will apply.

We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as detailed in the Privacy Policy.

While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may not:

1. 1. use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access control;
2. 2. use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is otherwise unlawful;
3. 3. falsely or misleadingly imply or suggest endorsement, approval, sponsorship, or association unless explicitly agreed to by Springer Nature in writing;
4. 4. use bots or other automated methods to access the content or redirect messages
5. 5. override any security feature or exclusionary protocol; or
6. 6. share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal content.

In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue, royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any other, institutional repository.

These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.

To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law, including merchantability or fitness for any particular purpose.

Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed from third parties.

If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not expressly permitted by these Terms, please contact Springer Nature at

onlineservice@springernature.com