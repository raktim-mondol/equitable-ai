<!-- Page 1 -->

nature

medicine
ARTICLES
https://doi.org/10.1038/s41591-019-0508-1

# Clinical-grade computational pathology with weakly supervised deep learning on whole slide images

Gabriele Campanella1,2, Matthew G. Hanna1, Luke Geneslaw1, Allen Mirafra1,Vitor Werneck Krauss Silva1, Klaus J. Busam1, Edi Brogi1, Victor E. Reuter1, David S. Klimstra1and Thomas J. Fuchs1,2*

The development of decision support systems for pathology and their deployment in clinical practice have been hindered by the need for large manually annotated datasets. To overcome this problem, we present a multiple instance learning-based deep learning system that uses only the reported diagnoses as labels for training, thereby avoiding expensive and time-consuming pixel-wise manual annotations. We evaluated this framework at a pathology conference using 15,187 patient images from 15,187 patients without any form of data curation. Tests on prostate cancer, basal cell carcinoma and breast cancer metastases to axillary lymph nodes resulted in areas under the curve above 0.98 for all cancer types. Its clinical application would allow pathologists to exclude 95% of slides while retaining 100% sensitivity. Our results show that this system has the ability to train accurate classification models at unprecedented scale, laying the foundation for the deployment of computational decision support systems in clinical practice.

Pathology is the cornerstone of modern medicine and, in particular, cancer care. The pathologist's diagnosis on glass slides is the basis for clinical and pharmaceutical research and, more importantly, for the decision on how to treat the patient. Nevertheless, the standard practice of microscopy for diagnosis, grading and staging of cancer has remained nearly unchanged for a century1,2. While other medical disciplines, such as radiology, have a long history of research and clinical application of computational approaches, pathology has remained in the background of the digital revolution. Only recently has computational pathology emerged as a potential new standard of care where glass slides are digitized into whole slide images (WSIs) using digital slide scanners. As scanner technologies have become more reliable, and WSIs increasingly available in larger numbers, the field of computational pathology has emerged to facilitate computer-assisted diagnostics and to enable a digital workflow for pathologists3–5. These diagnostic decision support tools can be developed to empower pathologists' efficiency and accuracy to ultimately provide better patient care.

Traditionally, predictive models used in decision support systems for medical image analysis relied on manually engineered feature extraction based on domain knowledge and pathologists were intrinsically domain specific and their performance was, in general, not sufficient for clinical applications. This approach was changed in recent years based on the development of deep learning, a form of deep learning in solving image classification tasks, such as classification and categorization on ImageNet6–10, where high-capacity deep neural network models have been reported to surpass human performance11.

The medical image analysis field has seen widespread application of deep learning, showing in some cases that clinical impact can be achieved for diagnostic tasks. Notably, ref.12 reported dermatologist-level diagnosis of dermoscopy images, while ref.13

showed ophthalmologist-level performance on optical coherence tomography images.

Computational pathology, compared with other fields, has to face additional challenges related to the nature of pathology data generation. The lack of large annotated datasets is even more severe than in other domains. This is due in part to the novelty of digital pathology and the high cost associated with the digitization of glass slides. Furthermore, pathology images are tremendously large: glass slides scanned at 20× magnification (0.5µm/pixel-1) produce image files of several gigabytes; about 470 WSIs contain roughly the same number of pixels as the entire ImageNet dataset. Leveraging the peculiarity of pathology datasets has led most efforts in computational pathology to apply supervised learning for classifying small tiles within a WSI14–16. This usually requires extensive annotations at the pixel level by expert pathologists. For these reasons, state-of-the-art pathology datasets are small and heavily curated. The CAMELYON16 challenge for breast cancer metastasis detection17 contains one of the largest labeled datasets in the field, with a total of 400 non-exhaustively annotated WSIs.

Applying deep learning for supervised classification on these small datasets has yielded promising results. Of note, the CAMELYON16 challenge reported performance on par with that of pathologists in discerning between benign tissue and metastatic breast cancer17. Yet, the limitations of these models in clinical practice remains in question because of the wide variance of these small samples that is not captured in small datasets. Experiments presented in this article will substantiate this claim.

To further address the shortcomings of current computational approaches and enable clinical deployment of decision support tools requires training and validation of models on large-scale datasets representative of the wide variance of cases encountered every day in the clinic. At that scale, reliance on expensive and

Department of Pathology, Memorial Sloan Kettering Cancer Center, New York, NY, USA. *Weill Cornell Graduate School of Medical Sciences, New York, NY, USA. *e-mail: fuchs@mskcc.org

NATURE MEDICINE | (2019) 23:1087–1090 | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1301

---

<!-- Page 2 -->

ARTICLES

NATURE MEDICINE

time-consuming, manual annotations is impossible. We address all of these issues by collecting a large computational pathology dataset and by proposing a new framework for training classification models at a very large scale without the need for pixel-level annotations. Furthermore, in light of the results we present in this work, we will formalize the concept of clinical-grade decision support systems, proposing—in contrast with the existing literature—a new measure for clinical applicability.

The main contributions of this work are the scale at which we learn classification models. We collected three datasets in the field of computational pathology: (1) a prostate core biopsy dataset consisting of 24,852 images, (2) a breast tissue dataset consisting of (3) a breast metastasis to lymph nodes dataset of 9,894 slides. Each of these datasets is at least one order of magnitude larger than all other datasets in the field. To put this in the context of other computer pathology problems, we collected 100,000 images from 200 to 88 ImageNet datasets (Fig. 1a). It is important to stress that the data were not curated. The slides collected for each tissue type represent equivalent requirements for a clinical pathology dataset and are representative of slides generated in a true pathology laboratory, including common artifacts, such as air bubbles, microscopy knife slicing irregularities, fixation problems, cauterity, folds and cracks, as well as digitalization artifacts. The datasets are heterogeneous across the three tissue types, we included 17,661 external slides, which were produced in the pathology laboratories of their respective countries and were annotated by pathologists from these countries (Extended Data Fig. 1), illustrating the unprecedented technical variability included in a computational pathology study.

The datasets chosen represent different but complementary views of clinical practice, and offer insight into the types of challenges a flexible and robust decision support system should be able to solve. Prostate cancer is the leading source of new cancer cases and the second most frequent cause of death among men after lung cancers34. Multiple studies have shown that prostate cancer diagnosis has a high inter- and intraobserver variability35–37 and is frequently based on the presence of very small lesions that comprise <10% of the entire prostate gland. The small size of the lesions makes them poorly reproducible and aiding in the diagnosis of cases with low tumor volume are examples of how decision support systems can improve patient care. The skin cancer basal cell carcinoma (BCC) rarely causes metastases or death38. In its most common form (nodular), pathologists can readily identify and diagnose the lesion. With approximately 4.3 million individuals diagnosed annually in the United States39, the large number of cases in this scenario, a decision support system should increase clinical efficiency by streamlining the work of the pathologist.

Finally, we leverage the large amount of information unfashionable to rely on supervised learning, which requires manual annotations. Instead, we propose to use the slide-level diagnosis, which is readily available from anatomic pathology laboratory information systems (LISs) or electronic medical records. The decision support model in a weakly supervised manner. Crucially, diagnostic data retrieved from pathology reports are easily scalable, as opposed to expert annotation which is time-consuming and expensive at scale. To be more specific, the slide-level diagnosis casts a weak label at all tiles within a particular WSI. In addition, we know that if the slide is negative, all of its tiles must also be negative and not conversely. In contrast, if the slide is positive, then at least one of all of the possible tiles contains tumor. This formalization of the WSI classification problem is an example of the general model multiple instance learning (MIL) problem, which was first described in ref.40. Multiple instance learning (MIL) has since been widely applied in many machine learning domains, including computer vision41–43.

Current methods for weakly supervised WSI classification rely on deep learning models trained under variants of the MIL assumption.

Typically, a two-step approach is used, where first a classifier is trained with MIL at the tile level and then the predicted scores for each tile within a WSI are aggregated, usually by combining (pooling) their results with various strategies44, or by learning a fusion model45. Inspired in these works, we developed a novel framework that leverages MIL to train deep neural networks, resulting in a semantically rich tile-level feature representation. These representations are then used as an input to a recurrent neural network (RNN) to integrate the information across the whole slide and report the final classification result (Fig. 1c,d).

## Results

