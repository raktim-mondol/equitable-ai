<!-- Page 1 -->

Expert Systems With Applications 292 (2025) 128266

Contents lists available at ScienceDirect

Expert Systems With Applications

journal homepage: 
[www.elsevier.com/locate/eswa](http://www.elsevier.com/locate/eswa)

Underrepresentation, label bias, and proxies:

Towards Data Bias Profiles for the EU AI act and beyond

Marina Ceccona,b,*, Giandomenico Cornacchiab, Davide Dalle Pezzec,d, Alessandro Fabrisc,d,e,f, Gian Antonio Sustog,a

a Department of Information Engineering, University of Padova, Italy

b IBM Research Europe, Dublin, Ireland

c Max Planck Institute for Security and Privacy, Bochum, Germany

d University of Trieste, Trieste, Italy

ARTICLE INFO

Keywords:

Algorithmic fairnessAnti-discriminationBias detectionData biasAI act

ABSTRACT

Undesirable biases encoded in the data are key drivers of algorithmic discrimination. Their importance is widely recognized in the algorithmic fairness literature, as well as legislation and standards on anti-discrimination in AI. Despite this recognition, data biases remain underexplored, hindering the development of computational best practices for their detection and mitigation.

In this work, we present three common data biases and study their individual and joint effect on algorithmic discrimination across a variety of datasets, and fairness measures. We find that underrepresentation of vulnerable populations in training sets is less conducive to discrimination than conventionally affirmed, while combinations of proxies and label bias can be far more critical. Consequently, we develop dedicated mechanisms to detect specific types of bias, and combine them into a preliminary construct we refer to as the Data Bias Profile (DBP). This initial formulation serves as a proof of concept for how different bias signals can be systematically documented. Through a case study with popular fairness datasets, we demonstrate the effectiveness of the DBP in predicting the risk of discriminatory outcomes and the utility of fairness-enhancing interventions. Overall, this article bridges algorithmic fairness research and anti-discrimination policy through a data-centric lens.

1. Introduction

Algorithmic anti-discrimination is a relatively young field, rapidly moving from niche research to market readiness (Álvarez et al., 2024). Several years of work carried out by a growing research community have convincingly shown that algorithms developed without attention to fairness put vulnerable groups at a systematic disadvantage (Angwin, Larson, Mattu, & Kirchner, 2016; Glazko, Mohammed, Kosa, Polturi, & Mancock, 2024; Obermeyer, Powers, Vogell, & Mullainathan, 2019). Recognizing the critical implications of this research, policymakers and standards organizations have published regulations and norms on the topic (ISO, 2021; Parliament, 2024; Schwartz et al., 2022). These documents require standardization to apply across many domains where fairness work is critical, including medicine (Obermeyer et al., 2019), finance (Gillies, Meursault, & Usun, 2024), employment (Fabris et al., 2024), and education (Baker & Havn, 2022).

Evaluations of data bias are key computational tools for anti-discrimination work. Since biases in the data are fundamental drivers of algorithmic discrimination (Brzezinski et al., 2024; Verro, Torchiano, & Mesci, 2021), bias management is mentioned in every recent standard and regulation on algorithmic anti-discrimination (ISO, 2021; Parliament, 2024; Schwartz et al., 2022). Policy formulations on this topic are rather vague, favouring flexibility on one hand, but leaving the contours of law-abiding bias management undefined for practitioners, contributing to legal risk and uncertainty. For example, recent regulation requires providers of AI systems in high-risk domains to signal sufficient efforts of bias detection and mitigation. How this should be done in practice, however, is left completely undefined (Deck, Müller, Braun, Zipperling, & Kühn, 2024).

Defining precise criteria for bias management requires answering several important questions, left mostly unaddressed in the fairness literature. First, different data biases are associated with algorithmic discrimination. Which combinations of biases are more critical for fairness?

* Corresponding authors.

E-mail addresses: marina.ceccon@phl.unipd.it (M. Ceccon), giandomenico.cornacchia@ibm.com (G. Cornacchia), davide.dallepezze@unipd.it (D. Dalle Pezze), alessandro.fabris@mpi-sp.org, alessandro.fabris@unipd.it (A. Fabris), gianantonio.susto@unipd.it (G.A. Susto).

https://doi.org/10.1016/j.eswa.2025.128266

Received 19 December 2024; Received in revised form 14 May 2025; Accepted 19 May 2025

Available online 26 May 2025

0957-4174/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

---

<!-- Page 2 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Second, data biases are typically described qualitatively but vastly lack a quantitative characterization. It is possible to monitor discrimination biases unambiguously? Third, while a plethora of fairness interventions exist in the literature, a set of guidelines to prioritize them is prominently lacking. In sum, how can practitioners and researchers make decisions about bias mitigation in a principled manner?

Contributions. In this work, we tackle the above questions, providing several contributions.

- • We study three types of data bias widely recognized for their negative influence on algorithmic fairness, namely underrepresentation, label leakage, and proxies. We also propose to monitor discrimination datasets, algorithms, and fairness measures we analyze their joint influence on algorithmic discrimination. Our experiments show that unfairness representation in training data is overemphasized in the literature while label bias is more critical. This novel result challenges conventional wisdom held in the algorithmic fairness community.
- • We propose a principled mechanism for bias detection that is widely applicable in practice. We propose to monitor the impact of data bias to detect specific data biases without auxiliary information from external sources. We integrate these measures into a preliminary construct, the Data Fairness Baseline (DFB), which provides a quantitative foundation for identifying and communicating data biases, as well as assessing the risk of algorithmic discrimination. This framework serves as a proof of concept, offering a concrete starting point that the research community can build upon to develop a more robust and systematic approach to bias-aware data documentation.
- • We discuss the far-reaching implications of our work for researchers and practitioners. We provide a set of guidelines to prioritize mitigated datasets with complementary properties for their experiments, overcoming the present limitations of fairness benchmarks. Finally, we recommend to algorithmic practitioners on the curation and utilization of anti-discrimination datasets.

Structure. Section 2 presents related work. Section 3 introduces data bias and experimental protocols to analyze it. Section 4 studies the effect of data bias. Section 5 describes bias detection, introducing and demonstrating DBFs. Sections 6 and 7 discuss our results in the broader context of algorithmic fairness work concluding with recommendations for researchers and practitioners.

## 2. Related work

Algorithmic fairness research keeps contributing new approaches to measure the risk of discrimination (Chen, Giudici, Liu, & Raffinetti, 2024; Goh, et al., 2023; Goh, et al., 2022; Goh, et al., 2021; Goh, et al., 2020; & Bisga, 2023) and to mitigate it (Cruz & Harth, 2024; Fajri, Saxena, Pei, & Pechenzyk, 2024; Yin, Raab, Liu, & Liu, 2023; Zhang, Cheng, Yuan, & Zhang, 2024). Moving fairness toward market readiness requires research on operationalizing algorithmic anti-discrimination policy (Section 2.1), on its close connection with data bias (Section 2.2), and on principled documentation practices to support anti-discrimination (Section 2.3).

### 2.1. AI policy on anti-discrimination

Influential legislation and standards on anti-discrimination in AI, such as the EU AI Act (Parliament, 2024) and the NIST report on bias in AI (Schwartz et al., 2022) require multi-disciplinary research to translate policy into computational best practices. Drukker et al. (2023), for example, complement NIST guidelines with a list of domain-specific biases that arise in the medical domain. Borgesius, Baranowska, Hacker, and Fabris (2024) focus on the AI Act, summarizing the main requirements for fairness and evaluation of bias, and their documentation. Desbrun et al. (2024) compile a list of practical challenges for compliance with anti-discrimination requirements outlined in the AI Act. By highlighting

the need for model owners to examine “possible biases that are likely to lead to discrimination prohibited under Union law”, they stress the pressing questions of which biases lead to discrimination models and what kind of evidence is required to signal sufficient efforts for bias detection and correction. Our work aims to provide flexible computational tools to answer this question across different domains.

### 2.2. Linking fairness with data properties

A growing line of work centers on quantifying data biases and their influence on models. Guerdan, Cotton, Wu, and Holstejn (2023) describe a framework for quantifying data properties that develop a central framework to disentangle them. Baumann, Castelnuovo, Crupi, Inverardi, and Regoli (2023) present several data biases and provide initial insights into their mitigation. Brazinski et al. (2024) study the variability of fairness measures in the context of underrepresentation of protected groups and the imbalance between positives and negatives. They postulate certain properties (e.g., “Fairness should not vary with underrepresentation”) that are not always satisfied and provide a method to identify “reliable”, Fragkathoulas, Papanikou, Kaidi, and Pitoura (2024) survey the intersection of fairness and explainability, including explanations that can describe sources of unfairness.

Venkataraman (2024) propose to predict the risk of discrimination against vulnerable groups from their underrepresentation in the data. Their work is highly influential for ours; it represents a first attempt at developing mechanisms to detect (a single type of) data bias and connect it with model fairness, opening the way to follow-up studies (Mecei, Torchiano, Verro, & De Martin, 2023; Mecei, Verro, & Torchiano, 2022), and providing a solid foundation for our work. Important contributions in methodology and conclusions. First, we consider three types of data bias, adding label bias and proxies to underrepresentation and studying their joint influence on fairness. Second, we assess model fairness on unbiased test sets. For example, to measure the effect of strong underrepresentation, we remove from the training set a large percentage of items from the disadvantaged group (even 100%), but we retain them in the test set. Third, we propose a rationale to conclude that underrepresentation in training sets is overemphasized in the algorithmic fairness literature and that other data biases can be more critical.

### 2.3. Quantitative data documentation

Data documentation is increasingly recognized as a central component of machine learning (Dubois, Meseles, Silvello, & Susto, 2022; Gebau et al., 2021; Golpuskar et al., 2024; Holland, Honty, Newman, Joseph, & Chmielnicki, 2020; Königstorfer & Thallmann, 2022; Pushkarna, Zaldívar, & Kjartansson, 2022; Rondina, Vetro, & De Martin, 2023; Sambasivan et al., 2023). With few exceptions, prominent data documentation frameworks are qualitative. Among quantitative frameworks, Holland et al. (2020) emphasize the analysis of correlations between variables to spot anomalous trends. Domingos-Casteln, Patarain, and Galar (2024) develop metrics to quantify representational and stereotypical biases, demonstrating them on a facial expression recognition dataset. In this work, we propose a principled suite of measures to quantify and document biases associated with underrepresentation. We outline how these can be composed into a preliminary construct, the Data Bias Profile (DBP), to support structured documentation and analysis. Our approach is tailored to one specific aspect of datasets and differs from existing methods, both quantitative and qualitative.

### 2.4. Data bias

Data is a fundamental driver of algorithmic discrimination (Mehrabri, Morstatter, Saxena, Lerman, & Galstyan, 2022; Schwartz et al., 2022; Schwartz et al., 2021). With few exceptions, prominent data properties that if unaddressed, lead to AI systems that perform better or worse for different groups (ISO, 2021). In this section, we describe three types of data

2

---

<!-- Page 3 -->

M. Cecon et al.

Expert Systems With Applications 292 (2025) 128266

bias widely recognized for their impact on algorithmic fairness along with corresponding bias injection mechanisms.

### 3.1. Underrepresentation

The term representativeness typically refers to the ability of a dataset to represent the development of an accurate model for a target population. Underrepresentation of disadvantaged groups in data is described at length in popular media (Cobham, 2020; Perez, 2019) and seminal fairness papers (Goodfellow et al., 2016; 2017; Mitchell et al., 2022; Shunshar et al., 2017) as a key driver of algorithmic discrimination. When groups from the target population are underrepresented in training data, it is argued, AI models will fail to generalize and underperform for those groups (Cohen & Guttag, 2021). Indeed, the underrepresentation of protected groups in training sets is studied as a predictor of model unfairness (Brzezinski et al., 2024; Vetroň et al., 2021). Influential legislation (e.g., the EU AI Act, 2024) and regulation as a central component of algorithmic anti-discrimination (Parliament, 2024; Schwartz et al., 2022) and mandate efforts to document and curb it.

### 3.2. Label bias

Labels (or target variables) are key to AI. They give machine learning a “ground truth” that models learn to replicate. Since data is a social mirror, labels reflect undesirable disparities in society (Barocas, Hardt, & Narayanan, 2023). Indeed, measurement methods can be biased across protected groups (Vardassi, de Rijke, Diaz, & Daghvani, 2024). Policing and arrest tend to target poorer neighbourhoods, therefore biasing crime data against black US citizens (Bao et al., 2021). Medical data suffers from underdiagnosis due to substandard medical care (Clairfanrness, Tamang, Yazdany, & Schmajuk, 2018) and barriers to access for vulnerable populations (Obermeyer et al., 2019). Semi-automated labels are especially likely to compound and reinforce spurious biases in training datasets (Jigwaw, 2018). Several methods have been proposed in the literature to counteract unfair label biases under simplifying assumptions (Goldman, Friedman, Moeller, Schöthebeck, & Venkatramanan, 2015; Kamiran & Calders, 2011; Liu et al., 2024; Wang, Liu, & Levy, 2021). Overall, measurement bias is inevitable (Jacobs & Wallace, 2021); it is especially problematic for anti-discrimination when it filters out labels associated with protected groups (Mehlitz, Suresh, & Guttag, 2021). Models trained to predict these labels will encode the underlying biases and harm disadvantaged groups (Bao et al., 2021; Obermeyer et al., 2019).

### 3.3. Proxies

Proxies are features that correlate with protected attributes. Protected attributes such as race can be revealed by individual features, such as names in a resume (Santamaría & Mihajlović, 2018), or by combinations of features, such as the browsing history of a person (Hü, Zeng, Li, Niu, & Chen, 2007). Pursuing fairness by simply removing protected attributes from features, an approach termed fairness through unawareness, is ineffective precisely for this reason: a redundant encoding of latent protected variables is present in other features (Barocas & Scheel, 2016; Hardt, Price, & Srebro, 2016) Pedreschi, Ruggieri, & Turini, 2008). Proxy removal, for example through feature selection or projection, is a popular approach to improve algorithmic fairness (Alves, Anblard, Bernier, Coceurel, & Napoli, 2021; Blind Stairs, 2024; Edwards & Storkey, 2016; Hivaw, 2022; Madian, Cropper, Pittosi, & Zemel, 2018). Conversely, input features that are strongly correlated with protected attributes are considered a driver of unfairness in data-driven models (Schwartz et al., 2022). Policymakers may therefore expect practitioners to actively identify and eliminate strong proxy features from models powering automated decisions (Bogon, 2024).

Table 1Notation. Main notational conventions adopted in this work.

