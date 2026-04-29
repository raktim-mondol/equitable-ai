

<!-- PAGE 1 -->

www.nature.com/scientificreports

# scientific reports

Check for updates

## OPEN Generalization of vision pre-trained models for histopathology

Milad Sikaroudi
^1^
, Maryam Hossieni
^1^
, Ricardo Gonzalez
^2,3^
, Shahrhaz Rahmanian
^1,2^
 & H. R. Tizhoosh
^1,2,4,5^

Out-of-distribution (OOD) generalization, especially for medical setups, is a key challenge in modern machine learning which has only recently received much attention. We investigate how different convolutional pre-trained models perform on OOD test data—that is data from domains that have not been seen during training—on histopathology repositories attributed to different trial sites. Different trial site repositories, pre-trained models, and image transformations are examined as specific aspects of pre-trained models. A comparison is also performed among models trained entirely from scratch (i.e., without pre-training) and models already pre-trained. The OOD performance of pre-trained models on natural images, i.e., (1) vanilla pre-trained ImageNet, (2) semi-supervised learning (SSL), and (3) semi-weekly-supervised learning (SWSL) models pre-trained on IS-18-Targeted are examined in this study. In addition, the performance of a histopathology model (i.e., KiNetaNet) trained on the most comprehensive histopathology dataset, i.e., TCGA, has also been studied. Although the performance of SSL and SWSL pre-trained models are conducive to better OOD performance in comparison to the vanilla ImageNet pre-trained model, the histopathology pre-trained model is still the best in overall. In terms of top-1 accuracy, we demonstrate that diversifying the images in the training using reasonable image transformations is effective to avoid learning shortcuts when the distribution shift is significant. In addition, XAI techniques—which aim to achieve high-quality human-understandable explanations of AI decisions—are leveraged for further investigations.

With artificial neural networks, model weights can be fitted to data to generate high-precision outputs, but generalization to unseen data remains challenging. These types of challenges can be addressed under different terminologies in the literature. Some works state that unsatisfactory out-of-distribution (OOD) generalization stems from learning shortcuts
^1–3^
 or biases
^4–6^
. Some other works focus on OOD generalization from a rather different perspective stating that existing domain shift between source and target domains is the reason behind a low OOD performance
^7,8^
.

We can summarize different nomenclatures describing generalization issues as follows:

- **Bias***Definition:*Inherent or acquired prejudice or favoritism toward an entity or group of entities known as bias, or unfairness^9^.*Example:*Correctional Offender Management Profiling for Alternative Sanctions (COMPAS) determines whether an offender is likely to commit another crime after being sentenced. COMPAS is used by judges to decide whether to release an offender or keep him or her in prison. The software was found to be biased against African-Americans after an investigation^10^.*Literature:*^11–14^
- **Outcome: Inducing the generalization issue on unseen data.**
- **Shortcuts***Definition:*A shortcut is a decision rule that performs well on independent and identically distributed (i.i.d.) test data but fails on OOD test data, resulting in a mismatch between what is intended and what has been learned.*Example:*There is a tendency for cows in unexpected environments (such as beaches instead of grasslands) to be misclassified since the background can be just as significant for recognition as the cow itself^15^.*Literature:*^1–3^

^1^
Kimia Lab, University of Waterloo, Waterloo, ON, Canada. 
^2^
Department of Laboratory Medicine and Pathology, Mayo Clinic, Rochester, MN, USA. 
^3^
Engineering Department, Brock University, St. Catharines, ON, Canada. 
^4^
Whites Lab, Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN, USA. 
^5^
email: tizhoosh.ram@mayo.edu

Scientific Reports | (2023) 13:605

https://doi.org/10.1038/s41598-023-33348-z

nature portfolio

<!-- PAGE 2 -->

Outcome: Inducing the generalization issue on unseen data.

- Domain/distribution shift**Definition:**In the context of transfer learning any differences between the source and target domain data is known as domain shift.**Example:**Differences in images due to sampling bias, differences in image content or view angle, or differences in image characteristics such as brightness, noise or color.**Literature:**^2,3^
- **Definition:**In the context of transfer learning any differences between the source and target domain data is known as domain shift.
- **Example:**Differences in images due to sampling bias, differences in image content or view angle, or differences in image characteristics such as brightness, noise or color.
- **Literature:**^2,3^
- Outcome: Inducing the generalization issue on unseen data.

In histopathology, Higgle et al.
^4^
 categorized 3 different types of biases in histopathology setups as below:

- Dataset biasFor example, only a small portion of each image is correlated with its class label. For instance, a small central region of each image represents the class label and the remaining parts are irrelevant. In this scenario, the deep network cannot generalize to test images in which subjects do not necessarily lie at the center.Label biasBias that are by chance correlated with class labels. If an image of a particular class has a unique red spot for instance, it may end up in a deep network that does not generalize to images lacking this distinctive spot.Sampling biasThe absence of certain critical tissue textures, such as necrosis, in the training, can lead to performance degradation in deep networks when testing them on not-seen textures.
- For example, only a small portion of each image is correlated with its class label. For instance, a small central region of each image represents the class label and the remaining parts are irrelevant. In this scenario, the deep network cannot generalize to test images in which subjects do not necessarily lie at the center.
- Label biasBias that are by chance correlated with class labels. If an image of a particular class has a unique red spot for instance, it may end up in a deep network that does not generalize to images lacking this distinctive spot.
- Bias that are by chance correlated with class labels. If an image of a particular class has a unique red spot for instance, it may end up in a deep network that does not generalize to images lacking this distinctive spot.
- Sampling biasThe absence of certain critical tissue textures, such as necrosis, in the training, can lead to performance degradation in deep networks when testing them on not-seen textures.
- The absence of certain critical tissue textures, such as necrosis, in the training, can lead to performance degradation in deep networks when testing them on not-seen textures.