Test performance of ResNet34 models trained with MIL for each tissue type. We trained ResNet34 models to classify tiles using MIL. At test time, a slide is predicted positive if at least one tile is predicted positive. We trained ResNet34 with this slide-level classification directly from the standard multiple instance assumption and is generally referred to as max-pooling. Performance on the test set was measured for models trained at different magnifications for each dataset (Extended Data Fig. 2). Histology contains information at different scales, and pathologists review patient tissue on glass slides at varying zoom levels. For example, in prostate histopathology, the histological and cytological features are both important for diagnosis and are more easily appreciated at different magnifications. For prostate, the highest magnification consistently gave better performance. For BCC and axillary lymph nodes, the 5× magnification showed higher accuracy (Extended Data Fig. 2b). Interestingly, the error modes on the test set across magnification conditions were complementary: in prostate, the 20× model performed better on cases of false negatives, while the 5× model performed better on false positives. Simple ensemble models were generated by max-pooling the response across the different magnifications. We note that these naive ensemble models outperform the single-scale models for the prostate dataset in terms of accuracy and area under the curve (AUC), but not for the other datasets. Models trained at 20× achieved AUCs of 0.986, 0.986 and 0.965 on the test set for prostate, BCC and axillary lymph nodes, respectively, highlighting the efficacy of the proposed method in discerning tumor regions from benign regions in a wide variety of tissue types.

Dataset size dependence of classification accuracy. We conducted experiments to determine whether the dataset was large enough to achieve good performance. For prostate, for these experiments, the prostate dataset (excluding the test portion) was split in a common validation set with 2,000 slides and training sets of different sizes (10,000, 20,000, 30,000, 40,000, 50,000, and 60,000). The training dataset being a superset of all of the previous datasets. The results indicate that while the validation error is starting to saturate, further improvement can be expected from even larger datasets (Extended Data Fig. 2c,d and axillary). Although the number of slides needed to achieve satisfactory results may vary by tissue type, we observed that, in general, at least 10,000 slides are necessary for good performance.

Model introspection by visualization of the feature space in two dimensions. To gain insight into the models' representation of histopathology, we visualized the learned feature space in two dimensions so that tiles that have similar features according to the model are shown close to each other (see Fig. 2b,c for the prostate dataset, BCC and axillary lymph nodes and axillary lymph nodes models). The prostate model shows a large region of different stroma tiles at the center of the plot in Fig. 2c, extending towards the top right corner. The top left corner is where benign-looking tiles are located. The bottom right corner contains tiles with glands and edge tiles. The discriminative tiles with high tumor probability

1302

NATURE MEDICINE | VOL 25 | OCT 2019 | 1301–1309 | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 3 -->

NATURE MEDICINE

ARTICLES

a

| Dataset | Years | Slides | Patients | Positive slides | External slides | ImageNet |
| --- | --- | --- | --- | --- | --- | --- |
| Prostate in house | 2016 | 12,132 | 836 | 2,402 | 0 | 19.8x |
| Prostate external | 2015–2017 | 12,727 | 6,323 | 12,413 | 12,727 | 29.0x |
| Skim | 2016–2017 | 9,962 | 5,325 | 1,659 | 3,710 | 21.4x |
| Axillary lymph nodes | 2013–2018 | 9,894 | 2,703 | 2,521 | 1,224 | 18.2x |
| Total |   | 44,732 | 15,187 |   |   | 88.4x |

b

29,840 px / 15.3 mm

63,744 px / 31.9 mm

3,000 px / 1.5 mm

1,200 px / 600 μm

300 px / 150 μm

c

Clinically relevant dataset

Slide tiling

Inference Classifier CNN

Tile probability

Ranked tiles

Learning Top tiles

Slide targets

1

0

0

d

Trained MIL model

Tumor probability

1.0

0.5

RNN aggregation

Diagnosis

MIL-based representation

1 2 3 4 5 6

Fig. 1 | Overview of the data and proposed deep learning framework presented in this study. a, Description of the datasets. This study is based on a total of 44,732 slides from 15,187 patients across three different tissue types: prostate, skin and axillary lymph nodes. The prostate dataset was divided into in-house slides and consultation slides to test for staining bias. The class imbalance varied from 1:4 for prostate to 1:3 for breast. A total of 17,661 slides were submitted to MSK from more than 800 outside institutions in 45 countries for a second opinion. To put the size of our dataset into context, the last column shows a comparison, in terms of the pixel count, with ImageNet—the state of the art in computer vision, containing over 14 million images. b, Left, hematoxylin and eosin slide of a biopsy showing prostatic adenocarcinoma. The diagnosis can be based on very small foci of cancer that account for <1% of the tissue surface. In the slide to the left, only about six small tumor glands are present. The right-most image shows an example of a malignant gland. Its relation to the entire slide is put in perspective to reiterate the difficulty of the task. c, The MIL training procedure includes a full inference pass through the dataset, to rank the tiles according to their probability of being positive, and learning on the top-ranked tiles per slide. CNN, convolutional neural network. d, Slide-level aggregation with a recurrent neural network (RNN). The 5 most suspicious tiles in each slide are sequentially passed to the RNN to predict the final slide-level classification.

are clustered in two regions at the bottom and left of the plot. A closer look reveals the presence of malignant glands. Interestingly, a subset of the top-ranked tiles with a tumor probability close to 0.5, indicating uncertainty, are tiles that contain glands suspicious of being malignant.

Comparison of different slide aggregation approaches. The max-pooling operation that leads to the slide prediction under the MIL assumption is not robust. A single spurious misclassification can change the slide prediction, possibly resulting in a large number of false positives. One way to mitigate this type of mistake is to learn a slide aggregation model on top of the MIL classification results.

For example, Hou et al.30 learned a logistic regression based on the number of tiles per class as predicted by an ensemble of tile classifiers. Similarly, Wang et al.31 extracted geometrical features from the tumor probability heat map generated by a tile-level classifier and trained a random forest model, winning the CAMELYON16 challenge. Following the latter approach, we trained a random forest model on manually engineered features extracted from the heat map generated by our MIL-based tile classifier. For prostate cancer classification, the random forest trained on the validation split at 20× magnification produced an AUC of 0.98 on the test set, which was not statistically significantly different from MIL alone (Extended Data Fig. 4). Although this procedure drastically decreased the false

NATURE MEDICINE | VOLUME 25 | AUGUST 2019 | 1300–1309 | www.nature.com/naturemedicine

1303

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 4 -->

ARTICLES

NATURE MEDICINE

Fig. 2 | Dataset size impact and model introspection. a, Dataset size plays an important role in achieving clinical-grade MIL classification performance. Training of ResNet34 was performed with datasets of increasing size, for every reported training set size, five models were trained, and the validation errors are reported as box plots (n=5). This experiment underlies the fact that a large number of slides are necessary for generalization of learning under the MIL assumption. b, c, The prostate model has learned a rich feature representation of histopathology tiles. b, A ResNet34 model trained at 20x was used to obtain the feature embedding before the final classification layer for a random set of tiles in the test set (n=182,912). The embedding was reduced to two dimensions with t-SNE and plotted using a hexagonal heat map. Top-ranked tiles coming from negative and positive slides are represented by points colored by their tumor probability. c, Tiles corresponding to points in the two-dimensional t-SNE space were randomly sampled from different regions. Abnormal glands are clustered together on the bottom and left sides of the plot. A region of tiles with a tumor probability of < 0.5 contains glands with features suspicious for prostatic adenocarcinoma. Normal glands are clustered on the top left region of the plot. Dataset size plays an important role in achieving clinical-grade MIL classification performance. Training of ResNet34 was performed with datasets of increasing size; for every reported training set size, five models were trained, and the validation errors are reported as box plots (n=5). This experiment underlies the fact that a large number of slides are necessary for generalization of learning under the MIL assumption. b, c, The prostate model has learned a rich feature representation of histopathology tiles. b, A ResNet34 model trained at 20x was used to obtain the feature embedding before the final classification layer for a random set of tiles in the test set (n=182,912). The embedding was reduced to two dimensions with t-SNE and plotted using a hexagonal heat map. Top-ranked tiles coming from negative and positive slides are represented by points colored by their tumor probability. c, Tiles corresponding to points in the two-dimensional t-SNE space were randomly sampled from different regions. Abnormal glands are clustered together on the bottom and left sides of the plot. A region of tiles with a tumor probability of < 0.5 contains glands with features suspicious for prostatic adenocarcinoma. Normal glands are clustered on the top left region of the plot.

positive rate, and at 20x achieved a better balanced error than the basic max-pooling aggregation, this came with an unacceptable decrease in sensitivity.

