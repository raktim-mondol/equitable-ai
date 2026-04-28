# JAMADermatology | Original Investigation

# Federated Learning for Decentralized Artificial Intelligence in Melanoma Diagnostics

Sarah Haggenmüller, MSc; Max Schmitt, MSc; Eva Krieghoff-Henning, PhD; Achim Hekler, MSc; RomanC. Maron, MSc; Christoph Wies, MSc; Jochen S. Utikal, MD; Friedegund Meier, MD; Sarah Hobelsberger, MD; Frank F. Gellrich, MD; Mildred Sergon, MD; Axel Hauschild, MD; Lars E. French, MD; Lucie Heinzerling, MD; Justin G. Schlager, MD; Kamran Ghoreschi, MD; Max Schlaak, MD; Franz J. Hilke, PhD; Gabriela Poch, MD; Sören Korsing, MD; Carola Berking, MD; Markus V. Heppt, MD; Michael Erdmann, MD; Sebastian Haferkamp, MD; Konstantin Drexler, MD; Dirk Schadendorf, MD; Wiebke Sondermann, MD; Matthias Goebeler, MD; Bastian Schilling, MD; Jakob N. Kather, MD; Stefan Fröhling, MD; Titus J. Brinker, MD

IMPORTANCE The development of artificial intelligence (AI)-based melanoma classifiers typically calls for large, centralized datasets, requiring hospitals to give away their patient data, which raises serious privacy concerns. To address this concern, decentralized federated learning has been proposed, where classifier development is distributed across hospitals.

OBJECTIVE To investigate whether a more privacy-preserving federated learning approach can achieve comparable diagnostic performance to a classical centralized (ie, single-model) and ensemble learning approach for AI-based melanoma diagnostics.

DESIGN, SETTING, AND PARTICIPANTS This multicentric, single-arm diagnostic study developed a federated model for melanoma-nevus classification using histopathological whole-slide images prospectively acquired at 6 German university hospitals between April 2021 and February 2023 and benchmarked it using both a holdout and an external test dataset. Data analysis was performed from February to April 2023.

EXPOSURES All whole-slide images were retrospectively analyzed by an AI-based classifier without influencing routine clinical care.

MAIN OUTCOMES AND MEASURES The area under the receiver operating characteristic curve (AUROC) served as the primary end point for evaluating the diagnostic performance. Secondary end points included balanced accuracy, sensitivity, and specificity.

RESULTS The study included 1025 whole-slide images of clinically melanoma-suspicious skin lesions from 923 patients, consisting of 388 histopathologically confirmed invasive melanomas and 637 nevi. The median (range) age at diagnosis was 58 (18-95) years for the training set, 57 (18-93) years for the holdout test dataset, and 61 (18-95) years for the external test dataset; the median (range) Breslow thickness was 0.70 (0.10-34.00) mm, 0.70 (0.20-14.40) mm, and 0.80 (0.30-20.00) mm, respectively. The federated approach (0.8579; 95% CI, 0.7693-0.9299) performed significantly worse than the classical centralized approach (0.9024; 95% CI, 0.8379-0.9565) in terms of AUROC on a holdout test dataset (pairwise Wilcoxon signed-rank, P < .001) but performed significantly better (0.9126; 95% CI, 0.8810-0.9412) than the classical centralized approach (0.9045; 95% CI, 0.8701-0.9331) on an external test dataset (pairwise Wilcoxon signed-rank, P < .001). Notably, the federated approach performed significantly worse than the ensemble approach on both the holdout (0.8867; 95% CI, 0.8103-0.9481) and external test dataset (0.9227; 95%CI, 0.8941-0.9479).

CONCLUSIONS AND RELEVANCE The findings of this diagnostic study suggest that federated learning is a viable approach for the binary classification of invasive melanomas and nevi on a clinically representative distributed dataset. Federated learning can improve privacy protection in AI-based melanoma diagnostics while simultaneously promoting collaboration across institutions and countries. Moreover, it may have the potential to be extended to other image classification tasks in digital cancer histopathology and beyond.

JAMADermatol . 2024;160(3):303-311. doi:10.1001/jamadermatol.2023.5550 Published online February 7, 2024.

Editorial

page 269

Supplemental content

Author Affiliations: Author affiliations are listed at the end of this article.

Corresponding Author: Titus J. Brinker, MD, Digital Biomarkers for Oncology Group, National Center for Tumor Diseases (NCT), German Cancer Research Center (DKFZ), Im Neuenheimer Feld 280, 69120 Heidelberg, Germany (titus.brinker@dkfz.de).

(Reprinted)

C onvolutional neural networks-deep neural networks most commonly applied to image classification-have shownpromiseinimprovingdiagnosticaccuracyforvarious diseases, 1-3 including melanoma. 4-7 Melanomaistheleading cause of skin cancer deaths worldwide. 8 Early-stage detection increases the survival chances of affected patients significantly but is challenging due to frequent morphological overlap between melanoma and atypical nevi. 9,10 In experimentalsettings, convolutional neural networks have achieved performance on par or even superior to that of human experts for both dermatological 11-14 and histopathological 15,16 classificationtasks.Theseresultssuggestthatartificialintelligence(AI) has the potential to revolutionize the diagnosis of melanoma in offering more accurate detection.

Nonetheless, AI models are highly data dependent, meaning that their performance correlates with the size and diverseness of the training set. The more diverse data an AI model is trained on, the more likely it is to perform well. 17-19 Therefore, to develop AI algorithms, patient data are typically transferred to one site for training and testing and stored in a centralized way (known as classical centralized learning). However, in the medical field, ensuring patient data confidentiality is of utmost importance; consequently, sharing patient data is heavily regulated. Thus, the transfer of patient data to an external facility to generate the envisaged algorithms can raise serious privacy concerns. Alternatively, institutions can use their own data and computing power to develop separate AI algorithms, whose decisions are subsequently merged into one (known as ensemble learning). However, clinical settings often face computational resource constraints, making it challenging to run complex ensemble models in real time. These framework conditions pose difficulties for collaboration and data collection, particularly in multicenter studies or international research collaborations.

Toaddressthesechallenges,newapproaches,suchasfederated learning (FL), 20,21 have been developed to enable the decentralized training of AI algorithms using data kept at their origin, while requiring less computational power on site. FL involves each institution training its own model with its own data, while communication and aggregation are executed by a central coordinator.

