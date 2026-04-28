<!-- Page 1 -->

Published as a conference paper at ICLR 2023

# MEDFAIR: BENCHMARKING FAIRNESS FOR MEDICAL IMAGING

Yongshuo Zong1, Yongxin Yang1, Timothy Hospedales1,2

1 School of Informatics, University of Edinburgh, 2 Samsung AI Centre, Cambridge{yongshuo.zong, yongxin.yang, t.hospedales}@ed.ac.uk

## ABSTRACT

A multitude of work has shown that machine learning-based medical diagnosis systems can be biased against certain subgroups of people. This has motivated a growing number of bias mitigation algorithms that aim to address fairness issues in machine learning. However, it is difficult to compare their effectiveness in medical imaging for two reasons. First, there is little consensus on the criteria to assess fairness. Second, existing bias mitigation algorithms are developed under different settings, e.g., datasets, model selection strategies, backbones, and fairness metrics, making a direct comparison and evaluation based on existing results impossible. In this work, we introduce MEDFAIR, a framework to benchmark the fairness of machine learning models for medical imaging. MEDFAIR covers eleven algorithms from various categories, ten datasets from different imaging modalities, and three model selection criteria. Through extensive experiments, we find that the under-studied issue of model selection criterion can have a significant impact on fairness outcomes; while in contrast, state-of-the-art bias mitigation algorithms do not significantly improve fairness outcomes over empirical risk minimization (ERM) in both in-distribution and out-of-distribution settings. We evaluate fairness from various perspectives and make recommendations for different medical application scenarios that require different ethical principles. Our framework provides a reproducible and easy-to-use entry point for the development and evaluation of future bias mitigation algorithms in deep learning. Code is available at https://github.com/ys-zong/MEDFAIR.

## 1 INTRODUCTION

Machine learning-enabled automatic diagnosis with medical imaging is becoming a vital part of the current healthcare system (Lee et al., 2017). However, machine learning (ML) models have been found to demonstrate a systematic bias toward certain groups of people defined by race, gender, age, and even the health insurance type with worse performance (Obermeyer et al., 2019; Larrazabal et al., 2020; Spencer et al., 2013; Seyed-Kalantari et al., 2021). The bias also exists in models trained from different types of medical data, such as chest X-rays (Seyed-Kalantari et al., 2020), CT scans (Zhou et al., 2021), skin dermatology images (Kinyanjui et al., 2020), etc. A biased decision-making system is socially and ethically detrimental, especially in life-changing scenarios such as healthcare. This bias exists in a growing body of work to understand bias and pursue fairness in the areas of machine learning and computer vision (Mehrabi et al., 2021; Louppe et al., 2017; Tartaglione et al., 2021; Wang et al., 2020).

Informally, given an observation input x (e.g., a skin dermatology image), a sensitive attribute s (e.g., male or female), and a target y (e.g., benign or malignant), the goal of a diagnosis model is to learn a meaningful mapping from x to y. However, ML models may amplify the biases and confounding factors that already exist in the training data related to sensitive attribute s. For example, data imbalance (e.g., over 90% individuals from UK Biobank (Sudlow et al., 2015) originate from European ancestors), attribute-class imbalance (e.g., in age-related macular degeneration (AMD) datasets, subgroups of older people contain more pathology examples than that of younger people (Farsiu et al., 2014)), label noise (e.g., Zhang et al. (2022) find that label noises in CheXpert dataset (Irvin et al., 2019) is much higher in some subgroups than the others), etc. Bias mitigation algorithms

arXiv:2210.01725v2 [cs.LG] 17 Feb 2023

1

---

<!-- Page 2 -->

Published as a conference paper at ICLR 2023

graph TD
    Algorithm[Algorithm] --> Dataset[Dataset]
    Dataset --> ModelSelection[Model Selection]
    ModelSelection --> Evaluation[Evaluation]
    Evaluation --> Algorithm
    MEDFAIR{MEDFAIR}
  

Algorithm

- Subgroup Rebalancing
- Domain-Independent
- Adversarial Training
- Disentanglement
- Domain Generalization

Dataset

- Diverse Imaging Modalities
- Sensitive Attributes
- Different Sources of Bias
- Diverse Sizes
- Paired data for OOD

Model Selection

- Performance-based
- Distance to Optimal (DTO)
- Minimax Pareto Optimal

Evaluation

- In-distribution
- Out-of-distribution
- Statistical Tests

Figure 1: Components of MEDFAIR benchmark.

therefore aim to help diagnosis algorithms learn predictive models that are robust to confounding factors related to sensitive attribute s (Mehrabi et al., 2021).

Given the importance of ensuring fairness in medical applications and the special characteristics of medical data, we argue that a systematic and rigorous benchmark is needed to evaluate the bias mitigation algorithms for medical imaging. However, a straightforward comparison of algorithmic fairness for medical imaging is difficult, as there is no consensus on a single metric for fairness of medical imaging models. Group fairness (Dwork et al., 2012; Verma & Rubin, 2018) is a popular and intuitive definition adopted by many debiasing algorithms, which optimises for equal performance among subgroups. However, this can lead to a trade-off of increasing fairness by decreasing the performance of the advantaged group, reducing overall utility substantially. Doing so may violate the ethical principles of beneficence and non-maleficence (Beauchamp, 2003), especially for some medical applications where all subgroups need to be protected. There are also other fairness definitions, including individual fairness (Dwork et al., 2012), minimax fairness (Diana et al., 2021), counterfactual fairness (Kusner et al., 2017), etc. It is thus important to consider which definition should be used for evaluations.

In addition to the use of differing evaluation metrics, different experimental designs used by existing studies prevent direct comparisons between algorithms based on the existing literature. Most obviously, each study tends to use different datasets to evaluate their debiasing algorithms, preventing direct comparisons of results. Furthermore, many bias mitigation studies focus on evaluating tabular data with low-capacity models (Madras et al., 2018; Zhao et al., 2019; Diana et al., 2021), and recent analysis has shown that their conclusions do not generalise to high-capacity deep networks used for the analysis of image data (Zietlow et al., 2022). A crucial but less obvious issue is the choice of model selection strategy for hyperparameter search and early stopping. Individual bias mitigation studies are divergent or vague in their model selection criteria, leading to inconsistent comparisons even if the same datasets are used. Finally, given the effort required to collect and annotate medical imaging data, models are usually deployed in a different domain than the domain used for data collection. (E.g., data collected at hospital A is used to train a model deployed at hospital B). While the maintenance of prediction quality across datasets has been well studied, it is unclear if fairness achieved within one dataset (in-distribution) holds under dataset shift (out-of-distribution).

In order to address these challenges, we provide the first comprehensive fairness benchmark for medical imaging – MEDFAIR. We conduct extensive experiments across eleven algorithms, ten datasets, four sensitive attributes, and three model selection strategies to assess bias mitigation algorithms in both in-distribution and out-of-distribution settings. We report multiple evaluation metrics and conduct rigorous statistical tests to find whether any of the algorithms is significantly better. Having trained over 7,000 models using 6,800 GPU-hours, we have the following observations:

- • Bias widely exists in ERM models trained in different modalities, which is reflected in the predictive performance gap between different subgroups for multiple metrics.

2

---

<!-- Page 3 -->

Published as a conference paper at ICLR 2023

- • Model selection strategies can play an important role in improving the worst-case performance. Algorithms should be compared under the same model selection criteria.
- • The state-of-the-art methods do not outperform the ERM with statistical significance in both in-distribution and out-of-distribution settings.

These results show the importance of a large benchmark suite such as MEDFAIR to evaluate progress in the field and to guide practical decisions about the selection of bias mitigation algorithms for deployment. MEDFAIR is released as a reproducible and easy-to-use codebase that all experiments in this study can be run with a single command. Detailed documentation is provided in order to allow researchers to create and evaluate the fairness of their own algorithms and datasets, and we will also actively maintain the codebase to incorporate more algorithms, datasets, model selection strategies, etc. We hope our codebase can accelerate the development of bias mitigation algorithms and guide the deployment of ML models in clinical scenarios.

## 2 FAIRNESS IN MEDICINE

### 2.1 PROBLEM FORMULATION

We focus on evaluating the fairness of binary classification of medical images. Given an image, we predict its diagnosis label in a way that is not confounded by any sensitive attributes (age, sex, race, etc.) so that the trained model is fair and not biased towards a certain subgroup of people.

Formally, let D \in [D]^I be a set of domains, where I is the total number of domains. A domain can represent a dataset collected from a particular imaging modality, hospital, population, etc. Consider an image D = (\mathcal{X}, \mathcal{Y}, \mathcal{S}) to be a distribution where we have input sample \mathcal{X} \in \mathbb{R}^d over input space \mathcal{X}, the corresponding binary label \mathcal{Y} \in \{0, 1\} over label space \mathcal{Y}, and sensitive attributes \mathcal{S} \in \{0, 1, \dots, n-1\} with n classes over sensitive space \mathcal{S}. We train a model h \in \mathcal{H} to output the prediction \hat{y} \in \{0, 1\}, i.e., h: \mathcal{X} \rightarrow \mathcal{Y}, where \mathcal{H} is the hypothesis class of models. Note that for each dataset D_i, there may exist several sensitive attributes at the same time, e.g., there are metadata of both patients' age and sex. We only consider one sensitive attribute at one time.

In-distribution Given a domain D_i, assume the input samples X_i, their labels Y_i, and the sensitive attributes S_i are identically and independently distributed (iid) from a joint probability distribution P_i(X_i, Y_i, S_i). We define the evaluation where the training and testing on the same domain D_i to be in-distribution, i.e., the training and testing set are from the same distribution. We train models for each combination of algorithms \times datasets \times sensitive attributes.

Out-of-distribution In clinical scenarios, due to the lack of training data, it is common to deploy a model trained in the original dataset to new hospitals/populations that have different data distributions. We define the training on domain D_i and testing on the other unseen domain D_j to be out-of-distribution settings, where D_i and D_j may have different distribution P_i(X_i, Y_i, S_i) and P_j(X_j, Y_j, S_j). In this case, we assume domains D_i and D_j must have the same input space (e.g., X-ray imaging), diagnosis labels, and sensitive attributes, but differ in their joint distributions due to collection from different locations or different imaging protocols. We evaluate if bias mitigation algorithms are robust to distribution shift by directly using the model selected from the in-distribution setting of the domain D_i to test on the domain D_j.

### 2.2 FAIRNESS DEFINITION IN MEDICINE

Here we consider two most salient fairness definitions for healthcare, i.e., group fairness and Max-Min fairness. We argue that one should focus on different fairness definitions depending on the specific clinical application.

Group Fairness Metrics based on group fairness usually aim to achieve parity of predictive performance across protected subgroups. For resource allocation problems that can be considered a zero-sum game due to the limited resources, e.g., prioritising which patients should be sent to a limited number of intensive care units (ICUs), it is important to consider group fairness to reduce the disparity among different subgroups (related discussions in Hellman (2008); Barocas & Selbst

1Our framework can be easily extended to non-binary classification.

3

---

<!-- Page 4 -->

Published as a conference paper at ICLR 2023

(2016)). We measure the performance gap in diagnosis AUC between the advantaged and disadvantaged subgroups as an indicator of group fairness. This is in line with the “separability” criteria (Chen et al., 2021; Dwork et al., 2012) that algorithm scores should be conditionally independent of the sensitive attribute given the diagnostic label (i.e., Y \perp S|Y), which is also adopted by (Gardner et al., 2019; Fong et al., 2021). On the other hand, Zielow et al. (2022) find that for high-capacity models in computer vision, this is typically achieved by worsening the performance of the advantaged group rather than improving the disadvantaged group, a phenomenon termed as leveling down in philosophy that has incurred numerous criticisms (Christiano & Brynen, 2008; Brown, 2003; Doran, 2001). Worse, practical implementations often lead to worsening the performance of both subgroups (Zielow et al., 2022), making it purely inefficient and comprehensively violating beneficence and non-maleficence principles (Beauchamp, 2003). Thus, we argue that group fairness alone is not sufficient to analyse the trade-off between fairness and utility.

Max-Min Fairness It is another definition of fairness (Lahoti et al., 2020) following Rawlsian max-min fairness principle (Rawls, 2001), which is also studied as minimax group fairness (Diana et al., 2021) or minimax Pareto fairness (Martinez et al., 2020). Here, instead of seeking to equalize the error rates among subgroups, it treats the model that reduces the worst-case error rates as the fairer one. It may be a more appropriate definition than group fairness for some medical applications such as diagnosis, as it better satisfies the beneficence and non-maleficence principles (Beauchamp, 2003; Chen et al., 2018; Ustun et al., 2019), i.e., do the best and do no harm. Formally, for a model h in the hypothesis class \mathcal{H}, denote U_s(h) to be a utility function for subgroup s. A model h^* is considered to be Max-Min Fair if it maximizes (Max-) the utility of the worst-case (Min) group:

h^* = \underset{h \in \mathcal{H}}{\operatorname{argmax}} \min_{s \in \mathcal{S}} U_s(h). \quad (1)

In practice, it is hard to quantify the maximum optimal utility, and therefore we treat a model h_k to be fairer than the other model h_l if

\min_{s \in \mathcal{S}} U_s(h_k) > \min_{s \in \mathcal{S}} U_s(h_l). \quad (2)

We measure both group fairness and Max-Min fairness to give a more comprehensive evaluation for fairness in medical applications.

### 3 MEDFAIR

We implement a reproducible and easy-to-use codebase MEDFAIR to benchmark fairness in machine learning algorithms for medical imaging. In our benchmark, we conduct large-scale experiments in ten datasets, eleven algorithms, up to three sensitive attributes for each dataset, and three model selection criteria, where all the experiments can be run with a single command. We provide source code and detailed documentation, allowing other researchers to reproduce the results and incorporate other datasets and algorithms easily.

#### 3.1 DATASETS

Ten datasets are included in MEDFAIR: CheXpert (Irvin et al., 2019), MIMIC-CXR (Johnson et al., 2019), PAPILA (Kovalyk et al., 2022), HAM10000 (Tschandl et al., 2018), Fitzpatrick17k (Groh et al., 2021), OI31 (Chaves et al., 2021), COVID-CT-MD (Afshar et al., 2021), OCT (Farsitu et al., 2014), ADNI 1.5T, and ADNI 3T (Petersen et al., 2010), to evaluate the algorithms comprehensively, which are all publicly available to ensure the reproducibility. We consider five important aspects during dataset selection:

Imaging modalities. We select datasets covering various 2D and 3D imaging modalities, including X-ray, fundus photography, computed tomography (CT), magnetic resonance imaging (MRI), spectral domain optical coherence tomography (SD-OCT), and skin dermatology images.

Potential sources of bias. We involve datasets that may introduce bias from different sources, including label noise, data/class imbalance, spurious correlation, etc. Note that each dataset may contain more than one source of bias.

Sensitive attributes. The selected datasets contain attributes that are commonly treated sensitively and may be biased in clinical practice, including age, sex, race, and skin type.

4

---

<!-- Page 5 -->

Published as a conference paper at ICLR 2023

Table 1: Detailed statistics of the datasets. “# images/scans” listed here are the actual numbers used in this study after removing those missing sensitive attributes. For potential bias, LN, CI, DI, and SC represent label noise, class imbalance, data imbalance, and spurious correlation, respectively.

| Dataset | Modality | # Images | Sensitive Attribute | Bias Sources |
| --- | --- | --- | --- | --- |
| CheXpert | Chest X-ray (2D) | 222,793 | Age, Sex, Race | LN, CI, DI |
| MIxMIC-CXR | Chest X-ray (2D) | 370,955 | Age, Sex, Race | LN, CI, DI |
| PAPILA | Fundus Image (2D) | 420 | Age, Sex | DI, CI |
| HAM10000 | Skin Dermatology (2D) | 9,948 | Age, Sex | DI, CI |
| Fitzpatrick17k | Skin Dermatology (2D) | 16,012 | Skin type | LN, DI, CI |
| OLZI | Heart CT (2D) | 8139 | Age, Sex | DI, CI, SC |
| Covid-CT-MD | Lung CT (3D) | 308 | Age, Sex | DI, CI |
| OCT | SD-OCT (3D) | 384 | Age | DI, CI |
| ADNI 1.5T | Brain MRI (3D) | 550 | Age, Sex | SC |
| ADNI 3T | Brain MRI (3D) | 110 | Age, Sex | SC |

