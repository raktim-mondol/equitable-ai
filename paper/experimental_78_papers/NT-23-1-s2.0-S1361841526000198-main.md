

<!-- PAGE 1 -->

Medical Image Analysis 109 (2020) 103950

ELSEVIER

Contents lists available at ScienceDirect

## Medical Image Analysis

journal homepage: 
[www.elsevier.com/locate/media](http://www.elsevier.com/locate/media)

## Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis

Gelei Xu
^a,*^
, Yuying Duan
^a^
, Jun Xia
^a^
, Ching-Hao Chiu
^a^
, Michael Lemmon
^b^
, Wei Jin
^a,†^
, Yipu Shi
^a,‡^

^a^
University of Notre Dame, Notre Dame, IN, 46556, USA
^b^
Yansey University, Atlanta, GA, 30322, USA

### ARTICLE INFO

**Keywords:**
Fairness
Skin disease
Group-specific model

### ABSTRACT

Recent efforts in medical image computing have focused on improving fairness by balancing it with accuracy within a single, unified model. However, this often creates a trade-off: gains for underrepresented groups can come at the expense of reduced accuracy for groups that were previously well-served. In high-stakes clinical contexts, even minor drops in accuracy can lead to serious consequences, making such trade-offs highly contentious. Rather than accepting this compromise, we refute the fairness objective in this paper as maximizing diagnostic accuracy for each patient group by leveraging additional computational resources to train group-specific models. To achieve this goal, we introduce SPARE, a novel data reweighting algorithm designed to optimize performance for a given group. SPARE evaluates the value of each training sample using two key feature utility, which reflects the sample's contribution to refining the model's decision boundary, and group similarity, which captures its relevance to the target group. By assigning greater weight to samples that score highly on both metrics, SPARE rebalances the training process partially leveraging the value of out-of-group data to improve group-specific accuracy while avoiding the traditional fairness-accuracy trade-off. Experiments on two skin disease datasets demonstrate that SPARE significantly improves group-specific performance while maintaining comparable fairness metrics, highlighting its promise as a more practical fairness paradigm for improving clinical reliability.

### 1. Introduction

Machine learning-based medical diagnosis systems have become increasingly prevalent. During the diagnosing process, these systems typically employ a “one-size-fits-all” approach, using models trained on data from diverse populations to maximize overall accuracy. However, due to substantial differences in disease prevalence and manifestations across patient groups, such generalized models typically achieve satisfactory performance only for well-represented populations, while underperforming for others. For instance, in dermatology, individuals with lighter skin have lower melanin levels (Caini et al., 2009), making them more susceptible to melanoma. Consequently, they are overrepresented in training datasets and are prioritized during the model's learning process, leading to better performance for lighter skin types compared to dark skin types. This discriminatory behavior can have serious societal consequences, including misdiagnoses or delayed treatments for certain groups, ultimately exacerbating existing healthcare disparities. To mitigate such biases, traditional fairness-aware algorithms (Ayyaswamy et al., 2020; Chiu et al., 2019; Zhang et al., 2022; Zong et al., 2025;

Mezrah et al., 2021; Payo-Antón et al., 2021) aim to reduce the accuracy gap between groups. This conventional approach, however, often improves accuracy for underrepresented groups at the expense of reducing performance for those originally well-served, embodying the well-known fairness-accuracy trade-off (Hodolin et al., 2021).

In clinical settings, where even minor losses in accuracy can lead to severe consequences (Chen et al., 2021), sacrificing precision for the sake of fairness is simply not an option. Unlike non-critical domains such as online search engines (Allmaras et al., 2023) or content recommendation systems (Jesse and Jannach, 2021) where slight degradation in performance may be acceptable, in healthcare they translate to missed or incorrect diagnoses that endanger patient safety. More critically, these reductions often occur near the decision boundary—precisely where clinical cases are most ambiguous and clinicians are most likely to make errors (Yuan et al., 2021). In such high-uncertainty scenarios, even a slight drop in accuracy can disproportionately increase the risk of misdiagnosis, amplifying clinical harm. At the same time, it is crucial to recognize that improving outcomes for underrepresented groups does not inherently require sacrificing performance for well-served ones.

* Corresponding authors.

† Email address: 
[weijin@nd.edu](mailto:weijin@nd.edu)
 (W. Jin).

‡ Email address: 
[ypshi@nd.edu](mailto:ypshi@nd.edu)
 (Y. Shi).

Received 19 May 2025; Received in revised form 8 November 2025; Accepted 14 January 2026
Available online 16 January 2026

1361-8415/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)
).

<!-- PAGE 2 -->

fairness algorithms are often framed as redistributing performance, but in practice, fairness groups in accuracy are neither necessary nor causally tied to gains for others. In fact, once improvements are achieved for disadvantaged groups, it is both feasible and desirable to retain their model output for the disadvantaged group as well. Therefore, we propose rethinking fairness in healthcare by shifting its definition from merely closing the gap between groups to achieving while keeping accuracy, it should be achieved by enabling each group to reach its maximum possible accuracy.

Central to our approach is a novel trade-off triangle involving fairness, group-specific accuracy, and computing resources. While every model-fairness group we consider is a priori privileged, they have largely confined their efforts to balancing group accuracy and fairness within a single model, implicitly assuming fixed computational resources and tolerable performance drops. In contrast, in this paper, we explicitly leverage additional computing power to train group-specific models, which are the traditional way of handling the trade-off. Our partitioned investment aims to maximize diagnostic precision for each group while remaining independently fair in the context of high-stakes applications. While many domains accept modest accuracy losses, in healthcare, group-specific accuracy is often the primary goal of groups justifying the investment in additional computational capacity.

This paper focuses on developing methods to maximize performance for each group and train dedicated models for each group. Our group-specific approach enables more precise modeling and leads to more group-specific accuracy gains. We propose a new training scheme to individual patient groups holds great promise, a central challenge is how to efficiently identify the most effective data for each group to get group. The most straightforward approach is to train exclusively on data from the target group, but this often leads to suboptimal performance due to data scarcity, the inability of the model to capture shared patterns. Conversely, leveraging the entire dataset may introduce suboptimal shifts that obscure the unique characteristics of the target group. This situation presents an inherent trade-off: while out-of-group data can enhance generalizability, it may simultaneously compromise the model’s ability to learn group-specific features. This trade-off is empirically shown in Section 2, and theoretically shown in Section 4.2.

Therefore, we propose incorporating a subset of out-of-group samples remains challenging without a reliable metric to assess each sample’s contribution. In addition, a data-driven approach for efficient integrating out-of-group data, optimizing model performance for each target group, and ensuring the highest possible diagnostic precision across all populations.

To address these challenges, we propose SPARE (Subgroup Performance Aware Re-weighting) algorithm. Our sample re-weighting framework aims to maximize subgroup performance by intelligently selecting and weighting individual samples. A core difficulty in this task lies in balancing two conflicting needs: identifying samples that contribute to improving the target group’s model while avoiding those that introduce harmful distribution shifts. Instead of handling these two objectives independently, SPARE provides an elegant, unified solution that optimizes utility and diagnostic precision through a shared perspective: the distance between a sample and its relevant decision boundaries. Specifically, samples closer to the boundary of the diagnosis are more informative, and samples further away, while we move near the boundary of the group label predictor better align with the target group’s performance. By integrating the distance into a scoring function, SPARE prioritizes samples that are both valuable and relevant to the target group, effectively maximizing both beneficial diagnostic data while mitigating the risks of distributional shift. This scoring-based approach enables principled integration of out-of-group data to optimize subgroup performance for each target group.

To validate the effectiveness of our approach, we focus on one of the most widely studied medical diagnostic tasks, skin disease diagnosis (Ansal et al., 2024; Chia et al., 2023). Experiments were conducted on two widely used dermatology datasets, where SPARE was evaluated against the current state-of-the-art fairness methods. These methods compare performance across groups by minimizing the gap between group-specific models or modalities. Experimental results show that, while most comparison methods achieve comparable performance, SPARE substantially improves performance for both groups. For instance, on the Fitzpatrick-174 dataset, SPARE achieves a 3.7% improvement for dark skin types and a 4.0% improvement for light skin types. On the Fitzpatrick-174 dataset, SPARE reduces the gap to the best existing methods. This outcome indicates that the process of training group-specific models under SPARE corrects performance gaps to underrepresented groups. A plausible explanation is that conventional training tends to allocate model capacity disproportionately toward privileged groups, where SPARE re-balances capacity during group-specific training. Overall, these results demonstrate SPARE’s ability to consistently improve performance for both groups, a more practical and effective solution for improving fairness in clinical medicine. We also provide a comprehensive analysis of the cost of implementing group-specific accuracy. SPARE contributes to a promising direction for advancing equitable medical AI systems.