Previous studies have examined the use of FL in diagnosing melanoma 22,23 andothermedicalapplications. 24-27 While Bdair et al 22 and Agbley et al 23 have demonstrated the promise of FL for classifying retrospective melanoma data, to our knowledge no study has evaluated FL leveraging prospectively collected, clinically representative distributed melanomadatanorexternallyvalidatedtheperformanceoftheproposedclassifiers. Thesegapsintheexistingliteraturehighlight the need for further research to explore the effectiveness of FLformelanomadiagnosticswhenleveragingprospectivedata andtoassess the generalizability of the respective classifiers. Therefore, we developed a model using a decentralized FL approach for the binary classification of invasive melanomas (IMs) and nevi based on histopathological whole-slide images (WSIs) and directly compared it retrospectively with the classical centralized and ensemble learning on both a hold-

# KeyPoints

Question Can a privacy-preserving federated learning approach achieve comparable diagnostic performance to classical centralized learning approaches for artificial intelligence-based melanoma diagnostics?

Findings In a consecutive multicenter diagnostic study involving 1025 whole-slide images of clinically melanoma-suspicious skin lesions from 923 patients, a melanoma-nevus classifier developed using classical centralized learning significantly outperformed the federated model in terms of area under the receiver operating characteristic curve on a holdout test dataset but performed significantly worse than the federated model on an external test dataset.

Meaning Federated learning has the potential to achieve at least on-par performance to classical centralized learning approaches while simultaneously promoting collaboration across institutions and countries.

out and an external test dataset using prospectively collected, clinically representative distributed data from 6 Germanuniversity hospitals.

# Methods

# Ethics Statement and Reporting Standards

Ethicsapprovalwasobtainedfromtheethicscommitteeatthe Technical University of Dresden, the Friedrich-Alexander University Erlangen-Nuremberg, the LMU Munich, the University of Regensburg, and the University Hospital Wuerzburg. Patients provided written informed consent. This work was performed in accordance with the Declaration of Helsinki. The Standards for Reporting of Diagnostic Accuracy (STARD) reporting guidelines were followed for the reporting of this study (eTable 2 in Supplement 1). 28

# Patient Cohorts and Slide Acquisition

Hematoxylin-eosin-stained reference slides of skin lesions were prospectively acquired at 6 German university hospitals (Berlin, Dresden, Erlangen, Munich, Regensburg, Wuerzburg) between April 2021 and February 2023. Study participants had to be at least 18 years old and were required to have clinically melanoma-suspiciousskinlesions.Lesionswerenot allowedtohavebeenpreviouslybiopsiedorlocatedunderthe fingernails or toenails. Diagnostic labels were histopathologically confirmed by at least 1 reference dermatopathologist at the corresponding hospital as part of routine clinical practice. In collision cases involving multiple tumors, the label of the larger tumor region was assigned. Only histopathologically confirmed IMs and nevi were eligible for this study.

# WSIPreprocessing

AnAperio AT2 DX slide scanner (Leica Biosystems) was used to digitize the hematoxylin-eosin-stained reference slides of all enrolled patients at ×40 magnification,producingWSIswith a resolution of 0.25 μm/pixel to generate patches for training

andtesting. After manually annotating the area of the epidermis (M. Schmitt), the region of interest was tessellated into downscaled square patches. Each patch had a uniform edge length of 224 pixels, corresponding to 103.04 μm. WSI annotation and tessellation were performed using QuPath, version0.2.3. 29 Additionally,blurdetectionwasimplementedwith custom code written in Python, version 3.7.0 (Python Software Foundation). A patch was classified as blurry if it had a Laplacian below a manually set threshold of 510 and subsequently discarded.

# Model Development

ResNet18pretrainedonImageNetwasusedtotrainonemodel with FL, one with centralized learning, and one with ensemble learning. A small architecture was used to limit training and inference time and streamline the experimental procedures. The tree-structured Parzen estimator 30 was used to choose the hyperparameters to maximize the area under the receiver operating characteristic curve (AUROC) at lesion level for a validation set. For each approach, the learning rate, numberoftrainingepochs,amountofdatausedin1epochperWSI, and,forFLspecifically,thefrequencyofweightexchangewere tuned for an equal number of optimization steps using the PythonlibraryOptuna. 31 Duringthisprocess,30%ofthetraining data served as the validation set, and the training followed Leslie Smith's 1-cycle policy, which involves training the model with a gradually increasing learning rate for the first half of the training cycle, followed by a gradual decrease in the learning rate for the second half. 32 Duringinference,the confidence value of every patch of a WSI was interpreted as the probability for classification as IM or nevus. The average of these probabilities was the final probability for each WSI.

Forthefederatedapproach,datafromhospitals1to5were leveraged.Eachhospital'smodelwastrainedforacertaintime intervalwiththesamehyperparameters.Thetimeintervalwas based on a synchronization factor, which was tuned during training and was proportional to the size of the dataset of the respective hospital. After each interval, model weights were collected and merged into a new model using a weighted average. The assigned weights were proportional to the amount ofdataavailableduringtraining.Subsequently,thenewmodel was(re)distributedtoeveryhospitaltocontinuetraining.Since communicationbetweentheparticipantsinthisapproachwas not the focus, this process was only simulated on 1 computational unit.

For the centralized approaches, the model Hfull represents the model that was trained using data from hospitals 1 to 5. The remaining 5 models (models H1, H2, H3, H4, and H5) were trained by excluding the data of hospitals 1, 2, 3, 4, or 5, respectively.

For the ensemble approach, 5 classifiers were trained separately using only 1 of the 5 training sets from hospitals 1 to 5 with individual hyperparameters. For inference, each model computed a probability for a given input. All 5 probabilities were subsequently averaged to calculate the final prediction. Training and inference were implemented in Python, version 3.7.0, using PyTorch, version 1.13.0, 33 and fastai, version 2.7.10. 34

Table 1. Characteristics of the Study Sample

| |No.| | |
|---|---|---|---|
|Hospital|Slides (patients)|Invasive melanomas|Nevi|
|1|71 (62)|19|52|
|2|97 (86)|56|41|
|3|107 (103)|59|48|
|4|178 (157)|37|141|
|5|236 (215)|75|161|
|6|336 (300)|142|194|
|Total|1025 (923)|388|637|


# Statistical Analysis

Two-sided χ 2 tests were used to identify significant differences between the training and test datasets. The AUROC served as the primary end point for evaluating the performance of the developed models. Secondary end points includedbalancedaccuracy,sensitivity,andspecificity.Themean valuesofthecorrespondingmetricswerecalculatedusing1000 iterations of bootstrapping to reduce the impact of stochastic events. The 95% CIs were calculated using the nonparametric percentile method. 35 For statistical comparisons of the AUROCs, pairwise 2-sided Wilcoxon signed-rank tests were applied. A significance level of P < .05 was set for all analyses. Significance levels were adjusted to 0.025 ( m = 2) or 0.01 ( m = 5) according to Bonferroni correction in case of multiple tests. Statistical analysis was performed in SPSS, version 29.0.0.0 (IBM Corporation).

# Results

