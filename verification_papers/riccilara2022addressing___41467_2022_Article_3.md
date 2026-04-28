<!-- Page 1 -->

Comment

[https://doi.org/10.1038/s41467-022-3186-3](https://doi.org/10.1038/s41467-022-3186-3)

# Addressing fairness in artificial intelligence for medical imaging

Maria Agustina Ricci Lara, Rodrigo Echeveste and Enzo Ferrante

 Check for updates

A plethora of work has shown that AI systems can systematically and unfairly be biased against certain populations in multiple scenarios. The field of medical imaging, where AI systems are beginning to be increasingly adopted, is no exception. Here we discuss the meaning of fairness in this area and comment on the potential sources of biases, as well as the strategies available to mitigate them. Finally, we analyze the current state of the field, identifying strengths and highlighting areas of vacancy, challenges and opportunities that lie ahead.

With the exponential growth in the development of artificial intelligence (AI) systems for the analysis of medical images, hospitals and medical centers have started to deploy such tools in clinical practice1. These systems are typically powered by a particular type of machine learning (ML) technique known as deep learning (DL). DL methods learn complex data representations by employing multiple layers of processing with different levels of abstraction, which are useful to solve a wide spectrum of tasks. In the context of medical image computing (MIC), examples of such tasks include pathology classification, anatomical segmentation, lesion delineation, image reconstruction, synthesis, registration and super-resolution, among many others2. While the number of scientific publications related to DL methods applied to different MIC problems in laboratory conditions has grown exponentially, clinical trials aimed at evaluating medical AI systems have only recently started to gain momentum. In fact, according to the American College of Radiology, to date less than 200 AI medical products related to radiology and other imaging domains have been cleared by the United States Food and Drug Administration3.

Recently, the research community of fairness in ML has highlighted that ML systems can be biased against certain sub-populations, in the sense that they present disparate performance for different sub-groups defined by protected attributes such as age, race/ethnicity, sex or gender, socioeconomic status, among others4.

In the field of healthcare, the potential unequal behavior of algorithms towards different population sub-groups could even be considered to go against the principles of bioethics: justice, autonomy, beneficence and non-maleficence5. In this context, fostering fairness in MIC becomes essential. However, this is far from being a simple task: ensuring equity in ML deployments requires tackling different and multiple aspects along the whole design, development and implementation pathway. While the implications of fairness in ML for the

broad field of healthcare have recently been surveyed and discussed6, in this comment we focus on the sub-field of medical imaging. Indeed, when it comes to biases in ML systems that can benefit certain sub-populations in detriment of others, the field of medical imaging is not the exception7,8. In what follows we will comment on recent work in the field and highlight valuable unexplored areas of research, discussing potential challenges and available strategies.

## What does it mean for an algorithm to be fair?

Let us start by considering this question in the context of patient sub-groups defined by skin tone or race/ethnicity, where a number of recent articles have compared the performance of MIC systems for suspected ophthalmologic, thoracic and/or cardiac pathologies. For example, when it comes to diagnosing diabetic retinopathy, a severe imbalance in the data used to train a model may result in a strong gap in the diagnostic accuracy (73% vs. 60.5%) for light-skinned vs. dark-skinned subjects9. In the same vein, it has been detected that models fed with chest radiography for pathology classification have a higher rate of underdiagnosis for under-served sub-populations, including Black patients8, so that the use of these tools could increase the probability of those patients being sent home without receiving the care they need. Lower performance of AI models designed for cardiac MRI segmentation (in terms of Dice coefficient) in this group has also been found10, which may result in compound biases if any further diagnostic analysis were required to be done on the automatically delineated silhouette.

After reading these examples, we immediately and automatically recognize these situations as unfair. However, establishing a criterion on how to determine whether a given algorithm can be said to be fair is a thorny issue. In the previous paragraph we have purposefully mentioned examples where different metrics were employed in each case. Indeed, the first issue one encounters is that a large number of candidate measures exist. One can for instance evaluate fairness by comparing standard ML performance metrics across different sub-groups, such as accuracy10,11, or AUC ROC (the area under the receiver operating characteristic curve)10,12, among others. Alternatively, one can choose to employ one of the (no less than ten) different fairness-specific criteria formulated by the community13 in order to audit the presence of bias in a given model10,14. To complicate matters further, even if one carries out a multi-dimensional study by simultaneously employing multiple metrics15 (e.g., which model to select at the end in a given setting might be no trivial matter and additional information will in general be required. Along these lines, on those occasions where there is a discrepancy between different sub-groups (Fig. 1, top row), special care must be taken in the selection of the fairness definition to be used16. For example, the demographic parity criterion (Fig. 1, bottom row, right side) which requires equal chances of positive predictions in each group, would hence suggest the

nature communications

(2022)13:4581 |

1

---

<!-- Page 2 -->

# Comment

The diagram illustrates group-fairness metrics using a toy-example of disease classification. It shows a population divided into two subgroups: blue and red. The top part shows the 'population ground truth' with symbols for 'satisfied ground truth' (blue circle with a plus), 'dissatisfied ground truth' (blue circle with a minus), 'FN' (false negative), and 'TP' (true positive). The middle part shows 'model predictions' for the same subgroups. Below this, it defines 'demographic parity' as the condition where the proportion of satisfied ground truth is equal across subgroups, represented by the equation \frac{\# \text{ satisfied ground truth}}{\# \text{ population}} = \frac{\# \text{ satisfied ground truth}}{\# \text{ population}}. It also defines 'equal opportunity' as the condition where the proportion of satisfied ground truth is equal for each subgroup, represented by the equation \frac{\# \text{ satisfied ground truth}}{\# \text{ population}} = \frac{\# \text{ satisfied ground truth}}{\# \text{ population}}. The bottom part shows two scenarios: 'not fulfilled' where the demographic parity is not met, and 'fulfilled' where the equal opportunity is met.

Fig. 1 | Group-fairness metrics. Here we include a toy-example in the context of disease classification, where two subgroups are characterized by different predicted attributes (in red and blue) present different disease prevalence (40% and 20% for blue and red subjects respectively, top row, x marks positive cases). A model optimized for discriminative performance was assessed on a test set achieving 100% accuracy (bottom row, left side, + marks positive predictions). Algorithm fairness was audited according to two common metric choices (bottom row, right side). In this case, as a consequence of the difference in disease frequency, the model would not fulfill the demographic parity criterion (bottom row, right side) since the predicted prediction rates vary between sub-groups: 40% (8 positive predictions over 20 cases) for the blue sub-group vs. 20% (4 positive predictions over 20 cases) for the red sub-group. On the other hand, the model would fulfill the equal opportunity criterion, as true positive rates match for both sub-groups reaching the value of 100% (8 true positives out of 8 positive ground truth cases for the blue sub-group and 4 true positives out of 4 positive ground truth cases for the red sub-group). FN, false negatives, FP, false positives, TN true negatives, TP true positives. See legend box with symbols on the top right corner.

algorithm is unfair for presenting a higher probability of a positive result for the sub-group with a greater target condition prevalence. This criterion assumes that the prediction of an algorithm is independent of the protected attribute that defines each sub-group, so it may be suitable in settings such as loan eligibility prediction or hiring for job vacancies, but not for disease prediction cases where the prevalence depends on the aforementioned attribute. In these cases, it would be more appropriate to resort to definitions such as the equal opportunity criterion (Fig. 1, bottom row, right side), which will compare the equality of true positive rates between sub-groups whose computation is independent of the pre-test probability. Overall, it becomes clear that a one-size-fits-all definition of fairness in MIC will not exist.

## Three reasons behind biased systems: data, models and people

Providing effective solutions to disparities in the outcomes of AI systems is by identifying the sources of bias and taking appropriate actions (Fig. 2). The lack of diversity and proper representation of the target population in the training databases has been identified as one of the

The diagram illustrates the main potential sources of bias in AI systems for MIC. It shows a flow from data (1) to models (2) to outcomes (3). Data (1) is represented by a stack of people and a database icon, with a legend indicating 'biased ground truth' (blue circle with a plus), 'dissatisfied ground truth' (blue circle with a minus), 'FN' (false negative), and 'TP' (true positive). Models (2) are represented by a stack of people and a model icon. Outcomes (3) are represented by a stack of people and an outcomes icon. Arrows indicate the flow from data to models to outcomes, with a feedback loop from outcomes back to data.

Fig. 2 | Main potential sources of bias in AI systems for MIC. The data being fed to the system during training (1), design choices for the model (2), and the people who develop those systems (3), may all contribute to biases in AI systems for MIC.

main reasons behind this phenomenon1 (Fig. 2D). In the context of MIC, ML systems are trained using big databases of images, usually accompanied by annotations or labels indicating the desired output that we expect from the system (e.g., X-ray images with labels associated with the radiological finding of interest like pneumonia or cardiomegaly). When the demographics of such databases do not match that of the target population, the trained model may be biased, presenting lower performance in the underrepresented groups2. Indeed, in chest X-ray pathology classification, only few of the major available datasets in that domain include information about race/ethnicity and, in cases where this information is included, databases tend to be skewed in terms of those attributes3.

One point to keep in mind is that a ML system violating one particular definition of fairness should not necessarily be considered biased. In this sense, the selection of appropriate metrics to assess and ensure fairness according to the specific use case is a delicate task that requires careful human intervention. Moreover, such a choice will also be conditioned by the fact that some of these metrics are mutually exclusive4, implying that, for example, building a classifier to be simultaneously maximally fair in terms of outcomes, opportunities and calibration will not be feasible most of the time. In addition, choices related to model design, such as the architecture, loss function, optimizer or even hyper-parameters, may also play a fundamental role in bias amplification or mitigation5 (Fig. 2D). The same happens with sampling criteria for database construction. For the above reasons, if decisions are made exclusively by developers, engineers, medical specialists, or data scientists in isolation, or by groups of people who share the same ethnic or social background, there is a risk that their own biases may be unintentionally incorporated in the system based on what they choose to prioritize (Fig. 2D).

Taking a step back, complex structural reasons for bias need also be taken into account. We highlight two of these here (see ref. 6 for an in-depth account). Unequal treatment of patients, as well as disparate access to the healthcare system due to economic inequalities conspires against investigating certain pathologies in underrepresented populations. Anatomical differences and even variability in the manifestation of diseases across sub-groups can moreover act as confounders. Likewise, many health problems of particular relevance to low income countries are often understudied due to lack of research funding. Finally, the development of predictive systems for potential biases, people may unintentionally only search within the possibilities and the reality with which they are familiar.

nature communications

(2022)13:4581 |

2

---

<!-- Page 3 -->

# Comment

## Bias mitigation strategies

Several studies in recent years have proposed solutions to mitigate bias and develop fairer algorithms1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015

---

<!-- Page 4 -->

# Comment

the sense that including sensitive attributes useful for bias audit may go against the privacy of the individuals. To overcome these limitations, the implementation of technical solutions to simultaneously address the demands for data protection and utilization becomes extremely important.10 Moreover, it must be noted that the subset of sensitive attributes either directly reported or estimated varies from dataset to dataset. The currently most widely reported characteristics are age and sex or gender,10,11 followed by skin tone or race/ethnicity,12,13 and, to a lesser extent socioeconomic characteristics.13,14 In some cases, where protected attributes are not available, estimates can be computed using image processing methods,15,16 and eventually manual labeling by professionals can be used.10,13 These strategies bring with them however an additional level of complexity and subtlety in their implementation which can limit reproducibility and comparison of results across sub-groups. Secondly, important uncertainties exist in the MIC task to be tackled. The vast majority of studies conducted to date deal with pathology classification tasks10,12,13,24. The study of fairness in the context of segmentation is however rare, and those of regression, prediction, synthesis and super-resolution are rarer still, leaving entire areas to be explored.

Incorporating fairness audits as common practice in MIC studies, as highlighted by a recent article10 which analyzed the common practices when reporting results for diagnostic algorithms in one of the major conferences on MIC, demographics are rarely mentioned, and disaggregated results are infrequently discussed by scientific publications in this domain. This matter is also addressed by the FUTURE AI Guidelines10, which include principles and consensus recommendations for trustworthy AI in medical imaging, and not only focus on fairness, but also cover accuracy, robustness, explainability, traceability, usability, robustness and explainability. In that sense, we believe the FUTURE AI guidelines may constitute a practical tool to improve the publication practices of our community.

Increasing diversity in database construction. As researchers working in Latin America, we want to stress the importance of widening the scope of representation in the datasets used for training our models. It has been acknowledged by several studies that the vast majority of MI databases employed for AI developments originate from high income countries, mostly in Europe and North America10,12. This introduces a clear selection bias since the demographics of these countries do not match that of other areas like Africa, Asia or Latin America. This fact, combined with experimental studies suggesting that race/ethnicity imbalance in MI databases may be one of the reasons for unequal performance10, calls for action towards building truly international databases which include patients from low income countries. This issue becomes even more relevant in the light of recent findings which confirm that AI can reliably predict protected attributes from medical images, even in a setting where clinical experts cannot like race/ethnicity in chest X-ray25 and ancestry in histologic images26. While this fact by itself does not immediately mean that systems will be biased, it can contribute to a feedback loop scheme in a setting with strong data imbalance, it may provide a direct vector for the reproduction of pre-existing racial disparities.

In this regard, initiatives such as the All of Us Research Program, which includes participants from all over the country, and the U.S. Census to create a more diverse health database, hope to promote and improve biomedical research, as well as medical care27. Efforts such as

this one, currently focused on an individual country, could be replicated and lay the groundwork for a collaborative enterprise that transcends geographic barriers.

Rethinking fairness in the context of medical image analysis. For some time now, research on fairness in MI has been carried out in decision-making scenarios such as loan applications, hiring systems, criminal behavior reexamination, among others10. However, the field of medical imaging is a particularly important one in particular, exhibit unique characteristics that require adapting the notion of fairness to this context. Take chest X-ray images for example: particular diagnostic tasks could be easier in one sub-population than the other due to anatomical differences18. How to ensure fairness across sub-populations in this case is far from obvious.

Another example is that of existing bias mitigation strategies which may result in reduced model performance for the majority, or even all sub-populations, in exchange for reducing the variance across them. This might be advisable in other contexts, but in the case of healthcare this implies purposely deteriorating the quality of the predictions for a given sub-population, causing ethical and legal problems related to the provision of alternative standards of care for different sub-groups18. Moreover, how to define such sub-groups is already an open question. Group-based models, usually applied in problems like loan grouping or intended to deal with legal notions of anti-discrimination, reinforce the idea that groups based on pre-specified demographic attributes are well-defined constructs that correspond to a set of homogeneous populations18. However, certain attributes like gender identity28, are fluid constructs difficult to categorize which require rethinking this framework. Similar issues may arise when using race or ethnicity10 as protected attributes to define groups of analysis and evaluate fairness metrics.

While some factors influencing fairness and model performance metrics such as target class imbalance are common to several MI domains, others such as differences in disease prevalence across sub-populations have to be carefully taken into consideration when it comes to MIC. The same holds for the cognitive biases that may be introduced by medical specialists when interpreting and annotating images. For example, if a specialist is trained as a potential tool to help out in reducing such biases, if not properly addressed, it could also become a mean to amplify and perpetuate them.

Overall there is no denying that the nascent field of fairness in MI studies for MIC still presents important vacancies both in terms of medical specialties and in terms of the types problems being tackled, which will require increased efforts from the community. However, the rapid growth of the field, the development of new guidelines, and the gain of attention reported here, are highly positive and encourage the MIC community to increase its effort to contribute towards delivering a more equitable standard of care.

Maria Agustina Ricci Lara  1,2, Rodrigo Echeveste  1,4 & Enzo Ferrante  1,4

1Health Informatics Department, Hospital Italiano de Buenos Aires, Ciudad Autónoma de Buenos Aires, Argentina. 2Universidad Tecnológica Nacional, Ciudad Autónoma de Buenos Aires, Argentina. 3Research Institute for Signals, Systems and Computational Intelligence sinc() (FICH-uni/CONICET), Santa Fe, Argentina. 4These authors contributed equally to this work: Maria Ricci Lara, Enzo Ferrante. ✉e-mail: maria.ricci@hospitalitaliano.org.ar; recheveste@sinc.edu.ar; eferrante@sinc.edu.ar

nature communications

(2023)13:4581

4

---

<!-- Page 5 -->

# Comment

Received: 8 March 2022; Accepted: 21 July 2022;Published online: 06 August 2022

## References

1. Esteva, A., et al. Deep learning-enabled medical computer vision.Proc. Med. J. 4, 149–58 (2017).
2. Litvin, G. A. Survey on deep learning in medical image analysis.Med. Image Anal. 42, 14–28 (2017).
3. Li, X., et al. A need to bridge the gap between us: fda clearance and real-world use of AI algorithms.Acad. Radiol. 26, 567–568 (2018).
4. Bolam, J. A debate: the role of medical specialists, interventional accuracy disparities in commercial gender classification. In:Conference on fairness and transparency, 77–91 (2019).
5. Zou, J., & Shchigel'nik, I. AI can be sexist and racist: It's time to make it fair.Nature 559, 100–101 (2018).
6. Bauchamp, T. C., T. L. Chidley, J. F. Principles of biomedical ethics (Oxford University Press, Oxford, 2018).
7. Chen, Y., et al. Ethical machine learning in healthcare.Ann. Rev. Biomed. Data Sci. 4, 125–144 (2017).
8. Yamaguchi, A., & Nieto, N. Peterson, V., Milone, D. H., Ferrante, E. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis.Proc. Natl. Acad. Sci. 117, 1263–1268 (2020).
9. Sayed-Kalantari, L., Zhang, H., McMeekin, M., Chen, J., & Y. Ghassami, M. Underdiagnosis and overdiagnosis in medical imaging: a systematic literature review. In:International Conference on Med. 276, 2716–2728 (2021).
10. Bal, N., & Kish, N. Political science and machine learning. M. Addressing artificial intelligence bias in neural diagnostics.Transl. Vis. Sci. Technol. 10, 13–15 (2019).
11. Payal, A., & R. Rajput, C. Fairness in cardiac MRI angiography: An investigation of bias due to data imbalance in deep learning based segmentation. In:International Conference on Medical Imaging Computing and Computer-Aided Intervention, 432–435 (Springer, 2021).
12. Yamaguchi, A., & M. Ferrante, E. Gender bias in diagnostic terms in radiology. In:International Conference on Medical Imaging Computing and Computer-Aided Intervention, 320–329 (Springer, 2020).
13. Groh, M., et al. Evaluating deep neural networks trained on clinical images in dermatology with a multi-task framework. In:Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 1820–1828 (2019).
14. Paul, W., Hettler, A., Najib, N., & R. Rautio, P. True training and representation alteration for AI fairness and domain generalization.Neural Comput. 34, 716–753 (2022).
15. Payal, A., & R. Rajput, C. Fairness in cardiac MRI angiography: A comparison of multi-modal coronary embolism detection from ct and x-ray.Preprint at arXivhttps://doi.org/10.48550/arXiv.2111.10650(2021).
16. Al-Ali, S., S. Raumann, R., Michels, B. E., Schouten, G. H., Cheplyakina, V. Risk of training diagnostic algorithms on data with demographic gaps. In:International Conference on Medical Imaging Computing and Computer-Aided Intervention, 181–192 (Springer, 2020).
17. Sayed-Kalantari, L., Liu, G., McMeekin, M., Chen, Y., & Ghassami, M. Chevalier's Fairness: A new deep learning classification framework.IEEE Trans. Med. Imaging, 1–12 (2020).
18. Payal, A., & R. Rajput, C. 22nd World Scientific Conference. Can you take unfair until you make it fair? Impacts of differentially partial synthetic data on downstream classification fairness. In:AI 22nd World Scientific Conference, 181–192 (2021).
19. Shchigel'nik, I. A. 100% of Computing for Machinecy AI (ACM, 2021).
20. Correa, R., et al. Two-step adversarial debiasing with partial learning-medical image case studies. In:AI 22nd World Scientific Conference, 181–192 (2021).
21. Glocker, B., & W. Krauck, S. Algorithmic encoding of protecting characteristics and its implications on disparities across subgroups.Preprint at arXivhttps://doi.org/10.48550/arXiv.2003.07231(2021).
22. Surykumaru, V. M., Papernop, N., Goldbein, A., & Ghassami, M. Chasing your tail: lifelong learning policies for computer-aided diagnosis. In:International Conference on Fairness, Accountability, and Transparency, 723–734 (Association for Computing Machinery, 2019).
23. Mohamed, N., Morstatter, F., Saxena, N., Lerman, K., & Gallay, A. A survey on bias and fairness in machine learning.ACM Comput. Surv. 54, 1–35 (2020).
24. Yamaguchi, A., Wu, Y., & Ferrante, E. Gender bias in medical imaging with adversarial learning.Preprint at arXivhttps://doi.org/10.48550/arXiv.2003.04243(2020).
25. Yamaguchi, A., & Ferrante, E. Gender bias in medical imaging.Med. Phys. Bull.Available online at:http://scirp.org/ebook/1407-26-wear-from-fair-in-health-in-medical-imaging(2022).
26. Yamaguchi, A., & Ferrante, E. Gender bias in medical imaging: A fair determination of risk scores. In:Proceedings of Innovations in Theoretical Computer Science (ITCS), 1991 (2021).
27. Hooker, S. Moving beyond "algorithmic bias is a data problem".Patterns 2, 100241 (2021).

1. Pfistl, S. F. Foreplay: A 50k-N, N-H, N-empirical characterization of fair machine learning for clinical risk prediction.J. Biomed. Inform. Sci. 11, 103021 (2021).
2. Kassas, C. A., Malikovic, M. L., Ruckert, D., & Bremer, R. F. Secure, privacy-preserving and federated machine learning in medical imaging.Nat. Med. 16, 1–2 (2012–2013).
3. Irvin, J. V., et al. CheXpert: A large chest radiograph dataset with uncertainty labels and expert correction. In:Proceedings of the AAAI Conference on Artificial Intelligence, 504–513, 509–557 (Association for the Advancement of Artificial Intelligence Press (AAAI), 2019).
4. Wang, K., et al. Chestx-ray Hospital-scale chest x-ray database and benchmarks on weakly-supervised classification in medical imaging. In:Proceedings of the AAAI Conference on Computer vision and pattern recognition, 2070–2076 (IEEE, 2017).
5. Johnson, J. S., et al. MIMIC-3: A de-identified public available database of chest radiographs with free-text reports.Sci. Data 4, 1–8 (2018).
6. Plains, D. E. D. Diagnostic performance of digital versus film mammography for breast cancer: A systematic review.Br. J. Radiol. 85, 1–11 (2012).
7. Codella, N. D. A skin lesion analysis toward melanoma detection 2018: A challenge hosted by the University of Michigan.arXiv preprint arXiv:1806.10904(2018).
8. 100239 (2018).
9. Roberts, S. A. Patient-centric data towards images and metadata for identifying melanoma using clinical reports.Sci. Data 3, 1–8 (2018).
10. Roberts, S. A. Patient-centric data towards images and related early-disease study (wells)-design implications arXiv preprint no. 1. Control.Trans. 20, 573 (1999).
11. Perera, S. A. A systematic review of the cardiac magnetic resonance protocol for trustworthy artificial intelligence in medical imaging.Preprint at arXivhttps://arxiv.org/abs/2009.06568(2020).
12. Wang, Y., et al. A systematic review of publicly available skin cancer image datasets: a systematic review.Lancet Digit. Health 8, E64–E74 (2021).
13. Khosla, N., et al. Towards a comprehensive and ontology-aware database for ophthalmological imaging: barriers to access, usability, and a generalisability.Lancet Digit. Health 3, e65–e74 (2021).
14. Ibrahim, H. L., Xu, Z., Rarita, N., Morris, A. D., & D. Denimino, A. AI: Health data poverty: an accessible barrier to medical image quality.Lancet Digit. Health 3, E20–E25 (2021).
15. Howard, P. N., et al. The impact of therapeutic medical imaging signatures on deep learning model accuracy and bias.Nat. Commun. 12, 1–13 (2021).
16. The All of Us Research Program Investigators. The "all of us" research program.N. Engl. J. Med. 385, e1–e1 (2021).
17. Ganz, M., Helm, S. H., & F. Hergens, A. Assessing bias in medical AI: Workshop on Interdisciplinary Research in Artificial Intelligence and Machine Learning.Proceedings of the 2021, Tommaso, N., McKee, K. R., & J. Mohamed, S. Fairness for unbalanced characteristics: Implications for medical AI.Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2415–2424 (2021).
18. AAM ACM Conference on AI, Ethics, and Society. AIS 21: 26–265 (Association for Computing Machinery, 2021).https://doi.org/10.1145/3462534.3462544.
19. Flanigan, A., Frey, J., Christensen, S. L., & Style Committee, A. M. An updated guidance on race in research and ethnicity in medical and science journals.JAMA 326, 621–627 (2021).
20. Irie, N., & R. Rautio, C. S. Heuristics and cognitive error in medical imaging.Am. J. Roentgenol. 200, 1–11 (2013).
21. Sun, X., Yang, S., Sun, M., & Wang, K. Benchmark for automatic visual classification of COVID-19.IEEE Trans. Med. Imaging, 1–12 (2020).
22. Cuadrado, R., & J. E. Brancik, J. E. A perspective on the Computer Vision for diabetic retinopathy screening.J. Biomed. Sci. Technol. 3, 509–516 (2019).

## Acknowledgments

We thank the Fundar foundation for supporting M.A.R.L. with a Fundatos Scholarship and the Program for Artificial Intelligence in Health at Hospital Italiano de Buenos Aires for providing the space to discuss and work on these issues. This work was supported by Argentina's National Scientific and Technical Research Council (CONICET), who covered the costs of R.I.E. E.T.F. The work of E.F. was partially supported by the ARPH AI project funded by a grant (Number 109584) from the International Development Research Center (IDRC) and the Swedish International Development Research Centre (SIDOC). We also acknowledge the support of Univeridad Nacional del Litoral (Grants CAIC-PIP-50220140100084L, 50620190100145UL), Agencia Nacional de Promoción de la Investigación, de Desarrollo Tecnológico y la Innovación (Grants RICIT 2018-3907, PRH 2017-0003) and Santa Fe Agency for Science, Technology and Innovation (Award ID: IC-138-19).

nature communications

(2022)13:4581

5

---

<!-- Page 6 -->

# Comment

## Author contributions

E.F. provided the initial concept for this article, which was further developed by all authors. M.A.R.L. conducted the literature search and performed the systematic analysis across areas of application, methods as well as strengths and vacancies. M.A.R.L. and R.E. produced the figures. R.E. and E.F. supervised the analysis. All authors wrote the paper.

## Competing interests

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to María Agustina Ricci Lara, Rodrigo Echeveste or Enzo Ferrante.

Peer review information Nature Communications thanks Jakob Kather, Judy Wewira Gichoya and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permission information is available at

http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2022

nature communications

(2022)13:4581

6