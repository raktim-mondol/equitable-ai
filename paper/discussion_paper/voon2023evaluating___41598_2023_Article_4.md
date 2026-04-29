<!-- Page 1 -->

www.nature.com/scientificreports

scientific reports

# OPEN Evaluating the effectiveness of stain normalization techniques in automated grading of invasive ductal carcinoma histopathological images

Wingates Voon1, Yan Chai Hum1,2,3, Yee Kai Tee1, Wun-She Yap2, Humaira Nisar2, Hamam Mokayed2, Neha Gupta3 & Khin Wee Lai4

Debates persist regarding the impact of Stain Normalization (SN) on recent breast cancer histopathological studies. While some studies propose no influence on classification outcomes, others argue for improvement. This study aims to assess the efficacy of SN in breast cancer histopathological classification, specifically focusing on Invasive Ductal Carcinoma (IDC) grading using Convolutional Neural Networks (CNNs). The null hypothesis asserts that SN has no effect on the accuracy of CNN-based IDC grading, while the alternative hypothesis suggests the contrary. We evaluated six SN techniques, with five templates selected as target images for the conventional SN techniques. We also utilized seven ImageNet pre-trained CNNs for IDC grading. The performance of models trained with and without SN was compared to discern the influence of SN on classification outcomes. The analysis unveiled a p-value of 0.11, indicating no statistically significant difference in Balanced Accuracy Scores between models trained with StainGAN-normalized images, achieving a score of 0.9196 (the best-performing SN technique), and models trained with non-normalized images, which scored 0.9308. As a result, we did not reject the null hypothesis, indicating that we found no evidence to support a significant discrepancy in effectiveness between stain-normalized and non-normalized datasets for IDC grading tasks. This study demonstrates that SN has a limited impact on IDC grading, challenging the assumption of performance enhancement through SN.

Invasive ductal carcinoma (IDC) is widely recognized as the most common form of breast cancer, accounting for over 80% of breast cancer cases1. IDC grading is a crucial factor in determining the prognosis of IDC and plays a critical role in evaluating its clinical outcome. Henson et al.2 found that the accuracy of IDC diagnosis improved when both the IDC grade and lymph node condition were considered. Similarly, the research conducted by Frkovic-Grazio and Bracko3 demonstrated that IDC grading effectively predicts the behavior of the tumor, particularly for early-stage, small tumors. Schwartz et al.4 also uncovered that when undergoing mastectomy, patients with high-grade IDC faced higher fatality rates and more frequent axillary lymph node involvement compared to those with lower-grade IDC. These findings highlight the significance of IDC grading in the prognostic evaluation of IDC.

The standard method of grading IDC is the Nottingham Grading Scheme (NGS), which is a semi-quantitative system based on three morphological features of IDC: mitotic count, nuclear pleomorphism, and degree of tubule formation5. These three criteria result in a total score that can be divided into grades 1 to 3, which indicate the

1Department of Mechatronics and Biomedical Engineering, Faculty of Engineering and Science, Lee Kong Chian, Universiti Tunku Abdul Rahman, Kampar, Malaysia. 2Department of Electrical and Electronic Engineering, Faculty of Engineering and Science, Lee Kong Chian, Universiti Tunku Abdul Rahman, Kampar, Malaysia. 3Department of Electronic Engineering, Faculty of Engineering and Green Technology, Universiti Tunku Abdul Rahman, 31900 Kampar, Malaysia. 4Department of Computer Science, Electrical and Space Engineering, Lulea University of Technology, Lulea, Sweden. 5School of Electronics Engineering, Vellore Institute of Technology, Amaravati, AP, India. 6Department of Biomedical Engineering, Universiti Malaysia, 30603 Kuala Lumpur, Malaysia. "email: humy@utar.edu.my"

Scientific Reports | (2023) 13:20518

| https://doi.org/10.1038/s41598-023-46619-6

nature portfolio

1

---

<!-- Page 2 -->

www.nature.com/scientificreports/

aggressiveness of the tumor. Lower-grade IDC is less aggressive, while higher-grade IDC is more aggressive10. Although manual IDC grading is still the standard, it can be time-consuming and prone to high intra- and inter-observer variations, with agreement among pathologists reaching only 75.3% at best11. To address these limitations, automated IDC grading systems, a type of computer aided diagnostic (CAD) technique, have been developed12.

The development of automated IDC grading systems has significantly advanced from traditional handcrafted feature extraction methods13–15 to the application of deep learning techniques15–21. This evolution extends beyond IDC grading, as deep learning also finds widespread utilization in various histopathological applications21,22. The process of generating digital IDC histopathological images involves several steps including the collection of IDC tissues, formalin fixation, section embedding, and digital scanning23–25. The slides are then digitized using Whole Slide Imaging technology26. H&E staining, the standard protocol in histopathological studies, highlights cell nuclei in blue and different components such as cytoplasm and connective tissue with various shades of pink27.

There is controversy surrounding the impact of Stain Normalization (SN) in recent breast cancer histopathological studies. Some studies have indicated that SN has no effect on classification results28–30, while others have claimed that SN improves classification outcomes31–33. The purpose of SN is to address color inconsistency in digital H&E stained images caused by external factors such as the temperature of staining solutions, fixation characteristics, imaging device characteristics34,35, and variations in light sources, detectors, or optics during slide digitization36. SN normalizes the color values of source images by matching the overall color distribution of target images37. However, the effectiveness of SN in improving classification results is uncertain due to the conflicting results in the literature.

In light of this, our aim is to investigate the effectiveness of SN in the breast cancer histopathological classification task using convolutional neural networks (CNNs), with a specific focus on classifying the Four Breast Cancer Grades (FBCG) dataset into four IDC grades. We attempted to answer the question: Is SN effective in the IDC grading task? by conducting a statistical significance analysis using Student's t-test with the significance level, \alpha=0.05. Below are our statements of null and alternative hypotheses:

1. 1. Null hypothesisH_0: A CNN trained with a stain-normalized dataset has no effect on the IDC grading accuracy.
2. 2. Alternative hypothesisH_1: A CNN trained with a stain-normalized dataset has an effect on the IDC grading accuracy.

In this paper, we selected six types of conventional and deep learning-based SN techniques to study their effectiveness with the FBCG dataset using CNNs, with a specific focus on conventional methods, including Reinhard38, Macenko39, Structure-preserving Color Normalization (SPCN)40 and Adaptive Color Deconvolution (ACD)41 techniques, require a template as the stain target reference to stain-normalize the images. Hence, we selected five templates from the FBCG dataset (a dataset derived from the FBCG dataset) as templates for the conventional methods. For the deep learning-based SN methods, we utilized the Camelyon1642 pre-trained StainGAN and StainNet43 to stain-normalize the images in the FBCG dataset. After normalizing the images, we implemented seven pre-trained CNNs: (1) EfficientNet-B044, (2) EfficientNet-V2-B045, (3) EfficientNet-V2-R0-21K46, (4) ResNeXt-V1-5047, (5) ResNeXt-V2-5048, (6) MobileNet-V149, and (7) MobileNet-V250 as feature extractors in our IDC grading models to conduct the classification task. Our source code can be accessed publicly from: https://github.com/wingates/SN_IDC_Grading.

In this study, we have made the following contributions and reached the following conclusions:

1. 1) We conducted a comprehensive evaluation of six conventional and deep learning-based SN techniques on the task of IDC grading using the FBCG dataset.
2. 2) We conducted a systematic review of ten recent studies that investigated the efficacy of SN in breast cancer histopathological classification. The findings are presented in the section on related works.
3. 3) Our results suggest that SN is deemed necessary in the image pre-processing pipeline, StainGAN, StainNet, and ACD techniques are preferable to Reinhard, Macenko, and SPCN techniques.
4. 4) Our statistical analysis revealed ap-value of 0.11 when comparing the mean balanced accuracy scores between models trained with the StainGAN-normalized FBCG dataset (the best performing SN technique), which achieved a score of 91.96, and those trained with the non-normalized dataset, which scored 91.938. This implies that we found no evidence of a significant difference in effectiveness between Stain-normalized and non-normalized datasets for grading tasks.
5. 5) Our findings challenge the assumption that stain normalization significantly improves histopathological classification tasks, as we found no evidence of a significant discrepancy in effectiveness between stain-normalized and non-normalized datasets for IDC grading tasks.