Although they have coined their own nomenclature for biases, but all their types of biases are commonly known as shortcuts in the machine learning community which can result in a deep network with a low OOD while proper in-distribution performance. In addition to categorizing different types of biases in histopathology setups, they have demonstrated the effectiveness of explainable AI techniques to visualize the biases.
^1^

Overall, it is critical to ensure a reliable deployment of deep models in real-life environments if there is a distribution shift, evident in differences in source and target data. For example, differences in acquisition pipelines between trial sites, or over time, may introduce a domain shift in digital pathology due to subtle and perhaps visually not apparent differences among WSI.

A deeper understanding of distribution shift and its consequences is required to harness the significant potential offered by deep learning in histopathology. Actions need to be taken to ensure that a model's predictions can be trusted when new data is introduced. Although correctly modeling and responding to data not seen during training is indeed a difficult problem, a few methods have recently been proposed to improve OOD generalization.

Multi-domain learning regimes (
*domain generalization and domain adaptation*
) leverage specialized training methods for OOD generalization. These types of techniques are mainly categorized into three types of methods for OOD data during training
^10,11^
: (2) learning invariant representations
^12^
; and (3) creating adversarial data acquisition scenarios
^13^
.

Even though domain generalization is a relatively well-studied field
^14^
, some works have cast doubt on the effectiveness of existing methods
^15,16^
. For example, Willett et al.
^17^
 focused on three types of shifts in distributions, (1) spurious correlations, (2) low-data shifts, and (3) unseen shifts. Although their results were more mixed than conclusive, they suggested that simple techniques such as data augmentation and pre-training are “often effective.” They also demonstrated that domain generalization algorithms are effective for certain domains and distribution shifts. They showed that the best approach cannot be selected a priori, and results differ over different datasets and attributes, demonstrating the need to further improve the algorithmic robustness in real-world settings. Therefore, it would be reasonable to ask whether domain generalization has progressed over a standard Expectation Risk Minimization (ERM) framework, while those results are discouraging for pre-trained models
^18^
.

Demonstrating that machine learning models can be generalized across datasets with different distributions
^19,20^
. For instance, some works advocate that pre-training on large datasets is effective for OOD generalization
^21,22^
. This paper presents a systematic investigation of pre-trained models for OOD generalization. Extensive experiments are conducted on different types of pre-trained models (trained with either natural images or histopathology images) with leave-one-hospital-out cross-validation. It means each of the WSI repositories associated with each hospital is held out in turn, and then the pre-trained models are fine-tuned using the remaining WSI repositories for the underlying task. To enable higher OOD generalization, our study focuses not on achieving state-of-the-art results on a benchmark dataset, but rather on a better understanding of how few-pre-trained models ensure proper OOD generalization. The rest of this research should provide new insights into bridging the in-distribution and OOD gap for future research endeavors. Our contribution is three-fold:

1. In the context of OOD generalization, we show that even though pre-training on large datasets is critical (Semi-Weakly Supervised Learning (SWSL)^23^and Semi-Supervised Learning (SSL)^24^versus vanilla ImageNet^25^pre-trained models), the natural pre-trained model is crucial as well (Kim et al.^26^, SWSL^27^and SSL^28^). A lack of one of these components may degrade OOD generalization according to our experiments.
2. With fixed-policy augmentations, OOD generalization can be improved by relying less on shortcuts and focusing more on semantically interpretable features. There is, however, a risk of complicating the deep network training as well. In other words, fixed-policy augmentation can be a friend or a foe. It all depends

<!-- PAGE 3 -->

on the OOD test data and we may not assume a fixed-policy augmentation a priori that works for all conditions.

3. There are cases in which improving distribution performance may deteriorate OOD performance, showing that in-distribution performance may not be a reliable indicator of OOD performance necessarily.

In the following, we introduce different types of pre-trained models that have been investigated in this study.

### Vanilla pre-trained models using ImageNet

The pre-training paradigm is dominant in computer vision because many tasks are very related, and it makes sense that a model trained on one dataset would help with another. As a result, the vanilla ImageNet pre-trained models, i.e., supervised learning on ImageNetK49, have been dominating the literature for various computer vision tasks
^20, 21^
. Although mainly successful, some reports cast a shadow over the usefulness of vanilla ImageNet pre-trained models. For instance, Shen et al.
^22^
 demonstrated that vanilla ImageNet pre-training fails when we consider a much different task such as Microsoft COCO object detection
^23^
. Furthermore, using strong regularization, Ghiasi et al.
^24^
 found that a model trained with random initialization outperforms the ImageNet pre-trained model in COCO object detection. Thus, it seems one should not rely heavily on vanilla pre-trained models.

### SSL and SWSL pre-trained models

The common sense in the AI community is that a more diverse dataset for pre-training would lead to better OOD generalization. Moreover, there have been some strong pieces of evidence that pre-trained models on more diverse datasets achieve better OOD generalization in real-life distribution shifts
^25–27^
. For instance, there are some types of pre-trained models
^28^
 that have shown better performance than vanilla ImageNet pre-trained models in terms of OOD and in-distribution top-1 accuracy levels (the one with the highest probability). Among those, two promising approaches have been introduced. (1) SSL