# NumberofEligible Slides and Patients

Atotal of 1025 slides from 923 patients, consisting of 388 IMs and 637 nevi, were included in the analysis ( Table 1 ). A further 373 slides were excluded for not meeting the predefined inclusion criteria of this study (eg, in situ tumors; Figure 1 ). Atotalof548755patcheswerederivedfromtheeligibleslides (296141 IMs, 252 614 nevi) for training and testing purposes (eTable 1 in Supplement 1).

# Patient Characteristics and Differences Among Datasets

The eligible cases in the training set (data from hospitals 1 to 5) and the holdout test dataset (data from hospitals 1 to 5) exhibited significant differences in lesion subtype and American Joint Committee on Cancer (AJCC) stage when compared to the external test dataset (data from hospital 6; P < .001). However, no significant differences were observed in lesion localization, age, or Breslow thickness. The median (range) age at diagnosis was 58 (18-95) years for the training set, 57 (18-93) years for the holdout test dataset, and 61 (18-95) years for the external test dataset; the median (range) Breslow thickness was 0.70 (0.10-34.00) mm, 0.70 (0.20-14.40) mm, and 0.80 (0.30-20.00) mm, respectively. Thus, the training andholdouttestdatasetswereconsideredtobedifferentlydistributed than the external one. Patient characteristics of the study sample are summarized in Table 2 .

jamadermatology.com

Figure 1. Flowchart of the Slide Inclusion Process

![image 1](data:image/png;base64,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)

1398

Scanned slides

362

Excluded

224

No histopathologically confirmed IM or nevus

127

Melanoma in situ

11

Histopathological diagnosis pending

1036

Eligible slides

11

Excluded

7

<50 Patches

4

Other reasons (eg, damaged file)

1025

Included slides

586

Training set

336

External set

103

Holdout test set

Slides were excluded from the analysis if there was no histopathologically confirmed label available or if the lesion proved to be neither invasive melanoma (IM) nor nevus (in situ tumors or other diagnoses, eg, basal cell carcinoma, squamous cell carcinoma). In addition, slides that exhibited fewer than 50 epidermal patches or other technical issues were removed.

# Comparison of FL With Other Approaches

To compare the performance of FL, a total of 586 lesions (209IMs,377nevi)derivedfrom5hospitalswereusedtotrain 3 distinct models (eFigure 1 in Supplement 1): first, the federated approach, where a model was built through decentralized training of individual models that were merged at regular intervals 36 ; second, the centralized approach (Hfull), where a model was built using all available data on a centralized server 37 ; andthird,theensembleapproach,whereamodelwas built for each participating hospital, and the results of all models were aggregated into one final prediction. 38 A randomly sampled holdout test dataset from the same hospitals already involved in model training, consisting of 103 lesions (37 IMs, 66 nevi), and an external test dataset from another hospital not involved in model training, consisting of 336 lesions (142 IMs, 194 nevi), were used to evaluate the performances of the approaches.

# Performance of FL on Holdout Test Dataset

Ontheholdouttestdataset,FLperformedtheworst( Table3 ), with a mean AUROC of 0.8579 (95% CI, 0.7693-0.9299; Figure 2 ), followed by the ensemble approach with a mean AUROC of 0.8867 (95% CI, 0.8103-0.9481). The centralized approach (model Hfull) performed best, with a mean AUROC of 0.9024 (95% CI, 0.8379-0.9565). The results indicate that on the holdout test dataset, the classical centralized model performed significantly better than the federated and ensemble approaches in terms of AUROC (pairwise Wilcoxon signed-rank, P < .001). For a detailed overview of the confusion matrices on the holdout test dataset, see eFigure 2 in Supplement 1.

# Performance of FL on External Test Dataset

Ontheexternaltest dataset, a different ranking was observed (Table 3). The centralized approach (model Hfull) performed

theworst,achievingameanAUROCof0.9045(95%CI,0.87010.9331), while FL demonstratedameanAUROCof0.9126(95% CI, 0.8810-0.9412; Figure 2). The ensemble approach performed the best on the external test dataset, with a mean AUROCof0.9227(95%CI,0.8941-0.9479).Altogether,onthe externaltestdataset,theFLapproachyieldedsignificantlybetter results than the centralized model in terms of AUROC (pairwiseWilcoxonsigned-rank, P < .001). Notably, both the FL and centralized modelsperformedsignificantlyworsethantheensemble approach (pairwise Wilcoxon signed-rank, P < .001). For a detailed overview of the confusion matrices on the external test dataset, see eFigure 3 in Supplement 1.

# Comparison of FL With a More Realistic Centralized Approach

Furthermore, the classical centralized approach was subjected to retraining using several smaller datasets (models H1, H2, H3, H4, and H5) for comparison with the original federated approach, which was trained with all available training data. This comparison was conducted to investigate whether FL would achieve at least comparable results to centralized approaches when it had access to more data (ranging from 71 to 236 more cases). Thereby, we explored the feasibility of potential future clinical FL application scenarios where hospitals might be more willing to participate in the developmentandrefinementofaclassifierwhennopatientdataneed to be transferred to an external institution.

After retraining, the centralized approach maintained its superiority on the holdout test dataset in terms of AUROC regardless of which hospital was omitted for classifier training (models H1, H2, H3, H4, and H5; pairwise Wilcoxon signedrank, P < .001; supporting data in Table 3). However, on the external test dataset, the model developed with the FL approach held its performance advantage over all 5 centralized models developed using smaller datasets (pairwise Wilcoxon signed-rank, P < .001; supporting data in Table 3). These results suggest that a surplus of training data does not necessarily result in superior classification performance for FL.

# Discussion

In this study, we aimed to develop and externally validate a decentralized trained FL model for melanoma-nevus classification using histopathological WSIs. Additionally, we directly compared FL with classical centralized and ensemble learning, which are commonly applied for melanoma classification tasks. In this context, FL achieved a mean AUROC of 0.8579(95%CI,0.7693-0.9299)ontheholdouttestdatasetand 0.9126 (95% CI, 0.8810-0.9412) on the external test dataset, thus representing a reliable alternative.

The utilized datasets encompassed a comprehensive representation of IM cases encountered in day-to-day clinical care due to the prospective and consecutive data collection from multiple centers. By avoiding selection bias that many have arisen in previous melanoma classification studies that applied FL but collected data retrospectively, 22,23 we minimized the risk of overestimating or underestimating the per-

Table 2. Patient Characteristics of the Study Sample