Our study provides insights into the effectiveness of SN techniques in breast cancer histopathological studies, with a particular focus on the IDC grading task. While there has been some debate over the impact of SN on classification outcomes, our research has shown that models trained with the non-normalized dataset can be just as effective as those trained with StainGAN-normalized images. This finding is valuable not only to the field and can help guide future research on SN techniques. We are optimistic that our study will encourage researchers to approach the topic with a critical lens and produce even more promising results in the future.

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-66613-6](https://doi.org/10.1038/s41598-023-66613-6)

nature portfolio

2

---

<!-- Page 3 -->

www.nature.com/scientificreports/

## Related works

In this section, we examine the development of automated IDC grading systems and various SN methods. The SN techniques are divided into two categories: (1) conventional approaches and (2) deep learning-based approaches. Next, we present studies that investigated the effect of SN in various breast cancer histopathological image classification tasks.

### Automated IDC grading systems

The development of automated IDC grading systems has progressed from manual feature extraction techniques to deep learning-based approaches. For instance, Doyle et al.141 proposed a method for extracting textural and architectural features by using spectral clustering to reduce the dimensionality of the extracted features, which were then used to train a deep learning model. They used a dataset of 1000 breast cancer images and created a multi-field-of-view (multi-FOV) classifier to identify the most salient image features from multiple FOV of varying sizes for the purpose of IDC grading. Dimitropoulos et al.142 transformed images into vectors of locally aggregated descriptors (VLAD) representations based on the Grassmann manifold. They then calculated the VLAD encoding of each image on the manifold to determine the IDC grade. However, these methods are heavily reliant on features and are computationally intensive, with a lack of heuristics for feature extraction143. As a result, more recent studies have introduced deep learning methods, specifically Convolutional Neural Networks (CNNs)144,145. For example, Senousy et al.146 developed an entropy-based elastic ensemble of CNNs (3E-Net) for IDC grading, and Yan et al.147 created a nuclei-guided network (NGNet) with a nuclei-guided attention module for IDC grading. The attention mechanism of transfer learning, Zero-grabbing, and the model-based model-free extractor in the BCNet to grade IDC. Similarly, Voon et al.148 evaluated the performance of seven pre-trained CNN models in the IDC grading task. In this study, we adopted the model implementation of Voon et al.148 which utilized transfer learning. This approach was chosen due to the improved performance of CNNs when trained on a limited number of training images.

### Stain normalization methods

#### Conventional stain normalization methods

Conventional approaches to Stain Normalization (SN) in histopathological images typically involve the analysis, transformation, and alignment of the color components of images45. The Reinhard method46 normalizes the images by adjusting the statistical color distribution of the source image to match that of a template image while preserving the background color and color intensities. The Macenko technique47 employs Single Value Decomposition (SVD) to form a plane that projects information, determining the corresponding angles and finally estimating the color matrix. The Khan method48 identifies the stain color of the source image using the Stain Color Descriptor (SCD), then uses a Relevance Vector Machine (RVM) to determine the position of each stain and transfers the color from the template to the source image using a non-linear spline-based color normalization technique. The Structure-Preserving Color Normalization (SPCN)49 decomposes the source images into sparse stain density maps and aligns the stain of the template image to change the color while preserving the structures. The Adaptive Color Deconvolution (ACD)50 normalizes the stains by integrating optimization to approximate the parameters of stain separation and color normalization. This technique, based on Color Deconvolution (CD)51, estimates the estimation of stain parameters. It uses the method52,53 to create a reference image to approximate the stain parameters, presenting a challenge to encompass all staining patterns or represent all input images. As a result, the use of suboptimal reference images may lead to incorrect estimation of stain parameters and result in inaccurate outcomes50.

#### Deep learning-based stain normalization methods

Recently, a significant shift has been observed towards the adoption of deep learning-based techniques for stain normalization. A deep learning approach offers a data-driven approach to stain normalization that relies on training images46,47,49,54. Zanjani et al.46 proposed the use of generative adversarial networks (GANs) to learn the relationship between image content structures and their respective color attributes, thereby facilitating color alignment without relying on color and intensity properties. Shahin et al.54 extended the approach by developing StainGAN. CycleGAN-based technique46 that enables the transfer of stain style from one domain to another without the need for paired data. Similarly, Kang et al.47 introduced StainNet, a method that leverages the output of StainGAN to better understand the pixel-wise color matching relationship within a given dataset. In our current study, we sought to investigate the effectiveness of SN in the context of IDC grading. To this end, we considered a wide range of techniques, including Reinhard, Macenko, Structure-Preserving Color Normalization (SPCN), Adaptive Color Deconvolution (ACD), StainGAN, and StainNet.

### Study of stain normalization in breast cancer histopathological images classification

This section presents an overview of the prior studies that have compared the performance of models trained with stain-normalized and non-normalized inputs in the context of breast cancer histopathological image classification. Despite the numerous studies in this field, there is still considerable controversy regarding the efficacy of SN on the performance of these models35–39.

On one hand, several studies35–39 have reported that SN has no significant impact on the performance of the models. For example, Benjeddad et al.35 evaluated the classification performance of texture-based features and contemporary classifiers using Reinhard-normalized BreakHis40 dataset and found that SN did not lead to improvement in the results. Similarly, Tellez et al.36 compared the performance of CNNs trained on Camelyon1737 dataset using Macenko47 and Benjeddad35 SN techniques, and revealed that SN did not enhance the performance, with the CNN trained on the non-normalized dataset even outperforming those trained on the stain-normalized

Scientific Reports | (2023) 13:20358 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

5

---

<!-- Page 4 -->

www.nature.com/scientificreports/

datasets. These findings were supported by Kumar et al.28, who found that a pre-trained VGG16 model trained on the non-normalized BreakKHS dataset outperformed the identical model trained on the Macenko-normalized dataset. Hameed et al.29 also found that the performance of deep learning-based ensemble models declined when using stain-normalized datasets, while Hameed et al.30 failed to find any performance improvement when the pre-trained Xception model was trained on the Colsantisat dataset30 with Reinhard, Macenko, CD, and SPEN SN techniques.

On the other hand, several studies31–35 have suggested that SN does indeed improve the performance of the models. For example, Nawaz et al.31 fine-tuned the AlexNet model on the ICIAR2018 dataset36 and found that the AlexNet trained on the Macenko-normalized dataset outperformed the model trained on the non-normalized dataset. They also compared the performance of the models trained with Macenko-normalized and non-normalized BreakKHS datasets and found that SN improved the model performance. Munien and Viriri32 implemented seven pre-trained EfficientNets to classify the original, Reinhard-normalized, and Macenko-normalized ICIAR2018 datasets. The results showed that models trained with stain-normalized datasets outperformed models trained with the non-normalized dataset. Salvi et al.33 attempted to classify the BACH challenge46 dataset with Stain Color Adaptive Normalization (SCAN) technique46. The authors found that the normalized dataset obtained better results than the non-normalized dataset. Similarly, Alkassar et al.34 utilized an ensemble of models trained with Khan-normalized and non-normalized BreakKHS datasets. The results showed that the models trained with the Khan-normalized dataset outperformed those trained with the non-normalized dataset. Therefore, we can conclude that these studies highlighted the benefits of SN in the classification task.

These inconsistent results created a knowledge gap in the field of histopathology image classification. To confusion among researchers about the effectiveness of SN in future studies. In light of this, we set out to answer the question: "Is SN effective in the IDC grading task?" by investigating the effectiveness of six conventional and deep learning-based SN techniques on the IDC grading task using the FBGC dataset and CNNs.

## Methodology

### Overview

In this section, we provide an outline of the six SN techniques used in the IDC grading task. We also elucidate the implementation details, which include aspects such as the FBGC dataset, image pre-processing procedures, CNN model implementations, and the evaluation metric. All experiments were conducted using Python and TensorFlow Keras. We used the Collaboratory platform47 to conduct our experiments. The experiments included a 2.30 GHz Intel Xeon CPU, up to 32 GB RAM, and an NVIDIA P100 or T4 GPU. We ensure that all procedures adhered to relevant guidelines and regulations. Figure 1 illustrates the general methodology of the study.

### Stain normalization

SN aims to normalize the color values of the source images by aligning the overall color distribution with that of target images. Our study explored six types of SN techniques, specifically Reinhard48, Macenko49, SPEN50, ACN51, StainGAN52 and StainNet53 (Note that the employed StainGAN and StainNet were pre-trained on the Camelyon16 dataset54).

### Template selection

The selection of an appropriate template is crucial for conventional SN techniques, which rely on a single template to perform color conversion between source and target images. If the template is not chosen wisely, the performance of SN techniques may be compromised55. Therefore, we selected five templates from T \in \{T1, T2, T3, T4, T5\} (see Fig. 2) from the PatchCamelyon (PCam) dataset46, our target dataset, to investigate the impact of each template on the SN techniques. It is imperative to note that the selection of these templates was not selected based on our initial decisions. Instead, we used an automated and algorithmic approach that involved generating an average image from the target dataset and using similarity functions to compare this average image with image samples within the target dataset. This approach helped us identify a template that most accurately reflects the overall color staining distribution of the dataset.

Average image generation. Before selecting any template, we generated an image I_{avg} that represents the average pixel values of the target dataset. In this case, we selected the PCam train set as the target dataset D_t to ensure a fair comparison between the Khan and StainNet models. The Khan model is a biological model that comprises patch-wise images with dimensions of 96 by 96 pixels. These images are extracted from histological scans of lymph node sections from the Camelyon16 Challenge, which focuses on breast cancer metastasis. To generate I_{avg}, all 262,144 images from the PCam train set were converted into floating-point arrays, followed by summing up the arrays to yield the average pixel values.

Templates 1 (T1) and Template 2 (T2) were selected using cosine similarity SIM_C. This method computes the dot product of two vectors and divides it by the product of their magnitude to determine their similarity. Specifically, we computed the SIM_C between I_{avg} and image X \in D_t to locate X that most resembles I_{avg}, resulting in T1. Likewise, selecting T2 adopted a similar approach. However, the most dominant color, C_{dom}, of I_{avg} and image X were obtained, followed by forming an image I_{dom,dom} and I_{dom,dom} based on each dominant color, respectively. Subsequently, we computed the SIM_C between I_{avg,dom} and I_{dom,dom}, resulting in T2. Equation (1) formally describes the SIM_C:

Scientific Reports | (2023) 13:20518 |

https://doi.org/10.1038/s41598-023-46619-6

nature portfolio

6

---

<!-- Page 5 -->

www.nature.com/scientificreports/

Figure 1 illustrates the overall methodology of the study. The process is divided into several steps:

- Step 1:Form FBGC Dataset. This involves combining the Benj class dataset and the BCKH dataset to form the FBGC dataset.
- Step 2:Model training with SFFCV to evaluate validation results. This step involves training the model using the FBGC dataset and evaluating the validation results.
- Step 3:Hyperparameters of the model are optimized until the model is stable across each fold. This is done using SFFCV.
- Step 4:Repeat Step 3 if the model is not optimized, else go to Step 5.
- Step 5:Once satisfactory model performance is achieved, the FBGC datasets undergo stain normalization using various techniques to formD_{N \times T}.
- Step 6:Form stain-normalized FBGC Datasets,D_{N \times T}. This step involves applying various stain normalization techniques (Retained Stain, MacroStain, SFCN, ACD, StainGAN, StainNet) to the FBGC datasets.
- Step 7:Finally, eachD_{N \times T}is fed forward into the model to retrain, followed by (8) obtaining the final test results.

The diagram also shows the internal structure of the SFFCV model, which is a three-stage model with hyperparameters based on validation results. The model implementation is shown as a 3D block diagram with layers I_0, I_1, I_2, I_3, I_4, I_5, I_6, I_7, I_8, I_9, I_{10}, I_{11}, I_{12}, I_{13}, I_{14}, I_{15}, I_{16}, I_{17}, I_{18}, I_{19}, I_{20}, I_{21}, I_{22}, I_{23}, I_{24}, I_{25}, I_{26}, I_{27}, I_{28}, I_{29}, I_{30}, I_{31}, I_{32}, I_{33}, I_{34}, I_{35}, I_{36}, I_{37}, I_{38}, I_{39}, I_{40}, I_{41}, I_{42}, I_{43}, I_{44}, I_{45}, I_{46}, I_{47}, I_{48}, I_{49}, I_{50}, I_{51}, I_{52}, I_{53}, I_{54}, I_{55}, I_{56}, I_{57}, I_{58}, I_{59}, I_{60}, I_{61}, I_{62}, I_{63}, I_{64}, I_{65}, I_{66}, I_{67}, I_{68}, I_{69}, I_{70}, I_{71}, I_{72}, I_{73}, I_{74}, I_{75}, I_{76}, I_{77}, I_{78}, I_{79}, I_{80}, I_{81}, I_{82}, I_{83}, I_{84}, I_{85}, I_{86}, I_{87}, I_{88}, I_{89}, I_{90}, I_{91}, I_{92}, I_{93}, I_{94}, I_{95}, I_{96}, I_{97}, I_{98}, I_{99}.

Figure 1. The overall methodology of the study. (1) The FBGC dataset is assembled by combining images from the 400X Benign class of the BreakHis dataset and images from the BCKH dataset. (2) To evaluate model stability, the implemented model is trained with D_{N \times T} using the Stratified Five-fold Cross-validation (SFFCV). (3) The hyperparameters of the model are optimized until the model is stable across each fold. (4) The SFFCV process is repeated until the model is optimized. (5) Once satisfactory model performance is achieved, (6) the FBGC datasets undergo stain normalization using various techniques to form D_{N \times T}. (7) Lastly, each D_{N \times T} is fed forward into the model to retrain, followed by (8) obtaining the final test results.

Figure 2 displays five templates selected from the PCam train set: (a) T1, (b) T2, (c) T3, (d) T4, and (e) T5. These templates are used for stain normalization in the study.

Figure 2. Five templates selected from PCam train set: (a) T1, (b) T2, (c) T3, (d) T4 and (e) T5.

SIM_C(A, B) = \frac{\sum_{i=1}^n A_i B_i}{\sqrt{\sum_{i=1}^n A_i^2} \sqrt{\sum_{i=1}^n B_i^2}} \quad (1)

where A and B denote vectors with n-th number of pixels flatten from I_{img} and image X \in D_i \in I_{img,diam} and I_{D_{train}}. Equation (2) formally describes the C_{sim}.

Scientific Reports | (2023) 13:5018 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

5

---

<!-- Page 6 -->

www.nature.com/scientificreports/

**Input:**
 
I_s, T \in \{T1, T2, T3, T4, T5\}

**Output:**
 
I_{out}

**Initiate**
 
i = 0
, number of channel, 
c = 3

1 Read 
I_s
 and 
T

2 Convert 
I_s
 and 
T
 from 
*RGB*
 to 
*lab*
 colour space
3 
**while**
 
i < c
 
**do**

4   
I_{out} \leftarrow
 transform 
I_s
 with Equations (5), (6) and (7)
5   
i \leftarrow i + 1

6 
**end while**

7 convert 
*lab*
 back to 
*RGB*
 color space

**Algorithm 1.**
 Reinhard Technique

C_{dom} = \arg \max_{c \in C(p)} N(c) \quad (2)

where P denotes the set of all pixels in an image, C(p) denotes the function that returns the color of pixel p, and N(c) denotes the function that returns the number of pixels of color c in the image.

Templates 3, 4 and 5. For Templates 3, 4, 5, we used different selection methods. Template 3 (T3) was selected using the Mean Square Error (MSE), while Template 4 (T4) was chosen based on the Structural Similarity Index (SSIM). Similar to T1 and T2, we computed the MSE and argmax between I_{out} and image X \in D_i to find the most similar X, resulting in T3 and T4. For Template 5 (T5), we identified the most dominant color in I_{out} and image X \in D_i. We then formed images I_{log,dom} and I_{D_{dom}} based on each dominant color. Then, we computed the MSE or SSIM between I_{log,dom} and I_{D_{dom}}, resulting in T5 (note that the results of MSE and SSIM are identical). Equations (3) and (4) describe MSE and SSIM respectively as followed:

MSE(I_A, I_B) = \frac{1}{n} \sum_{i=1}^n (I_{A,i} - I_{B,i})^2 \quad (3)

SSIM(I_A, I_B) = \frac{(2\mu_{I_A}I_{I_B} + C_1)(2\sigma_{I_A}I_{I_B} + C_2)}{(\mu_{I_A}^2 + \mu_{I_B}^2 + C_1)(\sigma_{I_A}^2 + \sigma_{I_B}^2 + C_2)} \quad (4)

where I_A and I_B denote input and output image matrices with n-th number of pixels respectively, \mu_{I_A} and \mu_{I_B} denote the luminance of I_A and I_B respectively, \sigma_{I_A} and \sigma_{I_B} denote the contrast of I_A and I_B respectively, C_1 and C_2 denote constants to ensure stability where C_1 and C_2 > 0.

#### Reinhard stain normalization technique

The Reinhard SN technique normalizes the source image I_s by aligning the mean \mu and standard deviation \sigma with a template T. Algorithm 1 outlines the workflow of the Reinhard algorithm. The Reinhard method transforms the RGB images to lab colour space where I represents the achromatic channel, a denotes the chromatic blue-yellow channel and b signifies the chromatic green-red channel. Subsequently, the following Eqs. (5), (6) and (7) are applied to perform the Reinhard transformation, then convert the output image I_{out} back to RGB color space8,9,10.

I_2 = \mu(I_1) + (1 - \mu(I_1)) \odot (\sigma(I_1) \otimes \sigma(I_1)) \quad (5)

\alpha_2 = \mu(\alpha_1) + (\alpha - \mu(\alpha)) \odot (\sigma(\alpha_1) \otimes \sigma(\alpha)) \quad (6)

\beta_2 = \mu(\beta_1) + (\beta - \mu(\beta)) \odot (\sigma(\beta_1) \otimes \sigma(\beta)) \quad (7)

where I_1 and I_2 depict the I_s, I_{out} and I_{out} in the I space respectively, \alpha_1 and \alpha_2 depict the I_s, T and I_{out} in the \alpha space respectively, \beta_1 and \beta_2 depict the I_s, T and I_{out} in the \beta space respectively; \odot denotes element-wise multiplication and \otimes denotes element-wise division.

#### Macenko stain normalization technique

The Macenko technique separates stains by identifying the fringe of pixel distribution in the Optical Density space (OD). Algorithm 2 provides a detailed description of the Macenko algorithm. Similar to Reinhard, Macenko converts the RGB image to lab colour space, followed by transforming the colors into OD values with Eq. (8):

OD = -\log_{10}(I_1) \quad (8)

The color transformation to OD values provides a space where a linear stain fusion yields a linear fusion of OD values. Subsequently, the transparent pixels are removed if the OD value is below a specific threshold. The OD value is split into two matrices, given by Eqs. (9) and (10).

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

6

---

<!-- Page 7 -->

www.nature.com/scientificreports/

**Input:**
 
I_s, T \in \{T1, T2, T3, T4, T5\}

**Output:**
 
I_{out}

**Initiate**
 tolerance for the pseudo-minimum 
\alpha^{th}
 and pseudo-maximum 
(100 - \alpha)^{th}

percentile, where 
\alpha = 1
, 
OD
 threshold value for transparent pixels 
\beta = 0.15
,
transmitted light intensity 
I_o = 240

1 Read 
I_s
 and 
T

2 Convert 
I_s
 and 
T
 from 
*RGB*
 to 
*OD*
 colour space with Equation (8)
3 
**if**
 
OD < \beta
 
**then**

4     remove transparent pixels
5 
**else**

6     Compute 
*SV*
D on the 
*OD*

7     Devise plane from the 
*SV*
D directions
8     Project data onto the plane, normalizing to unit length
9     Compute each angle point corresponding to the first 
*SV*
D direction
10    Locate robust extremes and transform extreme values back to 
*OD*
 space
11    Determine normalization stain concentration
12    
I_{out} \leftarrow
 recreate the normalized image using reference mixing matrix
13 
**end if**

**Algorithm 2.**
 Macenko Technique

OD = V \star S \quad (9)

S = Vr \star OD \quad (10)

where S represents each stain saturation and V denotes stain vector matrix. Equations (8) and (9) locate the stain vector of each image based on the color (if OD = 0, then the corresponding pixel = white; the stain is absent). Next, we compute the singular value decomposition (SVD) on the OD value, followed by locating the stain vector terminal points using the Geodesic path32. We can then assess the plane, which is created by vectors. The procedure is conducted by creating a plane with two vectors corresponding to the two most significant SVD values. Afterwards, we project all OD values into the plane, normalizing to unit length and curving the projected line. With these, we can compute each angle to the first SVD direction, thus, mapping the direction in the plane. As a result, the pixel intensity histogram can be computed, followed by determining the concentration of each stain with the H&E matrix in relation to the OD values. Finally, we can yield I_{out} by using the H&E matrix with the normalized stain concentration33,34.

#### Structure-preserving color normalization

Structure-Preserving Color Normalization (SPCN)35 operates by decomposing I_s into sparse stain density maps while integrating the stain from T. Algorithm 3 illustrates the implementation of SPCN. Given I_s \in \mathbb{R}^{m \times n} is the RGB image matrix, where m denotes the number of RGB channels and n denotes the number of pixels. Let w \in \mathbb{R}^{m \times n} be the stain matrix with columns representing the chromatic variance of each stain, where r represents the stain number. Let H \in \mathbb{R}^{r \times n} represents the stain density maps where the rows denote the stain concentration. Thus, I_s is described as:

I_s = I_e \star WH \quad (11)

Let V be the OD maps then,

V = \log\left(\frac{I_o}{I_s}\right) \quad (12)

By utilizing Eq. (11), we can form:

V = WH \quad (13)

where V = observation matrix, H = stain density map matrix, and W = stain color appearance matrix. Next, we implement the sparse non-negative matrix factorization (SNMF) for stain separation. Based on the Beer-Lambert law, the RGB image is converted into the OD maps with Eq. (14). Then, the sparseness constraint is added in Eq. (11). SNMF separates stain with l_1- sparseness and H_1 = stain mixing coefficient where, j = index of stains that is j = 1, 2, \dots, r.

\varphi(p) = -\log(V(p)) \quad (14)

where \varphi denotes as the OD space, p = pixel intensity where, p \in \text{pixel}P.

Scientific Reports | (2023) 13:20518 |

https://doi.org/10.1038/s41598-023-46619-6

nature portfolio

7

---

<!-- Page 8 -->

www.nature.com/scientificreports/

|   | **Input:** I_{in}, T \in \{T1, T2, T3, T4, T5\} |
| --- | --- |
|   | **Output:** I_{out} |
| 1 | Read I_{in} and T |
| 2 | Apply BLT with Equation (14) |
| 3 | Sparse stain separation using SNMF with Equations (15) and (16) |
| 4 | Stain normalization |
| 5 | Apply inverse BLT |
| 6 | I_{out} \leftarrow normalized I_z |

**Algorithm 3.**
 Structure-Preserving Color Normalization

\min_{\lambda} \frac{1}{2} \|V - WH\|_F^2 + \sum_{j=1}^C \|H(j, :)\|_1, W, H \geq 0 \quad (15)

\|W(c, :)\|_2^2 = 1 \quad (16)

where \lambda is the sparsity and regularization parameter. Additional constraints on W and H will decrease the solution space of W/\alpha and \alpha H, where \alpha is a positive value. Equation (12) represents a non-convex optimization problem, which can be addressed by alternating optimizing one parameter of H and W while holding the other constant. Elements are randomly selected from the optical density \tau to initialize the color appearance matrix.

Subsequently, we transfer the color \mu of T to I_z while approximating the color appearance matrix for stain normalization. Utilizing the SNMF, we factorize the stain density maps V_s into W_s H_s and V_t into W_t H_t. Afterwards, the stain density maps of source H_s are merged with the template W, color appearance matrix instead of the source color appearance matrix W_s to produce the normalized image. As a result, stain density map H maintains the structure while the color appearance matrix W maintains changes in the color appearance. Lastly, the inverse Beer-Lambert transformation (BLT) is applied to the normalized stains to obtain I_{out}^{color}.

*Adaptive color deconvolution technique*

Adaptive Color Deconvolution (ACD)10 normalizes stains by integrating optimization to approximate the stain separation parameters and color normalization. ACD is based on color deconvolution (CD)17. Let x_i \in \mathbb{R}^{3 \times 1} denote the RGB values of each i-th pixel in I_c. CD is described with Eqs. (17) and (18):

o_i = -\ln \left( \frac{x_i}{I_{max}} \right) \quad (17)

s_i = D \cdot o_i \quad (18)

Where o_i \in \mathbb{R}^{3 \times 1} represents the OD of RGB channels, I_{max} is background intensity, and D \in \mathbb{R}^{3 \times 3} is CD matrix. The separated densities of stains are denoted s_i = (h_i, c_i, d_i)^T, where h_i = hematoxylin stain, c_i = eosin stain, and d_i = separation residual. CD matrix D is decided by a Stain Color Appearance (SCA) matrix M, where D = M^{-1}. Therefore, ACD is derived by applying a stain-weight matrix W = \text{diag}(w_{h_1}, w_{c_1}, w_{d_1}) to directly optimize the stain separation parameters and color normalization. We modify Eq. (18) to form Eq. (19):

s_i = W \cdot D \cdot o_i \quad (19)

The SCA matrix M = (m_{h_1}, m_{c_1}, m_{d_1}), where m_j \in \mathbb{R}^{3 \times 1} (j = h_i, c_i, d_i) is a unit vector representing the contributions of the j-th stain to the RGB channels intensities. M is determined by \varphi, representing as M(\varphi) and CD matrix D as D(\varphi), where \varphi is a collection of six-degree variables \varphi = (\alpha_{h_1}, \beta_{h_1}, \alpha_{c_1}, \beta_{c_1}, \alpha_{d_1}, \beta_{d_1}). Thus, we perform optimization by minimizing the objective function \mathcal{L}_{ACD}(\varphi) of variables \varphi and W:

(\bar{\varphi}, \bar{W}) = \text{argmin} \mathcal{L}_{ACD}(\varphi, W) \quad (20)

We employed the gradient descent to solve \mathcal{L}_{ACD}(\varphi, W) which is continuous and differentiable for variables \varphi and W. By resolving \mathcal{L}_{ACD}(\bar{\varphi}, \bar{W}) and \bar{W} can be obtained, followed by determining the adaptive matrices M(\bar{\varphi}) and D(\bar{\varphi}) for the I_c. After the optimization, we obtain the adaptive variables for the stain separation \bar{D} and stain intensity normalization \bar{W}. Subsequently, we separate the I_c stain components with \bar{D} followed by weighting with \bar{W}. Lastly, we recombine the weighted stain components with the SCA matrix of the template T \bar{M} to obtain I_{out}. The following Eqs. (17), (21) and (22) summarize ACD techniques for the i-th pixel x_i:

o_i = -\ln \left( \frac{x_i}{I_{max}} \right) \quad (17)

\bar{w}_i = \bar{M} \cdot \bar{W} \cdot o_i \quad (21)

Scientific Reports | (2023) 13:20518 |

https://doi.org/10.1038/s41598-023-46619-6

nature portfolio

6

---

<!-- Page 9 -->

www.nature.com/scientificreports/

Input: I_s, T \in \{T1, T2, T3, T4, T5\}, I_{max}, D, \phi, \bar{M}
Output: I_{out}

1. 1 ReadI_sto obtainx_i
2. 2 ReadTto obtain\bar{M}
3. 3 ConvertRGBtoODspace with Equation (17)
4. 4D(\phi), \bar{W} \leftarrowoptimise Equation (19) by minimizingL_{ACD}(\phi, W)with gradient descent
5. 5I_{out} \leftarrowstain separation, weighting\bar{W}and recombination with\bar{M}with Equations (21) and (22)
6. 6 ConvertODback toRGBcolor space

Algorithm 4. Adaptive Color Deconvolution

I_{out} = \bar{x}_i = \exp(-\bar{v}_i) \cdot I_{max} \quad (22)

### StainGAN

StainGAN40 is inspired by CycleGAN45 that transfers stains between two domains without requiring paired data from both domains. StainGAN is composed of two pairs, each consisting of a generator and a discriminator. The first pair (G_1 and D_1) aims to map images from Domain B to Domain A (X_{B1} \rightarrow X_{A1}). The Generator G_1 aims to generate images that match Domain A. The discriminator D_1 tries to verify if images originate from Domain A or the fake generated ones. The other pair (G_2 and D_2) undergoes the same process in the reverse direction, G_2: X_{A2} \rightarrow X_{B2} as:

\hat{X}_A = G_A(X_B; \theta_A), \hat{X}_B = G_B(X_A; \theta_B), s.t. d(\hat{X}_B, \bar{X}_B) \leq \epsilon \quad (23)

\hat{X}_B = G_B(X_A; \theta_B), \hat{X}_A = G_A(X_B; \theta_A), s.t. d(\hat{X}_A, \bar{X}_A) \leq \epsilon \quad (24)

where d(\cdot, \cdot) = distance metric between the input image and the reconstructed image (cycle-consistency constraint), and both \theta_A and \theta_B are the model parameters. StainGAN is trained to minimize adversarial and cycle-consistency loss (see Algorithm 5 for StainGAN training details). The cycle-consistency loss ensures that the output from G_1 can be reconstructed back to the input for G_2 and similarly, the output from G_2 can be reconstructed back to the input for G_1. The adversarial loss assures that the stain of the reconstructed images is coherent with the actual stain distribution.

Where the cycle-consistency loss for the B \rightarrow A \rightarrow B cycle, \mathcal{L}_{cycle}^{(B \rightarrow A \rightarrow B)} is described as follow:

\mathcal{L}_{cycle}^{(B \rightarrow A \rightarrow B)} = \frac{1}{m} \sum_{i=1}^m (b^{(i)} - D_{A \rightarrow B}(G_{B \rightarrow A}(b^{(i)})))^2 \quad (25)

### StainNet

StainNet47 normalizes the source dataset by learning the color mapping relationship from the target dataset and adjusting its color value pixel by pixel. StainNet is a CNN comprising three convolutional layers with 32 kernels. StainNet necessitates the pairing of source and target images to facilitate the learning of color space conversion from the source to the target. Therefore, StainNet relies on the output of StainGAN to obtain the paired images. Specifically, we treat StainGAN as the teacher model while StainNet as the student model. The output images from StainGAN are treated as truth labels for the StainNet to train. Thus, the primary objective of the StainNet is to minimize the L1 loss with SGD optimizer corresponding to the normalized images generated by StainGAN (see Algorithm 6 for StainNet training details). The mapping association of StainGAN is contingent on the image content. Therefore, by training on images normalized by StainGAN, StainNet can convert the content-based mapping association of StainGAN into a pixel value-based mapping.

### Implementation details

This section outlines the implementation details of training CNN models on various stain-normalized datasets. The objective is to evaluate the performance of these models when trained on diverse stain-normalized datasets.

#### Dataset description

Dataset description We adopted the dataset strategy proposed by Abdelli et al.13, known as the Four Breast Cancer FBCG dataset (FBCG) dataset to address the limitations of the existing small IDC grading datasets. The FBCG dataset entails 888 RGB H&E stained 400X-magnification IDC histopathological images with four classes: Grade 0 (G0),

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

9

---

<!-- Page 10 -->

www.nature.com/scientificreports/

Inputs: Domain A, Domain B
1 for epoch in epochs do
2   Draw a minibatch of samples \{a^{(1)}, \dots, a^{(m)}\} from Domain A
3   Draw a minibatch of samples \{b^{(1)}, \dots, b^{(m)}\} from Domain B
4   Compute discriminator loss on inputs from Domain A:
L_A^{(D)} = \frac{1}{m} \sum_{i=1}^m (D_A(a^{(i)}) - 1)^2 + \frac{1}{n} \sum_{j=1}^n (D_B(b^{(j)}) - 1)^2
5   Compute discriminator loss on inputs from Domain B:
L_B^{(D)} = \frac{1}{m} \sum_{i=1}^m (D_B(G_{A \rightarrow B}(a^{(i)})) - 1)^2 + \frac{1}{n} \sum_{j=1}^n (D_A(G_{B \rightarrow A}(b^{(j)})) - 1)^2
6   Update D_A and D_B
7   Compute the B \rightarrow A generator loss:

L_{(G_{B \rightarrow A})} = \frac{1}{m} \sum_{i=1}^m (D_A(G_{B \rightarrow A}(b^{(i)})) - 1)^2 + L_{\text{cycle}}^{(B \rightarrow A \rightarrow B)}

8   Compute the A \rightarrow B generator loss:
L_{(G_{A \rightarrow B})} = \frac{1}{n} \sum_{j=1}^n (D_B(G_{A \rightarrow B}(a^{(j)})) - 1)^2 + L_{\text{cycle}}^{(A \rightarrow B \rightarrow A)}
9   Update G_A and G_B
10 end for

**Algorithm 5.**
 StainGAN Training Loop

Input: normalized images from StainGAN, D_{SG}
1 for epoch in epochs do
2   for X batch in D_{SG} do
3     \hat{y} = \text{StainNet}(X, \theta)
4     Compute \text{loss} = L_{1, \text{loss}}(\hat{y}, y)
5     Compute gradient, \nabla_{\text{loss}} of the \theta with respect to the \text{loss}
6     Update \theta \leftarrow \text{SGD}(\nabla_{\text{loss}}, \theta)
7   end for
8 end for

**Algorithm 6.**
 StainNet Training Loop

|   | Grade 0 | Grade 1 | Grade 2 | Grade 3 | Total |
| --- | --- | --- | --- | --- | --- |
| Train set | 470 | 86 | 82 | 73 | 711 |
| Test set | 118 | 21 | 20 | 18 | 177 |
| Total | 588 | 107 | 102 | 91 | 888 |

**Table 1.**
 The class distribution and proposed train-test split of the FBCG dataset.

Grade 1 (G1), Grade 2 (G2), and Grade 3 (G3). The images in the G0 class (588 in total) are sourced from the Benign class of the BreastHs dataset48, captured at a 400X magnification. The images in the other classes (500 in total) are sourced from the BCHI dataset49. Table 1 summarizes the composition of the FBCG dataset.

RCHI dataset. The Breast Carcinoma Histological Images (BCHI) dataset49 includes 300 H&E-stained breast histopathology images (1280 × 960 pixels) from the pathology department at “Agios Pavlos” Hospital in Thessaloniki, Greece. The images, which depict carcinoma specimens, are categorized into three grades: Grade 1 (with 107 images), Grade 2 (with 102 images), and Grade 3 (with 91 images). These images are sourced from 21 IDC

Scientific Reports | (2023) 13:20513 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

10

---

<!-- Page 11 -->

www.nature.com/scientificreports/

Figure 3. Samples images with 400X magnification from the BCHI dataset: (a) Grade 1, (b) Grade 2, (c) Grade 3.

Figure 4. Samples from the BreakHIs dataset distributed into two major classes: (a) Benign and (b) Malignant with four magnification factors.

patients. The images were captured using a Nikon camera and a 40X magnification objective lens on a compound microscope (see Fig. 3).

BreakHIs dataset. The BreakHIs dataset60 comprises 7909 histopathological images of breast cancer, sourced from 82 patients. Initially, the H&E-stained slide was captured at four magnification factors (40X, 100X, 200X, and 400X), using four objective lenses (4X, 10X, 20X, and 40X). These images were then converted into digital RGB format dimensions of 700 by 460 pixels. The BreakHIs is primarily divided into two categories: (1) Benign (2450 images) and (2) Malignant (5429 images). Each of the category can be further subdivided into four sub-classes. For the Benign class, these are: (1) Adenosis, (2) Fibroadenoma, (3) Phyllodes Tumor, and (4) Tubular Adenoma. For the Malignant class, the sub-classes are: (1) Ductal Carcinoma, (2) Lobular Carcinoma, (3) Mucinous Carcinoma, and (4) Papillary Carcinoma (see Fig. 4). Table 2 provides a detailed distribution of the images by major classes and magnifications within the BreakHIs dataset.

#### Experiment setup

In this study, we assessed the base dataset (original FBGC dataset), represented as D_B, comprising 2D pixel elements with three RGB channels and their corresponding ground truth labels. We employed six selected SN techniques: Reinhard (R), Macenko (M), SPCN (S), ACD (A), StainGAN (SG) and StainNet (ST) on D_B to create stain-normalized dataset D_{SN}. Here, SN \in \{R, M, S, A, SG, ST\} denotes the SN technique and T \in \{T1, T2, T3, T4, T5, \emptyset\} (The \emptyset is reserved for SG and ST where T is not required) signifies the template used. For example, D_{R,T1} refers to the dataset normalized using the Reinhard technique with Template T1. Each dataset was split into a training set D_{Tr} and a test set D_{Te} in an 80%-20% ratio (see Table 1 for the train/test split).

We conducted Stratified Five-fold Cross-validation (SFCV) on the training set D_{Tr} by dividing it into five subsets, using one subset for validation and the remaining subsets for training. With SFCV, we can compute the

Scientific Reports | (2023) 13:25018 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

11

---

<!-- Page 12 -->

www.nature.com/scientificreports/

| Magnification | Benign | Malignant | Total |
| --- | --- | --- | --- |
| 40x | 625 | 1,370 | 1,995 |
| 100x | 644 | 1,437 | 2,081 |
| 200x | 623 | 1,390 | 2,013 |
| 400x | 588 | 1,232 | 1,820 |
| Total | 2,480 | 5,429 | 7,909 |

Table 2. The BreakHis image distribution by two major classes and four magnifications.

| Architecture | Characteristic | FLOPs (B) | Parameters (M) |
| --- | --- | --- | --- |
| EfficientNet-B0 (EffB0) 10 | Compound scaling | 0.39 | 5.3 |
| EfficientNet-V2-B0(EffB0V2) 10 | Progressive learning | 0.72 | 7.1 |
| EfficientNet-V2-B0-V18(EffB0V2-21k) 10 | Progressive learning | 0.72 | 7.1 |
| ResNet-V1-50(RN1) 11 | Residual learning | 4.1 | 25.6 |
| ResNet-V2-50(RN2) 11 | Identity mapping | 4.1 | 25.6 |
| MobileNet-V1(MB1) 12 | Depth-wise separable convolutions | 0.6 | 4.2 |
| MobileNet-V2(MB2) 12 | Inverted residuals and linear bottlenecks | 0.3 | 3.4 |

Table 3. Description of the seven pre-trained CNNs in terms of their characteristics, number of FLOPs, and number of parameters.

Figure 5. The structure of the model. (a) input layer, (b) augmentation layers, (c) feature extractor (non-trainable), (d) dropout layer, (e) dense layer (trainable), and (f) output prediction layer (trainable).

mean \mu and standard deviation \sigma from results obtained from each subset for model stability evaluation (based on \sigma) and hyperparameters optimization. This process helps to minimize result variability, promote model stability, and provide a comprehensive performance evaluation across the base dataset D_b. After SFFCV, we retrained our models with the whole training set D_{Trn} and tested the testing set D_{Trs} to obtain our baseline test result. Then, we repeated this procedure the stain-normalized training sets D_{Trn} in D_{Stn,T} and tested on the stain-normalized testing sets D_{Trs} in D_{Stn,T} to investigate the performance of CNN models trained with different stain-normalized datasets (see Algorithm 8).

Before model training, we generated batches of pre-processed image data from each dataset with different image pre-processing functions (see Table 5). We also applied the class-weighting algorithm to address imbalanced classes in each dataset, ensuring the model converges for the minor classes in minimizing loss26. Equation (26) below describes the class-weighting algorithm.

ClassWeight = \frac{N}{N_b \times N_c} \quad (26)

where N = number of images of all classes, N_b = number of classes and N_c = number of images per class.

For the model implementation, we adhered to the approach outlined in Voon et al.28. We utilized seven pre-trained CNNs (see Table 3) from EfficientNet10 and ImageNet-21k12 as feature extractors. Each model is composed of an input layer, augmentation layers, a feature extractor denoted as f_\theta with model parameter \theta, and a classifier denoted as C(\cdot|W) with weight matrix W \in \mathbb{R}^{d \times c}. Our model structure is illustrated in Fig. 5. The classifier C(\cdot|W) includes of two dropout layers and dense layers, with the final dense layer equipped with four neurons and a SoftMax activation function for classification (see Table 4). We kept the parameter \theta in the f_\theta fixed and trained a new classifier C(\cdot|W) on each training set D_{Trn} by minimizing the weighted categorical cross-entropy loss, WCCE_{loss} (see Eq. (27)) using the Adam Optimizer27. Subsequently, we tested each trained classifier on its

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

12

---

<!-- Page 13 -->

www.nature.com/scientificreports/

| Block | Detail |
| --- | --- |
| 0 | Input layer, shape = (224, 224, 3) |
| 1 | Augmentation layers: |
| 1 | Random flip layer, mode = horizontal and vertical |
| 1 | Random rotation layer, factor = 0.2 |
| 1 | Random zoom layer, height factor = 0.2 |
| 2 | Feature extractor f_\theta |
| 3 | Dropout layer, rate = 0.5 |
| 3 | Dense layer, 256 neurons with ReLU function |
| 3 | Dropout layer, rate = 0.4 |
| 3 | Dense layer, 4 neurons with SoftMax function for final prediction |

Table 4. The structure of the model which follows the implementation of Voon et al.56.

|   | Operation | Value |
| --- | --- | --- |
| Pre-processing function | Rescale | 1/255 |
| Pre-processing function | Resize | 224 by 224 pixels |
| Pre-processing function | Shuffle | true |
| Pre-processing function | Seed | 123 |
| Pre-processing function | Batch | 16 |
| Hyperparameter | Loss function | WCCF loss |
| Hyperparameter | Optimizer | Adam |
| Hyperparameter | Learning rate | 0.001 |
| Hyperparameter | Metric | accuracy |
| Hyperparameter | Epochs | 100 |

Table 5. Details of image pre-processing and hyperparameters for model compilation.

corresponding testing set D_{TS}. The optimal learning rate and the number of epochs for model training were determined through SIFTCCV (see Table 5).

WCCF_{loss} = -w_T \log \left( \frac{e^y}{\sum_j e^{y_j}} \right) \quad (27)

where w_T = classes weights, S_y = positive output score and S_j = other classes output scores.

We primarily utilized the Balanced Accuracy (BAC) score as the evaluation metric for assessing model performance. The BAC, which calculates the average recall of each class, is computed using true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN). The following mathematical expression defines the BAC:

BAC = \frac{1}{|N_T|} \sum_{i=1}^{|N_T|} \frac{TP_i}{TP_i + FN_i} \quad (28)

## Results and discussion

### Results of stratified five-fold cross-validation

Table 6 presents the cross-validation and test outcomes of the seven models trained on the base dataset D_B. Please note, the test result forms the baseline for subsequent comparisons. Interestingly, all models secured high BAC scores (> 0.9) in the base test set D_{TS} in D_B. Among all models, the EBOV2-21k and MBI models achieve the highest BAC score (0.9524). For the validation result, we observe that the EBOV2-21k model achieves the highest BAC with relatively high stability (\mu = 0.9666, \sigma = 0.0185). Generally, all models show low result variability. In other words, the models can generalize well across different subsets in D_{TS}.

### Results of conventional stain normalization techniques

Figure 6, derived from Supplementary Tables 2–5, depicts the mean test BAC scores of seven models trained with datasets normalized using Reinhard, Macenko, SPCC, and ACD techniques across T_i. Our results underscore that the ACD technique yielded the highest average BAC score (0.905) across T_i, succeeded by Macenko (0.8835), SPCC (0.8567), and Reinhard (0.8407) techniques. Nonetheless, none of the techniques managed to surpass

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

13

---

<!-- Page 14 -->