Size of datasets. As the sizes of medical imaging datasets are often limited by privacy issues, etc., it is important to inspect whether the fairness algorithms are effective with different sizes of datasets. The dataset sizes change from 420 ~ 370,955 for 2D images and 110 ~ 550 for 3D scans.

Out-of-distribution evaluation. We include two pairs of datasets with the same modality but collected from different locations or different imaging protocols for out-of-distribution evaluations. Specifically, we choose two 2D chest X-ray datasets i.e., CheXpert and MIxMIC-CXR, and two 3D brain MRI datasets i.e., ADNI 1.5T and ADNI 3T.

Table 1 lists the basic datasets information, and more detailed statistics are provided in Appendix B.

### 3.2 ALGORITHMS

MEDFAIR incorporates 11 algorithms across 5 categories (related work in Appendix A): subgroup rebalancing, domain-independence, adversarial training, disentanglement, and domain generalization. We carefully re-implement the following algorithms based on the original official codes:

- •Baseline– Empirical Risk Minimization (ERM) (Vapnik, 1999) minimizes the average error across the dataset without considering the sensitive attributes.
- – Empirical Risk Minimization (ERM) (Vapnik, 1999) minimizes the average error across the dataset without considering the sensitive attributes.
- •Subgroup Rebalancing–Resamplingmethod upsampled the minority groups so that all of the subgroups appear during training with equal chances.
- –Resamplingmethod upsampled the minority groups so that all of the subgroups appear during training with equal chances.
- •Domain-independence– Domain independent N-way classifier (DomainInd) (Wang et al., 2020) trains separate classifiers for different subgroups with a shared encoder.
- – Domain independent N-way classifier (DomainInd) (Wang et al., 2020) trains separate classifiers for different subgroups with a shared encoder.
- •Adversarial Training– Learning Adversarially Fair and Transferable Representations (LAFT) (Madras et al., 2018) de-biases the representation by minimizing the ability to recognize sensitive attributes.– Conditional learning of Fair representation (CFair) (Zhao et al., 2019) tries to enforce the balanced error rate and conditional alignment of representations during training.– Learning Not to Learn (LNL) (Kim et al., 2019) unlearns the bias information iteratively by minimizing the mutual information between feature representation and bias.
- – Learning Adversarially Fair and Transferable Representations (LAFT) (Madras et al., 2018) de-biases the representation by minimizing the ability to recognize sensitive attributes.
- – Conditional learning of Fair representation (CFair) (Zhao et al., 2019) tries to enforce the balanced error rate and conditional alignment of representations during training.
- – Learning Not to Learn (LNL) (Kim et al., 2019) unlearns the bias information iteratively by minimizing the mutual information between feature representation and bias.
- •Disentanglement– Entangle and Disentangle (EnD) (Tartaglione et al., 2021) disentangles confounders by inserting an “information bottleneck”, while still passing the useful information.– Orthogonal Disentangled Representations (ODR) (Sarahan et al., 2020) disentangles the useful and sensitive representations by enforcing orthogonality constraints for independence.
- – Entangle and Disentangle (EnD) (Tartaglione et al., 2021) disentangles confounders by inserting an “information bottleneck”, while still passing the useful information.
- – Orthogonal Disentangled Representations (ODR) (Sarahan et al., 2020) disentangles the useful and sensitive representations by enforcing orthogonality constraints for independence.

5

---

<!-- Page 6 -->

Published as a conference paper at ICLR 2023

- •Domain Generalization (DG)– Group Distributionally Robust Optimization (GroupDRO) (Sagawa et al., 2019) minimizes the worst-case training loss with increased regularization.– Stochastic Weight Averaging Densely (SWAD) (Cha et al., 2021), a state-of-the-art method in DG, aims to find a robust flat minima by a dense stochastic weight sampling strategy.– Sharpness-Aware Minimization (SAM) (Foret et al., 2020) seeks parameters that lie in neighborhoods having uniformly low loss during optimization.
- – Group Distributionally Robust Optimization (GroupDRO) (Sagawa et al., 2019) minimizes the worst-case training loss with increased regularization.
- – Stochastic Weight Averaging Densely (SWAD) (Cha et al., 2021), a state-of-the-art method in DG, aims to find a robust flat minima by a dense stochastic weight sampling strategy.
- – Sharpness-Aware Minimization (SAM) (Foret et al., 2020) seeks parameters that lie in neighborhoods having uniformly low loss during optimization.

The hyper-parameter tuning strategy is described in Appendix B.2.2.

### 3.3 MODEL SELECTION

The trade-off between fairness and utility has been widely noted (Kleinberg et al., 2016; Zhang et al., 2022), making hyper-parameter selection criteria particularly difficult to define given the multi-objective nature of optimizing for potentially conflicting fairness and utility. Previous work differs greatly in model selection. Some use conventional utility-based selection strategies, e.g., overall validation loss, while others have no explicit specification. We provide a summary of model selection strategies across the literature in Table A1. To investigate the influence of model selection strategies on the final performance, we study three prevalent selection strategies in MEDFAIR.

Overall Performance-based Selection This is one of the most basic and common strategies for model selection. In this model that has the smallest loss value or highest accuracy/AUC across the validation set of all sub-populations. However, this strategy tends to select the model with better performance in the majority group to achieve the best overall performance, leading to a potentially large performance gap among subgroups, which is illustrated in the red pentagon on the right side of Figure 2 (note that it is not necessarily Pareto optimal).

Minimax Pareto Selection The concept of Pareto optimality was proposed by Mas-Colell et al. (1995) and utilized in fair machine learning to study the trade-off among subgroup accuracies (Martinez et al., 2020). Intuitively, for a model on the Pareto front, no group can achieve better performance without hurting the performance of other groups. In other words, it defines the set of best achievable trade-offs among subgroups (without introducing unnecessary harm). Based on this definition, we select the model that lies on the Pareto front and achieves the best worst-case AUC (the red star in the middle top of Figure 2). We present a formal definition of minimax Pareto selection in Appendix B.4.

DTO-based Selection Distance to optimal (DTO) (Han et al., 2021) is calculated by the normalized Euclidean distance between the performance of the current model and the optimal utopia point. Here, we construct the utopia point by taking the maximum AUC value of each subgroup among all models. The DTO strategy selects the model that has the smallest distance to the utopia point (the red hexagon in Figure 2).

Figure 2. Illustration of three different model selection strategies. Each data point represents a different hyper-parameter combination for one algorithm, where the red points are the models lying on the Pareto front.

### 3.4 EVALUATION AND IMPLEMENTATION

We apply the bias mitigation algorithms to medical image classification tasks and evaluate fairness based on the performance of different subgroups (sensitive attributes). The sensitive attributes are regarded as available for training (if needed). We consider two settings to evaluate fairness for medical imaging, i.e., in-distribution and out-of-distribution.

Evaluation Metrics We use the area under the receiver operating characteristic curve (AUC) as the major metric, which is a commonly used metric for medical binary classification. We evaluate

6

---

<!-- Page 7 -->

Published as a conference paper at ICLR 2023

the algorithms from three aspects: (1) utility: overall AUC across all subgroups; (2) group fairness: AUC gap between the subgroups that have maximum AUC and minimum AUC; (3) Max-Min fairness: AUC of the worst-case group. Besides, we also report the values of binary cross entropy (BCE), expected calibration error (ECE), false positive rate (FPR), false negative rate (FNR), and true positive rate (TPR) at 80% true negative rate (TNR) of each subgroup, as well as the Equalized Odd (EqOdd). We provide detailed explanations of these metrics in Appendix B.3.

Statistical Tests Prior work has empirically evaluated bias mitigation algorithms and occasionally claimed that some algorithm works well based on results from a couple of datasets. We note that to make a stronger conclusion that would be more useful to practitioners, e.g., “algorithm A works better than B for medical imaging” (i.e., A is better general, rather than better for dataset C specifically), one needs to evaluate the algorithms across several datasets and perform significance tests that check for consistently good performance that can not be explained by overfitting to a single dataset. This is where the MEDFAIR benchmark suite comes in. To rigorously compare the relative performance of different algorithms, we perform the Friedman test (Friedman, 1937) followed by Nemenyi post-hoc test (Nemenyi, 1945) to identify if any of the algorithms is significantly better than the others, following the authoritative guide of Demšar (2006). We first calculate the relative ranks among all algorithms on each dataset and sensitive attribute separately, and then take the average ranks for the Nemenyi test if significance is detected by Friedman test. We consider a p-value lower than 0.05 to be statistically significant. The testing results are visualized by Critical Difference (CD) diagrams (Demšar, 2006). In CD diagrams, methods that are connected by a horizontal line are in the same group, meaning they are not significantly different given the p-value, and methods that are in different groups (not connected by the same line) have statistically significant difference.

Implementation Details We adopt 2D and 3D ResNet-18 backbone (He et al., 2016; Hara et al., 2018) for 2D and 3D datasets, respectively. The light backbone is used to avoid overfitting as there are datasets with small sizes, and also to remain consistent with the backbone used in the original literature (Kim et al., 2019; Wang et al., 2020; Tartaglione et al., 2021; Sarhan et al., 2020). Binary cross entropy loss is used as the major objective. To ensure the stability of randomness, for each experiment, we report the mean values and the standard deviations for three separate runs with three randomly selected seeds. Further implementation details for all datasets and algorithms can be found in Appendix B.

## 4 RESULTS

### 4.1 BIAS WIDELY EXISTS IN ML MODELS TRAINED IN DIFFERENT MODALITIES AND TASKS

Firstly, we train ERM on different datasets and sensitive attributes, and select models using the regular overall performance-based strategy. For each dataset and sensitive attribute, we calculate the maximum and minimum AUC and underdiagnosis rate among subgroups, where we use FNR for the malignant group and TPR for the benign group. “No” and “Yes” are the true rate. As shown in Figure 3, most points are to the side of the equality line, showing that the performance gap widely exists. This confirms a problem that has been widely discussed (Seyyed-Kalantari et al., 2021) but, until now, has never been systematically quantified for deep learning across a comprehensive variety of modalities, diagnosis tasks, and sensitive attributes.

### 4.2 MODEL SELECTION SIGNIFICANTLY INFLUENCES WORST-CASE GROUP PERFORMANCE

We study the impact of model selection strategies on ERM using our three metrics of interest. The AUC of the worst-case group, the AUC gap, and overall AUC with ERM. We first conduct a hyper-parameter sweep for ERM while training on all the datasets, and then compute the metrics and the relative ranks of the three model selection strategies. The results, including statistical significance tests are summarised in Figure 4, and the raw data in Table A3. Each sub-plot corresponds to a metric of interest (worst-case AUC, AUC Gap, Overall AUC), and the average rank of each selection strategy (Pareto, DTO, Overall) is shown on a line. Selection strategies not connected by the bold bars have significantly different performances. The results show that for the worst-case AUC metric (left), the Pareto-optimal model selection strategy has the highest average rank of around 1.5, which is statistically significantly better than the overall AUC model selection strategy’s average rank of around 2.5. Meanwhile, in terms of the overall AUC metric (right) the Pareto selection strategy is

7

---

<!-- Page 8 -->

Published as a conference paper at ICLR 2023

Figure 3: The AUC (left) and underdiagnosis rates (right) for the advantaged and disadvantaged subgroups across each dataset and sensitive attribute, when training with ERM. Most points are off the blue equality line, showing that bias widely exists in conventional ERM-trained models.

Figure 4: Influence of model selection strategies on ERM, illustrated in CD diagrams. The higher the rank of the AUC Gap, the smaller the gap.

not significantly worse than the overall model selection strategy. Thus, even without any explicit bias mitigation algorithm, max-min fairness can be significantly improved simply by adopting the corresponding model selection strategy in place of the standard overall strategy – and this intervention need not impose a significant cost to the overall AUC.

#### 4.3 NO METHOD OUTPERFORMS ERM WITH STATISTICAL SIGNIFICANCE

Figure 5: Performance of bias mitigation algorithms summarised across all datasets as average rank CD diagrams. (a) in-distribution, (b) out-of-distribution. SWAD is the highest ranked method for worst- and overall-AUC metrics, but it is still not significantly better than ERM.

We next ask whether any of the purpose-designed bias mitigation algorithms is significantly better than ERM, and which algorithm is best overall? To answer these questions, we evaluate the perfor-

8

---

<!-- Page 9 -->

Published as a conference paper at ICLR 2023

measure of all methods using the Pareto model selection strategy. We report the Nemenyi post-hoc test results on worst-group AUC, AUC gap, and overall AUC in Figure 5 for in-distribution (top row) and out-of-distribution (bottom row) settings with raw data in Tables A9 and A10. For in-distribution, while there are some significant performance differences, no method outperforms ERM significantly for any metric. ERM is always in the best-second-best group (reported without significant differences). The conclusion is the same for the out-of-distribution testing, and some methods that rank higher than ERM in the in-distribution setting perform worse than ERM when deployed to an unseen domain, suggesting that preserving fairness across domain-shift is challenging.

It is worth noting there are some methods that consistently perform better, e.g., SWAD ranks a clear first for the worst-case and overall AUC for both settings, and thus could be a promising method for promoting fairness. However, the statistical significance of our view, SWAD is still not significantly better despite the fact that we use a much larger sample size (number of datasets) than most of the previous fairness studies. This shows that many studies do not use enough number of datasets to justify their desired claims. Our benchmark suite provides the largest collection of medical imaging datasets for fairness to date, and thus provides the best platform for future research to evaluate the efficacy of any method works in a rigorous statistical way.

## 5 DISCUSSION

Source of bias There are multiple confounding effects that can lead to bias, rather than any single easy-to-isolate factor. As summarised in Table 1 and discussed further in Appendix A.4 and E, these include both measurable and unmeasurable factors spanning imbalance in subgroup size, imbalance in subgroup disease prevalence, difference in imaging protocols/time/location, spurious correlations, the intrinsic difference in difficulty of diagnosis for different subgroups, unintentional bias from the human labellers, etc. It is difficult or even impossible to disentangle all of these factors, making algorithms that specifically optimise for one particular factor to succeed.

Failure of the bias mitigation algorithms Although bias mitigation algorithms are not consistently effective across all benchmark suites, we are certainly not trying to disparage them. It is understandable because some are not originally designed for medical imaging, which contains characteristics distinct from those of natural images or tabular data, and more work may be necessary to design medical imaging specific solutions. More fundamentally, different algorithms may succeed if addressing solely the specific confounding factors for which they are designed to compensate, but fail when presented with other confounders or a mixture of multiple confounders. For example, resampling specifically targets data imbalance, while disentangling focuses more on removing spurious correlations. But real datasets may also simultaneously contain other potential sources of bias such as label noise. This may explain why SWAD is the most consistently high-ranked algorithm, as it optimises a general notion of robustness without any specific assumption on confounders or sensitive attributes, and thus may be more broadly beneficial to different confounding factors.

Relation of domain generalization and fairness The aim of domain generalization (DG) algorithms is to maintain stable performance on unseen sub-populations, while the fairness-promoting algorithms try to ensure that no known sub-populations are poorly treated. Despite this difference, they share the eventual goal — being robust to changes in distribution across different sub-populations. As shown in section 4, some domain generalization methods, such as SWAD, consistently improve the performance of all subgroups, and thus overall utility. However, we also notice that they may also entangle the performance gap among subgroups. It introduces a question of whether a systematically better algorithm (i.e., improving Max-Min fairness) is fairer if it increases the disparity (i.e., not satisfying group fairness)? This question goes beyond machine learning and depends on application scenarios. We suggest that a relevant differentiator may be between diagnosis and zero-sum resource allocation problems where Max-Min and group fairness could be prioritised respectively.