| |Patients, No. (%)| | | | | |
|---|---|---|---|---|---|---|
| |Training set (hospitals 1-5)| |Holdout test dataset (hospitals 1-5)| |External test dataset (hospital 6)| |
|Characteristic|IM (n = 209)|Nevus (n = 377)|IM (n = 37)|Nevus (n = 66)|IM (n = 142)|Nevus (n = 194)|
|Age at diagnosis, y| | | | | | |
|<35|5 (2.4)|75 (19.9)|1 (2.7)|16 (24.2)|4 (2.8)|51 (26.3)|
|35-54|45 (21.5)|129 (34.2)|8 (21.6)|19 (28.8)|19 (13.4)|67 (34.5)|
|55-74|84 (40.2)|124 (32.9)|17 (45.9)|22 (33.3)|58 (40.8)|48 (24.7)|
|>74|74 (35.4)|49 (13.0)|11 (29.7)|9 (13.6)|61 (43.0)|28 (14.4)|
|Unknown|1 (0.5)|0|0|0|0|0|
|Lesion localization| | | | | | |
|Palms/soles|1 (0.5)|6 (1.6)|1 (2.7)|3 (4.5)|4 (2.8)|5 (2.6)|
|Face/scalp/neck|43 (20.6)|17 (4.5)|8 (21.6)|4 (6.1)|24 (16.9)|26 (13.4)|
|Upper extremities|37 (17.7)|38 (10.1)|5 (13.5)|9 (13.6)|18 (12.7)|13 (6.7)|
|Lower extremities|45 (21.5)|78 (20.7)|8 (21.6)|13 (19.7)|29 (20.4)|34 (17.5)|
|Back|54 (25.8)|134 (35.5)|8 (21.6)|18 (27.3)|43 (30.3)|59 (30.4)|
|Abdomen|13 (6.2)|48 (12.7)|3 (8.1)|9 (13.6)|9 (6.3)|29 (14.9)|
|Chest|12 (5.7)|37 (9.8)|2 (5.4)|8 (12.1)|10 (7.0)|16 (8.2)|
|Buttock|2 (1.0)|10 (2.7)|1 (2.7)|2 (3.0)|1 (0.7)|5 (2.6)|
|Genitalia|1 (0.5)|5 (1.3)|1 (2.7)|0|1 (0.7)|3 (1.5)|
|Unknown|1 (0.5)|4 (1.1)|0|0|3 (2.1)|4 (2.1)|
|Lesion subtype| | | | | | |
|Superficial spreading melanoma|142 (67.9)|NA|24 (64.9)|NA|35 (24.6)|NA|
|Nodular melanoma|25 (12.0)|NA|4 (10.8)|NA|20 (14.1)|NA|
|Lentigo maligna melanoma|29 (13.9)|NA|5 (13.5)|NA|9 (6.3)|NA|
|Acral lentiginous melanoma|8 (3.8)|NA|2 (5.4)|NA|6 (4.2)|NA|
|Desmoplastic melanoma|0|NA|0|NA|2 (1.4)|NA|
|Spitzoid melanoma|1 (0.5)|NA|1 (2.7)|NA|0|NA|
|Other types of IM/combined forms of IM/subtype unknown|4 (1.9)|NA|1 (2.7)|NA|70 (49.3)|NA|
|Spitz nevus and variants|NA|6 (1.6)|NA|0|NA|4 (2.1)|
|Dysplastic nevus/Clark nevus|NA|155 (41.1)|NA|30 (45.5)|NA|110 (56.7)|
|Acral nevus|NA|7 (1.9)|NA|4 (6.1)|NA|12 (6.2)|
|Recurrent nevus|NA|1 (0.3)|NA|0|NA|1 (0.5)|
|Blue nevus|NA|21 (5.6)|NA|3 (4.5)|NA|6 (3.1)|
|Other types of nevi/combined|NA|187 (49.6)|NA|29 (43.9)|NA|61 (31.4)|
|AJCC stage a| | | | | | |
|IA|87 (41.6)|NA|13 (35.1)|NA|70 (49.3)|NA|
|IB|23 (11.0)|NA|8 (21.6)|NA|30 (21.1)|NA|
|IIA|13 (6.2)|NA|3 (8.1)|NA|6 (4.2)|NA|
|IIB|7 (3.3)|NA|0|NA|14 (9.9)|NA|
|IIC|7 (3.3)|NA|3 (8.1)|NA|7 (4.9)|NA|
|IIIA|4 (1.9)|NA|0|NA|3 (2.1)|NA|
|IIIB|4 (1.9)|NA|0|NA|5 (3.5)|NA|
|IIIC|12 (5.7)|NA|1 (2.7)|NA|6 (4.2)|NA|
|IV|2 (1.0)|NA|1 (2.7)|NA|1 (0.7)|NA|
|Unknown|50 (23.9)|NA|8 (21.6)|NA|0|NA|
|Breslow thickness,mm b| | | | | | |
|≤1.00 (T1)|126 (60.3)|NA|23 (62.1)|NA|89 (62.7)|NA|
|1.01-2.00 (T2)|25 (12.0)|NA|6 (16.2)|NA|16 (11.3)|NA|
|2.01-4.00 (T3)|27 (12.9)|NA|1 (2.7)|NA|19 (13.4)|NA|
|>4.00 (T4)|23 (11.0)|NA|6 (16.2)|NA|17 (12.0)|NA|
|Unknown|8 (3.8)|NA|1 (2.7)|NA|1 (0.7)|NA|


of IM.

Abbreviations: AJCC, American Joint Committee on Cancer; IM, invasive melanoma; NA, not applicable.

b Breslow thickness describes the extent of anatomic spread and serves as an important prognostic factor for IM.

a AJCC staging constitutes the criterion standard for histopathological reporting

Table 3. Performance Metrics of the Different Classification Approaches on the Holdout and External Test Datasets