^29^
 pre-trained models, i.e., pre-training on a subset of the unlabeled YFCC100M public image dataset
^30^
 and fine-tuned with the ImageNet1K training dataset. (2) SWSL
^31^
 pre-trained models, i.e., training on 340 million public images with 1.5 K hashtags and 1000 ImageNet1K synsets, followed by fine-tuning on ImageNet1K. Therefore, in this study, we investigate these types of pre-trained models to see how they perform in presence of distribution shift across different histopathology image repositories.

### KimiaNet pre-trained model

It is worth testing a deep model that has been pre-trained for histopathology. Compared to models trained with natural images, one might expect better performance from such networks. KimiaNet
^32^
 is a pre-trained model which has borrowed the DenseNet topology
^33^
 and has been trained on the most diverse, multi-organ public image repository, namely The Cancer Genome Atlas (TCGA) dataset. The details of the pre-trained models in this study has been reported in Table 1.

### Experimental setup and methods

In most cases, the datasets for studying OOD performance on histopathology setups come from TCGA
^34–36, 37^
. Given that KimiaNet
^32^
 has already been trained on all WSIs on TCGA data, we may not define the OOD test set from that dataset. Hence, our options are to further narrowed down to other datasets. CAMELYON17 is a proper option because it contains data from various hospitals. In the following section, we describe the data and models used in our study, followed by the setup of the experiments.

### CAMELYON17 dataset

The CAMELYON17 dataset
^38^
 contains 1000 WSIs collected from five medical centers. These WSIs have not only various conditions in stain colors
^39^
 but also variations in morphology and tumor staging across the trial sites
^40–42^
 (see Fig. 1). A total of 500 WSIs were used for training in the CAMELYON17 challenge, and the remaining 500 WSIs were used for testing. The training dataset of CAMELYON17 consists of 318 negative WSIs and 182 WSIs with metastases. Since only 50 WSIs of all the slides contained pixel-level annotations, only these 50 slides were sampled for tumor and non-tumor cells. Samples of non-tumor cells from the remaining slides might introduce some more variations; however, they are not likely to have a significant effect on the result
^43^
. Tumor areas often cover only a minor fraction of the slide area, contributing to a substantial patch-level imbalance. To address this imbalance issue, we applied a patch sampling strategy similar to that in
^44^
. Specifically, we sample the same number of tumor/normal patches on each slide with a uniform distribution of patches. Finally, for each hospital, we ended up with approximately 3000 patches, half of which are tumors and half non-tumors.

| Pre-trained model | Architectures | Pre-trained on | ImageNet |
| --- | --- | --- | --- |
| Vanilla | ResNet18^45^ | ImageNet | 512 |
| SSL | ResNet18^45^ | IG-1B-Target, ImageNet | 512 |
| SWSL | ResNet18^45^ | IG-1B-Target, ImageNet | 512 |
| KimiaNet | DenseNet121^33^ | Subsary of TCGA WSIs | 1024 |

<!-- PAGE 4 -->

www.nature.com/scientificreports/

**Figure 1.**
 The bulk RGB histogram of the 512 × 512 extracted patches as well as sample tumor and non-tumor patches of each center/hospital in the CAMELYON17 dataset. Hospitals 3 and 5 have quite different histograms in comparison to the rest of the hospitals.

**OOD hospital and data chunks.**
 In this study, for each hospital, i.e., 
H_{H_{train}}
 using leave-one-hospital-out, the backbone is only trained using the images of remaining hospitals, i.e., 
H_{H_{train}}
. The 
H_{H_{train}}
 is then split into training, validation, and in-distribution test set with 70, 10, and 20% chunks, respectively. The accuracy on the 
H_{H_{train}}
 or OOD top-1 accuracy and in-distribution top-1 accuracy are calculated during the training at each epoch.

**Different scenarios for the training data.**
 Here, we propose different scenarios for fine-tuning or training the models in our experiments. In this aim, three different scenarios for the training are assessed according to Fig. 2 as follows:

- **Scenario 1:**The training images, i.e.,H_{H_{train}}are fed to the network without any changes.
- **Scenario 2:**Several types of distortions in histopathology setups (see Fig. 2) are simulated and randomly (uniformly) applied toH_{H_{train}}before inputting these images to the deep network. These transformations are as follows:

- HE jitter^17^randomly perturbs the HED color space value on an RGB histopathology image. Firstly, the hematoxylin and eosin color channels are separated by a color deconvolution method^18^. Following that, the hematoxylin, eosin, and Diaminobenzidine (DAB) stains are perturbed independently. In the end, the resulting stains are transformed into regular RGB color space. These perturbations are expected to make the model stain invariant.

<!-- PAGE 5 -->

**Scenario 1**
 Images without change

**Transformations**

**Scenario 2**
 Diversifying images by transformations

**Scenario 3**
 Shortcut overlaid

**Figure 2.**
 A sample training batch for different scenarios. Note that the patches in scenario 1 train sets did not undergo any augmentation. As it can be seen, among identity, HE2 jitter, color jitter, and Gaussian blurring transformations with uniform distribution (
p=0.25
), in scenario 2, one transformation is picked for each image in the batch. In scenario 3, the correct label (0: non-tumor, 1: tumor) of each image is overlaid on the image itself.

