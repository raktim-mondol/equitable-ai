<!-- Page 1 -->

1

# A survey of recent methods for addressing AI fairnessand bias in biomedicine

Yifan Yang1,2, Mingquan Lin3, Han Zhao4, Yifan Peng3, Furong Huang2, Zhiyong Lu1,*

1National Center for Biotechnology Information (NCBI), National Library of Medicine (NLM), National Institutes of Health (NIH), Bethesda, MD, USA

2Department of Computer Science, University of Maryland, College Park USA

3Department of Population Health Sciences, Weill Cornell Medicine, New York, USA

4Department of Computer Science, University of Illinois at Urbana-Champaign, Champaign, IL

*Corresponding author

Zhiyong Lu, PhD FACMI FIAHSI

zhiyong.lu@nih.gov; 301-435-4920

Keywords: fairness, bias, biomedicine, AI

---

<!-- Page 2 -->

2

## ABSTRACT

Objectives: Artificial intelligence (AI) systems have the potential to revolutionize clinical practices, including improving diagnostic accuracy and surgical decision-making, while also reducing costs and manpower. However, it is important to recognize that these systems may perpetuate social inequities or demonstrate biases, such as those based on race or gender. Such biases can occur before, during, or after the development of AI models, making it critical to understand and address potential biases to enable the accurate and reliable application of AI models in clinical settings. To mitigate bias concerns during model development, we surveyed recent publications on different debiasing methods in the fields of biomedical natural language processing (NLP) or computer vision (CV). Then we discussed the methods, such as data perturbation and adversarial learning, that have been applied in the biomedical domain to address bias.

Methods: We performed our literature search on PubMed, ACM digital library, and IEEE Xplore of relevant articles published between January 2018 and December 2023 using multiple combinations of keywords. We then filtered the result of 10,041 articles automatically with loose constraints, and manually inspected the abstracts of the remaining 890 articles to identify the 55 articles included in this review. Additional articles in the references are also included in this review. We discuss each method and compare its strengths and weaknesses. Finally, we review other potential methods from the general domain that could be applied to biomedicine to address bias and improve fairness.

Results: The bias of AIs in biomedicine can originate from multiple sources such as insufficient data, sampling bias and the use of health-irrelevant features or race-

---

<!-- Page 3 -->

3

adjusted algorithms. Existing debiasing methods that focus on algorithms can be categorized into distributional or algorithmic. Distributional methods include data augmentation, data perturbation, data reweighting methods, and federated learning. Algorithmic approaches include unsupervised representation learning, adversarial learning, disentangled representation learning, loss-based methods and causality-based methods.

---

<!-- Page 4 -->

4

## 1. INTRODUCTION

Over the past decade, Artificial intelligence (AI) systems that use deep neural networks have become increasingly popular in medicine. AI's diagnostic capabilities have proven to be on par with domain experts in multiple specialties, such as pathology classification, anatomical segmentation, lesion delineation, cardiovascular medicine, diabetic retinopathy, skin cancer, pneumonia, and hepatocellular cancer.1-6 For example, AI models fed with live streaming Electronic Health Record (EHR) data in surgical decision-making can address the weakness of time-consuming manual data entry and suboptimal accuracy.7 In ophthalmology, the application of AI models can reduce the usage of manpower and the cost of screening, including in remote settings.4,8 Using acoustics, MRIs, CTs, or x-rays, AI systems can screen for indicators of osteoporosis, such as bone mass or fragility fractures, or automatically segment images of patients with or at risk of osteoporosis.9

Despite the remarkable achievements of AI, there are still substantial concerns regarding the fairness and bias of AI models in the field of biomedicine. Prior work defines bias in healthcare as systematic error due to flaws in the study's design, conduct, or analysis.10 This type of error can bias the study results and make it difficult to accurately interpret the findings. The issue of bias and fairness in AI systems has been the subject of extensive research and discussion in the broader field of AI and computer science for many years.11-13 In this work, the emphasis is on biases related to demographic or geographic subgroups. We define bias as the presence of systematic errors or disparities within decision-making processes that disproportionately affect specific subgroups. Conversely, fairness is defined as the eradication/diminishing of

---

<!-- Page 5 -->

5

these biases to ensure outcomes that are both equitable and just. In machine learning, there are many different fairness definitions, focusing on different aspects of the evaluation.14 For example, demographic parity requires the probability of positive prediction to be the same across different sub-groups, and accuracy parity focuses on equalizing the error rate of sub-groups. In the context of biomedicine, the criteria for making subgroups can be demographic information such as race, sex, or age, and can also be things like admitted hospitals and brand of radiographic devices used in diagnosis.

The unequal behavior of algorithms toward different population sub-groups may be considered a violation of the principles of bioethics, which include justice, autonomy, beneficence, and non-maleficence.3 When predicting in-hospital mortality, physiological decompensation, length of stay, and phenotype classification, models have demonstrated lower performance for minority populations.15 Studies have shown that AI models can predict unnecessarily protected information, such as gender, race, and institution, from the representation of scan images.16–18

Several reviews in the biomedical domain have summarized the issue of fairness in artificial intelligence3,19–21. Unlike these studies, we focus on existing debiasing methods from biomedical natural language processing (NLP) or computer vision (CV). We discuss each method, compare their strengths and weaknesses, and examine what problem each category of method can potentially solve. Finally, we discuss other potential methods from the general domain that could be applied to biomedicine to address bias and improve fairness, and provide future directions on fairness in biomedicine AI.

---

<!-- Page 6 -->

6

| **Problem** | Artificial Intelligence (AI) systems perpetuate social inequities or demonstrate biases, such as those based on race or gender. |
| --- | --- |
| **What is Already Known** | AI systems have the potential to revolutionize clinical practices, including improving diagnostic accuracy and surgical decision-making, while also reducing costs and manpower. It is critical to understand and address potential biases to enable the application of AI models accurately and reliably in clinical settings. |
| **What This Paper Adds** | We surveyed recent papers on AI bias and then discussed the source of bias for biomedicine AI. We also include methods, such as data perturbation and adversarial learning, that have been applied in the biomedical domain to address bias. We also discuss methods that have been applied in the general domain to address bias that could be applied to clinical tasks. Understanding the Taxonomy of methods and the source of bias would help choose the correct measure to address bias in various situations. |

## 2. MATERIALS AND METHODS

We performed our literature search on PubMed, ACM digital library, and IEEE Xplore. The overall pipeline is demonstrated in Figure 1. We searched peer-reviewed articles on PubMed between January 2018 and December 2022 with the combination of two sets of keywords: (AI or ML or Deep learning or Algorithmic) + (equity or bias). On the ACM digital library and IEEE Xplore with the same time frame, we included

---

<!-- Page 7 -->