www.nature.com/scientificreports/

**Input:**
 train set from the FBGC dataset, 
D_{TR} \in D_B
, class weights 
w

**Output:**
 validation results, 
val\_result

1 
**for**
 
K, (K - 1)
 
**in**
 
SFCV(D_{TR})
 
**do**

2   
**for**
 
epoch \in epochs
 
**do**

3     
**for**
 
X, y
 
**batch**
 
\in D_{(K-1)}
 
**do**

4       
\hat{y} = C(X|W, w)

5       Compute 
loss = WCC_{loss}(\hat{y}, y)

6       Compute the gradient, 
\nabla_{loss}
 of the 
W
 with respect to the 
loss

7       Update 
W \leftarrow Adam(\nabla_{loss}, W)

8   
**end for**

9 
**end for**

10 
**end for**

11 
\hat{y} = C(D_{tr}|W)

12 
val\_result = BAC(\hat{y}, y)

**Algorithm 7.**
 SFCV Model Training and Validation Loop

**Input:**
 train set, 
D_{TR}
, test set, 
D_{TS}
, and class weights 
w

**Output:**
 test results, 
test\_result

1 
**for**
 
epoch \in epochs
 
**do**

2   
**for**
 
X, y
 
**batch**
 
\in D_{TR}
 
**do**