- Color jitter directly perturbs the image attributes including brightness, contrast, and saturation to increase image diversity so that the model is more robust to variations in color.
- Gaussian blurring adds some blurring using a Gaussian kernel with a specific radius.
- Identity does not make any changes to the input images.

**Scenario 3.**
 A digit (0: non-tumor and 1: tumor) corresponding to the label of images are overlaid on the top left corner of each image according to Fig. 2. We kept aside this experiment for the later sections when the shortcut learning is discussed.

**Training the pre-trained models.**
 The vanilla ImageNet pre-trained model as well as SSL
^13^
 and SWSL
^13^
 pre-trained models, all on the ResNet18 backbone
^66^
, have been used and assessed. In addition to pre-trained models on natural images, the KimiaNet pre-trained model
^67^
, which is a domain-specific (histopathology) model, has also been assessed.

For all the experiments, according to
^68,69^
, the total batch size was 32, and base learning rate was set to 0.01 for the training-from-scratch cases, and 0.001 for the pre-training cases along with step-LR schedule of 7 steps and 
\gamma=0.1
. Stochastic Gradient Descent (SGD) optimizer, a frequently used optimizer in the literature
^69^
, was used for the training with the weight decay value of 
1e^{-4}
.

**Results and discussion**

During the experiments, it was observed that the in-distribution test accuracy was increasing almost smoothly during the training, while the OOD top-1 accuracy did not follow the same pattern. The underlying reason behind oscillating OOD top-1 accuracy across the epochs is that most likely during the training, a combination of both semantic and non-semantic features are learned. The non-semantic (or hospital-specific) features would counter-intuitively degrade the generalization of the OOD test data. In what follows, we compare different types of pre-trained models in terms of OOD performance.

<!-- PAGE 6 -->

**OOD performance of the pre-trained models.**
 From scratch versus pre-trained. The first observation was that pre-trained models outperform training from scratch on average by 3%. According to Table 2, the difference between training from scratch and pre-training is significant. One might conclude that using any types of reasonably pre-trained models is better than training from scratch when it comes to the OOD performance. This finding has already been reported in
^45^
.

For the training from scratch cases, according to Table 2, scenario 2 outperforms scenario 1 in most cases. For the pre-trained models, according to Table 2, scenario 2 outperformed scenario 1 when the hold-out dataset was hospital 2, 3, or 5. In other words, by starting from proper initial weights (pre-trained), adding complications (augmentation/diversification) to training would result in a more generalized model. In contrast, if the deep network does not start with a proper initial weight (training from scratch), adding complexity to training would confuse it and cause it to deviate from learning meaningful and semantic features.

**Vanilla versus SSL and SWSL.**
 In Table 2, the maximum performance on each hold-out hospital has been highlighted. Neither training from scratch nor the vanilla pre-trained model has been highlighted in none of the cases. It can be observed that SSL
^46^
 and SWSL
^47^
 pre-trained models are decent alternatives for the vanilla pre-trained model. This can be justified since these two pre-trained models (i.e., SSL
^46^
 and SWSL
^47^
) have been pre-trained on a larger and more representative dataset enabling them to preserve more generic features. There have been some experiments in which training with scenario 2 has degraded OOD performance, for example, when hospital 2 was the hold-out set. Considering that this hospital has a smaller number of images than other hospitals (>2000 vs >3000), it may be suggested that image classification/augmentation lowers performance as it increases the risk of complicating training of the deep network.

**KimiaNet.**
 Table 3 summarizes the result of the KimiaNet for (1) linear probing
^48^
 (which freezes the feature extractor and trains only the classification head), and for (2) fine-tuning (all the model parameters are updated). As apparent from Table 3, the results of the fine-tuning outperformed linear probing. The average results in both splits 2, 3, and 5 are lower and more variable in comparison to hospitals 1 and 4. Training using scenario 2 has outperformed scenario 1 when the hold-out site was hospital 1, 3, and 5.

Considering both Tables 2 and 3, KimiaNet outperformed all the other pre-trained models at least for three of five external validations. Hence, the domain-specific (histopathology) pre-trained model is conducive to better OOD generalization. Although linear probing, in both scenario 1 and scenario 2 cases, has outperformed training from scratch, it has underperformed all the fine-tuning cases regardless of the utilized pre-trained model.

**Hospitals 3 and 5 OOD versus in-distribution performance.**
 The variation in accuracy and performance in Tables 2 and 3 between pre-trained models and training from scratch for hold-out hospitals from training from scratch shows that deep networks perform the least among the other holdout hospitals when hospitals 2, 3, and 5 are the hold-out hospitals. Hospital 2 in comparison to the other hospitals has a lower amount of patches (<2000 vs >3000) so the variability of results and lower performance when it is used as the hold-out OOD hospital.

| Pre-training | Weight | Training scenario | Hospital 1 | Hospital 2 | Hospital 3 | Hospital 4 | Hospital 5 | Average |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F | Random | S1 | 89.02 | 84.95 | 84.95 | 91.06 | 81.08 | 86.19 |
| F | Random | S2 | 92.73 | 90.28 | 82.01 | 92.02 | 86.73 | 87.14 |
| T | Vanilla | S1 | 98.75 | 96.03 | 94.42 | 96.63 | 90.54 | 95.12 |
| T | Vanilla | S2 | 99.14 | 93.6 | 97.98 | 97.13 | 96.52 | 96.86 |
| T | SSL | S1 | 98.82 | 96.92 | 94.8 | 97.06 | 96.61 | 96.91 |
| T | SSL | S2 | 99.18 | 94.98 | 95.09 | 97.29 | 97.23 | 96.84 |
| T | SWSL | S1 | 99.08 | 96.52 | 94.87 | 96.55 | 93.83 | 95.65 |
| T | SWSL | S2 | 99.31 | 96.19 | 97.44 | 98.09 | 98.71 | 96.13 |
|  | Average | 97.43 | 95.5 | 94.22 | 95.6 | 93.8 | 94.8 |