[{"titles": "The figure is titled 'Figure 1. Pipeline of searching and filtering the literature for this review', located at the bottom center of the image in a bold black font.", "x_labels": "There are no x-axis labels as this is a flow diagram, not a standard coordinate plot.", "y_labels": "There are no y-axis labels as this is a flow diagram, not a standard coordinate plot.", "x_ticks": "There are no x-axis ticks as this is a flow diagram.", "y_ticks": "There are no y-axis ticks as this is a flow diagram.", "legends": "There is no formal legend; the components of the flowchart are labeled directly within the diagram.", "series": "The data series represent the number of articles at each stage of the pipeline: 10,041 articles after the initial 'Article search' (January 2018 to December 2022), 890 articles after 'Keyword filtering' (filtering duplicates and irrelevant articles), and 55 articles after 'Manual screening' (selecting articles based on title and abstract). Additionally, 'Additional articles' (including relevant articles from references) are added to the final count."}]

[[{"id": 1, "x": 150, "y": 150, "x2": 350, "y2": 250, "color": "#FFFFE0", "stroke": "#000000"}, {"id": 2, "x": 350, "y": 150, "x2": 550, "y2": 250, "color": "#FFFFE0", "stroke": "#000000"}, {"id": 3, "x": 550, "y": 150, "x2": 750, "y2": 250, "color": "#FFFFE0", "stroke": "#000000"}, {"id": 4, "x": 550, "y": 250, "x2": 750, "y2": 350, "color": "#FFFACD", "stroke": "#000000"}, {"id": 5, "x": 150, "y": 250, "x2": 350, "y2": 350, "color": "#FFFACD", "stroke": "#000000"}, {"id": 6, "x": 350, "y": 250, "x2": 550, "y2": 350, "color": "#FFFACD", "stroke": "#000000"}, {"id": 7, "x": 550, "y": 250, "x2": 750, "y2": 350, "color": "#FFFACD", "stroke": "#000000"}], [{"x": 150, "y": 250, "x2": 350, "y2": 350}, {"x": 350, "y": 250, "x2": 550, "y2": 350}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2": 550, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 250}, {"x": 550, "y": 250, "x2": 750, "y2": 350}], [{"x": 150, "y": 250, "x2": 350, "y2": 250}, {"x": 350, "y": 250, "x2":

---

<!-- Page 8 -->

8

The diagram illustrates the flow of bias in a machine learning process. On the left, five rectangular boxes are stacked vertically, each containing a different type of bias: 'Historic bias' (with a gear icon), 'Representation bias' (with a person icon), 'Aggregation bias' (with a magnifying glass icon), 'Population bias' (with a globe icon), and 'Measurement bias' (with a ruler icon). A large orange arrow points from this stack to the right. On the right, two rectangular boxes are stacked vertically: 'Biased dataset' (with a question mark icon) and 'Biased ML system' (with a brain icon).

Figure 2. Different sources of bias that can lead to biased datasets and ML systems in biomedicine

### 3.1 Causes of Biases

To apply AI models accurately and reliably to clinical settings, it is necessary to understand and address potential biases. Bias can occur at any stage of the process, from data collection to model development22. Mehrabi et al. present a categorization of bias in ML systems, delineating them into three primary types: biases originating from data to algorithm, from user interaction to data, and from algorithm to user interaction23. Additionally, they elaborate on 19 distinct types of biases within these categories. Similarly, Suresh et al. pinpointed 7 sources of bias in the ML system life cycle that ranges from data collection to model deployment24. While these taxonomies are broadly applicable in ML fairness, the biomedicine domain faces unique challenges and specific bias sources. Biases in biomedicine AI not only align with general AI biases but also include distinct causes pertinent to this field, such as disparities in healthcare access, disease prevalence variations across populations, and differing quality of medical data.

---

<!-- Page 9 -->

9

This context specificity is crucial for understanding and mitigating biases in biomedical AI. Figure 2 illustrates the various sources of biases specifically in biomedical AI systems. These biases significantly impact ML system outcomes, potentially favoring or disadvantaging specific demographic or geographic subgroups, or leading to biased data collection that can result in unfair ML systems with serious implications for healthcare equality and efficacy.

### 3.1.1 Historic bias

Historical bias, stemming from existing societal and technological issues, can exist in the data generation processes, established tools or pretrained models23. A 2019 study revealed historic bias related to race in heart-failure management at a Boston emergency department, influenced by the American Heart Association's (AHA) scoring system. This system, the Get with the Guidelines—Heart Failure Risk Score, assigns higher risk points to "nonblack" patients, resulting in black and Latinx patients being less likely than white patients to be admitted to cardiology services26. In a study by Zhang et al., they used MIMIC-III26, a publicly available clinical note database, to finetune a BERT model initialized from SciBERT27. The researchers found that modifying race can generate a worse course of action for African American patients and observed a prediction gap between different genders and races, suggesting the inherent bias of pretrained models28. The underlying disadvantage for African Americans learned by the language model is a type of historic bias.

### 3.1.2 Representation bias

Representation bias arises when a development sample does not adequately represent a section of the population, leading to its inability to effectively generalize for a

---

<!-- Page 10 -->

10

specific subset of the user population24. For instance, in diabetic retinopathy, the data imbalance results in a large accuracy gap between light-skinned and dark-skinned subjects3. Another example is facial recognition software with AI for early detection of acromegaly, where existing studies have been performed only in predominantly White or Asian populations29. Considering that the data collected is always biased towards the population that can afford healthcare, the representation bias in biomedicine AI is also related to the historic bias2,21,29-32.

### 3.1.3 Aggregation bias

Aggregation bias occurs when incorrect assumptions about individuals or subgroups are made based on observations of the entire population23. This can happen when making predictions about a subgroup based on evidence from a larger population. For example, in precision medicine for selection for type 2 diabetes, a large patient group better suited for SGLT2 inhibitor therapy was under-recommended for it due to low overall cardiorenal disease risk, with only 14.3% receiving the suggestion. Conversely, a smaller group, ideal for DPP4 inhibitor therapy, had 75% recommended SGLT2 inhibitors instead, influenced by their older age and higher cardiorenal risk31.

### 3.1.4 Population bias

Population bias in biomedical AI emerges when the characteristics, demographics, and statistical profiles of the patient population differ significantly from those of the intended patient population24. For example, predictive models trained on data dominated by White Americans result in higher error rates for African Americans33. In the context of cardiac imaging technologies and digital histology, the quality of images produced by cardiac MRI machines and the coloring and quality of uploaded

---

<!-- Page 11 -->

11

tumor tissue slides can vary among institutions and vendors, resulting in site-specific signatures or conventions that can introduce population bias when applying trained models to different sites2,8,18.

### 3.1.5 Measurement bias

Measurement bias occurs due to the selection, usage, and measurement of specific features23. An algorithm using healthcare costs may incorrectly conclude that dark-skinned patients are healthier than light-skinned patients with equal levels of illness, as they may receive less healthcare funding. This may result in a significant reduction in the number of dark-skinned patients receiving treatment22,25, and healthcare costs can be viewed as a mismeasured proxy.

In this review, we focus on methods that can be applied during model development. We adopt a modified taxonomy from a recent work34 and categorize the recent debiasing methods into two groups: distributional and algorithmic (Table 1). Distributional debiasing methods aim to change the underlying data distribution of the dataset to improve fairness, whereas algorithmic debiasing methods modify the training procedure or model architecture to ensure fairness. We excluded methods that collect extra data through crowdsourcing or other means of human annotation, as these approaches are usually more expensive or difficult to obtain in the biomedical domain.

| Distributional methods | *Data augmentation [35–45] | Increase size and diversity by generating synthetic data and can help anonymize source data to increase availability. |
| --- | --- | --- |
| Distributional methods | Data perturbation [46–49] | Increases the dataset diversity by altering demographic information on |

---

<!-- Page 12 -->

12

|   |   | existing data. Mostly applicable to text data. |
| --- | --- | --- |
|   | *Data reweighting [50,51] | Compensate under-represented subgroups by duplicating those samples. |
|   | *Federated learning [52,53] | Allow the central model to be exposed to data from various sources by merging training results from multiple centers. |
| Algorithmic methods | *Unsupervised representation learning [54–58] | Can be used to learn models that extract useful features with unlabeled small datasets. |
| Algorithmic methods | *Adversarial learning [59–63] | Removes bias by training the model to forget protected attributes. |
| Algorithmic methods | Disentangled representation learning [64–67] | Disentangles the learned representation into protected and target attributes, and promotes fairness and explainability by only using the target attribute. |
| Algorithmic methods | *Loss function [67–69] | Optimize the model directly to achieve fairness or equivalent constraint. |
| Algorithmic methods | Causality [70,71] | Identifies stable data relationships across various contexts to build models resilient to input changes and biases |

Table 1. List of debiasing model-driven methods for AI systems in CV, NLP, and biomedicine covered in this work

Note. * denotes that the method has been applied to address equity in the biomedicine domain.

### 3.2 Distributional methods in the biomedical domain and general domain

#### 3.2.1 Data augmentation

One approach to reducing bias in machine learning models is to balance the dataset, as training models with balanced and high-quality datasets may result in reduced bias. There are two ways to balance a dataset: remove data from dominant groups or add data in the under-represented group. Collecting new data, however, is often time-consuming and costly. Hence, a common approach is to create synthetic

---

<!-- Page 13 -->

13

data in the under-represented group using algorithms such as generative adversarial networks (GANs). This approach is also commonly referred to as data augmentation.

GANs are machine learning models that generate synthetic samples similar to a given input dataset.35 GANs typically consist of two main components: a generator model and a discriminator model. The generator model aims to generate samples similar to real data, while the discriminator model attempts to distinguish between real and generated samples. The two models are typically trained simultaneously, with the generator model attempting to fool the discriminator model and the discriminator model trying to correctly identify generated samples. This adversarial training process can lead to the generation of high-quality synthetic samples. There are many applications of GANs in ophthalmology, such as the generation of the synthetic fundus, optical coherence tomography (OCT), or fluorescein angiography images.36

Studies have shown success in augmenting the medical dataset with GANs to address the bias in the dataset. Burlina et al. used GANs to change the retinal pigmentation in retinal fundus images and create a more balanced dataset.37 Coyner et al. demonstrate that PGAN, a method that progressively increases the size of GAN models during training to stably produce large and high-quality images, is able to synthesize retinal vessel maps that better represent the distribution of plus disease compared to the original dataset, potentially reducing bias due to limited sample size.38 Conditional GANs allow infusion of external information when generating images, which can help counterbalance biased datasets by generating data in the less represented subgroups.39 In addition to addressing issues with data imbalance and sparsity, the images generated by GANs are distinguishable from the original dataset, potentially

---

<!-- Page 14 -->

14

reducing privacy concerns associated with sharing the generated data and enabling further research. GANs are also widely applied in CV as a debiasing data augmentation method.40,41 Diffusion models are also gaining popularity. Although such models have not been widely applied to debiasing, the nature of such generative models makes them similar to how GANs are used in debiasing. Diffusion models learn a function that recovers data from noise. In the training process, data such as images are first transformed into Gaussian, then back to images from Gaussian.42 The diffusion steps can be treated as a long Markov chain.

Prior work has also shown that using a text-guided prompt or a classifier for conditional image synthesis, which can be applied in debiasing a dataset, is promising.43,44 A recent work, RoentGen, explores the potential of latent diffusion models on Chest X-ray image generation.45 RoentGen is able to use a text prompt as a guide to synthesizing X-ray images and demonstrates that combining synthesized and real data achieves the highest accuracy. This is promising, as the method also can address dataset equity problems in the biomedicine domain.

### 3.2.2 Data perturbation

Data perturbation increases the diversity and balance of the dataset by adding “noise” to existing samples. Under the concept of data perturbation, CDA is a dataset debiasing method that involves adding crafted samples, usually through a template or heuristic.46,47 In NLP research, CDA is used to craft samples by replacing words that may cause bias with words that refer to under-represented groups. For instance, to reduce gender bias in training data, CDA would modify the phrase, “He is a doctor,” to

---

<!-- Page 15 -->

15

“She is a doctor,” to generate new samples in the dataset.46 Addressing the limitations of heuristic-based generation, a recent work makes use of a sequence-to-sequence model to generate perturbed sentences of high quality.48 The work of Burlina et al. can be viewed as a combination of CDA and GANs, whereby images of another protected attribute were generated through GANs.37 Similar to CDA, Minot et al. propose to remove gender-specific words in the dataset, and show that their model can achieve a fairer performance using the truncated HER on health-condition classifications49.

### 3.2.3 Data reweighting

A surprisingly popular approach is to duplicate the minority class data. Acknowledging that word embeddings generated from language models can be biased, Agrmon et al. duplicate clinical trials that include more female participants in the training data and gain a slight improvement in the female subclass in comorbidity classification, hospital length of stay and ICU readmission prediction.50 Similarly, Afrose et al. propose a double-prioritized bias correction that replicates the minority demographic subgroup to address data imbalance in mortality prediction.51

### 3.2.4 Federated Learning

Federated learning is a class of methods that uses multiple devices, often distant from each other, to train models. In federated learning, a central machine aggregates learning from other devices that are often referred to as clients. It has the benefit of preserving privacy while utilizing multiple data sources, addressing the data issue. A common source of bias in biomedicine comes from limited data sources or skewed

---

<!-- Page 16 -->

16

demographic distribution in the dataset. Federated learning allows data usage of various centers, potentially exposing the model to different demographic populations. One key to federated learning algorithms is aggregating weights returned from different devices. Using multiple fairness aggregation algorithms, Meerza et al. show that it is possible to learn a fair prediction on Alzheimer's Disease using spontaneous speech data from daily collections52. Federated Learning with a Centralized Adversary (FELICIA) is another method based on federated learning, and has shown effectiveness on skin lesion classification53. FELICIA makes the adversarial discriminator component of GAN as the central control, and the communication between the central discriminator and the clients only consists of synthetic images, preserving privacy while achieving fairness.

### 3.2.5 Discussion on distributional methods

Distributional methods offer solutions to the challenge of insufficient non-diverse data. Prior research has shown that techniques such as synthesizing dark-color retinal images or collaborating with different centers through federated learning can effectively address the issue of this challenge. Moreover, in the context of biomedicine NLP tasks, such as search retrieval and report generation, data perturbation techniques can also yield potential benefits.

GAN models have been widely studied and shown to have state-of-the-art results. However, studies have shown that they capture less diversity than other models, such as diffusion-based ones. It is often difficult and time-consuming to train GAN models, and they have a collapsing problem, whereby the generator model

---

<!-- Page 17 -->

17

produces a few images.43 In contrast, diffusion models are faster and more stable in training. Due to the long Markov chain process, however, the generation time is longer than in GAN models. The generated images may also contain existing biases in the training data, introduce new biases, and training on generated images may make the model worse72. Counterfactual data augmentation (CDA) methods, in comparison, are mostly rule-based; however, they are applicable to only text data. Duplicating data in the minority subgroups requires a lot of fine-tuning and would take a lot of time. An easier operation would be to implement different weights to samples. Both Agmon et al. and Afrose et al. explore different configurations of the number of times that minority data are duplicated, and the improvements are limited.50,51 .

While federated learning increases data diversity, applying this method in reality is often burdensome. Different centers may have different data formats and computation power. The communication between the central machine and clients is another bottleneck of applying federated learning.

### 3.3 Algorithmic methods in the biomedical domain and general domain

#### 3.3.1 Unsupervised learning

Bias can occur when the dataset is small, such as under-represented groups in a large dataset or datasets of rare diseases. Recent work proposes to address biases in the model by using Deep InfoMax or its variant, Augmented Multiscale Deep InfoMax (AMDIM).54,55 These architectures are designed to learn image representations in a self-supervised manner, using techniques such as predicting part of an image using the whole image, like a cloze task in computer vision. This self-supervised learning

---

<!-- Page 18 -->

18

approach allows the model to learn useful representations of the data without the need for external labels. The goal of Deep InfoMAX and AMDIM is to generate unique, view-invariant representations of images that also maintain local consistency across structural locations within the image.54,55 Burlina et al. find that using the representation learned by AMDIM, the performance of downstream tasks (such as disease prediction) was acceptable even when using relatively small training sizes; in addition, the performance degradation when using very small training sizes was less severe.56

Variational Auto-Encoder (VAE) is another commonly used unsupervised representation learning algorithm. This method learns by decomposing and reconstructing the input. Building from VAE, Conditional VAE (CVAE)57 introduces a variational posterior as an approximation of the true posterior. Using Conditional Variational Auto-encoder, Liu et al. propose a method to learn a fair prior distribution of the dataset, and show reduced bias in EHR modeling58.

### 3.3.2 Adversarial learning

Protected attributes, such as race, should not be used in algorithms as a feature.17 One way to debias AI models is to force them to not learn the protected attributes. Hard debiasing is a technique that reduces bias in a model's representations by training a linear classifier to predict the protected attributes. The technique propagates the sign-flipped gradient of the classifier that predicts the protected attributes. Through such adversarial training, the model avoids learning protected attributes, such as institution and gender,28 or forgets the learned protected attributes. Prior work in colorectal cancer prediction has shown that after debiasing, the

---

<!-- Page 19 -->

19

representation space is more invariant to the bias variables. In contrast, the baseline representation space shows a clear correlation between the protected attributes and the learned representation.59 There has also been success in reducing the effect of the biased features of deep learning models on histopathology images through adversarial training.60 Other than adversarial training or finetuning the whole model, Wu et al. propose FairPrune, a method to promote fairness by determining and pruning the subset of a model that is contributing to bias,61 and show that it is effective in dermatology disease classification. The authors use the second derivative of model parameters to quantify their importance and remove a certain percentage of parameters repeatedly until the target fairness metric is achieved.

Instead of using a sign-flipped gradient in adversarial learning, other methods, such as INP, can be used to remove the unwanted information learned by the classifier.62 This is done by iteratively projecting the representation that contains protected information into the null space of the classifier's weight matrix.

Following the philosophy of adversarial learning, Zanna et al. hypothesis that when the model is the most uncertain about protected labels, the weights of the model can be fully utilized for the task63. By estimating the model's uncertainty, they propose a bias mitigation technique for anxiety prediction that also preserves fairness.

### 3.3.3 Disentangled representation learning

A type of method related to content-style disentanglement is disentangled representation learning. Representations learned by AI systems are information or features extracted from data. Such representation is a combination of many features.

---

<!-- Page 20 -->

20

Disentangling representations into subspaces and excluding the subspace related to protected attributes can promote a fairer AI system. It is worth noting that disentangled representation learning has been used in the biomedicine domain to address problems such as disease decomposition, artifact reduction, harmonization, and so forth.73 Research, however, focuses mainly on methods that disentangle the style and content of images. Disentangled representation learning might be more effective (in terms of accuracy) in a low-resource setting; however, the improvement is limited.64 A prior work modified the vanilla variational autoencoder to produce flexibly fair representations that can be applicable in many datasets.65 Based on the concern that removing all protected attributes might reduce the model's performance, a common situation in the biomedical setting, others have proposed subcategorizing a mutual attribute latent space in addition to the target and protected attribute latent representation space, which allows for less loss of information.66

### 3.3.4 Loss function

Machine learning algorithms are trained to minimize their loss function. Thus, infusing a fairness constraint in the loss function can help learn a fair model. Using Rényi's divergence, Gronowski et al. derive a loss function via a variational approach to promote fairness in diabetic retinopathy detection67. Serna et al. propose a discrimination-aware loss function for face recognition algorithms based on a triplet loss function and a sensitive triplet generator68. Zafar et al. add a trackable constraint to limit model's decision boundaries and unfairness. By adding a fairness constraint to ensure

---

<!-- Page 21 -->

21

similar individuals are treated similarly, Dwork et al.'s method guarantees statistical parity69.

### 3.3.5 Causality

Causal invariant learning, a technique that identifies stable data relationships across varied environments, helps build models resistant to input biases and changes. A common theorem applied in causal invariant learning is backdoor adjustment74, which aims to eliminate the effect of spurious correlations that is often the reason for biased models. Following this theorem, Causal Intervention by Semantic Smoothing (CISS) learns the causal effect between text input and labels for robust predictions70. Causal Intervention by Instrumental Variable (CiIV) employs retinotopic sampling masks and consistency regularization loss, encouraging neural networks to prioritize causal features over local confounders, thereby boosting adversarial robustness in visual tasks71.

### 3.3.6 Discussion on algorithmic methods

Algorithmic methods inherently address bias issues from the model's perspective, offering a valuable approach to mitigating bias, especially in cases where data collection exhibits inherent bias. These methods serve to safeguard the model against the inadvertent exploitation of undesired distributional information, thereby promoting fairness and reducing the potential for bias-related issues.

Unsupervised representation learning with fill-in-the-blank tasks, such as a cloze task, is common in masked language model pretraining, such as BERT,75 and it has

---

<!-- Page 22 -->

22

been shown that this type of pretraining significantly improves convergence speed and performance for downstream tasks.76 The results from Burlina et al. show, however, that the improvement is not significant when the dataset is large, suggesting that the method improves performance only when the dataset is small.

Adversarial methods/algorithms that aim to remove sensitive information are difficult to train and are not so effective, as classifiers are still able to extract the protected attributes. Additional training after debiasing might improve the model's performance77; however, whether this will make the model regain the ability to learn protected attributes is unclear. Iterative null space projection (INP) does not guarantee the removal of desired attributes and may not work when the representation is fed into a non-linear classifier.

Loss function can be very sensitive to model architecture and regularization parameters. A loss function may work on one type of data but fail to converge on another.

A key limitation of causality-based methods lies in their dependency on the accuracy of the presumed causal relationships. Misidentifying or overlooking these relationships can significantly impact their effectiveness. For example, incorrectly assuming no causal relationships between breast cancer and sexuality will lead to inaccurate and ineffective methods.

### 3.4 Beyond model-oriented methods

While the primary emphasis of this study lies in model-oriented approaches, we also wish to underscore the significance of endeavors extending beyond these

---

<!-- Page 23 -->

23

methodologies. The literature we reviewed discussed methods that are not model oriented to address biases and fairness in AI systems applied in biomedicine. Indeed, the workflow of AI models, especially in the biomedical domain, involves not just model development but also data collection, system deployment, system operation, and so forth.

In addition to the model-oriented methods of addressing bias in AI systems, there are important aspects to consider, one of which is explainability or transparency, the ability of the algorithm to provide clear and understandable reasoning for its predictions or decisions. The lack of transparency in AI systems can make it difficult to determine whether the system is biased or to identify ways to address any existing biases.21 Improving transparency is also key to advancing the use of AI systems in clinical settings5,7,21,30,78; it can help to ensure that the algorithms are being used ethically and in a way that aligns with the goals of the healthcare system. Models such as recurrent neural networks and attention models can help to locate which part of a longitudinal EHR dataset is playing an important role in prediction, whereas saliency maps and SHapely Additive exPlanations (SHAP) have been utilized to identify which area of an image the model attends to in various tasks.22,59,78,79 Prior research has called for using fairness audits as a common practice instead of as reparments to the flaws of existing work.3 Protocols such as Prediction model Risk Of Bias ASsessment (PROBAST) and PROBAST-AI help researchers, clinicians, systematic reviewers, and policymakers to evaluate machine learning-based prediction model studies with standardized approaches to bias evaluation, allowing users to critically assess the quality of these studies and make more informed decisions about their utility.13,80 Data statements that

---

<!-- Page 24 -->

24

include the curation rationale and demographic characteristics of the dataset should also be included when datasets are published.51 We list the potential datasets that researchers can use to conduct fairness research in biomedical tasks in Table 2, and more datasets in the medical imaging domain can be found in the work of Xu et al. and Lara et al.3,19. We strongly recommend that future datasets be enriched by including anonymized demographic information, as this would allow for more nuanced and comprehensive analysis of the methods, and would help to ensure that research and analysis are conducted in a fair and ethical manner.

| Name | Modality | Gender | Age | Race/Ethnicity |
| --- | --- | --- | --- | --- |
| CheXpert 82 | Chest radiograph | √ | √ | √ |
| MIMIC.Chest X-Ray 83 | Chest radiograph with report | √ | √ | √ |
| ChestX-ray8 84 | Chest radiograph | √ | √ | X |
| UK Biobank 85 | Cardiac MRI | √ | √ | √ |
| RadFusion 86 | EHR and CT scans for pulmonary embolisms | √ | √ | √ |
| PaPILa 87 | Retinal fundus image and related medical data for glaucoma assessment | √ | √ | X |
| HAM10000 88 | Dermatoscopic images of common pigmented skin lesions | √ | √ | X |
| EchoNet-Pediatric 89 | Pediatric echocardiography | √ | √ | X |
| COVID-CT-MD 90 | CT scans for COVID-19 | √ | √ | X |
| ISIC 2020 91 | Dermatology images for skin lesions | √ | √ | X |

Table 2. Publicly available fairness research datasets that contain demographic information.

Such information could include age, gender, ethnicity, and other relevant factors.

It is also important to increase the diversity of datasets. The majority of the datasets used for training machine learning algorithms are sourced from high-income countries in Europe and North America, which introduces a bias, as the demographics of these countries do not accurately represent those of other regions, such as Africa,

---

<!-- Page 25 -->

25

Asia, and Latin America.3 As a result, the AI systems developed using these datasets may not be applicable or effective in other parts of the world. Existing methods for addressing bias due to imbalanced demographic distributions in datasets can help improve the fairness of AI systems. Increasing the diversity of groups represented in the dataset can further promote fairness and improve the performance of the models.

#### 4. DISCUSSION

In this work, we identify five major types of sources causing bias and unfairness in medical AI systems. Accurately pinpointing the specific source of this bias is crucial as it informs the choice of the most effective approach to counteract and diminish these biases. For instance, algorithmic methods can help address population bias. If the biases in medical imaging stem from images sourced from various centers and different device brands, a viable solution could be using disentangled representation methods for style transfer. A model that is exclusively trained on data gathered from a hospital predominantly serving white patients may not perform as effectively for other races. In such cases, the use of adversarial learning to forget demographic attributes from the model could help it focus more on disease characteristics and promote fairness.

Insufficient data, one of the potential causes of representation bias, is particularly acute in domains like biomedicine. Common tasks in CV or NLP can utilize untrained annotators, as models in the general domain aim to replicate abilities that most individuals possess. However, in biomedicine, data annotation often necessitates the involvement of highly skilled clinicians and physicians, which can be time-consuming and sometimes challenging to achieve inter-annotator consensus due to varying

---

<!-- Page 26 -->

26

standards across different centers. Distributional techniques can help mitigate these issues by generating controlled synthetic data to enhance and diversify the dataset, or by facilitating collaboration between different centers by utilizing data under federated learning protocols.

This is not to imply that certain techniques are solely capable of addressing specific bias sources. Instead, each approach possesses its own merits and limitations, and in practice, multiple sources of bias can happen at the same time. The purpose of this review is to discuss the potential of different methods and provide a possibility for future research.

AI research in biomedicine has not been adequately tested for bias. Further, studies may have a limited sample size and only be validated within a single institution or region, potentially restricting their external validity when applied to other populations or when tested by operators outside of the original study.1,2 A recent review that examined the design and the risk of bias in medical imaging found that only 54.3% of the studies surveyed provided validation with a different geographical dataset.92 In addition, large biomedical datasets often do not provide population characteristics. This lack of population characteristics in large datasets can hinder the ability to conclude the generalizability of the results to other populations, potentially introducing bias toward specific demographics.1

As AI becomes more prevalent, it is important to develop ethical guidelines to ensure that these technologies are used responsibly. The weight is not only on the technical side but also in the phases of system deployment, such as data collection, and on developers, system integrators, and operators.93 One way to develop ethical

---

<!-- Page 27 -->

27

guidelines is to provide physicians who use AI systems with education on the construction of these systems, the datasets they are based on, and their limitations, which can help to ensure that physicians are aware of the potential risks and benefits of using these technologies in their practice.94 Incorporating input from patients and communities through community advisory boards and patient advisory panels can also help ensure that AI systems are fair and representative of diverse backgrounds.95

## 5. CONCLUSION

As AI systems continue to be successfully implemented in various biomedicine applications, there is a growing need for research on biases in these systems. In the literature reviewed, only a small proportion of studies address algorithmic methods for addressing bias, with the majority focusing on policies.

Our review systematically covered literature only from January 2018 to December 2022. Although some works prior to this period are included, there might be more related works that are not included in this review. Our search was performed on PubMed, and other relevant articles that are not listed in the PubMed database may not be included. Our review does not cover topics related to bias metrics. There has been a lot of research in regard to designing different bias metrics, and reviews such as Xu et al. contain more details than this review.96

Although some debiasing methods have been applied in the biomedicine domain, there are other methods that have been used in general domains that may also be applicable in biomedicine. Different methodologies can be applied to different sources of bias, and identifying the exact source of bias is also crucial to addressing fairness in

---

<!-- Page 28 -->

28

biomedicine. In addition to technical considerations, factors such as dataset diversity, community engagement, and interpretability can significantly impact the performance and utility of AI systems in biomedicine and should be carefully considered in any analysis or implementation.

Acknowledgment: This work is supported by the NIH Intramural Research Program, National Library of Medicine.

## REFERENCES

1. 1 Liu X, Faes L, Kale AU,et al.A comparison of deep learning performance against health-care professionals in detecting diseases from medical imaging: a systematic review and meta-analysis.The Lancet Digital Health2019;1: e271–97.
2. 2 Tat E, Bhatt DL, Rabbat MG. Addressing bias: artificial intelligence in cardiovascular medicine.The Lancet Digital Health2020;2: e635–6.
3. 3 Ricci Lara MA, Echeveste R, Ferrante E. Addressing fairness in artificial intelligence for medical imaging.Nat Commun2022;13: 4581.
4. 4 Islam MdM, Poly TN, Walther BA, Yang HC, Li Y-C (Jack). Artificial Intelligence in Ophthalmology: A Meta-Analysis of Deep Learning Models for Retinal Vessels Segmentation.J Clin Med2020;9: 1018.
5. 5 Watson DS, Krutzinna J, Bruce IN,et al.Clinical applications of machine learning algorithms: beyond the black box.BMJ2019;364: 1886.
6. 6 Lai Q, Spoletrini G, Mennini G,et al.Prognostic role of artificial intelligence among patients with hepatocellular cancer: A systematic review.World J Gastroenterol2020;26: 6679–88.
7. 7 Artificial Intelligence and Surgical Decision-Making - PMC.https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7286802/(accessed Nov 30, 2022).
8. 8 Nakayama LF, Kras A, Ribeiro LZ,et al.Global disparity bias in ophthalmology artificial intelligence applications.BMJ Health Care Inform2022;29: e100470.
9. 9 Ferizi U, Honig S, Chang G. Artificial Intelligence, Osteoporosis and Fragility Fractures.Curr Opin Rheumatol2019;31: 368–75.
10. 10 Althubaiti A. Information bias in health research: definition, pitfalls, and adjustment methods.J Multidiscip Healthc2016;9: 211–7.

---

<!-- Page 29 -->

29

11 Meade N, Poole-Dayen E, Reddy S. An Empirical Survey of the Effectiveness of Debiasing Techniques for Pre-trained Language Models. 2022; published online April 2. DOI:10.48550/arXiv.2110.08527.

12 Lyu L, He X, Li Y. Differentially Private Representation for NLP: Formal Guarantee and An Empirical Study on Privacy and Fairness. In: Findings of the Association for Computational Linguistics: EMNLP 2020. Online: Association for Computational Linguistics, 2020: 2355–65.

13 Collins GS, Dhiman P, Andaur Navarro CL, et al. Protocol for development of a reporting guideline (TRIPOD-AI) and risk of bias tool (PROBAST-AI) for diagnostic and prognostic prediction model studies based on artificial intelligence. BMJ Open 2021; 11: e048008.

14 Zhao H, Gordon G. Inherent Tradeoffs in Learning Fair Representations. In: Advances in Neural Information Processing Systems. Curran Associates, Inc., 2019. https://papers.nips.cc/paper_files/paper/2019/hash/b4189d9de0fb2b9cce090bd1a15e3420-Abstract.html (accessed Dec 20, 2023).

15 Röösli E, Bozkurt S, Hernandez-Boussard T. Peeking into a black box, the fairness and generalizability of a MIMIC-III benchmarking model. Sci Data 2022; 9: 24.

16 Korot E, Pontikos N, Liu X, et al. Predicting sex from retinal fundus photographs using automated deep learning. Sci Rep 2021; 11: 10286.

17 Vyas DA, Eisenstein LG, Jones DS. Hidden in Plain Sight — Reconsidering the Use of Race Correction in Clinical Algorithms. N Engl J Med 2020; 383: 874–82.

18 Howard FM, Dolezal J, Kochanny S, et al. The impact of site-specific digital histology signatures on deep learning model accuracy and bias. Nat Commun 2021; 12: 4423.

19 Xu Z, Li J, Yao Q, Li H, Shi X, Zhou SK. A Survey of Fairness in Medical Image Analysis: Concepts, Algorithms, Evaluations, and Challenges. 2022; published online Nov 12. DOI:10.48550/arXiv.2209.13177.

20 Grote T, Keeling G. On Algorithmic Fairness in Medical Practice. Camb Q Healthc Ethics 2022; 31: 83–94.

21 Panch T, Mattie H, Atun R. Artificial intelligence and algorithmic bias: implications for health systems. J Glob Health; 9: 020318.

22 Sourlos N, Wang J, Nagaraj Y, van Ooijen P, Vliegenthart R. Possible Bias in Supervised Deep Learning Algorithms for CT Lung Nodule Detection and Classification. Cancers (Basel) 2022; 14: 3867.

23 Mehrahi N, Morstatter F, Saxena N, Lerman K, Galstyan A. A Survey on Bias and Fairness in Machine Learning. ACM Comput Surv 2021; 54: 115:1–115:35.

24 Suresh H, Guttag J. A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle. In: Equity and Access in Algorithms, Mechanisms, and Optimization. — NY USA: ACM, 2021: 1–9.

---

<!-- Page 30 -->

30

25 Dissecting racial bias in an algorithm used to manage the health of populations | Science. https://www.science.org.proxy-um.researchport.umd.edu/doi/10.1126/science.aax2342 (accessed Nov 17, 2022).

26 Johnson AEW, Pollard TJ, Shen L, et al. MIMIC-III, a freely accessible critical care database. Sci Data 2016; 3: 16035.

27 Beltagy I, Lo K, Cohan A. SciBERT: A Pretrained Language Model for Scientific Text. 2019; published online Sept 10. DOI:10.48550/arXiv.1903.10676.

28 Zhang H, Lu AX, Abdalla M, McDermott M, Ghassemi M. Hurtful Words: Quantifying Biases in Clinical Contextual Word Embeddings. 2020; published online March 11. DOI:10.48550/arXiv.2003.11515.

29 Thomasian NM, Eickhoff C, Adashi EY. Advancing health equity with artificial intelligence. J Public Health Policy 2021; 42: 602–11.

30 Nelson GS. Is Art Artificial Intelligence. North Carolina Medical Journal 2019; 80: 220–2.

31 Health TLD. Equitable precision medicine for type 2 diabetes. The Lancet Digital Health 2022; 4: e850.

32 Larrazabal AJ, Nieto N, Peterson V, Milone DH, Ferrante E. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis. Proc Natl Acad Sci USA 2020; 117: 12592–4.

33 Li J, Bzdek D, Chen J, et al. Cross-ethnicity/race generalization failure of behavioral prediction from resting-state functional connectivity. Sci Adv; 2022; eabj1812.

34 Parraga O, More MD, Oliveira CM, et al. Debiasing Methods for Fairer Neural Models in Vision and Language Research: A Survey. 2022; published online Nov 10. DOI:10.48550/arXiv.2211.05617.

35 Goodfellow I, Pouget-Abadie J, Mirza M, et al. Generative adversarial networks. Commun ACM 2020; 63: 139–44.

36 Chen JS, Coyner AS, Chan RVP, et al. Deepfakes in Ophthalmology. Ophthalmol Sci 2021; 1: 100079.

37 Burlina P, Joshi N, Paul W, Pacheco KD, Bressler NM. Addressing Artificial Intelligence Bias in Retinal Diagnostics. Transl Vis Sci Technol 2021; 10: 13.

38 Coyner AS, Chen JS, Chang K, et al. Synthetic Medical Images for Robust, Privacy-Preserving Training of Artificial Intelligence. Ophthalmol Sci 2022; 2: 100126.

39 Campello VM, Xia T, Liu X, et al. Cardiac aging synthesis from cross-sectional data with conditional generative adversarial networks. Front Cardiovasc Med 2022; p. 983091.

40 Bias Remediation in Driver Drowsiness Detection Systems Using Generative Adversarial Networks | IEEE Journals & Magazine | IEEE Xplore. https://ieeexplore.ieee.org/document/9042231 (accessed Dec 14, 2022).

41 Gambs S, Ngueveu RC. Fair mapping. 2022; published online Sept 1. DOI:10.48550/arXiv.2209.00617.

---

<!-- Page 31 -->

31

42 Sohl-Dickstein J, Weiss EA, Maheswaranathan N, Ganguli S. Deep Unsupervised Learning using Nonequilibrium Thermodynamics. 2015; published online Nov 18. DOI:10.48550/arXiv.1503.03585.

43 Dhariwal P, Nichol A. Diffusion Models Beat GANs on Image Synthesis. 2021; published online June 1. DOI:10.48550/arXiv.2105.05233.

44 Nichol A, Dhariwal P, Ramesh A, et al. GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models. 2022; published online March 8. DOI:10.48550/arXiv.2112.10741.

45 Chambon P, Bluethgen C, Delbrouck J-B, et al. RoentGen: Vision-Language Foundation Model for Chest X-ray Generation. 2022; published online Nov 23. DOI:10.48550/arXiv.2211.12737.

46 Lu K, Mardziel P, Wu F, Amancarla P, Datta A. Gender Bias in Neural Natural Language Processing. 2019; published online May 30. DOI:10.48550/arXiv.1807.11714.

47 Barikeri S, Lauscher A, Vulić I, Glavaš G. RedditBias: A Real-World Resource for Bias Evaluation and Debiasing of Conversational Language Models. In: Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers). Online: Association for Computational Linguistics, 2021: 1941–55.

48 Qian R, Ross C, Fernandes J, Smith E, Kiela D, Williams A. Perturbation Augmentation for Fairer NLP. 2022; published online Oct 12. http://arxiv.org/abs/2205.12586 (accessed Dec 14, 2022).

49 Minot JR, Cheney N, Maier M, Elbers DC, Danforth CM, Dodds PS. Interpretable Bias Mitigation for Textual Data: Reducing Genderization in Patient Notes While Maintaining Classification Performance. ACM Trans Comput Healthcare 2022; 3: 39:1–39:41.

50 Agmon S, Gillis P, Horvitz E, Radinsky K. Gender-sensitive word embeddings for healthcare. J Am Med Inform Assoc 2022; 29: 415–23.

51 Afrose S, Song W, Nemeroff CB, Lu C, Yao DD. Subpopulation-specific machine learning prognosis for underrepresented patients with double prioritized bias correction. Commun Med (Lond) 2022; 2: 111.

52 Ali Meerza SI, Li Z, Liu L, Zhang J, Liu J. Fair and Privacy-Preserving Alzheimer’s Disease Diagnosis Based on Spontaneous Speech Analysis via Federated Learning. In: 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). 2022: 1362–5.