The previous aggregation methods do not take advantage of the information contained in the feature representation learned during training. Given a vector representation of tiles, even if singularly they were not classified as positive by the tile classifier, taken together they could be suspicious enough to trigger a positive response by a representation-based slide-level classifier. Based on these ideas and

empirical support from ref.11, we introduce an RNN-based model that can integrate information at the representation level to emit a final slide classification (Fig. 1d). Interestingly, information can also be integrated across the various magnifications to produce a multiscale classification. At 20x, the MIL-RNN models resulted in 0.991, 0.989 and 0.965 AUCs for the prostate, BCC and breast metastases datasets, respectively (Fig. 3). For the prostate experiment, the MIL-RNN method was statistically significantly better than max-pooling aggregation. The multiscale approach was tested on the prostate

1304

NATURE MEDICINE | VOL 25 | AUGUST 2019 | 1301–1309 | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 5 -->

NATURE MEDICINE

ARTICLES

Fig. 3 | Weakly supervised datasets achieve high performance across all tissue types. a, The performances of the models trained at 20× magnification on the respective tissue datasets were measured in terms of AUC for each tumor type. a, For prostate cancer (n=1784) the MIL-RNN model significantly (P<0.0001) outperformed the model trained with MIL alone, resulting in an AUC of 0.998 (a). b, The BCC model (n=1375) performed at 0.988 (b), while breast metastases detection (n=1473) achieved an AUC of 0.996 (c). For these latter datasets, adding an RNN did not significantly improve performance. Statistical significance was assessed using DeLong's test for two correlated ROC curves.

data, but its performance was not better than that achieved by the single-scale model trained at 20×.

#### Pathology expert analysis of the MIL-RNN error modes.

Pathologists specialized in each discipline analyzed the test set errors made by MIL-RNN models trained at 20× magnification (a selection of cases is presented in Fig. 4a–c). Several discrepancies (six in prostate, eight in BCC and 23 in axillary lymph nodes; see Fig. 4d) were found between the reported case diagnosis and the true slide class (that is, presence/absence of tumor). Because the ground truth is reliant on the diagnosis reported in the LIS, the observed discrepancies can be due to several factors: (1) under the current WSI scanning protocol, as only select slides are scanned in each case, there exists the possibility of a mismatch between the slide scanned and the reported LIS diagnosis linked to each case; (2) a deeper slide level with no carcinoma present could be selected for scanning; and (3) tissue was removed to create tissue microarrays before slide scanning. Encouragingly, the training procedure proved robust to the ground truth noise in our datasets.

For the prostate model, three of the 12 false negatives were correctly predicted as negative by the algorithm. Three other slides showed atypical morphological features, but they were not sufficient to diagnose carcinoma. The confirmed six false negatives were characterized by having a high degree of hyperplastic nuclear morphology corrections to the ground truth, the AUC for the prostate test set improved from 0.991 to 0.994. The 72 false positives were reviewed as well. The algorithm falsely identified small foci of glands as cancer, focusing on small foci of hyperplastic nuclei. The false positives contained at least a few cells with prominent nucleoli. Many of the flagged glands also showed intraluminal secretions. Overall, the algorithm was justified in not diagnosing carcinoma in these cases as suspicious, thus fulfilling the requisites of a screening tool.

For the BCC model, four false negatives were corrected to true positives, and four false positives were corrected to true positives. Given these corrections, the AUC improved from 0.988 to 0.994. The 12 cases determined to be false negatives were characterized by low tumor volume. The 15 false positives included squamous cell carcinomas and miscellaneous benign neoplastic and nonneoplastic skin lesions.

For the breast metastasis model, 17 of the initially classified false negatives were correctly classified as negatives, while four slides contained suspicious morphology that would likely require further tests. A total of 21 false negatives were corrected to true positives.

In addition, two false positives were corrected to true positives. False negative to true negative corrections were due to the tissue of interest being present in the slide, the histology and the slide, or sampling error at the time the frozen section was prepared. Several positive to true positive corrections were due to soft tissue metastatic deposits or tumor emboli. The AUC improved from 0.965 to 0.989 given these corrections. Of the 23 false negatives, eight were macro-metastasis, 13 were micro-metastasis and two were isolated tumor cells (ITCs). Notably, 12 cases (four false negatives and eight false positives) showed signs of treatment effect from neoadjuvant chemotherapy.

Investigation of technical variability introduced by slide preparation at multiple institutions and different scanners. Several sources of variability come into play in computational pathology. In addition to all of the morphological variability, technical variability is introduced during glass slide preparation and scanning. How this variability can affect the prediction of an assistive model is a question that must be investigated thoroughly.

Assessing the performance of models on slides digitized on different scanners is crucial for establishing the applicability of the same model in departments with varied scanner vendor workflows or smaller clinics that operate scanners from different vendors and do not have access to the same scanner. We therefore failed to train a model to test the effect of the whole slide scanner type on model performance, we scanned a substantial subset of the in-house prostate test set (1,274 out of 1,784) on a Philips Intelliscan Ultra Fast Scanner that was used to prepare the slides for the Food and Drug Administration for primary diagnostic use. We observed a decrease in performance in terms of AUC of 3% points (Fig. 5a and Extended Data Fig. 5a). Analysis was justified by the fact that the predictions on the two WSIs and their matching Philips digital slides revealed a perceived difference in brightness, contrast and sharpness that could affect the prediction performance. In practice, an effective solution to reducing the generalization error even further could be training on a second dataset or fine-tuning the model on data from the new scanner.

To measure the effects of slide preparation on model performance, we used a very large dataset consisting of over 1,000 slide consultation slides submitted to the Memorial Sloan Kettering Cancer Center (MSK) from other institutions in the United States and abroad. It should be noted that these slides are typically diagnostically challenging and are the basis for the requested expert pathologist review. We applied the MIL-RNN model trained

NATURE MEDICINE | VOLUME 25 | AUGUST 2019 | 1300–1309 | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1305

---

<!-- Page 6 -->

ARTICLES

NATURE MEDICINE

Fig. 4 | Pathology analysis of the misclassification errors on the test sets. a–c Randomly selected examples of classification results on the test set. Examples of true positive, false negative and false positive classifications are shown for each tumor type. The MIL-RNN model trained at 20× magnification was run with a step size of 20 pixels across a region of interest, generating a tumor probability heat map. On every slide, the blue square represents the enlarged area. For the prostate dataset (a), the true positive represents a difficult diagnosis due to tumor found next to atrophy and inflammation; the false negative shows a very low tumor volume; and for the false positive the model identified atypical small acinar proliferation, showing a small focus of glands with atypical epithelial cells. For the BCC dataset (b), the true positive has a low tumor volume; the false negative has a low tumor volume; and for the false positive the tongue of the epithelium abutting from the base of the epidermis shows an architecture similar to BCC. For the axillary lymph nodes dataset (c), the true positive shows ITCs with a neoadjuvant chemotherapy treatment effect; the false negative shows a slightly out of focus cluster of ITCs missed due to the very low tumor volume and blurring; and the false positive shows displaced epithelium/benign papillary inclusion in a lymph node. d Subsequently pathologists analyzed the slides that were misclassified by the MIL-RNN models. While slides can either be positive or negative for a specific tumor, sometimes it is not possible to diagnose a single slide with certainty based on morphology alone. These cases were grouped into the categories ‘atypical’ and ‘suspicious’ for prostate and breast lesions, respectively. The ‘other’ category consisted of skin biopsies that contained tumors other than BCC. We observed that some of the misclassifications stem from incorrect ground truth labels.

at 20× to the large submitted slides dataset and observed a drop of about 6% points in terms of AUC (Fig. 5a and Extended Data Fig. 5a). Importantly, the decrease in performance was mostly seen in the specificity to the new test set, while sensitivity remained high.

Comparison of fully supervised learning with weakly supervised learning. To substantiate the claim that models trained under full supervision on small curated datasets do not translate well to clinical practice, several experiments were performed with the CAMELYON16 dataset11, which includes pixel-wise annotations for 270 training slides and is one of the largest annotated, public digital pathology datasets available. We implemented a model for automatic detection of metastatic breast cancer on the CAMELYON16 dataset, modeled after Wang et al.11—the winning team of the