|Model|AUROC (95% CI)|Balanced accuracy,% (95% CI)|Sensitivity,% (95% CI)|Specificity,% (95% CI)|
|---|---|---|---|---|
|Performance metrics of the different classification approaches| | | | |
|Holdout| | | | |
|FL|0.8579 (0.7693-0.9299)|76.76 (67.70-84.89)|59.54 (42.86-75.00)|93.99 (87.84-98.55)|
|Ensemble|0.8867 (0.8103-0.9481)|81.46 (73.10-88.94)|84.02 (70.59-94.59)|78.89 (68.57-88.06)|
|Centralized|0.9024 (0.8379-0.9565)|85.23 (77.30-92.31)|83.91 (70.97-94.59)|86.55 (77.46-93.94)|
|External| | | | |
|FL|0.9126 (0.8810-0.9412)|81.73 (77.36-85.77)|80.92 (74.21-86.90)|82.54 (77.07-87.92)|
|Ensemble|0.9227 (0.8941-0.9479)|76.47 (72.69-80.48)|95.79 (92.19-98.65)|57.16 (50.51-63.96)|
|Centralized|0.9045 (0.8701-0.9331)|80.56 (76.71-84.38)|93.66 (89.21-97.22)|67.46 (60.87-74.05)|
|Performance metrics of the original federated approach and all 5 retrained leave-1-hospital-out approaches| | | | |
|Holdout| | | | |
|FL|0.8579 (0.7693-0.9299)|76.76 (67.70-84.89)|59.54 (42.86-75.00)|93.99 (87.84-98.55)|
|H1|0.9139 (0.8508-0.9648)|79.30 (70.90-87.40)|67.59 (52.63-82.50)|91.02 (83.33-97.06)|
|H2|0.8874 (0.8041-0.9529)|82.76 (74.68-90.05)|72.91 (57.89-86.67)|92.61 (86.15-98.41)|
|H3|0.8675 (0.7879-0.9337)|74.15 (65.63-82.90)|54.23 (37.50-70.97)|94.06 (87.67-98.59)|
|H4|0.8851 (0.8099-0.9511)|81.55 (73.26-89.44)|81.19 (68.29-93.55)|81.91 (72.06-90.77)|
|H5|0.8710 (0.7961-0.9401)|84.10 (75.96-91.18)|89.24 (78.38-97.50)|78.95 (68.75-88.06)|
|External| | | | |
|FL|0.9126 (0.8810-0.9412)|81.73 (77.36-85.77)|80.92 (74.21-86.90)|82.54 (77.07-87.92)|
|H1|0.8868 (0.8517-0.9207)|76.90 (72.60-80.99)|89.49 (84.09-94.24)|64.31 (57.43-70.77)|
|H2|0.8941 (0.8585-0.9252)|79.69 (75.59-83.84)|89.43 (84.29-93.92)|69.95 (63.37-76.22)|
|H3|0.8831 (0.8465-0.9172)|78.82 (74.30-82.76)|88.66 (82.99-93.48)|68.99 (62.43-75.13)|
|H4|0.8670 (0.8281-0.9020)|76.29 (71.84-80.39)|86.61 (81.21-91.88)|65.97 (59.28-72.77)|
|H5|0.8296 (0.7837-0.8698)|72.39 (67.77-76.60)|88.78 (83.45-93.63)|55.99 (49.46-62.78)|


Abbreviations: AUROC, area under the receiver operating characteristic curve; FL, federated learning.

formance of the compared classifiers. A strength of our study is the long-tailed distribution of localizations and IM subtypes (including rare subtypes, such as spitzoid melanomas), andallpossibleAJCCstagesandBreslowthicknesscategories. 39 Training the model on such a heterogeneous dataset that captures the complexity of clinical IM data enables the model to effectively recognize lesions of different types, severity levels, and depths and allows the model to learn spatial patterns and specific characteristics associated with diverse body regions.Thisenhancesitsoverallgeneralizability,ultimatelyleading to robust performance.

The data from hospital 6 served as an out-of-distribution test dataset, consisting of unseen data from an institution that was not part of the model training process. Notably, there weresignificant differences in the AJCC stages and lesion subtypescomparedtothetrainingandholdoutdatasets(Table2). Thedatafromhospital6includedlesionsfromaslightlyolder patient group, specifically, more patients with IM older than 74 years. On the other hand, the holdout test dataset (ie, unshown data derived from hospitals 1 to 5) tended to contain slightly more lesions from the Breslow thickness categories T2 (1.01-2.00 mm) and T4 (>4.00 mm; Table 2). These differences may also be evident in the corresponding WSIs and could have influenced the performance of the evaluated approaches.

Overall, the classical centralized model (Hfull) significantly outperformed FL on the holdout test dataset (ie, tested on unshown data from hospitals involved in model training) intermsofAUROC(0.9024vs0.8579),whileFLperformedsignificantly better (0.9126 vs 0.9045) on the external test dataset (ie, on data from a hospital not involved in model training). The findings demonstrate that FL techniques may not be as well suited to solve in-distribution classification problems (ie, same distribution as the training data), as indicated by the inferior performance on the holdout test dataset. On the other hand, they show that FL may provide additional advantages in terms of out-of-distribution generalizability, as indicated by theenhancedperformanceontheexternaltestdatasets(similar to observations in Warnat-Herresthal et al 20 and Dayan et al 25 ). The observed superior performance on the external test set could be due to the FL model not fully converging during training, possibly introducing a slight regularization effect. This phenomenon of nonconvergence is frequently encounteredinFLduetothechallengingtaskoftrainingondata from different distributions. 40

While the observed differences between FL and the centralized approach may not be large in absolute terms, they are consistentover1000iterationsofbootstrapping(ie,paireddata comparisons), thereby demonstrating a sustained outperformance of the centralized approach. Despite the compara-

![image 2](data:image/png;base64,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)

Figure 2. Mean Area Under the Receiver Operating Characteristic Curve (AUROC) of the 3 Investigated Approaches

A

B

Federated vs centralized, holdout test dataset

Federated vs centralized, external test dataset

1.0

1.0

0.8

0.8

Sensitivity, %

Sensitivity, %

0.6

0.6

0.4

0.4

Mean federated AUROC

Mean federated AUROC

0.2

0.2

(AUC = 0.8579)

(AUC = 0.9126)

Mean centralized AUROC

Mean centralized AUROC

(AUC = 0.9024)

(AUC = 0.9045)

0

0

0

0.2

0.4

0.6

0.8

1.0

0

0.2

0.4

0.6

0.8

1.0

1-Specificity, %

1-Specificity, %

C

D

Federated vs ensemble, holdout test dataset

Federated vs ensemble, external test dataset

1.0

1.0

0.8

0.8

Sensitivity, %

Sensitivity, %

0.6

0.6

0.4

0.4

Mean federated AUROC

Mean federated AUROC

0.2

0.2

(AUC = 0.8579)

(AUC = 0.9126)

Mean ensemble AUROC

Mean ensemble AUROC

(AUC = 0.8867)

(AUC = 0.9227)

0

0

0.2

0.4

0.6

0.8

1.0

0

0.2

0.4

0.6

0.8

1.0

0

1-Specificity, %

1-Specificity, %

Mean AUROCs on the holdout and external test dataset after 1000 iterations of bootstrapping, including the corresponding 95% CIs (shaded areas), are illustrated for the federated learning (FL) and the centralized approach (model Hfull) (A and B) and for the FL and the ensemble approach (C and D). AUCindicates area under the curve.

tively lower statistical power of the Wilcoxon signed-rank test, this marginalyetpersistentperformanceimprovementisclinically highly relevant, as any melanoma misclassification can lead to fatal outcomes.