53 Rajotte J-F, Mukherjee S, Robinson C, et al. Reducing bias and increasing utility by federated generative modeling of medical images using a centralized adversary. In: Proceedings of the Conference on Information Technology for Social Good. New York, NY, USA: Association for Computing Machinery, 2021: 79–84.

54 Bachman P, Hjelm RD, Buchwalter W. Learning Representations by Maximizing Mutual Information Across Views. .

55 Hjelm RD, Fedorov A, Lavoie-Marchildon S, et al. Learning deep representations by mutual information estimation and maximization. 2022. https://openreview.net/forum?id=BkIr3j0cX (accessed Dec 13, 2022).

---

<!-- Page 32 -->

32

56 Burlina P, Paul W, Mathew P, Joshi N, Pacheco KD, Bressler NM. Low-Shot Deep Learning of Diabetic Retinopathy With Potential Applications to Address Artificial Intelligence Bias In Retinal Diagnostics and Rare Ophthalmic Diseases. JAMA Ophthalmol 2020; 138: 1070–7.

57 Sohn K, Lee H, Yan X. Learning Structured Output Representation using Deep Conditional Generative Models. In: Advances in Neural Information Processing Systems. Curran Associates, Inc., 2015. https://papers.nips.cc/paper_files/paper/2015/hash/8d55a2496baa5c0677297520da2051-Abstract.html (accessed June 21, 2023).