3     
\hat{y} = C(X|W, w)

4     Compute 
loss = WCC_{loss}(\hat{y}, y)

5     Compute gradient, 
\nabla_{loss}
 of the 
W
 with respect to the 
loss

6     Update 
W \leftarrow Adam(\nabla_{loss}, W)

7   
**end for**

8 
**end for**

9 
\hat{y} = C(D_{tr}|W)

10 
test\_result = BAC(\hat{y}, y)

**Algorithm 8.**
 Model Training and Test Loop

| Model | SFCV ( \mu \pm \sigma ) | Test |
| --- | --- | --- |
| EB0 | 0.9030 \pm 0.0322 | 0.9518 |
| EB0V2 | 0.9076 \pm 0.0398 | 0.9024 |
| EB0V2-21k | **0.9666 \pm 0.0185** | **0.9524** |
| RN1 | 0.9253 \pm 0.0310 | 0.9239 |
| RN2 | 0.9346 \pm 0.0156 | 0.9198 |
| MB1 | 0.9518 \pm 0.0232 | **0.9524** |
| MB2 | 0.9362 \pm 0.0322 | 0.9128 |
| \mu \pm \sigma | **0.9361 \pm 0.0189** | 0.9308 \pm 0.0211 |

**Table 6.**
 Cross-Validation and test BACs of seven models trained in 
