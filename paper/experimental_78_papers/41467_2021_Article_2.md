<!-- Page 1 -->

nature

COMMUNICATIONS
ARTICLE
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)
OPEN

# The impact of site-specific digital histology signatures on deep learning model accuracy and bias

Frederick M. Howard 1, James Dolezal1, Sara Kochanny1, Jefree Schulte 2, Heather Chen2, Lara Heij 3,4, Dezheng Huo 5,6, Rita Nanda 1,6, Olufunmilayo I. Olopade 1,6, Jakob N. Kathe7,8,9, Nicole Cipriani 2,6, Robert L. Grossman1,6,10 & Alexander T. Pearson 1,6,10

The Cancer Genome Atlas (TCGA) is one of the largest biorepositories of digital histology. Deep learning (DL) models have been trained on TCGA to predict numerous features directly from histology, including survival, gene expression patterns, and driver mutations. However, we demonstrate that these features vary substantially across tissue submitting sites in TCGA for over 3,000 patients with six cancer subtypes. Additionally, we show that histologic image differences between submitting sites can easily be identified with DL. Site detection remains possible despite commonly used color normalization and augmentation methods, and we quantify the image characteristics constituting this site-specific digital histology signature. We demonstrate that these site-specific signatures lead to biased accuracy for prediction of features including survival, genomic mutations, and tumor stage. Furthermore, ethnicity can also be inferred from site-specific signatures, which must be accounted for to ensure equitable application of DL. These site-specific signatures can lead to overoptimistic estimates of model performance, and we propose a quadratic programming method that abrogates this bias by ensuring models are not trained and validated on samples from the same site.

1Section of Hematology/Oncology, Department of Medicine, University of Chicago, Chicago, IL, USA. 2Department of Pathology, University of Chicago, Chicago, IL, USA. 3Department of Surgery and Transplantation, University Hospital RWTH Aachen, Aachen, Germany. 4Institute of Pathology, University Hospital RWTH Aachen, Germany. 5Department of Public Health Sciences, University of Chicago, Chicago, IL, USA. 6University of Chicago Comprehensive Cancer Center, Chicago, IL, USA. 7Department of Medicine III, University Hospital RWTH Aachen, Aachen, Germany. 8Pathology and Data Analytics, Leeds Institute of Medical Research at St James's, University of Leeds, Leeds, UK. 9Medical Oncology, National Center for Tumor Diseases, University Hospital Heidelberg, Heidelberg, Germany. 10Email: rgrossman@uchicago.edu; apearson@medicine.bsd.uchicago.edu

NATURE COMMUNICATIONS | (2021)12:4423 | 
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)
 | 