58 Liu Z, Li X, Yu P. Mitigating health disparities in EHR via deconfounder. In: Proceedings of the 13th ACM International Conference on Bioinformatics, Computational Biology and Health Informatics. New York, NY, USA: Association for Computing Machinery, 2022: 1–6.

59 Bustos A, Payá A, Torrubia A, et al. xDEEP-MSI: Explainable Bias-Rejecting Microsatellite Instability Deep Learning System in Colorectal Cancer. Biomolecules 2021; 11: 1786.

60 Asilian Bidgoli A, Rahnamayan S, Dekhkharganian T, Grami A, Tizhoosh HR. Bias reduction in representation of histopathology images using deep feature selection. Sci Rep 2022; 12: 19994.

61 Wu Y, Zeng D, Xu X, Shi Y, Hu J. FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis. In: Wang L, Dou Q, Fletcher PT, Speidel S, Li S, eds. Medical Image Computing and Computer Assisted Intervention – MICCAI 2022. Cham: Springer Nature Switzerland, 2022: 743–53.

62 Ravfogel S, Elazar Y, Gonen H, Twiton M, Goldberg Y. Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. Online: Association for Computational Linguistics, 2020: 7237–56.

63 Zanna K, Sridhar K, Yu H, Sano A. Bias Reducing Multitask Learning on Mental Health Prediction. In: 2022 10th International Conference on Affective Computing and Intelligent Interaction (ACII). Nara, Japan: IEEE, 2022: 1–8.