The main contributions of this paper are as follows:

1. We present a practice-oriented view that frames fairness as maximizing performance within each subgroup. Guided by this view, we introduce a new subgroup-specific data selection scheme, wherein out-of-group data can improve generalizability but may dilute group-specific features.
2. We develop SPARE, a sample-wise reweighting method that quantifies each sample’s value through two factors: utility and similarity to balance generalizability and group-specific performance during the training process.
3. Empirical experiments results demonstrate that SPARE substantially improves performance across all subgroups, while matching or exceeding state-of-the-art methods on fairness metrics across multiple real-world datasets.

### Empirical analysis of group-specific training

In this section, we empirically demonstrate the importance of reweighting appropriate data samples to achieve optimal performance for specific demographic groups. We adopt the Fitzpatrick-174 dataset for our experiments. The Fitzpatrick-174 dataset contains 174 skin types that are grouped as light skin and T4 to six dark skin. The dataset contains 11,000 images of skin lesions, and is split into train/validation/test sets as 11,000/2,000/2,000. In our experiments, we use the same preprocessing and training settings as in Section 4.2, where we first experimentally demonstrate the importance of group-specific training. We then train and validate/test on a subset of 6,222, which we use for all subsequent experiments. In our experiments, we divide the data into several subsets based on Fitzpatrick skin types and evaluate the performance of different combinations of training samples on both light and dark skin test groups. The results are presented in Figure 1, where the x-axis denotes the specific combinations of training subsets, and the y-axis denotes the test accuracy of the model on the corresponding light and the dark skin group (darker line). From this figure, we observe the following:

1. For the light skin subgroup, performance does not peak when trained on the full dataset. Instead, using only the light skin training samples, achieving a 2.1% improvement over training on the full dataset, as confirmed by McBurney’s test on paired predictions (p < .05). This result indicates that training on the full dataset is not optimal for lower-performing groups in a single-model setting. Second, adding dark skin samples to the training set improves the performance of the proportion of dark skin samples increases further, the performance on light skin declines. While out-of-group data can enhance generalization,

<!-- PAGE 3 -->

Fig. 1. Left: Distribution of data volume across skin types in the Fitzpatrick-175 dataset. Right: Model performance trained with different skin types and evaluated exclusively on light skin data. Skin skin samples have enhanced skin skin accuracy; however, at the proportion of dark skin samples increases further, the performance on light skin declines.

It can also introduce distributional shifts that negatively impact performance. This highlights the importance of quantifying both the benefits and limitations of incorporating out-of-distribution data into an optimizer group-specific performance. Third, for the originally well-performed dark-skin type, training exclusively on dark-skin data yields lower accuracy than training exclusively on light-skin data. This explanation is that the light-skin subset is substantially larger in size, so the benefit of its greater data volume outweighs the distributional shift introduced, ultimately providing a more reliable signal for the dark-skin model.

These empirical findings highlight the need for data-driven approaches that optimize performance for individual subgroups. In particular, the results suggest that tailoring models to specific demographic groups may be especially beneficial for those that are originally under-represented in the training data. This may be attributed to the limited influence of underrepresented subgroups on the shared feature space in generalized models, which often fail to capture their specific characteristics. In contrast, subgroup-specific models can dedicate their full computational capacity to the target groups, resulting in improved performance, particularly for minority populations (Afroz et al., 2022).

### 3. Related works

#### 3.1. Fairness definitions in healthcare

Most fairness methods in healthcare focus on reducing disparities across demographic groups by minimizing differences in performance metrics such as true positive rates and false positive rates. This is commonly formalized through criteria like Equal Opportunity and Equalized Odds (Hardt et al., 2016), which aim to ensure similar outcomes across subgroups for different targets from the same ground truth.

Existing fairness approaches are commonly categorized into three groups: pre-processing, in-processing, and post-processing methods. Pre-processing techniques aim to achieve fairness by modifying the training data before model development. For example, Xu et al. (2018), Chen et al. (2020), Liu et al. (2020) and others specify data transformations to remove discriminatory patterns, while Kamiran and Calders (2012) assigns varying weights to individual samples to suppress the influence of sensitive attributes. In-processing methods intervene during model training to balance multiple objectives, typically aiming to jointly optimize for accuracy and fairness. A widely adopted approach in this category is adversarial training, where an auxiliary adversary network is trained to predict sensitive attributes from learned representations, while the main model is trained to minimize the adversary’s success, thereby reducing the encoding of sensitive information (Jia et al., 2018; Zhang et al., 2018; Wang et al., 2022). Another line of work focuses on regularization-based methods, which penalize correlations between sensitive attributes and the model’s output to encourage fairness (Jung et al., 2021; Quadratino et al., 2019). For instance, Gresley et al. (2018) learns fair representations by minimizing the fair information from a teacher model into a student model using the Maximum Mean Discrepancy loss. More recently, techniques such as pruning and quantization have been explored to reduce bias by removing model components that disproportionately contribute to disparities across sensitive groups (Choi et al., 2020; Han et al., 2020). Post-processing methods operate after the model has been trained, adjusting its outputs to enhance fairness. A typical approach involves threshold adjustment, where different prediction thresholds are applied to different subgroups to satisfy fairness criteria (Hardt et al., 2016; Valera et al., 2018). In addition, Afroz et al. (2022) proposes a subgroup-specific training approach that distributes training data based on the subgroup’s performance, using both the number of raw predictions and subgroup-specific attribute information as inputs.

These fairness-aware methods inherently face limitations at the Pareto frontier, where it becomes infeasible to simultaneously improve the performance of all groups (Valera et al., 2020). Consequently, such methods often leave at least one group in a suboptimal state. More concerning, fairness constraints can lead to performance degradation across all groups in some cases, undermining the overall utility of the model (Wu et al., 2022; Duan et al., 2022). A notable example lies in the common practice of suppressing sensitive attributes during training. While this strategy may appear effective in improving fairness metrics, it neglects the critical role of such attributes in clinical decision-making. Attributes like skin type, race, and gender are not merely confounders but often inform diagnosis. For instance, skin type provides crucial information for assessing UV susceptibility (Goini et al., 2009; Narayanan et al., 2010), and disease prevalence varies by race and gender (Omayez et al., 2019; Gonsior et al., 2013). In high-stakes clinical environments, compromising diagnostic accuracy for fairness can often be impractical and potentially hazardous. Therefore, fairness and accuracy should be treated not as trade-offs but as complementary goals to ensure reliable and effective medical care.

#### 3.2. Fairness through subgroup performance maximization

Beyond gap-reduction approaches, several studies have pursued fairness by directly maximizing performance within each subgroup. In medical imaging, Peng and Gao (2021) propose a subgroup-specific training approach that optimizes the model’s performance on each subgroup by maximizing the model’s performance on each subgroup. More recently, Zhang et al. (2023) introduced Stratified ERM for clear X-rays, which partitions data by subgroup and learns distinct empirical risk minimizers, while the MEDAIR benchmark (Zong et al., 2022) formalized a similar objective using a weighted sum of subgroup-specific losses for multi-view imaging modalities. These approaches share a common goal of enhancing subgroup-specific accuracy rather than minimizing disparities across groups.

Similar ideas appear outside the medical imaging domain, where fairness has been more broadly conceptualized in terms of subgroup-specific performance. For instance, Wang et al. (2020) propose group-specific classifiers that learn distinct parameters for each subgroup for each subgroup, while Doweth et al. (2018) design a decoupled classification framework where distinct classifiers are trained for different groups. In addition, Mehrahi et al. (2021) provide a comprehensive review of fairness methods, explicitly highlighting strategies that

<!-- PAGE 4 -->

ethically implementing subgroup-level performance. Collectively, these methods provide perspectives that have not yet been considered, but with reducing inter-group disparities, but can instead be framed as ensuring that each subgroup reaches its maximum achievable accuracy.