| Fine-tuning vs. Linear-probing | Training scenario | Hospital 1 | Hospital 2 | Hospital 3 | Hospital 4 | Hospital 5 | Average |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fine-tuning | S1 | 98.75 | 96.6 | 96.44 | 98.38 | 95.54 | 97.21 |
| Fine-tuning | S2 | 99.18 | 95.99 | 96.31 | 98.45 | 96.45 | 97.86 |
| Linear-probing | S1 | 97.59 | 86.77 | 92.45 | 95.58 | 80.57 | 91.25 |
| Linear-probing | S2 | 96.77 | 86.77 | 94.73 | 96.7 | 91.62 | 93.3 |
| Average |  | 98.15 | 94.87 | 95.23 | 97.34 | 91.47 | 94.7 |

<!-- PAGE 7 -->

is in factifiable. However, there is a need to investigate hospitals 3 and 5 since their variability can indicate that these two medical centers are likely to have a disproportionate distribution shift from others. The OOD versus in-distribution accuracies has been plotted according to Fig. 3.

Better OOD performance is preferred when it comes to real-world applications. Among different pre-trained models, we can see that when the hold-out set was hospital 3, KimiaNet outperformed other pre-trained models in terms of OOD performance: SWSL
^1
, vanilla, and SSL
^2
 pre-trained models. In the next places when training using scenario 2 is considered. However, in scenario 1 KimiaNet secured the first rank, and SWSL, SSL, and vanilla pre-trained models came after respectively.

Another observation was that training using scenario 2 improves OOD performance better than scenario 1 while worsens in-distribution performance for all types of pre-trained models. In other words, the transformations used in scenario 2 are effective in improving OOD performance while they caused degradation in the in-distribution performance. This implies that in-distribution accuracy cannot be an indicator of OOD performance necessarily. For instance, the KimiaNet model has the worst in-distribution performance while the best OOD performance. It is also a noteworthy point that KimiaNet in scenario 1, when the hold-out hospital was hospital 3, has the best in-distribution and OOD performance while scenario 2 boosted the scenario 1 at the cost of degrading in-distribution performance. This is the case for short-cut learning since the shortcuts, based on our general understanding, make satisfactory in-distribution performance while degrading OOD performance. Hence, we further study this case using XAI techniques to shed light on possible shortcuts.

### Uncovering shortcut learning.

Neural networks (or any machine learning algorithm) generally implement decision rules that define a relationship between input and output, e.g., assigning a category to each input image in classification tasks. Relying on shortcuts, the network performs well on training and in-distribution tests but not on OOD tests, indicating a mismatch between intended and learned solutions
^3
.

**Short-cut vs. bias.**
 In machine learning, bias is any kind of favoritism toward an entity
^4
. Favoritism can be directed toward a specific race, or it can be directed toward particular data from a specific hospital, or even some data with specific characteristics. These types of favoritism may not lead to shortcuts, but it may be assumed that a bias exists when just the images from a single specific trial site are included in the training of the deep network. As a result, we would train a biased deep network that could only perform decently on OOD test images. The diversity of the images in that trial site determines the outcome. We may encounter a generalization issue if the images from a particular trial site are not diverse enough. Using scenario 3, we simulate a scenario in which the training images contain meaningful digits indicating their true labels. We may bias our results in favor of images with overlaid labels in this manner. While this bias results in satisfactory results when tested on images with overlaid labels, it causes the deep network to ignore the remaining content of the images, i.e., become biased towards the overlaid labels. In overall, all shortcuts can be termed as a bias but not all biases can be assumed as shortcuts because of other words, among all types of biases, those that end up with in-distribution performance and low OOD performance are referred to as biases.

For all the experiments in this section, we used KimiaNet
^5
 with the same hyperparameters that we already used in former sections, with hospital 3 as the hold-out set.

### Scenario 3.

As experimental shortcuts, one can overlay the true labels on the training images. When the deep network is trained using scenario 3 it may use this opportunity during training, and most likely some decision rules are learned based on this shortcut opportunity. This type of shortcut are termed as 
*label bias in the literature*
^6
. The network will not take into account the intended and general features of the tissue context but rather the overlaid label digit. When an image without an overlaid label is tested after training, since the network has not learned meaningful decision rules, it will just output the overlaid category.

GradCAM
^7
 was used to provide some explainability such that providing heatmaps containing the salient areas relevant to the classification. According to Figs. 4 and 5, the GradCAM heatmaps show that scenario 3 caused the deep network to focus on the overlaid label and failed to pay attention to the tissue morphology.

(a) Hold-out set: Hospital 3

(b) Hold-out set: Hospital 5

**Figure 3.**
 The OOD versus in-distribution top-1 accuracy for the model trained using scenario 1 versus scenario 2 for the hospitals 3 and 5 with significant distribution shift relative to other hospitals.

<!-- PAGE 8 -->