| symbol | meaning |
| --- | --- |
| x \in S | protected attribute |
| s = x | historically disadvantaged group |
| y \in Y | historically advantaged group |
| y = g(x) | target variables |
| y = g(x, \theta) | positive and negative target values |
| \hat{y} \in \hat{Y} | non-protected attributes |
| \hat{y} = \hat{g}(x) | estimation of y through classifier \hat{g}(\cdot) |
| \hat{y} = \hat{g}(x, \theta) | estimation of y through classifier \hat{g}(\cdot) |
| P_{\hat{y}}(s = d) | prevalence of d in set s |
| \sigma_{\hat{y}}(s = d) | percentage of disadvantaged points from group d |
| \sigma_{\hat{y}}(s = y) | training set and target labels after bias injection |
| \sigma_{\hat{y}}(s = y \| \hat{y} = d) | percentage of disadvantaged instances retained for training |
| \sigma_{\hat{y}}(s = y \| \hat{y} = y) | underrepresentation factor |
| u = -1 | flip label or label bias: f = \Pr(\hat{y}_s = \hat{y}, s = d) |
| f \in (0, 1) |   |

### 3.4. Data bias injection

Notation. Table 1 summarizes the notational conventions. We let s \in S denote a sensitive attribute, with value y = a(s = d) denoting the historically (dis)advantaged group. We let \hat{y} indicate the target variable, with values in \hat{Y} = \{\hat{B}, \hat{G}\}, and we let x \in X denote the non-protected features used for classification. Target variables are estimated through a classifier \hat{g}(\cdot) such that \hat{y} = \hat{g}(x, \hat{y}_s) denote a sample and P_{\hat{y}}(s = d) indicate the prevalence of items with \hat{y}_s = d in that sample. To inject biases in training sets, we subsample the disadvantaged group and flip its labels. We use \sigma^* to denote a training set derived from s via bias injection.

Underrepresentation. We let \sigma^*(s = d) denote the percentage of instances from the disadvantaged group retained for training, so that

\Pr(s = d) = r \cdot \Pr(\hat{y} = d) \quad \sigma^*(s = d) = r \cdot \sigma(\hat{y} = d), \quad (1)

where u = -1 is the underrepresentation factor for the disadvantaged group. We vary u across its full range, extreme values u = 1 and u = 0 denote complete underrepresentation and no underrepresentation, respectively.

Label bias. For label bias, we selectively flip labels. We let f \in (0, 1) indicate the proportion of positive instances (y = \hat{G}) from the vulnerable group whose label is flipped to negative (y = \hat{B}), i.e.

f = \Pr(\hat{y}_s^f = \hat{B} | y_s = \hat{B}, s = d). \quad (2)

We let the flip factor f vary between f = 0 and f = 1; the former corresponds to no bias injection, the latter to maximum bias where all the positive items from the disadvantaged group in the training set are flipped to a negative target label.

Proxies. We quantify the strength of proxies as their joint ability to predict sensitive attributes. We train a classifier \hat{h}(\cdot) to estimate the protected attribute s and we compute its AUC to measure the strength of proxies.

\hat{h} = \text{h}(x), \quad \text{sAUC} = \text{AUC}(\hat{h}). \quad (3)

We term AUC the proxy factor and propose two mechanisms to vary it. An additive protocol adds to the non-sensitive variables x a new feature correlated with sensitive variables

x_{\text{new}} = x + v, \quad v \sim \mathcal{N}(0, \text{std}^2) \quad \hat{X}' = X' \times x_{\text{new}}. \quad (4)

1 We use the nomenclature sensitive and protected attribute interchangeably.

3

---

<!-- Page 4 -->

M. Ceccan et al.

Expert Systems With Applications 292 (2018) 128266

## Table 2

Dataset biases. We report dataset name, sensitive attribute information such as (dis)advantaged groups and their prevalence, and target variables information such as positive classes and their prevalence among members of the advantaged and disadvantaged groups.

| Dataset | s | a | d | y | y = \emptyset | Pr_{\gamma}(s = a) | Pr_{\gamma}(y = \emptyset \| s = a) | Pr_{\gamma}(y = \emptyset \| s = d) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adult | Gender | Male | Female | income | > 50K | 0.68 | 0.3125 | 0.1136 |
| Adult | Marital status | Married | Not married/ Divorced | income | > 50K | 0.68 | 0.4513 | 0.0668 |
| Compas | Ethnicity | Caucasian | African-American | recidivism | no reoffense | 0.60 | 0.6091 | 0.4769 |
| Critics | Ethnicity | Caucasian | Other | violate crime rate | low | 0.7035 | 0.1805 | 0.1805 |
| Folkwares | Ethnicity | Caucasian | Other | employment | employed | 0.89 | 0.5688 | 0.5048 |
| German | Age | > 25 y | <= 25 y | credit risk | good | 0.81 | 0.7284 | 0.5789 |
| NH | Gender | Male | Female | chest pathologies | presence | 0.54 | 0.4112 | 0.3981 |
| Fitzpatrick17K | Skin type | Light | Dark | skin conditions | presence of condition | 0.86 | 0.2826 | 0.1897 |

where \nu is a normal random variable with zero mean and \text{std}^2 variance; we increase the strength of proxies by reducing std. In addition, we consider a two-step protocol, iteratively removing from the non-sensitive variables X the strongest predictors of the sensitive attribute

X_{\text{drop}} = \max(\text{sim}(x, v))

X'_{\text{drop}} = X_{\text{drop}} - X_{\text{drop}}^* \quad (5)

where \text{sim}(x, v) denotes a similarity function (e.g. correlation) and X'_{\text{drop}} is the feature space obtained removing X_{\text{drop}} from the original feature set.2

## 4. Effect of data bias

In this section, we investigate the impact of data biases. We inject data bias into the training and validation datasets of classification models and assess their combined influence on algorithmic discrimination, evaluating fairness metrics on unbiased test sets.

### 4.1. Overall setup

Datasets. We consider five tabular and two medical imaging datasets, described in Table 2. These datasets are popular in the fairness literature and span several domains where fairness work is critical. Datasets contain information on protected attributes including gender, age, ethnicity, and marital status. Table 2 additionally reports the target variable of each dataset, the prevalence of the disadvantaged and the advantaged groups, as well as the prevalence of positive items in each group. The advantaged group has a higher rate of positive samples compared to the disadvantaged group. Notice that the positive class indicates the advantaged group, whereas the negative class indicates the disadvantaged group. We also consider a loan dataset, which is associated with critical resource allocation (loans, medical attention) or lower penalties (incarceration, strict policing). This makes high true positive rates unambiguously important to counter undesirable patterns harming disadvantaged groups, such as underloaning and overcriminalization. More details on each dataset are reported in Appendix A.

Models. We train deep learning models for medical imaging datasets and traditional machine learning models for tabular data. Models optimize accuracy-oriented loss functions without any fairness-enhancing component. For each of the tabular datasets, we train a random forest (RF), a support vector classifier (SVC), and a linear regression (LR). Following the recommendations of Goodfellow et al. (2016) on NIH and a vgg16 model on Fitzpatrick17K (Gross et al., 2012; Seyed-Valianesi, Liu, McDermott, Chen, & Ghassemi, 2020).

Splitting & repetitions. We process tabular datasets with an 80-10-10 train-validation-test split. For NIH, we follow the literature with an 80-10-10 train-validation-test split (Seyed-Valianesi et al., 2020). For Fitzpatrick17K, we use a 70-15-15 split to ensure sufficient representation of the disadvantaged group in the test set, favoring more stable fairness measurements. After splitting the data, we inject biases in the training

and validation set. We keep the test set unbiased for a reliable evaluation.3 For each experiment, we perform 10 training repetitions (with different initial seeds), reporting the mean and standard deviation for metrics of interest.

Performance metrics. To evaluate the classification performance of each model, we use \ell_1 (Gibson et al., 2017). Briefly, we consider the balanced accuracy on the test set, i.e. the average between the true positive rate and the true negative rate:

BA_{\gamma} = \frac{Pr_{\gamma}(\hat{y} = y | y = a) + Pr_{\gamma}(\hat{y} = \emptyset | y = d)}{2} \quad (6)

Fairness metrics. To assess the model fairness, we consider three complementary metrics: demographic parity, equal opportunity, and predictive quality parity. Demographic parity (DP), also called independent parity (Babernagel et al., 2017), is defined as a mean difference (Zlobin, 2017), is defined as the difference between the acceptance rates computed on different groups

DP_{\gamma} = Pr_{\gamma}(\hat{y} = y | s = a) - Pr_{\gamma}(\hat{y} = y | s = d) \quad (7)

and it is independent of the ground truth labels. It is especially salient in contexts where reliable ground truth information is hard to obtain and a positive outcome is especially important, e.g. employment, health, and criminal justice (Du, Yang, Zou, & Hu, 2021; Gajane & Pechenizky, 2018).

Contrary to DP, the equal opportunity (EO) metric is based on the target variable y (Hardt et al., 2016). It is defined as the difference in the true positive rates:

EO_{\gamma} = Pr_{\gamma}(\hat{y} = y | s = a, y = a) - Pr_{\gamma}(\hat{y} = y | s = d, y = a). \quad (8)

EO is especially important in contexts, such as healthcare, where a ground truth of reasonable accuracy is available and false negatives (missed diagnosis) are especially harmful.

A third anti-discrimination criterion, focused on both types of misclassification, is represented by prediction quality parity (PQP) (Du et al., 2021). We define it as the difference in balanced accuracy between sensitive groups:

PQP_{\gamma} = BA_{a, \gamma} - BA_{d, \gamma} \quad (9)

In the experiments below, we measure algorithmic fairness according to these metrics as we inject controlled biases the training sets. We present results for logistic regression (or tabular datasets) and equal opportunity (or non-tabular datasets) across all models and datasets. The results for the remaining models and metrics can be found in Appendix B; unless explicitly stated, they are equivalent to those illustrated below.

### 4.2. Underrepresentation

Setup. To study the effect of underrepresentation, we train models in four different settings, varying the underrepresentation factor by

2 We use the term unbiased in a narrow sense, to denote simple random samples of the original dataset, as opposed to subsets where we deliberately inject different types of data bias.

2 Eq. (5) is a single iteration of the subtractive protocol.

4

---

<!-- Page 5 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128626

### Table 3

Model fairness is mostly unaffected by underrepresentation in the training set. Equal Opportunity (EO), varying the underrepresentation of the minority group in the training set from u = 0 (no bias) to u = 1 (maximum bias), Mean and standard deviation over 10 replications. Symbols “*” and “**” denote statistically significant differences with respect to u = 0 at p = .05 and p = .01, respectively, measured with an unpaired t-test.

| Dataset | sensitive | model | EO | EO | EO | EO |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.06 \pm 0.02 | 0.09 \pm 0.02 | 0.09 \pm 0.02 | 0.21 \pm 0.07** |
| Adult | marital-status | LR | 0.36 \pm 0.03 | 0.36 \pm 0.03 | 0.37 \pm 0.03 | 0.29 \pm 0.04** |
| Compas | race | LR | 0.17 \pm 0.03 | 0.17 \pm 0.03 | 0.16 \pm 0.02 | 0.16 \pm 0.02 |
| Crisis | race | LR | 0.33 \pm 0.11 | 0.33 \pm 0.12 | 0.30 \pm 0.14 | 0.28 \pm 0.13 |
| Folklores | race | LR | 0.05 \pm 0.04 | 0.05 \pm 0.04 | 0.05 \pm 0.04 | 0.05 \pm 0.04 |
| German | gender | LR | 0.07 \pm 0.13 | 0.06 \pm 0.11 | 0.07 \pm 0.09 | 0.06 \pm 0.07 |
| NIH | gender | DeeSNet | 0.01 \pm 0.02 | 0.04 \pm 0.01** | 0.03 \pm 0.02 | 0.06 \pm 0.02** |
| Fitzpatrick17k | skin type | vgg16 | 0.09 \pm 0.02 | 0.14 \pm 0.02 | 0.11 \pm 0.02 | 0.11 \pm 0.02 |

undersampling the disadvantaged group. We consider the unbiased case (u = 0), the fully biased case (u = 1), where the disadvantaged group is completely absent from the training set, and two intermediate settings (u = 0.2, u = 0.8).

Results. Remarkably, Table 4 shows that the underrepresentation of the minority group does not have a strong impact on fairness: EO is approximately constant as u varies in all datasets. The only datasets for which the increase in disparity is statistically significant are NIH and Adult (gender). For Crime and Adult (marital status), the gap even decreases slightly when the disadvantaged group is removed from the training set.

This trend is surprising and contradicts popular narratives about the effect of underrepresentation on algorithmic fairness. To further analyze these results, we split EO into its groupwise TPR components (Eq. (8)). Fig. 1 reports boxplots of the TPR for the advantaged and disadvantaged groups in NIH and Folklores, which are representative of the remaining datasets. Fig. 1 shows that the TPR remains approximately stable as underrepresentation u varies maximally. Specifically, the TPR for both the advantaged and disadvantaged groups in Folklores are perfectly stable, while they slightly decrease for NIH. The decrease is more marked for the disadvantaged group, leading to a small increase in EO. Underrepresentation is more important for NIH since nearly half of the original training set consists of points from the disadvantaged group (Table 2).

Interpretation. This notable result contradicts the position commonly held in algorithmic fairness that increasing the representation of disadvantaged groups in training sets is critical for equitable outcomes. We defer a broader interpretation of this result to Section 6, where we

discuss our findings in broader context of algorithmic fairness research and practice. We also highlight here as an indication that underrepresentation in training sets is overhyped and that other biases may be stronger drivers of model unfairness.

### 4.3. Label bias

Setup. In this section, we train models on data affected by different degrees of label bias. Specifically, we take a portion (f) of positive samples from the disadvantaged group in the training set and flip their labels to negative. We let the flip factor (Eq. (2)) take values f = 0 (no bias), f = 0.2 (moderate bias), f = 0.8 (strong bias), and f = 1 (maximum bias). Additionally, we study the interplay between label bias and underrepresentation by analyzing a scenario in which the prevalence of the disadvantaged group is decreased and part of its positives are flipped. More in detail, at the end of this section, we assess the joint effect of a weak label bias (f = (0.0, 0.2)) and widely-ranging underrepresentation (u \in (0, 1)).

We report the mean and standard deviation of EO across ten replications. As in the previous section, we focus on LR, while results for other models are available in Appendix B along with additional fairness measures.

Results. Table 4 shows that label bias has a large impact on fairness, sizably stronger than underrepresentation (Table 3). Indeed, across all experiments, unfairness grows as f increases. In datasets like NIH and Adult, this increase is very sizable, while for others such as Folklores it is more contained. Tables B.15, B.16, and B.19 in Appendix C show

Fig. 1. Large underrepresentation induces minor variations in the True positive rates (TPR) of both groups. Boxplots represent the TPR of the advantaged (s = a) and disadvantaged group (s = d) as u varies.

5

---

<!-- Page 6 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Table 4

Model fairness is strongly affected by label bias. Equal Opportunity (EO), as the percentage of flipped positives in the disadvantaged group varies from f = 0 (no bias) to f = 1 (maximum bias). Mean and standard deviation over 10 repetitions. Symbols (*) and (**) denote statistically significant differences with respect to f = 0 at p = .05 and p = .01, respectively, measured with an unpaired t-test.