Beyond fairness-specific literature, adjacent paradigms also resonate with this perspective. Multi-task learning (Eigenschaft and Pontil, 2004; Arjov and Arjov, 2004) and personalized learning (Liu and Zhang, 2022; Tan et al., 2022) both aim to balance knowledge transfer across groups. However, with the need for subgroup-specific performance. While these methods are not explicitly designed for fairness, their principle of combining global generalization with local specialization aligns well with our objective of maximizing subgroup performance.

While prior approaches also aim to achieve fairness without considering accuracy by improving subgroup-specific performance, they typically regard each group as an isolated entity and train models using only its group data. In contrast, our method extends this line of work by explicitly leveraging out-of-group data to boost the performance of under-performing subgroups, such data can further enhance subgroup performance. This insight has been leveraged in several recent works to improve subgroup-specific methods as baselines for comparison. It is also worth noting that subgroup-optimizing subgroup performance does not necessarily guarantee improvements in traditional gap-based fairness metrics discussed in Section 3.1, in practice we often observe such metrics improve in a by-product, likely because subgroup-optimizing groups tend to achieve larger relative gains when subgroup-specific performance is maximized.

### 3.3. Bridging fairness, domain shift and out-of-distribution generalization

A central cause of fairness issues in machine learning is the uneven distribution of data across demographic groups. When certain groups are underrepresented or exhibit unique feature-label relationships, models trained on aggregate data often generalize poorly to these groups. This performance gap is closely related to challenges studied in out-of-distribution (OOD) generalization and domain adaptation, where models fail under distribution shifts between training and deployment conditions (Quelleno-Candela et al., 2022; Sun and Szezello, 2016).

In OOD generalization, the goal is to learn representations that can robustly cross diverse domains, minimizing reliance on spurious correlations introduced by domain shifts (Srivastava and Ungar, 2019). To address this, researchers have proposed techniques such as minimizing worst-case loss (Sagawa et al., 2019), pruning based samples (Chen et al., 2024), and adversarial representation learning (Jozefowicz et al., 2019). These strategies are conceptually aligned with fairness, as both aim to reduce the impact of disparities between groups on group-invariant features. However, such approaches often discard group-specific characteristics, limiting their ability to achieve optimal performance within each individual distribution.

In contrast, domain adaptation focuses not on learning shared features across all domains, but on improving performance in a particular domain by transferring knowledge from related distributions (Ganin et al., 2016). Domain-adversarial training (Ganin et al., 2016), domain-invariant representation learning (Torres et al., 2019), and weighted empirical risk minimization (Zhang et al., 2018; Bai et al., 2022) are three methods that are aligned with our goal of group-specific optimization, where the objective is to improve performance in a specific subgroup. However, approach departs from traditional domain adaptation in two key ways. First, we are not training each subgroup-specific model, but instead use cross-group samples as a finer, sample-wise granularity to assess their utility for improving target group performance. Second, we introduce principled mechanisms to ensure that both utility and distribution similarity when selecting which out-of-group samples to incorporate. This allows us to balance the benefits of domain borrowing and adaptively leverage the most beneficial examples, regardless of origin.

Recent studies have begun exploring fairness generalization across domains and groups, but these efforts have primarily focused in a source environment when deploying a model under distribution shifts in a new target environment. For example, Plam et al. (2023) seek to improve both fairness and accuracy in downstream tasks using a model while Liang et al. (2023) and Sun and Fontana (2024) investigate domain adaptation techniques that improve fairness in downstream classification. While such work on fairness robustness is valuable, our work focuses on a much more challenging scenario, where we are thus seeking to preserve fairness only after an external domain shift, we use the theoretical tools of domain adaptation to address the imbalance between groups, and we do not assume that a model’s “domain” need not be limited to environmental changes encountered after deployment; instead, each demographic group can be framed as its own domain. This reframing allows fairness to be pursued through a domain-aware perspective. To the best of our knowledge, we present the first method that explicitly addresses this challenging framework that links fairness considerations with data-driven strategies for optimizing performance across subgroups.

### 4. Methodology

#### 4.1. Problem formulation

Consider a dataset 
D = \{(x_i, y_i)_{i=1}^n\}
, where 
x_i \in \mathcal{X}
 represents an input sample, and each sample 
x_i
 is associated with a label 
y_i \in \mathcal{Y}
. Here, 
x_i \in \mathcal{X} \subset \mathbb{R}^d
, 
\mathcal{Y} = \{1, \dots, K\}
 denotes the class label, while 
\mathcal{X} \subset \mathbb{R}^d
 (0 ≤ d ≤ 1) represents a binary group label (e.g., gender, race). In this paper we focus on binary group labels for clarity, though our approach extends easily to multiple groups with minor modifications. We partition the dataset into two subsets, 
D_1
 and 
D_2
, corresponding to groups 0 and 1, respectively. Our approach builds upon a basic ensemble model that dynamically selects the group-specific classifier corresponding to the most resemble consists of two group-specific models, 
f_0: \mathcal{X} \to \mathcal{Y}
 and 
f_1: \mathcal{X} \to \mathcal{Y}
, trained exclusively on 
D_0
 and 
D_1
, respectively. Additionally, a group label predictor 
f_g: \mathcal{X} \to \{0, 1\}
 is designed, which predicts the group to which a sample belongs.

Our goal is to optimize the group-specific models 
f_0
 and 
f_1
, such that 
f_0
 maximizes accuracy on 
D_0
, and 
f_1
 maximizes accuracy on 
D_1
. To achieve this, we introduce a weighting scheme that assigns higher weights to samples that are more similar to the target group. Without loss of generality, the following method description focuses on maximizing the performance of Group 0. That is, we treat Group0’s dataset (
D_0
) as the primary set and Group 1’s dataset (
D_1
) as the auxiliary set, selecting relevant samples from 
D_1
 to enhance 
f_0
. The process is summarized in Algorithm 1. We use 
\mathcal{F}_0
 to denote the set of samples 
f_0
 selects, to emphasize its role as the classifier for Group 0. A direct approach to improving 
f_0
 is to train it on 
D_0
 alone, but that improves its performance on 
D_0
 only, which incorporated. However, this selection process is NP-hard and inherently imposes a binary classification of sample importance, which limits its ability to capture the full spectrum of sample usefulness. Our approach addresses this by selecting samples that are most similar to 
D_0
, and thus can be incorporated into 
D_0
 to improve 
f_0
. This is achieved by using a weighted empirical risk minimization (WERM) framework, where the objective is to minimize the weighted empirical risk over the entire dataset, with weights determined by the similarity between each sample and the target group. The weights are calculated using a similarity metric, such as the cosine similarity between the feature vector of the sample and the mean feature vector of the target group. The similarity metric is defined as:

w_i = \frac{1}{1 + \exp(-\alpha \cdot \text{sim}(x_i, \mu_0))}

where 
\alpha
 is a hyperparameter that controls the sensitivity of the similarity metric, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of the target group. The similarity metric is defined as:

\text{sim}(x_i, \mu_0) = \frac{x_i \cdot \mu_0}{\|x_i\| \cdot \|\mu_0\|}

where 
x_i
 is the feature vector of the sample, and 
\mu_0
 is the mean feature vector of

<!-- PAGE 5 -->

Figure 2 illustrates the Illustration of the distances from a sample to the decision boundaries of the diagnosis classifier and the group predictor. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
.

Figure 3 illustrates the Empirical Sample Size. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The empirical sample size is defined as the number of samples in the same group as the sample, within a certain distance threshold.

Figure 4 illustrates the Quantifying utility and similarity. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The utility and similarity are defined based on the distances and the group membership of the sample.

Figure 5 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 6 illustrates the Quantifying utility and similarity. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The utility and similarity are defined based on the distances and the group membership of the sample.

Figure 7 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 8 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 9 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 10 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 11 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 12 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 13 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 14 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 15 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 16 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 17 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 18 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 19 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance to Group 0 boundary), and 
d_1^-
 (negative distance to Group 1 boundary). The sample is classified as Group 0 if 
d_0 < d_1
, and Group 1 if 
d_1 < d_0
. The distance to decision boundaries is used as a proxy for the utility and similarity of the sample.