Are the evaluations enough for now? Although we have tried our best to include a diverse set of algorithms and datasets in our benchmark, it is certainly not exhaustive. There are methods to promote fairness from other perspectives, e.g., self-supervised learning may be more robust (Liu et al., 2021; Aizii et al., 2022). Also, datasets from other medical data modalities (e.g., cardiology, digital pathology) should be used. Beyond image classification, other important tasks in medical imaging, such as segmentation, regression, and detection, are underexplored. We will keep our codebase alive and actively incorporate more algorithms, datasets, and even other tasks in the future.

9

---

<!-- Page 10 -->

Published as a conference paper at ICLR 2023

REPRODUCIBILITY STATEMENT

We report the data preprocessing in Appendix B.1.2, hyper-parameter space in Appendix B.2.2. All of the datasets we use are publicly available, and we provide the download links in Table A6. Source code and documentation are available at https://yse-zong.github.io/MEDFAIR/. Running all the experiments required ~ 0.77 NVIDIA A100-SXM-80GB GPU years.

ACKNOWLEDGMENT

Yongshuo Zong is supported by the United Kingdom Research and Innovation (grant EP/S02431X/1), UKRI Centre for Doctoral Training in Biomedical AI at the University of Edinburgh, School of Informatics. For the purpose of open access, the author has applied a creative commons attribution (CC BY) licence to any author accepted manuscript version arising. We thank Dr. Maria Valdés Hernández for the discussion of data preprocessing. We acknowledge the data resources providers at Appendix F.

REFERENCES

Parnian Afshar, Shahin Heidarian, Nastaran Eshaei, Farnoosh Naderkhanian, Moezinedd Javid Rafiei, Anastasia Oikonomou, Faranak Babaki Fard, Kavesh Samimi, Konstantinos N Plataniotis, and Arash Mohammadi. Covid-et-md, covid-19 computed tomography scan dataset applicable in machine learning and deep learning. Scientific Data, 8(1):1–8, 2021.

Shekoofeh Azizi, Laura Culp, Jan Freyberg, Basil Mustafa, Sebastian Baur, Simon Koblith, Ting Chen, Patricia MacWilliams, S Sara Mahdavi, Ellery Wulczyn, et al. Robust and efficient medical imaging with self-supervision. arXiv preprint arXiv:2205.09723, 2022.

Solon Barocas and Andrew D Selbst. Big data’s disparate impact. Calif. L. Rev., 104:671, 2016.

Tom L Beauchamp. Methods and principles in biomedical ethics. Journal of Medical ethics, 29(5): 269–274, 2003.

Rachel KE Bellamy, Kuntal Day, Michael Hind, Samuel C Hoffman, Stephanie Houde, Kalapriya Kaman, Pranay Lohia, Jacquelyn Martino, Sameep Mehta, Aleksandra Mojsilović, et al. Ai fairness 360: An extensible toolkit for detecting and mitigating algorithmic bias. IBM Journal of Research and Development, 63(4/5):4–1, 2019.

Aharon Ben-Tal, Laurent El Ghaoui, and Arkadi Nemirovski. Robust optimization, volume 28. Princeton university press, 2009.

Lukas Biewald. Experiment tracking with weights and biases, 2020. URL https://www.wandb.com/. Software available from wandb.com.

Sarah Bird, Miro Dudík, Richard Edgar, Brandon Horn, Roman Lutz, Vanessa Milan, Mehroosh Samaki, Hanna Wallach, and Kathleen Walker. Fairlearn: A toolkit for assessing and improving fairness in ai. Microsoft, Tech. Rep. MSR-TR-2020-32, 2020.

Campbell Brown. Giving up levelling down. Economics & Philosophy, 19(1):111–134, 2003.

Joao Carreira and Andrew Zisserman. Quo vadis, action recognition? a new model and the kinetics dataset. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 6299–6308, 2017.

Alessandro Castelnovo, Riccardo Crupi, Greta Greco, Daniele Regoli, Ilaria Giuseppina Penco, and Andrea Claudio Cosini. A clarification of the nuances in the fairness metrics landscape. Scientific Reports, 12(1):1–21, 2022.

Junbin Cha, Sanghyuk Chun, Kyungjae Lee, Han-Cheol Cho, Seungyun Park, Yunsung Lee, and Sungrae Park. Swad: Domain generalization by seeking flat minima. Advances in Neural Information Processing Systems, 34:22405–22418, 2021.

10

---

<!-- Page 11 -->

Published as a conference paper at ICLR 2023

Shubham Chaudhary, Sadbhawna Sauthawna, Vinit Jakhetiya, Badri N Subudhi, Ujjwal Baid, and Sharath Chandra Guntuku. Detecting covid-19 and community acquired pneumonia using chest ct scan images with deep learning. In ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 8583–8587. IEEE, 2021.

Juan M Zambrano Chaves, Akshay S Chaudhari, Andrew L Wentland, Arjun D Desai, Imon Banerjee, Robert D Boutin, David J Maron, Fatima Rodriguez, Alexander T Sandhu, R Brooke Jeffrey, et al. Opportunistic assessment of ischemic heart disease risk using abdominal/pelvic computed tomography and medical record data: a multimodal explainable artificial intelligence approach. medRxiv, 2021.

Nitesh V Chawla, Kevin W Bowyer, Lawrence O Hall, and W Philip Kegelmeyer. Smote: synthetic minority over-sampling technique. Journal of artificial intelligence research, 16:321–357, 2002.

Irene Chen, Fredrik D Johansson, and David Sontag. Why is my classifier discriminatory? Advances in neural information processing systems, 31, 2018.

Richard J Chen, Tiffany Y Chen, Jana Lipkova, Judy J Wang, Drew FK Williamson, Ming Y Lu, Sharifa Sahai, and Faisal Mahmood. Algorithm fairness in ai for medicine and healthcare. arXiv preprint arXiv:2110.00603, 2021.

Thomas Christiano and Will Braynen. Inequality, injustice and levelling down. Ratio, 21(4):392–420, 2008.

Elliott Creager, David Madras, Jörn-Henrik Jacobsen, Marissa Weis, Kevin Swersky, Toniann Pitassi, and Richard Zemel. Flexibly fair representation learning by disentanglement. In International conference on machine learning, pp. 1436–1445. PMLR, 2019.

Elliott Creager, Jörn-Henrik Jacobsen, and Richard Zemel. Exchanging lessons between algorithmic fairness and domain generalization. 2020.

Janez Demšar. Statistical comparisons of classifiers over multiple data sets. The Journal of Machine learning research, 7:1–30, 2006.

Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition, pp. 248–255. Ieee, 2009.

Emily Diana, Wesley Gill, Michael Kearns, Krishnaram Kenthapadi, and Aaron Roth. Minimax group fairness: Algorithms and experiments. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society, pp. 66–76, 2021.

Brett Doran. Reconsidering the levelling-down objection against egalitarianism. Utilitas, 13(1): 65–85, 2001.

John Duchi, Peter Glynn, and Hongseok Namkooa. Statistics of robust optimization: A generalized empirical likelihood approach. arXiv preprint arXiv:1610.03425, 2016.

Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Richard Zemel. Fairness through awareness. In Proceedings of the 3rd innovations in theoretical computer science conference, pp. 214–226, 2012.

Sina Farsius, Stephanie J Chiu, Rachelle V O’Connell, Francisco A Folgar, Eric Yuan, Joseph A Izatt, Cynthia A Toth, Age-Related Eye Disease Study 2 Ancillary Spectral Domain Optical Coherence Tomography Study Group, et al. Quantitative classification of eyes with and without intermediate age-related macular degeneration using optical coherence tomography. Ophthalmology, 121(1): 162–172, 2014.

Hortense Fong, Vineet Kumar, Anay Mehrotra, and Nisheth K Vishnoi. Fairness for auc via feature augmentation. arXiv preprint arXiv:2111.12823, 2021.

Pierre Foret, Ariel Kleiner, Hossein Mohabi, and Behnam Neyshabur. Sharpness-aware minimization for efficiently improving generalization. arXiv preprint arXiv:2010.01412, 2020.

11

---

<!-- Page 12 -->

Published as a conference paper at ICLR 2023

Sorelle A Friedler, Carlos Scheidegger, Suresh Venkatasubramanian, Sonam Choudhary, Evan P Hamilton, and Derek Roth. A comparative study of fairness-enhancing interventions in machine learning. In Proceedings of the conference on fairness, accountability, and transparency, pp. 329–338, 2019.

Milton Friedman. The use of ranks to avoid the assumption of normality implicit in the analysis of variance. Journal of the american statistical association, 32(200):675–701, 1937.

Josh Gardner, Christopher Brooks, and Ryan Baker. Evaluating the fairness of predictive student models through slicing analysis. In Proceedings of the 9th international conference on learning analytics & knowledge, pp. 225–234, 2019.

Judy Wawira Gichoya, Imon Banerjee, Ananth Reddy Bhimireddy, John L Burns, Leo Anthony Celi, Li-Ching Chen, Ramon Correa, Natalie Dullerud, Marzyeh Ghassemi, Shih-Cheng Huang, et al. AI recognition of patient race in medical imaging: a modelling study. The Lancet Digital Health, 2022.

Ary L Goldberger, Luis An Amaral, Leon Glass, Jeffrey M Hausdorff, Plamen Ch Ivanov, Roger G Mark, Joseph E Mietus, George B Moody, Chung-Kang Peng, and H Eugene Stanley. PhysioBank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals. circulation, 101(23):e215–e220, 2000.

Matthew Groh, Caleb Harris, Luis Soensken, Felix Lau, Rachel Han, Aerin Kim, Arash Koocheh, and Omar Badri. Evaluating deep neural networks trained on clinical images in dermatology with the Fitzpatrick 17k dataset. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 1820–1828, 2021.

Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. On calibration of modern neural networks. In International conference on machine learning, pp. 1321–1330. PMLR, 2017.

Xudong Han, Timothy Baldwin, and Trevor Cohn. Balancing out bias: Achieving fairness through balanced training. arXiv, 2021.

Xudong Han, Ali Shen, Yitong Li, Lea Fremmann, Timothy Baldwin, and Trevor Cohn. fairlib: A unified framework for assessing and improving classification fairness. arXiv preprint arXiv:2205.01876, 2022.

Kensho Hara, Hirokatsu Kataoka, and Yutaka Satoh. Can spatiotemporal 3d cnns retrace the history of 2d cnns and imagenet? In Proceedings of the IEEE conference on Computer Vision and Pattern Recognition, pp. 6546–6555, 2018.

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 770–778, 2016.

Deborah Hellman. When is discrimination wrong? Harvard University Press, 2008.

Sepp Hochreiter and Jürgen Schmidhuber. Flat minima. Neural computation, 9(1):1–42, 1997.

Badr Youbi Idrissi, Martin Arjovsky, Mohammad Pezeshki, and David Lopez-Paz. Simple data balancing achieves competitive worst-group-accuracy. In Conference on Causal Learning and Reasoning, pp. 336–351. PMLR, 2022.

Jeremy A. Irvin, Pranav Rajpurkar, Michael Ko, Yifan Yu, Silviana Ciurea-Illusc, Chris Chute, Henrik Markland, Belzad Haghogh, Rohyn L. Ball, Katie S. Shpansky, Jayne Seekins, David Andrew Mong, Safwan S. Halabi, Jesse K. Sandberg, Ricky Jones, David B. Larson, C. Langlotz, Bhavik N. Patel, Matthew P. Lungren, and A. Ng. Cheppert: A large chest radiograph dataset with uncertainty labels and expert comparison. In AAAI, 2019.

Pavel Izmailov, Dmitrii Podoprikin, Timur Garipov, Dmitry P. Vetrov, and Andrew Gordon Wilson. Averaging weights leads to wider optima and better generalization. In Amir Globerson and Ricardo Silva (eds.), Proceedings of the Thirty-Fourth Conference on Uncertainty in Artificial Intelligence, UAI 2018, Monterey, California, USA, August 6-10, 2018, pp. 876–885. AUAI Press, 2018. URL http://auai.org/uai2018/proceedings/papers/313.pdf.

12

---

<!-- Page 13 -->

Published as a conference paper at ICLR 2023

Alistair Johnson, Lucas Bulgarelli, Tom Pollard, Steven Horng, Leo Anthony Celi, and Roger Mark. Mimic-iv. PhysioNet. Available online at: https://physionet.org/content/mimiciv/1.0/accepted/August%23,2021%2C2020.

Alistair EW Johnson, Tom J Pollard, Nathaniel R Greenbaum, Matthew P Langren, Chih-ying Deng, Yifan Peng, Zhiyong Lu, Roger G Mark, Seth J Berkowitz, and Steven Horng. Mimic-cx-jpg, a large publicly available database of labeled chest radiographs. arXiv preprint arXiv:1901.07042, 2019.

Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp mining. arXiv preprint arXiv:1609.04836, 2016.

Sajad Khodadadian, AmirMerd Ghassami, and Negar Kiyavash. Impact of data processing on fairness in supervised learning. In 2021 IEEE International Symposium on Information Theory (ISIT), pp. 2643–2648. IEEE, 2021.

Byungju Kim, Hyunwoo Kim, Kyungsi Kim, Sungjin Kim, and Junmo Kim. Learning not to learn: Training deep neural networks with biased data. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9012–9020, 2019.

Newton M Kinyanjui, Timothy Odonaga, Celia Cintas, Noel CF Codella, Rameswar Panda, Prasanna Sattigeri, and Kush R Varshney. Fairness of classifiers across skin tones in dermatology. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pp. 320–329. Springer, 2020.

Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan. Inherent trade-offs in the fair determination of risk scores. arXiv preprint arXiv:1609.05807, 2016.

Oleksandr Kovalyuk, Juan Morales-Sánchez, Rafael Verdú-Monedero, Immaculada Sellés-Navarro, Ana Palazón-Cabanes, and José-Luis Sancho-Gómez. Papila: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment. Scientific Data, 9(1):1–12, 2022.

Matt J Kusner, Joshua Loftus, Chris Russell, and Ricardo Silva. Counterfactual fairness. Advances in neural information processing systems, 30, 2017.

Preeti Lahoti, Alex Beutel, Jiilin Chen, Kang Lee, Flavien Prost, Nithum Thain, Xuezhi Wang, and Ed Chi. Fairness without demographics through adversarially reweighted learning. Advances in neural information processing systems, 33:728–740, 2020.

Agostina J Larrazabal, Nicolás Nieto, Victoria Peterson, Diego H Milone, and Enzo Ferrante. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis. Proceedings of the National Academy of Sciences, 117(23):12592–12594, 2020.

Chelsea E Lee, Kaela S Singleton, Melissa Wallin, and Victor Faundez. Rare genetic diseases: nature’s experiments on human development. Science, 23(5):101123, 2002.

June-Goo Lee, Sanghoon Jun, Young-Won Cho, Hyunna Lee, Guk Bae Kim, Joon Beom Seo, and Namkyung Kim. Deep learning in medical imaging: general overview. Korean journal of radiology, 18(4):570–584, 2017.

Jungsoo Lee, Eungyeup Kim, Juyoung Lee, Jihyeon Lee, and Jaegul Choo. Learning debiased representation via disentangled feature augmentation. Advances in Neural Information Processing Systems, 34:25123–25133, 2021.

Hong Liu, Jeff Z HaoChen, Adrien Gaidon, and Tengyu Ma. Self-supervised learning is more robust to dataset imbalance. arXiv preprint arXiv:2110.05925, 2021.

Jianfang Liu, Tara Lichtenberg, Katherine A Hoadley, Laila M Poisson, Alexander J Lazar, Andrew D Cherniack, Albert J Kovatch, Christopher C Benz, Douglas A Levine, Adrian V Lee, et al. An integrated tega pan-cancer clinical data resource to drive high-quality survival outcome analytics. Cell, 173(2):400–416, 2018.