64 Liu X, Thermos S, Valvano G, Chartsias A, O’Neil A, Tsafaris SA. Measuring the Biases and Effectiveness of Content-Style Disentangling. 2021; published online Sept 15. http://arxiv.org/abs/2008.12378 (accessed Jan 3, 2023).

65 Creager E, Madras D, Jacobsen J-H, et al. Flexibly Fair Representation Learning by Disentangling. .

66 Park S, Hwang S, Kim D, Byun H. Learning Disentangled Representation for Fair Facial Attribute Classification via Fairness-aware Information Alignment. Proceedings of the AAAI Conference on Artificial Intelligence 2021; 35: 2403–11.

67 Gronowski A, Paul W, Alajaji F, Ghareisfard B, Burlina P. Rényi Fair Information Bottleneck for Image Classification. In: 2022 17th Canadian Workshop on Information Theory (CWIT). Ottawa, ON, Canada: IEEE, 2022: 11–5.

68 Serna I, Morales A, Fierrez J, Obradovich N. Sensitive loss: Improving accuracy and fairness of face representations with discrimination-aware deep learning. Artificial Intelligence 2022; 305: 103682.

---

<!-- Page 33 -->

33

69 Dwork C, Hardt M, Pitassi T, Reingold O, Zemel R. Fairness through awareness. In: Proceedings of the 3rd Innovations in Theoretical Computer Science Conference. New York, NY, USA: Association for Computing Machinery, 2012: 214–26.