Figure 20 illustrates the Distance to decision boundaries as a proxy. The diagram shows a feature space with axes labeled Group 0 and Group 1. A sample point is shown, along with its projection onto the boundary line. The distances are labeled: 
d_0
 (distance to Group 0 boundary), 
d_1
 (distance to Group 1 boundary), 
d_0^+
 (positive distance to Group 0 boundary), 
d_1^+
 (positive distance to Group 1 boundary), 
d_0^-
 (negative distance

<!-- PAGE 6 -->

Fig. 3. The distance between a sample and a model’s decision boundary is estimated using adversarial perturbations. For the group predictor, the minimal perturbation required to alter the prediction for group 0 is computed. For the diagnosis classifier, the predicted class 
y
 is first identified, and the smallest perturbation needed to change the output to any 
y'
 is then computed.

**Algorithm 1 Training algorithm for FAPR.**

**Input:**
 Full dataset 
D = \{x_i, y_i\}
, diagnosis model 
f_i
, group model 
f_g
, Output: Optimized group-specific model 
f_i^*

1. Phase 1: Compute sample weights
2. for each samplex \in DdoCompute\delta_x^iusingf_iandf_gusing Eq. (3)Compute\delta(x) = \alpha \delta_x^i + (1-\alpha) \delta_x^{i-1}Setw_x = e^{-\delta(x)}
3. Compute\delta_x^iusingf_iandf_gusing Eq. (3)
4. Compute\delta(x) = \alpha \delta_x^i + (1-\alpha) \delta_x^{i-1}
5. Setw_x = e^{-\delta(x)}
6. Phase 2: Train group-specific model
7. Trainf_i^*on using fixed weights\{w_x\}
8. returnf_i^*

controls the balance between minimizing perturbation size and maximizing prediction change. We solve this optimization using an iterative gradient-based approach that refines 
\delta_x^i
 progressively minimizing the objective until a classification flip is achieved.

#### 4.3.2. Final weighting function

The resulting perturbation norm 
\|\delta_x^i\|
 serves as the distance metric for 
x
 and 
\delta_x^i
. These distances are then combined by Eq. (2) to determine the weight assigned to 
x
, ensuring that STARE prioritizes inputs that are both close to decision boundaries and distributionally aligned with 
D_i
. Since the distribution of the calculated 
\delta(x)
 is highly skewed, we ultimately use 
w_x = e^{-\delta(x)}
 to map 
\delta(x)
 inversely to a range between 0 and 1 to obtain the final weight of an image 
x
. Algorithm 1 shows the training procedure for obtaining the group-specific model for Group 0.

#### 5. Experiments and results

To evaluate the effectiveness of the proposed method, we conduct comprehensive experiments designed to answer the following research questions (RQs):

- **RQ1:**General performance comparison. How does the proposed method perform compared to state-of-the-art bias mitigation approaches across different backbone architectures?
- **RQ2:**Weight distribution analysis. How do the weight distributions differ across demographic groups in group-specific models trained using our method?
- **RQ3:**Impact of weighting strategies. Our method assigns individual sample weights, subsequently normalized to the range [0, 1] via an exponential mapping. To what extent do alternative weighting strategies influence model performance?
- **RQ4:**Utility vs. similarity comparison. How does the hyperparameter\alpha, which balances utility and similarity in the weighting function, affect overall performance?
- **RQ5:**Ablation study of the combined distance. How do the utility and similarity components, individually and in alternative formulations, contribute to the overall effectiveness of the proposed combined distance?
- **RQ6:**Resource-performance trade-off. In scenarios with limited computational resources, where training separate models per group is infeasible, how does the use of partially shared models impact performance?

#### 5.1. Datasets, training protocol and metrics

**Dataset and Training Details.**
 The proposed methods are evaluated on two skin disease classification datasets: the Fitzpatrick17K dataset (Groth et al., 2021) and the ISIC 2019 challenge dataset (Combalia et al., 2019; Teichardt et al., 2019). The Fitzpatrick17K dataset comprises 16,577 images representing 114 different skin conditions. We group skin types 1–3 as light skin and 4–6 as dark skin, following the same settings as in Section 2. ISIC 2019 dataset contains 223,331 images across 8 categories. While gender is frequently selected as the sensitive attribute in fairness-aware learning, we instead choose age due to its quasi-continuous nature, which facilitates finer subgroup partitioning and enables more nuanced downstream visualization. Accordingly, we divided the dataset into young and old groups for analysis. A standard preprocessing step for both datasets involves resizing all the images to a uniform size of 128×128 pixels. Various techniques such as random horizontal flipping, vertical flipping, rotation, scaling, and augmentation are used to augment the data, consistent with (Cohen et al., 2018). The dataset is split into train, validation, and test with a ratio of 6:2:2. Unless otherwise specified, we use ResNet-18 (He et al., 2016)

<!-- PAGE 7 -->

as the backbone. All models are trained for 200 epochs using the SGD optimizer with a fixed batch size of 128 to ensure consistency of the methods. For the learning rate, we performed a small validation-based search over {10
^-5^
, 10
^-4^
, 10
^-3^
} and selected 10
^-4^
, which yielded the best performance. The setting was applied uniformly to both SPARE and all baselines. For the proposed SPARE method, the trade-off parameter 
\alpha
 in Eq. (2) is analyzed in detail in Section 5.2.4, with 
\alpha = 0.5
 used by default unless otherwise specified. The adversarial perturbation balance factor 
\beta
 is set to 100 following the setting in [20]. For each group, we repeat this process three times and report the average to ensure consistency of the results. Since SPARE is designed to train separate models for each group, we report the average performance of the group-specific corresponding group-specific model in the results.

**Metrics.**
 Since the fairness objective of this paper is to improve diagnostic performance for every specific group, we adopt commonly used classification metrics-precision, recall, and F1-score as the main criteria and report group-wise and group-average performance effects. While our proposed approach does not explicitly minimize inter-group disparities, we also report fairness metrics that provide wider insights into fairness metrics to enable comprehensive comparisons with prior state-of-the-art methods. Specifically, we report the group-wise and group-wise versions of Equalized Opportunity (EqOp) and Equalized Odds (EqOd), following the definitions and implementations in Yu et al. (2022). In addition, we report the trade-off between the two fairness objectives, which we also report the Fairness-Aware Trade-Off Evaluation (FATE) metric introduced in Yu et al. (2022). The FATE metric is defined as the favorable balance between accuracy and fairness, and the FATE metric is computed as:

FATE(E_{\theta, \phi}) = \frac{ACC_{\theta, \phi} - ACC_{\theta, \phi}^*}{ACC_{\theta, \phi} + ACC_{\theta, \phi}^*} \quad (5)

Here, 
ACC_{\theta, \phi}
 denotes the model's predictive performance, for which we use F1-score, and 
PC
 refers to the fairness criterion (e.g., EqOp or EqOd). These metrics are all computed on the test set and reported in the results, respectively. The hyperparameter 
\alpha
 controls the relative weight of the fairness objective and accuracy objective, and we set 
\alpha = 1
 in all experiments.

### 5.2. Result and discussions

#### 5.2.1. RQ1: Performance comparison with state-of-the-art

We compare SPARE with various baseline algorithms on the ResNet-18 backbone. Vanilla refers to models trained directly on ResNet-18 without any fairness constraints. FairDecision [19] is a fairness-aware optimization-sensitive attributes (Xu et al., 2023). For this method, we followed the grid search range reported in the original paper (0.1, 0.2, 0.3) for its fairness-aware parameter 
\alpha
 and used 
\alpha = 1.0
. SC FairPrune (Kong et al., 2024) and FairQuantize (Guo et al., 2024) enhance fairness through pruning and quantization, respectively. Since our dataset and backbone settings match those used in their papers, we directly adopted the reported hyperparameters for SC FairPrune: 
pre = 2\%
 and 
\alpha = 1
; for FairQuantize, we used a quantization ratio of 80% with 
\beta = 0.75
 on ISIC2019, and a ratio of 20% with 
\beta = 1.0
 on Fitzpatrick. We also evaluated fairness metrics based on group-specific training. GroupModel (Fuyol-Astúa et al., 2023) trains a separate model for every group using only data from that group. DeepOod (Wang et al., 2020) learns group-specific classifiers with shared parameters. In addition, we also report the results of the originally designed for broader group/domain adaptation but conceptually aligned with subgroup performance maximization. Regularized Multi-Task Learning (MTL) (Ruder and Pontil, 2009) encourages related groups to share information through joint parameterization while still allowing group-specific performance, making it a natural baseline in our setting. ADE (Liu and Wu, 2022) learns group-specific Directed Relationship (DR) weights that determine how much each subgroup borrows from others, which parallels our goal of leveraging out-of-group samples to improve generalization.

**Results on ISIC 2019 dataset.**
 Table 1 reports the results on the ISIC 2019 dataset, demonstrating that SPARE consistently outperforms all baselines in accuracy and fairness metrics for all groups. For instance, compared to the ResNet-18 backbone, SPARE achieves a 3.7% improvement in accuracy for the Black group and a 5.8% improvement for the old group. Such gains are particularly valuable in high-stakes medical settings, where even small improvements can lead to the detection of well-served groups or falling to capture the group-specific characteristics of underrepresented populations. By training group-specific models, SPARE addresses the limitations of group-agnostic models and improves representation across demographic groups.

Meanwhile, SPARE also demonstrates strong performance on fairness metrics. It ranks first in both EqOp and EqOd, and second in EqP1 compared to the baseline. SPARE reduces EqOp by 10.7% and EqOd by 26.5% for the old group by 30.5%. This means that, without explicitly incorporating bias mitigation constraints, SPARE effectively reduces disparities between groups, given that it is trained using the group-specific approaches (GroupModel, DomainAdapt, MTL, ADE, and EqOp). In addition, SPARE achieves the highest F1-score for the younger subgroup compared to non-group-specific baselines FairADan, SC FairPrune, and FairQuantize. For example, group-specific models achieve the younger subgroup F1-score of 86.1% compared to 84.0% to 0.780 (SPARE) and 0.752 (DomainAdapt), whereas non-group-specific methods such as EqOp, EqP1, EqP2, EqP3, EqP4, EqP5, and EqP6 show the younger subgroup and even lower its performance. This may be due to the fact that the younger subgroup is more likely to be underrepresented in overrepresented groups, thereby suppressing the learning of group-varying features associated with minority groups. In contrast, group-specific models enable better representation of each group's unique features, with underrepresented groups benefiting more substantially from this tailored optimization. Given the superior performance on both accuracy and fairness metrics, SPARE achieves substantially higher FATE scores compared to other baseline models. For instance, in FATE (EqOp), SPARE achieves the highest FATE score, outperforming the second-best baselines by 36.5%, 11.7%, and 47.9%, respectively.

Notably, although GroupModel, DomainAdapt, MTL, ADE and SPARE all adopt group-specific training strategies, SPARE consistently and significantly higher accuracy compared to other bias mitigation methods. SPARE stands out by attaining the best overall performance in both accuracy and fairness metrics. These results demonstrate that SPARE's group-specific training is non-trivial, underlining the unique advantage of SPARE in effectively balancing fairness and accuracy while maintaining utility and guide model learning.

**Results on Fitzpatrick-17k dataset.**
 Table 2 presents the results of our method applied to the ResNet-18 backbone on the Fitzpatrick-17k dataset. SPARE outperforms all baseline methods across all accuracy metrics. In terms of fairness, it achieves the best performance (EqOp) and ranks second on both EqOp and EqOd. Consistent with the results obtained on the ISIC 2019 dataset, SPARE achieves the highest fairness effectiveness of training group-specific models in both narrowing inter-group performance disparities and maximizing per-group performance, indicating that SPARE is a promising approach for group-specific applications. Furthermore, SPARE demonstrates the highest FATE scores for all groups, which indicates that the FATE metric is a good indicator of EqOp and EqOd exceed those of the second-best methods by 25.6%, 25.6%, and 25.6%, respectively.

**Comparison with state-of-the-art in different backbones.**
 To further evaluate the generalizability of our approach, we replaced the backbone with VGG-11 (Simonyan and Zisserman, 2015) and repeated the experiments described in Section 5.2.1. The results are presented in Table 3, which shows that SPARE consistently outperforms all baseline methods. Our method achieves the highest performance across all accuracy metrics on both datasets, while also maintaining competitive results

<!-- PAGE 8 -->

Table 1

Results of accuracy and fairness on ISC 2019 dataset using ResNet-18 backbone.

| Method | Age | Precision | Recall | F1-score | Accuracy | Fairness |
| --- | --- | --- | --- | --- | --- | --- |
| EqualP / RATE 1 | EqualP / RATE 1 | EqualP / RATE 1 | EqualP / RATE 1 | EqualP / RATE 1 | EqualP / RATE 1 |
| ResNet-18 | Young | 0.718 | 0.766 | 0.743 |  |  |  | 0.018 / 0.000 | 0.021 / 0.000 | 0.558 / 0.000 |
| Old | 0.754 | 0.765 | 0.758 |  |  |  |  |  |  |
| GroupHold | Young | 0.724 | 0.762 | 0.740 | 0.021 | / 0.160 | 0.116 | / 0.131 | 0.560 | / 0.003 |
| Old | 0.777 | 0.798 | 0.782 |  |  |  |  |  |  |
| DomainHold | Young | 0.723 | 0.777 | 0.752 | 0.016 | / 0.117 | 0.075 | / 0.271 | 0.442 | / 0.124 |
| Old | 0.760 | 0.789 | 0.776 |  |  |  |  |  |  |
| MTL | Young | 0.745 | 0.756 | 0.747 | 0.018 | / 0.013 | 0.082 | / 0.207 | 0.555 | / 0.014 |
| Old | 0.757 | 0.766 | 0.760 |  |  |  |  |  |  |
| APPLE | Young | 0.743 | 0.769 | 0.749 | 0.016 | / 0.118 | 0.075 | / 0.277 | 0.539 | / 0.044 |
| Old | 0.773 | 0.764 | 0.764 |  |  |  |  |  |  |
| FairAdNN | Young | 0.713 | 0.772 | 0.739 | 0.015 | / 0.104 | 0.073 | / 0.278 | 0.458 | / 0.173 |
| Old | 0.739 | 0.755 | 0.752 |  |  |  |  |  |  |
| SFC-FairPrune | Young | 0.722 | 0.780 | 0.750 | 0.016 | / 0.114 | 0.089 | / 0.131 | 0.521 | / 0.070 |
| Old | 0.759 | 0.764 | 0.760 |  |  |  |  |  |  |
| FairQuantize | Young | 0.707 | 0.781 | 0.738 | 0.015 | / 0.159 | 0.086 | / 0.130 | 0.420 | / 0.240 |
| Old | 0.762 | 0.765 | 0.760 |  |  |  |  |  |  |
| SPARE | Young | 0.768 | 0.803 | 0.780 | 0.015 | / 0.217 | 0.075 | / 0.835 | 0.388 | / 0.855 |
| Old | 0.809 | 0.785 | 0.796 |  |  |  |  |  |  |

Table 2

Results of accuracy and fairness on Fitzpatrick-17k dataset using ResNet-18 backbone.

| Method | Skin Tone | Accuracy | Fairness |
| --- | --- | --- | --- |
| Precision | Recall | F1-score | EqualP / RATE 1 | EqualP / RATE 1 | EqualP / RATE 1 |
| ResNet-18 | Dark | 0.512 | 0.511 | 0.490 | 0.0031 | / 0.000 | 0.333 | / 0.000 | 0.186 | / 0.000 |
| Light | 0.467 | 0.468 | 0.449 |  |  |  |  |  |  |
| GroupHold | Dark | 0.511 | 0.512 | 0.492 | 0.0030 | / 0.045 | 0.320 | / 0.048 | 0.164 | / 0.107 |
| Light | 0.475 | 0.472 | 0.453 |  |  |  |  |  |  |
| DomainHold | Dark | 0.501 | 0.522 | 0.494 | 0.0030 | / 0.041 | 0.320 | / 0.045 | 0.163 | / 0.103 |
| Light | 0.465 | 0.479 | 0.459 |  |  |  |  |  |  |
| MTL | Dark | 0.514 | 0.529 | 0.500 | 0.0020 | / 0.051 | 0.302 | / 0.110 | 0.164 | / 0.108 |
| Light | 0.458 | 0.488 | 0.454 |  |  |  |  |  |  |
| APPLE | Dark | 0.521 | 0.517 | 0.491 | 0.0020 | / 0.047 | 0.312 | / 0.075 | 0.171 | / 0.064 |
| Light | 0.477 | 0.487 | 0.464 |  |  |  |  |  |  |
| FairAdNN | Dark | 0.493 | 0.495 | 0.469 | 0.0020 | / 0.057 | 0.302 | / 0.065 | 0.171 | / 0.024 |
| Light | 0.450 | 0.443 | 0.435 |  |  |  |  |  |  |
| SFC-FairPrune | Dark | 0.512 | 0.512 | 0.490 | 0.0020 | / 0.049 | 0.289 | / 0.147 | 0.164 | / 0.106 |
| Light | 0.490 | 0.472 | 0.469 |  |  |  |  |  |  |
| FairQuantize | Dark | 0.498 | 0.513 | 0.480 | 0.0028 | / 0.082 | 0.291 | / 0.109 | 0.156 | / 0.118 |
| Light | 0.450 | 0.470 | 0.448 |  |  |  |  |  |  |
| SPARE | Dark | 0.534 | 0.542 | 0.517 | 0.0020 | / 0.103 | 0.289 | / 0.200 | 0.158 | / 0.195 |
| Light | 0.508 | 0.499 | 0.488 |  |  |  |  |  |  |

In fairness metrics. Compared to the baseline VGG-11 model, SPARE yields average improvements across two datasets of 21.1%, 36.4%, and 29.9% in 
Top1
, 
TopP
, and 
TopR
, respectively. Additionally, it attains the highest 
FATE
 score among all methods on both datasets. These findings underscore the robustness of our approach across different neural network architectures.

3.2.2. RQ2: Weight distribution analysis on group-specific models

Fig. 6 presents the weight distribution boxplots for data with different Fitzpatrick skin types from the Fitzpatrick-17k dataset, evaluated using two group-specific models: the light-skin model (left) and the dark-skin model (right). The results show that for in-group data, most weights remain high, typically exceeding 0.8. In contrast, for out-of-group data, weights tend to decrease as the distance from the group increases in terms of Fitzpatrick skin type. Furthermore, we observe that the light-skin model assigns relatively lower weights to dark-skin samples, whereas the dark-skin model tends to place slightly higher weights on light-skin data. A Mann-Whitney U test confirmed that this difference is statistically significant (
p < 0.01
), although the effect size is small (
Cliff's d = -0.004
). These nuanced but consistent asymmetries suggest that the light-skin model performance may be more dependent on in-group data, potentially due to a greater distributional mismatch between dark-skin samples and the light-skin subgroup. This interpretation aligns with our empirical findings in Section 2, despite having a larger training set, the light-skin group underperforms in the global model. This may be due to dark-skin samples being further from the

<!-- PAGE 9 -->

Table 3

Results of accuracy and fairness on Fitzpatrick-17k dataset and ISIC 2019 dataset using VG-11 backbone.

| Method | Group | Accuracy | Fairness |
| --- | --- | --- | --- |
| Precision | Recall | F1-score | IoU@1 / FATE-1 | IoU@1 / FATE-1 | IoU@1 / FATE-1 |
| Fitzpatrick-17k Dataset |
| VG-11 | Dark | 0.493 | 0.490 | 0.495 | 0.0002 / 0.000 | 0.282 / 0.000 | 0.142 / 0.000 |
| Light | 0.435 | 0.447 | 0.422 |
| GroupModel | Dark | 0.496 | 0.486 | 0.474 | 0.0029 / 0.101 | 0.273 / 0.040 | 0.136 / 0.049 |
| Light | 0.441 | 0.459 | 0.439 |
| DomainAdapt | Dark | 0.499 | 0.488 | 0.475 | 0.0029 / 0.068 | 0.276 / 0.028 | 0.143 / 0.003 |
| Light | 0.443 | 0.450 | 0.427 |
| MTL | Dark | 0.493 | 0.488 | 0.483 | 0.0029 / 0.143 | 0.271 / 0.049 | 0.135 / 0.082 |
| Light | 0.499 | 0.449 | 0.439 |
| APPE | Dark | 0.497 | 0.482 | 0.473 | 0.0029 / 0.093 | 0.273 / 0.064 | 0.143 / 0.023 |
| Light | 0.497 | 0.452 | 0.440 |
| FairInAdv | Dark | 0.487 | 0.478 | 0.469 | 0.0029 / 0.044 | 0.277 / 0.001 | 0.138 / 0.012 |
| Light | 0.458 | 0.454 | 0.432 |
| SCP-FairProm | Dark | 0.494 | 0.496 | 0.478 | 0.0029 / 0.115 | 0.277 / 0.038 | 0.133 / 0.089 |
| Light | 0.451 | 0.454 | 0.438 |
| FairQuantile | Dark | 0.482 | 0.474 | 0.461 | 0.0029 / 0.086 | 0.268 / 0.013 | 0.129 / 0.032 |
| Light | 0.422 | 0.427 | 0.402 |
| SPARE | Dark | 0.512 | 0.517 | 0.492 | 0.0029 / 0.106 | 0.267 / 0.125 | 0.130 / 0.166 |
| Light | 0.474 | 0.472 | 0.449 |
| ISIC 2019 Dataset |
| VG-11 | Young | 0.669 | 0.724 | 0.687 | 0.023 / 0.000 | 0.150 / 0.000 | 0.078 / 0.000 |
| Old | 0.728 | 0.798 | 0.766 |
| GroupModel | Young | 0.675 | 0.722 | 0.688 | 0.021 / 0.130 | 0.116 / 0.340 | 0.060 / 0.128 |
| Old | 0.731 | 0.802 | 0.762 |
| DomainAdapt | Young | 0.677 | 0.724 | 0.689 | 0.021 / 0.090 | 0.103 / 0.316 | 0.061 / 0.345 |
| Old | 0.728 | 0.796 | 0.766 |
| MTL | Young | 0.669 | 0.728 | 0.688 | 0.022 / 0.042 | 0.108 / 0.279 | 0.060 / 0.229 |
| Old | 0.720 | 0.773 | 0.747 |
| APPE | Young | 0.686 | 0.739 | 0.703 | 0.022 / 0.005 | 0.095 / 0.372 | 0.072 / 0.082 |
| Old | 0.752 | 0.773 | 0.760 |
| FairInAdv | Young | 0.643 | 0.717 | 0.663 | 0.018 / 0.196 | 0.084 / 0.418 | 0.060 / 0.209 |
| Old | 0.727 | 0.770 | 0.748 |
| SCP-FairProm | Young | 0.662 | 0.724 | 0.683 | 0.020 / 0.125 | 0.098 / 0.341 | 0.068 / 0.123 |
| Old | 0.743 | 0.792 | 0.763 |
| FairQuantile | Young | 0.657 | 0.718 | 0.675 | 0.019 / 0.163 | 0.088 / 0.403 | 0.060 / 0.230 |
| Old | 0.743 | 0.785 | 0.755 |
| SPARE | Young | 0.713 | 0.765 | 0.729 | 0.018 / 0.369 | 0.090 / 0.565 | 0.052 / 0.398 |
| Old | 0.786 | 0.814 | 0.789 |

group label predictor's decision boundary, which allows them to dominate the shared representation space and shift the model's focus toward dark-skin-specific features.

Similarly, Fig. 6b shows the weight distributions across age groups in the ISIC 2019 dataset for two group-specific models: the young model (left) and the old model (right). To enable clearer visualization, we divided the age range into six categories: (0-15), (16-30), (31-45), (46-60), (61-75), and 6 (76-90). Compared to the more structured trends observed in Fitzpatrick-17k, the age-based results appear less regular. For example, in the old model, age group 2 (16-30) receives a weight similar to or slightly higher than group 3 (31-45). This may be attributed to the fact that, unlike skin tone, age-related changes are less visually distinct in skin images-particularly among individuals aged 16 to 45, where textural changes are subtle and difficult to detect visually. Overall, the observed trend that each group-specific model assigns higher weights to in-group data and gradually decreases weights as the group difference increases reflects the intended effect of our design, where weights are derived from distances to the corresponding group-specific decision boundary. In conjunction with the performance gains reported in Section 5.2.1, these results suggest that the proposed group-specific weighting scheme effectively captures group distinctions and contributes to improved fairness.

### 5.2.3. RQ3: Impact of weighting strategies

In this section, we examine alternative strategies for converting the combined distance 
d(x)
 (defined in Section 4.3) into sample weights. Specifically, given a set of samples each associated with a distance score 
d(x)
, the question is how to map these scores into weights. We compare our proposed continuous weighting in SPARE against several classical alternatives, as shown in Table 4. GroupWeight assigns a fixed weight to all samples within a group, without accounting for intra-group variations (Huang et al., 2016). Selection applies a binary threshold: samples with scores above the threshold receive a weight of 1, while others are assigned a weight of 0. Ranking sorts samples by their score and assigns weights based on their percentile rank (Roztoka et al., 2013). Experimental results show that the weighting strategy used in SPARE

<!-- PAGE 10 -->

Table 4
Performance comparison across weighting strategies on Fitzpatrick-176 and ISIC 2019 datasets.

|  | Fitzpatrick-176 | ISIC 2019 |
| --- | --- | --- |
| Skin Tone | Precision | Recall | F1 | Skin Tone | Precision | Recall | F1 |
| GroupType | Light | 0.483 | 0.477 | 0.480 | Young | 0.742 | 0.797 | 0.762 |
|  | Dark | 0.514 | 0.521 | 0.516 | Old | 0.785 | 0.798 | 0.772 |
| Selection | Light | 0.498 | 0.485 | 0.496 | Young | 0.749 | 0.794 | 0.764 |
|  | Dark | 0.529 | 0.538 | 0.532 | Old | 0.789 | 0.775 | 0.775 |
| Ranking | Light | 0.481 | 0.480 | 0.481 | Young | 0.731 | 0.792 | 0.754 |
|  | Dark | 0.512 | 0.513 | 0.492 | Old | 0.779 | 0.796 | 0.784 |
| SPARF | Light | 0.508 | 0.499 | 0.504 | Young | 0.803 | 0.790 | 0.796 |
|  | Dark | 0.534 | 0.542 | 0.537 | Old | 0.809 | 0.785 | 0.796 |

Fig. 4. Sample weight distribution for the (a) light and dark skin models on Fitzpatrick-176 dataset and (b) young and old models on ISIC 2019 dataset.

outperforms all alternatives across both datasets. Selection ranks second, suggesting that binary filtering can yield reasonably good performance, though it lacks the granularity of continuous weighting. Both GroupWeight and Ranking perform less effectively. This may be attributed to GroupWeight’s inability to capture within-group heterogeneity, and to Ranking’s reliance on carefully tuned mappings between rank percentages and assigned weights. Overall, these findings further support the effectiveness of SPARF’s weighting mechanism. Its simple yet powerful design enables sample-level weighting based on both similarity and utility, providing a fine-grained way to capture the informativeness of individual data points across multiple dimensions.

5.2.4. 
*RQ4: Utility vs. similarity comparison through different a values*

Fig. 5 illustrates the performance of two group-specific models on the Fitzpatrick-176 and ISIC 2019 datasets under varying values of 
\alpha
, which controls the trade-off between similarity and utility in the data weighting function. Specifically, 
\alpha = 0
 indicates that only similarity is considered, while 
\alpha = 1
 means that only utility determines the weight. The results show that, on the Fitzpatrick-176 dataset, the light-skin model achieves optimal performance at 
\alpha = 0.6
, while the dark-skin model peaks at 
\alpha = 0.6
, suggesting that similarity plays a more dominant role in the light-skin model. For the ISIC 2019 dataset, both the young and

old models perform best at 
\alpha = 0.5
, indicating the value of balancing both factors.

Across both datasets, models trained using only similarity information (
\alpha = 0
) consistently outperform those using only utility (
\alpha = 1
). This highlights the central importance of similarity in guiding sample selection. Group-specific models tend to directly capture the discriminative alignment between samples and their target group. Utility, meanwhile, also contributes to model effectiveness, but serves more as a complementary signal modulating the relative influence of samples based on their estimated informativeness. Together, the two dimensions provide a flexible and principled basis for weighting data in group-specific model training.

5.2.5. 
*RQ5: Ablation study of the combined distance*

To further validate the design of the combined distance, we conduct an ablation study that systematically examines the contribution of its utility and similarity components. While the previous analysis varied the trade-off parameter 
\alpha
, it remained unclear whether both components are individually necessary and whether alternative formulations could provide comparable benefits. Our ablation study therefore crucial to verify that our design is not only effective but also essential. We select three representative alternatives to compare against our definitions. For similarity, we consider feature contrast distance (FCD), which measures the distance between group feature means, and maximum mean discrepancy (MMD) (Yoo et al., 2017), which captures higher-order distributional differences. For utility, we adopt the logit gap (LG) (Nasir et al., 2020), a common measure of sample difficulty based on the margin between predicted class probabilities. Our alternatives provide meaningful baselines to test the robustness of our design choices.

Fig. 5 presents the results of this ablation study. When only utility or only similarity is used, performance drops across both datasets and groups, indicating that neither component alone is sufficient. Replacing our similarity with FCD or MMD also leads to weaker results, as these definitions fail to align group distributions as effectively as our approach. Likewise, substituting our utility with logit gap produces inferior performance, indicating that our informativeness signal provides a stronger foundation to guide the full method SPARF, which combines our definitions of both utility and similarity, consistently achieves the best balance of precision, recall, and F1 scores across groups. Together, these conclusions confirm that both components are indispensable and that the particular design choices in SPARF are critical to its effectiveness. The results thus provide strong evidence for the necessity of the combined distance in enabling robust group-specific modeling.

5.2.6. 
*RQ6: resource-performance trade-off*

Our framework trains separate models for different demographic groups to better capture group-specific group representations. While experimental results demonstrate that this strategy yields significant performance improvements, it is not fully independent of each other and may be impractical in scenarios with a large number of groups or constrained computational resources. Notably, deep neural networks often

<!-- PAGE 11 -->

Fig. 5. Performance variation with different 
\epsilon
 values for the (a) light and dark skin models on Fitzpatrick-17k dataset and (b) young and old models on ISIC 2019 dataset.

Table 5
Ablation study of the combined distance on Fitzpatrick-17k and ISIC 2019 datasets.

|  | Fitzpatrick-17k | ISIC 2019 |
| --- | --- | --- |
| Skin Tone | Precision | Recall | Skin Tone | Precision | Recall |
| Utility Only | Light | 0.479 | 0.522 | 0.468 | Young | 0.771 | 0.778 | 0.778 |
|  | Dark | 0.507 | 0.532 | 0.495 | Old | 0.777 | 0.748 | 0.766 |
| Similarity Only | Light | 0.487 | 0.482 | 0.473 | Young | 0.739 | 0.798 | 0.765 |
|  | Dark | 0.530 | 0.538 | 0.508 | Old | 0.781 | 0.776 | 0.780 |
| Utility + FCD | Light | 0.481 | 0.485 | 0.468 | Young | 0.741 | 0.796 | 0.759 |
|  | Dark | 0.518 | 0.535 | 0.496 | Old | 0.783 | 0.765 | 0.772 |
| Utility + MMD | Light | 0.480 | 0.482 | 0.471 | Young | 0.745 | 0.798 | 0.762 |
|  | Dark | 0.532 | 0.538 | 0.498 | Old | 0.780 | 0.783 | 0.776 |
| Similarity + LG | Light | 0.481 | 0.492 | 0.477 | Young | 0.734 | 0.797 | 0.771 |
|  | Dark | 0.525 | 0.531 | 0.507 | Old | 0.807 | 0.763 | 0.781 |
| SPARE | Light | 0.508 | 0.499 | 0.488 | Young | 0.758 | 0.805 | 0.780 |
|  | Dark | 0.534 | 0.542 | 0.517 | Old | 0.809 | 0.785 | 0.796 |

Table 6
Performance comparison across different sharing layers on Fitzpatrick-17k and ISIC 2019 datasets.

|  | Fitzpatrick-17k | ISIC 2019 |
| --- | --- | --- |
| Skin Tone | Precision | Recall | Skin Tone | Precision | Recall |
| Full Sharing | Light | 0.487 | 0.468 | 0.489 | Young | 0.718 | 0.786 | 0.743 |
|  | Dark | 0.512 | 0.511 | 0.490 | Old | 0.764 | 0.755 | 0.758 |
| Mini Sharing | Light | 0.484 | 0.484 | 0.479 | Young | 0.718 | 0.788 | 0.754 |
|  | Dark | 0.519 | 0.521 | 0.494 | Old | 0.779 | 0.773 | 0.774 |
| Half Sharing | Light | 0.497 | 0.487 | 0.479 | Young | 0.756 | 0.796 | 0.771 |
|  | Dark | 0.514 | 0.482 | 0.517 | Old | 0.782 | 0.780 | 0.785 |
| No Sharing | Light | 0.508 | 0.499 | 0.488 | Young | 0.768 | 0.803 | 0.780 |
|  | Dark | 0.534 | 0.542 | 0.517 | Old | 0.809 | 0.785 | 0.796 |

learn low-level, generic features (e.g., edges and textures) in the early layers. This observation raises a natural question: Is it necessary to train entirely separate models for each group, or can early layers be shared without substantially sacrificing performance?

To address this, we conducted additional experiments to explore the impact of sharing early network layers across groups. Using ResNet-18 as the backbone, we evaluated four configurations on two datasets:

1. Full sharing: a fully shared model with no group-specific components;
2. Mini sharing: a model where only the final layer is group-specific;
3. Half sharing: a partially specialized model in which approximately half of the layers are group-specific and
4. No sharing: fully group-specific models. The results, presented in Table 6, show that performance is lowest when all groups share the entire model. As more group-specific layers are introduced, performance consistently improves, reaching its highest point with fully separated models.

These findings highlight a trade-off exists between performance and computational efficiency. While fully specialized models offer the best performance, they require proportionally more resources. In resource-constrained environments, sharing early layers among groups provides a practical compromise, enabling competitive performance while significantly reducing the computational burden.

## 6. Discussion and conclusion

Ensuring fairness in medical AI remains a complex and actively debated challenge. Performance disparities across demographic groups are particularly concerning in clinical contexts, where diagnostic decisions have direct and potentially serious implications for patient outcomes. If left unresolved, these inequities may erode trust in AI-assisted diagnosis among both clinicians and patients. Existing fairness-aware

<!-- PAGE 12 -->

al. et al.

algorithm have made progress in addressing these gaps. However, most of the current methods rely on a shared, generic model and seek to maximize outcomes through implicit resource reallocation. This approach often improves performance for underrepresented groups at the expense of reduced accuracy for those already well-served. While this trade-off may be acceptable in low-risk domains, in healthcare—even small drops in accuracy can have serious clinical consequences. As a result, whether fairness should be achieved by compromising performance for any group remains an open and pressing question in high-stakes clinical applications.

In this work, rather than seeking fairness by trading off accuracy, we advocate for fairness through group-specific performance guarantees. While this approach may demand additional computational resources, we argue that such investment is justified in domains like healthcare, where precision and reliability are essential. To operationalize this idea, we propose SPARE: a sample reweighting algorithm that enhances group-specific model performance by selectively incorporating out-of-group training samples. SPARE estimates the utility of each candidate sample and its distributional similarity to the target group, before performance gain with robustness to distributional shift. Empirical results demonstrate a marked decrease in demographic disparities while significantly improves performance for target groups while preserving fairness metrics comparable to state-of-the-art baselines. These findings suggest that SPARE may serve as a practical paradigm for achieving fairness guarantees, especially in clinical applications where model reliability must remain a top-priority patient population.

While we advocate for subgroup-specific performance maximization as a more appropriate paradigm for achieving fairness in medical AI, this work also opens up several avenues for further exploration. One consideration lies in the complexity of demographic structures in real-world populations. In practice, demographic groups are rarely binary; instead, they consist of complex intersections—such as combinations of gender, race, and age—resulting in a potentially vast number of subgroups. Training a dedicated model for each subgroup is infeasible. A promising direction may lie in group clustering, identifying a small number of representative subgroups that capture the key variations across the population, and then applying group-specific optimization at this reduced granularity. Another opportunity for future research concerns scalability. Recent advances in parameter-efficient fine-tuning (Liu et al., 2023, 2023) suggest that full model retraining for each group may not be necessary. Instead, lightweight modules could offer a scalable way to tailor models while filtering harmful out-of-group samples or adapting representations selectively. These techniques may provide practical means to support subgroup performance without incurring prohibitive computational overhead. Finally, it is worth noting that while our approach consistently improves both subgroup performance and fairness metrics in SPARE, it does not explicitly optimize fairness criteria such as Equal Opportunity or Equalized Odds, and therefore cannot guarantee improvements under these definitions. Encouragingly, we observe that fairness metrics often improve as a byproduct, likely because the reweighted groups benefit disproportionately when subgroup-specific performance is maximized. Future work could investigate the theoretical connection between performance maximization and fairness-gap reduction, potentially providing formal support for when and why such improvements occur.

We view SPARE as an initial step toward this more flexible approach to fairness that moves beyond uniformity and allows models to adapt to group-specific needs while maintaining clinical rigor. We hope this work encourages further research into practical fairness strategies that can more effectively support equitable outcomes across diverse patient populations.

**CRediT authorship contribution statement**

Gelai Xu: Writing – review & editing, Writing – original draft, Visualization, Methodology, Conceptualization; Yuying Duian: Writing – review & editing, Validation, Formal analysis, Conceptualization; Jun Wu: Writing – review & editing, Validation, Data curation; Qingchun Chiu: Writing – review & editing, Methodology, Conceptualization; Michael Lam: Writing – review & editing, Methodology, Conceptualization; Wei Jia: Writing – review & editing, Methodology, Conceptualization; Yixu Shi: Writing – review & editing, Supervision, Resources, Methodology, Investigation.

**Declaration of generative AI and AI-assisted technologies in the writing process**

During the preparation of this work, the author(s) used ChatGPT
^4^
 to assist with the readability and language. After using this tool service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.

**Declaration of competing interest**

The authors declare the following financial interests/‘personal relationships’ which may be considered as potential competing interests: Gelai Xu, Yuying Duian, Jun Wu, Qingchun Chiu report financial support was provided by University of Notre Dame. If there are other authors that declare that they have no known competing interests or personal relationships that could have appeared to influence the work reported in this paper.

**Acknowledgment**

This project is supported in part by the National Institutes of Health under Grant R01LM033837, and by the National Science Foundation under Grant IIS-2247607.

**Appendix A.**

**A.1. Proof for Eq. (1)**

Proof: We have:

e_{\mu}(f_{\mu} + e_{\mu} f_{\mu}) = e_{\mu}(f_{\mu} + e_{\mu} f_{\mu}) + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{\mu} + e_{\mu} f_{\mu} = e_{\mu} f_{\mu} + e_{\mu} f_{

<!-- PAGE 13 -->

Gu et al. Medial Image Analysis 19 (2020) 105590

References

Ayushmann, Guddey, H., Mittel, V., Chawla, M., Gupta, G.R., 2014. Fair and accurate skin disease classification using deep learning. 
*IEEE J. Biomed. Health Inform.*
 18 (1), 166–174.

Ayushmann, Guddey, H., Mittel, V., Chawla, M., Gupta, G.R., 2014. Fair and accurate skin disease classification using deep learning. 
*IEEE J. Biomed. Health Inform.*
 18 (1), 166–174.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Agata, A., Nasonov, M., Iida, S., 2020. MTA4R: low-risk adaptation approach for efficient medical image processing. 
*IEEE Trans. Med. Imaging*
 39 (11), 3696–3705.

Vision and Pattern Recognition, pp. 16196–16205.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Agata, A., Nasonov, M., Iida, S., 2020. MTA4R: low-risk adaptation approach for efficient medical image processing. 
*IEEE Trans. Med. Imaging*
 39 (11), 3696–3705.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE Trans. Med. Imaging*
 41 (1), 1–14.

Alvarez, S., Song, W., Nemeth, C.R., Liu, Y., Xu, D., 2022. Subpopulation-specific medical image analysis for radiologists with double precision. 
*IEEE*

<!-- PAGE 14 -->

G. Xu et al.