**Figure 4.**
 KimiaNet trained using Scenario 3 when tested with a tumorous OOD patch with different class labels overlaid and their corresponding GradCAM heatmaps. (left) When false label (0: non-tumour) has been overlaid on the image. According to the class prediction of the network, the network has thoroughly paid attention to the overlaid digit and misclassified the image with its misleading shortcut. (right) When the true label (1: tumour) has been overlaid. The network, by focusing on the shortcut, classified the patch with a high degree of certainty.

**Figure 5.**
 KimiaNet trained using Scenario 3 when tested with a healthy (non-tumour) OOD patch with different class labels overlaid and their corresponding GradCAM heatmaps. (left) When true label (0: non-tumour) has been overlaid on the image. The network, by relying on the shortcut, classified the patch with confidence. (right) When the false label (1: tumour) has been overlaid. According to the class prediction of the network, the network has thoroughly paid attention to the overlaid digit and misclassified the image with its misleading shortcut.

In other words, the extreme case of a shortcut which can be the overlaid label of the image takes precedence over any other content of the image in these cases. The deep network in these cases, similar to a digit recognizer, can only make a decision based on the digit overlaid on the image. When the overlaid class label is missed or misleading the deep network cannot provide satisfactory results.

We also tested the KimiaNet trained using scenario 3 with images without class labels overlaid. The result was the deep network randomly generated class labels and similar to flipping a coin, the accuracy was > 50%.

**Scenario 1 and 2.**
 We trained KimiaNet by holding out the hospital 3 images and using both scenarios 1 and 2. An OOD tumorous patch from hospital 3 with pathologist pixel-level annotation for the tumorous area is shown in Fig. 6a–i. The model trained using scenario 2, correctly classified the image as tumorous and Fig. 6ii shows its salient tumorous area. While the model trained using scenario 1 misclassified the patch as healthy, the explainability heatmap for salient healthy areas is shown in Fig. 6iv. Although some tumorous areas are missed

<!-- PAGE 9 -->

**Figure 6.**
 The result of training using 
*scenario 1*
 and 
*scenario 2*
: (i) an OOD tumorous patch (from hospital 3) with different anatomical structures. (ii) Tumor cells, (iii) lymphocyte, (iv) Erythrocyte. (ii) Expert annotation for tumorous regions. (iii) GradCAM heatmap for the model trained using 
*scenario 2*
 which correctly classified the patch. (iv) GradCAM heatmap for the model trained using 
*scenario 3*
 which misclassified the patch as a healthy patch.

in the explainability heatmap (Fig. iii), the activated areas correlate well with the expert annotation whereas lymphocyte areas have not been activated. In contrast, the model trained using 
*scenario 1*
 misclassified the patch as healthy. Fig. 
*iv*
 shows its heatmap for salient healthy regions. Although this heatmap is highly correlated with the healthy area (according to Fig. 
*iii*
) but some tumorous regions erroneously have been activated as well. These regions may be attributed to shortcut opportunities that have been eliminated using the transformations of 
*scenario 2*
.

Figure 7
*i*
 shows a patch containing healthy tissue. The trained network using 
*scenario 1*
, erroneously classified this image as tumorous while the model trained by 
*scenario 2*
 correctly classified it as healthy. Figure 7
*ii*
 and 
*iii*
 show heatmaps for salient tumorous and healthy areas for 
*scenario 1*
 and 
*scenario 2*
, respectively. As it can be seen, the shortcut-trained model, or the model trained using 
*scenario 1*
, has correlated fibrous tissues with the tumorous region. While in the model trained using 
*scenario 2*
 salient healthy areas are mostly immune cells and adipocytes. Thus, it can be observed that training using 
*scenario 2*
 de-focused the deep-network on non-symmetric features (induced by spurious variations in stain colors or differences in morphology and tumor staging across hospitals/ritual sites) rather than what we intend to do, that is the semantics of tumorous or healthy patterns.

**Different pre-training: paying attention to different image aspects.**
 Pre-training on a related task vs. ImageNet. While pre-training on natural images, such as vanilla, SSL, and SWEL pre-trained weights, has been dominant for many computer vision tasks, there is evidence to suggest that domain-specific pre-trained weights may be more effective for certain tasks
^34,35^
. Accordingly, it is likely that a pre-trained model on a comprehensive histopathology task, e.g., cancer subtyping on TCGA, would perform better than ImageNet pre-training for a histopathology downstream task, i.e., tumorous vs. non-tumorous breast tissues on GAMELYON. This is perhaps because histopathology images have unique characteristics, such as variation in cell structures and tissue patterns, that may not be well represented in ImageNet, which is a dataset of natural images. Through pre-training on TCGA, the model would have learned more relevant features and patterns for better performance on histopathology downstream tasks.

Moreover, KinimNet has been trained on all the common cancer types from various hospitals such as Memorial Sloan Kettering Cancer Center (MSKCC) and National Cancer Institute Urologic Oncology Branch (NCI), as well as others. Through Empirical Risk Minimization (ERM) with the labels being cancer subtypes, the trained representations can be considered hospital-invariant to some extent. The variation among hospitals can indeed act as a form of data augmentation that can indirectly help improving the generalization of the KinimNet. As a result, pre-training on TCGA can end up overlooking some irrelevant hospital-specific aspects of the images

<!-- PAGE 10 -->

Figure 7. (i) an OOD healthy patch with different anatomical structures. (I) Immune cells, (II) Adipocyte, (III) Fibrous tissue, (IV) Erythrocyte. (ii) GradCAM heatmap for the model trained using scenario 1 which misclassified the patch as a healthy patch. (iii) GradCAM heatmap for the model trained using scenario 2 which correctly classified the patch.