[www.nature.com/naturecommunications](http://www.nature.com/naturecommunications)
1

---

<!-- Page 2 -->

ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

A standard component of the diagnosis of nearly all human cancers is the histologic examination of hematologic and eosin-stained tumor biopsy sections. Histologic characteristics identified by pathologists help characterize tumor subtypes, prognosis, and at times can predict response to treatment1. Quantification of more subtle pathologic features can further discriminate between good and poor prognosis tumors, such as the quantification of tumor-infiltrating lymphocytes in breast cancer, but such detailed analysis can be time-consuming and variable between pathologists2,3. The increasing availability of digital pathology artifacts and the development of image recognition has led to computational approaches to rigorously assess pathologic correlates associated with a variety of tumor-specific features. Deep learning is a subdomain of artificial intelligence, referred to as deep learning, that uses machine learning to identify increasingly higher-order image characteristics to allow for the accurate identification of features of interest. Deep learning in digital histology has been used to recognize status4 to identify standard histologic features such as grade5–9, mitosis10,6, and invasion8–10. Recently, deep learning approaches have been applied to identify less apparent features of interest, including clinical biomarker receptor status11, tumor microenvironment12, microsatellite instability10,11, or the presence of pathogenic virus in cancer12. These approaches have been further extended to infer more complex features of tumor biology directly from pathology images, including gene expression, pathogenic mutations, and tumor heterogeneity. The predictive accuracy of many of these models has been validated in external datasets, but studies often rely on single-data sources13 and both internal and external validation.

The Cancer Genome Atlas (TCGA) has been critical for the development of deep-learning histology models, containing over 20,000 digital slide images from 24 tumor types, along with associated clinical, genomic, and radiomic data. Due to the propensity of machine learning algorithms to overfit, performance is typically reported in a reserved testing set or evaluated with cross-validation, and both internal and external validation14. However, the overfitting of digital histology models to site-level characteristics has been incompletely characterized and is infrequently accounted for in the internal validation of deep learning models. The genome-wide cancer atlas (GCA) is a large-scale, throughput sequencing endeavora have been well-characterized, and are the product of the hundreds of tissue source sites contributing samples and the multiple sites for genome sequencing and data centerization. The GCA is a unique resource that contains characteristic signatures unique to each tissue submitting site (Fig. 1). Prior to sectioning, tissue is first fresh-frozen or fixed in formalin and embedded in paraffin. Each slide is then scanned and generates unique artifacts23. Slides are then stained with the eponymous hematoxylin and eosin stains, the color and intensity of which can vary based on the specific stain formulation and the amount of time each stain is applied. The digitization of slides may then vary due to scanner calibration and choice of resolution and magnification24,25. Finally, histologic characteristics of tumors can differ between sites to account for differences in specimens between the patients treated at different centers. Thus, differences in specimen acquisition, staining, digitization, and patient demographics all contribute to a unique site-specific digital histology signature, which could in turn lead to a lack of generalizability of digital image models.

Several methods have been proposed to eliminate these site-specific signatures to improve the validity of histology image analysis, primarily through correction for differences in slide staining between institutions26. This includes methods designed to reduce color variation across images proposed by Reinhard et al.27, and methods designed specifically for histology by Macenko et al.28. Color augmentation (Fig. 1), where the color

channels of images are altered at random during training to prevent a model from learning stain characteristics of a specific site have also been utilized in histology deep-learning tasks29,30. Most assessments of stain-normalization and augmentation techniques have focused on the performance of models in validation sets, rather than true elimination of the site-specific signature that may lead to model bias31,32. Here, we describe the clinical and slide-level variability between sites in TCGA that constitute site-specific digital histology signatures, and methods to ensure robust use of internal and external validation to minimize false-positive findings with deep learning image analysis.

## Results

Characterization of clinical and digital image heterogeneity in TCGA. Important clinical variables differ across tissue slides submitted to TCGA. Figure 1A shows the recognized prevalence of outcomes and survival vary across sites for a number of cancers33, but even more fundamental factors differ depending on submitting organization. We compared the distribution of basic demographic characteristics of age, ancestry, gender, and body weight index and tumor-specific factors such as stage and histologic subtype. Sites were included for comparison if they submitted at least 20 tissue slides to TCGA. We found that the distribution of all demographic characteristics as well as estrogen receptor status (n = 969), progesterone receptor status (n = 966), HER2 expression (n = 847), PAM50 subtype (n = 914), TP53 mutational status (n = 1010), and tumor stage (n = 1010) varied by year-prognostic survival (n = 458)34 varied significantly between cohorts, with false discovery rate correction and P < 0.05 (Fig. 2). We systematically evaluated the impact of each major site characteristic types, and demonstrate that multiple impactful clinical features vary by the site for all tumor subtypes tested—including ALK fusion status in squamous cell lung cancer (LUSC-TCGA cohort, n = 112) and human papillomavirus (HPV) status in head and neck squamous cell carcinoma (HNSC TCGA cohort, n = 332)—all with P < 0.05 and significant after FDR correction (Supplementary Table 3). In addition, we found that the distribution of the increasing interest in developing survival models based on pathology, stage varied by the site in all cancer subtypes tested, and 3-year survival was significantly different across the sites in all cancers, except lung and colorectal adenocarcinoma.

We then applied classical descriptive statistics for image analysis to document the differences in slide image characteristics across cancer types, tumor subtypes, and second-order Haralick texture features for comparison across sites35,36. All first- and second-order statistics demonstrated variance according to tissue type and cancer type, as measured by the ANOVA F-statistic (Fig. 3 and Supplementary Table 2). Similar findings were seen in the analysis of other cancer subtypes (Supplementary Fig. 2). Applying stain-normalization techniques at a slide level to tissue samples from the same cancer type did not alter the measures of dissimilarity for all second-order characteristics (as measured by F-statistic) remained greater than that of any first-order characteristics (Fig. 4 and Supplementary Table 2). Of note, the stain-normalization techniques did not remove the most dissimilar image characteristic (highest F-statistic) with any form of stain normalization for all cancer types, except lung and head and neck squamous cell carcinoma (Supplementary Table 2 and Supplementary Fig. 2).

Deep-learning algorithms accurately identify tissue submitting site. To assess the ability of deep learning to predict tissue submitting site, we trained a deep-learning convolutional neural network based on CXception architecture to predict site37. To

2

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

---

<!-- Page 3 -->

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

ARTICLE

Fig. 1 ETLs of site-specific digital histology signatures, and methods for correction. The submitting institution of a digital histology image can often be readily detected due to a site-specific signature unique to each institution. A number of factors can contribute to site-specific signatures, ranging from true histologic and biologic differences between batches of histologic artifacts termed batch effect. The batch effect can originate from every step from the procurement of tissue to digital image creation. Frozen and formalin-fixed specimens will have unique histologic artifacts, the intensity of hematoxylin and eosin exposure can vary between institutions, and the digitization of slides may result in compression artifacts. A variety of methods have been developed to mitigate the impact of stain differences between slides. Stain normalization refers to changes in color characteristics to reduce the effect of staining differences between slides. Augmentation refers to random variations applied to individual tiles during machine learning to prevent overfitting with regards to the varied characteristic.

assess the accuracy of site prediction, we used threshold cross-validation stratified by site (Fig. 5a) and calculated the one-versus rest area under the receiver-operating characteristic (AUROC) curve (Supplementary Table 2). The slide characteristics used by such a model to predict site can be illustrated with a UMAP visualization of final layer activations, with representative slide tiles selected for each UMAP coordinate26—in this case, demonstrating a hematoxylin-predominant to eosin-predominant color gradient for patients in TCGA-BRCA (n = 1006, Fig. 5b). To assess the ability of stain normalization and color augmentation to prevent prediction of site, we repeated this process with normalization or augmentation applied at the tile level across six examined cancer subtypes (Supplementary Table 3). Site discrimination was highly accurate at baseline, with an average one-versus- (OVR) area under the receiver-operating characteristic curve (AUROC) ranging from 0.999 for clear cell renal cancer (TCGA-KIRC, n = 508) to 0.964 for TCGA-LUSC (n = 463). For comparison, AUROC for a neural network model trained to predict site from the clinical characteristics described in Supplementary Table 1 achieved an average AUROC of 0.935, ranging from 0.511 in TCGA-LUSC to 0.781 in TCGA-COADREAD (Supplementary Table 4). Stain-normalization techniques modestly decreased the accuracy of site prediction, but stain normalization remained highly accurate with an average OVR AUROC of over 0.850 with all normalization techniques for all cancers. For all cancer subtypes tested, the greatest decline in AUROC for site prediction was seen with one of the two forms of grayscale normalization. To further evaluate how stain normalization

influences model inference of site, a UMAP and mosaic representation of TCGA-BRCA site prediction after Macenorm normalization was generated, which did not demonstrate as clear a color gradient (Supplementary Fig. 4a). The most clearly separable site (A7—Chirians) in this UMAP remains the same in both plots—suggesting that either subtle stain-related differences persist, or other components of its unique digital histology signature continue to render this site unique from others.

An artificial simulation of site-specific digital histology signatures. As described earlier, there are a variety of putative causes of site-specific signatures in digital histology (Fig. 1) that may contribute to highly accurate detection of the tissue submitting site for a slide. To better describe the relationship between biological factors (such as true differences between populations) and batch effect (i.e., nonbiologic differences between histologic images), we designed a simulation of site-specific signatures using patients from the University of Pittsburgh, the largest contributor to the TCGA dataset. We simulated a 15-ER-positive, n = 23 ER-negative. A single site was chosen as this would theoretically minimize any batch effect due to site-related differences in sample procurement, staining, or digitization. We assessed the ability of deep-learning models to identify 23 random slides from within a cohort of 69 patients while introducing both a biologic cofounder (ER status) and stain-related confounder—representing two different contributors to a site-specific signature. ER status was chosen as the biologic cofounder as it is highly detectable from

NATURE COMMUNICATIONS | (2022)13:44167 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

3

---

<!-- Page 4 -->

ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

Fig. 2 Demographics and tumor characteristics of breast cancer across sites with 20 or more slides in TCGA. Each row represents a demographic, clinical, or tumor characteristic of patients in TCGA-BRCA. The chi-squared test was performed to quantify heterogeneity between sites, with the listed P values corrected for a false discovery rate of 0.05. A number of features display marked heterogeneity—for example, only two sites (ILSBio and Christiana) submitted patients where the majority had disease progression within 3 years. IGC, International Genomics Consortium; MSKCC, Memorial Sloan Kettering Cancer Center; GPCC, Greater Poland Cancer Center; EUR, European; ARF, African; AMR, Native American; IDC, invasive ductal carcinoma; ILC, invasive lobular carcinoma.

histology, and the University of Pittsburgh dataset has a reasonable number of positive and negative samples. We varied the ER negativity of the 23 target slides from 0 to 100%, whereas the remainder of the slides were maintained as ER-positive (Supplementary Fig. 5, Supplementary Table 5). Similarly, we applied an artificial staining artifact to 0–100% of the target slides, whereas the remainder of the slides were unaffected. While the accuracy of target feature prediction increased monotonically when the target feature became more strongly ER-negative, this relationship no longer held as the stain artifact was applied to more slides. In addition, stain-normalization techniques did not shroud the impact of the artificial stain artifact, with a reduction from an AUROC of 1.00 when 100% of target slides had staining artifact, down to a minimum AUROC of 0.934 with grayscale stain normalization. The accuracy at baseline and reduction with grayscale normalization were more strongly ER-negative, with site prediction, further suggesting that batch effect, as opposed to biologic subpopulation differences, are the predominant cause of highly accurate site prediction by deep-learning models.

Preserved-site cross-validation—a quadratic programming solution. Naturally, if a deep-learning model can distinguish sites based on nonbiologic differences between staining patterns and slide acquisition techniques, models designed to predict certain clinical variables could instead learn staining variability or other site-specific features that is analogous to the Huxley versus Wolf problem, where a deep-learning model distinguishes

pictures of these two canines based on the fact that more wolves are pictured in the snow—rather than physical differences between the two animals, leading to a potential lack of external validity39. A similar problem can also occur if true biologic subpopulation differences (rather than batch effect) are correlated with the outcome of interest, but only in specific sites. To evaluate the dependence of deep-learning model accuracy on site-specific digital histology signatures, we propose comparing models trained to assess features of interest across two different methods of cross-validation (Fig. 5c). We can correct for biased results by ensuring sites are isolated to a single data fold, or preserved site cross-validation. However, if submitting sites within a dataset are randomly split into equal-sized groups for cross-validation, it is likely that a feature of interest would not be evenly represented among these groups, resulting in biased estimates of accuracy40. Optimal cross-validation methods for cross-validation while isolating each site to an individual k-fold can be achieved using convex optimization/quadradic programming41. In other words, an optimization problem can be constructed with the goal of equipping the proportion of patients with/without a feature of interest across each fold. We applied this method of cross-validation to all outcomes listed in Fig. 2 and Supplementary Table 1. Notably, our method of preserved site cross-validation produces perfect stratification (all subgroups with identical distribution to standard cross-validation) in 55% (32/58) of outcomes tested (Supplementary Table 6). Meaningful imbalances, where the distribution of patients differed from perfect stratification by over 10 for a subgroup in any fold was seen in 12% (7/

4

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

---

<!-- Page 5 -->

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

ARTICLE

Fig. 3 Variation of image characteristics in breast cancer digital histology across TCGA. Sites contributing at least 50 slides are included (n = 607 slides, 7 sites), demonstrating that image variation is not solely a function of small sites that infrequently contributed to the TCGA. a First-order characteristics for red, green, and blue are shown in their respective colors. b Haralick second-order textural features also vary by submitting site. STD: standard deviation, ASM: angular second moment, GPC: Greater Poland Cancer Center.

58) of outcomes. All of these meaningful imbalances occurred in the TCGA-COADREAD dataset, where a smaller number of sites contributed to patients.

Impact of site-specific digital histology signatures on deep-learning model performance. To further characterize the influence of site-specific signatures on deep-learning model performance, we trained convolutional neural network models with standard and preserved-site cross-validation to predict the previously described demographic, clinical, and genomic outcomes across six cancer subtypes using the dataset splits as highlighted in Supplementary Tables 3 and 4. For 58 features evaluated, the average decrease in AUROC between standard and preserved-site cross-validation was 0.069 (range: -0.042 to 0.291). We assessed which models had a significant decline in performance using a one-sided t-test, and again repeated this assessment with stain-normalization and augmentation techniques, using an FDR of 0.05 for significance testing. Of the 56 features which were predictable with standard cross-validation, 51 (91.1%) had a decline in AUROC with preserved-site cross-validation, and 20 (35.7%) were no longer significantly detectable (Fig. 6a and Supplementary Tables 7 and 8). A similar proportion of predictable features had a decline in AUROC with other methods of stain normalization/augmentation, ranging 84.6% with grayscale (Fig. 6b) to 89.1% with heavy HSV augmentation. Interestingly, the percentage of features that are no longer accurately detected with preserved-site cross-validation decreased modestly with normalization/augmentation, ranging from 17.5% with Macenko normalization to 26.8% with Reinhard normalization.

Of demographic features, the proportion of genomic ancestry42 prediction declined drastically with preserved-site cross-validation in a number of disease subtypes regardless of normalization/augmentation, including TCGA-BRCA (n = 905, AUROC 0.798 versus preserved-site AUROC of 0.507, P < 0.001), TCGA-

COADREAD (n = 483, AUROC 0.883 versus 0.795, P < 0.001), and TCGA-LUSC (n = 422, AUROC 0.789 versus 0.504, P < 0.001). Accuracy of age prediction in the TCGA-COADREAD cohort also declined with preserved-site validation (n = 541, AUROC 0.605 versus 0.479, P < 0.001), as did stage prediction in both lung cancer cohorts (TCGA-LUSC n = 474, AUROC 0.537 versus 0.466, P < 0.001; TCGA-LUAD n = 468, AUROC 0.599 versus 0.521, P < 0.001). As one might expect—these demographic features are often as strongly indicative of disease outcome as pure biologic factors—and outcome prediction demonstrated a significant impact of site-specific signatures in multiple disease cohorts. Performance declined significantly for prediction of 3-year PFS in the TCGA-LUSC (n = 227, AUROC 0.589 versus 0.485, P < 0.001) and TCGA-HNSC (n = 272, AUROC 0.614 versus 0.548) cohorts.

The detection of standard histologic features was less perturbed by preserved-site cross-validation with no difference in accuracy with the prediction of HER2 status in TCGA-BRCA and of grade in TCGA-HNSC. Other histologic features remained largely unaffected by preserved-site cross-validation—with minimal decreases in AUROC—including prediction of lobular surface ductal histology in TCGA-BRCA, prediction of estrogen, and progesterone receptor status in TCGA-BRCA and prediction of grade in TCGA-KIRC. Prediction of mucinous histology for TCGA-COADREAD, however, did decline with preserved-site cross-validation at baseline (n = 578, AUROC 0.788 versus 0.712, P < 0.001) and with all forms of normalization/augmentation. Nonetheless, this decline was not dramatic and mucinous histology remained detectable with preserved-site cross-validation.

This has been increasing interest in using deep learning to detect non-intuitive features directly from histology, including our previously described work on detection of genetic driver mutations directly from histology15—raising the question of

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

5

---

<!-- Page 6 -->

ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

Fig. 4 | ANOVA F-statistics for first- and second-order image characteristics for breast cancer histology in TCGA. Variance in first- and second-order image characteristics between tissue submitting sites in the breast cancer TCGA dataset (n = 888 slides over 14 sites) is assessed with ANOVA. The ANOVA F-statistic is listed for multiple methods of stain normalization, with the lowest F-statistic (least variability) with any method of normalization indicated in the rightmost column. Stain normalization does not completely resolve first-order stain variability (by F-statistic), and minimal impact is seen on second-order Haarlet features. STD, standard deviation, ASM, angular second moment.

whether the accurate prediction of some of these features in TCGA may be due to recognition of site-specific signatures rather than histologic characteristics driven by these mutations. We analyzed a subset of the driver mutations that were accurately predicted in our previous work and found that the majority were unaffected/initially unaffected by preserved-site validation, including TP53 and MAP2K4 in TCGA-BRCA, BRAF in TCGA-COADREAD, TP53 in TCGA-HNSC, and STK11 and TP53 in TCGA-LUAD. However, several mutations were no longer accurately detectable, including PIK3CA in TCGA-LUSC (n = 458, AUROC 0.614 versus 0.386, P < 0.001), RHOA in TCGA-HNSC (n = 443, AUROC 0.733 versus 0.470, P < 0.001), and RNPS3 in TCGA-COADREAD (n = 556, 0.688 versus 0.494, P < 0.001). The detection of other genomic features was also dependent on site-specific signatures, including ALK fusion detection in lung cancer (TCGA-LUSC, n = 270, AUROC 0.678 versus 0.404, P < 0.001), TCGA-LUAD (n = 231, AUROC 0.637 versus 0.417, P < 0.001) and immune subtype23 detection in half of the cancers analyzed.

To further explore why some features exhibit a decline in accuracy, we produced a UMAP and mosaic map of two features in TCGA-BRCA: (1) ancestry, which correlates with site and declined substantially in accuracy (Supplementary Fig. 4b); and (2) BRCA mutational status, which correlates poorly with site and remained detectable in preserved-site cross-validation (Supplementary Fig. 4c). Although the most readily identifiable site (A7, Christiania Healthcare) clusters closely in both, it is not as distinctly separate from other sites in the BRCA UMAP, and is a less clear color gradient with BRCA as opposed to ancestry

prediction. This suggests that site-specific histologic patterns weigh less heavily in the decision-making for BRCA mutational status, whereas they may contribute to the prediction of ancestry, resulting in the marked decline in preserved-site cross-validation.

We can further demonstrate that models are weighting the unique histologic pattern of individual sites in making predictions by evaluating model performance within specific sites, where patient demographics do not match the overall dataset (Supplementary Fig. 6). We take as an example the slides submitted by the University of Chicago for TCGA-BRCA, the only site where patients of African ancestry comprise the majority of samples. We hypothesized that false-positive predictions of genomic African Ancestry24 would be significantly higher with standard cross-validation than with preserved-site cross-validation, models with standard cross-validation may for example learn that the University of Chicago staining pattern is associated with a high rate of African Ancestry. However, for patients in this dataset, data folds, false-positive predictions for African ancestry (measured at the tile level, n = 2206 tiles, 20 patients, 17 with African ancestry, 3 with European ancestry) are significantly higher with standard cross-validation balanced by ancestry, as compared to preserved-site cross-validation (Fig. 6b and Supplementary Table 9). In other words, standard cross-validation in TCGA-BRCA classifies European patients from a site with predominant African ancestry, as the decision is likely related to nonbiologic site-specific signatures in this tissue repository.

## Discussion

We have demonstrated that site-specific digital histology signatures exist within TCGA across diverse cancer types, and inadequately controlling for the ease in which deep-learning models detect site results in biased estimates of accuracy. Although normalization can resolve some of the perceptual variation and augmentation can mask differences in color, second-order image characteristics are unaffected by these methods, and stain normalization does not resolve the ability of models to detect site-specific features in a tissue or site. When predicting demographic, clinical, and genetic features with preserved-site validation, a consistent decrease in accuracy is seen despite perfect stratification of features of interest by site. This suggests that models are identifying the perceptivity of features and is absent for most features with a clear histologic basis such as tumor histologic subtype and grade. Conversely, we demonstrate that models are accurately identifying relevant features such as progression-free survival for squamous lung cancer and head and neck cancer, as well as genomic features such as certain driver mutations, ALK fusion status, and immune gene expression for certain cancers, are significantly driven by site-specific signatures—despite any form of normalization/augmentation.

Demographic features have a less straightforward histologic basis, and are more likely to be imperfect that some of the detected from histology. For example, young age is correlated with high-grade tumors and older age associated with lobular histology in breast cancer25. A clear biologic link between ethnicity and cancer risk is not yet identified in breast cancer—with higher tumor grade, more frequent triple-negative receptor status, and recurrent genetic differences in genome-wide association studies characterizing American and Asian breast cancer26,27. However, we demonstrated that deep-learning models trained on multisite repositories such as TCGA may base predictions on the histologic signatures of submitting sites, rather than intrinsic tumor biology, when these site-specific signatures are correlated with the outcome of interest. Demographic features

6

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | nature.com/naturecommunications

---

<!-- Page 7 -->

NATURE COMMUNICATIONS | 
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)