70 Zhao H, Ma C, Dong X, Liu AT, Deng Z-H, Zhang H. Certified Robustness Against Natural Language Attacks by Causal Intervention. 2022; published online Oct 14. DOI:10.48550/arXiv.2205.12331.

71 Tang K, Tao M, Zhang H. Adversarial Visual Robustness by Causal Intervention. 2021; published online Oct 6. DOI:10.48550/arXiv.2106.09534.

72 Shumailov I, Shumaylov Z, Zhao Y, Gal Y, Papernot N, Anderson R. The Curse of Recursion: Training on Generated Data Makes Models Forget. 2023; published online May 31. DOI:10.48550/arXiv.2305.17493.

73 Liu X, Sanchez P, Thermos S, O’Neil AQ, Tsafaris SA. Learning disentangled representations in the imaging domain. Medical Image Analysis 2022; 80: 102516.

74 Pearl J. Causality. Cambridge university press, 2009.

75 Devlin J, Chang M-W, Lee K, Toutanova K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. .

76 Wang T, Roberts A, Hesslow D, et al. What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization? 2022; published online April 12. http://arxiv.org/abs/2204.05832 (accessed March 1, 2023).

77 Correa R, Jeong JJ, Patel B, Trivedi H, Gichoya JW, Banerjee I. Two-step adversarial debiasing with partial learning – medical image case-studies. 2021; published online Nov 16. DOI:10.48550/arXiv.2111.08711.