**Figure 7.**
 (i) an OOD healthy patch with different anatomical structures. (I) Immune cells, (II) Adipocyte, (III) Fibrous tissue, (IV) Erythrocyte. (ii) GradCAM heatmap for the model trained using scenario 1 which misclassified the patch as a healthy patch. (iii) GradCAM heatmap for the model trained using scenario 2 which correctly classified the patch.

way better than pre-training on ImageNet. To support this hypothesis, heatmaps produced by XAI techniques were utilized in the following manner.

**Heatmaps of the initial layers.**
 The heatmaps generated by XAI techniques, especially GradCAM in this study, for the initial layers tend to highlight low-level features such as edges and corners in comparison to deeper layers which are more abstract and high-levels. These initial layers are usually left unchanged when fine-tuning a well-suited pre-trained model for the problem at hand, as they have already learned to detect “useful” features that are likely relevant to the new downstream task
^8^
. Accordingly, a crucial aspect of determining whether pre-trained weights are well-suited for downstream tasks is to assess whether fine-tuning induces significant changes to the initial layers. We investigated this issue by analyzing GradCAM heatmaps of the image shown in Fig. 8 for the first layer of each pre-trained model before and after fine-tuning (Fig. 9). Our results indicate that the initial layer responses of KimaNet remain consistent after fine-tuning on an OOD healthy patch belonging to hospital 3, suggesting that the features captured by this pre-trained model are well-suited for the downstream task. However, for the other pre-trained models, changes in initial layer responses were observed, with the random weight model displaying the most dramatic changes. These findings suggest that careful consideration should be given to the choice of pre-trained weights for downstream tasks.

**Conclusions**

Although a fixed-policy diversification of images, similar to scenario 2 in this study, may lead to OOD generalization improvement, that is not necessarily the case. We showed that in some cases the data diversification, counter-intuitively, leads to poor OOD and in-distribution performance due to complicating the training of the deep networks. Hence, it is not always possible to a priori assume a policy that fits all scenarios unless the target test data and its distribution are available/known. A good example is the learnable augmentation policies
^9^
 using Cycle-Generative Adversarial Networks (Cycle-GANs)
^10^
 which is utilized for adapting the target data to source data for improving the OOD generalization. However, in this study, we assumed that there is no access to the target data during the training.

<!-- PAGE 11 -->