13

---

<!-- Page 14 -->

Published as a conference paper at ICLR 2023

Francesco Locatello, Gabriele Abbati, Thomas Rainforth, Stefan Bauer, Bernhard Schölkopf, and Olivier Bachem. On the fairness of disentangled representations. Advances in Neural Information Processing Systems, 32, 2019.

Gilles Louppe, Michael Kagan, and Kyle Cranmer. Learning to pivot with adversarial networks. Advances in neural information processing systems, 30, 2017.

David Madras, Elliot Creager, Toniann Pitassi, and Richard Zemel. Learning adversarially fair and transferable representations. In International Conference on Machine Learning, pp. 3384–3393. PMLR, 2018.

Roman C Maron, Michael Weichenthal, Jochen S Utikal, Achim Hekler, Carola Berking, Axel Hauschild, Alexander H Enk, Sebastian Haferkamp, Joachim Klode, Dirk Schadendorf, et al. Systematic outperformance of 112 dermatologists in multiclass skin cancer image classification by convolutional neural networks. European Journal of Cancer, 119:57–65, 2019.

Natalia Martinez, Martin Bertran, and Guillermo Sapiro. Minimax pareto fairness: A multi objective perspective. In International Conference on Machine Learning, pp. 6755–6764. PMLR, 2020.

Andreu Mas-Colell, Michael Dennis Whinston, Jerry R Green, et al. Microeconomic theory, volume 1. Oxford university press New York, 1995.

Ninareh Mehrafi, Fred Moststater, Nripsuta Saxena, Krisiina Lerman, and Aram Galstyan. A survey on bias and fairness in machine learning. ACM Computing Surveys (CSUR), 54(6):1–35, 2021.

Kaisa Miettinen. Introduction to multiobjective optimization: Noninteractive approaches. In Multi-objective optimization, pp. 1–26. Springer, 2008.

Peter Bjorn Nemyenyi. Distribution-free multiple comparisons. Princeton University, 1963.

Jeremy Nixon, Michael W Dusenberry, Linchuan Zhang, Ghassem Jerfel, and Dustin Tran. Measuring calibration in deep learning. In CVPR Workshops, volume 2, 2019.

Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan. Dissecting racial bias in an algorithm used to manage the health of populations. Science, 366(6464):447–453, 2019.

Sungbo Park, Jewook Lee, Pilhyeon Lee, Sunhee Hwang, Dohyung Kim, and Hyeran Byun. Fair contrastive learning for facial attribute classification. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 10389–10398, 2022.

R. C. Petersen, P. S. Aisen, L. A. Beckett, M. C. Donohue, A. C. Gamst, D. J. Harvey, C. R. Jack, W. J. Jagust, L. M. Shaw, A. W. Toga, J. Q. Trojanowski, and M. W. Weiner. Alzheimer’s disease neuroimaging initiative (adni). Neurology, 74(3):201–209, 2010. ISSN 0028-3878. doi: 10.1212/WNL.0b013e3181cb3e25.

Geoff Pleiss, Manish Raghavan, Felix Wu, Jon Kleinberg, and Kilian Q Weinberger. On fairness and calibration. Advances in neural information processing systems, 30, 2017.

John Rawls. Justice as fairness: A treatise. Harvard University Press, 2001.

Charan Reddy, Deepak Sharma, Soroush Mehri, Adriana Romero-Soriano, Samira Shabanian, and Sina Honari. Benchmarking bias mitigation algorithms in representation learning through fairness metrics. In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1), 2021.

Amelie Royer and Christoph H Lampert. Classifier adaptation at prediction time. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 1401–1409, 2015.

Shiori Sagawa, Pang Wei Koh, Tatsunori B Hashimoto, and Percy Liang. Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. arXiv preprint arXiv:1911.08731, 2019.

Mild Hasan Sarhan, Nassir Navab, Abouzar Eslami, and Shadi Albarquani. Fairness by learning orthogonal disentangled representations. In European Conference on Computer Vision, pp. 746–761. Springer, 2020.

14

---

<!-- Page 15 -->

Published as a conference paper at ICLR 2023

Laleh Seyyed-Kalantari, Guanxiong Liu, Matthew McDermott, Irene Y Chen, and Marzieh Ghaseemi. Chexclusion: Fairness gaps in deep chest x-ray classifiers. In BIOCOMPUTING 2021: proceedings of the Pacific symposium, pp. 232–243. World Scientific, 2020.

Laleh Seyyed-Kalantari, Haoran Zhang, Matthew McDermott, Irene Y Chen, and Marzieh Ghaseemi. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature medicine, 27(12):2176–2182, 2021.

Christine S Spencer, Darrell J Gaskin, and Eric T Roberts. The quality of care delivered to patients within the same hospital varies by insurance type. Health Affairs, 32(10):1731–1739, 2013.

Cathie Sudlow, John Gallacher, Naomi Allen, Valerie Beral, Paul Burton, John Danesh, Paul Downey, Paul Elliott, Jane Green, Martin Landray, et al. UK biobank: an open access resource for identifying the causes of a wide range of complex diseases of midland and old age. PLoS medicine, 12(3):e1001779, 2015.

Enzo Tartaglione, Carlo Alberto Barbano, and Marco Grangetto. End: Entangling and disentangling deep representations for bias correction. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 13508–13517, 2021.

Philipp Tschandl, Cliff Rosendahl, and Harald Kiltner. The ham10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Scientific data, 5(1):1–9, 2018.

Berk Ustun, Yang Liu, and David Parkes. Fairness without harm: Decoupled classifiers with preference guarantees. In International Conference on Machine Learning, pp. 6373–6382. PMLR, 2019.

Vladimir N Vapnik. An overview of statistical learning theory. IEEE transactions on neural networks, 10(5):988–999, 1999.

Sahil Verma and Julia Rubin. Fairness definitions explained. In 2018 ieee/acm international workshop on software fairness (fairware), pp. 1–7. IEEE, 2018.

Zeyu Wang, Klint Qinani, Ioannis Christos Karakozis, Kyle Genova, Prem Nair, Kenji Hata, and Olga Russakovsky. Towards fairness in visual recognition: Effective strategies for bias mitigation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 8919–8928, 2020.

David Wen, Saad M Khan, Antonio Ji Xu, Hussein Ibrahim, Luke Smith, Jose Caballero, Luis Zepeda, Carlos de Blas Perez, Alastair K Denniston, Xiaoxuan Liu, et al. Characteristics of publicly available skin cancer image datasets: a systematic review. The Lancet Digital Health, 2021.

Julia K Winkler, Christine Fink, Ferdinand Toberer, Alexander Enk, Teresa Deinlein, Rainer Hofmann-Wellenhof, Luc Thomas, Ainiolos Lillas, Andreas Blum, Wilhelm Stolz, et al. Association between surgical skin markings in dermatoscopic images and diagnostic performance of a deep learning convolutional neural network for melanoma recognition. JAMA dermatology, 155(10):1135–1141, 2019.

Qizhe Xie, Zihang Dai, Yulun Du, Edward Hovy, and Graham Neubig. Controllable invariance through adversarial feature learning. Advances in neural information processing systems, 30, 2017.

Brian Hu Zhang, Blake Lemoine, and Margaret Mitchell. Mitigating unwanted biases with adversarial learning. In Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society, pp. 335–340, 2018.

Haoran Zhang, Natalie Dullerud, Karsten Roth, Lauren Odden-Royer, Stephen Pfohl, and Marzieh Ghaseemi. Improving the fairness of chest x-ray classifiers. In Conference on Health, Inference, and Learning, pp. 204–233. PMLR, 2022.

Han Zhao, Amanda Coston, Tameem Adel, and Geoffrey J Gordon. Conditional learning of fair representations. In International Conference on Learning Representations, 2019.

15

---

<!-- Page 16 -->

Published as a conference paper at ICLR 2023

Yuyin Zhou, Shih-Cheng Huang, Jason Alan Fries, Alaa Youssef, Timothy J. Amrhein, Marcello Chang, Imon Banerjee, Daniel L. Rubin, Lei Xing, Nigam H. Shah, and Matthew P. Lungren. Radfusion: Benchmarking performance and fairness for multimodal pulmonary embolism detection from ct and ehr. ArXiv, abs/2111.11665, 2021.

Dominik Zietlow, Michael Lohaus, Guha Balakrishnan, Matthäus Kleindessner, Francesco Locatello, Bernhard Schölkopf, and Chris Russell. Leveling down in computer vision: Pareto inefficiencies in fair deep classifiers. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 10410–10421, 2022.

16

---

<!-- Page 17 -->

Published as a conference paper at ICLR 2023

## A RELATED WORK

In Appendix A, We present a broad review of the model selection strategies adopted by existing literature, current bias mitigation algorithms, existing fairness benchmarks, and domain generalization methods and their relationship to fairness.

### A.1 MODEL SELECTION STRATEGY IN FAIRNESS

Considering the trade-off between fairness and the utility, how to select the appropriate model among hyper-parameters remains an important problem. We broadly review and summarize the model selection strategies of recent work in Table A1. N/A means they do not explicitly specify their model selection strategies in their papers (although they may have implemented it in their open-source code). It can be seen that the model selection strategies differ greatly among existing literature, making a direct comparison infeasible. Hence, we investigate the influence of model selection strategies in our study.

Table A1: Summary of model selection strategies of fairness-aware methods and benchmarks.

| Reference | Paper Type | Selection Strategy | Dataset Type | Model Type |
| --- | --- | --- | --- | --- |
| Locatello et al. (2019) | Benchmark | N/A | Images | Deep |
| Reddy et al. (2021) | Benchmark | Report best test results for each metric | Tabular / Images | Shallow |
| Zhang et al. (2022) | Benchmark | Best validation worst-group AUC | Images | Deep |
| Han et al. (2022) | Benchmark | Best validation loss / DTO | NLP | Deep |
| Friedler et al. (2019) | Benchmark | N/A | Tabular | Shallow |
| Wang et al. (2020) | Method | Best validation weighted mAP | Images | Deep |
| Madras et al. (2018) | Method | Report fairness/accuracy trade-off | Tabular | Shallow |
| Zhao et al. (2019) | Method | Report fairness/accuracy trade-off | Tabular | Shallow |
| Creager et al. (2019) | Method | Report fairness/accuracy trade-off | Tabular/Images | Shallow/Deep |
| Kim et al. (2019) | Method | N/A | Images | Deep |
| Tartaglione et al. (2021) | Method | Optimized on validation set | Images | Deep |
| Sarhan et al. (2020) | Method | Best validation loss | Images | Deep |
| Park et al. (2022) | Method | N/A | Images | Deep |
| Martinez et al. (2020) | Method | Best validation worst-group risk | Images/Tabular | Shallow/Deep |
| Idrissi et al. (2022) | Method | Best validation worst-group accuracy | Images | Deep |
| Lalabi et al. (2020) | Method | Best validation overall AUC | Tabular | Shallow |
| Lee et al. (2021) | Method | N/A | Images | Deep |

### A.2 BIAS MITIGATION ALGORITHMS

According to the stage when bias mitigation methods are introduced, they can be mainly classified into three categories, namely pre-processing, in-processing, and post-processing. The pre-processing methods aim to curate the data in the dataset to remove the potential bias before learning a model (Khodadadian et al., 2021), while the post-processing methods seek to adjust the predictions given a trained model according to the sensitive attributes (Pleiss et al., 2017). In this paper, we focus on benchmarking in-processing methods, which aim to mitigate the bias during the training of the models. Below, we review four popular categories of bias mitigation algorithms.

Subgroup Rebalancing For imbalanced data, synthetic minority oversampling technique (SMOTE) (Chawla et al., 2002) is a classic resampling method that over-samples the minority class and under-samples the majority class. Recent work found that simply using data balancing can effectively improve the worst-case group accuracy (Idrissi et al., 2022).

Domain-Independence Wang et al. (2020) develop a domain-independent training strategy that applies different classification heads to different subgroups. (Royer & Lampert, 2015) propose

17

---

<!-- Page 18 -->

Published as a conference paper at ICLR 2023

classifier adaption strategies in the prediction time to reduce the error rates when the distribution of testing domain is different.

Adversarial Learning There are two major categories of adversarial learning: (1) it plays a minimax game that the classification head tries to achieve the best classification performance while minimizing the ability of the discriminator to predict the sensitive attributes (Zhang et al., 2018; Kim et al., 2019). After training, the sensitive attributes in the representation are expected to be indistinct. (2) it enforces the fairness constraints (e.g., group fairness) on the representation during training, and the representation is used for downstream tasks later (Xie et al., 2017; Madras et al., 2018; Zhao et al., 2019).

Disentanglement Disentanglement methods (Tartaglione et al., 2021; Sarhan et al., 2020; Creager et al., 2019; Lee et al., 2021) isolates independent factors of variation into different and independent components of a representation vector. In other words, these methods disentangle the sensitive attributes and task-relevant information in the representation level. Then, the classification tasks can be conducted on representation containing only task-specific representation so that the sensitive attributes and other unobserved factors will not make an impact.

In our benchmark, we select typical in-processing algorithms from these categories to provide a comprehensive comparison.

### A.3 FAIRNESS BENCHMARKS

There are efforts in general machine learning communities to benchmark the performance of the fairness-aware algorithms, inspecting their effectiveness in different aspects. AIF360 (Bellamy et al., 2019) implements a wide range of fairness metrics and debiasing algorithms, which is available in both Python and R language. Fairlearn (Bird et al., 2020) also provides debiasing algorithms and fairness metrics to evaluate ML models. Friedler et al. (2019) benchmark a series of fairness-aware machine learning techniques. However, they only study the traditional machine learning models. For deep learning models, Reddy et al. (2021) benchmark algorithms from the perspective of representation learning on synthetic datasets, and find they can successfully remove spurious correlation. Locatello et al. (2019) specifically benchmark the disentanglement fair representation learning methods on 3D shape datasets, suggesting disentanglement can be a useful property to encourage fairness.

In the area of computational medicine, machine learning models have been found to demonstrate a systematic bias toward a wide range of attributes, such as race, gender, age, and even the health insurance type (Obermeyer et al., 2019; Larranzabal et al., 2020; Spencer et al., 2013; Seyyed-Kalanari et al., 2021). The bias also exists in different types of medical data, such as chest X-ray (Seyyed-Kalanari et al., 2020), CT scans (Zhou et al., 2021), skin dermatology (Kinyanjui et al., 2020), health record (Obermeyer et al., 2019), etc.

The most relevant work to ours is Zhang et al. (2022), which compares a series of algorithms on chest X-ray images, and finds no method outperforms simple data balancing. However, it is unclear whether the conclusion can be generalized to other medical imaging modalities, and whether the selection of methods is comprehensive. In contrast, we benchmark a wider range of algorithms on different data modalities, study the ultimately more significant issue of model selection, and provide further analysis on the underlying mechanisms of algorithms and evaluation algorithms. To the best of our knowledge, we are the first to provide a comprehensive benchmark for a wide range of algorithms and datasets, and a comprehensive analysis of different model selection criteria.

### A.4 SOURCE OF BIAS

Data imbalance across subgroups is one of the most common sources of bias for medical imaging, as many biomedical examples lack demographic diversity. For example, many datasets are developed with individuals originating from European ancestries, such as UK Biobank and The Cancer Genome Atlas (TCGA) (Snouvel et al., 2015; Liu et al., 2018). Also, more data samples in total will be from older people if the dataset is collected to study a specific disease that occurs in older people, e.g. dataset for Age-related macular degeneration (AMD) (Farsiu et al., 2014). Overall,

18

---

<!-- Page 19 -->

Published as a conference paper at ICLR 2023

when there are more samples in one subgroup than the other, it can be expected that the machine learning model may have different prediction accuracy for different subgroups.