78 Lee EE, Torous J, De Choudhury M, et al. Artificial Intelligence for Mental Healthcare: Clinical Applications, Barriers, Facilitators, and Artificial Wisdom. Biol Psychiatry Cogn Neurosci Neuroimaging 2021; 6: 856–64.

79 A unified approach to interpreting model predictions | Proceedings of the 31st International Conference on Neural Information Processing Systems. 2023; published online Dec 15, 2022. https://dl.acm.org/doi/10.5555/3295222.3295230 (accessed Dec 15, 2022).

80 Moons KGM, Wolff RF, Riley RD, et al. PROBAST: A Tool to Assess Risk of Bias and Applicability of Prediction Model Studies: Explanation and Elaboration. Ann Intern Med 2019; 170: W1–33.

81 Bender EM, Friedman B. Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science. Transactions of the Association for Computational Linguistics 2018; 6: 587–604.

82 Irvin J, Rajpurkar P, Ko M, et al. CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison. AAAI 2019; 33: 590–7.

---

<!-- Page 34 -->

34

83 Johnson AEW, Pollard TJ, Greenbaum NR, et al. MIMIC-CXR-JPG, a large publicly available database of labeled chest radiographs. 2019; published online Nov 14. DOI:10.48550/arXiv.1901.07042.

84 Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-Scale Chest X-Ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases. .