ARTICLE

Figure 5 consists of three panels (a, b, c) illustrating the model development process for site and feature prediction in TCGA.

Panel a: A workflow diagram for training and validation. On the left, a vertical bar labeled 'TCGA-BRCA' is split into three sections (1, 2, 3) by a '3-Fold Split Stratified by Site'. Each section contains five colored segments representing Site 1 (blue), Site 2 (yellow), Site 3 (orange), Site 4 (green), and Site 5 (purple). Arrows from sections 1 and 2 point to a computer icon labeled 'Training', and an arrow from section 3 points to a computer icon labeled 'Validation'. An arrow from the validation computer points to a box labeled 'Site'.

Panel b: A UMAP representation of the final activation weight vector. The plot shows a dense cloud of points on the left, with a clear gradient of color towards the right. A horizontal bar at the top is divided into two regions: 'Hematoylin-dominant' (purple) and 'Eosin-dominant' (pink). A legend on the left shows 'Site Code' with colored dots for sites AC, AJ, AL, AU, AV, AO, AD, AB, BH, and a 'Cell Code' with colored dots for cells CD, DB, EB, EN, EW, GM, GL, LL, OL, PE, PL, and S3.

Panel c: A workflow diagram for feature prediction. On the left, a vertical bar labeled 'TCGA-BRCA' is split into three sections (1, 2, 3) by a '3-Fold Split Stratified by Feature'. Each section contains two segments representing 'Feat. A' (blue) and 'Feat. B' (grey). An arrow from section 3 points to a vertical bar labeled 'TCGA-BRCA' which is split into three sections (1, 2, 3) by a '3-Fold Split Preserved Sites'. This bar contains five colored segments (Site 1 to Site 5) and two grey segments (Feat. A and Feat. B). Arrows from sections 1 and 2 point to a computer icon labeled 'Training', and an arrow from section 3 points to a computer icon labeled 'Validation'.