| Dataset |   | model | EO | EO | f = 1 | f = 1 |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset |   | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.08 ± 0.02 | 0.21 ± 0.02** | 0.52 ± 0.03** | 0.55 ± 0.02* |
| Adult | marital-status | LR | 0.36 ± 0.03 | 0.42 ± 0.04** | 0.62 ± 0.02* | 0.65 ± 0.02** |
| Compas | race | LR | 0.17 ± 0.03 | 0.21 ± 0.05 | 0.21 ± 0.05 | 0.15 ± 0.05 |
| Compas | Crime | LR | 0.33 ± 0.11 | 0.39 ± 0.11 | 0.62 ± 0.17* | 0.67 ± 0.15** |
| Folktables | Folklib04 | LR | 0.05 ± 0.04 | 0.09 ± 0.04 | 0.09 ± 0.04 | 0.09 ± 0.04 |
| Folktables | age | LR | 0.07 ± 0.13 | 0.10 ± 0.14 | 0.22 ± 0.16 | 0.25 ± 0.10** |
| NHIH | gender | Decisionet | 0.01 ± 0.02 | 0.09 ± 0.02** | 0.46 ± 0.03** | 0.48 ± 0.01** |
| NHIH | Fitzpatrick17k | vgg16 | 0.09 ± 0.05 | 0.16 ± 0.06* | 0.21 ± 0.08* | 0.28 ± 0.02** |

Fig. 2. Label bias induces sizeable variations in groupwise true positive rates (TPR); the disadvantaged group f especially affected the TPR on the advantaged and disadvantaged group (y axis), as the percentage of disadvantaged group items with flipped labels increases in the training set (x axis).

a large increment in unfairness across the remaining metrics (POP and DP) and models (random forests and SVC).

Zooming in on this result, Fig. 2 depicts the TPR for both sensitive groups on Folktables and NHIH. We observe that label bias has a significant impact on the TPR of the disadvantaged group in both datasets, a trend observed consistently across all 10 evaluated datasets. On the other hand, the impact on the TPR of the advantaged group differs between datasets. Fig. 2 shows a relatively stable TPR for NHIH, while for Folktables, the TPR of the advantaged group decreases with f. Results for the remaining datasets are reported in Tables B.17 and B.16 in the appendix.

Broadly speaking, we distinguish two categories of datasets based on the effect of f on the TPR of the advantaged group. Datasets such as Adult, Crime, Fitzpatrick17k, and NHIH exhibit stable values for the TPR of the advantaged group while the TPR of the disadvantaged group decreases, therefore widening the gap. Conversely, datasets like German and Compas show patterns akin to Folktables, resulting in a less pronounced TPR gap. This diverging behavior is explained in Section 4.4.

On the joint effect of label bias and underrepresentation. Table 4 suggests that even a weak label bias can have a sizeable impact on model fairness. We therefore study the joint effect of a weak label bias (f \in [0, 0.02]) and widely-ranging underrepresentation (u \in [0, 1]). Specifically, Table 5 summarizes the impact of excluding the disadvantaged group from the training set by presenting the difference between fairness under maximum underrepresentation (EO_{\text{max}}) and no underrepresentation (EO_{\text{min}}):

\Delta EO = EO_{\text{max}} - EO_{\text{min}}.

Positive values of \Delta EO indicate that the inclusion of the disadvantaged group in the training set (u = 0) leads to a decrease in the EO metric

and, therefore, a relative improvement in their TPR. We quantify this improvement under no label bias (f = 0) and weak label bias (f = 0.2). As discussed in Section 4.2, underrepresentation of the disadvantaged group in the training set (without label bias) has no clear effect on fairness, as confirmed by the first column of Table 4 (f = 0) displaying both positive and negative values. On the other hand, the second column (f = 0.2) consistently displays negative values (with the exception of NHIH and Compas). This means that, in the presence of relatively weak label bias, it may become preferable for the disadvantaged group to be completely omitted from the training set.

Increasing the representation of the disadvantaged group in the training set under these conditions is not only unbeneficial but, can, in some cases, be detrimental.

Interpretation. The results presented in this section underscore the critical importance of precise and well-curated ground truth labels in datasets used for training classification models. Specifically, if the labels associated with one demographic group contain noise due to structural discrimination, this can significantly impact model fairness, thereby exacerbating existing biases. Our findings indicate that model performance for the disadvantaged group is consistently and substantially affected when the input labels for this group are subject to systematic bias. Conversely, label bias against the disadvantaged group has a weaker impact on the advantages group, especially when proxies are strong (see Section 4.4); this discrepancy invariably leads to a fairness decline. Furthermore, we showed that even a small proportion of flipped labels can negatively affect the TPR gap. Overall, this shows that hastily adding disadvantaged groups into training sets without careful label curation can cause more harm than good for the members of those groups.

6

---

<!-- Page 7 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128286

Table 5

In the presence of weak label noise (f = 0.2), it becomes preferable to omit the disadvantaged group from the training set. The table below illustrates the Equal Opportunity difference (EOD) between non-representation and full representation for the disadvantaged group across two scenarios: one without label noise (f = 0) and one with weak label noise (f = 0.2). Negative values indicate a relative decline in the T^* of the disadvantaged group.

| Dataset | sensitive | model | AUC | AUC |
| --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 | f = 0.2 |
| Adult | gender | LR | 0.13 ± 0.07 | -0.01 ± 0.08 |
| Adult | marital-status | LR | -0.07 ± 0.05 | 0.13 ± 0.06 |
| Compas | race | LR | 0.01 ± 0.01 | 0.02 ± 0.04 |
| Crime | race | LR | 0.00 ± 0.17 | -0.11 ± 0.17 |
| Folkliaks | race | LR | 0.00 ± 0.06 | -0.01 ± 0.06 |
| German | age | LR | -0.01 ± 0.15 | -0.09 ± 0.17 |
| NIH | gender | DenseNet | 0.05 ± 0.03 | 0.03 ± 0.03 |
| Fitzpatrick17k | skin type | vgg16 | 0.02 ± 0.07 | -0.05 ± 0.08 |

Table 6

The datasets with strong proxies are most affected by label bias. Strength of proxies for all datasets as measured by AUC across 10 repetitions. We report sample means and standard deviations. The datasets with high AUC values are bold and NIH (bold) display the highest unfairness under label bias (Table 4).

| Dataset | sensitive | model | sAUC |
| --- | --- | --- | --- |
| Adult | gender | LR | 0.9349 ± 0.0025 |
| Adult | marital-status | LR | 0.9895 ± 0.0011 |
| Compas | race | LR | 0.6940 ± 0.0140 |
| Crime | race | LR | 0.9847 ± 0.0074 |
| Folkliaks | race | LR | 0.6825 ± 0.0073 |
| German | age | LR | 0.7939 ± 0.0382 |
| NIH | gender | DenseNet | 0.9979 ± 0.0013 |
| Fitzpatrick17k | skin type | vgg16 | 0.8946 ± 0.0100 |

#### 4.4. Proxies

Setup. In this section, we study the effect of proxies on model fairness. We train classifiers f = f(\theta) to estimate the protected attribute \sigma and we compute their AUC of measure the strength of proxies (sAUC – Eq. (3)). To vary the strength of proxies, we leverage the subtractive protocol introduced in Section 3.4 by iteratively removing the feature that is most correlated with the protected attribute; we train a new classifier on the reduced input space and repeat this process until a random classifier performance is reached. We study proxies in conjunction with label bias (f \in \{0, 1\}).

Results. Table 6 reports sAUC values for all datasets. Based on these values, we distinguish two types of datasets with diverging properties. Datasets show statistical significance (LR) and NIH (bold) have very strong proxies for sensitive attributes (AUC > 0.9). While Compas and Folkliaks have weaker proxies (sAUC < 0.7), indicating less information on sensitive attributes encoded in non-sensitive ones. This division mirrors Table 4, where the four high-proxy datasets have the worst (highest) values for EO under maximum label bias (f = 1) and three out of four – i.e., Adult (gender), Adult (marital-status), and NIH (age) – show statistically significant proxies. Compas and NIH have proxies (f = 0.2). Conversely, the negative effects of label bias are weaker for low-proxy datasets: both Folkliaks and Compas have no significant differences in EO even under maximum label bias (f = 1).

To further investigate this trend, we jointly study label bias and proxies. Fig. 3 depicts EO for Adult (gender) and Folkliaks as the flip factor f increases. Curves with different colors represent input spaces whose number of features is iteratively reduced by one. For both datasets, the impact of flips on EO (summarized by average curve slopes) decreases with sAUC. The decrease is more marked for Adult since it

has stronger proxies and therefore starts from higher sAUC values, as reported in Table 6.

Interpretation. These results prove that the presence of strong proxies amplifies the risk of algorithmic discrimination, particularly under label bias: when sAUC is large, the removal of correlated features can mitigate this risk by reducing the model's reliance on sensitive information. These findings highlight the critical role of proxy strength in exacerbating label bias and influencing the effectiveness of fairness interventions.

#### 5. Bias detection

In this section, we introduce mechanisms for bias detection. We evaluate their ability to highlight the presence of a specific type of bias in the data.

##### 5.1. Methods

We propose three measures to detect the presence of each type of bias in the data. It is worth noting that in the previous section, we used a biased training set to train algorithms and an unbiased test set for the evaluation. In this section, we take the perspective of practitioners looking to evaluate their development dataset \sigma for biases without having access to unbiased data sources. We therefore split \sigma into two parts: distributed training and test sets.

Underrepresentation. We propose the Representation Difference (RD), to measure the underrepresentation of the disadvantaged group.

\text{RD}(\sigma) = \frac{\|\sigma_{\text{train}} - \sigma_{\text{test}}\|}{\|\sigma\|} \cdot \Pr(\sigma \text{ is } a) - \Pr(\sigma \text{ is } \bar{a}) \quad (10)

RD quantifies the difference between the prevalence of the advantaged and disadvantaged groups. RD is a directional measure: positive (negative) values indicate a larger proportion of individuals from the (dis)advantaged group. A group \sigma can be considered fairly represented in \sigma if \text{RD}(\sigma) is within certain limits. For example, practitioners can pick a threshold based on the prevalence of \bar{a} in a target population.

Label Bias. We introduce two measures of systematic label noise: \text{LabelBias}(\sigma, \sigma_{\text{train}}) and \text{LabelBias}(\sigma, \sigma_{\text{test}}). We train a base classifier f = f(\sigma) and evaluate AUC curves distinguishing between sensitive groups. We let p_{\text{true}}(x_j) denote the posterior probabilities obtained by the classifier and we define the cross-dataset AUC of x_j as

\text{sAUC}_j(\sigma_1, \sigma_2) = \text{mean}_{\theta} \left( \sum_{j=1}^n p_{\text{true}}(x_j) \cdot \mathbb{E}_{\theta} [y \in \theta_1, j \in \theta_2] \right),

i.e. the probability that x_j is correctly ranks a positive item from \theta_1 higher than a negative one from \theta_2.

Our first measure, initially introduced by Kallus and Zhou (2019), leverages a partition of \sigma into a disadvantaged set \sigma_d and an advantaged set \sigma_a, computes both measures of cross-dataset AUC, and defines their difference as

\Delta \text{sAUC}_j = \text{sAUC}(\sigma_d, \sigma_a) - \text{sAUC}(\sigma_a, \sigma_d). \quad (11)

4 h(x) takes as input the same features x we used to train f(x).

7

---

<!-- Page 8 -->

M. Cecoon et al.

Expert Systems With Applications 292 (2025) 128266

Fig. 3. Proxies exacerbate the risk of algorithmic discrimination caused by label bias. EO (y axis) increases with label bias f (x axis). This effect is mediated by proxies: weaker proxies (lower \Delta AUC) correspond to a lower slope and a weaker effect of label bias f on fairness.

Positive values indicate that pairs of advantaged positives and disadvantaged negatives are easier to separate correctly than pairs of disadvantaged positives and advantaged negatives.

Next, we define the within-group AUC difference as

\Delta AUC_g = AUC_g(x) - AUC_g(y) \\ = \Pr_{n_0}(p_i(x_i) > p_{j_i}(x_i) | y_i = \Theta, y_j = \Theta) \\ - \Pr_{n_1}(p_i(x_i) > p_{j_i}(x_i) | y_i = \bar{\Theta}, y_j = \bar{\Theta}). \quad (12)

i.e. we compute the AUC for advantaged (x = 0) and disadvantaged items (x = 1) separately and measure their difference. Large absolute values indicate a better separability for one group. Notice that both Eqs. (11) and (12) are directional: positive (negative) values indicate better separability for advantaged (disadvantaged) group.

Finally, we compute Separation Difference (SD) as their average

SD(\sigma) = \frac{\Delta AUC(x) + \Delta AUC(y)}{2} \quad (13)

and employ it in the remainder of this section. We expect label bias to worsen the separability for the disadvantaged group and therefore yield high values of SD.

Proxies. To quantify the information about protected features encoded in non-protected ones, which may act as proxies, we train a classifier h(\cdot) : x \mapsto x to predict sensitive attributes from non-sensitive ones. The classifier's performance is then evaluated using the area under the ROC curve for the s predictor (\sigma AUC).

\sigma AUC(x) = AUC_s(h)(x). \quad (14)

Higher values of this metric indicate a better ability of the classifier to predict the sensitive feature from the non-sensitive one, indicating stronger proxies.

## 5.2. Experiments

Setup. We leverage bias injection mechanisms to test bias detection. We use sf = 0 to train a classifier and part of x to evaluate its performance. We maintain an 80-10-10 train-validation-test split for tabular datasets and NIH and a 70-15-15 split for Fitzpatrick17k. As in Section 4, we sample the disadvantaged group by varying the underrepresentation factor \nu \in \{0, 0.2, 0.8, 1\}.

Similarly, we inject label bias letting the flip factor vary in f \in \{0, 0.2, 0.8, 1\}.5

5 Since extreme values such as \nu = 1 and f = 1 would render computation of SD and AUC infeasible, we replace them with \nu = 0.95 and f = 0.95. It is worth reiterating that, in this section, training sets and test sets are drawn from the same distribution, differently from the previous section, where test sets were unbiased.

Finally, we inject proxies through the additive mechanism presented in Section 3.4. We expand the input space with an additional feature derived as the average of the sensitive attribute s and a normal variable with zero mean and decreasing standard deviation.6 The standard deviation varies to achieve Pearson correlation coefficients between the sensitive attribute and the additional feature of approximately \{0.25, 0.5, 0.75, 1\}. A correlation of 0 corresponds to the baseline scenario with no additional feature, while a correlation of 1 reflects the maximally biased scenario in which the additional feature is identical to the protected attribute.