CAMELYON16 challenge. The approach can be considered state of the art for this task and relies on fully supervised learning and pixel-level expert annotations. The main differences in our implementation of ref. 11 are the architecture used (ResNe43n instead of GoogLeNetv3), their usage of hard negative mining, and the features extracted to train the slide-level random forest classifier. Our implementation achieved an AUC of 0.930 on the CAMELYON16 test set, similar to the 0.925 achieved in ref. 11. This model would have won the classification portion of the CAMELYON16 challenge and would be ranked fifth on the open leaderboard. The same model, trained under full supervision on CAMELYON16, was applied to the MSK test set of the axillary lymph nodes dataset and resulted in an AUC of 0.727, constituting a 20% drop compared with its performance on the CAMELYON16 test set (Fig. 5b, right panel).

1306

NATURE MEDICINE | VOL 35 | AUGUST 2019 | 1301–1309 | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 7 -->

NATURE MEDICINE

ARTICLES

Figure 5 consists of two bar charts, (a) and (b), comparing the Area Under the Curve (AUC) performance of different models. Both charts have an y-axis labeled 'AUC' ranging from 0.5 to 1.0. The x-axis for both charts lists four models: MSK in-house test set (n=1,784), MSK in-house test set (n=1,274), MSK external test set (n=12,420), and MSK test set (n=1,473). The bars represent the mean AUC, with error bars indicating 95% confidence intervals. Red arrows indicate the performance drop from the MSK in-house test set to the MSK test set.

| Model | AUC (Mean) | AUC (95% CI) | Drop to MSK test set (%) |
| --- | --- | --- | --- |
| MSK in-house test set (n=1,784) | ~0.95 | ~0.94 - 0.96 | -8.6% |
| MSK in-house test set (n=1,274) | ~0.95 | ~0.94 - 0.96 | -8.6% |
| MSK external test set (n=12,420) | ~0.95 | ~0.94 - 0.96 | -8.6% |
| MSK test set (n=1,473) | ~0.86 | ~0.85 - 0.87 | -8.6% |

| Model | AUC (Mean) | AUC (95% CI) | Drop to MSK test set (%) |
| --- | --- | --- | --- |
| MSK (n=1,473) | ~0.95 | ~0.94 - 0.96 | -15% |
| CAMELYON16 (n=129) | ~0.95 | ~0.94 - 0.96 | -15% |
| CAMELYON16 (n=129) | ~0.95 | ~0.94 - 0.96 | -15% |
| MSK (n=1,473) | ~0.85 | ~0.84 - 0.86 | -20.2% |

Fig. 5 | Weak supervision on large datasets leads to higher generalization performance than fully supervised learning on small curated datasets. The generalization performance of the proposed prostate and breast models were evaluated on different external test sets. a, Results of the prostate model trained with MIL on MSK in-house slides and tested on: (1) the in-house test set (n=1,784) digitized on Leica Aperio AT2 scanners; (2) the in-house test set tested on a Philips Ultra Fast Scanner (n=1,274); and (3) external slides submitted to Pathology (n=12,427). Performance in terms of AUC decreased by 3 and 6% for the Philips scanner and external slides, respectively. b, Comparison of the proposed MIL approach with state-of-the-art fully supervised learning for breast metastasis detection in lymph nodes. Left, the model was trained on MSK data with our proposed method (MIL-RNN) and tested on the MSK breast data test set (n=1,473) and on the test set of the CAMELYON16 challenge (n=129), showing a decrease in AUC of 15%. Right, a fully supervised model was trained following ref.10 on CAMELYON16 training data. While the resulting model would have won the CAMELYON16 challenge (n=129), its performance drops by over 20% when tested on a larger test representing real-world clinical cases (n=1,473). Error bars represent 95% confidence intervals for the true AUC calculated by bootstrapping each test set.

The reverse experiment, done by training our MIL model on the MSK auxiliary lymph node data and testing it on the CAMELYON16 test data, produced an AUC of 0.899, representing a much smaller drop in performance compared with the 0.965 on the MSK test set (Fig. 5a, left panel).

These results illustrate that current deep learning models, trained on small datasets, even with the advantage of exhaustive, pixel-wise labels, are not able to generalize to clinical-grade, real-world data. We hypothesize that small, well-curated datasets are not sufficient to capture the vast biological and morphological variability of cancer, as well as the technical variability introduced by the staining and preparation processes in histopathology. Our observations urge caution and in-depth evaluation on real-world datasets before applying deep learning models for decision support in clinical practice. These results also show that weakly supervised approaches such as the one proposed here have a clear advantage over conventional fully supervised learning in that they enable training on massive, diverse datasets without the necessity for data curation.

## Discussion

The main hypothesis addressed in this work is that clinical-grade performance can be achieved with weakly supervised learning. To test our hypothesis, we developed a deep learning framework that combines convolutional neural networks with RNNs under a MIL approach. We compiled a large dataset comprising 44,732 slides from 15,187 patients across three different cancer types. We built a state-of-the-art compute cluster that was essential for the feasibility of the project. Extensive validation experiments confirmed the hypothesis and showed that clinical-grade decision support is feasible.

The implications of these results are wide ranging. (1) The fact that manual pixel-level annotation is not necessary allows for the compilation of datasets with much larger magnitudes than in previous studies. (2) This, in turn, allows our algorithm to learn from

the full breadth of slides presented to clinicians from real-life clinical practice, representing the full wealth of biological and technical variability. (3) As a result, no data curation is necessary because the model can learn that artifacts are not important for the classification task. (4) The proposed MIL approach allows the model to train with the proposed method to generalize better to real data that would be observed in pathology practice. (5) The generalization performance is clinically relevant with AUCs greater than 0.98 for all cancer types tested. (6) We rigorously define clinical grade and propose a strategy to integrate this system in the clinical work flow.

Most literature refers to clinical grade in terms of comparison with a human performing the same task, usually under time or other constraints. We suggest that these comparisons are artificial and offer little insight into how to use such systems in clinical practice. We propose a different approach to measure clinical-grade performance. In clinical practice, a case, especially if challenging, is reviewed by multiple pathologists with the help of immunohistochemistry and molecular information in addition to hematoxylin and eosin morphology. The pathologist's comparison information, one can assume that a team of pathologists at a comprehensive cancer center will operate with 100% sensitivity and specificity. Under these conditions, the pathologist's comparison support is not mean not surpassing the performance of pathologists, which is impossible, but achieving 100% sensitivity with an acceptable false positive rate. This formulation lends itself to a clinical application as follows.

At a fully operational digital pathology department, the predictive model is run on each scanned slide. The algorithm sorts cases, and slides within each case, based on the predicted tumor probability, as soon as they are available from the pathology laboratory. During diagnostic reporting, the pathologist is presented with the model's recommendations through an interface that would flag possible slides for rapid review in a screening scenario, or disregard all benign slides in a diagnostic scenario. In this latter case, we show

NATURE MEDICINE | VOLUME 25 | AUGUST 2019 | 1300–1309 | www.nature.com/naturemedicine

1307

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 8 -->

ARTICLES

NATURE MEDICINE

Fig. 6 | Impact of the proposed decision support system on clinical practice. a, By ordering the cases, and slides within each case, based on their tumor probability, pathologists can focus their attention on slides that are probably positive for cancer. b, Following the algorithm's prediction would allow pathologists to potentially ignore more than 75% of the slides while retaining 100% sensitivity for prostate cancer at the case level (n = 1,754).

in Fig. 6. (See Extended Data Fig. 6 for BCC and breast metastases) that our prostate model would allow the removal of more than 75% of the slides from the workload of a pathologist without any loss in sensitivity at the patient level. For pathologists who must operate in the increasingly complex, detailed and data-driven environment of cancer diagnostics, tools such as this will allow non-subspecialized pathologists to confidently and efficiently classify-cancer with 100% sensitivity.

## Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of code and data availability and associated accession codes are available at https://doi.org/10.1038/s41591-019-01008-1.

Received 23 October 2018; Accepted: 3 June 2019;

Published online: 15 July 2019

## References