D_B
. The bolded values represent the highest score in each section.

the baseline result (0.9308). Among T, T5 yields the highest average BAC scores with Reinhard, Macenko, and SPCCN techniques, whereas T1 attains the highest BAC using the ACD technique. T5 consistently achieves good results across different SN techniques. The superior performance of T5 may be attributed to the consideration of the dominant color in the target images. In histopathological images, the dominant color often corresponds to the stain used, which carries crucial information for classification tasks. By effectively capturing the dominant

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

14

---

<!-- Page 15 -->

www.nature.com/scientificreports/

| Model | Reinhard | Macenko | SPCC | ACD | Baseline |
| --- | --- | --- | --- | --- | --- |
| T1 | 0.84 | 0.85 | 0.86 | 0.87 | 0.9308 |
| T2 | 0.86 | 0.87 | 0.88 | 0.89 | 0.9308 |
| T3.1 | 0.87 | 0.88 | 0.89 | 0.90 | 0.9308 |
| T3.2 | 0.88 | 0.89 | 0.90 | 0.91 | 0.9308 |
| T3.3 | 0.89 | 0.90 | 0.91 | 0.92 | 0.9308 |
| T4 | 0.85 | 0.86 | 0.87 | 0.88 | 0.9308 |
| T5 | 0.87 | 0.88 | 0.89 | 0.90 | 0.9308 |

Figure 6. The mean test BAC scores of the seven models across T with different conventional SN techniques from Supplementary Tables 1, 2, 3, and 4. The ACD technique tops other techniques across all templates but failed to outperform the baseline result.

color, T5 can guide the SN process to better preserve or standardize this critical information, leading to improved classification performance.

Among conventional SN techniques, we noted that template selection minimally impacts the ACD technique due to its small \sigma (refer to Supplementary Table 4). In contrast, the Reinhard, Macenko and SPCC techniques are more heavily affected by the template selection. Hence, we propose that judicious template selection is crucial for Reinhard, Macenko and SPCC techniques. Additionally, we suggest using the ACD technique for SN over other techniques if a conventional SN technique is required in the image pre-processing pipeline.

#### Results of deep learning-based stain normalization techniques

Figure 7, derived from Table 6 and Supplementary Table 5, depicts the test BAC scores of seven models trained with StainGAN-normalized, StainNet-normalized, and non-normalized datasets. We noted a high similarity in the performance of models trained with StainGAN-normalized and StainNet-normalized datasets, aligning with the findings by Kang et al.72 Nonetheless, models trained with the StainGAN-normalized dataset exhibited marginally higher mean test BAC scores (0.9196) than those trained with the StainNet-normalized dataset (0.9192). Additionally, our findings highlight that deep learning-based SN techniques failed to outperform the baseline result. Therefore, our results underscore the importance of context-specific application of these techniques and suggests that they may not universally lead to improved performance in every scenario.

#### Evaluation of the effectiveness of stain normalization in the IDC grading task

In this section, we assessed the efficacy of SN in IDC grading using the FBGC dataset. Figure 8 illustrates the mean test BAC scores of the seven models trained in six different stain-normalized and the non-normalized datasets. Our results underscore that models trained with StainGAN-normalized images surpass those trained with other stain-normalized images. Hence, we compared the test mean BAC score between models trained with the StainGAN-normalized dataset and models trained with the non-normalized dataset. The results of the t-test indicated that the mean BAC score was statistically insignificant between models trained with the StainGAN-normalized FBGC dataset (\mu = 0.9196, \sigma = 0.0188) and models trained with the non-normalized dataset (\mu = 0.9308, \sigma = 0.0211), p = 0.11. The p-value indicates that the probability of obtaining the results is 11% by chance. Since the p-value of 0.11, higher than the significance level, \alpha = 0.05, suggests the difference in mean BAC scores between models trained with the StainGAN-normalized dataset and models trained with the non-normalized dataset is statistically insignificant. Consequently, we did not dismiss the null hypothesis, suggesting no significant difference in the performance of stain-normalized and non-normalized datasets for IDC grading tasks.

Furthermore, it is possible that SN techniques strip distinct color features10 from IDC images, leading to poorer model performance. Findings oppose the previous work that SN is essential to accomplish good performance in histopathological classification tasks, aligning with other similar studies36–39. Therefore, we suggest that future studies should conduct ablation studies with the employed dataset regarding the effectiveness of SN in their applications. Despite the ineffectiveness of SN in our IDC grading task, we acknowledge its contribution as evidenced by its benefits in other studies41–45. In response to the claim that SN may eliminate color features in IDC images, future studies could explore the influence of these color features on the generalizability of the CNN.

Scientific Reports | (2023) 13:25018 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

15

---

<!-- Page 16 -->

www.nature.com/scientificreports/

| Dataset | Model | Mean Test BAC |
| --- | --- | --- |
| StainGAN | ESM | 0.6215 |
| StainGAN | RNN1 | 0.6276 |
| StainGAN | RNN2-21k | 0.6232 |
| StainGAN | RNN | 0.6236 |
| StainGAN | RNN | 0.6234 |
| StainGAN | MGG | 0.6298 |
| StainGAN | MGG | 0.6242 |
| Baseline | ESM | 0.6200 |
| Baseline | RNN1 | 0.6202 |
| Baseline | RNN2-21k | 0.6202 |
| Baseline | RNN | 0.6202 |
| Baseline | RNN | 0.6202 |
| Baseline | MGG | 0.6202 |
| Baseline | MGG | 0.6202 |

Figure 7. The test BAC scores of seven models trained with StainGAN-normalized, StainNet-normalized, and non-normalized datasets. Although the results are comparable among the deep learning-based SN techniques, the mean BAC scores of the seven models trained in the StainGAN-normalized dataset achieve slightly higher than models trained in the StainNet-normalized dataset but lower than the baseline result.

| Technique | Mean Test BAC |
| --- | --- |
| Reinhard | 0.8407 |
| Macenko | 0.8835 |
| SPCN | 0.8507 |
| ACD | 0.9003 |
| StainGAN | 0.9196 |
| StainNet | 0.9192 |

Figure 8. The mean test BAC scores of the seven models trained in six different stain-normalized and the non-normalized FBCG datasets. Among the six SN techniques, the StainGAN technique outperforms other SN techniques. However, the baseline result tops the best SN results by 0.0112 score.

In summary, the impact of SN on recent breast cancer histopathological studies has been the subject of debate. Our study aimed to elucidate this matter by scrutinizing the efficacy of SN techniques in breast cancer histopathological classification tasks, particularly in IDC grading, using CDDN. We selected six conventional and deep learning-based SN techniques to evaluate their effectiveness, along with seven pre-trained CNNs from ImageNet and ImageNet-21k as feature extractors. Our findings revealed that the impact of SN on this task was not statistically significant. Consequently, we did not reject the null hypothesis, suggesting that there was no substantial difference in effectiveness between stain-normalized and non-normalized datasets for IDC grading tasks. This outcome challenges the prevailing assumption that SN invariably enhances classification outcomes, thereby contributing a nuanced perspective to the discourse on the role of SN in breast cancer histopathological studies.

#### Limitations of study

The scope and limitations of our study focused on investigating the effectiveness of SN on IDC grading using only the FBCG dataset. Future work will incorporate other IDC grading datasets, such as DataBioxx and

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

16

---

<!-- Page 17 -->

www.nature.com/scientificreports/

PathIODCG38. Additionally, our study did not account for potential variations in staining protocols across different centers. This is a significant consideration, since the staining process can greatly influence the color and intensity of histopathological images, which in turn can impact the performance of the model. While our findings underscore the impact of SN on IDC grading, they may not extend to scenarios where training and testing data come from separate centers. This limitation will be addressed in future work.

We utilized six different SN techniques in this study and plan to incorporate additional techniques39,40 in future research. Subsequently, we selected five templates from the PCAN train set to accommodate the CanSlay16 pre-trained StainGAN and StainNet. These templates were chosen as the results of applying three different similarity functions: (1) Cosine Similarity (Sim_C), (2) Mean Square Error (MSE), and (3) the Structural Similarity Index (SSIM), along with considering the most dominant color of the average image and the target images. The selection process aimed to identify templates that closely resemble the stain distributions in the target dataset. By using different similarity metrics, we were able to ensure that each template provided a unique perspective on the target data. This approach allowed us to select the five templates that best captured the color characteristics of the target dataset. This selection process has an empirical aspect, as there is no one-size-fits-all rule for template selection in style transfer.