Class imbalance can occur along with the data imbalance, where one subgroup has more samples of some specific classes while the other subgroup has more samples from other classes. For example, in the AMD dataset, subgroups of older people contain more pathology examples than subgroups of younger people. Also, the problem of class imbalance happens for rare diseases, which is generally due to genetic mutations that occur in a very limited number of people (Lee et al., 2020), e.g., 10 in 1,000,000. So, the class imbalance is severe and there would never be enough data (even worldwide) for a balanced representation in the training set.

Spurious correlation can be learned by machine learning models undesirably from imaging devices. For example, a model can learn to classify skin diseases by looking at the markings placed by dermatologists near the lesions, instead of really learning the diseases (Walter et al., 2019). It is also related to the fact that correlation and class imbalance are two different concepts that may occur more frequently in a subgroup with a smaller number of examples by simply remembering all the data points, i.e., overfitting. Moreover, class imbalance itself may lead to a spurious correlation. For example, the model may try to use age-related features to predict pathology in a dataset where most of the older patients are unhealthy.

Label noise can also be a source of bias for medical imaging datasets. As the labeling of medical imaging datasets is labor-intensive and time-consuming, some large-scale datasets are labeled by automatic tools (Irvin et al., 2019; Johnson et al., 2019), which may not be precisely accurate and thus introduce noises. Zhang et al. (Zhang et al., 2022) recruit a board-certified radiologist to relabel a subset of the chest X-ray dataset CheXpert, and find that the label noises are much higher in some subgroups than the others.

Inherent characteristics of the data of certain subgroups can lead to different performance for different subgroups even if the dataset is balanced, i.e., the tasks in some subgroups are inherently difficult even for humans. For example, in skin dermatology images, the lesions are usually more difficult to recognize for darker skin than that for light skin due to the low contrast (Wen et al., 2021). Thus, even with balanced datasets, a trained ML model can still give lower accuracy to patients with darker skin. Considering this, other measures beyond algorithms should be adopted to promote fairness, such as collecting more representative samples and improving imaging devices.

In summary, the bias is usually not from a single source, and different sources of bias also usually correlate with each other, leading to the unfairness of the machine learning model.

## A.5 DOMAIN GENERALIZATION AND FAIRNESS

Domain generalization (DG) algorithms aim to maintain good performance on unseen subpopulation, while fairness-promoting algorithms try to ensure that no known sub-population is poorly treated. CSDM, though differing in detail, their eventuality goal is the same—being robust to distribution changes across different sub-populations, which is also discussed in (Craeger et al., 2020). Hence, in this work, we also explore fairness from the perspective of domain generalization.

One line of work for DG is to treat it as a robust optimization problem (Ben-Tal et al., 2009), where the goal is to try to minimize the worst-case loss for subgroups of the training set. Duchi et al. (2016) propose to minimize the worst-case loss for constructed distributional uncertainty sets with Distributionally Robust Optimization (DRO). GroupDRO (Sagawa et al., 2019) extends this idea by adding increased regularization to overparameterized networks and achieves good worst-case performance.

Another line of work focuses on finding flat minima in the loss landscape during optimization. As flat minima in the loss landscape is considered to be able to generalize better to different domains (Hochreiter & Schmidhuber, 1997), methods have been proposed to optimize for flatness (Izmailov et al., 2018; Chu et al., 2021; Keskar et al., 2016; Foret et al., 2020). Stochastic weight averaging (SWA) (Izmailov et al., 2018) finds flat minima by averaging model weights during parameters updating every K epoch. Stochastic weight averaging densely (SWAD) adopts a similar weight ensemble strategy to SWA, but with weights densely, i.e., for every iteration. Also, SWAD searches the start and end iterations for averaging by considering the validation loss to avoid overfitting. Sharpness-aware minimization (SAM) (Foret et al., 2020) finds flat minima by seeking parameters

19

---

<!-- Page 20 -->

Published as a conference paper at ICLR 2023

that lie in neighborhoods having uniformly low loss. We select three popular methods of them in our benchmark — GroupDRO, SAM, and SWAD.

20

---

<!-- Page 21 -->

Published as a conference paper at ICLR 2023

## B IMPLEMENTATION AND EVALUATION DETAILS

### B.1 DATA

#### B.1.1 DATASET

We summarize the statistics of the subgroups and class labels in Table A2 to A5. The numbers with percentages out of the brackets are the percentage of the appearing prevalence, and the numbers in the brackets are the percentage of being unhealthy (class label). The used datasets are all publicly available, but we cannot directly include the downloading links in our benchmark. Thus we provide the access links in Table A6 provides.

Table A2: The statistics of the subgroups and class labels. The numbers with percentages out of the brackets are the percentage of the appearing prevalence, and the numbers in the brackets are the percentage of being unhealthy (class label).

|   | CheXpert | MIMIC-CXR | HAM10000 |
| --- | --- | --- | --- |
| **# Images** | 222,793 | 370,955 | 9,948 |
| **# Patients** | 64,428 | 222,793 | Unknown |
| **Male** | 59.34% (90.12%) | 52.16% (62.64%) | 54.28% (16.81%) |
| **Female** | 40.65% (89.78%) | 47.83% (57.11%) | 45.72% (11.65%) |
| **White** | 56.39% (90.02%) | 60.56% (65.2%) | Unknown |
| **non-White** | 43.61% (89.92%) | 39.44% (52.01%) | Unknown |
| **Age 0-20** | 0.8% (78.62%) | 0.75% (25.37%) | 2.42% (0.41%) |
| **Age 20-40** | 16.05% (79.56%) | 13.3% (36.66%) | 45.01% (5.71%) |
| **Age 40-60** | 31.07% (87.6%) | 15.2% (53.46%) | 6.98% (9.51%) |
| **Age 60-80** | 39.01% (93.0%) | 31.13% (67.24%) | 29.2% (23.92%) |
| **Age 80+** | 13.08% (96.3%) | 39.63% (76.65%) | 16.39% (32.13%) |

Table A3: The statistics of the subgroups and class labels. The numbers with percentages out of the brackets are the percentage of the appearing prevalence, and the numbers in the brackets are the percentage of being unhealthy (class label). Age group 0 and age group 1 range from 0-60 and 60+ except for the OCT dataset, whose age groups are from 55-75 and 75+.

|   | PAPILA | OCT | ADNI | ADNI3T |
| --- | --- | --- | --- | --- |
| **# Images** | 420 | 384 | 550 | 182 |
| **# Patients** | 210 | 269 | 417 | 80 |
| **Male** | 34.76% (23.97%) | Unknown | 52.55% (44.98%) | 34.62% (42.86%) |
| **Female** | 65.24% (18.98%) | Unknown | 47.45% (43.30%) | 65.38% (39.50%) |
| **Age Group 0** | 42.38% (8.43%) | 40.89% (52.23%) | 49.82% (44.16%) | 46.70% (45.36%) |
| **Age Group 1** | 57.62% (29.75%) | 59.11% (14.54%) | 50.18% (44.20%) | 53.30% (55.29%) |

#### B.1.2 DATA PREPROCESSING

Data splitting for experiments: unless otherwise specified, we randomly split the whole dataset into training/validation/testing sets with a proportion of 80/10/10 for 2D datasets and 70/10/20 for 3D datasets.

21

---

<!-- Page 22 -->

Published as a conference paper at ICLR 2023

Table A4: The statistics of the Fitzpatrick17k dataset.

| Skin Type | I | II | III | IV | V | VI |
| --- | --- | --- | --- | --- | --- | --- |
| % Images | 18.40% | 30.03% | 20.66% | 17.37% | 9.57% | 3.97% |
| % Malignant | 15.37% | 15.43% | 13.78% | 10.82% | 10.82% | 9.61% |

Table A5: The statistics of the subgroups and class labels. The numbers with percentages out of the brackets are the percentage of the appearing prevalence, and the numbers in the brackets are the percentage of being unhealthy (class label). Age group 0 and age group 1 range from 0-60 and 60+.

|   | COVID-CT-MD | OL3I |
| --- | --- | --- |
| # Images | 305 | 8139 |
| # Patients | 305 | 8139 |
| Male | 60.00% (59.02%) | 40.46% (5.53%) |
| Female | 40.00% (50.00%) | 59.54% (3.57%) |
| Age Group 0 | 73.11%(56.50%) | 67.91% (2.26%) |
| Age Group 1 | 26.89%(52.44%) | 32.09% (8.81%) |

CheXpert We first incorporate ethnicity labels (Gichoya et al., 2022) and the original data (Links in Table A6), dropping those images without sensitive attribute labels. The "No Finding" label is used for training and testing. We use all of the available frontal and lateral images, and images of the same patient do not share across train/validation/test split.

MIMIC-CXR The race data is available via MIMIC-IV (Johnson et al., 2020) dataset, which is also deposited in the PhysioNet database (Goldberger et al., 2000). We merge it to the original MIMIC-CXR metadata based on "subject ID". Other preprocessing steps are similar to that of CheXpert.

PAPILA We exclude the "suspect" label class and use images with labels of glaucomatous and non-glaucomatous for binary classification tasks. The dataset contains right-eye and left-eye images of the same patient. We split the train/validation/test in a proportion of 70/10/20, and images of the same patient do not share across the train/validation/test split.

HAM10000 We split 7 diagnostic labels into binary labels, i.e., benign and malignant following Maron et al. (2019). Benign contains basal cell carcinoma (bcc), benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df), melanocytic nevi (nv), and vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vaso). malignant contains Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec), and melanoma (mel). We discard images whose sensitive attributes are not recorded, resulting in 9948 images in total.

Fitzpatrick17k We split the three partition labels into binary labels i.e., benign and malignant. We treat "non-neoplastic" and "benign" as the benign label, and use "malignant" as the malignant label. Fitzpatrick skin type labels are used as sensitive attributes.

OL3I Opportunistic L3 computed tomography slices for Ischemic heart disease risk assessment (OL3I) dataset provides 8,139 axial computed tomography (CT) slices at the third lumbar vertebrae (L3) level of individuals. We design the task to predict whether the individual would be diagnosed with ischemic heart disease one year after the scan according to the labels provided (i.e. prognosis). Sex and age are treated as sensitive attributes.

22

---

<!-- Page 23 -->

Published as a conference paper at ICLR 2023

Table A6: Access to the datasets.

| Dataset | Access |
| --- | --- |
| CheXpert | Original data: https://stanfordmlgroup.github.io/competitions/chexpert/ Demographic data: https://stanfordai.m.azurewebsites.net/datasets/192ada7c-4dd3-466e-b8bb-8b1992b80cf |
| MIMIC-CXR | https://physionet.org/content/mimic-cxr-jpg/2.0.0/ |
| PAPILA | https://www.nature.com/articles/s41597-022-01388-1#sec6 |
| HAM10000 | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T |
| OCT | https://people.duke.edu/~sf59/REPEDC_Ophth_2013_dataset.htm |
| OL3i | https://stanfordai.m.azurewebsites.net/datasets/3263e34a-252e-460f-8f63-d585a9bfeccf |
| Fitzpatrick17k | https://github.com/mattgroh/fitzpatrick17k |
| COVID-CT-MD | https://doi.org/10.6084/m9.figshare.12991592 |
| ADNI-1.5T ADNI-3T | https://1da.loni.usc.edu/login.jsp?project=ADNI |

OCT The task is to predict if the patients have age-related macular degeneration (AMD). The dataset only contains people whose ages are over 55. Thus, we treat age as a binary attribute splitting from 75 years old, i.e., group-0: 55-75, group-1: 75+. Scans are resized to 224 × 224 × 100, and random cropping of the size of 192 × 192 × 96 is used for training.

COVID-CT-MD We design the task to predict whether the patients are infected by COVID-19, i.e., COVID-19 in one class, Community Acquired Pneumonia (CAP) and Normal in the other class. We resize each slice to a resolution of 256 × 256, and then take the central 80 slices for training, as the crucial signal associated with infection of COVID and CAP is often present in the middle slices (Chaudhary et al., 2021). Random cropping of size of 224 × 224 × 80 is used for training. We split train/validation/test in a proportion of 70/10/20.

ADNI-1.5T/ADNI-3T We design the task to predict if patients have Alzheimer’s disease (AD). MRI scans from ADNI have been preprocessed. We resize the height and width of scans of both 1.5T and 3T to the same size of 224 × 224 × 144 to reduce the variance for cross-domain testing. Random cropping of the size of 196 × 196 × 128 is used for training.

## B.2 TRAINING

### B.2.1 IMPLEMENTATION DETAILS

The experiments are conducted on a Scientific Linux release version 7.9 with one NVIDIA A100-SXM-80GB GPU. We trained over 7,000 models using ~ 0.77 GPU year. The implementation is based on Python 3.9 and PyTorch 1.10. We adapt the source code released by the original authors to our framework. We use ResNet-18 for 2D images and 3D ResNet-18 for 3D images as the backbone network for all experiments except otherwise specified.

For 2D datasets, we resize the images to the size of 256 × 256, and apply standard data augmentation strategies, i.e., random cropping to 224 × 224, random horizontal flipping, and random rotation of up to 15 degrees. The backbone network is initialized using ImageNet (Deng et al., 2009) pretrained weights and images are normalized with the ImageNet mean and standard deviation values. For 3D datasets, we resize 3D images according to the original imaging characteristics as described in B.1.2.

23

---

<!-- Page 24 -->

Published as a conference paper at ICLR 2023

The backbone network is initialized using kinetics (Carreira & Zisserman, 2017) pretrained weights and images are normalized with the kinetics mean and standard deviation values. Dataset-specific preprocessing and hyper-parameters can be found below.

### B.2.2 HYPER-PARAMETERS

To achieve the optimal performance of each algorithm for fair comparisons, we perform a Bayesian hyper-parameter optimization search for each algorithm and each combination of datasets and sensitive attributes using a machine learning platform Weights & Bias (Biewald, 2020). We use the batch size 1024 and 8 for 2D and 3D images respectively. SGD optimizer is used for all methods and we apply early stopping if the validation worst-case AUC does not improve for 5 epochs. The following hyper-parameter space is searched (20 runs for each method per dataset \times sensitive attribute), where |\cdot| means the value range, and \{\cdot\} means the discrete values:

ERM/Resampling/DomainInd Learning rate lr \in [1e-3, 1e-5].
LAFTR Learning rate lr \in [1e-3, 1e-4]. Adversarial coefficients \eta \in [0.01, 5].
CFair Learning rate lr \in [1e-3, 1e-4]. Adversarial coefficients \eta \in [0.01, 5].
LNL Learning rate lr \in [1e-3, 1e-4]. Adversarial coefficients \eta \in [0.01, 5].
EnD Learning rate lr \in [1e-3, 1e-4]. Entangling term coefficients \alpha \in [0.01, 5]. Disentangling term coefficients \beta \in [0.01, 5].
ODR Learning rate lr \in [1e-3, 1e-4]. Entropy Weight coefficients \lambda_E \in [0.01, 5]. Orthogonal-Disentangled loss coefficients \lambda_{OD} \in [0.01, 5]. KL divergence loss coefficients \gamma_{OD} \in [0.01, 5]. Entropy Gamma \gamma_E \in [0.1, 5].
GroupDRO Learning rate lr \in [1e-3, 1e-4]. Group adjustments \eta \in [0.01, 5]. Weight decay L_2 \in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5].
SWAD Learning rate lr \in [1e-3, 1e-4]. Starting epoch E_s \in \{3, 5, 7, 9\}. Tolerance epochs E_t \in \{3, 5, 7, 9\}. Tolerance ratio T_t \in [0.01, 0.3].
SAM Learning rate lr \in [1e-1, 1e-4]. Neighborhood size r_{hoo} \in [0.01, 5].

Empirically, we find the best learning rate for all methods is around 1e-4 except SAM, which requires a higher learning rate at around [1e-1, 1e-3] depending on the datasets.

### B.2.3 METHODS

We summarize the benchmarked methods in Table A7. We show their categories, whether they can accept multiple sensitive attributes for training, and whether they require the information of sensitive attributes for training and testing.

### B.3 METRICS

We explain the metrics used in this study in detail below:

AUC Area under the receiver operating characteristic curve (AUROC) is a standard metric to measure the performance of binary classification tasks, whose value is not affected by the imbalance of class labels. We use the name AUC in our text for simplicity. We measure the average AUC and the AUC of each subgroup. We pay particular attention to the AUC gap and the worst-case AUC to evaluate group fairness and max-min fairness.

ECE Expected calibration error (ECE) (Guo et al., 2017; Nixon et al., 2019) is an indicator of group sufficiency (Castelnovo et al., 2022). A high ECE value may result in a different optimal best decision threshold.

BCE Binary cross entropy (BCE) is the objective function we optimize for the classification task.

24

---

<!-- Page 25 -->

Published as a conference paper at ICLR 2023

Table A7: A list of methods used in the benchmark. SA is short for Sensitive Attributes. Y and N represent Yes and No, respectively.

| Method | Category | Multiple SA | SA for Training | SA for Testing |
| --- | --- | --- | --- | --- |
| ERM (Vapnik, 1999) | Baseline | Y | N | N |
| Resampling (Idrissi et al., 2020) | Subgroup Rebalancing | Y | Y | N |
| DomainInd (Wang et al., 2020) | Domain-Independence | Y | Y | N |
| LAFFR (Madras et al., 2018) | Adversarial | N | Y | N |
| CFair (Zhao et al., 2019) | Adversarial | N | Y | N |
| LNL (Kim et al., 2019) | Adversarial | Y | Y | N |
| EnD (Tartaglione et al., 2021) | Disentanglement | Y | Y | N |
| ODR (Sarhan et al., 2020) | Disentanglement | Y | Y | N |
| GroupDRO (Sagawa et al., 2019) | Domain Generalization | Y | Y | N |
| SWAD (Cha et al., 2021) | Domain Generalization | Y | N | N |
| SAM (Foret et al., 2020) | Domain Generalization | Y | N | N |

TPR, FPR, FNR, FNR Define true positive (TP) and true negative (TN) are values that are actually positive (negative) and correctly predicted positive (negative). Define false positive (FP) and false negative (FN) are values that are actually negative (positive) but wrongly predicted positive (negative). Then, we define true positive rate (TPR), true negative rate (TNR), false positive rate (FPR), and false negative rate (FNR) as

TPR = \frac{TP}{TP + FN} = 1 - FNR \quad (3)

TNR = \frac{TN}{TN + FP} = 1 - FPR. \quad (4)

We report the overall FPR, FNR, and following the value for each subgroup. The threshold is selected based on the minimum F1 score following (Seyyed-Kalantari et al., 2021). We also report the value of TPR at 80% TNR, which indicates the true positive rate of a given desirable true negative rate.

EqOdd Equalized Odds is a widely used group fairness metric that the true positive and false positive rates should be equalized across subgroups. Denote the input, label, and sensitive attribute as x, y, s, the prediction and the output probability as \hat{y}, p. Following (Reddy et al., 2021), we define Equality of Opportunity w.r.t. y as 1, i.e., \text{EqOpp}_0 and \text{EqOpp}_1, as

\text{EqOpp}_0 = 1 - |p(\hat{y} = 1|y = 0, s = \text{group-}0) - p(\hat{y} = 1|y = 0, s = \text{group-}1)|. \quad (5)

\text{EqOpp}_1 = 1 - |p(\hat{y} = 1|y = 1, s = \text{group-}0) - p(\hat{y} = 1|y = 1, s = \text{group-}1)|. \quad (6)

Then, we have \text{EqOdd} = 0.5 \times (\text{EqOpp}_0 + \text{EqOpp}_1).

#### B.4 MINIMAX PARETO SELECTION

Following (Martinez et al., 2020) and the dominance definition (Miettinen, 2008), we give a formal definition of the Pareto optimal regarding AUC.

Dominant vector A vector t' \in \mathbb{R}^k is said to dominate t \in \mathbb{R}^k if t'_i \geq t_i, \forall i = 1, \dots, k and \exists j : t'_j > t_j (namely strictly inequality on at least one component), denoted as t' > t.

25

---

<!-- Page 26 -->

Published as a conference paper at ICLR 2023