Results. In Fig. 4, we present bias detection results for Folktalks and NIH. Experimental results for the other datasets are provided in Appendix C. As expected, the bias detection metric specifically captures the type of bias it is designed to identify. The metrics exhibit strong variation in the diagonal panels of Fig. 4, while remaining relatively stable across the remaining panels.

Specifically, underrepresentation is suitably captured by RD increasing linearly in the first column, while SD and \sigma AUC exhibit minor oscillations in their average values. Notice that extreme underrepresentation leads to large variations around mean values for SD and \sigma AUC due to numerical instability (see Footnote 5). In the second column, label bias leads to an increase in SD, while RD and \sigma AUC remain constant. Finally, proxies to increasing strength are detected by \sigma AUC in the third column, while RD and SD remain stable. These trends are consistent across nearly all datasets, except for the SD metric on Compa, whose increase with f is barely noticeable. Overall, these results show the effectiveness of the proposed measures in detecting specific data biases.

Interpretation. After confirming the influence of data bias on algorithmic fairness in the previous section, in this section, we have provided a demonstration of bias detection based on principled measures. Each measure can detect a specific type of data bias. Crucially, their computation requires no access to unbiased test sets, making them widely applicable in practice.

## 5.3. Data bias profile

Based on these measures, we initiate the development of Data Bias Profiles (DBP), an extensible quantitative framework to describe bias biases. We envision that the DBP will be used in fairness work to highlight biases that can lead to discrimination and inform decisions on fairness-enhancing measures. Additionally, DBP is suited to analyze biases in the documentation accompanying a dataset. We position this as an initial but foundational contribution—significant work remains to validate, refine, and extend the DBP into a mature, fully realized

6 For image datasets, the additional proxy is fed to the penultimate layer of the neural network.

8

---

<!-- Page 9 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Fig. 4. The proposed measures capture specific types of bias. Bias detection on Folktales and NIH. Columns correspond to three bias injection mechanisms; rows correspond to bias detection measures. Measures vary when the corresponding bias increases (diagonal) and remain relatively flat with other biases (off-diagonal).

tool. Achieving this vision will require a coordinated effort across the research community to evolve the DBP into a robust and widely adopted quantitative framework.

Fig. 5 demonstrates DBP with a practical use case. On the left, we present DBPs for two datasets. Adult (marital-status) presents considerable label bias and strong proxies. As shown in Section 4, this entails a high proximity of algorithmic discrimination. Folktales, on the other hand, has low label bias and weak proxies, highlighting a contained risk of algorithmic discrimination. This is confirmed by the right panel in Fig. 5, where round markers depict the average unfairness (DP and EO – Eqs. (7) and (8)) for a logistic regression model over ten random splits of the datasets. DBPs also hint at the effectiveness of proxy reduction as a bias mitigation strategy. Tackling the strong proxies in Adult can largely reduce unfairness; Folktales, on the other hand, displays weak proxies and is unlikely to benefit from the same approach. We test this hypothesis by removing from each dataset the feature that is most strongly correlated with the sensitive attribute. Star-shaped markers depict EO and DP for the resulting models in the right panel of Fig. 5. As predicted, proxy removal strongly curbs unfairness on Adult (marital-status), while its effect on Folktales is barely noticeable.

## 6. Discussion

We discuss our results in the broader context of responsible AI. Table 7 summarizes the implications of this work for researchers and practitioners.

Underrepresentation in training is overemphasized. Increasing the prevalence of vulnerable groups in training sets is touted as the key strategy to achieve fairness. In stark contradiction with this credence, Section 4 shows that extreme variations in the prevalence of protected groups have a minor impact on fairness across diverse datasets, machine learning models, and metric choices. First and foremost, we urge practitioners and researchers against using these results as a blanket justification to neglect inclusion efforts. Although challenging, expanding and diversifying datasets in a responsible manner is fundamental for keeping algorithmic systems in check. We provide a more nuanced interpretation. High-quality data from disadvantaged groups annotated with sensitive attributes is likely to be scarce, stemming e.g. from targeted curation efforts. Since including disadvantaged groups in training sets is often unlikely to bring meaningful improvements, we recommend prioritizing this data for reliable system evaluations (rather than training), including

9

---

<!-- Page 10 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Fig. 5. Data bias profiles hint at the risk of algorithmic discrimination and effectiveness of fairness intervention. DBP of Adult (left) and Folktales (center); on the right, model fairness summarized by demographic parity (x axis) and equality of opportunity (y). DBP highlights strong proxies and label bias for Adult (marital status), leading to a high risk of discrimination (red round marker), which can be mitigated with proxy reduction (star-shaped marker). Folktales has weak proxies and label bias, translating into lower unfairness and ineffectiveness of proxy mitigation (blue markers).

#### Table 7

Implications. Takeaways and recommendations for algorithmic fairness researchers (R) and practitioners (P).

| Takeaway | Recommendations |
| --- | --- |
| Underrepresentation in training is overemphasized | (R) Critically reconsider widespread emphasis on underrepresentation (U) Use score annotated data for reliable evaluations |
| Label bias is critical | (R) Research techniques for label bias detection (P) Seek and critically assess multiple target labels |
| Data Bias Profile (DBP) can link data bias & group fairness | (R) Diversify fairness toolbox with DBP (P) Use DBP to select fairness interventions (P) Include DBP in data documentation |

measurements of algorithmic fairness. If fairness evaluations yield problematic results, practitioners should carry out an assessment of multiple bias factors that go beyond underrepresentation.

Label bias is critical. Systematic bias against vulnerable groups in target variables (in short: label bias) is a common cause due to structural societal differences. Section 4 shows that label bias has a major impact on fairness across diverse metrics, models, and datasets as well as significant interactions with other types of data bias. For example, in the presence of label bias, increasing training set representation can have a detrimental effect on vulnerable groups. In this setting, underrepresentation may actually benefit vulnerable groups, challenging common wisdom. Notice that label bias is especially critical because there is a high risk it will go undetected if models are trained and evaluated with datasets that exhibit the same bias (e.g. identically distributed training and test sets). Based on these findings, we make two recommendations. Practitioners should seek multiple target variables for their models and carefully choose the most suitable one(s) to minimize the potential for label bias. This effort should blend qualitative approaches grounded in domain expertise with quantitative approaches for bias detection. In concert, researchers should develop reliable techniques for label bias detection. Section 5 is a first step in this direction. Data Bias Profiles (DBP) can link label bias and Bias. Overall, this work contributes a list of independent data biases with mechanisms to study them (Section 3), a study of their joint influence on fairness

(Section 4), and principled methods for bias quantification (Section 5). Building upon these contributions, we advocate a broader community effort to develop the Data Bias Profile (DBP), as a first attempt to summarize key bias indicators in a unified format. Rather than presenting a finalized framework, we offer an extensible prototype. In their current form, DBPs are brief summaries of dataset-level aggregate bias quantification methods for a principled analysis of fairness problems guided by data. Model developers should use DBPs to reason about sources of model unfairness and select tailored approaches for mitigation. For example, detecting strong label bias may direct a developer towards fairness interventions for target label repair. Additionally, DBPs can develop into reference documentation frameworks that practitioners will use to comply with data governance requirements, including bias detection provisions specified in the AI Act. From a research standpoint, the DBP offers promising directions. DBPs can guide the development of fairness benchmarks, i.e. standardized collections to evaluate alternative fairness algorithms. For example, datasets can be distinguished based on the presence of strong proxies and weak proxies.

As we have shown, both vanilla algorithms (solely focused on accuracy) and fairness interventions behave differently based on the strength of proxies encoded in non-sensitive features. Fairness testbeds should thus include both strong-proxy and weak-proxy datasets to evaluate models under diverse conditions.

Finally, DBPs may bridge hundreds of fairness algorithms (Hort, Chen, Zhang, Harman, & Sarro, 2024) and datasets (Fabris et al., 2022), by helping to answer the key question: given a model that produces unfair predictions on a dataset, which type of fairness-enhancing algorithm is most suitable for that type of data and algorithm?

#### 6.1. Limitations

This study has some limitations. First, we only cover three types of data bias. Although these are the most cited in scholarly articles and technical reports, different types of data bias are possible (Bannoun et al., 2023; Mehrafi et al., 2022). Future work should consider additional biases, including feature bias, omitted variable bias, and concept drift across protected groups. Second, we consider binary protected attributes. While our results generalize to multi-group attributes by casting them as one-s-all problems, this may become impractical for large cardinality [5]. Natively catering to multi-group attributes will require careful design of fairness metrics and algorithms to distinguish between mild and excessive bias with our detection mechanisms. In its current form, the DBP is useful for relative comparisons across datasets;

10

---

<!-- Page 11 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

it will need further refinement to support thresholding. Fourth, while we experiment with popular and diverse fairness datasets, this is unlikely to be exhaustive of all settings encountered in practice. Future work should include additional datasets, with special attention to datasets with complementary properties. Finally, we note that it may be impossible to distinguish proper data bias, i.e. a shift between the data and a target population, from situations where the data is “uncorrupted,” yet naturally encodes groupwise differences. Our work contributes a principled way to link numerical data properties with algorithmic fairness properties. Arguments on the source of those numerical properties are extremely valuable and complement our contributions.

## 7. Conclusion

Data biases are key drivers of algorithmic discrimination. While this fact is broadly recognized, their relative importance and interaction remain understudied. In this paper, we work with a systematic study of bias conduction factors, their influence on algorithmic discrimination, and their detection through dedicated mechanisms. These are necessary steps to stop a shared lesson to describe data bias, document it unambiguously, and link it to fairness interventions in a principled fashion.

To realize these goals, we call for a community-wide effort to expand, formalize, and critically assess the Data Bias Profile, paving the way for a shared and trustworthy approach to quantitative bias documentation.

This line of work will be critical to steer anti-discrimination policy toward technically meaningful standards and to translate algorithmic fairness research into law-abiding practice.

## CRediT authorship contribution statement

Marina Ceccon: Conceptualization, Formal analysis, Investigation, Writing – original draft, Writing – review & editing, Methodology, Software; Giandomenico Cornacchia: Conceptualization, Formal analysis, Investigation, Writing – original draft, Writing – review & editing, Methodology, Data curation; Diego Dalle Pozze: Conceptualization, Formal analysis, Investigation, Writing – original draft, Writing – review & editing, Methodology; Alessandro Fabris: Conceptualization, Formal analysis, Investigation, Writing – original draft, Writing – review & editing, Methodology, Supervision; Gian Antonio Susto: Conceptualization, Formal analysis, Investigation, Writing – original draft, Writing – review & editing, Methodology, Supervision.

## Data availability

Data will be made available on request.

## Declaration of interests

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

Marina Ceccon and Gian Antonio Susto reports financial support was provided by Ministry of Education and Merit. Alessandro Fabris reports financial support was provided by Alexander von Humboldt Foundation. Gian Antonio Susto reports that he has other author agreements that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was supported by the Alexander von Humboldt Foundation and FINDR. The authors would like to thank the following for their support: ID: 101070212 (A. Fabris) and by Ministero dell’Università della Ricerca (MUR), iniziativa Dottorati PON (M. Ceccon, G.A. Susto).

## Appendix A. Datasets

In this paper, we present algorithmic fairness datasets and their processing in this work. Sensitive features (s) that are used for fairness evaluations are excluded from input features.

Adult1: is a prominent dataset hosted by the UCI Machine Learning Repository, originally derived from the 1994 US Census database (Kohavi, 1996). The primary objective of this dataset is to predict whether an individual’s annual income exceeds $50,000. We follow Domini, Oneto, Ben-David, Shawe-Taylor, and Pontil (2018), keeping all the features in the dataset. We use gender and marital-status as sensitive attributes.

Compas2 comprises data from the COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) algorithm, a commercial tool used to predict recidivism among convicted individuals. The original dataset is used to audit the COMPAS system, surfaced discrimination against African-American defendants. We follow the pre-processing from Russo, Balunovic, Fischer, and Vecchey (2020) and use the following variables.

- •age:age of the defendant.
- •c_charge_degree:charge degree (F: Felony, M: Misdemeanor).
- •diff_custody:time spent in custody.
- •diff_time_in_custody:time spent in jail.
- •sex:sex of the defendant.
- •priors_count:number of prior criminal records.
- •length_of_stay_in_custody:length of stay in jail.
- •v_score_text:COMPAS quantized score, summarizing additional features used by model but unavailable in the data collected by ProPublica.

The target variable is two year recid, indicating whether an individual re-offended within 2 years of the first offense. Protected attributes, we focus on race, distinguishing between Caucasian (advantaged group) and African-American defendants (disadvantaged group).

Crime3 is a real-world dataset from the UCI Machine Learning Repository, based on predicting violent crime rates across various communities in the US. The task involves predicting whether a community can be classified as violent based on its crime rates, specifically when the number of crime rates is above the median value of crimes across all states. We follow the setup from Balunovic, Russo, and Vecchey (2022), including binarized race as a sensitive attribute. We keep all the non-sensitive features for inference (s = 127).

Feedback4 is a Python package designed to provide access to datasets derived from the US Census Bureau’s American Community Survey (ACS) (Ding, Hardt, Miller, & Schmidt, 2021). The complete data sources are available for download for all ACS years, full ACS data, spanning all US states, multiple years, and prediction targets. In this work, we focus on the employment prediction task (ACSEmployment), filtering the data to include individuals aged between 16 and 90. We subsample at 1 % of the dataset size, stratifying on the target and sensitive label to maintain the distribution of the original data. We use the standard data loader keeping the following features:

- •ESR:employment status of the individual, represented as a binary categorical feature (1: Employed, 0: Otherwise).
- •RACP (1):detailed race record (categorical values 1–9).
- •AGEPC:age in years, with a maximum value of 99.
- •ANC:ancestry record (categorical).
- •CIT:citizenship status of the individual, represented as a categorical string.

1 https://archive.ics.uci.edu/dataset/2/adult

2 https://github.com/propublica/compas-analysis

3 https://archive.ics.uci.edu/dataset/183/compas+and+crime

4 https://github.com/socialfoundations/feedback

11

---

<!-- Page 12 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128286

- • DEAR: hearing difficulty (binary).
- • DEVI: vision difficulty (binary).
- • DIS: disability recode (1: citizen with disability, 2: without).
- • DREM: cognitive difficulty of the individual, indicating if they have difficulty remembering, concentrating, or making decisions (binary).
- • ESP: employment status of parents (categorical).
- • MAR: marital status of the individual (categorical).
- • MIG: Mobility status, indicating residence one year ago (categorical).
- • MIL: military service (binary).
- • NATIVITY: binary variable indicating US native or foreign-born.
- • RELP: relationship (categorical values 1–17).
- • SEX: sex/categorical, along with the loan approval values 1–24, or NA).
- • SEX: sex/Gender (1: Male, 2: Female).