Fig. 5 Model development for the site and feature prediction for patients in TCGA. a To predict tissue submitting site, data is split into threefolds, with each site represented equally in all folds. Cross-validation is then performed, where a model is trained on two of the datasets and performance is assessed on the third dataset. This process is repeated threefold for an averaged performance metric. b UMAP representation of final activation weight vector of the model trained to recognize submitting site in TCGA-BRCA (n = 1006 slides). Each point on the left figure represents the centroid tile from a single slide. The nearest tile to each UMAP coordinate is visualized on the right, demonstrating a clear gradient from tiles that demonstrate predominant hematoylin staining to those demonstrating predominant eosin. c We assess the impact of including slides from a tissue submitting site within both the training and validation sets on the prediction of a variety of clinical, genomic, and demographic features, using two methods of generating folds for cross-validation. First, we split the data into threefolds, stratifying by the feature of interest, irrespective of site. For a comparator, we split the data into threefolds where each site is isolated into a single fold, with the secondary objective of equalizing the ratio of features in each fold.

such as genomic ancestry, which varies greatly from site to site due to differences in catchment areas of hospitals, may be particularly susceptible to such bias. This is evidenced by the fact that ancestry is predictable in TCGA-BRCA with standard but not preserved-site cross-validation, and predictive accuracy for ancestry declined significantly with preserved-site cross-validation for most cancer subtypes. This poses a challenging ethical

dilemma for the implementation of deep-learning histology models. It has been well documented that women of African ancestry with breast cancer have a poorer prognosis that is not completely accounted for by stage and receptor subtype48,49. Contributing factors may include delays in treatment initiation and inadequate intensity of therapy50, and more research is needed to disentangle the biologic and nonbiologic factors

NATURE COMMUNICATIONS | (2021)12:4423 | 
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)
 | 
[www.nature.com/naturecommunications](http://www.nature.com/naturecommunications)

7

---

<!-- Page 8 -->

ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

a

No Normalization

Correlated p-value

Decrease in AUROC with Preserved Site Validation

ALK, RHOA, PIK3CA, RNF43, ALK

Age, Stage, 3 Year PFS, Immune Subtype, Ancestry, Grade, Gender, Genetic Feature, Other

BRCA, COADREAD, LUAD, LUSC, HNSC, KIRC

b

Grayscale

Correlated p-value

Decrease in AUROC with Preserved Site Validation

ALK, RHOA, PIK3CA, RNF43, ALK

Age, Stage, 3 Year PFS, Immune Subtype, Ancestry, Grade, Gender, Genetic Feature, Other

BRCA, COADREAD, LUAD, LUSC, HNSC, KIRC

c

False Positive European Ancestry

False Positive African Ancestry

False Positive Ratio

Balanced by Ancestry, Preserved Sites

Baseline, Mutation, Promoter, Genebody, CopyNumber, CopyNumber Loss/Gen, HueSat HSV, HueSat HSV

Fig. 6 Impact of site-specific digital histology signatures on deep-learning model accuracy and bias. a The distribution of the average difference in AUROC with standard and preserved-site cross-validation for various clinical, genomic, and demographic features (n = 58 features) for six cancer subtypes in TCGA is shown (pictured graphic for baseline models without normalization/augmentation). The decrease in AUROC is statistically significant for a number of features (one-sided t-test, illustrated on y axis with false discovery correction, as described in Supplementary Table 7) for a subset of features. Jitter is added to ease visualization, although significance/insignificance of individual findings is preserved. b The same graph is provided for grayscale stain adjustment (for which the smallest changes in AUROC were seen). c False-positive prediction of European ancestry and African ancestry for patients within the University of Chicago dataset (measured at the tile-level: n = 2206 tiles from 20 patients, 17 with African ancestry, 3 with European ancestry) for models trained with standard and preserved-site cross-validation. The presented bars illustrate the proportion (e.g., the number of tiles falsely predicted to be European divided by the total number of tiles predicted to be European), with error bars signifying the estimated standard deviation of the proportions. PFS: progression-free survival, HSV: hue saturation value.

8

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

---

<!-- Page 9 -->

NATURE COMMUNICATIONS | (2022)13:4423 | https://doi.org/10.1038/s41467-021-24698-1

ARTICLE

contributing to disparities in prognosis. As deep-learning models are able to infer patient ancestry from site-specific signatures, models must be carefully implemented in an equitable fashion to avoid recapitulating the pre-existing inequities in cancer care61. Further study within single-site repositories, or repositories where tissue is stained and digitized at a single center, may promote more accurate modeling of demographic factors with deep learning.

When developing predictive histologic models for a large number of features, external validation of every finding can be impractical/infeasible. However, if the validation dataset has many features not be readily available for rare cancer subtypes. As such, multiple studies have trained and validated models using TCGA with no external validation or only partial validation in a sub-sample1,2,10,11,13,14,16,17,19,20,22,23,25,26,28,29,30,32,33,35,36,38,39,40,42,43,45,46,48,49,50,52,53,55,56,58,59,60,62,63,64,65,67,68,69,70,72,73,75,76,78,79,80,81,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988

---

<!-- Page 10 -->

ARTICLE

NATURE COMMUNICATIONS | 
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)