Dominant Classifier Given a set of group-specific metrics function T(h), i.e. AUC in our case, a model h' is said to dominate h'' if T(h') \succ T(h''), denote h' \succ h''. Likewise, a model h' \succeq h'' if T(h') \succeq T(h'').

Pareto Optimality Given a set of models H, and a set of group-specific metrics function T(h), a Pareto front model is P_{g,H} = \{h \in H : \nexists h' \in H | h' \succ h\} = \{h \in H : h \succeq h' \forall h' \in H\}. We call a model h a Pareto optimal solution iff h \in P_{g,H}.

Finally, a model h^* is a minimax Pareto fair classifier if it maximizes the worst-group AUC among all Pareto front models. For example, in Figure 2, each data point represents a different hyper-parameter combination for one algorithm, where the red points are models lying on the Pareto front. As we can see from the figure, the Pareto optimal points cannot improve the AUC of group 0 without hurting the AUC of group 1, and vice versa, indicating the best trade-off between different groups. The worst-case group is group 1, as the best AUC achieved for group 1 is lower than the best AUC achieved for group 0. In this case, we select the model that achieves the best AUC of group 1 (red star point) – the disadvantaged group, to make the selection as fair as possible.

26

---

<!-- Page 27 -->

Published as a conference paper at ICLR 2023

C ADDITIONAL RESULTS

Table A8 are the results of ERM under different model selection strategies behind Figure 4. Table A9 presents in-distribution results of the maximum and minimum AUC, and the gap between them for all datasets, as well as their average ranks. Table A10 presents out-of-distribution results. The highest maximum and minimum AUC values, and the smallest value of the performance gap are in bold.

We also report the BCE, ECE, TPR @80 NRN, FPR, FNR and EqOdd (for binary attributes) of each subgroup for a complete evaluation in the in-distribution setting in Table A11 to A13, and out-of-distribution setting in Table A14 and A15.

Table A8: Performance of different model selection strategies of ERM. The numbers separated by slashes are the mean values and ranks of overall AUC, the worst-case AUC, and the AUC gap, respectively. Mean values are reported.

| Dataset/Attr. | Overall Performance-based | DTIO | Minimax Pareto Optimal |
| --- | --- | --- | --- |
| ADNI 1-ST / Age | 91.83 / 87.53 / 4.70 | 91.55 / 91.37 / 1.43 | 91.20 / 92.38 / 1.04 |
| ADNI 1-ST / Sex | 82.77 / 76.97 / 18.72 | 81.57 / 75.33 / 22.73 | 81.36 / 78.52 / 24.90 |
| COVID-CT-MD / Age | 73.89 / 57.03 / 8.73 | 72.51 / 60.02 / 7.99 | 71.93 / 65.00 / 8.91 |
| COVID-CT-MD / Sex | 73.41 / 69.48 / 0.11 | 74.26 / 73.30 / 0.17 | 74.49 / 75.34 / 0.09 |
| CheXpert / Age | 80.59 / 78.01 / 10.80 | 89.62 / 77.92 / 10.92 | 88.09 / 78.36 / 10.33 |
| CheXpert / Sex | 89.01 / 88.12 / 0.13 | 88.43 / 88.01 / 0.08 | 88.90 / 88.70 / 0.02 |
| CheXpert / Race | 88.64 / 87.53 / 0.20 | 88.23 / 88.07 / 0.29 | 87.92 / 87.84 / 0.16 |
| Fitzpatrick17k / Skin Type | 90.38 / 91.37 / 3.72 | 90.01 / 90.02 / 4.05 | 91.51 / 90.67 / 3.70 |
| HAM10000 / Age | 84.13 / 84.07 / 3.52 | 85.74 / 84.21 / 3.39 | 85.20 / 83.12 / 3.31 |
| HAM10000 / Sex | 89.23 / 76.77 / 16.73 | 88.67 / 78.42 / 15.82 | 90.00 / 77.53 / 14.72 |
| MIMIC-CXR / Age | 86.31 / 80.64 / 6.19 | 85.98 / 81.97 / 5.78 | 86.40 / 81.06 / 5.32 |
| MIMIC-CXR / Race | 87.04 / 85.44 / 0.73 | 87.52 / 85.02 / 1.26 | 86.26 / 85.52 / 0.85 |
| MIMIC-CXR / Sex | 87.10 / 85.40 / 2.37 | 86.39 / 85.49 / 1.32 | 86.45 / 85.62 / 1.41 |
| OCT / Age | 98.37 / 98.25 / 0.74 | 97.88 / 91.24 / 5.88 | 95.92 / 91.44 / 7.31 |
| PAPILA / Age | 66.27 / 55.88 / 25.34 | 64.07 / 56.31 / 23.48 | 64.98 / 53.22 / 24.90 |
| PAPILA / Sex | 80.97 / 77.14 / 3.25 | 80.04 / 74.39 / 2.49 | 81.36 / 78.52 / 3.02 |
| OL31 / Sex | 74.25 / 67.41 / 9.27 | 74.01 / 68.55 / 9.13 | 73.87 / 68.93 / 8.57 |
| OL31 / Age | 69.13 / 57.94 / 9.27 | 67.99 / 58.22 / 8.93 | 66.58 / 58.43 / 8.48 |
| Avg. Rank | **1.56** / 2.53 / 2.29 | 2.19 / 1.93 / 2.05 | 2.29 / **1.49** / 1.65 |

27

---

<!-- Page 28 -->

Published as a conference paper at ICLR

Table A9: Results of the in-distribution evaluation.

| Dataset | Att. | Metrics | Resample | DomainIn | LATFR | Cfair | LNL | EOB | ORR | GroupRO | SVAD | SAM |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HAM1000 | Sex | Overall | 85.20 | 86.94 | 86.63 | 86.48 | 86.24 | 86.58 | 86.02 | 86.36 | 87.03 | 91.44 | 89.90 |
| HAM1000 | Sex | Min. | 82.12 | 85.04 | 84.93 | 86.00 | 85.56 | 86.03 | 84.96 | 85.54 | 85.52 | 91.14 | 89.35 |
| HAM1000 | Sex | Gap | 3.31 | 3.90 | 2.79 | 0.48 | 5.12 | 0.93 | 3.29 | 4.92 | 1.80 | 0.44 | 0.73 |
| HAM1000 | Sex | Overall | 90.00 | 90.10 | 89.03 | 89.26 | 89.06 | 88.78 | 89.22 | 89.23 | 89.23 | 90.61 | 90.23 |
| HAM1000 | Sex | Min. | 77.29 | 82.73 | 78.23 | 80.03 | 82.95 | 81.10 | 81.21 | 79.56 | 80.00 | 86.66 | 86.54 |
| HAM1000 | Age | Overall | 14.72 | 9.68 | 15.95 | 11.59 | 9.31 | 11.43 | 15.96 | 13.61 | 13.01 | 8.72 | 11.27 |
| HAM1000 | Age | Min. | 8.69 | 3.64 | 8.73 | 8.79 | 6.55 | 8.98 | 14.61 | 12.12 | 8.43 | 3.87 | 8.67 |
| HAM1000 | Age | Gap | 78.36 | 6.16 | 59.06 | 33.86 | 8.22 | 54.61 | 59.39 | 83.83 | 79.91 | 84.54 | 12.12 |
| HAM1000 | Age | Min. | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| HAM1000 | Age | Gap | 88.09 | 87.72 | 88.13 | 87.77 | 87.97 | 86.87 | 86.54 | 87.96 | 86.27 | 88.79 | 88.09 |
| Chon | Sex | Overall | 0.02 | 0.48 | 0.03 | 0.20 | 0.13 | 0.20 | 0.50 | 0.01 | 0.06 | 0.13 | 0.15 |
| Chon | Sex | Min. | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.02 | 0.02 |
| Chon | Sex | Gap | 0.02 | 0.47 | 0.03 | 0.20 | 0.13 | 0.20 | 0.50 | 0.01 | 0.06 | 0.13 | 0.15 |
| Chon | Sex | Overall | 87.92 | 87.76 | 88.01 | 88.01 | 87.77 | 86.65 | 84.84 | 88.12 | 86.30 | 88.75 | 87.75 |
| Chon | Sex | Min. | 47.84 | 47.84 | 47.84 | 47.84 | 47.73 | 46.77 | 46.77 | 48.39 | 46.05 | 48.65 | 47.64 |
| Chon | Age | Overall | 0.16 | 0.16 | 0.23 | 0.04 | 0.06 | 0.12 | 0.01 | 0.03 | 0.05 | 0.05 | 0.23 |
| Chon | Age | Min. | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Chon | Age | Gap | 0.16 | 0.16 | 0.23 | 0.04 | 0.06 | 0.12 | 0.01 | 0.03 | 0.05 | 0.05 | 0.23 |
| Chon | Age | Overall | 86.22 | 86.07 | 86.22 | 86.05 | 86.29 | 86.18 | 85.87 | 86.26 | 85.80 | 87.05 | 85.80 |
| Chon | Age | Min. | 81.06 | 79.07 | 79.87 | 81.13 | 81.05 | 66.60 | 73.18 | 70.78 | 78.62 | 82.15 | 77.97 |
| MDR-COR | Sex | Overall | 85.16 | 85.21 | 85.39 | 85.42 | 85.37 | 85.38 | 85.38 | 85.38 | 85.38 | 85.38 | 85.38 |
| MDR-COR | Sex | Min. | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 | 84.65 |
| MDR-COR | Sex | Gap | 0.51 | 3.01 | 3.21 | 2.56 | 0.53 | 0.73 | 0.39 | 1.07 | 0.26 | 3.64 | 0.71 |
| MDR-COR | Sex | Overall | 86.45 | 86.21 | 86.31 | 86.24 | 86.36 | 85.18 | 85.97 | 86.42 | 85.80 | 87.05 | 83.65 |
| MDR-COR | Sex | Min. | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 85.55 | 82.69 |
| MDR-COR | Race | Overall | 1.41 | 1.53 | 1.35 | 1.60 | 1.41 | 1.70 | 1.19 | 1.34 | 1.61 | 1.39 | 1.75 |
| MDR-COR | Race | Min. | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| MDR-COR | Race | Gap | 1.52 | 1.53 | 1.35 | 1.60 | 1.41 | 1.70 | 1.19 | 1.34 | 1.61 | 1.39 | 1.75 |
| MDR-COR | Race | Overall | 82.38 | 90.79 | 89.21 | 84.11 | 88.80 | 92.35 | 97.71 | 74.43 | 72.17 | 72.80 | 81.90 |

---

<!-- Page 29 -->

Published as a conference paper at ICLR 2023

Table A10: Results of the out-of-distribution evaluation. In the dataset column, the dataset in the first row is the training domain, and the second row is the testing domain.

| Dataset | Attr. | Metrics | ERM | Resample | DomainInfl | LAFTRE | CFair | LNL | EdD | OE | GroupPRO | SWAD | SAM |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUC-ROUGE-2 Subgroup | Age | Overall | 83.05 | 80.71 | 79.85 | 83.10 | 82.44 | 80.80 | 79.87 | 79.75 | 79.12 | **83.56** | 82.26 |   |
| AUC-ROUGE-2 Subgroup | Age | Min. | 76.50 | 75.09 | 72.43 | 76.06 | 76.11 | 74.83 | 74.05 | 74.28 | 74.35 | **76.66** | 75.01 |   |
| AUC-ROUGE-2 Subgroup | Age | Gap | 6.92 | 5.55 | 7.01 | 7.13 | 6.25 | 5.24 | 5.97 | **5.82** | 8.67 | 7.00 | 6.01 |   |
| AUC-ROUGE-2 Subgroup | Sex | Overall | 82.73 | 82.92 | 82.86 | 82.51 | 82.73 | 81.96 | 82.65 | 83.34 | 81.94 | **83.91** | 83.68 |   |
| AUC-ROUGE-2 Subgroup | Sex | Min. | 81.63 | 81.97 | 81.93 | 81.49 | 81.84 | 81.25 | 81.84 | 82.44 | 80.83 | **83.04** | 82.73 |   |
| AUC-ROUGE-2 Subgroup | Sex | Gap | 1.96 | 1.67 | 1.65 | 1.79 | 1.39 | **1.21** | 1.53 | 1.54 | 1.94 | 1.50 | 1.67 |   |
| AUC-ROUGE-2 Subgroup | Race | Overall | 82.50 | 82.39 | 83.30 | 82.63 | 81.08 | 81.46 | 82.33 | 82.91 | 81.72 | **83.50** | 83.25 |   |
| AUC-ROUGE-2 Subgroup | Race | Min. | 81.40 | 81.49 | 82.50 | 81.76 | 80.98 | 80.60 | 81.60 | 82.20 | 80.46 | **82.45** | 82.43 |   |
| AUC-ROUGE-2 Subgroup | Race | Gap | 1.28 | 0.90 | 0.70 | 0.76 | **0.43** | 0.69 | 0.50 | 0.50 | 1.63 | 1.02 | 0.73 |   |
| AUC-ROUGE-2 Subgroup | MILES-CAR Subgroup | Age | Overall | 85.87 | 84.10 | 86.06 | 85.17 | 84.60 | 84.71 | 85.68 | 85.15 | 85.10 | **86.80** | 85.67 |
| AUC-ROUGE-2 Subgroup | MILES-CAR Subgroup | Age | Min. | 78.84 | 77.29 | 78.70 | 76.89 | 76.84 | 77.58 | **79.27** | 77.77 | 76.19 | 80.18 | 77.97 |
| AUC-ROUGE-2 Subgroup | MILES-CAR Subgroup | Age | Gap | 5.57 | 7.68 | 8.40 | 10.64 | 9.65 | 8.00 | 7.05 | 9.40 | 10.18 | 9.22 | **6.68** |
| Sex | MILES-CAR Subgroup | Overall | 86.26 | 85.67 | 85.42 | 86.04 | 85.77 | 85.47 | 85.44 | 85.77 | 85.26 | **86.95** | 84.89 |   |
| Sex | MILES-CAR Subgroup | Min. | 85.72 | 85.34 | 85.09 | 85.56 | 85.40 | 85.16 | 84.96 | 85.25 | 84.51 | **86.56** | 84.29 |   |
| Sex | MILES-CAR Subgroup | Gap | 0.90 | 0.34 | 0.55 | 0.46 | **0.30** | 0.69 | 0.09 | 0.80 | 1.26 | 0.66 | 1.01 |   |
| Race | MILES-CAR Subgroup | Overall | 85.91 | 85.64 | **85.69** | 85.92 | 84.99 | 84.86 | 82.04 | 84.62 | 85.90 | **86.77** | 85.78 |   |
| Race | MILES-CAR Subgroup | Min. | 85.45 | 85.55 | 85.68 | 83.76 | 84.02 | 84.77 | 81.94 | 84.46 | 85.82 | **86.77** | 85.61 |   |
| Race | MILES-CAR Subgroup | Gap | 0.13 | 0.16 | **0.02** | 0.29 | 0.67 | 0.16 | 1.82 | 0.29 | 0.12 | 0.20 | 0.34 |   |
| AUC-IST Subgroup | MILES-CAR Subgroup | Age | Overall | **89.22** | 87.46 | 84.55 | 79.89 | 78.04 | 80.30 | 76.06 | 86.65 | 80.19 | 88.16 | 87.02 |
| AUC-IST Subgroup | MILES-CAR Subgroup | Age | Min. | **91.22** | 89.03 | 85.06 | 80.80 | 75.29 | 87.45 | 75.63 | 87.09 | 82.54 | 88.36 | 88.86 |
| AUC-IST Subgroup | MILES-CAR Subgroup | Age | Gap | **0.18** | 0.52 | 6.22 | 2.44 | 9.27 | 6.76 | 3.78 | 0.52 | 0.91 | 1.31 | 11.63 |
| AUC-IST Subgroup | Sex | Overall | 84.33 | 86.36 | 83.05 | 79.40 | 83.75 | 82.05 | 86.16 | **89.81** | 86.45 | 86.47 | 55.97 |   |
| AUC-IST Subgroup | Sex | Min. | 84.31 | 83.74 | 82.63 | 77.63 | 82.68 | 82.51 | 85.66 | **89.65** | 85.96 | 85.45 | 49.87 |   |
| AUC-IST Subgroup | Sex | Gap | 0.24 | 4.03 | **0.18** | 2.73 | 1.92 | 0.24 | 1.05 | 1.35 | 0.41 | 1.66 | 8.92 |   |
| AUC-IST Subgroup | Avg. Min. Rank | Avg. Min. Rank | 3.81 | 5.88 | 5.75 | 5.38 | 7.0 | 7.62 | 8.56 | 8.56 | 7.62 | **1.38** | 8.0 |   |
| AUC-IST Subgroup | Avg. Min. Rank | Avg. Min. Rank | 3.88 | 5.5 | 6.0 | 6.38 | 7.19 | 7.88 | 6.81 | 5.12 | 8.25 | **1.75** | 7.25 |   |
| AUC-IST Subgroup | Avg. Gap Rank | Avg. Gap Rank | 5.84 | 5.06 | 4.75 | 8.19 | 6.25 | **4.19** | 5.44 | 4.81 | 7.88 | 6.0 | 7.5 |   |

---

<!-- Page 30 -->

Published as a conference paper at ICLR 2023

Table A.1: Results of other metrics for HAM10000, CheXpert, and ADNI 1.5T dataset

| Dataset | Attr. | Group | ECG | Resnet | Unimodal | LoRA | Char | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO | LoO</ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

---

<!-- Page 31 -->

Published as a conference paper at ICLR 2023

Table A12: Results of other metrics for MIMIC-CXR, OCT, and Fitzpatrick17k dataset

| Dataset | Att. | Metrics | RCM | Ensemble | Domain-invariant | LAVER | CTar | LSI | ODR | ODR | GroupODR | SYNOD | SAM |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HICET | Age | CPU | 0.44800 | 0.47100 | 1.04800 | 0.43100 | 0.44200 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44265 |   |
| HICET | Age | GPU | 0.43000 | 0.44000 | 1.03000 | 0.43000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.442815 |   |
| HICET | Sex | CPU | 0.44800 | 0.44800 | 1.04800 | 0.43100 | 0.44200 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44265 |   |
| HICET | Sex | GPU | 0.43000 | 0.44000 | 1.03000 | 0.43000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.442815 |   |
| HICET | Race | CPU | 0.44800 | 0.44800 | 1.04800 | 0.43100 | 0.44200 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44265 |   |
| HICET | Race | GPU | 0.43000 | 0.44000 | 1.03000 | 0.43000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.442815 |   |
| HICET | ECG | CPU | 0.44800 | 0.44800 | 1.04800 | 0.43100 | 0.44200 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44400 | 0.44265 |   |
| HICET | ECG | GPU | 0.43000 | 0.44000 | 1.03000 | 0.43000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.44000 | 0.442815 |   |
| HICET | Age | TPPROM | CPU | 78.25421 | 71.0685 | 79.1577 | 77.9423 | 71.0487 | 78.0812 | 77.9823 | 77.9811 | 77.9811 | 77.9811 | 77.9811 |
| HICET | Age | TPPROM | GPU | 77.24824 | 72.14848 | 74.2201 | 73.5311 | 70.6411 | 47.9767 | 77.6233 | 77.6711 | 68.8311 | 77.7658 | 64.2431 |
| HICET | Age | PPR | CPU | 68.8311 | 65.9917 | 66.9917 | 66.1963 | 66.1963 | 66.1963 | 66.1963 | 66.1963 | 66.1963 | 66.1963 | 66.1963 |
| HICET | Age | PPR | GPU | 67.21847 | 71.0685 | 79.1577 | 77.9423 | 71.0487 | 78.0812 | 77.9823 | 77.9811 | 77.9811 | 77.9811 | 77.9811 |
| FPR | Age | CPU | 39.8311 | 42.0912 | 44.8849 | 42.1310 | 43.10 | 44.657 | 39.8672 | 38.1842 | 35.9487 | 39.9710 | 39.7810 |   |
| FPR | Age | GPU | 36.1545 | 45.8050 | 51.5457 | 45.8050 | 51.5457 | 45.8050 | 51.5457 | 45.8050 | 51.5457 | 45.8050 | 51.5457 |   |
| HICET-CXR | Age | Age | CPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | Age | Age | GPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | Age | Sex | CPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | Age | Sex | GPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | Age | Race | CPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | Age | Race | GPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |
| HICET-CXR | ECG | CPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |   |
| HICET-CXR | ECG | GPU | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 | 15.1811 |   |
| HICET-CXR | Sex | TPPROM | CPU | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 | 10.6100 |
| HICET-CXR | Sex | TPPROM | GPU | 10.6100 | 10.6100 | 10.610 |   |   |   |   |   |   |   |   |

---

<!-- Page 32 -->

Published as a conference paper at ICLR 2023

Table A13: Results of other metrics for COVID-CT-MD, PAPILA, and OLZI dataset.

| Dataset | Attr. | Metric | Group | KEM | Rescale | Denoised | LAUTRE | Chair | LSI | EAD | ROD | GroupROD | SWAD | SAM |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | Attr. | Metric | Group | KEM | Rescale | Denoised | LAUTRE | Chair | LSI | EAD | ROD | GroupROD | SWAD | SAM |   |
| COVID-19 | Age | BCE | Group | 0.756924 | 0.735088 | 1.156571 | 0.731865 | 0.728502 | 0.737088 | 0.695500 | 0.712600 | 0.686520 | 0.686520 | 0.686520 | 0.686520 |
| COVID-19 | Age | BCE | LSI | 0.735088 | 0.731865 | 1.156571 | 0.731865 | 0.728502 | 0.737088 | 0.695500 | 0.712600 | 0.686520 | 0.686520 | 0.686520 |   |
| COVID-19 | Age | TPP | Group | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 |
| COVID-19 | Age | TPP | LSI | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 |   |
| COVID-19 | Age | TPP | Group | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 |
| COVID-19 | Age | TPP | LSI | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 | 0.731865 |   |
| COVID-19 | Sex | BCE | Group | 0.915463 | 0.864863 | 0.864863 | 0.915463 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |
| COVID-19 | Sex | BCE | LSI | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |   |
| COVID-19 | Sex | TPP | Group | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |
| COVID-19 | Sex | TPP | LSI | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |   |
| COVID-19 | Sex | TPP | Group | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |
| COVID-19 | Sex | TPP | LSI | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |   |
| PAPILA | Age | BCE | Group | 0.801264 | 0.786030 | 0.786030 | 0.801264 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |
| PAPILA | Age | BCE | LSI | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |   |
| PAPILA | Age | TPP | Group | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |
| PAPILA | Age | TPP | LSI | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |   |
| PAPILA | Age | TPP | Group | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |
| PAPILA | Age | TPP | LSI | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 | 0.786030 |   |
| PAPILA | Sex | BCE | Group | 0.915463 | 0.864863 | 0.864863 | 0.915463 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |
| PAPILA | Sex | BCE | LSI | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |   |
| PAPILA | Sex | TPP | Group | 0.864863 | 0.864863 | 0.864863 | 0.864863 | 0.864863 |   |   |   |   |   |   |   |

---

<!-- Page 33 -->

Published as a conference paper at ICLR 2023

Table A14: Results of other metrics in out-of-distribution setting. In the dataset column, the dataset in the first row is the training domain, and the second row is the testing domain.

| Dataset | Att. | Metrics | Group | ECM | Resim | Domainal | LATRE | CM | LM | IOI | IOI | OGD | OGD+IOI | SNAD | SAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCE |   |   | Group 1 | 0.646(0.03) | 0.646(0.03) | 0.646(0.03) | 0.768(0.05) | 0.768(0.05) | 10.01(1.37) | 13.64(1.34) | 0.736(0.07) | 0.736(0.07) | 0.736(0.07) | 0.736(0.07) | 0.736(0.07) |
| BCE |   |   | Group 2 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 3 | 0.725(0.03) | 0.725(0.03) | 0.725(0.03) | 0.869(0.03) | 0.869(0.03) | 0.756(0.12) | 0.856(0.05) | 0.756(0.12) | 0.756(0.12) | 0.756(0.12) | 0.756(0.12) | 0.756(0.12) |
| BCE |   |   | Group 4 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 5 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 6 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 7 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 8 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 9 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| BCE |   |   | Group 10 | 0.736(0.03) | 0.736(0.03) | 0.736(0.03) | 0.834(0.04) | 0.834(0.04) | 0.767(0.17) | 0.846(0.08) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) | 0.758(0.09) |
| Agri |   |   | Group 1 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 2 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 3 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 4 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 5 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 6 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 7 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) | 0.7106(0.07) |
| Agri |   |   | Group 8 | 0.7346(0.03) | 0.6645(0.03) | 0.6533(0.04) | 0.7240(0.07) | 0.7240(0.07) | 0.642(0.08) | 0.7106(0.07) | 0.7 |   |   |   |   |

---

<!-- Page 34 -->

Published as a conference paper at ICLR 2023

Table A15: Results of other metrics in out-of-distribution setting. In the dataset column, the dataset is the first row in the training row, and the second row is the testing domain.