[www.nature.com/scientificreports/](#)

**Figure 8.**
 Sample non-tumorous patch at 20x magnification from Hospital 3.

**Figure 9.**
 Activation maps of first layer weights: pre-training weights (Gray-highlighted) and fine-tuning (Yellow-highlighted) using the same downstream task for each pre-training scenario.

Although there are some works claiming that pre-training is not sufficiently effective, this paper showed that the use of pre-training in computer vision should not be dismissed. We have demonstrated that the newly released pre-trained vision models (SWVL and SSL) do improve performance in many scenarios as other works have already shown that
^40^
. Additionally, we showed that KimiaNet which is a histopathology-tailored pre-trained model can outperform pre-trained models tailored toward natural images by far when the distribution shift is significant and the domain of study is histopathology.

We utilized XAI techniques to provide explanations and interpretations for certain conclusions. We presented empirical evidence that data diversification could enhance OOD performance by eliminating shortcuts, and investigated how the suitability of various pre-trained models affects the activation maps of the initial layers in deep networks.

Although some of these conclusions may be obvious, this paper presented a thorough examination of various histopathology trial site repositories, pre-trained models, and image transformations. Moreover, the paper could

**Scientific Reports**
 | (2023) 13:6065 | 
[https://doi.org/10.1038/s41598-023-33348-z](https://doi.org/10.1038/s41598-023-33348-z)
 | 
[nature portfolio](#)

<!-- PAGE 12 -->

serve as a reference for practitioners who are not acquainted with the prevailing ideas in the field. It seems it is a common practice among the computational pathology community to utilize ImageNet-pre-trained models for their histopathology downstream tasks.

### Limitations.

Although our study extensively examined the performance of various pre-trained models on COVID test data in histopathology repositories, it is important to acknowledge limitations. Firstly, the study only applied ERM on different pre-trained models and did not explore other approaches such as domain adaptation and domain generalization that may offer better generalization on OOD data. Secondly, while XAI techniques were employed for interpreting the results, the explanations generated were not thoroughly analyzed. A more comprehensive investigation of these explanations could provide deeper insights into the causes of the distribution shift in histopathology data.

Furthermore, our study only considered a limited set of pre-trained models, including vanilla ImageNet, Seli, Seli-S, and KimiaNet pre-trained models. There are many other pre-trained models designed for different tasks. Therefore, the results may not be generalized to all pre-trained models.

### Data availability

The dataset CAMeLYON17 analyzed during the current study is available in the Grand Challenge repository: 
[https://camelyon17.grand-challenge.org/](https://camelyon17.grand-challenge.org/)
.

Received: 29 November 2022; Accepted: 12 April 2023
Published online: 13 April 2023

### References

1. Graham, R. et al. Shortest learning in deep neural networks.*Nat. Mach. Intell.*2, 667–673 (2020).
2. Jun, X. et al. Benefiting the short-cut learning of background for few-shot learning.*Adv. Neural Proc. Syst.*34, 1497–1508 (2021).
3. Esteban, J. et al. Can contrastive learning avoid shortcut solutions?*Adv. Neural Proc. Syst.*34, 4974–4986 (2021).
4. Esteban, J., Parikh, N., Cappos, R. & Tytgat, T. A deeper look at dataset bias. In*Domain Adaptation in Computer Vision Applications*57–59 (Springer, 2017).
5. Stoyanov, D., Iannitti, I., Wang, Y. & Radev, D. Implicit data crimes: Machine learning bias arising from misuse of public data.*Proc. Natl. Acad. Sci. U.S.A.*121(7131) (2022).
6. Dabholkarappa, T. et al. Biased data biased AI: Deep networks predict the acquisition site of tga images (2021).
7. Stucke, E., Ellerath, E., Unger, J. & Lundstrom, C. A closer look at domain shift for deep learning in histopathology: xAI preprint arXiv:2001.13755 (2020).
8. Lin, Y., Zheng, L., Guan, Y., Yu, J. & Yang, Y. Taking a closer look at domain shift: Category-level adversarial feature consistency domain adaptation. In*Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*2507–2514 (2021).
9. Stucke, E., Ellerath, E., Unger, J. & Lundstrom, C. Measuring domain shift for deep learning in histopathology.*IEEE J. Biomed. Health Inform.*25, 325–336 (2022).
10. Mikolov, N., Sutskever, I., Chen, X., Corrado, G. & Salakhutdinov, R. A. survey on bias and fairness in machine learning.*ACM Comput. Surv. (CSUR)*54, 1–35 (2021).
11. Rey, S., Van Horn, G. & Perrone, P. Recognition in tira incognita. In*Proceedings of the European Conference on Computer Vision (ECCV) 646–674*(2018).
12. Kone, W. M. & Loop, M. A review of domain adaptation without target labels.*IEEE Trans. Pattern Anal. Mach. Intell.*43, 768–785 (2020).
13. Hagge, M. et al. Avoiding challenges in deep learning-based analyses of histopathological images using explanation methods.*Sci. Rep.*10, 1–12 (2020).
14. Li, D., Yang, Y., Song, Y. & Hospedales, T. Learning to generalize: Meta-learning for domain generalization. In*Proceedings of the AAAI Conference on Artificial Intelligence*2316–2323 (2018).
15. Dwu, D., Coello de Castro, D., Kaminski, K. & Glocker, B. Domain generalization via modality-agnostic learning of semantic features.*Adv. Neural Proc. Syst.*34, 2021.
16. Sharma, M., Bahrami, S., Baltrusaitis, H., H. H., H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H. H

<!-- PAGE 13 -->

30. Lang, I., Buehler, E., & Darrell, T. Fully convolutional networks for semantic segmentation. In 
*Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*
 3431–3439 (2015).

31. Chen, G., Papandreou, G., Kokkinos, I., Murphy, K., & Yuille, A. L. DeepLab: Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs. 
*IEEE Trans. Pattern Anal. Mach. Intell.*
 40, 834–848 (2017).

32. Zeng, Z. et al. Object detection with deep feature supervision. 
*IEEE Trans. Pattern Anal. Mach. Intell.*
 42, 399–412 (2019).

33. Lin, T.-Y. et al. Microsoft coco: Common objects in context. In 
*European Conference on Computer Vision*
 740–755 (Springer, 2014).

34. Ghiasi, G. et al. S. Y. Li, & Q. V. Le. DropBlock: A regularization method for convolutional networks. 
*arXiv: Neural Inf. Process. Syst.*
 31, 100, 
[https://doi.org/10.48550/arXiv.1812.01187](https://doi.org/10.48550/arXiv.1812.01187)
 (2018).

35. Hendrycks, D. et al. The many faces of robustness: A critical analysis of out-of-distribution generalization. In 
*Proceedings of the IEEE/CVF International Conference on Computer Vision*
 8380–8389 (2021).

36. Monroe, B. et al. VGG16One: The state-of-the-art multi-class research. 
*Commun. ACM*
 64, 76–73 (2016).

37. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

38. Levy, H., Padir, A., & Anand, D. Kumar, S. & Neubeck, K. Q. Density connected correlation networks. In 
*Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*
 4706–4708 (2017).

39. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

40. Levy, H., Padir, A., & Anand, D. Kumar, S. & Neubeck, K. Q. Density connected correlation networks. In 
*Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*
 4706–4708 (2017).

41. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

42. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

43. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

44. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

45. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

46. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

47. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

48. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

49. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

50. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

51. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

52. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

53. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

54. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

55. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

56. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

57. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

58. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

59. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

60. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

61. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

62. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

63. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

64. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

65. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

66. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

67. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

68. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

69. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

70. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

71. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

72. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

73. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

74. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

75. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

76. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

77. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

78. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

79. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

80. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

81. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

82. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

83. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

84. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

85. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

86. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

87. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

88. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

89. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

90. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

91. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

92. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

93. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

94. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

95. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

96. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

97. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

98. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

99. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

100. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

101. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

102. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

103. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

104. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

105. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

106. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

107. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

108. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64, 76–73 (2016).

109. Huang, G. et al. Very deep learning for natural language processing. 
*Commun. ACM*
 64,

<!-- PAGE 14 -->

www.nature.com/scientificreports/

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit 
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)
.

© The Author(s) 2023

Scientific Reports | (2023)13:6065 | 
[https://doi.org/10.1038/s41598-023-33348-z](https://doi.org/10.1038/s41598-023-33348-z)
 | nature portfolio