85 Petersen SE, Matthews PM, Francis JM, et al. UK Biobank's cardiovascular magnetic resonance protocol. Journal of Cardiovascular Magnetic Resonance 2016; 18: 8.

86 Zhou Y, Huang S-C, Fries JA, et al. RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR. 2021; published online Nov 26. http://arxiv.org/abs/2111.11665 (accessed March 10, 2023).

87 Kovalyk O, Morales-Sánchez J, Verdú-Monedero R, Sellés-Navarro I, Palazón-Cabanes A, Sancho-Gómez J-L, PAPIA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment. Sci Data 2022; 9: 291.

88 Tschandl P, Rosendahl C, Kittler H. The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Sci Data 2018; 5: 180161.

89 Reddy CD, Lopez L, Ouyang D, Zou YJ, He B. Video-Based Deep Learning for Automated Assessment of Left Ventricular Ejection Fraction in Pediatric Patients. J Am Soc Echocardiogr 2023; : S0894-7317(23)00068-8.

90 Afshar P, Heidarian S, Enshaei N, et al. COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning. Sci Data 2021; 8: 121.

91 Rotemberg V, Kurtansky N, Betz-Stablein B, et al. A patient-centric dataset of images and metadata for identifying melanomas using clinical context. Sci Data 2021; 8: 34.

92 Nagendran M, Chen Y, Lovejoy CA, et al. Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies. BMJ 2020; 368: m689.

93 Tabassi E (Fed). AI Risk Management Framework: Second Draft - August 18, 2022. 2022.

94 Char DS, Shah NH, Magnus D. Implementing Machine Learning in Health Care — Addressing Ethical Challenges. N Engl J Med 2018; 378: 981–3.

95 Clark CR, Wilkins CH, Rodriguez JA, et al. Health Care Equity in the Use of Advanced Analytics and Artificial Intelligence Technologies in Primary Care. J GEN INTERN MED 2021; 36: 3188–93.

96 Xu J, Xiao Y, Wang WH, et al. Algorithmic fairness in computational medicine. EBioMedicine 2022; 84: 104250.