1. Bull, C. S. The early history of the compound microscope.Bios. Sci.51: 60 (1986).
2. Hajdu, S. Microscopic contributions of pioneer pathologists.Ann. Clin. Lab. Med.41: 201–206 (2011).
3. Fuchs, T., T. Wild, F. J. Moch, H. E. Buhmann, J. M. Computational pathology analysis of tissue microarrays predicts survival of renal clear cell carcinoma patients. InProc. International Conference on Medical Image Computing and Computer-Assisted Intervention 1–8 (Lecture Notes in Computer Science Vol. 5432). Springer, 2008.
4. Fuchs, T., & Buhmann, J. M. Computational pathology: challenges and promises for tissue analysis.Comput. Med. Imaging Graph.35, 515–530 (2011).
5. Louis, D. N. et al. The Computational pathology—a path ahead.Arch. Pathol. Lab. Med.140: 41–50 (2016).
6. McDonnell, B. & Hinton, G. Deep learning.Nature521: 436–444 (2014).
7. Deng, J. et al. ImageNet: a large-scale hierarchical image database. InProc. IEEE Conference on Computer Vision and Pattern Recognition248–255 (IEEE, 2009).
8. Krizhevsky, A., Sutskever, I. & Hinton, G. E. ImageNet classification with deep convolutional neural networks.Adv. Neural Inf. Process. Syst.1097–1105 (2012).
9. He, Y., K. & Zisserman, A. Very deep convolutional networks for large-scale image recognition. Preprint athttps://arxiv.org/abs/1409.1556(2014).
10. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. Preprint athttps://arxiv.org/abs/1512.03385(2015).
11. Esteva, A. J. et al. Dermatologist-level classification of skin cancer with deep neural networks.Nature542: 115–118 (2017).
12. De Fava, P. J. et al. Clinically applicable deep learning for diagnosis and referral in retinal disease.Nat. Med.24: 1342–1350 (2018).

1. Liu, Y. et al. Detecting cancer metastases on gigapixel pathology images. Preprint athttps://arxiv.org/abs/1703.04421(2017).
2. Das, K., Karki, S. P. K., Guha Roy, A., Chatterjee, J. & Sheet, D. Classifying histopathology whole-slides using fusion of decisions from deep convolutional networks on a collection of random multi-views at Biomedical Imaging. In2017 IEEE 14th International Symposium on Biomedical Imaging1024–1027 (IEEE, 2017).
3. Vallone, M. et al. Metastatic detection from whole slide images using local features and random forests.Cytom. Part A91: 555–565 (2017).
4. Bejourni, R. E. et al. Deep convolutional neural networks to identify and classify tumor-associated stroma in diagnostic breast biopsies.Med. Radiol.91: 1502–1512 (2018).
5. Mobadersary, P. et al. Predicting cancer outcomes from histology and genomics using convolutional networks.Proc. Natl. Acad. Sci. USA115, 12970–12979 (2018).
6. Wang, D., Khoda, A., Gargoya, R., Irshad, H. & Beck, A. H. Deep learning for identifying metastatic breast cancer. Preprint athttps://arxiv.org/abs/1606.05718(2016).
7. Janowczyk, A. & Madabhushi, A. Deep learning for digital pathology image analysis: a comprehensive tutorial with selected use cases.J. Pathol. Inform.7, 29 (2016).
8. Litvin, G. et al. Deep learning as a tool for increased accuracy and efficiency of histopathological diagnosis.Sci. Rep.6, 26386 (2016).
9. Coudray, N. et al. Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning.Nat. Med.24, 1559–1567 (2018).
10. Olsen, T. et al. Diagnostic performance of deep learning algorithms applied to three common diagnoses in dermatopathology.J. Pathol. Inform.9, 32 (2018).
11. Etheiressan Bejourni, R. et al. Diagnostic assessment of deep learning algorithms for detection of lymph node metastases in women with breast cancer.J. Am. Med. Assoc.318, 2199–2210 (2017).
12. Sogel, R. L., Miller, K. D. & Jemal, A. Classifying metastatic cancer.Clin. Cancer J.16: 66–70 (2016).
13. Ozawa, S. et al. A. Intracerebral and intraventricular reproducibility of WHO and Gleason histologic grading systems in prostatic adenocarcinomas.Int. Urol. Nephrol.28, 73–77 (1986).
14. Saunders, D. R. Histologic grading of carcinoma reproducibility of histologic grading.APMIS83, 67–71 (1985).
15. Gleason, D. F. Histologic grading of prostate cancer: a perspective.Hum. Pathol.23, 273–279 (1992).
16. Leblot, P. E. et al.Pathology and Genetics of Skin Tumours(IARC Press, 2006).
17. Chen, J., H. & K. J. et al. Histologic grading. In A. A. J. & C. D. Goldstein, B. M. Incidence estimate of nonmelanoma skin cancer (keratinocyte carcinomas) in the US population. Preprint athttps://arxiv.org/abs/1011.1066(2013).
18. Dieterich, E. G., Lathrop, R. H. & Lozano-Perez, T. Solving the multiple instance problem with axis-parallel rectangles.Artif. Intell.89, 31–51 (1996).
19. Andrews, S., Hofmann, T. & Tschandharani, J. Multiple instance learning with generalist deep learning machines. In A. A. J. & J. 943–944 (AAAI, 2012).
20. Nakul, V. Learning from Data with Low Intrinsic Dimensionality (Univ. California, 2012).

1308