The Employment Status Records (ESR) is the target variable (equal to 1 if employed, 0 otherwise). The advantaged group consists of individuals with RACIP equal to 1 (Caucasian), while the disadvantaged group includes all individuals with RACIP values other than 1 (other races). The dataset is annotated by a recognized dataset from the UCI Machine Learning Repository, encompassing records of bank loan applications in Germany. This dataset contains demographic and financial details of individuals, along with the loan approval outcomes. The primary prediction task is binary, aimed at determining creditworthiness based on loan repayment. We use the following features:

- • age (*): The age of the applicant, binarized with a 25-year threshold.
- • amount: credit amount in Deutsche Mark.
- • credit_history: history of credit usage and repayment by the applicant (categorical).
- • duration: duration of the loan in months (numeric).
- • employment_duration: tenure with current employer (numeric).
- • housing: type of housing (categorical).
- • installment_rate: percentage of applicant's income allocated to loan installments (categorical).
- • job_applicant's job and employability (categorical).
- • number_of_credit_checks: number of checks on this bank (categorical).
- • other_debtors: indication of an additional debtor or a guarantor for the credit (categorical).
- • other_installment_plans: installment plans with other banks (categorical).
- • people_liable: number of people who are financially dependent on the applicant (categorical).
- • property: applicant's most valuable property (categorical).
- • purpose: purpose of loan (categorical).
- • present_residence: years lived at current address (categorical).
- • savings: savings account balance (categorical).
- • status: status of the individual's saving accounts (categorical).
- • telephone: whether the applicant has a registered telephone line.

ChestX-ray-14 (NIH)12 is a comprehensive medical imaging dataset containing 112,120 frontal-view chest X-ray images from 30,805 unique patients, collected between 1992 and 2015 (Wang et al., 2017). Disease labels for 100 most common thoracic conditions were extracted from radiological reports using natural language processing.

The labeled conditions include: atelectasis, cardiomegaly, consolidation, emphysema, effusion, hyperpnea, hernia, infarction, interstitial mass, nodule, pneumonia, pneumothorax. The associated classification task is multi-label, with each of the 14 target labels indicating the presence of a specific disease. Additionally, patient metadata provides information on both gender and age.

We include only one image per patient, as previous studies have shown that this approach reduces bias without significantly affecting overall performance (Wong, Bipladi, Persson, & Fenzag, 2023). We conduct evaluations independently for each disease and report macro-averaged metrics across all diseases. In this study, binary gender is the secondary target variable.

Fitzpatrick17K13 is a medical imaging dataset containing 16,577 clinical images (Groh et al., 2021), each annotated with labels for skin conditions and skin type based on the Fitzpatrick scale (Fitzpatrick, 1988). The images were sourced from two open-access dermatology atlases: 12,672 images from DermaAmm and 3905 from Atlas Dermatologic14. The dataset includes 114 distinct disease labels and two additional labels for skin type and skin conditions, respectively, structured according to the skin lesion taxonomy proposed by Esteva et al. (2017). At the broadest classification level, skin conditions are divided into three main categories: benign lesions, malignant lesions and non-neoplastic lesions. In a more detailed classification, skin conditions are categorized into nine types: inflammatory, malignant epidermal, genodermatoses, benign dermal, benign epidermal, malignant melanoma, benign melanocyte, benign cutaneous lymphoma, malignant dermal. Our classification task is based on a binary variable derived from the highest-level skin condition classification, distinguishing between neoplastic, hence tumoral (either benign or malignant), and non-neoplastic diseases. This mimics a preliminary assessment for the presence of tumoral conditions through assistive technology used by dermatology experts. The Fitzpatrick skin type labels follow a six-point scale, with 1 being the lightest and 6 the darkest skin type. We binarize them into light (1–4) and very dark (5–6).

## Appendix B. Additional results on the effect of data bias

In this section, we report the effect of data bias on all machine learning models, datasets, and metrics. Specifically, performance is evaluated through balanced accuracy (Tables B.8 and B.14), while fairness is assessed through prediction quality parity (PQP – Tables B.9 and B.15), equal opportunity (EO – Tables B.12 and B.18), and demographic parity (DP – Tables B.13 and B.19). We zoom in on EO by breaking it down into groupwise true positive rate (TPR – Tables B.10, B.11, B.16, and B.17) components. We provide results for underrepresentation (Appendix B.1) and label bias (Appendix B.2).

As in Section A, the tables include indicators of statistical significance: symbols (*) and (**) denote statistically significant differences with respect to the unbiased scenario thresholds at p = .05 and p = .01, respectively.

### B.1. Underrepresentation

#### B.2. Label bias

11 https://archive.ics.uci.edu/dataset/522/soth-german+credit

12 https://nihbe.app.com/v/X/ChestX-ray-NIHC

13 https://github.com/mattgroh/fitzpatrick17k

14 https://atlasdermatologico.com.br

12

---

<!-- Page 13 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Table B.8

Balanced accuracy varying the percentage of minority-group points retained in the training set from 
u = 0
 (no bias) to 
u = 1
 (maximum bias).

| Dataset | sensitive | model | Balanced Accuracy | Balanced Accuracy | Balanced Accuracy | Balanced Accuracy |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.77 ± 0.00 | 0.77 ± 0.00 | 0.77 ± 0.00 | 0.76 ± 0.01* |
| Adult | gender | RF | 0.78 ± 0.00 | 0.78 ± 0.01 | 0.78 ± 0.00 | 0.77 ± 0.01* |
| Adult | gender | SVC | 0.77 ± 0.01 | 0.77 ± 0.01 | 0.77 ± 0.01 | 0.76 ± 0.01 |
| Adult | marital-status | LR | 0.77 ± 0.00 | 0.77 ± 0.00 | 0.77 ± 0.00 | 0.77 ± 0.00 |
| Adult | marital-status | RF | 0.78 ± 0.00 | 0.78 ± 0.00 | 0.78 ± 0.00 | 0.78 ± 0.01 |
| Adult | marital-status | SVC | 0.77 ± 0.01 | 0.77 ± 0.01 | 0.77 ± 0.01 | 0.77 ± 0.01 |
| Compas | race | LR | 0.67 ± 0.02 | 0.67 ± 0.02 | 0.67 ± 0.01 | 0.67 ± 0.01 |
| Compas | race | RF | 0.69 ± 0.02 | 0.69 ± 0.01 | 0.69 ± 0.02 | 0.68 ± 0.02 |
| Compas | race | SVC | 0.65 ± 0.03 | 0.65 ± 0.02 | 0.65 ± 0.02 | 0.65 ± 0.01 |
| Compas | race | LR | 0.84 ± 0.02 | 0.84 ± 0.02 | 0.83 ± 0.02 | 0.83 ± 0.02 |
| Crime | race | RF | 0.83 ± 0.03 | 0.84 ± 0.03 | 0.83 ± 0.02 | 0.81 ± 0.03 |
| Crime | race | SVC | 0.84 ± 0.02 | 0.84 ± 0.02 | 0.83 ± 0.02 | 0.83 ± 0.03 |
| Crime | race | LR | 0.73 ± 0.01 | 0.73 ± 0.01 | 0.73 ± 0.01 | 0.73 ± 0.01 |
| Crime | race | RF | 0.78 ± 0.00 | 0.78 ± 0.01 | 0.77 ± 0.01* | 0.78 ± 0.00 |
| Folktables | race | SVC | 0.72 ± 0.01 | 0.72 ± 0.01 | 0.72 ± 0.01 | 0.72 ± 0.01 |
| Folktables | race | LR | 0.66 ± 0.06 | 0.65 ± 0.05 | 0.64 ± 0.07 | 0.65 ± 0.05 |
| Folktables | race | RF | 0.68 ± 0.06 | 0.68 ± 0.05 | 0.65 ± 0.05 | 0.64 ± 0.05 |
| German | age | SVC | 0.66 ± 0.07 | 0.66 ± 0.07 | 0.63 ± 0.06 | 0.63 ± 0.06 |
| German | age | LR | 0.64 ± 0.01 | 0.64 ± 0.02 | 0.64 ± 0.02 | 0.63 ± 0.02 |
| NIH Fitzpatrick17k | gender skin type | DeepNet | 0.70 ± 0.01 | 0.70 ± 0.01** | 0.70 ± 0.02 | 0.70 ± 0.02** |
| NIH Fitzpatrick17k | gender skin type | vgg16 | 0.73 ± 0.01 | 0.73 ± 0.01 | 0.73 ± 0.02 | 0.73 ± 0.02** |

Table B.9

Prediction quality parity (PQP) varying the percentage of minority-group points retained in the training set from 
u = 0
 (no bias) to 
u = 1
 (maximum bias).

| Dataset | sensitive | model | PQP | PQP | PQP | PQP |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.00 ± 0.01 | 0.00 ± 0.01 | 0.01 ± 0.01 | 0.06 ± 0.03** |
| Adult | gender | RF | 0.01 ± 0.01 | 0.01 ± 0.01 | 0.02 ± 0.01 | 0.11 ± 0.01** |
| Adult | gender | SVC | 0.01 ± 0.01 | 0.01 ± 0.01 | 0.01 ± 0.01 | 0.08 ± 0.01** |
| Adult | marital-status | LR | 0.09 ± 0.01 | 0.09 ± 0.02 | 0.09 ± 0.02 | 0.06 ± 0.02** |
| Adult | marital-status | RF | 0.08 ± 0.01 | 0.08 ± 0.01 | 0.09 ± 0.01 | 0.02 ± 0.02** |
| Adult | marital-status | SVC | 0.08 ± 0.02 | 0.09 ± 0.02 | 0.08 ± 0.02 | 0.06 ± 0.01* |
| Compas | race | LR | -0.06 ± 0.03 | -0.06 ± 0.03 | -0.06 ± 0.04 | -0.06 ± 0.04 |
| Compas | race | RF | -0.01 ± 0.05 | -0.02 ± 0.05 | -0.02 ± 0.05 | -0.02 ± 0.04 |
| Compas | race | SVC | -0.05 ± 0.03 | -0.05 ± 0.04 | -0.06 ± 0.03 | -0.06 ± 0.04 |
| Crime | race | LR | -0.02 ± 0.08 | -0.01 ± 0.09 | -0.04 ± 0.10 | -0.06 ± 0.10 |
| Crime | race | RF | -0.03 ± 0.05 | -0.04 ± 0.09 | -0.04 ± 0.07 | -0.08 ± 0.07 |
| Crime | race | SVC | -0.03 ± 0.08 | 0.01 ± 0.06 | -0.05 ± 0.05 | -0.06 ± 0.06 |
| Folktables | race | LR | 0.01 ± 0.04 | 0.01 ± 0.04 | 0.02 ± 0.04 | 0.02 ± 0.04 |
| Folktables | race | RF | 0.01 ± 0.03 | 0.00 ± 0.03 | 0.01 ± 0.03 | 0.01 ± 0.03 |
| Folktables | race | SVC | 0.02 ± 0.03 | 0.02 ± 0.03 | 0.02 ± 0.03 | 0.02 ± 0.03 |
| German | age | LR | 0.07 ± 0.13 | 0.05 ± 0.09 | 0.08 ± 0.08 | 0.08 ± 0.10 |
| German | age | RF | -0.01 ± 0.07 | 0.02 ± 0.07 | 0.06 ± 0.05 | 0.04 ± 0.08 |
| German | age | SVC | 0.03 ± 0.10 | 0.03 ± 0.08 | 0.02 ± 0.10 | 0.02 ± 0.09 |
| NIH Fitzpatrick17k | gender skin type | DeepNet | -0.01 ± 0.01 | 0.00 ± 0.01 | 0.01 ± 0.01** | 0.02 ± 0.01** |
| NIH Fitzpatrick17k | gender skin type | vgg16 | -0.01 ± 0.01 |   |   |   |

---

<!-- Page 14 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 123626

**Table B.10**

True positive rate (TPR) of the advantaged group varying the percentage of minority-group points retained in the training set from 
u = 0
 (no bias) to 
u = 1
 (maximum bias).

| Dataset | sensitive | model | TPR ( u = a ) | TPR ( u = a ) | TPR ( u = a ) | TPR ( u = a ) |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.61 ± 0.01 | 0.62 ± 0.01 | 0.62 ± 0.01 | 0.62 ± 0.01 |
| Adult | gender | RF | 0.64 ± 0.01 | 0.63 ± 0.01 | 0.64 ± 0.01 | 0.63 ± 0.01 |
| Adult | gender | SVC | 0.61 ± 0.01 | 0.61 ± 0.01 | 0.61 ± 0.01 | 0.61 ± 0.01 |
| Adult | marital-status | LR | 0.65 ± 0.01 | 0.65 ± 0.01 | 0.65 ± 0.01 | 0.66 ± 0.01 |
| Adult | marital-status | RF | 0.66 ± 0.01 | 0.63 ± 0.01 | 0.66 ± 0.01 | 0.67 ± 0.01 |
| Adult | marital-status | SVC | 0.64 ± 0.01 | 0.64 ± 0.01 | 0.65 ± 0.01 | 0.66 ± 0.01** |
| Compas | race | LR | 0.85 ± 0.02 | 0.86 ± 0.01 | 0.87 ± 0.02 | 0.88 ± 0.02* |
| Compas | race | RF | 0.81 ± 0.03 | 0.81 ± 0.02 | 0.81 ± 0.02 | 0.81 ± 0.03 |
| Compas | race | SVC | 0.85 ± 0.04 | 0.86 ± 0.05 | 0.91 ± 0.02** | 0.92 ± 0.02** |
| Crime | race | LR | 0.90 ± 0.04 | 0.90 ± 0.04 | 0.89 ± 0.04 | 0.91 ± 0.04 |
| Crime | race | RF | 0.90 ± 0.03 | 0.90 ± 0.03 | 0.91 ± 0.03 | 0.92 ± 0.03 |
| Crime | race | SVC | 0.91 ± 0.04 | 0.91 ± 0.03 | 0.91 ± 0.03 | 0.92 ± 0.03 |
| Folknables | race | LR | 0.83 ± 0.01 | 0.83 ± 0.01 | 0.83 ± 0.01 | 0.83 ± 0.01 |
| Folknables | race | RF | 0.85 ± 0.01 | 0.86 ± 0.01 | 0.86 ± 0.01 | 0.86 ± 0.01 |
| Folknables | race | SVC | 0.85 ± 0.01 | 0.85 ± 0.01 | 0.85 ± 0.01 | 0.85 ± 0.01 |
| German | age | LR | 0.89 ± 0.05 | 0.89 ± 0.05 | 0.91 ± 0.05 | 0.91 ± 0.05 |
| German | age | RF | 0.93 ± 0.02 | 0.91 ± 0.04 | 0.93 ± 0.02 | 0.92 ± 0.06 |
| German | age | SVC | 0.93 ± 0.02 | 0.92 ± 0.02 | 0.93 ± 0.04 | 0.94 ± 0.04 |
| NHI Fitzpatrick17k | gender | DenseNet | 0.46 ± 0.03 | 0.49 ± 0.02 | 0.45 ± 0.05 | 0.45 ± 0.04 |
| NHI Fitzpatrick17k | skin type | vgg16 | 0.70 ± 0.02 | 0.68 ± 0.02 | 0.68 ± 0.01* | 0.69 ± 0.01 |