contained over three-fourths of available patients because one organization contributed the majority of samples where MSI status was known. However, for MSI status, poor stratification did not significantly affect performance when tested with preserved site cross-validation—consistent with the fact that MSI status has a well-proven histologic basis10. This limitation does not apply for majority of features evaluated, and preserved-site cross-validation can likely be applied to most multisite histology repositories.

Multiple methods for assessment of statistical significance have been proposed for TCGA data11,12, and we used the method proposed by Delong et al.6,7. However, application to the aggregate of predictions using Delong's method fails to capture the variance in predictive accuracy seen when training with different subsets of data. It is also not possible to apply Delong's method to all features as those we used for submitting site and stage prediction. Bootstrapping per se Hanley and McNeil13 is also highly utilized, but in a non-discriminatory manner. We used a bootstrap method in performance without bootstrapping. As the number of features we planned on analyzing grew, we updated our analytic plan to include bootstrapping as described to allow for reasonable estimates of significance. We also used a bootstrap method to mirror the methods of our group's prior work in genomic feature detection, allowing for better comparison to these results14.

Clearly, feature detection and analysis are two distinct differences, which is just one component of data contributors to the site-specific signatures seen in TCGA (Fig. 1). It is likely that some of the declines in performance seen with preserved-site cross-validation could be due to the inclusion of samples from processing, slide scanning, or subsampling differences between enrolling sites. For example, other studies describe that JPEG quality had a strong confounding effect on classification tasks in TCGA15. We attempted to minimize the influence of resolution on our findings by sampling slides on our deep-learning models at a fixed pixel to um ratio, but we did not directly assess the ability of our deep-learning models to capture differences in image findings support slide stain differences as a primary etiology of site-specific signatures in TCGA. First, a UMAP of final layer activations for site prediction as well as other highly affected features in TCGA revealed that the slides from different institutions (Fig. 5b). This suggests that stain variation is one of the most important distinguishing elements used in the prediction of these features, although there may be confounding between staining practices and stain differences. The basic first-order imaging characteristics such as average red, green, and blue values vary significantly between sites with all methods of stain normalization. However, the influence of these differences may still play a role in differentiation between sites. Nonetheless, second-order image characteristics vary more than these first-order characteristics—and further study of the impact of staining, choice of slide scanner, and method of sample acquisition on image characteristics can further elucidate the drivers of these differences. When varying both subsampling differences (ER status) and stain differences (ER status), the influence of slide staining abnormalities clearly predominates and reduces the impact of biologic differences on accuracy (Supplementary Fig. 5). Thus, when significant slide staining differences are present (as seen in Fig. 5b), the influence of biologic differences is likely minimal. Furthermore, the pattern of decline of the artificial stain shift mirrors what was seen with stain normalization for site detection (Supplementary Fig. 5). This suggests that the use of stain normalization does not eliminate the effect of stain differences. Although the etiology of the decline in performance with preserved-site validation is debatable, preserved-site cross-validation may provide valuable insight into performance on external datasets when site-specific staining,

scanning, specimen processing, and subsampling differences are present. However, it must be noted that preserved-site cross-validation has the potential to negate true biologic associations between histology and features of interest if these associations are only present in a single site. We have also only chosen a subset of proposed stain correction methods, but there have been other approaches that may further reduce the intrasite variability in TCGA. An alternative approach is to use a research-only stain that has been proposed, but did not outperform augmentation in test datasets15. Adversarial networks may also allow for models to be evaluated on a larger number of datasets.

In summary, we have demonstrated that digital histology in TCGA carries a multifactorial site-specific signature that is characteristic of the tissue submitting site. This signature can be used to predict the site of origin and can be used to assess overestimation of model accuracy if multiple sites are included in both the training and validation datasets. We have demonstrated that using a deep-learning model trained to the approach to accurately predict clinical findings ranging from progression-free survival, gene expression, genetic mutations, and ancestry with standard cross-validation. Care should be taken to describe the data contributors to the model. For cross sites, if significant, a submitting site should be isolated to either the cohort used for training or for testing a model. A quadratic programming approach can maintain optimal stratification while isolating submitting sites to either training or validation datasets.

## Methods