NATURE MEDICINE | Vol. 25 | August 2019 | 1301–1309 | 
[www.nature.com/naturemedicine](https://www.nature.com/naturemedicine)

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 9 -->

NATURE MEDICINE

ARTICLES

33. Zhang, C., Plati, J. C. & Viola, P. A. Multiple instance boosting for object detection. Adv. Neural Inf. Process. Syst. 1417–1424 (2006).

34. Zhang, Q. & Goldman, S. A. EM-DD: an improved multiple-instance learning technique. Adv. Neural Inf. Process. Syst. 1073–1080 (2002).

35. Kraus, O. Z., Ba, J. L. & Frey, B. J. Classifying and segmenting microscopy images with deep multiple instance learning. Bioinformatics 32, i52–i59 (2016).

36. Hou, L. et al. Patch-based convolutional neural network for whole slide tissue image classification. In Proc. IEEE Conference on Computer Vision and Pattern Recognition 2424–2433 (IEEE, 2016).

37. Bychkov, D. et al. Deep learning based tissue analysis predicts outcome in colorectal cancer. Sci. Rep. 8, 3395 (2018).

### Acknowledgements

We thank The Warren Alpert Center for Digital and Computational Pathology and MSK's high-performance computing team for their support. We also thank J. Samboy for leading the digital scanning initiative and E. Stamou and F. Cao, from the pathology informatics team at MSK, for their invaluable help querying the digital slide and LIS databases. We are in debt to P. Schiffer for extending the digital whole slide viewer specifically for this study and for supporting its use by the whole research team. Finally, we thank G. Virgo for managing the project, D. V. K. Yalagadda for development support and D. Schum for help editing the manuscript. This research was funded in part through the NIH/NCI Cancer Center Support Grant P30 CA008748.

### Author contributions

G.G. and T.I.F. designed the experiments. G.G. wrote the code, performed the experiments and analyzed the results. L.G. queried MSK's WSI database and transferred the digital slides to the compute cluster. V.W.K.S. and V.E.R. reviewed the prostate cases.

K.I.B. reviewed the BCC cases. M.G.H. and E.B. reviewed the breast metastasis cases. A.M. classified the free text diagnosis for the BCC cases. G.G., D.S.K. and T.I.F. conceived the project. All authors contributed to preparation of the manuscript.

### Competing interests

T.I.F. is the Chief Scientific Officer of Paige AI. T.I.F. and D.S.K. are co-founders and equity holders of Paige AI. M.G.H., V.W.K.S., D.S.K. and V.E.R. are consultants for Paige AI. V.E.R. is a consultant for Cepheid. M.G.H. is on the medical advisory board of PathFinder. D.S.K. has received speaking/consulting compensation from Merck. G.G. and T.I.F. have intellectual property interests relevant to the work that is the subject of this paper. MSK has financial interests in Paige AI, and intellectual property interests relevant to the work that is the subject of this paper.

### Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41591-019-0508-1.

Supplementary information is available for this paper at https://doi.org/10.1038/s41591-019-0508-1.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to T.I.F.

Peer review information: Javier Carmona was the primary editor on this article and managed its editorial process and peer review in collaboration with the rest of the editorial team.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature America, Inc. 2019

NATURE MEDICINE | VOLUME 25 | AUGUST 2019 | 1301–1309 | 
[www.nature.com/naturemedicine](http://www.nature.com/naturemedicine)

Content courtesy of Springer Nature, terms of use apply. Rights reserved

1309

---

<!-- Page 10 -->

ARTICLES

NATURE MEDICINE

Methods

Hardware and software. All experiments were conducted on MSKs high-performance computing cluster. In particular, we took advantage of seven NVIDIA DGX-1 compute nodes, each containing eight V100 GPU physics processing units (GPUs) and 8TB SSD local storage. Each model was trained on a single GPU (NVIDIA JetPack3.5, version 3.4.1) using the MSK files directly, and Pytorch® (version 1.0) for data loading, building models and training. The final statistical analysis was performed in R® (version 3.3.3), using RPROC® (version 0.3.0) for receiving operating characteristics (ROC) statistics and ggplot2 (version 3.0.0) for generating plots.

Statistics. AUCs for the various ROC curves were calculated in R with pROC. Confidence intervals were computed with the pROC package® using bootstrapping with 1,000 samples, uncorrected for multiple testing by Carpenter and Beitel®. Pairs of AUCs were compared with the pROC package using the two-tailed Delong's test for two correlated ROC curves®.

WSI datasets. We collected three large datasets of hematoxylin and eosin-stained digital images for the following tasks: (1) histological classification, (2) tumor classification, and (3) the detection of breast cancer metastasis in axillary lymph nodes. The first two tasks were performed on the histological classification dataset scanned at 40 μm with Leica Aperio AT2 scanners at 20× equivalent magnification (0.5 μm/pixel2). Each dataset was randomly divided at the patient level in training (70%), validation (10%) and test (20%) sets. The third task was performed using hyper-parameter tuning and model selection. The final models were run on the test set (20%) to evaluate performance.

The prostate dataset consisted of 12,132 needle biopsy slides produced and scanned at 60 μm (we refer to these as in-house slides). A subset of 2,402 slides were annotated with carcinoma, adenocarcinoma, and benign tissue labels. We used an in-depth stratification by Gleason grade and tumor size is included in Supplementary Table 1. In addition, we also included a set of 12,277 prostate core needle biopsy submitted to MSK for a second opinion from other institutions around the world. These slides were produced at their respective institutions and scanned at 40 μm. The prostate dataset was used for the first task, the external slides were not used during training, but only test to estimate generalization to scanned slides from other institutions.

A portion of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a Phillips Intelligence Ultra scanner to test generalization to 960-pixel images by scanning variations of the slide thickness. The dataset consisted of 960-pixel images, including variations of the whole of the prostate (1,274 out of 1,784) test set was scanned on a

---

<!-- Page 11 -->

NATURE MEDICINE

ARTICLES

averaging (161–170) ten-bin local histogram of edges with a linear window of edges 7 \times 8 \times 7 aggregated with max-pooling, and (171–180) ten-bin local histogram of edges with a linear window of size 7 \times 8 \times 7 aggregated by averaging. The random forest was learned of the validation set instead of the training set to avoid over-fitting.

RNN-based slide integration. Model/mapping a tile to class probability consists of two parts: a feature extractor f_i that transforms the pixel space to representation space, and a linear classifier f_c that projects the representation vector into the class probability space. The output of f_i for a given image of size S is a 312-dimensional vector representation. Given a slide and model f, we can obtain the output of the S modules of f_i in terms of probabilities p_i by averaging. The ordered sequence of vector representations s = c_1, \dots, c_S is the input to an RNN with a state vector r. The state vector is initialized with a zero vector. Then, for each i = 1, \dots, S of the recurrent forward pass, the new state vector h_i is given by equation (2):

h_i = \text{ReLU}(W_{f_i}^T W_{f_i} h_{i-1} + b) \quad (2)

where W_{f_i} and W_{f_c} are the weights of the RNN model. At step S, the slide classifier f_c is simply applied to the state vector h_S to produce the probabilities. With S in the model does not recur and the RNN should learn the slide classifier. This approach can be easily extended to integrate information at multiple scales. Given the h_{i-1} and h_i of the RNN, we can calculate the difference between the S most interesting tiles from a slide by averaging the prediction of the three modules extracted from the RNN at each step and applying a different magnification. Now, the inputs to the RNN at each step i are c_{i-1}, h_{i-1} and the state vector h_{i-1}. The new state vector is then given by equation (3):

h_i = \text{ReLU}(W_{f_i}^T c_{i-1} + W_{f_i}^T h_{i-1} + b) \\ + W_{f_c}^T h_{i-1} \quad (3)

In all of the experiments, we used 128 dimensional vectors for the state representation of the recurrent unit, ten recurrent steps (5–10), and weighted the positive class to give more importance to the sensitivity of the model. All RNN models were trained with a learning rate of 0.0001.

MIL exploratory experiments. We performed a set of exploratory experiments on the prostate dataset. At least five training runs were completed for each condition. The minimum balanced error on the validation set for each run was used to decide the best condition in each experiment. ReNet84 achieved the best results over other architectures tested. The relative balanced error rates with respect to ReNet84 were +0.0738 (t-SNE), +0.0738 (t-SNE), +0.0738 (t-SNE), +0.0265 for ReNet101 and +0.0085 for DenseNet201. Using a class weighted loss led to better performance overall, and we adopted weights in the range of 0.80–0.95 in subsequent experiments. Given the scale of our data, augmenting the data with rotations and flips did not significantly affect the results: the best balanced error rate of the model trained with augmentation was 0.095 higher than without augmentation. During training, we weighted the false negative errors more heavily to obtain models with high sensitivity.

Visualization of feature space. For each dataset, we sampled 100 tiles from each test slide, in addition to its top-ranked tile. Given the trained 20c models, we extracted for each of the sampled tiles the final feature embedding before the classification layer. We used a distributed stochastic neighbor embedding (t-SNE)39 for dimensionality reduction to two dimensions.

Pathology analysis of model errors. A gonitourinary subspecialized pathologist (V.E.R.) reviewed the prostate cases. A dermatopathology subspecialized pathologist (M.G.H.B.) reviewed the BCC cases. Two subspecialized pathologists (E.B. and M.G.H.) jointly reviewed the breast cases. For each tissue type, the respective pathologists were presented with all of the test errors and a randomly selected sample of 20 tiles from the test dataset. We used the pathologists' model predictions and interpreting possible systematic error modalities. During the pathologists' pathology review, access to the models' prediction and the full pathology report for each case.

CAMELYON6 experiments. The CAMELYON6 dataset contains 400 total patients for whom a single WSIs in provided in a tag image file format (TIFF). Amos et al.40 reviewed the CAMELYON6 dataset and found that the errors in each positive slide. For each annotation, several regions, defined by vertex coordinates, may be present. Since these slides were scanned at a higher resolution than the

slides scanned at MSK, a tiling method was developed to extract tiles containing tissue from both inside and outside the annotated regions at MSK 20x equivalent magnification (0.5 mm2 pixel2) to enable direct comparison with our datasets. This method generates a grid of possible tiles, excludes background via Otsu thresholding and determines whether a tile is inside an annotation region by solving a point in polygon problem.

We used 80% of the training data to train our model, and we left 20% for model selection. We extracted at random 1,000 tiles from each negative slide, and 1,000 positive tiles from each of the positive slides. A ReNet54 model was trained augmenting the dataset on the fly by 90° rotations, horizontal flips, and vertical flips (0.5 mm2 pixel2) (Fig. S1). The best performing model on the validation set was selected. Slide-level predictions were generated with the random forest aggregation approach explained before and trained on the entire dataset. We trained the RNN on the validation set to train the random forest model, we exhaustively tiled with no overlap the training slides to generate the validation probability maps. The trained random forest was then evaluated on the CAMELYON6 test dataset and on our large breast lymph node metastasis data datasets.

Data protection. This project was governed by an Institutional Review Board. The data were de-identified and were not used for consent/authorship purposes and was waived before research was carried out. All data collection, research and analysis was approved by the Institutional Review Board.

All publicly shared WSIs were de-identified and do not contain any protected health information or label text.

Reporting Summary. Further information on research design is available in the Nature Reporting Summary linked to this article.

## Data availability

The publicly shared breast cancer metastases dataset is available at http://thomaslabshub.org/data/. The dataset consists of 130 de-identified WSIs of axillary lymph node specimens from 78 patients (see Extended Data Fig. 7). The dataset is available on the CML and co-in and scanned on Leica Biodymatics AT2 digital slide scanners at MSK. Metastatic carcinoma is present in 36 whole slides from the dataset. The validation and test data are included in the dataset. The remaining data that support the findings of this study were offered to editors and peer reviewers at the time of submission for the purposes of evaluating the manuscript upon request. The remaining data are not publicly available, in accordance with institutional requirements governing human subject privacy protection.

## Code availability

The source code for this work can be downloaded from https://github.com/MSKCC-Computational-Pathology/MIL-nature-medicine-2019.

## References

1. Goode, A., Gilbert, B., Hurles, J., Ickis, D. & Satyanarayanan, M. OpenSlide: a vendor-neutral software foundation for digital pathology.J. Pathol. Inform.4, 27 (2013).
2. Paszke, A. et al. Automatic differentiation in PyTorch. In31st Conference on Neural Information Processing Systems(2017).
3. R Development Core Team.R: A Language and Environment for Statistical Computing(R Foundation for Statistical Computing, 2017).
4. Robins, J. et al. PHOENIX: an open-source package for R and S+ to analyze and compare ROC curves.BMC Bioinformatics12, 77 (2011).
5. Wickens, H., gopel: Elegant Graphics for Data Analysis (Springer, 2016).
6. Carpenter, J. & Bihell, J. Bootstrap confidence intervals: when, what? A practical guide for medical statisticians.Stat. Med.19, 1141–1164 (2000).
7. Delgado-Rodriguez, M. & Clarke, S. J. A comparison of the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach.Biometrika87, 155–163 (1988).
8. Yu, Y. et al. Sentinel lymph node biopsy after neoadjuvant chemotherapy for breast cancer: retrospective comparative evaluation of clinically axillary lymph node positive and negative patients, including those with axillary lymph node metastases confirmed by fine needle aspiration.BMC Cancer16, 200 (2016).
9. Van der Maaten, L. & Hinton, G. Visualizing data using t-SNE.J. Mach. Learn. Res.9, 2597–2605 (2008).

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

11

---

<!-- Page 12 -->

ARTICLES

NATURE MEDICINE

a) Map of the United States showing the geographical distribution of consultation slides. Red dots indicate the locations of pathology laboratories. The bar chart below shows the number of slides per state, with Washington DC and Puerto Rico having the highest counts.

| US State | Number of Slides |
| --- | --- |
| Washington DC | ~17,000 |
| Puerto Rico | ~248 |
| California | ~10,000 |
| New York | ~8,000 |
| Illinois | ~5,000 |
| Florida | ~4,000 |
| Massachusetts | ~3,000 |
| Michigan | ~2,000 |
| Ohio | ~1,500 |
| Georgia | ~1,000 |
| Alabama | ~800 |
| Arkansas | ~600 |
| Mississippi | ~500 |
| North Carolina | ~400 |
| South Carolina | ~300 |
| Tennessee | ~250 |
| Kentucky | ~200 |
| Virginia | ~150 |
| West Virginia | ~100 |
| Indiana | ~100 |
| Alabama | ~100 |
| Missouri | ~100 |
| Wisconsin | ~100 |
| Minnesota | ~100 |
| Iowa | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |
| Nebraska | ~100 |
| Idaho | ~100 |
| Montana | ~100 |
| North Dakota | ~100 |
| South Dakota | ~100 |

---

<!-- Page 13 -->

NATURE MEDICINE

ARTICLES

Prostate

BCC

Axillary LNs

Scale

- Ensemble (AUC: 0.989)
- 20x (AUC: 0.986)
- 10x (AUC: 0.983)
- 5x (AUC: 0.974)

Scale

- 20x (AUC: 0.986)
- 5x (AUC: 0.990)

Scale

- 20x (AUC: 0.965)

Extended Data Fig. 2 | ML model classification performance for different cancer datasets. Performance on the respective test datasets was measured in terms of AUC. a, Best results were achieved on the prostate dataset (n=1,784), with an AUC of 0.989 at 20x magnification. b, For BCC (n=1,575), the model trained at 5x performed the best, with an AUC of 0.990. The worst performance came on the breast metastasis detection task (n=1,473), with an AUC of 0.965 at 20x. The axillary lymph node dataset is the smallest of the three datasets, which is in agreement with the hypothesis that larger datasets are necessary to achieve lower error rates on real-world clinical data.

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 14 -->

ARTICLES

NATURE MEDICINE

Extended Data Fig. 3 | t-SNE visualization of the representation space for the BCC and axillary lymph node models. Two-dimensional t-SNE projection of the 512-dimensional representation space were generated for 100 randomly sampled tiles per slide. a, BCC representation (n=144,935). b, Axillary lymph nodes representation (n=139,178).

Extended Data Fig. 3 | t-SNE visualization of the representation space for the BCC and axillary lymph node models. Two-dimensional t-SNE projection of the 512-dimensional representation space were generated for 100 randomly sampled tiles per slide. a, BCC representation (n=144,935). b, Axillary lymph nodes representation (n=139,178).

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 15 -->

NATURE MEDICINE
ARTICLES

The figure is a plot of Sensitivity versus Specificity, showing four ROC curves for different scales of the prostate dataset. The x-axis (Specificity) ranges from 1.00 to 0.00, and the y-axis (Sensitivity) ranges from 0.00 to 1.00. A diagonal line from (1.00, 0.00) to (0.00, 1.00) represents a random classifier. The curves for the different scales are as follows:

| Scale | AUC |
| --- | --- |
| Ensemble | 0.9867 |
| 20x | 0.9821 |
| 5x | 0.9738 |
| 10x | 0.9711 |

Extended Data Fig. 4 | Performance of the MIL-RF model at multiple scales on the prostate dataset. The MIL model was run on each slide of the test dataset (n = 1,764) with a stride of 40 pixels. From the resulting tumor probability heat map, hand-engineered features were extracted for classification with the random forest (RF) model. The best MIL-RF model (ensemble model; AUC = 0.987) was not statistically significantly better than the MIL-only model (20x model; AUC = 0.986; see Fig. 3), as determined using DeLong's test for two correlated ROC curves.

NATURE MEDICINE | www.nature.com/naturemedicine
Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 16 -->

ARTICLES

NATURE MEDICINE

Extended Data Fig. 5 consists of three ROC curve plots labeled (a), (b), and (c). Each plot has Sensitivity on the y-axis and Specificity on the x-axis, both ranging from 0.00 to 1.00. A diagonal line from (0,0) to (1,1) represents random performance.

- Plot (a): Prostate Model Trained in MSK data.Shows three curves: MSK In-house Aperio (AUC: 0.991) in red, MSK In-house Philips (AUC: 0.966) in green, and MSK External Aperio (AUC: 0.932) in blue.
- Plot (b): Breast Model Trained on MSK data.Shows two curves: MSK test set (AUC: 0.965) in red and CAMELYON16 test set (AUC: 0.895) in blue.
- Plot (c): Breast Model Trained on CAMELYON16.Shows two curves: CAMELYON16 test set (AUC: 0.930) in red and MSK test set (AUC: 0.727) in blue.

Extended Data Fig. 5 | ROC curves of the generalization experiments summarized in Fig. 5. a, Prostate model trained with MIL on MSK in-house slides tested on: (1) an in-house slides test set (n=1,784) digitized on Aperio scanners; (2) an in-house slides test set digitized on a Philips scanner (n=1,274); and (3) external slides submitted to MSK for consultation (n=12,727). b, c, Comparison of the proposed MIL approach with state-of-the-art fully supervised learning for breast metastasis detection in lymph nodes. For b, the breast model was trained on MSK data with our proposed method (MIL-RNN) and tested on the MSK breast data test set (n=1,473) and on the test set of the CAMELYON16 challenge (n=129), and achieved AUCs of 0.965 and 0.895, respectively. For c, the fully supervised model was trained on CAMELYON16 data and tested on the CAMELYON16 test set (n=129), achieving an AUC of 0.930. Its performance dropped to AUC = 0.727 when tested on the MSK test set (n=1,473).

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 17 -->

NATURE MEDICINE

ARTICLES

Extended Data Fig. 6 consists of two panels, (a) and (b), each containing two vertically stacked plots. The top plot in each panel shows Sensitivity (y-axis, 0.00 to 1.00) against the percentage of slides reviewed (x-axis, 0 to 100). The bottom plot shows Probability (y-axis, 0.00 to 1.00) against the same x-axis. The background of the top plots is divided into a red region labeled 'Predicted Positive' and a blue region labeled 'Predicted Negative'. In panel (a), the red region extends to approximately 25% slides reviewed, while in panel (b), it extends to approximately 21%. The probability curves in the bottom plots show a sharp drop in probability as the percentage of slides reviewed increases, with the drop occurring earlier in panel (b) than in panel (a).

Extended Data Fig. 6 | Decision support with the BCC and breast metastases models. For each dataset, slides are ordered by their probability of being positive for cancer, as predicted by the respective MILL-RNN model. The sensitivity is computed at the case level. a, BCC (n = 1,575); given a positive prediction threshold of 0.025, it is possible to ignore roughly 68% of the slides while maintaining 100% sensitivity. b, Breast metastases (n = 1,473); given a positive prediction threshold of 0.21, it is possible to ignore roughly 65% of the slides while maintaining 100% sensitivity.

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 18 -->

ARTICLES
NATURE MEDICINE

The figure consists of four vertically stacked panels, each showing a histological slide of a tissue section. The tissue is stained purple and has a wavy, elongated shape. A scale bar in the top right of the first panel indicates 2 mm. The panels are labeled as follows:

- WSI: Whole Slide Image, showing the entire tissue section.
- 20x (0.5 mpp): The tissue section is tiled with a grid of small red squares, each representing a 0.5 mpp (microns per pixel) instance.
- 10x (1 mpp): The tissue section is tiled with a grid of larger red squares, each representing a 1 mpp instance.
- 5x (2 mpp): The tissue section is tiled with a grid of even larger red squares, each representing a 2 mpp instance.

Extended Data Fig. 7 | Example of a slide tiled on a grid with no overlap at different magnifications. A slide represents a bag, and the tiles constitute the instances in that bag. In this work, instances at different magnifications are not part of the same bag. mpp, microns per pixel.

NATURE MEDICINE | www.nature.com/naturemedicine
Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 19 -->

NATURE MEDICINE

ARTICLES

The figure consists of two bar charts, one for 'Multiple Instance Learning' and one for 'Fully Supervised Learning'. Both charts show the Area Under the Curve (AUC) for three datasets: MSK, MSK public, and CAMELYON16. The y-axis represents AUC, ranging from 0.5 to 1.0. Error bars represent 95% confidence intervals.

| Learning Method | Dataset | n | AUC |
| --- | --- | --- | --- |
| Multiple Instance Learning | MSK test set | 1473 | ~0.96 |
| Multiple Instance Learning | MSK public test set | 130 | ~0.95 |
| Multiple Instance Learning | CAMELYON16 test set | 129 | ~0.80 |
| Fully Supervised Learning | CAMELYON16 test set | 129 | ~0.93 |
| Fully Supervised Learning | MSK test set | 1473 | ~0.73 |
| Fully Supervised Learning | MSK public test set | 130 | ~0.73 |

Extended Data Fig. 8 | The publicly shared MSK breast cancer metastases dataset is representative of the full MSK breast cancer metastases test set. We created an additional dataset of the size of the test set of the CAMELYON16 challenge (130 slides) by subsampling the full MSK breast cancer metastases test set, ensuring that the models achieved similar performance for both datasets. Left, the model was trained on MSK data with our proposed method (MIL-RNN) and tested on: the full MSK breast data test set (n=1473; AUC = 0.968), the public MSK dataset (n=130; AUC = 0.965); and the test set of the CAMELYON16 challenge (n=129; AUC = 0.898). Right, the model was trained on CAMELYON16 data with supervised learning1 and tested on: the test set of the CAMELYON16 challenge (n=129; AUC = 0.932); the full MSK breast data test set (n=1473; AUC = 0.731); and the public MSK dataset (n=130; AUC = 0.737). Error bars represent 95% confidence intervals for the true AUC calculated by bootstrapping each test set.

NATURE MEDICINE | www.nature.com/naturemedicine

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 20 -->

nature research

Corresponding author(s): Thomas J. Fuchs

Last updated by author(s): May 22, 2019

## Reporting Summary

Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist.

### Statistics

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.

n/A Confirmed

- The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
- A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
- The statistical test(s) used AND whether they are one- or two-sidedOnly common tests should be described; describe more complex techniques in the Methods section.
- A description of all covariates tested
- A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
- A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
- For null hypothesis testing, the test statistic (e.g.F,t,r) with confidence intervals, effect sizes, degrees of freedom andPvalue notedGivePvalues as exact values whenever possible.
- For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
- For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
- Estimates of effect sizes (e.g. Cohen'sd, Pearson'sr), indicating how they were calculated

Our web collection on statistics for biologists contains articles on many of the points above.

### Software and code

Policy information about availability of computer code

| Data collection | Glass slides were digitized with Leica Aperio AT2 scanners and Philips Ultra Fast Scanner at a resolution of 0.5 microns per pixel. |
| --- | --- |
| Data analysis | The algorithms were written in python. We used opendile (version 3.4.1) to access the whole slide images, and pytorch (version 1.0) to train deep learning models. R (version 3.3.3) was used for the statistical analysis of the results. |

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers. We strongly encourage code-deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.

### Data

Policy information about availability of data

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:

- - Accession codes, unique identifiers, or web links for publicly available datasets
- - A list of figures that have associated raw data
- - A description of any restrictions on data availability

The publicly shared MSK breast cancer metastases dataset is available at http://thomasfuchslab.org/data/. The dataset consists of 130 de-identified whole slide images of axillary lymph node specimens from 78 patients (see Supplemental Figure 6). The tissue was stained with H&E and scanned on Leica Biosystems AT2 digital slide scanners at Memorial Sloan Kettering Cancer Center. Metastatic carcinoma is present in 25 whole slides from 27 patients and the corresponding label is included in the dataset.

The remaining data that supports the findings of this study were offered to editors and peer reviewers at the time of submission for the purposes of evaluating the manuscript upon request. The remaining data is not publicly available in accordance to institutional requirements governing human subject privacy protections.

Content courtesy of Springer Nature, terms of use apply. Rights reserved

nature research | reporting summary

nature research

1

---

<!-- Page 21 -->

nature research | reporting summary

## Field-specific reporting

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.

 Life sciences  Behavioural & social sciences  Ecological, evolutionary & environmental sciences

For a reference copy of the document with all sections, see nature.com/documents/in-reporting-summary-flat.pdf

## Life sciences study design

All studies must disclose on these points even when the disclosure is negative.

| Sample size | No sample-size calculations were performed. Within the enrollment years listed in Figure 1a all cases with digitizes whole slides were included in the study without data curation. |
| --- | --- |
| Data exclusions | Less than ten whole slide images were excluded because of excessive pen ink marks present on the image. The exclusion criteria was pre-established. |
| Replication | Models were trained five times with each condition to ensure the stability of the training procedure. Replication was successful for all conditions for which test results were reported. |
| Randomization | Patients were randomly divided in three groups: training, validation, and test sets. No other covariates were controlled for. |
| Blinding | Since our experiments are based on digitized pathology slides, blinding is not necessary. |

## Reporting for specific materials, systems and methods

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.

| Materials & experimental systems | Methods |
| --- | --- |
| n/a | n/a |
| Involved in the study | Involved in the study |
| Antibodies | ChIP-seq |
| Eukaryotic cell lines | Flow cytometry |
| Palaeontology | MRI-based neuroimaging |
| Animals and other organisms |   |
| Human research participants |   |
| Clinical data |   |

## Human research participants

Policy information about studies involving human research participants

| Population characteristics | Digital images of microscope slides from patients that were diagnosed at MSKCC over a period of at least 1 year and up to 5 years depending on the tissue type. |
| --- | --- |
| Recruitment | No patient recruitment was performed. All digital images that were available for the pre-established collecting period were analyzed. |
| Ethics oversight | Memorial Sloan Kettering Cancer Center |

Note that full information on the approval of the study protocol must also be provided in the manuscript.

nature research

6

Content courtesy of Springer Nature, terms of use apply. Rights reserved

---

<!-- Page 22 -->

## Terms and Conditions

Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH ("Springer Nature").

Springer Nature supports a reasonable amount of sharing of research papers by authors, subscribers and authorised users ("Users"), for small-scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use ("Terms"). For these purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.

These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription (to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will apply.

We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as detailed in the Privacy Policy.

While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may not:

1. 1. use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access control;
2. 2. use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is otherwise unlawful;
3. 3. falsely or misleadingly imply or suggest endorsement, approval, sponsorship, or association unless explicitly agreed to by Springer Nature in writing;

1. 4. use bots or other automated methods to access the content or redirect messages

1. 5. override any security feature or exclusionary protocol; or

1. 6. share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal content.

In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue, royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any other, institutional repository.

These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.

To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law, including merchantability or fitness for any particular purpose.

Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed from third parties.

If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not expressly permitted by these Terms, please contact Springer Nature at

online-service@springernature.com