**Table B.11**

True positive rate (TPR) of the disadvantaged group varying the percentage of minority-group points retained in the training set from 
u = 0
 (no bias) to 
u = 1
 (maximum bias).

| Dataset | sensitive | model | TPR ( u = d ) | TPR ( u = d ) | TPR ( u = d ) | TPR ( u = d ) |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.53 ± 0.02 | 0.53 ± 0.02 | 0.53 ± 0.02 | 0.41 ± 0.07** |
| Adult | gender | RF | 0.54 ± 0.02 | 0.54 ± 0.02 | 0.52 ± 0.03 | 0.34 ± 0.03** |
| Adult | gender | SVC | 0.53 ± 0.02 | 0.53 ± 0.02 | 0.51 ± 0.03 | 0.36 ± 0.04** |
| Adult | marital-status | LR | 0.29 ± 0.03 | 0.29 ± 0.03 | 0.29 ± 0.03 | 0.27 ± 0.03** |
| Adult | marital-status | RF | 0.35 ± 0.03 | 0.34 ± 0.03 | 0.33 ± 0.02 | 0.31 ± 0.04** |
| Adult | marital-status | SVC | 0.30 ± 0.03 | 0.30 ± 0.03 | 0.31 ± 0.03 | 0.39 ± 0.02** |
| Compas | race | LR | 0.68 ± 0.03 | 0.68 ± 0.03 | 0.71 ± 0.03 | 0.72 ± 0.02** |
| Compas | race | RF | 0.66 ± 0.03 | 0.67 ± 0.03 | 0.68 ± 0.04 | 0.70 ± 0.03** |
| Compas | race | SVC | 0.68 ± 0.06 | 0.69 ± 0.07 | 0.76 ± 0.05* | 0.78 ± 0.03** |
| Crime | race | LR | 0.57 ± 0.10 | 0.54 ± 0.12 | 0.59 ± 0.14 | 0.63 ± 0.13 |
| Crime | race | RF | 0.57 ± 0.07 | 0.58 ± 0.10 | 0.62 ± 0.08 | 0.75 ± 0.09** |
| Crime | race | SVC | 0.59 ± 0.08 | 0.55 ± 0.08 | 0.61 ± 0.07 | 0.63 ± 0.09 |
| Folknables | race | LR | 0.79 ± 0.04 | 0.79 ± 0.04 | 0.78 ± 0.04 | 0.78 ± 0.05 |
| Folknables | race | RF | 0.83 ± 0.03 | 0.84 ± 0.04 | 0.85 ± 0.03 | 0.84 ± 0.04 |
| Folknables | race | SVC | 0.80 ± 0.04 | 0.81 ± 0.04 | 0.81 ± 0.04 | 0.81 ± 0.03 |
| German | age | LR | 0.82 ± 0.13 | 0.82 ± 0.12 | 0.84 ± 0.10 | 0.85 ± 0.09 |
| German | age | RF | 0.90 ± 0.07 | 0.87 ± 0.07 | 0.90 ± 0.07 | 0.89 ± 0.07 |
| German | age | SVC | 0.87 ± 0.09 | 0.89 ± 0.09 | 0.92 ± 0.10 | 0.90 ± 0.11 |
| NHI Fitzpatrick17k | gender | DenseNet | 0.44 ± 0.05 | 0.45 ± 0.03 | 0.42 ± 0.04 | 0.39 ± 0.03* |
| NHI Fitzpatrick17k | skin type | vgg16 | 0.61 ± 0.05 | 0.58 ± 0.0 |   |   |

---

<!-- Page 15 -->

M. Cecon et al.

Expert Systems With Applications 292 (2025) 123626

**Table B.12**

Equal opportunity (EO) varying the percentage of minority-group points retained in the training set from u = 0 (no bias) to u = 1 (maximum bias).

| Dataset | sensitive | model | EO | EO | EO | EO |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.08 ± 0.02 | 0.09 ± 0.02 | 0.09 ± 0.02 | 0.21 ± 0.07** |
| Adult | gender | RF | 0.10 ± 0.02 | 0.09 ± 0.02 | 0.12 ± 0.03 | 0.36 ± 0.03** |
| Adult | gender | SVC | 0.08 ± 0.02 | 0.08 ± 0.02 | 0.10 ± 0.03 | 0.25 ± 0.03** |
| Adult | marital-status | LR | 0.36 ± 0.03 | 0.36 ± 0.03 | 0.37 ± 0.03 | 0.29 ± 0.04** |
| Adult | marital-status | RF | 0.31 ± 0.03 | 0.31 ± 0.03 | 0.31 ± 0.03 | 0.16 ± 0.05** |
| Adult | marital-status | SVC | 0.34 ± 0.03 | 0.34 ± 0.03 | 0.34 ± 0.03 | 0.27 ± 0.02** |
| Compas | race | LR | 0.17 ± 0.03 | 0.17 ± 0.03 | 0.16 ± 0.02 | 0.16 ± 0.02 |
| Compas | race | RF | 0.15 ± 0.05 | 0.14 ± 0.04 | 0.13 ± 0.04 | 0.11 ± 0.05 |
| Compas | race | SVC | 0.18 ± 0.04 | 0.17 ± 0.04 | 0.15 ± 0.04 | 0.13 ± 0.03** |
| Compas | crime | LR | 0.33 ± 0.11 | 0.36 ± 0.12 | 0.30 ± 0.14 | 0.28 ± 0.13 |
| Compas | crime | RF | 0.33 ± 0.06 | 0.32 ± 0.11 | 0.29 ± 0.08 | 0.16 ± 0.09** |
| Compas | crime | SVC | 0.32 ± 0.08 | 0.36 ± 0.09 | 0.30 ± 0.07 | 0.31 ± 0.07 |
| Folktables | race | LR | 0.05 ± 0.04 | 0.05 ± 0.04 | 0.05 ± 0.04 | 0.05 ± 0.04 |
| Folktables | race | RF | 0.02 ± 0.04 | 0.02 ± 0.03 | 0.02 ± 0.03 | 0.02 ± 0.04 |
| Folktables | race | SVC | 0.04 ± 0.03 | 0.04 ± 0.04 | 0.04 ± 0.03 | 0.04 ± 0.03 |
| Folktables | race | LR | 0.07 ± 0.13 | 0.06 ± 0.11 | 0.07 ± 0.09 | 0.06 ± 0.07 |
| German | age | RF | 0.03 ± 0.06 | 0.03 ± 0.06 | 0.03 ± 0.07 | 0.03 ± 0.08 |
| German | age | SVC | 0.06 ± 0.08 | 0.05 ± 0.08 | 0.01 ± 0.08 | 0.04 ± 0.08 |
| German | age | LR | 0.01 ± 0.02 | 0.04 ± 0.01** | 0.03 ± 0.02 | 0.06 ± 0.02** |
| Flitzpatrick17k | gender skin type | DenseNet vgg16 | 0.09 ± 0.05 | 0.11 ± 0.06 | 0.11 ± 0.05 | 0.11 ± 0.05 |

**Table B.13**

Demographic parity (DP) varying the percentage of minority-group points retained in the training set from u = 0 (no bias) to u = 1 (maximum bias).

| Dataset | sensitive | model | DP | DP | DP | DP |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | u = 0 (no bias) | u = 0.2 | u = 0.8 | u = 1 (max bias) |
| Adult | gender | LR | 0.18 ± 0.01 | 0.18 ± 0.01 | 0.18 ± 0.01 | 0.20 ± 0.01** |
| Adult | gender | RF | 0.18 ± 0.01 | 0.18 ± 0.01 | 0.18 ± 0.01 | 0.21 ± 0.01** |
| Adult | gender | SVC | 0.17 ± 0.00 | 0.17 ± 0.00 | 0.18 ± 0.01* | 0.20 ± 0.01** |
| Adult | marital-status | LR | 0.37 ± 0.01 | 0.37 ± 0.01 | 0.38 ± 0.01 | 0.36 ± 0.02 |
| Adult | marital-status | RF | 0.36 ± 0.02 | 0.35 ± 0.02 | 0.36 ± 0.01 | 0.31 ± 0.02** |
| Adult | marital-status | SVC | 0.36 ± 0.01 | 0.36 ± 0.01 | 0.36 ± 0.01 | 0.34 ± 0.01** |
| Compas | race | LR | 0.26 ± 0.03 | 0.27 ± 0.03 | 0.26 ± 0.03 | 0.25 ± 0.03 |
| Compas | race | RF | 0.21 ± 0.05 | 0.20 ± 0.04 | 0.19 ± 0.04 | 0.17 ± 0.05 |
| Compas | race | SVC | 0.26 ± 0.02 | 0.25 ± 0.02 | 0.23 ± 0.02* | 0.22 ± 0.03** |
| Compas | race | LR | 0.62 ± 0.06 | 0.63 ± 0.05 | 0.61 ± 0.05 | 0.61 ± 0.05 |
| Crime | race | RF | 0.62 ± 0.07 | 0.63 ± 0.07 | 0.61 ± 0.06 | 0.53 ± 0.07** |
| Crime | race | SVC | 0.62 ± 0.07 | 0.62 ± 0.06 | 0.61 ± 0.05 | 0.63 ± 0.06 |
| Crime | race | LR | 0.06 ± 0.03 | 0.06 ± 0.03 | 0.06 ± 0.03 | 0.06 ± 0.03* |
| Folktables | race | RF | 0.05 ± 0.03 | 0.05 ± 0.03 | 0.04 ± 0.04 | 0.04 ± 0.03 |
| Folktables | race | SVC | 0.06 ± 0.03 | 0.06 ± 0.03 | 0.05 ± 0.02 | 0.05 ± 0.02 |
| Folktables | race | LR | 0.06 ± 0.13 | 0.07 ± 0.09 | 0.04 ± 0.09 | 0.04 ± 0.08 |
| German | age | RF | 0.09 ± 0.08 | 0.07 ± 0.08 | 0.03 ± 0.09 | 0.04 ± 0.08 |
| German | age | SVC | 0.09 ± 0.10 | 0.06 ± 0.09 | 0.04 ± 0.07 | 0.07 ± 0.04 |
| German | age | LR | 0.00 ± 0.00 | 0.01 ± 0.00** | 0.01 ± 0.01* | 0.01 ± 0.01** |
| Flitzpatrick17k | gender skin type | DenseNet vgg16 | 0.15 ± 0.02 | 0.15 ± 0.02* | 0.11 ± 0.02** | 0.09 ± 0.02 |

---

<!-- Page 16 -->

M. Cecon et al.

Expert Systems With Applications 292 (2025) 128266

Table B.14Balanced accuracy as the percentage of flipped positives in the disadvantaged group varies from f = 0 (no bias) to f = 1 (maximum bias).

| Dataset | sensitive | model | Balanced Accuracy | Balanced Accuracy | Balanced Accuracy | Balanced Accuracy |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.77 ± 0.001 | 0.76 ± 0.01* | 0.73 ± 0.001* | 0.73 ± 0.001* |
| Adult | gender | RF | 0.78 ± 0.00 | 0.77 ± 0.01* | 0.74 ± 0.01** | 0.74 ± 0.00** |
| Adult | gender | SVC | 0.77 ± 0.01 | 0.76 ± 0.01 | 0.73 ± 0.01** | 0.73 ± 0.01** |
| Adult | gender | LR | 0.77 ± 0.00 | 0.76 ± 0.01* | 0.75 ± 0.01** | 0.75 ± 0.01** |
| Adult | marital-status | RF | 0.78 ± 0.00 | 0.77 ± 0.00** | 0.75 ± 0.00** | 0.75 ± 0.00** |
| Adult | marital-status | SVC | 0.77 ± 0.01 | 0.76 ± 0.01 | 0.75 ± 0.01** | 0.75 ± 0.01** |
| Adult | marital-status | LR | 0.67 ± 0.02 | 0.68 ± 0.02 | 0.58 ± 0.01** | 0.55 ± 0.01** |
| Adult | marital-status | RF | 0.69 ± 0.02 | 0.69 ± 0.02 | 0.59 ± 0.01** | 0.57 ± 0.01** |
| Compas | race | SVC | 0.65 ± 0.03 | 0.65 ± 0.03 | 0.55 ± 0.01** | 0.50 ± 0.00** |
| Compas | race | LR | 0.84 ± 0.02 | 0.83 ± 0.02 | 0.82 ± 0.02 | 0.81 ± 0.03 |
| Compas | race | RF | 0.83 ± 0.03 | 0.83 ± 0.02 | 0.82 ± 0.03 | 0.81 ± 0.02 |
| Compas | race | SVC | 0.84 ± 0.02 | 0.84 ± 0.02 | 0.82 ± 0.02 | 0.81 ± 0.02* |
| Crime | race | LR | 0.73 ± 0.01 | 0.73 ± 0.01 | 0.72 ± 0.01 | 0.72 ± 0.01 |
| Crime | race | RF | 0.78 ± 0.00 | 0.78 ± 0.01 | 0.78 ± 0.01 | 0.78 ± 0.01 |
| Crime | race | SVC | 0.72 ± 0.01 | 0.72 ± 0.01 | 0.73 ± 0.01 | 0.73 ± 0.01 |
| Crime | race | LR | 0.66 ± 0.06 | 0.68 ± 0.07 | 0.70 ± 0.08 | 0.70 ± 0.08 |
| German | age | RF | 0.68 ± 0.06 | 0.67 ± 0.05 | 0.72 ± 0.05 | 0.71 ± 0.05 |
| German | age | SVC | 0.66 ± 0.07 | 0.66 ± 0.07 | 0.70 ± 0.07 | 0.70 ± 0.06 |
| German | age | LR | 0.64 ± 0.02 | 0.65 ± 0.01 | 0.64 ± 0.02 | 0.59 ± 0.02* |
| German | age | DecisionTree | 0.64 ± 0.02 | 0.65 ± 0.01** | 0.70 ± 0.02* | 0.70 ± 0.02** |
| NH Fitzpatrick17k | gender | vgg16 | 0.73 ± 0.01 | 0.71 ± 0.01** | 0.70 ± 0.02* | 0.70 ± 0.02** |
|   | skin type |   |   |   |   |   |

Table B.15

Prediction quality parity (PQP) as the percentage of flipped positives in the disadvantaged group varies from f = 0 (no bias) to f = 1 (maximum bias).