Despite these positive findings, the ensemble approach continued to outperform FL and the classical centralized approach in terms of AUROC (0.9227 vs 0.9126 and 0.9045, respectively). Nevertheless, an ensemble approach poses extensive challenges for the explainability of the results, since understanding multiple sets of model weights is more difficult than dealing with 1 set in the FL approach. This is particularly relevant given the legislative requirement that medical devices must be explainable to a certain extent, 41 as well as its substantial influence on patients' and physicians' acceptance. 42

# Limitations

This study has limitations. Although the WSIs were digitized using the same slide scanner (Leica Aperio AT2 DX), heterogeneity was ensured by different staining and cutting protocolsoftheparticipatinghospitals.Whilethelabelsforthisstudy jamadermatology.com

were established based on the criterion standard of care (ie, histopathological verification), caution should be exercised in interpreting the results, as previous studies observed a discordance between pathologists of up to 25% in classifying melanoma. 9,10 Future studies may involve the integration of independent pathologist panels or epigenetic analyses (eg, methylation analyses) to further reduce interrater variability.

# Conclusions

The results of this diagnostic study demonstrate that FL can achieveacomparableperformancetothatofclassicalcentralized or ensemble approaches, making it a reliable alternative for the classification of IMs and nevi. Additionally, FL empowers institutions to contribute to the development of AI models, even with relatively small datasets or strict data protection rules, thereby fostering collaboration across institutions andcountries. Moreover, FL may have the potential to be furtherextendedtootherimageclassificationtasksindigitalcancer histopathology and beyond. Future research could build

onthisworkbyassessingitseffectivenesswithdifferenttypes of medical images (eg, dermoscopic or hyperspectral images), evaluating its feasibility for diagnosing various types of cancer,andinvestigatingitseffectivenessusingtechnicallydif-

ferent (eg, attention-based methods) AI models. In our ongoing research, we are exploring the scalability of FL for refined diagnostic tasks by incorporating in situ tumors as a clinically highly relevant but separate classification class.

# ARTICLE INFORMATION

Accepted for Publication: September 1, 2023. Published Online: February 7, 2024. doi:10.1001/jamadermatol.2023.5550

OpenAccess: This is an open access article distributed under the terms of the CC-BY License. ©2024Haggenmüller S et al. JAMADermatology .

Author Affiliations: Digital Biomarkers for Oncology Group, National Center for Tumor Diseases (NCT), German Cancer Research Center (DKFZ), Heidelberg, Germany (Haggenmüller, Schmitt, Krieghoff-Henning, Hekler, Maron, Wies, Brinker); Department of Dermatology, Venereology and Allergology, University Medical Center Mannheim, Ruprecht-Karls University of Heidelberg, Mannheim, Germany (Utikal); Skin Cancer Unit, German Cancer Research Center (DKFZ), Heidelberg, Germany (Utikal); DKFZ Hector Cancer Institute at the University Medical Center Mannheim, Mannheim, Germany (Utikal); Skin Cancer Center at the University Cancer Center and National Center for Tumor Diseases Dresden, Department of Dermatology, University Hospital Carl Gustav Carus, Technische Universität Dresden, Dresden, Germany (Meier, Hobelsberger, Gellrich, Sergon); Department of Dermatology, University Hospital (UKSH), Kiel, Germany (Hauschild); Department of Dermatology and Allergy, University Hospital, LMU Munich, Munich, Germany (French, Heinzerling, Schlager); Dr Phillip Frost Department of Dermatology and Cutaneous Surgery, Miller School of Medicine, University of Miami, Miami, Florida (French); Department of Dermatology, University Hospital Erlangen, Comprehensive Cancer Center Erlangen-European Metropolitan Region Nürnberg, CCC Alliance WERA, Erlangen, Germany (Heinzerling, Berking, Heppt, Erdmann); Department of Dermatology, Venereology and Allergology, Charité-Universitätsmedizin Berlin, Corporate member of Freie Universität Berlin and Humboldt-Universität zu Berlin, Berlin, Germany (Ghoreschi, Schlaak, Hilke, Poch, Korsing); Department of Dermatology, University Hospital Regensburg, Regensburg, Germany (Haferkamp, Drexler); Department of Dermatology, Venereology and Allergology, University Hospital Essen, Essen, Germany (Schadendorf, Sondermann); Department of Dermatology, Venereology and Allergology, University Hospital Würzburg and National Center for Tumor Diseases (NCT) WERA, Würzburg, Germany (Goebeler, Schilling); Else Kroener Fresenius Center for Digital Health, Technical University Dresden, Dresden, Germany (Kather); Department of Translational Medical Oncology, National Center for Tumor Diseases (NCT) Heidelberg and German Cancer Research Center (DKFZ), Heidelberg, Germany (Fröhling).

Author Contributions: Dr Brinker had full access to all of the data in the study and takes responsibility for the integrity of the data and the accuracy of the data analysis. Ms Haggenmüller and Mr Schmitt contributed equally to this work. Concept and design: Haggenmüller, Schmitt, Krieghoff-Henning, Kather, Brinker.

Acquisition, analysis, or interpretation of data: Haggenmüller, Schmitt, Hekler, Maron, Wies, Utikal, Meier, Hobelsberger, Gellrich, Sergon, Hauschild, French, Heinzerling, Schlager, Ghoreschi, Schlaak, Hilke, Poch, Korsing, Berking, Heppt, Erdmann, Haferkamp, Drexler, Schadendorf, Sondermann, Goebeler, Schilling, Fröhling, Brinker. Drafting of the manuscript: Haggenmüller, Schmitt,

Hauschild. Haggenmüller, Schmitt, Krieghoff-Henning, Hekler,

Critical review of the manuscript for important intellectual content: All authors. Statistical analysis: Haggenmüller, Wies. Obtained funding: Haferkamp, Brinker. Administrative, technical, or material support: Maron, Utikal, Meier, Sergon, Hauschild, Heinzerling, Schlager, Hilke, Heppt, Haferkamp, Schadendorf, Fröhling, Brinker. Supervision: Krieghoff-Henning, Hekler, French, Goebeler, Kather, Brinker.