For the model implementation, we only selected seven pre-trained CNNs for evaluations based on the implementation of Voon et al.39. We omitted other state-of-the-art CNNs41–43 from our study but reserved them for future work. This study focused on the effectiveness of SN in the application; thus, we disregarded advanced model optimizations such as model fine-tuning and hyperparameter tuning.

## Challenges of study

We encountered two significant challenges during the experimentation: (1) data imbalance and (2) model overfitting. An imbalance in the majority class bias into the CNN, causing the CNN to favor the majority class. Hence, we implemented the class-weighting algorithm that assigned higher weights to minority classes to increase the penalty. Given the relatively small size of our FBCG dataset compared to other breast cancer-related datasets, we noted a risk of model overfitting with complex CNN architectures. To mitigate this, we incorporated augmentation layers into our model to enhance data diversity and avoid two dropout layers in our classifier to randomly nullify input units, thereby preventing overfitting during training.

## Conclusion

In this study, we set out to address the question of the effectiveness of Stain Normalization (SN) in the task of Invasive Ductal Carcinoma (IDC) grading. To accomplish this, we utilized seven pre-trained Convolutional Neural Network (CNN) models as feature extractors to classify the FBCG dataset into four IDC grades. The FBCG dataset was stain-normalized using six techniques: StainGAN, StainNet, StainGAN, and StainNet. For the conventional SN techniques, we selected five templates to investigate their impacts on each method. We conducted a comparative analysis of models trained with and without SN to understand the impact of SN on the classification results for enhanced data diversity and avoid two dropout layers in our classifier to randomly nullify input units, thereby preventing overfitting during training. Our findings revealed that the StainGAN and StainNet Accuracy (BAC) score of models trained with StainGAN-normalized (best-performing SN technique) images and non-normalized images. This indicates that there is no statistically significant difference in the effectiveness of stain-normalized datasets for IDC grading tasks. Contrary to common belief, our study suggests that SN may not be as crucial for histopathological classification tasks as previously thought. However, if SN is required in the image pre-processing pipeline, we recommend StainGAN, StainNet, and ACD techniques due to their relative performance in stain normalizing images. Looking forward, in addition to extending our future work with the consideration mentioned in Sect. 4.5, we plan to examine the generalizability of the CNN model with respect to color features in IDC. Additionally, we aim to explore the inconsistent effects of SN on different breast cancer histopathological classification tasks.

## Data availability

The origin datasets combined for the current study are available in the Four Breast Cancer Grades (FBCG) Dataset, https://web.itl.nifp.fr/v1/databases/breast-cancer-histopathological-database-breakish/, and Breast cancer histological images from the Department of Pathology, https://zenodo.org/record/839410#.WXhxt4rfjFcs. Should there be any inquiries regarding the employed datasets, please contact the corresponding author, Dr. Hlum Yan Chai (hlumyan@eudmu.y) for further information and clarification.

Received: 28 February 2023; Accepted: 2 November 2023

Published online: 22 November 2023

## References

1. Sharma, G. N., Dave, R., Soodia, I., Sharma, P. & Sharma, M. K. Various types and management of breast cancer: An overview.J. Adv. Phys. Technol. Res.1, 109–120 (2010).
2. Henson, D. E., Ries, L., Freedman, L. S. & Carriaga, M. Relationship among outcome, stage of disease, and histologic grade for 22,616 cases of breast cancer. The basis for a prognostic index.Cancer68, 242–249 (1991).
3. Friakov-Grazio, S. & Bracco, M. Long-term prognostic value of Nottingham histological grade and its components in early (T1) Infiltrating breast carcinoma.J. Clin. Pathol.55, 88–92 (2002).
4. Schwartz, A. M., Henson, D. E., Chen, D. & Ramamurthy, S. Histologic grade remains a prognostic factor for breast cancer regardless of the number of positive lymph nodes and tumor size: A study of 161 708 cases of breast cancer from the SEER program.Arch. Pathol. Lab. Med.148, 1048–1052 (2014).
5. Kabak, E. A. et al. Breast cancer prognostic classification in the molecular era: The role of histological grade.Breast Cancer Res.12, 2607 (2010).

Scientific Reports | (2023) 13:25018 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

17

---

<!-- Page 18 -->

www.nature.com/scientificreports/

1. 6. Johns Hopkins University.Staging and Grade - Breast Pathology(Johns Hopkins Pathology, 2021).https://pathology.jhu.edu/breast/staging/grade.
2. 7. He, L., Leng, L., Antonsi, S. & Thoma, G. R. Histology image analysis for carcinoma detection and grading.Comput. Methods Programs Biomed.107, 538–556 (2012).
3. 8. Elmine, J. G. et al. Diagnostic concordance among pathologists interpreting breast biopsy specimens.JAMA313, 1122–1132 (2015).
4. 9. Príego-Torres, B. M., Sánchez-Morillo, D., Fernandez-Granero, M. A. & García-Rojo, M. Automatic segmentation of whole-slide H&E-stained breast histopathology images using a deep convolutional neural network architecture.Expert Syst. Appl.151, 113387 (2020).
5. 10. Dulle, J., Leow, W. K., Racocevic, D., Tutac, A. E. & Putter, K. Automatic breast cancer grading of histopathological images.Annu. Int. Conf. IEEE Eng. Med. Biol. Soc.2008, 3052–3055 (2008).
6. 11. Doyle, S., Agner, S., Madabhushi, A., Feldman, M. & Tomaszewski, J. Automated grading of breast cancer histopathology using spectral clustering with a deep architectural image feature extractor.IEEE Trans. Med. Imaging36, 1090–1100 (2017).https://doi.org/10.1109/TMI.2017.2691090(From Nano to Macro, Proceedings, IEEE 49th Conf.,https://doi.org/10.1109/ISSN.2088.4541041(2018)).
7. 12. Nalk, S. et al. Automated gland and nuclei segmentation for grading of prostate and breast cancer histopathology.20th IEEE International Symposium on Biomedical Imaging: From Nano to Macro, Proceedings, IEEE 28th–287,https://doi.org/10.1109/ISBI.2020.9349888(2020).
8. 13. Basavanthula, A. et al. Multi-field-of-view framework for distinguishing tumor grade in ER+ breast cancer from entire histopathology slides.IEEE Trans. Biomed. Eng.60, 2089–2099 (2013).
9. 14. Dimitropoulos, K. et al. Automatic invasive breast carcinoma grading using Grassmannian VLAD encoding.PLoS ONE12, e0185110 (2017).
10. 15. Wan, T., Cao, J., Chen, J. & Zhu, Z. Automated grading of breast cancer histopathology using cascaded ensemble with combination of multi-level image features.Neurocomputing229, 34–41 (2017).
11. 16. Li, L. et al. Multi-task deep learning for fine-grained classification and grading in breast cancer histopathological images.Multimed. Tools Appl.79, 14509–14520 (2018).
12. 17. Yan, R. et al. NANet: Neural-aware network for grading of breast cancer in HE-stained pathological images.Proceedings—2020 IEEE International Conference on Bioinformatics and Biomedicine, BIBM 2020865–870,https://doi.org/10.1109/BIBM49491.2020.9313292(2020).
13. 18. Senosaly, Z., Abdelmamek, M. M., Mohamed, M. M. & Gaber, M. M. 3E-net: Entropy-based elastic ensemble of deep convolutional neural networks for grading of breast cancer histopathology.IEEE Access9, 420–429 (2020).
14. 19. Abdull, A., Saouli, R., Dlemek, K. & Yonkura, I. Combined datasets for breast cancer grading based on multi-CNN architectures.2020 IEEE International Conference on Image Processing Theory, Tools, and Applications, IPTA 2020(https://doi.org/10.1109/IPTA.2020.9268653) (2020).
15. 20. Zervos, P. H., Safiye, A. & Bolbasani, H.BCNet: A Deep Convolutional Neural Network for Breast Cancer Grading.https://arxiv.org/arXiv:2010.070507(2021).
16. 21. Koo, J. C. et al. Non-annotated renal histopathological image analysis with deep ensemble learning.Quant. Imaging. Med. Surg.13, 5902–5920 (2023).
17. 22. Yung, M. P. et al. Histopathological gastric cancer detection on GavisHiSD dataset using deep ensemble learning.Diagnostic Med.13, 1793 (2023).
18. 23. McCann, M. T. Tools for automated histology image analysis.Carrie Kimmel University Thesis Report(2015).
19. 24. McCann, M. T., Ordek, J. A., Castro, C. A., Parvin, B. & Koraevski, J.Automated histology analysisOpportunities for signal processing.IEEE Signal Process. J.32, 72–77,https://doi.org/10.1109/SPJ.2013.6722100(2013).
20. 25. Ghaznavi, E. Evans, A., Madabhushi, A. & Feldman, M. Digital image in pathology: Whole-slide imaging and beyond.Annu. Rev. Pathol.8, 120982,https://doi.org/10.1146/annurev.biomed.8.0803.095959(2013).
21. 26. Delle, D. et al. Quantifying the effects of data augmentation and stain color normalization in convolutional neural networks for computational pathology.Medicine in Computer Sci.10, 10344 (2019).
22. 27. Gupta, V., Singh, A., Shukla, R. & Bhavar, A. Automated classification for breast cancer histopathology images: Is stain normalization important?Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)10534LNCS, 160–169 (2017).
23. 28. Kumar, A. et al. Deep feature learning for histopathological image classification of canine mammary tumors and human breast cancer.Int. J. Sci. (IV)508, 406–411 (2020).
24. 29. Hameed, Z., Zahra, S., Garcia-Zapirain, B., Aguirre, J. J. & Vanegas, A. M. Breast cancer histopathology image classification using an ensemble of deep learning models.Sensors20, 4373 (2020).
25. 30. Hameed, Z., Garcia-Zapirain, B., Aguirre, J. J. & Raza-Rugut, M. A. Multiclass classification of breast cancer histopathology images using multi-level features of deep convolutional neural network.Sci. Rep.12, 1–21 (2022).
26. 31. Naray, W., Ahmed, S., Khan, H. & Khan, H. A. Classification of histopathology images Using ALEXNET.Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)10882LNCS, 869–876 (2018).
27. 32. Mantien, C. & Virris, S. Classification of hematoxylin and eosin-stained breast cancer histology microscopy images using transfer learning with EfficientNets.Comput. Intell. Neurosci.2021, 1–17 (2021).
28. 33. Sabri, M., Molinari, E., Archibugi, R., Molinari, R. & Melchiorri, K. M. Impact of stain normalization and patch selection on the performance of convolutional neural networks in histological breast and prostate cancer classification.Comput. Methods Programs Biomed Update1, 100062 (2021).
29. 34. Alkasar, S., Johar, B. A., Abdullah, M. A., Al-Khalidi, J. H. & Chambers, J. A. Going deeper: Magnification-invariant approach for breast cancer classification using histopathological images.IET Comput. Vis.15, 151–164 (2021).
30. 35. Shahadi, J., David, S. M., Al-Mufti, A., Ahmed, N. A. & Maaref, M. A. Histopathology classification using deep learning approaches and histopathology image. A comparison study.IEEE Access8, 187531–187552 (2020).
31. 36. Elhoteb, Rajesh, B. et al. stain specific standardization of whole-slide histopathological images.IEEE Trans. Med. Imaging35, 405–414 (2016).
32. 37. Buntina, P., Hashimoto, R. & Yagi, Y. Color standardization in whole slide imaging using a color calibration slide.J. Pathol. Inform.5, 4 (2014).
33. 38. Vera, M., Pluini, P. J. W., van Dieën, P. J. & Viergever, M. A. Breast cancer histopathology image analysis: A review.IEEE Trans. Biomed. Eng.61, 1400–1411 (2014).
34. 39. Khan, A. M., Rajpoot, N., Treacan, D. & Magee, D. A nonlinear mapping approach to stain normalization in digital histopathology images using image-specific color deconvolution.IEEE Trans. Biomed. Eng.61, 1729–1738 (2014).
35. 40. Reinhard, E., Ashikhmin, I., Shapley, P. C., Troch, D. & Shapley, P. C.Color and illumination invariance(Graph Paper, 21, 34–41 (2001)).
36. 41. Macenko, M. et al. A method for normalizing histology slides for quantitative analysis. InIEEE International Symposium on Image Processing1107–1110 (IEEE, 2009).
37. 42. Valadares, A. et al. Structure-preserving color normalization and sparse stain separation for histological images.IEEE Trans. Med Imaging35, 1962–1971 (2016).

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