| Dataset | Att. | Model | Comp. | ERNA | Recongn. | Num-out | LASTR | CFat | LSN | Indf | GM | Compo | EMAD | SMR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Age | BCS | ICU | Comp. 9 | 0.668±0.39 | 0.728±0.39 | 1.226±0.51 | 1.058±0.57 | 0.660±0.66 | 0.646±0.26 | 0.635±0.01 | 0.630±0.14 | 0.614±0.22 | 0.514±0.12 | 0.726±0.02 |
| Age | BCS | ICU | Comp. 10 | 1.448±0.11 | 1.448±0.11 | 1.448±0.11 | 1.768±0.13 | 0.537±0.09 | 0.536±0.09 | 0.536±0.09 | 0.536±0.09 | 0.536±0.09 | 0.536±0.09 | 1.728±0.01 |
| Age | BCS | ICU | Comp. 11 | 0.218±0.08 | 0.246±0.07 | 0.226±0.05 | 0.268±0.05 | 0.186±0.05 | 0.214±0.06 | 0.225±0.10 | 0.225±0.08 | 0.236±0.01 | 0.166±0.03 | 0.176±0.02 |
| Age | TPP@90 | TSS | Comp. 9 | 88.845±0.7 | 79.881±0.72 | 12.164±0.6 | 56.480±1.0 | 0.796±0.03 | 7.898±1.17 | 0.588±0.02 | 0.779±0.03 | 0.588±0.02 | 0.763±0.03 | 25.142±0.11 |
| Age | TPP@90 | TSS | Comp. 10 | 82.896±0.6 | 82.21±0.7 | 80.73±0.6 | 88.752±1.0 | 0.146±0.02 | 9.214±0.02 | 0.080±0.01 | 0.146±0.02 | 0.080±0.01 | 0.146±0.02 | 25.142±0.11 |
| Age | TPP@90 | TSS | Comp. 11 | 16.650±0.6 | 14.94±0.7 | 13.794±0.3 | 17.823±0.3 | 0.376±0.03 | 11.483±0.2 | 0.988±0.04 | 0.739±0.03 | 0.988±0.04 | 0.739±0.03 | 11.483±0.2 |
| Age | PNR | TSS | Comp. 9 | 28.59±0.0 | 30.11±0.0 | 27.86±0.0 | 36.71±0.0 | 0.19±0.0 | 1.726±0.7 | 0.514±0.0 | 0.438±0.0 | 0.514±0.0 | 0.19±0.0 | 32.45±0.0 |
| Age | PNR | TSS | Comp. 10 | 28.59±0.0 | 30.11±0.0 | 27.86±0.0 | 36.71±0.0 | 0.19±0.0 | 1.726±0.7 | 0.514±0.0 | 0.438±0.0 | 0.514±0.0 | 0.19±0.0 | 32.45±0.0 |
| Age | PNR | TSS | Comp. 11 | 5.38±0.0 | 7.58±0.0 | 6.71±0.0 | 10.18±0.0 | 0.71±0.0 | 14.52±0.0 | 12.92±0.0 | 7.41±0.0 | 12.92±0.0 | 7.41±0.0 | 10.18±0.0 |
| Age | EqM | TSS | Comp. 9 | 88.12±0.7 | 87.74±0.7 | 76.71±0.6 | 77.03±0.3 | 0.376±0.03 | 82.26±0.3 | 84.14±0.7 | 0.739±0.03 | 0.774±0.03 | 0.739±0.03 | 82.44±0.7 |
| Age | EqM | TSS | Comp. 10 | 88.12±0.7 | 87.74±0.7 | 76.71±0.6 | 77.03±0.3 | 0.376±0.03 | 82.26±0.3 | 84.14±0.7 | 0.739±0.03 | 0.774±0.03 | 0.739±0.03 | 82.44±0.7 |
| Age | EqM | TSS | Comp. 11 | 0.628±0.04 | 0.536±0.04 | 0.846±0.28 | 0.768±0.29 | 0.593±0.22 | 0.666±0.06 | 0.593±0.01 | 1.146±0.38 | 0.524±0.01 | 0.568±0.15 | 0.714±0.04 |
| Sex | BCS | ICU | Comp. 9 | 1.628±0.14 | 1.598±0.14 | 1.688±0.48 | 0.768±0.26 | 0.666±0.26 | 0.666±0.26 | 0.564±0.01 | 1.166±0.2 | 0.526±0.01 | 0.598±0.06 | 0.716±0.04 |
| Sex | BCS | ICU | Comp. 10 | 1.628±0.14 | 1.598±0.14 | 1.688±0.48 | 0.768±0.26 | 0.666±0.26 | 0.666±0.26 | 0.564±0.01 | 1.166±0.2 | 0.526±0.01 | 0.598±0.06 | 0.716±0.04 |
| Sex | BCS | ICU | Comp. 11 | 0.214±0.03 | 0.224±0.03 | 0.274±0.03 | 0.274±0.03 | 0.134±0.03 | 0.214±0.03 | 0.114±0.02 | 0.236±0.07 | 0.194±0.01 | 0.166±0.01 | 0.214±0.03 |
| Sex | TPP@90 | TSS | Comp. 9 | 71.28±0.18 | 71.98±0.18 | 62.14±0.16 | 82.35±0.08 | 0.268±0.03 | 46.14±0.0 | 0.444±0.0 | 0.666±0.0 | 0.444±0.0 | 0.166±0.0 | 0.166±0.0 |
| Sex | TPP@90 | TSS | Comp. 10 | 71.28±0.18 | 71.98±0.18 | 62.14±0.16 | 82.35±0.08 | 0.268±0.03 | 46.14±0.0 | 0.444±0.0 | 0.666±0.0 | 0.444±0.0 | 0.166±0.0 | 0.166±0.0 |
| Sex | TPP@90 | TSS | Comp. 11 | 28.01±0.13 | 24.24±0.0 | 38.84±0.0 | 42.82±0.13 | 0.734±0.0 | 46.06±0.2 | 0.576±0.2 | 0.394±0.2 | 0.576±0.2 | 0.394±0.2 | 0.734±0.0 |
| Sex | PNR | TSS | Comp. 9 | 24.16±0.0 | 24.16±0.0 | 24.16±0.0 | 24.16±0.0 | 0.000±0.0 | 0.000±0.0 | 0.000±0.0 | 0.000±0.0 | 0.000±0.0 | 0.000±0.0 | 0.000±0.0 |
| Sex | PNR | TSS | Comp. 10 | 24.16±0.0 | 24.16±0.0 | 2 |   |   |   |   |   |   |   |   |

---

<!-- Page 35 -->

Published as a conference paper at ICLR 2023

## D INCORPORATE NEW DATASETS AND ALGORITHMS IN MEDFAIR

We implement MEDFAIR using the PyTorch framework. We show example pseudo codes to demonstrate how to incorporate new datasets and algorithms. Detailed documentation can be found at https://ys-zong.github.io/MEDFAIR/.

### D.1 ADDING NEW DATASETS

We implement a base dataset class BaseDataset, and a new dataset can be added by creating a new file and inheriting it.

from datasets.BaseDataset import BaseDataset
class DatasetX(BaseDataset):
    def __init__(self, metadata, path_to_images, sens_name, sens_classes,
                transform):
        super(DatasetX, self).__init__(metadata, sens_name, sens_classes,
                                      transform)

    def __getitem__(self, idx):
        item = self.metadata.iloc[idx]
        img = Image.open(path_to_images[idx])

        # apply image transform/augmentation
        img = self.transform(img)
        label = torch.FloatTensor([[int(item['binaryLabel'])]])

        # convert to sensitive attributes to numerical values
        sensitive = self.get_sensitive(self.sens_name, self.sens_classes,
                                    item)

        return img, label, sensitive, idx

### D.2 ADDING NEW ALGORITHM

We implement a base algorithm class BaseNet, which contains basic configuration and regular training/validation/testing loop. A new algorithm can be added by inheriting it and rewriting the training loop, loss, etc. if needed.

For example, SAM (Forêt et al., 2020) algorithm can be added by re-implementing the training loop.

class SAM(BaseNet):
    def __init__(self, opt):
        super(SAM, self).__init__(opt)
    def __train__(self, loader):
        self.network.train()
        for i, (images, targets, sensitive_attr, index) in
                enumerate(loader):
            enable_running_stats(self.network)
            outputs, features = self.network(images)
            loss = self.criterion(outputs, targets)
            loss.mean().backward()
            self.optimizer.first_step(zero_grad=True)
            self.scheduler.step()

            disable_running_stats(self.network)
            outputs, features = self.network(images)
            self._criterion(outputs, targets).mean().backward()
            self.optimizer.second_step(zero_grad=True)
            self.scheduler.step()

35

---

<!-- Page 36 -->

Published as a conference paper at ICLR 2023

E ANALYSIS OF SOURCE OF BIAS

We take two datasets HAM10000 and MIMIC-CXR as case studies to analyze the source of bias. As shown in Table A2, we can observe severe data and class imbalance as the direct sources of bias for both datasets. Thus, we utilize resampling strategies to explicitly mitigate the imbalance. We use three types of resampling to upsample the minority subgroup, class, or both subgroup and class so that all groups appear with equal chances during training, i.e. subgroup resampling, class resampling, and subgroup and class resampling, respectively.

For the HAM10000 dataset, we take the cartesian product of age and sex subgroups to construct 8 intersectional subgroups, whose statistics are shown in Table A16 (excluding age 0-20 as it has too few samples). The results of the ERM, resampling strategies, and the best-performing SWAD method are shown in Table A17. The worst-performing subgroup is “40-60 Male”, which neither contains the least number of images nor not the most class-imbalanced subgroup. Also, it can be seen that for intersectional subgroups, different resampling strategies produce a similar performance as the ERM and sometimes even worse, where all of them are worse than SWAD. In other words, there are other sources of bias beyond the observable data/class imbalance, which explains why resampling methods do not lead to better performance. For example, the skin type can be a potential source of bias (not recorded by metadata) as it is a dermatology dataset, and lesions on darker skin are intrinsically more difficult to diagnose than that on lighter skin. Overall, they are difficult or impossible to disentangle given the metadata as the sensitive attributes of different datasets can be correlated in different ways. Therefore, methods specifically optimizing for one particular factor are usually less effective.

Table A16: The statistics of the intersectional subgroup HAM10000 dataset. M. represents Male and F. represents female.

| Subgroup | 20-40 M. | 40-60 M. | 60-80 M. | 80+ M. | 20-40 F. | 40-60 F. | 60-80 F. | 80+ F. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| % Images | 7.27% | 9.52% | 23.09% | 23.05% | 18.97% | 10.96% | 5.16% | 1.99% |
| % Malignant | 4.53% | 6.60% | 10.93% | 8.09% | 25.75% | 20.77% | 31.14% | 34.72% |

Table A17: The performance of different methods on HAM10000 dataset.

| Attr. | Metric | ERM | Subgroup-R | Class-R | Subgroup, class-R | SWAD |
| --- | --- | --- | --- | --- | --- | --- |
| Sex | Overall | 87.24 | 88.03 | 87.89 | 88.76 | **91.46** |
| Sex | Min. | 86.48 | 86.23 | 87.42 | 88.11 | **91.14** |
| Sex | Gap | 1.59 | 4.43 | 1.13 | 1.28 | **0.54** |
| Age | Overall | **90.00** | 89.72 | 87.38 | 88.60 | 89.61 |
| Age | Min. | 77.53 | 82.73 | 79.41 | 85.02 | **86.66** |
| Age | Gap | 14.72 | 9.68 | 8.85 | 5.52 | **5.72** |
| Intersection | Overall | 88.13 | 88.03 | 88.78 | 87.75 | **89.32** |
| Intersection | Min. | 78.60 | 69.33 | 79.59 | 75.12 | **81.25** |
| Intersection | Gap | 17.23 | 24.02 | 17.29 | 18.43 | **15.02** |

Following a similar procedure, we further analyze the intersectional subgroup of MIMIC-CXR dataset, where we obtain 20 subgroups by taking the cartesian product of the age, sex, and race subgroups. As it can be seen from Table A18, the number of images and the value of labels (“No Finding”) vary greatly among different subgroups. The worst-performing subgroup is the “60-80 non-White Female”, which is imbalanced in data and class, but also does not contain the least number of images nor not the most class-imbalanced subgroup.

From the results of Table A18, we do observe a slight performance increase of the worst-case subgroup after resampling the minority subgroup, class, or both, while there are also decreases in the overall performance. A possible reason is that the label noises in some subgroups are more severe

36

---

<!-- Page 37 -->

Published as a conference paper at ICLR 2023

than the other subgroups as identified by Zhang et al. (2022), and the upsampled subgroups may contain more noisy labels to worsen the overall performance.

To summarize, most of the medical imaging datasets contain multiple sources of bias instead of only one, where they are correlated in different ways and it is difficult or impossible to fully disentangle for separate analyses. The mixture of multiple confounders makes the algorithms that specifically optimize for one particular factor (e.g. data imbalance) fail to succeed, i.e. do not outperform ERM. This, to some extent, explains why the domain generalization method SWAD is the most consistently high-ranked algorithm as it does not have a specific assumption of the source of bias. Increasing the general notion of robustness may be beneficial to various kinds of confounders.

Table A18: The statistics of the intersectional subgroup MIMIC-CXR dataset.

| Subgroup | % Images | % "No Finding" |
| --- | --- | --- |
| 0-20 non-White Female | 0.12% | 57.48% |
| 20-40 non-White Female | 0.22% | 72.18% |
| 40-60 non-White Female | 0.11% | 81.27% |
| 60-80 non-White Female | 0.3% | 80.72% |
| 80+ non-White Female | 2.50% | 50.69% |
| 0-20 White Female | 4.01% | 62.38% |
| 20-40 White Female | 2.58% | 59.98% |
| 40-60 White Female | 4.22% | 73.8% |
| 60-80 White Female | 10.18% | 40.51% |
| 80+ White Female | 6.75% | 47.58% |
| 0-20 non-White Male | 7.03% | 44.91% |
| 20-40 non-White Male | 7.17% | 55.74% |
| 40-60 non-White Male | 15.27% | 29.67% |
| 60-80 non-White Male | 6.12% | 34.17% |
| 80+ White Male | 11.35% | 32.43% |
| 0-20 White Male | 6.88% | 38.9% |
| 20-40 White Male | 5.41% | 22.04% |
| 40-60 White Male | 1.60% | 21.54% |
| 60-80 White Male | 6.03% | 23.64% |
| 80+ White Male | 2.17% | 27.14% |

Table A19: The performance of different methods on MIMIC-CXR dataset.

| Attr. | Metric | ERM | Subgroup-R | Class-R | Subgroup.class-R | SWAD |
| --- | --- | --- | --- | --- | --- | --- |
| Race | Overall | 86.26 | 86.07 | 86.20 | 86.33 | **87.10** |
| Race | Min. | 85.52 | 85.31 | 85.46 | 85.56 | **86.38** |
| Race | Gap | **0.85** | 0.88 | 0.86 | 0.95 | **0.88** |
| Sex | Overall | 86.45 | 86.21 | 86.37 | 86.24 | **87.05** |
| Sex | Min. | 85.62 | 85.31 | 85.45 | 85.39 | **86.23** |
| Sex | Gap | 1.41 | 1.53 | 1.60 | 1.46 | **1.39** |
| Age | Overall | 86.40 | 85.53 | 86.02 | 85.43 | **87.08** |
| Age | Min. | 81.06 | 70.97 | 74.69 | 73.24 | **82.15** |
| Age | Gap | 5.32 | 6.99 | 5.87 | 6.08 | **5.10** |
| Intersection | Overall | 86.26 | 85.06 | 86.25 | 85.37 | **86.35** |
| Intersection | Min. | 72.43 | 74.31 | 73.31 | 74.18 | **75.96** |
| Intersection | Gap | 18.92 | **11.59** | 16.06 | 15.45 | 14.78 |

37

---

<!-- Page 38 -->

Published as a conference paper at ICLR 2023

## F ACKNOWLEDGEMENT TO DATA RESOURCES

For the usage of ADNI dataset:

Data used in preparation of this article were obtained from the Alzheimer's Disease Neuroimaging Initiative (ADNI) database (adni.ioni.usc.edu). As such, the investigators within the ADNI contributed to the design and implementation of ADNI and/or provided data but did not participate in analysis or writing of this report. A complete listing of ADNI investigators can be found at: https://adni.ioni.usc.edu/wp-content/uploads/how_to_apply/ADNI_acknowledgement_List.pdf

The ADNI was launched in 2003 as a public-private partnership, led by Principal Investigator Michael W. Weiner, MD. The primary goal of ADNI has been to test whether serial magnetic resonance imaging (MRI), positron emission tomography (PET), other biological markers, and clinical and neuropsychological assessment can be combined to measure the progression of mild cognitive impairment (MCI) and early Alzheimer's disease (AD). For up-to-date information, see www.adni-info.org.

Data collection and sharing for this project was funded by the Alzheimer's Disease Neuroimaging Initiative (ADNI) (National Institutes of Health Grant U01 AG024904) and DOD ADNI (Department of Defense award number W81XWH-12-2-0012). ADNI is funded by the National Institute on Aging, the National Institute of Biomedical Imaging and Bioengineering, and through generous contributions from the following: AbbVie, Alzheimer's Association; Alzheimer's Drug Discovery Foundation; Aracelon Biotech; BioClinica, Inc.; Biogen; Bristol-Myers Squibb Company; CereSpir, Inc.; Cogstate; Eisai Inc.; Elan Pharmaceuticals, Inc.; Eli Lilly and Company; EuroImmune; F. Hoffmann-La Roche Ltd and its affiliated company Genentech, Inc.; Fujiirebio; GE Healthcare; IXICO Ltd; Janssen Alzheimer Immunotherapy Research & Development, LLC; Johnson & Johnson Pharmaceutical Research & Development LLC; Lumosity; Lundbeck; Merck & Co., Inc.; Meso Scale Diagnostics, LLC; NeuroRx Research; Neuronack Technologies; Novartis Pharmaceuticals Corporation; Pfizer Inc.; Piramal Imaging; Servier; Takeda Pharmaceutical Company; and Transition Therapeutics. The Canadian Institutes of Health Research is providing funds to support ADNI clinical sites in Canada. Private sector contributions are facilitated by the Foundation for the National Institutes of Health (www.fnih.org). The grantee organization is the Northern California Institute for Research and Education, and the study is coordinated by the Alzheimer's Therapeutic Research Institute at the University of Southern California. ADNI data are disseminated by the Laboratory for Neuro Imaging at the University of Southern California.

38