Patients: Patient data and whole-slide images were selected from six of the tumor types from TCGA with the highest number of slides available to better identify site-specific digital histology signatures. Tumor types included breast (BRCA), colon (COAD), liver (LIHC), lung (LUAD), and prostate (PRAD) (to both cohorts)16. Lung squamous cell carcinoma (USCC), lung adenocarcinoma (LUAD), and liver cell (LIHC), and head and neck squamous cell carcinoma (HNSCC)17. Slides and associated clinical data were accessed through the Genomic Data Commons Portal (https://portal.gdc.cancer.gov/). Ancestry was determined using the 24-way Ancestry panel18. The TCGA research and colleagues' data computation as described in their work19. Immune subtypes were determined from the TCGA research and colleagues' data computation was obtained from the participants in TCGA, and ethics oversight is described at https://www.cancer.gov/about-us/organization/research/structural-genomic/cg/ethics/history/policies.

Image processing and deep-learning model. Scanned whole-slide images of hematoxylin and eosin-stained tissue were acquired in SVS format from TCGA. Each slide was reviewed by a pathologist for tumor annotation of the site of the tumor using QuPath version 0.12 to ensure ink or other non-cancer artifacts did not interfere with the analysis. The tumor border and order and orientation of image characteristics, slides were downsampled to 5 microns per pixel and approximately 22x magnification. For deep-learning applications, the tumor region was segmented from the whole slide image, each with a resolution of 512x512x305 x 302 area of histology, effectively generating an optical magnification of 500x. The segmentation was performed using the Cellpose methodology that is available (https://doi.org/10.5281/zenodo.3699949). An average of 1% of slides was used for validation and testing (Supplementary Fig. 1 and Table 1). Convolutional neural networks models were written in Python 3.8 with Tensorflow 2.3.0, using the Xception model architecture20 pre-trained on the ImageNet database21. The final model was trained on the validation data. The final fully connected layer was a single layer with width 500, followed by a softmax layer for prediction. This architecture was trained on the validation data. The validation data was a subset of TCGA, a comparison of our findings to such studies14,22. Models were trained over 3 epochs of data, using the Adam optimizer23, with a learning rate of 10-4, a batch size of 128, and a learning rate decay of 1.2 with a single learning rate dropout. For the prediction of cancer sites using clinical tumor characteristics, we used a fully connected layer with width 500, with a single learning rate with a width of 500.

Each slide was labeled as a label associated with the outcome of interest. The libraries were also balanced by category to eliminate bias, with downsampling such that the number of sites for each target category was equivalent. Stain normalization and subsampling were performed using the methods of training data. The original Macenko and Reinhardt normalization is applied as previously described24 using a color space transformation to convert the images to grayscale and then to grayscale, and "grayscale normalized" refers to conversion to grayscale with histogram equalization25. Both light and heavy levels of hue saturation value (HSV) augmentation was applied, with light augmentation multiplying each of these three

10

NATURE COMMUNICATIONS | (2021)12:4423 | 
[https://doi.org/10.1038/s41467-021-24698-1](https://doi.org/10.1038/s41467-021-24698-1)
 | 
[www.nature.com/naturecommunications](http://www.nature.com/naturecommunications)

---

<!-- Page 11 -->

NATURE COMMUNICATIONS | (2023) 14:2293 | https://doi.org/10.1038/s41467-021-24668-1

ARTICLE

channels by a scalar from 0.9 to 1.1, and heavy augmentation multiplying the hue and saturation channels by a random scalar from 0.7 to 1.3. In addition, further augmentation through random shifts of the image is performed, and further image normalization ensures inputs have a mean of zero and a variance of one. Models are trained with threefold cross-validation, learning from two splits of the data and then evaluated on the third split (Supplementary Table 2). First-order statistics and evaluation was performed on 16 deep-learning-specific NVidia Tesla V100s graphical processing unit (GPU) nodes within a HIPAA-compliant environment.

Statistics and reproducibility. To quantify differences between categorical clinical features across sites, a chi-square test, a subtyping over 20 sites, with significance determined using a false discovery rate (FDR) of 0.05 with the Benjamini-Hochberg procedure (Supplementary Table 1) was performed, and further significance (Table 1). The 20 slide cutoff was chosen for these descriptive analyses to prevent variance metrics from being driven by sites submitting small numbers of slides that may be skewed by a small number of patient admissions. Second-order and degrees of freedom for each analysis is described in Supplementary Table 1. The variability in site-level metrics is quantified as the number of patient admissions per site, using the ANOVA F-statistic to measure variation for each individual image characteristic, with degrees of freedom equal to one less than the number of included sites, with the standard error (SE) in Table 2. First-order statistics are calculated from individual red, green, and blue pixel values across images, and include mean, standard deviation, skewness, kurtosis, and entropy, the latter being calculated as follows:

\text{Skewness} = \frac{m_3}{m_2^{3/2}} \quad (1)

\text{Kurtosis} = \frac{m_4}{m_2^2} \quad (2)

\text{Entropy} = N_i = \frac{m_i}{\sum_{j=1}^k m_j} \cdot \log_2 N_i \quad (3)

Where m_i = \sum_{j=1}^k m_j \cdot \log_2 N_i are calculated from the gray-level co-occurrence matrix P.

\text{Contrast} = \sum_{j=1}^k P_{j,j} \cdot (j - 1)^2 \quad (4)

\text{Dissimilarity} = \sum_{j=1}^k P_{j,j} \cdot |j - 2| \quad (5)

\text{Homogeneity} = \frac{255}{\sum_{j=1}^k P_{j,j}} \cdot I_{j,j} \quad (6)

\text{Angular smooth momentum} = \sum_{j=1}^k P_{j,j} \cdot j^2 \quad (7)

\text{Correlation} = \frac{255}{\sum_{j=1}^k P_{j,j}} \cdot \frac{(j - \mu)(j - \mu)}{\sigma^2 \sqrt{\sigma^2}} \quad (8)

Similar values for calculated features were seen for angles of 0°, 45°, 90°, and 135° so reported values for second-order features are averaged across these four angles. Second-order image characteristics were calculated using the photon statistic library, version 0.18.067.

Deep-learning models are assessed with the area under the ROC curve (AUROC), averaged over the threefolds generated for cross-validation. Confidence intervals and statistical testing were computed using a ×10 bootstrap experiment. For multivariate models (such as a prediction of the tissue submitting site of a slide, or prediction of Stage I vs II vs III disease), the reported AUROC values were averaged over AUROC, calculated using the Scikit-learn library, version 0.23.2.

For the prediction of tissue submitting sites, deep-learning models were trained using the aforementioned stratified cross-validation between average OVA, AUROC for prediction of site with different methods of stain normalization was performed. A two-fold cross-validation was performed with an FDR of 0.05, and comparisons to assess if average AUROC was greater than random chance (AUROC 0.50) were performed with a one-sided t-test with an FDR of 0.05 and two degrees of freedom (Supplementary Table 3).

Deep-learning models were also trained in a series of artificial experiments to predict a tissue submitting site with the University of Pennsylvania (100% of 115 ER-positive, \geq 33 ER-negative). Models were trained to detect 23 patients (100% of 115 ER-positive, \geq 33 ER-negative) and 100% of 115 ER-negative stain alteration (0–100%, as per Supplementary Fig. 5 and Supplementary Table 3). The stain alteration consisted of a 0.5% increase in hue, saturation, and value. These patients were combined with 46 ER-positive patients with no stain

alterations, and accuracy of prediction of the feature of interest was assessed with average AUROC with threefold cross-validation.

Accuracy for prediction of clinical features is reported with standard cross-validation—stratifying by site, and with preserved-site cross-validation—where each site is isolated to a single fold, and secondarily stratifying by the site. In other words, for standard cross-validation, all sites are merged into a single data set; each site is excluded with respect for site, such that classes are balanced and three equal folds are produced. Conversely, for preserved-site cross-validation, the dataset is divided into several folds, such that patients from a single site are all contained within the same fold. This split of sites is also selected to ensure the distribution of patients in each fold with respect to the outcome of interest is reflective of the larger population. To calculate k folds for preserved site cross-validation, the number of folds is equal to the number of patients in a single site, variable indicating if site i is a member of fold k, and n_{ij} is an integer indicating the number of samples from the site i in the categorical feature class j, then k seeks to minimize the mean square error in variance from perfect stratification:

\text{Error} = \sum_{i=1}^k \left( \frac{\sum_{j=1}^m n_{ij} \cdot \mu_{ij}}{\sum_{j=1}^m n_{ij}} - \left( \frac{\sum_{j=1}^m n_{ij}}{\sum_{i=1}^k n_{ij}} \right) \right)^2 \quad (9)

With the constraints that for all sites s:

\sum_{i=1}^k n_{is} = m_s \quad (10)

We used CPLEX v12.0, IBM to solve the optimal solution of Eqs. (9) and (10)68. Our code used for fold generation for preserved-site cross-validation is available from https://github.com/ncicb/ncicb.

We assess the impact of site-specific signatures on model accuracy across 58 features. For each feature, we trained a model with both standard and preserved-site validation—the cross-validation folds and sample sizes used in this assessment are listed in Supplementary Table 6. To assess if site-specific signatures reduce the performance of models, we used a one-sided t-test with four degrees of freedom to compare standard and preserved site cross-validated AUROCs. One-sided t-test was used to compare the difference in AUROC values between the two validation does not improve model accuracy. To assess if a model significantly improves performance with preserved-site validation, we used the one-sided methods of cross-validation are greater than random chance (0.50) using a one-sided t-test. For example, in some cases, a feature may be accurately predicted with no cross-validation, but not with preservation, but no decline in performance with grayscale normalization (as neither model can make any accurate predictions in grayscale). Both comparisons are performed for all methods of stain normalization, with an FDR of 0.05 for each feature analyzed (Supplementary Tables 7 and 8). Comparisons between the false-positive rates for African ancestry in TCGA-BRCA were performed using a one-sided t-test with one degree of freedom and an FDR of 0.05 (Supplementary Table 9).

To ensure reproducibility, the code used to support the main findings of this work was run in duplicate with equivalent results, including the subversion of sites into groups for cross-validation using the provided software.

Reporting summary. Further information on research design is available in the Nature Reporting Summary linked to this article.

## Data availability

Data for TCGA included digital histology and the clinical and genetic annotations available from https://portal.gdc.cancer.gov/. Annotations for immune subtypes are available from the published work of Thorsson et al.69 (https://doi.org/10.1038/s41586-017-01616-1; Immunomaster 0.023), and annotations for genomic ancestry are available from the work of Carare-Zaratz et al.70 (https://doi.org/10.1038/s41586-020-0412-0). Annotations for driver mutations are available from https://www.cancer.gov/ncicb/ncicb. All other results in support of this manuscript are available from the corresponding author upon reasonable request. Source data are provided with this paper.

## Code availability

Our code used for fold generation for cross-validation is available from https://github.com/fimhanson/PreservedSiteCV.

Received: 6 December 2020; Accepted: 1 July 2021

Published online: 20 July 2021

## References

1. 1. Carraga, M. T. & Henson, D. E. The histologic grading of cancer.Cancer70, 406–421 (1995).

NATURE COMMUNICATIONS | (2023) 14:2293 | https://doi.org/10.1038/s41467-021-24668-1 | www.nature.com/naturecommunications

11

---

<!-- Page 12 -->

ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

2. Salgado, R. et al. The evaluation of tumor-infiltrating lymphocytes (TILs) in breast cancer recommendations by an International TILs Working Group. Ann. Oncol. 26, 1633–1640 (2015).

3. Bulwen, W. et al. Automated deep-learning system for Gleason grading of prostate cancer using biopsies: a diagnostic study. Lancet Oncol. 21, 233–241 (2020).

4. Couture, H. D. et al. Image analysis with deep learning to predict breast cancer for mitotic detection, histologic subtype, and intrinsic subtype. npj Breast Cancer 4, 1–8 (2018).

5. Saha, M., Chakrabarty, C. & Racoceanu, D. Efficient deep learning model for mitotic detection using a multi-scale architecture. IEEE Access 7, 11939–11947 (2019).

6. Alomairi, S. et al. Aggregating histological learning from crowds for mitosis detection in breast cancer histology images. IEEE Trans. Med. Imaging 35, 1313–1321 (2016).

7. Iliuta, S. et al. Deep learning models for histopathological classification of gastric and colonic epithelial tumours. Sci. Rep. 10, 1504 (2020).

8. Alomairi, S. et al. Accurate prediction of breast cancer histology detection in whole-slide images: a deep learning approach for quantifying tumor extent. Sci. Rep. 7, 46450 (2017).

9. Alomairi, S. et al. Sharing intelligence algorithms to assess hormonal status from tissue microarrays in patients with breast cancer. JAMA Netw Open 2, e1979700 (2019).

10. Eiche, A. et al. Clinical-grade detection of microsatellite instability in colorectal tumors by deep learning. GenetomeMed 10, doi:10.1055/s-00000020-0201 (2020).

11. Kather, J. N. et al. Deep learning can predict microsatellite instability directly from histology in gastrointestinal cancers. Nat. Med. 25, 1054–1056 (2019).

12. Kather, J. N. et al. Deep learning detects virus presence in cancer histology. Preprint arXiv:1609.07100 (https://doi.org/10.1101/690206) (2016).

13. Schmitt, R. et al. Deep learning for the prediction of cancer expression of tumours from whole slide images. Nat. Commun. 11, 3877 (2020).

14. Kather, J. N. Integrating histological and genomic data for cancer expression morphology via deep learning. Nat. Biomed. Eng. 4, 827–834 (2020).

15. Radler, L. & Stencel, E. Identifying transcriptional correlates of histology using deep learning. PLoS ONE 15, e0232858 (2020).

16. Kather, J. N. et al. Pan-cancer image-based detection of clinically actionable gene alterations. Nat. Cancer 1–11, https://doi.org/10.1038/s41508-020-0087-6 (2020).

17. Coudray, N. et al. Classification and mutation prediction from non-small-cell lung cancer histopathology images. Nat. Med. 24, 1559–1567 (2018).

18. Dey, D. D. et al. Deep learning of Digital Slide Archive: an information system to support integrated in silico analysis of TCGA pathology data. J. Am. Med. Inf. Assoc. 20, 1099–1108 (2019).

19. Eche, A. et al. Deep learning in cancer pathology: a new generation of clinical biomarkers. Br. J. Cancer 111; https://doi.org/10.1038/s41416-020-01122-x (2020).

20. Chao, J.-H., Hong, S.-E. & Woo, H. G. Pan-cancer analysis of systematic batch effects in somatic sequence variations. BMC Nucleic Acids 18, 1–10 (2017).

21. Koh, W. B., Wang, Y. & Zhou, B. Deep learning with effective genomic data, and how to avoid them. Trends Microbiol. 35, 498–507 (2017).

22. Tom, J. A. et al. Identifying and mitigating batch effects in whole genome sequencing data. BMC Bioinformatics 17, 1–11 (2016).

23. Katherjee, S. Artifacts in histopathology. J. Oral. Maxillofac. Pathol. 18, S111 (2016).

24. Kotzki, S. et al. Removing batch effects from histopathological images for enhanced cancer diagnosis. IEEE J. Biomed. Inform. Hist. 18, 765–772 (2014).

25. Fu, J. et al. Pan-cancer cross-tissue histopathology reveals mutations, tumor composition and prognosis. Nat. Cancer 1, 800–810 (2020).

26. Komura, D. & Ishikawa, S. Machine learning methods for histopathological image analysis. Comput. Struct. Biomech. J. 16, 34–42 (2019).

27. Kather, J. N. & Alomairi, S. et al. A unified color transfer between histology images. IEEE Computer Graphics 21, 34–41 (2019).

28. Maeneno, M. et al. A method for normalizing histology slides for quantitative analysis in 2009. IEEE Computer Graphics 28, 1–10 (2009).

29. Mao, Z. & Mao, H. 11700 (IEEE, 2009. https://www.nature.com/articles/s41467-021-24697-y).

30. Tellez, A. et al. Whole-slide mitosis detection in H E breast histology using PHES as a reference to train distilled state-invariant convolutional networks. IEEE Trans. Med. Imaging 37, 1216–1236 (2018).

31. Liu, Y. et al. Detecting cancer metastases on gigapixel pathology images. Preprint arXiv:1809.07100 (https://doi.org/10.1101/302412) (2018).

32. Tellez, A. et al. Quantitative histopathology image segmentation and stain color normalization in convolutional neural networks for computational pathology. IEEE Trans. Med. Imaging 38, 1616–1626 (2019).

33. Anglè, A. et al. A high-performance system for robust stain normalization of whole-slide images in histopathology. Front. Med. 6, 193 (2019).

34. Liu, J. et al. An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics. Gef 173, 400–416 (2018).

35. The Cancer Genome Atlas. The immune landscape of cancer. Immunity 48, 812–830. e14 (2018).

36. Agarwal, N. & Agarwal, K.R. First and second order statistics features for histological image classification. IEEE Trans. Inf. Sci. J. 43, 1467–1475 (2014).

37. Haralick, R. M., Shmugam, K. M. & Dinstein, I. Textural features for image classification. IEEE Trans. Syst. Man Cybern. SMC-3, 610–621 (1973).

38. Chollat, F. Xception: deep learning with deconvlutive separable convolutions. https://arxiv.org/abs/1603.02673 (2017).

39. Alomairi, S. et al. A deep learning model for manifold approximation and projection for dimension reduction. Preprint at arXiv:1809.07100 (2018).

40. Alomairi, S. et al. A deep learning model for manifold approximation and projection for Singh, S. & Guestin, C. ‘Why should I trust you?’, explaining the predictions of any classifier. Preprint at arXiv:1602.04938 (2016).

41. Raschka, S. Model evaluation, model selection, and algorithm selection for machine learning. https://arxiv.org/abs/1011.1280 (2010).

42. Boyd, S., Boyd, S. P. & Vandenberghe, L. Convex Optimization (Cambridge University Press, 2004).

43. Cather, J. N. et al. A comprehensive analysis of genetic ancestry and its molecular correlates in cancer. Cancer Cell 39, 659–646 (2020).

44. Cather, J. N. et al. Histology of breast cancer in relation to age. Br. J. Cancer 75, 593–596 (1997).

45. Iupatt, E. O., Kuopio, T. & Collan, Y. Proliferation in African breast cancer histology: a study of cancer tissue and normal tissue material. Br. J. Cancer 55, 1783–1789 (2002).

46. Cather, J. N. et al. Tumor differences in breast cancer survey by indigenous African women reveals over-representation of triple-negative breast cancer. J. Clin. Oncol. 27, 4515–4521 (2009).

47. Cather, J. N. et al. Differences in breast cancer hormone receptor status and histology by race and ethnicity among women 50 years of age and older. Am. J. Obstet. Gynecol. Prev. 11, 401–407 (2016).

48. Hoo, D. J. et al. Genome-wide association studies in women of African ancestry identified 32q6.21 as a novel susceptibility locus for osteogenic receptor negative breast cancer. Hum. Mol. Genet. 25, 4437–4446 (2016).

49. Daly, B. & Olapade, O. A. A perfect storm: How tumor biology, genomics, and health disparities intersect to impact racial survival of breast cancer and breast cancer proposed interventions for change. Ca. (A. J. Clin. J. Clin. Med.) 221, 238 (2015).

50. Hsu, T. H. & Olapade, O. I. Epidemiology of triple-negative breast cancer: a review. Cancer 27, 8–16 (2022).

51. Hsu, T. H. & Olapade, O. I. Racial disparities in adult breast cancer treatment. JCO 34, 1357–1362 (2020).

52. Chao, D. S., Shah, N. H. & Magnus, D. Implementing machine learning in healthcare: a review. Stat. Med. 38, 983–983 (2019).

53. Chen, J. et al. Pathomic Feature Fusion Framework for Fusion Histopathology and Genomic Features for Cancer Diagnosis and Prognosis. IEEE Transactions on Medical Imaging 1–1 (2020). https://doi.org/10.1109/TMI.2020.3000001.

54. Jaber, M. I. et al. A deep learning image-based intrinsic molecular subtype classifier for breast tumors with tumor-tumor heterogeneity that may affect survival. Proc. Natl. Acad. Sci. U.S.A. 117, 10220–10227 (2020).

55. Mobadarey, P. et al. Predicting cancer outcomes from histology and genomics in multiethnic networks. Proc. Natl. Acad. Sci. U.S.A. 115, E2979–E2989 (2018).

56. Wu, Z. et al. DeepRHE: a deep convolutional neural network framework to evaluate histology cancer recurrence. Proc. Natl. Acad. Sci. U.S.A. 115, doi:10.1073/pnas.1710608115 (2018).

57. Wainess, J. et al. Deep learning-based survival prediction for multiple cancer types using histopathology images

---

<!-- Page 13 -->

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-24698-1

ARTICLE

100-111 (MICCAT Workshop). https://www.nature.com/articles/srep296.

64. Tang, T., Zwanzili, J. A., Francis, K. N., Qutub, A. A. & Gaber, M. W. Image-based classification of tumor type and growth rate using machine learning: a preclinical study. Sci. Rep. 9, 13259 (2019).

65. Delong, E., DeLong, M. M. & Clarke-Pearson, D. L. Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. Biometrics 44, 837–845 (1988).

66. Hanley, J. A. & McNeil, B. J. A method of comparing the areas under receiver operating characteristic curves derived from the same cases. Radiology 148, 83–93 (1983).

67. Zanjani, G. J., Zinger, S., Bejforieh, B. E., Laak, J. A. W. M. van der & With, P. H. N. de. Stain normalization of histopathology images using generative adversarial networks. In 2018 IEEE International Symposium on Biomedical Imaging (ISBI 2018), 573–577 (IEEE, 2018).

68. Perot, C. M. et al. Molecular portraits of human breast tumours. Nature 406, 747–752 (2000).

69. Mouton, D. M. et al. Comprehensive molecular characterization of human colon and rectal cancer. Nature 487, 330–337 (2012).

70. Hammerman, P. S. et al. Comprehensive genomic characterization of squamous cell lung cancers. Nature 489, 219–225 (2012).

71. Collison, E. A. et al. Comprehensive molecular profiling of lung adenocarcinoma. Nature 511, 543–550 (2014).

72. Cresswell, C. J. et al. Comprehensive molecular characterization of clear cell renal cell carcinoma. Nature 499, 43–49 (2013).

73. Lawrence, M. S. et al. Comprehensive genomic characterization of head and neck squamous cell carcinomas. Nature 517, 576–582 (2015).

74. Deng, J. et al. ImageNet: a large-scale hierarchical image database. In 2009 IEEE Conference on Computer Vision and Pattern Recognition, 248–255 (IEEE, 2009). https://www.nature.com/articles/s41467-020-0376-2.

75. Kingma, D. P. & Ba, J. Adam: a method for stochastic optimization. Preprint at https://arxiv.org/abs/1412.6980 (2017).

76. Byrdland, P. Peter50/StainTools patch release for DOI. https://doi.org/10.5281/zenodo.3031700 (2019).

77. Gonzalez, R. C. & Woods, R. E. Image Image Processing, 3rd edn. (Prentice-Hall, Inc., 2006).

78. Wall, Svander et al. scikit-image: image processing in Python. PeerJ 2, e453 (2014).

79. IBM. IBM ILOG CPLEX 12.10 User's Manual (IBM ILOG CPLEX Division, Incelle Village, 2017).

80. Frederick, Matthew Howard. Preserved Site Cross Validation, Zenodo https://doi.org/10.5281/zenodo.4718204 (2021).

## Acknowledgements

A.T.P. received support from the NIH/NIDDK (R01-DEB26500), the NCI (U01-CA240577), the Adenosin Cytosine Carcinoma Research Foundation, the Cancer Research Foundation, and the American Cancer Society. D.H., R.N., and O.I.O. received support from the NIH/NCI (P20-CA233307). Figure 1 and Supplementary Figure 5 were created in part with BioRender.com.

## Author contributions

F.M.H. and A.T.P. were responsible for concept proposal and study design. F.M.H., J.D., S.K., and J.N. performed conceptual, programming (J.D., S.K., H.C.), and analysis, performed manual oversight and quality control for digital pathology, along with segmentation of tumors. F.M.H., J.D., S.K., D.H., R.N., O.I.O., J.N.G., and A.T.P. contributed to data interpretation and statistical approaches. All authors contributed to the data analysis and writing of the manuscript.

## Competing interests

R.N. reports relationships with Aduro, Cardinal Health, Glavis, Fujifilm, GI Therapeutics, Genentech, Immunomedics/Gilad, Ionis, Troco Genomics, Merck, Oncose, Pfizer, Seattle Genetics, serves on the data safety monitoring board for GI Therapeutics, and receives research funding from Arvinas, AstraZeneca, Celgene, Corcept Therapeutics, Genentech/Roche, Immunomedics/Gilad, Merck, OHL Pharma, Odonate Therapeutics, Oncose, Pfizer, Seattle Genetics, Talio, O.I.O. reports relationships with CancerBio, Tempus, and Sigena, and speaks as an Advocate for Sanaa G. Komen and the American Cancer Society. J.N.G. reports a relationship with Oxoid. A.T.P. reports a relationship with New Rhein and serves on the advisory board for Prelude Therapeutics.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-021-24698-1.

Correspondence and requests for materials should be addressed to R.L.G. or A.T.P.

Peer review information Nature Communications thanks Jeffrey Chuang, Wilson Goh and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer review reports are available.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holders. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2021

NATURE COMMUNICATIONS | (2021)12:4423 | https://doi.org/10.1038/s41467-021-24698-1 | www.nature.com/naturecommunications

13