18

---

<!-- Page 19 -->

www.nature.com/scientificreports/

43. Zheng, Y. et al. Adaptive color deconvolution for histological WSU normalization. Comput. Methods Programs Biomed. 170, 107–120 (2019).

44. Voelling, R. S., Limmons, J., Winkens, J., Cohen, T. & Welling, M. Rotation Equivariant CNNs for Digital Pathology. arXiv preprint arXiv:1709.11238 (2018).

45. Bejond, B. S., Limmons, J., Winkens, J., Cohen, T. & Welling, M. Rotation Equivariant CNNs for Digital Pathology. arXiv preprint arXiv:1709.11238 (2018).

46. Shaban, M. T., Baur, C., Navuk, N. & Albarqouni, S. StainGAN: Stain style transfer for detection of lymphoid histological images. In 2019 IEEE 16th International Symposium on Biomedical Imaging (ISBI 2019) vol. 2019, April 935–956 (IEEE, 2019).

47. Kang, H. et al. StainNet: A fast and robust stain normalization network. Front. Med. 6, 740307 (2021).

48. Tan, M. & Le, Q. V. et al. Diagnostic assessment of histological WSU normalization. Comput. Methods Programs Biomed. 170, 107–120 (2019).

49. Machine Learning. KCML 2019 vol. 2019 June 10091–10700. International Machine Learning Society (IMLS), 2019.

50. Tan, M. & Le, Q. V. EfficientNet2.0 Smaller Models and Faster Training. 2020.

51. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition 2016, 760–778 (2016).

52. He, K., Zhang, X., Ren, S. & Sun, J. Identity mappings in deep residual learning. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics) 9908, 630–645 (2016).

53. Howard, A. G. et al. MultiNet: Efficient Convolutional Neural Networks for Multi-Task Applications (2017).

54. Sandler, M., Howard, A. G., Zhu, M., Zhongnan, A. & Chen, L. C. MultiNetV2: Inverted residual and linear bottleneck networks. In 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition 4510–4520 (IEEE, 2018). https://doi.org/10.1109/CVPR.2018.00474.

55. Pan, X. et al. Multi-task deep learning for fine-grained classification/grading in breast cancer histopathology images. Stud. Comput. Intell. 85, 85–95 (2019).

56. Yan, R. et al. Neural-guided network for breast cancer grading in HE-stained pathological images. Sensors 22, 4061 (2022).

57. Voon, W. et al. Performance analysis of seven Convolutional Neural Networks (CNNs) with transfer learning for Invasive Ductal Carcinoma (IDC) grading in breast histopathology images. Comput. Methods Programs Biomed. 231, 291–299 (2021).

58. Rufikova, A. C. & Johnston, D. A. Quantification of histochematic staining by color deconvolution. Anal. Quant. Cytol. Histol. 23, 291–299 (2001).

59. Zheng, Y. et al. Stain standardization capsule for application-driven histopathological image normalization. IEEE J. Biomed. Health Inform. 25, 537–547 (2021).

60. Zhou, N., Cai, D., Han, X. & Yao, J. Enhanced color-cisistent generative adversarial network for color normalization of H&E stained images. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics) 11764, 694–704 (2019).

61. Zanjan, G. F., Singer, S. de W. P. H. N., Bejond, B. E. & van der Laak, J. Histopathology stain-color normalization using deep generative models. Medical Imaging with Deep Learning (2018).

62. Lei, J. et al. StainCNet: An Efficient stain feature learning method. Neurocomputing 406, 267–273 (2020).

63. Zhu, J., Yang, T., Sola, P. S., Erfe, A. A. unpaired image-to-image translation using cisistent adversarial networks. Proceedings of the IEEE International Conference on Computer Vision 2017: October 2242–2251 (2017).

64. Spangol, E. A., Oliveira, L. S., Petiteau, C. & Heutte, L. A dataset for breast cancer histopathological image classification. IEEE Trans. Biomed. Eng. 63, 1455–1462 (2016).

65. Bindi, P. et al. From detection of individual metastases to classification of lymph node status at the patient level: The CAMELYON17 challenge. IEEE Trans. Med. Imaging 38, 550–560 (2019).

66. Areña, C. et al. RACEI: A challenge on breast cancer histology images. Med. Image Anal. 56, 121–123 (2019).

67. Salvi, M., Michelloni, N. & Molinari, F. Stain Color Adaptive Normalization (SCAN) algorithm: Separation and standardization of histological stains in digital pathology. Comput. Methods Programs Biomed. 170, 107–120 (2019).

68. Banconi, F. et al. Evaluation of colour pre-processing on patch-based classification of H&E stained images. Eur. Congr. Digit. Pathol. 14, 455–461 (2012).

69. Roy, S., Kumar Jain, A., Lal, S. & Kini, A. A study about colour normalization methods for histopathology images. Microsc. J. 42, 61 (2018).

70. Zlogas, C. et al. Breast carcinoma histological images from the Department of Pathology, ‘Agios Pavlos’ General Hospital Thessaloniki, Greece, Greece. ZENODO https://doi.org/10.5281/ZENODO.834910 (2017).

71. Analytics Vidhya. How to Normalize Images with Imbalanced Class-weights in Python. Analytics Vidhya https://www.analyticsvidhya.com/blog/2020/10/improve-class-imbalance-class-weights/ (2020).

72. Deng, J. et al. ImageNet: A Large-Scale Hierarchical Image Database. 248–255 https://doi.org/10.1109/CVPR.2009.526048 (2010).

73. Rabin, T., Ben-Benayeh, A. & Zelik-Manon, L. ImageNet-218: Pretraining for the ImageNet-218 (2021).

74. Kingma, D. P. & Ba, J. L. A simple, positive semi-convex optimization. In 3rd International Conference on Learning Representations. ICLR 2015 (International Conference on Learning Representations in Computer Vision) 908–916 (2015). https://arxiv.org/abs/1512.05583.

75. Bolshakov, H., Amjadi, E., Tabatabaeian, M. & Jassbi, S. J. A histopathological image dataset for grading breast invasive ductal carcinomas. Inform. Med. Utilization 19, 100341 (2021).

76. Lee, C., Kuo, P. T. F. & Peng, C.-H. H&E stain normalization using U-net. In 2022 IEEE 22nd International Conference on Bioinformatics and Bioengineering (BIBE) 29–32 (IEEE, 2022). https://doi.org/10.1109/BIBE5577.2022.00014.

77. Perez-Puero, P. et al. BiFC: A CNN for H and I band color deconvolution. Applications to stain normalization, data augmentation and cancer classification. Computat. Methods Imaging and Graphics 97, 102048 (2022).

78. Huang, G., Liu, Z., Van Der Maaten, L. & Weinberger, K. Q. Densely connected convolutional networks. In 3rd International Conference on Computer Vision and Pattern Recognition, CVPR 2017 vol. 2017: January 2241–2249. (Institute of Electrical and Electronics Engineers Inc., 2016).

79. Simonyan, K. & Zisserman, A. Very deep convolutional networks for large scale image recognition. In 3rd International Conference on Learning Representations, ICLR 2016. Conference Tracts Proceedings (International Conference on Learning Representations, ICLR 2016). https://doi.org/10.48550/arXiv:1409.1556.

80. Liu, Z. et al. A ComNet for the 2020s. arXiv preprint arXiv:11966-11976 https://doi.org/10.48550/arXiv.2201.03454 (2022).

## Author contributions

In this study, W.V was responsible for conducting a comparative analysis and drafting the main manuscript. Y.C.H designed the methodology, produced the figures, and oversaw the research. Y.K.T, W.S.Y, and H.N provided assistance with result interpretation. H.M validated the findings, while N.G and K.W.L explored the data.

## Funding

The authors would like to gratefully acknowledge the support of Universiti Tunku Abdul Rahman Research Fund (Ref IPSR/RMC/UTARRF/2022-C/1107).

Scientific Reports | (2023) 13:20518 |

[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)

nature portfolio

19

---

<!-- Page 20 -->

www.nature.com/scientificreports/
**Competing interests**

The authors declare no competing interests.

**Additional information**

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1038/s41598-023-46619-6.

Correspondence and requests for materials should be addressed to Y.C.H.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

The image shows the Creative Commons Attribution 4.0 International License logo, which consists of two circular icons: one with the letters 'cc' and another with a person icon.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023

Scientific Reports | (2023) 13:20518 |
[https://doi.org/10.1038/s41598-023-46619-6](https://doi.org/10.1038/s41598-023-46619-6)
nature portfolio
20