Conflict of Interest Disclosures: MsHaggenmüller reported grants from Federal Ministry of Health, Berlin, Germany (grants: Skin Classification Project 2 [SCP2] and Tumor Behavior Prediction Initiative [TPI]; grant holder in both cases: Titus J. Brinker, German Cancer Research Center, Heidelberg, Germany) during the conduct of the study. Dr Krieghoff-Henning reported grants from German Federal Ministry of Health during the conduct of the study. Mr Hekler reported grants from German Federal Ministry of Health during the conduct of the study. Mr Maron reported grants from German Federal Ministry of Health during the conduct of the study. Prof Utikal reported personal fees from Amgen, Bristol Myers Squibb, GSK, Immunocore, LEO Pharma, Merck Sharp & Dohme, Novartis, Pierre Fabre, Roche, and Sanofi outside the submitted work. Prof Meier reported grants from Novartis and Roche; other (travel support or/and speaker's fees or/and advisor's honoraria) from BMS, MSD, and Pierre Fabre outside the submitted work. Dr Hobelsberger reported clinical trial support from Almirall and speaker's honoraria from Almirall, UCB, and AbbVie and travel support from UCB, Janssen Cilag, Almirall, Novartis, Lilly, LEO Pharma, and AbbVie outside the submitted work. Prof Heinzerling reported other (clinical studies) from BMS, MSD, Pierre Fabre, Replimune, and Sanofi; personal fees from Biomedx, BMS, MSD, Sun, Pierre Fabre, Novartis, and Sanofi; and grants from Therakos outside the submitted work. Dr Schlaak reported personal fees from BMS, Novartis, Immunocore, Sun Pharma, MSD, Recordati, and Sanofi Aventis outside the submitted work. Prof Berking reported grants from BMG Bundesministerium für Gesundheit to institute during the conduct of the study; personal fees from BMS, MSD, InflaRx, Novartis, Sanofi, LEO Pharma, Almirall Hermal, Pierre Fabre, Immunocore, and Delcath outside the submitted work. Dr Sondermann reported grants from Almirall and Medi GmbH; and personal fees from AbbVie, BMS, Boehringer Ingelheim, Celgene, Janssen, LEO Pharma, Lilly, Novartis, Pfizer, Sanofi Genzyme, and UCB outside the submitted work. Prof Goebeler reported grants from DKFZ Heidelberg

during the conduct of the study; grants (clinical study) from Argenx, Novartis, Janssen, and Galderma; personal fees from Almirall (consulting), Janssen (advisory board, speaker), GSK (advisory board, speaker), and Lilly (speaker) outside the submitted work. Prof Kather reported personal fees from Owkin, Panakeia, DoMore Diagnostics, Histofy, Roche, MSD, BMS, Eisai, Bayer, Fresenius, and Pfizer outside the submitted work. Dr Brinker reported being owner of Smart Health Heidelberg GmbHoutside the submitted work. No other disclosures were reported.

Funding/Support: This study was funded by the Federal Ministry of Health, Berlin, Germany (grants: Skin Classification Project 2 [SCP2] and Tumor Behavior Prediction Initiative [TPI]; grant holder in both cases: Titus J. Brinker, German Cancer Research Center, Heidelberg, Germany), and the Studienstiftung des deutschen Volkes, Bonn, Germany (scholarship holder: Sarah Haggenmüller).

Role of the Funder/Sponsor: The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

Data Sharing Statement: See Supplement 2.

Additional Information: This research is part of the doctoral thesis of Ms Haggenmüller.

# REFERENCES

- 1 . McKinney SM, Sieniek M, Godbole V, et al. International evaluation of an AI system for breast cancer screening. Nature . 2020;577(7788):89-94. doi:10.1038/s41586-019-1799-6
- 2 . Bulten W, Kartasalo K, Chen PC, et al; PANDA challenge consortium. Artificial intelligence for diagnosis and Gleason grading of prostate cancer: the PANDA challenge. Nat Med . 2022;28(1):154-163. doi:10.1038/s41591-021-01620-2
- 3 . Mei X, Lee HC, Diao KY, et al. Artificial intelligence-enabled rapid diagnosis of patients with COVID-19. Nat Med . 2020;26(8):1224-1228. doi:10.1038/s41591-020-0931-3
- 4 . Esteva A, Kuprel B, Novoa RA, et al. Dermatologist-level classification of skin cancer with deep neural networks. Nature . 2017;542 (7639):115-118. doi:10.1038/nature21056
- 5 . Haggenmüller S, Maron RC, Hekler A, et al. Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts. Eur J Cancer . 2021;156:202-216. doi:10.1016/j.ejca.2021.06.049
- 6 . Han SS, Park I, Eun Chang S, et al. Augmented intelligence dermatology: deep neural networks empower medical professionals in diagnosing skin cancer and predicting treatment options for 134 skin disorders. J Invest Dermatol . 2020;140(9): 1753-1761. doi:10.1016/j.jid.2020.01.019


7 . Haenssle HA, Fink C, Toberer F, et al; Reader Study Level I and Level II Groups. Man against machine reloaded: performance of

a market-approved convolutional neural network in classifying a broad spectrum of skin lesions in comparison with 96 dermatologists working under less artificial conditions. Ann Oncol . 2020;31(1): 137-143. doi:10.1016/j.annonc.2019.10.013

8 . Schadendorf D, van Akkooi ACJ, Berking C, et al. Melanoma. Lancet . 2018;392(10151):971-984. doi:10.1016/S0140-6736(18)31559-9

9 . Elmore JG, Barnhill RL, Elder DE, et al. Pathologists' diagnosis of invasive melanoma and melanocytic proliferations: observer accuracy and reproducibility study. BMJ . 2017;357:j2813. doi:10.1136/bmj.j2813

10 . Lodha S, Saggar S, Celebi JT, Silvers DN. Discordance in the histopathologic diagnosis of difficult melanocytic neoplasms in the clinical setting. J Cutan Pathol . 2008;35(4):349-352. doi:10.1111/j.1600-0560.2007.00970.x

11 . Haenssle HA, Fink C, Schneiderbauer R, et al; Reader study level-I and level-II Groups. Man against machine: diagnostic performance of a deep learning convolutional neural network for dermoscopic melanoma recognition in comparison to 58 dermatologists. Ann Oncol . 2018;29(8):18361842. doi:10.1093/annonc/mdy166

12 . Yu C, Yang S, Kim W, et al. Acral melanoma detection using a convolutional neural network for dermoscopy images. PLoS One . 2018;13(3):e0193321. doi:10.1371/journal.pone.0193321

13 . Tschandl P, Codella N, Akay BN, et al. Comparison of the accuracy of human readers versus machine-learning algorithms for pigmented skin lesion classification: an open, web-based, international, diagnostic study. Lancet Oncol . 2019;20(7):938-947. doi:10.1016/S1470-2045(19) 30333-X

14 . Marchetti MA, Liopyris K, Dusza SW, et al; International Skin Imaging Collaboration. Computer algorithms show potential for improving dermatologists' accuracy to diagnose cutaneous melanoma: results of the International Skin Imaging Collaboration 2017. J Am Acad Dermatol . 2020;82 (3):622-627. doi:10.1016/j.jaad.2019.07.016

15 . Hekler A, Utikal JS, Enk AH, et al. Deep learning outperformed 11 pathologists in the classification of histopathological melanoma images. Eur J Cancer . 2019;118:91-96. doi:10.1016/j.ejca.2019.06.012