| Dataset | sensitive | model | PQP | PQP | PQP | PQP |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.00 ± 0.01 | 0.06 ± 0.01** | 0.21 ± 0.01** | 0.23 ± 0.01** |
| Adult | gender | RF | 0.01 ± 0.01 | 0.06 ± 0.02** | 0.24 ± 0.01** | 0.25 ± 0.01** |
| Adult | gender | SVC | 0.01 ± 0.01 | 0.05 ± 0.01** | 0.22 ± 0.01** | 0.24 ± 0.01** |
| Adult | gender | LR | 0.09 ± 0.01 | 0.12 ± 0.02** | 0.21 ± 0.01** | 0.21 ± 0.01** |
| Adult | marital-status | RF | 0.08 ± 0.01 | 0.11 ± 0.02** | 0.25 ± 0.01** | 0.25 ± 0.01** |
| Adult | marital-status | SVC | 0.08 ± 0.02 | 0.11 ± 0.01** | 0.23 ± 0.01** | 0.24 ± 0.01** |
| Adult | marital-status | LR | -0.06 ± 0.05 | -0.03 ± 0.05 | 0.06 ± 0.02** | 0.05 ± 0.02** |
| Adult | marital-status | RF | -0.01 ± 0.05 | 0.00 ± 0.06 | 0.06 ± 0.03** | 0.05 ± 0.02** |
| Compas | race | SVC | -0.05 ± 0.03 | -0.04 ± 0.05 | 0.01 ± 0.01** | 0.00 ± 0.00** |
| Compas | race | LR | -0.02 ± 0.08 | 0.01 ± 0.07 | 0.11 ± 0.10* | 0.13 ± 0.08** |
| Compas | race | RF | -0.03 ± 0.05 | 0.02 ± 0.06 | 0.16 ± 0.07* | 0.17 ± 0.06** |
| Compas | race | SVC | -0.03 ± 0.08 | 0.01 ± 0.08 | 0.10 ± 0.07* | 0.14 ± 0.07** |
| Folktables | race | LR | 0.01 ± 0.04 | 0.01 ± 0.04 | 0.02 ± 0.04 | 0.02 ± 0.04 |
| Folktables | race | RF | 0.01 ± 0.03 | 0.01 ± 0.02 | 0.00 ± 0.03 | 0.01 ± 0.03 |
| Folktables | race | SVC | 0.02 ± 0.03 | 0.02 ± 0.04 | 0.02 ± 0.04 | 0.02 ± 0.04 |
| Folktables | race | LR | 0.07 ± 0.13 | 0.06 ± 0.15 | 0.05 ± 0.16 | 0.06 ± 0.14 |
| German | age | RF | -0.01 ± 0.07 | 0.05 ± 0.09 | 0.07 ± 0.09 | 0.09 ± 0.14 |
| German | age | SVC | 0.03 ± 0.10 | 0.02 ± 0.10 | 0.02 ± 0.11 | 0.03 ± 0.15 |
| German | age | LR | -0.01 ± 0.01 | 0.01 ± 0.01** | 0.10 ± 0.01** | 0.14 ± 0.01** |
| German | age | DecisionTree | -0.01 ± 0.01</ |   |   |   |

---

<!-- Page 17 -->

M. Cecon et al.

Expert Systems With Applications 292 (2025) 128266

**Table B.16**

True positive rate (TPR) of the advantaged group as the percentage of flipped positives in the disadvantaged group varies from 
f = 0
 (no bias) to 
f = 1
 (maximum bias).

| Dataset | sensitive | model | TPR ( \tau = \alpha ) | TPR ( \tau = \alpha ) | TPR ( \tau = \alpha ) | TPR ( \tau = \alpha ) |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.61 ± 0.01 | 0.61 ± 0.01 | 0.60 ± 0.01 | 0.60 ± 0.01 |
| Adult | gender | RF | 0.64 ± 0.01 | 0.63 ± 0.01 | 0.62 ± 0.01* | 0.62 ± 0.01* |
| Adult | gender | SVCC | 0.61 ± 0.01 | 0.60 ± 0.01 | 0.60 ± 0.01 | 0.59 ± 0.01** |
| Adult | marital-status | LR | 0.65 ± 0.01 | 0.65 ± 0.01 | 0.65 ± 0.01 | 0.65 ± 0.01 |
| Adult | marital-status | RF | 0.66 ± 0.01 | 0.65 ± 0.01 | 0.65 ± 0.01 | 0.66 ± 0.01 |
| Adult | marital-status | SVCC | 0.64 ± 0.01 | 0.64 ± 0.01 | 0.65 ± 0.01 | 0.65 ± 0.01 |
| Compas | race | LR | 0.85 ± 0.02 | 0.76 ± 0.03** | 0.33 ± 0.04** | 0.22 ± 0.04** |
| Compas | race | RF | 0.81 ± 0.03 | 0.74 ± 0.03** | 0.28 ± 0.04** | 0.25 ± 0.05** |
| Compas | race | SVCC | 0.85 ± 0.04 | 0.79 ± 0.03** | 0.03 ± 0.06** | 0.00 ± 0.06** |
| Compas | crime | LR | 0.90 ± 0.04 | 0.89 ± 0.04 | 0.87 ± 0.04 | 0.85 ± 0.05 |
| Compas | crime | RF | 0.90 ± 0.03 | 0.89 ± 0.03 | 0.86 ± 0.03** | 0.85 ± 0.02** |
| Compas | crime | SVCC | 0.91 ± 0.04 | 0.90 ± 0.04 | 0.88 ± 0.04 | 0.87 ± 0.04 |
| Folktables | race | LR | 0.83 ± 0.01 | 0.82 ± 0.01 | 0.77 ± 0.01** | 0.75 ± 0.01** |
| Folktables | race | RF | 0.85 ± 0.01 | 0.85 ± 0.01 | 0.83 ± 0.02** | 0.83 ± 0.02** |
| Folktables | race | SVCC | 0.85 ± 0.01 | 0.83 ± 0.01** | 0.78 ± 0.01** | 0.76 ± 0.01** |
| Folktables | age | LR | 0.89 ± 0.05 | 0.88 ± 0.05 | 0.82 ± 0.05* | 0.79 ± 0.06* |
| Folktables | age | RF | 0.93 ± 0.02 | 0.91 ± 0.04 | 0.86 ± 0.05* | 0.82 ± 0.05* |
| Folktables | age | SVCC | 0.93 ± 0.02 | 0.90 ± 0.06 | 0.83 ± 0.05* | 0.82 ± 0.06* |
| NIH Fitzpatrick17k | gender | DemseNet | 0.46 ± 0.03 | 0.49 ± 0.03 | 0.59 ± 0.06* | 0.52 ± 0.05* |
| NIH Fitzpatrick17k | skin type | vgg16 | 0.70 ± 0.02 | 0.70 ± 0.02 | 0.69 ± 0.02 | 0.70 ± 0.01 |

**Table B.17**

True positive rate (TPR) of the disadvantaged group as the percentage of flipped positives in the disadvantaged group varies from 
f = 0
 (no bias) to 
f = 1
 (maximum bias).

| Dataset | sensitive | model | TPR ( \tau = \delta ) | TPR ( \tau = \delta ) | TPR ( \tau = \delta ) | TPR ( \tau = \delta ) |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.53 ± 0.02 | 0.40 ± 0.03** | 0.07 ± 0.02** | 0.05 ± 0.02** |
| Adult | gender | RF | 0.54 ± 0.02 | 0.43 ± 0.04** | 0.06 ± 0.01** | 0.04 ± 0.01** |
| Adult | gender | SVCC | 0.53 ± 0.02 | 0.42 ± 0.03** | 0.06 ± 0.02** | 0.03 ± 0.03** |
| Adult | marital-status | LR | 0.29 ± 0.03 | 0.22 ± 0.04** | 0.03 ± 0.01** | 0.02 ± 0.01** |
| Adult | marital-status | RF | 0.35 ± 0.03 | 0.29 ± 0.03** | 0.00 ± 0.00** | 0.00 ± 0.00** |
| Adult | marital-status | SVCC | 0.30 ± 0.03 | 0.26 ± 0.03** | 0.01 ± 0.01** | 0.00 ± 0.00** |
| Compas | race | LR | 0.68 ± 0.03 | 0.55 ± 0.05** | 0.11 ± 0.02** | 0.07 ± 0.02** |
| Compas | race | RF | 0.66 ± 0.03 | 0.57 ± 0.04** | 0.16 ± 0.02** | 0.09 ± 0.01** |
| Compas | race | SVCC | 0.68 ± 0.06 | 0.58 ± 0.05** | 0.01 ± 0.02** | 0.00 ± 0.00** |
| Compas | crime | LR | 0.57 ± 0.10 | 0.50 ± 0.11 | 0.25 ± 0.15** | 0.18 ± 0.12** |
| Compas | crime | RF | 0.57 ± 0.07 | 0.47 ± 0.10 | 0.19 ± 0.12** | 0.18 ± 0.10** |
| Compas | crime | SVCC | 0.59 ± 0.08 | 0.50 ± 0.11 | 0.26 ± 0.11** | 0.18 ± 0.10** |
| Folktables | race | LR | 0.79 ± 0.04 | 0.77 ± 0.04 | 0.69 ± 0.04* | 0.66 ± 0.04** |
| Folktables | race | RF | 0.83 ± 0.03 | 0.82 ± 0.03 | 0.77 ± 0.05* | 0.77 ± 0.05* |
| Folktables | race | SVCC | 0.80 ± 0.04 | 0.78 ± 0.04 | 0.70 ± 0.04* | 0.67 ± 0.04* |
| Folktables | age | LR | 0.82 ± 0.13 | 0.78 ± 0.15 | 0.60 ± 0.17** | 0.54 ± 0.12** |
| Folktables | age | RF | 0.90 ± 0.07 | 0.80 ± 0.09** | 0.60 ± 0.10** | 0.50 ± 0.16** |
| Folktables | age | SVCC | 0.87 ± 0.09 | 0.83 ± 0.14 | 0.61 ± 0.11** | 0.55 ± 0.11** |
| NIH Fitzpatrick17k | gender | DemseNet | 0.44 ± 0.05 | 0.40 ± 0.04 | 0.18 ± 0.07** | 0.03 ± 0.01** |
| NIH Fitzpatrick17k | skin type | vgg16 | 0.61 ± 0.05 | 0.52 ± 0. |   |   |

---

<!-- Page 18 -->

M. Cecon et al.

Expert Systems With Applications 292 (2025) 128266

Table B.18Equal opportunity (EO) as the percentage of flipped positives in the disadvantaged group varies from f = 0 (no bias) to f = 1 (maximum bias).

| Dataset | sensitive | model | EO | EO | EO | EO |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.08 ± 0.02 | 0.21 ± 0.02** | 0.52 ± 0.03** | 0.55 ± 0.02** |
| Adult | gender | RF | 0.10 ± 0.02 | 0.20 ± 0.04** | 0.56 ± 0.01** | 0.57 ± 0.02** |
| Adult | gender | SVCC | 0.08 ± 0.02 | 0.18 ± 0.02** | 0.54 ± 0.02** | 0.56 ± 0.01** |
| Adult | marital-status | LR | 0.36 ± 0.03 | 0.43 ± 0.04** | 0.62 ± 0.02** | 0.63 ± 0.02** |
| Adult | marital-status | RF | 0.31 ± 0.03 | 0.39 ± 0.03** | 0.65 ± 0.01** | 0.66 ± 0.01** |
| Adult | marital-status | SVCC | 0.34 ± 0.03 | 0.39 ± 0.02** | 0.65 ± 0.01** | 0.65 ± 0.01** |
| Compas | race | LR | 0.17 ± 0.03 | 0.21 ± 0.05 | 0.21 ± 0.05 | 0.15 ± 0.05 |
| Compas | race | RF | 0.15 ± 0.05 | 0.19 ± 0.05 | 0.19 ± 0.05 | 0.15 ± 0.05 |
| Compas | race | SVCC | 0.18 ± 0.04 | 0.21 ± 0.04 | 0.02 ± 0.04* | 0.00 ± 0.00** |
| Crime | race | LR | 0.33 ± 0.11 | 0.39 ± 0.11 | 0.62 ± 0.17** | 0.67 ± 0.15** |
| Crime | race | RF | 0.33 ± 0.06 | 0.42 ± 0.12 | 0.66 ± 0.15** | 0.67 ± 0.10** |
| Crime | race | SVCC | 0.32 ± 0.08 | 0.40 ± 0.12 | 0.62 ± 0.12** | 0.69 ± 0.12** |
| Folktables | race | LR | 0.05 ± 0.04 | 0.05 ± 0.04 | 0.08 ± 0.04 | 0.09 ± 0.04 |
| Folktables | race | RF | 0.02 ± 0.04 | 0.02 ± 0.03 | 0.05 ± 0.04 | 0.06 ± 0.03 |
| Folktables | race | SVCC | 0.04 ± 0.03 | 0.06 ± 0.04 | 0.08 ± 0.02* | 0.09 ± 0.04* |
| German | age | LR | 0.07 ± 0.13 | 0.10 ± 0.14 | 0.22 ± 0.16 | 0.25 ± 0.10** |
| German | age | RF | 0.03 ± 0.06 | 0.11 ± 0.08 | 0.26 ± 0.09* | 0.32 ± 0.15** |
| German | age | SVCC | 0.06 ± 0.08 | 0.09 ± 0.11 | 0.22 ± 0.10* | 0.26 ± 0.13** |
| NIH Fitzpatrick17k | gender | DenseNet | 0.01 ± 0.02 | 0.09 ± 0.02** | 0.40 ± 0.03** | 0.48 ± 0.01** |
| NIH Fitzpatrick17k | skin type | vgg16 | 0.09 ± 0.05 | 0.16 ± 0.06* | 0.21 ± 0.08** | 0.28 ± 0.02** |

Table B.19

Demographic parity (DP) as the percentage of flipped positives in the disadvantaged group varies from f = 0 (no bias) to f = 1 (maximum bias).