16 . Brinker TJ, Schmitt M, Krieghoff-Henning EI, et al. Diagnostic performance of artificial intelligence for histologic melanoma recognition compared to 18 international expert pathologists. J Am Acad Dermatol . 2022;86(3):640-642. doi:10.1016/j.jaad.2021.02.009

17 . Muti HS, Heij LR, Keller G, et al. Development and validation of deep learning classifiers to detect Epstein-Barr virus and microsatellite instability status in gastric cancer: a retrospective multicentre cohort study. Lancet Digit Health . 2021;3(10): e654-e664. doi:10.1016/S2589-7500(21)00133-3

18 . Campanella G, Hanna MG, Geneslaw L, et al. Clinical-grade computational pathology using jamadermatology.com

weakly supervised deep learning on whole slide images. Nat Med . 2019;25(8):1301-1309.

doi:10.1038/s41591-019-0508-1

19 . Echle A, Grabsch HI, Quirke P, et al. Clinical-grade detection of microsatellite instability in colorectal tumors by deep learning. Gastroenterology . 2020;159(4):1406-1416.e11. doi:10.1053/j.gastro.2020.06.021

20 . Warnat-Herresthal S, Schultze H, Shastry KL, et al; COVID-19 Aachen Study (COVAS); Deutsche COVID-19 Omics Initiative (DeCOI). Swarm learning for decentralized and confidential clinical machine learning. Nature . 2021;594(7862):265-270. doi:10.1038/s41586-021-03583-3

21 . Li Y, Chen C, Liu N, Huang H, Zheng Z, Yan Q. Ablockchain-based decentralized federated learning framework with committee consensus. IEEE Netw . 2021;35(1):234-241. doi:10.1109/MNET. 011.2000263

22 . Bdair T, Navab N, Albarqouni S. Semi-supervised federated peer learning for skin lesion classification. MELBAJ . 2022;1:011. doi:10.59275/j.melba.2022-8g82

23 . Agbley BLY, Li J, Haq AU, et al. Multimodal melanoma detection with federated learning. In: 2021 18th International Computer Conference on Wavelet Active Media Technology and Information Processing (ICCWAMTIP). IEEE; 2021.

24 . Adnan M, Kalra S, Cresswell JC, Taylor GW, Tizhoosh HR. Federated learning and differential privacy for medical image analysis. Sci Rep . 2022;12 (1):1953. doi:10.1038/s41598-022-05539-7

25 . Dayan I, Roth HR, Zhong A, et al. Federated learning for predicting clinical outcomes in patients with COVID-19. Nat Med . 2021;27(10):1735-1743. doi:10.1038/s41591-021-01506-3

26 . Saldanha OL, Quirke P, West NP, et al. Swarm learning for decentralized artificial intelligence in cancer histopathology. Nat Med . 2022;28(6): 1232-1239. doi:10.1038/s41591-022-01768-5

27 . Lu MY, Chen RJ, Kong D, et al. Federated learning for computational pathology on gigapixel whole slide images. MedImage Anal . 2022;76: 102298. doi:10.1016/j.media.2021.102298

28 . Bossuyt PM, Reitsma JB, Bruns DE, et al; STARD Group. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. BMJ . 2015;351:h5527. doi:10.1136/bmj. h5527

29 . Bankhead P, Loughrey MB, Fernández JA, et al. QuPath: open source software for digital pathology image analysis. Sci Rep . 2017;7(1):16878.

doi:10.1038/s41598-017-17204-5

30 . Bergstra J, Bardenet R, Bengio Y, Kégl B. Algorithms for hyper-parameter optimization. Accessed March 4, 2023. https://proceedings. neurips.cc/paper/2011/file/ 86e8f7ab32cfd12577bc2619bc635690-Paper.pdf

31 . Akiba T, Sano S, Yanase T, Ohta T, Koyama M. Optuna: a next-generation hyperparameter

optimization framework. In: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery . Association for Computing Machinery; 2019: 2623-2631. doi:10.1145/3292500. 3330701

32 . Smith LN. A disciplined approach to neural network hyper-parameters: part 1-learning rate, batch size, momentum, and weight decay. arXiv . Preprint posted online March 26, 2018. doi:10.48550/arXiv.1803.09820

33 . Paszke A, Gross S, Massa F, et al. PyTorch: an imperative style, high-performance deep learning library. In: Wallach H, Larochelle H, Beygelzimer A, d' Alché-Buc F, Fox E, Garnett R, eds. Advances in Neural Information Processing Systems . Vol 32. Curran Associates Inc; 2019. https://proceedings.neurips.cc/paper/2019/file/ bdbca288fee7f92f2bfa9f7012727740-Paper.pdf

34 . Howard J, Gugger S. Fastai: a layered API for deep learning. Information . 2020; 11(2):108. doi:10.3390/info11020108

35 . Efron B, Tibshirani RJ. An Introduction to the Bootstrap . CRC Press; 1994. doi:10.1201/ 9780429246593

36 . McMahan HB, Moore E, Ramage D, Hampson S, Arcas BAY. Communication-efficient learning of deep networks from decentralized data. arXiv . Preprint posted online February 17, 2016. doi:10.48550/arXiv.1602.05629

37 . Kather JN, Pearson AT, Halama N, et al. Deep learning can predict microsatellite instability directly from histology in gastrointestinal cancer. Nat Med . 2019;25(7):1054-1056. doi:10.1038/ s41591-019-0462-y

38 . Maji D, Santara A, Mitra P, Sheet D. Ensemble of deep convolutional neural networks for learning to detect retinal vessels in fundus images. arXiv . Preprint posted online March 15, 2016. doi:10.48550/arXiv. 1603.04833

39 . Leitlinienprogramm Onkologie. Diagnostik, therapie und nachsorge des melanoms. Langversion 3.3; July 2020, AWMF Registernummer: 032/024OL. Publication in German. Accessed August 29, 2023. https://www. leitlinienprogramm-onkologie.de/fileadmin/user_ upload/Downloads/Leitlinien/Melanom/Melanom_ Version_3/LL_Melanom_Langversion_3.3.pdf

40 . Kairouz P, McMahan HB, Avent B, et al. Advances and open problems in federated learning. arXiv . Preprint posted online March 9, 2021. doi:10.48550/arXiv.1912.04977

41 . Hauser K, Kurz A, Haggenmüller S, et al. Explainable artificial intelligence in skin cancer recognition: a systematic review. Eur J Cancer . 2022;167:54-69. doi:10.1016/j.ejca.2022.02.025

42 . Jutzi TB, Krieghoff-Henning EI, Holland-Letz T, et al. Artificial intelligence in skin cancer diagnostics: the patients' perspective. Front Med (Lausanne) . 2020;7:233. doi:10.3389/fmed.2020. 00233