| Dataset | sensitive | model | DP | DP | DP | DP |
| --- | --- | --- | --- | --- | --- | --- |
| Dataset | sensitive | model | f = 0 (no bias) | f = 0.2 | f = 0.8 | f = 1 (max bias) |
| Adult | gender | LR | 0.18 ± 0.01* | 0.20 ± 0.01** | 0.25 ± 0.01** | 0.25 ± 0.01** |
| Adult | gender | RF | 0.18 ± 0.01 | 0.20 ± 0.01** | 0.24 ± 0.01** | 0.24 ± 0.01** |
| Adult | gender | SVCC | 0.17 ± 0.00 | 0.17 ± 0.01* | 0.24 ± 0.01* | 0.24 ± 0.01* |
| Adult | marital-status | LR | 0.37 ± 0.01 | 0.38 ± 0.01 | 0.40 ± 0.01** | 0.40 ± 0.01** |
| Adult | marital-status | RF | 0.36 ± 0.02 | 0.36 ± 0.02 | 0.38 ± 0.01* | 0.38 ± 0.02 |
| Adult | marital-status | SVCC | 0.36 ± 0.01 | 0.37 ± 0.01 | 0.39 ± 0.01** | 0.39 ± 0.01** |
| Compas | race | LR | 0.26 ± 0.03 | 0.28 ± 0.02 | 0.18 ± 0.04* | 0.12 ± 0.03** |
| Compas | race | RF | 0.21 ± 0.05 | 0.20 ± 0.05 | 0.16 ± 0.04 | 0.12 ± 0.04** |
| Compas | race | SVCC | 0.26 ± 0.02 | 0.28 ± 0.02 | 0.02 ± 0.02* | 0.00 ± 0.00** |
| Crime | race | LR | 0.62 ± 0.06 | 0.63 ± 0.06 | 0.69 ± 0.07 | 0.70 ± 0.08 |
| Crime | race | RF | 0.62 ± 0.07 | 0.64 ± 0.07 | 0.67 ± 0.06 | 0.67 ± 0.06 |
| Crime | race | SVCC | 0.62 ± 0.07 | 0.64 ± 0.07 | 0.70 ± 0.06* | 0.70 ± 0.07 |
| Folktables | race | LR | 0.06 ± 0.03 | 0.07 ± 0.03 | 0.09 ± 0.03 | 0.09 ± 0.03 |
| Folktables | race | RF | 0.05 ± 0.03 | 0.06 ± 0.03 | 0.09 ± 0.03* | 0.09 ± 0.04 |
| Folktables | race | SVCC | 0.06 ± 0.03 | 0.06 ± 0.03 | 0.09 ± 0.03 | 0.09 ± 0.03 |
| German | age | LR | 0.06 ± 0.13 | 0.11 ± 0.13 | 0.24 ± 0.16* | 0.27 ± 0.15** |
| German | age | RF | 0.09 ± 0.08 | 0.12 ± 0.08 | 0.28 ± 0.12** | 0.31 ± 0.11** |
| German | age | SVCC | 0.09 ± 0.10 | 0.09 ± 0.11 | 0.26 ± 0.14* | 0.30 ± 0.11** |
| NIH Fitzpatrick17k | gender | DenseNet | 0.00 ± 0.00 | 0.02 ± 0.00** | 0.10 ± 0.02* | 0.10 ± 0.01** |
| NIH Fitzpatrick17k | skin type | vgg16 | 0.15 ± 0.02 | 0.17 ± 0.02 | 0.22 ± |   |

---

<!-- Page 19 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

### Appendix C. Additional results on bias detection

In this section, we report bias detection results regarding all datasets except Folktables and NIH, which are discussed in Section 5 Figs. C.6–C.11.

Adult (gender)

Figure C.6 displays the results of bias detection methods on the Adult (gender) dataset. The figure is organized into a 3x3 grid of plots. The columns represent three different scenarios: Underrepresentation, Label bias, and Proxies. The rows represent three bias detection methods: RD(̑), SD(̑), and sAUC(̑). The x-axis for the Underrepresentation scenario is U (values: 0, 0.2, 0.8, 0.95). The x-axis for the Label bias scenario is f (values: 0, 0.2, 0.8, 1). The x-axis for the Proxies scenario is correlation (values: 0, 0.25, 0.50, 0.75, 1). The y-axis for all plots represents the bias detection method's value, ranging from 0.0 to 1.0. The plots show that bias detection methods generally perform better (higher values) as the bias increases, with the Proxies scenario showing the most significant increase in bias detection as correlation increases.

Fig. C.6. Results of the bias detection methods on Adult (gender). The columns represent the three different scenarios while the rows represent the three bias detection methods.

Adult (marital status)

Figure C.7 displays the results of bias detection methods on the Adult (marital status) dataset. The figure is organized into a 3x3 grid of plots. The columns represent three different scenarios: Underrepresentation, Label bias, and Proxies. The rows represent three bias detection methods: RD(̑), SD(̑), and sAUC(̑). The x-axis for the Underrepresentation scenario is U (values: 0, 0.2, 0.8, 0.95). The x-axis for the Label bias scenario is f (values: 0, 0.2, 0.8, 1). The x-axis for the Proxies scenario is correlation (values: 0, 0.25, 0.50, 0.75, 1). The y-axis for all plots represents the bias detection method's value, ranging from 0.0 to 1.0. The plots show that bias detection methods generally perform better (higher values) as the bias increases, with the Proxies scenario showing the most significant increase in bias detection as correlation increases.

Fig. C.7. Results of the bias detection methods on Adult (marital status). The columns represent the three different scenarios while the rows represent the three bias detection methods.

19

---

<!-- Page 20 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Fig. C.8. Results of the bias detection methods on Compas. The columns represent the three different scenarios while the rows represent the three bias detection methods.

Fig. C.9. Results of the bias detection methods on Crime. The columns represent the three different scenarios while the rows represent the three bias detection methods.

20

---

<!-- Page 21 -->

M. Ceccon et al.

Expert Systems With Applications 292 (2025) 128266

Fig. C.10. Results of the bias detection methods on German. The columns represent the three different scenarios while the rows represent the three bias detection methods.

Fig. C.11. Results of the bias detection methods on Fitzpatrick17k. The columns represent the three different scenarios while the rows represent the three bias detection methods.

21

---

<!-- Page 22 -->

M. Cecon et al.

Expert Systems With Applications 2021 (2025) 128266

References

Alvarez J., M. Colmenarejo, A. B. Ebadi, A. Fabrizieri, S. Fahimi, M. Ferrara, A. Grados, S. Mognaschi, P. Pappagennaro, I. Lobo, P. R. Russo, M. Scott, K. M. Sante, L. Zhao, X., and Ruggieri, S. (2024). Policy advice and best practices on bias and fairness in machine and information technology. 2021, https://doi.org/10.1109/ACCESS.2021.3509476.

Alves, G., Ambard, M., Berrier, F., Coceire, M., & Napoli, A. (2021). Reducing uncertainty of bias of ML models on tabular and textual data. In IEEE International conference on data science and advanced analytics, DSAA 2021, Porto, Portugal, October 6–8, 2021, Proceedings (Part I) (Vol. 1206). IEEE, https://doi.org/10.1109/DSAA54903.2021.9441291.

Angwin, J., Larson, J., Matti, S., & Richerme, L. (2016). Machine bias: A ProPublica report. https://www.propublica.org/article/machine-bias-risk-analysis-alarms-society.

Baker, B. E., & Hawo, A. (2022). Algorithmic bias in education. International Journal of Educational Analytics, 1(1), 1–10. https://doi.org/10.3390/ijea1010005.

Bartel, A. S., & J. J. J. van der Velde, M. T. (2022). Fairness-utility trade-off in the new international conference on learning representations, ICLR 2022, virtual event, April 25–29, 2022, OpenAccess.net. https://openaccess.net/fairness-trd-RfRfK2R2.

Bau, A. A., Zettlitz, A., & B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B. B.

---

<!-- Page 23 -->

Expert Systems With Applications 292 (2025) 128266

M. Cecon et al.

Campbell, G.J., 1992. How to use the 1991 Census 1991 Census. https://doi.org/10.1145/100377.

Hu, J., Zeng, H., Li, H., Wu, C., and Chen, Z. (2007). Demographic prediction based on user's knowing behavior. In C. L. Williamson, E. M. Zuhro, P. F. Patel-Schneider, and P. J. Shany (Eds.), Proceedings of the 16th international conference on world wide web. WWW '07, Banff, Alberta, Canada, May 8–12, 2007. ACM, New York, NY, 1245272–1245294.

Brown, S. (2019). Decision technology – artificial intelligence (AI) – bias in AI systems and AI aided decision making. https://www.iso.org/standards/7667.html.

Jacobs, A. E., and Willich, R. (2021). Measurement and fairness. In C. M. Elida, W. Isaac, & R. S. Zemel (Eds.), Facet 21: 2021 ACM conference on fairness, accountability, and transparency, virtual event. Toronto, Canada, March 3–10, 2021. 3975–3803. ACM, https://doi.org/10.1145/3465088.

Gladys, A., and Kozak, A. (2019). The fairness of risk scores beyond classification: Bipartite ranking and the AUC metric. https://arxiv.org/abs/1902.05824.

Kallus, A., & Zolitschka, T. (2021). The fairness of risk scores beyond classification: Bi-partite ranking and the AUC metric. https://arxiv.org/abs/2102.05824.

Karimi, F., & Balducci, D. (2021). Data preprocessing techniques for classification: Bi-partite ranking (2019). Knowledge and Information Systems, 33(1), 1–33. https://doi.org/10.1145/3465088.

Kohavi, R. (1996). Scaling up the accuracy of naive-bayes classifiers: A decision-tree hybrid. In E. Srinivas, J. Han, & U. M. Fayyad (Eds.), Proceedings of the second international conference on knowledge discovery in databases. Portland, Oregon, USA, 2002. 2007. AAAI Press. http://www.aaai.org/Library/KDD/1996/KDD960001.0001.html.

Konigsteger, F., & Thalheimer, A. (2022). And: Documentation: A path to accountability. https://doi.org/10.1145/3465088.

Liu, Z., Qiu, R., Zeng, Z., Zhu, Y., Hamani, H., & Tong, H. (2024). AIism: Attributing, measuring, and mitigating algorithmic inequality. AI, 14(4), 261–267. https://doi.org/10.1145/3509787.

Madras, D., Creager, E., Pissati, T., & Zemel, R. (2018). Learning adversarially fair and trustworthy representations. In C. G. Dy, & A. Krause (Eds.), Proceedings of the 35th international conference on machine learning. ACM, 2018. Stockholm/Sweeden, Stockholm, Sweden, July 10–15, 2018. 5381–5389. PMLR (vol. 80). Proceedings of machine learning research. https://proceedings.mlr.press/v80/madras18.html.

Mecei, M., Torchiano, M., Verbi, A., & De Martin, J. C. (2023). Measuring imbalance on intersectoral protected attributes and on target variable to forecast unfair classifications. IEEE Access, 11, 26996–27011. https://doi.org/10.1109/ACCESS.2023.3252279.

Mecei, M., Verbi, A., & Torchiano, M. (2022). Detecting risk of biased output with balance measures. AI, Journal of Data and Inequality, 14(4), 261–267. https://doi.org/10.1145/3509787.

Mehrab, N., Mostafareh, F., Saesna, N., Lemam, K., & Galyani, A. (2022). A survey on bias and fairness in machine learning. AI, Computing Systems, 54(6), 1151–1153.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. Science, 366(6460), 447–453. https://doi.org/10.1126/science.aba3685.

Parliament, B. (2024). Artificial intelligence act. https://www.europarl.europa.eu/docs/documents_fr_a-2024-1818.en.pdf.

Pedreschi, L., Ruggieri, S., & Tufano, F. (2008). Discrimination-aware data mining. In Y. Li, B. Liu, & S. Sarigamy (Eds.), Proceedings of the 14th ACM SIGKDD international conference on knowledge discovery and data mining. Las Vegas, Nevada, USA, August 24–27, 2008. ACM, 560–568. ACM, https://doi.org/10.1145/1401169.

Perez, C. C. (2019). Invisible women. Data bias in the world. For men, August, 14–28. Publishers, M., Zaldivar, A., & Kijurians, O. (2022). Data curation and transparent data documentation for responsible AI. In Facet 21: 2022 ACM conference on fairness, accountability, and transparency, Seoul, Republic of Korea, June 21–26, 2022. ACM, https://doi.org/10.1145/3465088.

Rondina, M., Verbi, A., & De Martin, J. C. (2023). Complementarity of data documentation on ML AI representations: An empirical investigation. In N. Monta, V. Val, C. Gascaho,

C. Silva, & R. Sebastiani (Eds.), Progress in artificial intelligence – 22nd EPIA conference on progress in artificial intelligence. Springer, Vienna, Austria, September 8–10, 2023. Springer, 79–91. Springer (https://doi.org/10.1007/978-3-030-72910-0_5).

Ruoss, A., Balcanquell, M., Fischer, M., & Vecher, M. T. (2020). Learning certified individual fair representations. In H. Larochelle, M. Hanzin, S. Redscell, M. Balcanquell, & H. Lin (Eds.), Advances in neural information processing systems 33. Advances in neural information processing systems 33. Vancouver, BC, Canada, December 6–12, 2020. https://proceedings.neurips.cc/paper/2020/huang2021.

Sambasivan, K., Kapasnis, S., Hightall, H., Akroyd, D., Parasho, P., & Ayroo, D. (2021). “Everyone wants to do the model work, not the data work”: Data cascades in high-scale AI. In M. Arslan, A. Chakraborty, S. K. Dasgupta, P. Bhatia, & S. M. Trivedi (Eds.), CHI '21: Conference on human factors in computing systems, virtual event. 5549–5561. ACM, https://doi.org/10.1145/3459809.

Santana, M., & Salvalhije, H. (2018). Comparison and benchmark of name-to-giver inference services. PeerJ Computer Science, 4:e156. https://doi.org/10.7717/peerj.ccs.v4i1/e156.

Schwartz, R., Vassilev, A., Greene, K., Petrie, S., Burt, A., & Hall, P. (2022). Towards a standard for identifying and managing bias in artificial intelligence. US Department of Commerce, National Institute of Standards and Technology.

Seyyed-Kalantari, L., Liu, G., McMillan, M., Chen, Y. J., & Ghassami, M. (2020). Characterizing and mitigating algorithmic inequality. AI, 12(1), 1–10. https://doi.org/10.1145/3465088.

Slankard, S., Halpern, Y., Brock, E., Avroff, J., Wilson, J. Y., & Sulem, D. (2017). No classification without bias: A survey of fairness in machine learning. AI, 9(1), 1–10. https://doi.org/10.1145/3465088.

Sorosh, A., & Sulem, D. (2017). Machine learning: Machine learning for the developing world. Developing World, 61(2), 159–166. https://doi.org/10.1177/0013164417700001.

Verbi, A., & Mecei, M. (2021). Life cycle of EAMOO 2021. AI, Conference on equity, fairness, accountability, and transparency, virtual event. Toronto, Canada, March 3–10, 2021. 173–179. ACM, https://doi.org/10.1145/3465088.

Vernon, C. (2019). The impact of algorithmic bias on the impact of group membership bias on the quality and fairness of exposure in ranking. In Proceedings of the 47th international conference on artificial intelligence and statistics. Proceedings of the 47th international conference on artificial intelligence and statistics. https://proceedings.mlr.press/v102/ver19.html.

Verbi, A., Torchiano, M., & Mecei, M. (2021). A data quality approach to the identification of fairness, accountability, and transparency, virtual event / Toronto, Canada, March 3–10, 2021. 10169–10174. ACM, https://doi.org/10.1145/3465088.

Wang, J., & Levy, C. C. (2021). Fair classification with group-dependent label noise. In C. M. Elida, W. Isaac, & R. S. Zemel (Eds.), Facet 21: 2021 ACM conference on fairness, accountability, and transparency, virtual event. Toronto, Canada, March 3–10, 2021. 5260–5306. ACM, https://doi.org/10.1145/3465088.

Wang, M., Peng, Y., Liu, L., Zhang, H., & Summers, R. R. (2017). Chest-nysf: Hospital-scale chest x-ray database and benchmarks on supervised classification and localization of common chest diseases. In Proceedings of the IEEE