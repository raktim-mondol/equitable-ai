

<!-- PAGE 1 -->

# Proceedings of ICSP2018

## Imbalanced Histopathological Breast Cancer Image Classification with Convolutional Neural Network

Md Shammir Reza, Jiwren Ma

Department of Information Science, School of Mathematical Sciences & IAMS

Peking University, Beijing, 100871, P.R. China

Email: shammir@pku.edu.cn, jiwren@math.pku.edu.cn

**Abstract**
—Breast cancer is one of the most common causes of all cancer deaths worldwide and presents a very high mortality rate when compared with the other types of cancer. Early diagnosis can significantly increase the chances of correct treatment and survival, but this process is very tedious, time-consuming and dependent on the experience of the pathologists. The task associated with this work is automatic classification between cancerous and non-cancerous tissue histopathology microscopic images, which would be a valuable computer-aided diagnosis tool for the clinicians. In this work, we conduct experiments on two public dataset one available at 
[http://andrewjanowczyk.com/mayo-TCDC](http://andrewjanowczyk.com/mayo-TCDC)
, regular 
[https://www.kaggle.com/c/camelyon16/data](https://www.kaggle.com/c/camelyon16/data)
 and other is BreakHis available at 
[http://www.inf.ufal.br/andres/breakhis/](http://www.inf.ufal.br/andres/breakhis/)
. Both of these datasets are heavily imbalanced among classes. Existing works in literature shows that Convolutional Neural Network (CNN) today the state-of-the-art approach to solving several complex problems, including medical image analysis, and in particular on histopathology image classification. However, class-imbalanced data is generally put to the side when it comes to the performance of CNN during the parameter learning. In order to overcome the class imbalanced problem, we utilize different over-sampling and under-sampling techniques. The imbalanced training data such that the performances of the CNN based classifiers can be improved to those of the class balanced dataset. Extensive experiments demonstrate that synthetic over-sampling can be an effective way to counter the impact of class imbalance of training data.

**I. INTRODUCTION**

Breast cancer is still one of the top leading causes of death and common cancer among women worldwide, which is ranked the second place following lung cancer. A recent survey about cancer mortality in recent years [1] Among the breast cancer subtypes, invasive ductal carcinoma (IDC) is the most common type of breast cancer and accounts for about 70–80% of all breast cancer diagnoses [2]. In every year, more than 180,000 women in the United States find out they have invasive breast cancer. Invasive breast cancer is the most prevalent type of cancer and early diagnosis and its treatment highly improves the chances of survival [4].

Diagnosing breast cancer usually involves a combination of procedures, including a physical examination and imaging tests such as digital Mammogram (X-ray). Magnetic resonance imaging (MRI), Ultrasound, and biopsy [5]. Biopsy is the only diagnostic procedure with confidence if cancer presents a suspected region. The procedure involves in collecting and extraction samples of cells from a suspicious microscopic examination. The final diagnosis, including grading and staging, is done by pathologists applying visual inspection of histological samples under microscope (Hematoxylin-Eosin (H&E) stain inspection. During this procedure, relevant regions of whole slide tissue scans and inspection of overall tissue architecture and variability for assessment of disease aggressiveness [6]. However, the manual diagnosis process is very tedious and subjective, causing inter-observer variations even among the same pathologist [7], [8]. Computer-aided diagnosis (CAD) systems based on machine learning platform are developing to help physician during the diagnosis procedure and reduce the workload of clinicians [9], [12], [14], [15]. Automated analysis of cancer is an ongoing topic of research and Deep learning (DL) based approaches were shown to outperform conventional machine learning methods in many image analysis task [11], [16]. More recently, Andrew Janowczyk et al. [17] presented a largest comprehensive study of DL approaches and valuable a unifying tool of seven unique histopathological task and in many cases, superior to results from the state-of-the-art hand-crafted feature-based classification approaches.

In the domain of medical imaging, deep learning has been successfully used for cancer segmentation, mitosis detection, lymphoma classification, and other problems. The development of deep learning model poses a significant challenge here the dataset is imbalanced, noisy, distribution and encountered a serious difficulty in most classifier learning algorithms. Specifically, the medical domain has received interest from researchers in recent years [13], [21], [27]. Although some methods [25], [26] are known to perform well in machine learning algorithms but there is no systematic research available on the effects of imbalanced data on CNN with addresses histopathological datasets. In the light of this, we adopt some sampling and synthetic based data augmentation approach to investigate the effect of imbalance on CNN classification. The experimental evaluation shows that imbalance class data lead to a negative impact on overall CNN performance and generalize poor results, compared to CNN trained with balanced data.

The rest of this paper is organized as follows: Section 2 describes dataset and gives a review of methods to address the problem of class imbalance, Section 3 we describe the CNN architecture and evaluation protocol. Section 4 present the results from our experiments and compare methods. The final section gives the conclusion.

978-1-5386-4673-1/18/$25.00 ©2018 IEEE

619

<!-- PAGE 2 -->

Fig. 1. Bar diagram of class label: (a). IDC cancer dataset; (b). BreakHis dataset.

## II. DATA AND METHODS

To evaluate the performance of CNN on histopathological imbalanced data, two datasets that include invasive ductal carcinoma cancer data and BreakHis. The details about the two datasets are as follows:

**A. Dataset Description-1 (IDC vs Non-IDC)**

The original dataset [16] consisted of 162 whole mount slide images of breast cancer specimens scanned at 40x. The recent release of the dataset publicly available at patch wise consists of 277,524 RGB digital image patches of size 50 × 50 [19]. Each patch’s file name is of the format: a_xX_yY_classC.png for example 13462_d455_d2251_y1951_class0.png. Where u is the patient ID (13462_id55), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-IDC and 1 is IDC. In Fig. (a), shows these dataset is heavily imbalanced, i.e. classes of data are not equally represented. In this data, the negative class image (71.61%), 198,738 IDC (negative) is represented about 3 times as much positive class (28.39%, 78,786 IDC positive). The goal is to classify of IDC and healthy tissues image.

**B. Dataset-2 (BreakHis)**

BreakHis [10] is a challenging large scale dataset including 7909 images and eight sub classes of breast cancer. The source of the data comes from 82 anonymous patients of Pathological Anatomy and Cytopathology (P&D) lab, Brazil. BreakHis is divided into benign and malignant tumors that consists of four magnification factors: 40x, 100x, 200x, and 400x. Particularly, both breast cancer tumors, benign and malignant, can be stored into different types of pathologists based on the aspect of tumor cells under microscopes. Image are of three channel RGB, eight bit depth in each channel, and 700 × 460 size. These dataset is also heavily class imbalanced, where the malignant class image were extracted 68.64% and benign class has 29.36% images. In this data set, the positive class is represented 2 times as much as negative class. The goal is to a binary classification of benign and malignant tumors image.

In Fig. 1, shows two interesting imbalanced histopathological database, one has negative class is about 3 times as well positive class and other (BreakHis) has positive class extracted two times than negative class. Dealing with these two contrary imbalanced data are still a challenging task in most of machine learning algorithms and CNN, because of most machine learning algorithms require a balanced distribution or the same distribution of classes for training. The predictive capability of classification algorithms is affected by class imbalance. Intuitively, since there are a large number of majority class examples, a classification model can achieve high classification accuracy even when it does not predict a single minority class instance correctly. The problem of class imbalance is a main reason.

**C. Dealing with Imbalanced Class**

Learning from class-imbalanced data continues to be a common problem in supervised learning and poses a significant challenge for the training of a deep learning model. Most of the standard classification algorithms are designed to handle balanced class distributions. However, in many real-world applications, imbalance data set is common in many practical applications such as applications include fraud detection in banking, rare medical diagnoses, and oil spill recognition in satellite images. Moreover, in the medical applications, the correct classification for the minority class samples is more valuable than for the majority class samples. For example, in a binary classification within the medical domain, if we are interesting to classify patients condition, the diagnosis of cancer of a patient, a minority class is more interest than the majority class of cancer free patients.

Many techniques have been proposed to mitigate the bias towards the plentiful class in the problem of class imbalance. Techniques aimed at improving classification in the presence of class imbalance, the machine learning community has addressed the issue of class imbalance in two ways: sampling based approaches [24] and cost function based approaches [23]. Sampling based can be divided into three broad categories: a) over sampling (b) under sampling c) hybrid of over-sampling and under-sampling.

<!-- PAGE 3 -->

Fig. 2. The Synthetic image creates by SMOTE. On the right bottom corner last two images are synthetic.

In under-sampling, resample the data by removing cases of the majority classes until the minority class becomes some specified percentage of the majority class. Moreover, the more imbalanced the dataset the more samples will be discarded when undersampling, therefore such methods risk the loss of important concepts and throwing away potentially useful information. Oversampling, on the other hand, may encourage overfitting when observations are merely duplicated. This technique is followed in overfitting which occurs when exact replicas of minority instances are added to the main dataset. This problem can be avoided by adding genuinely new samples to alleviate the problem of random undersampling and oversampling, there are some hybrid algorithm developed regarding as synthetic examples are generated from the minority class rather than replication of instances. These synthetic instances are then added to the original dataset by operating in the feature space rather than the data space. The new dataset has no loss of useful information and used as a sample to train the classification models. Some popular of such algorithms are Synthetic Minority Over-sampling Technique (SMOTE) [25], adaptive synthetic (ADASYN) [26] etc. However, SMOTE is still very popular due to its simplicity that was proposed to improve random over-sampling. In SMOTE, there are three steps involve to generate a synthetic sample:

- Firstly, it chooses a random minority observation a.
- Among its k nearest minority class neighbors, instance b is selected.
- Finally, a new sample x is created by randomly interpolating the two samples: i.e. x=a+(b-a)*rand(0,1). rand(0,1) generates a random number between 0 and 1.

In “Fig. 2”, showed SMOTE creates two new IDC positive images from displayed 0 original images of IDC and non-IDC. The synthetic two positive image has generated rather than replication of original data. In this study, we investigate different over-sampling and a under-sampling technique to handle class imbalanced problem of both dataset, and comparing their performance using CNNs architecture.

| Layer | Num Kernels | Kernel Size | Activation |
| --- | --- | --- | --- |
| Input |  |  |  |
| Convolution2D | 32 | 3 x 3 | ReLU |
| Convolution2D | 64 | 3 x 3 | ReLU |
| MaxPooling2D |  | 2 x 2 |  |
| Fully Connected | 128 |  | Dropout (0.25) |
| Fully Connected | 2 |  | Dropout (0.5) + ReLU |
| SoftMax |  |  |  |

### III. CLASSIFICATION BY CNN

This section describes experiments are showing the effectiveness of CNN image classification performance due to imbalanced distribution in training data. A CNN consists of a multiple trainable stages stacked on top of each other, followed by a supervised classifier and sets of arrays named feature maps represent both input and output of each stage. A deep net is trained by feeding it input and letting it compute layer by layer to generate the final output for comparison with correct answer.

#### A. Network Architecture

To conduct experiment by CNN, one of the popular deep learning framework Keras has been used with the TensorFlow backend. Keras is a model-level library, providing high-level building blocks for developing deep learning models, which is very fast and simple to use. The network used in the experiments was keras-team of Francois Chollet’s setups for mnist digit classification [30]. They are commonly used network setups where a simple and straightforward setup is required. The network had 3 convolutional layer, 8 output nodes, 8 epochs and 128 batch size. In our experiment, we will use 20 epochs for better classification performance. In “Table I”, describes summary of the CNN architecture.

<!-- PAGE 4 -->

TABLE II
CNN PERFORMANCES ON INSALVINE DUCTAL CARCINOMA DATASET

| Sampling Method | Sensitivity | Specificity | F-score | Accuracy | BAC |
| --- | --- | --- | --- | --- | --- |
| Imbalanced data | 0.7141 | 0.9098 | 0.7359 | 0.8540 | 0.8119 |
| Under-sampling | 0.8789 | 0.7336 | 0.8194 | 0.8062 | 0.8063 |
| Over-sampling (WR) | 0.8435 | 0.8454 | 0.8443 | 0.8444 | 0.8449 |
| ADASYN | 0.8297 | 0.8510 | 0.8402 | 0.8402 | 0.8405 |
| SMOTE | 0.8085 | 0.9012 | 0.8748 | 0.8548 | 0.8548 |

The network consists of two Convolution2D layers and a MaxPooling2D layer following after the second convolution. To regularise model, a dropout layer was applied after pooling layer, and after the first Dense layer. Afterwards, the output of the second pooling layer is flattened to 1D (via the Flatten layer), and passed through two fully connected (Dense) layers. ReLU activations will once again be used for all layers except the output dense layer, which will be used as a softmax activation. The remainder of the model specification, the cross-entropy loss function as the objective function, and Adam as the optimiser for gradient descent. In addition, the model includes ImageDataGenerator API in Keras for generating existing training images and create some altered versions of the same image. This provides more images to train on, but can also help expose our classifier to a wider variety of lighting and coloring situations so as to make our classifier more robust.

### B. Experimental Set-up and Evaluation Protocol

In the experimental set-up CNN on invasive ductal carcinoma dataset, the patch-based dataset randomly divided into 70% training, and 30% validation set, and classification performances evaluated over testing dataset.

On BreakHis data, the database is composed of 7909 700×700 pixel images captured from four magnification factor 40×, 100×, 200×, and 400×. Generally, convolutional neural network models for larger images can result in more complex architecture, with large set of parameters can substantially increase the complexity of the model. In this work the original 700 × 400 images were reduced to 224 × 224, and merging all the magnifications factor (40×, 100×, 200×, and 400×) to generate a comprehensive, indexed and available dataset for CNN training. The dataset has been randomly divided into a 70% training, 30% testing set and we evaluated classification rate at the image level, not considering the patient level.

To evaluate the performances of CNN in medical image dataset, there are several computing methods to access the results [10], [16]. By using their evaluation metrics, we report the performance measures are sensitivity (true positive rate), specificity (true negative rate), F-measure and balanced accuracy (BAC). According to [16], BAC is defined as:

BAC = \frac{\text{sensitivity} + \text{specificity}}{2} \quad (1)

In medical imaging, F-score and balance accuracy play key role to robustify the model performances. For BreakHis data classification, accuracy represents the image level recognition on testing dataset.

### IV. RESULTS DISCUSSION

The impact of class imbalance on CNN classification performance are shown in “Table II”, “Table III” and “Fig. 5”. The results show that the imbalanced data has a negative impact on the performance of CNN. Both tables indicate that the oversampling techniques consistently produced the best results, in terms of classification performances index. For both dataset, the difference between sensitivity and specificity of imbalanced data is very high compared to balanced data. By under-sampling, we have solved the class imbalance issue and increased the sensitivity but drop the value of specificity. F-score and recognition rate. A proper reason could be decided that we trained our classifiers using few samples. Since our datasets are heavily imbalanced resulting more samples is discarded when undersampling, therefore throwing away potentially useful information. In “Table II”, the IDC and healthy tissue classification results show that all oversampling approach can improve the balanced accuracy up to 3.4% than imbalanced data. The sensitivity of imbalance data indicates that 4.5% capable of correctly diagnosis positive cancer cases among those having the cancer disease, and 90.98% confidence to classify cancer free cases those without the cancer diseases. Whereas in “Table II”, all of oversampling CNN framework provided better sensitivity, specificity, F-score, accuracy and balanced accuracy, and showed slightly better results in terms of F-measure and BAC (84.78%, 85.48%) compared to two best previous results using the same dataset (71.8%, 84.23%) [16], and (76.48%, 84.68%) [17]. However, our obtained results are not straight comparable to state-of-art approaches due to publicly unavailable the ground truth of the data. The state-of-the-art approaches focused the detection of IDC and the IDC region in whole-slide images, whereas we are considering the classification of image patches into 2 classes, opposite to the segmentation problem considered in [16] and [17].

Analysis of BreakHis benchmark data to binary classification (benign vs. malignant), the experimental result is presented in “Table III”. It is apparent that CNN with a balanced dataset leads to better classification performances compared

<!-- PAGE 5 -->

Fig. 3. BreakHis data. (a) The sketches of datasets is imbalanced. From (b-d) The sketch of dataset are under-sampling, over-sampling with replacement (WR) and SMOTE respectively.

| Sampling Method | Sensitivity | Specificity | F-score | Accuracy | BAC |
| --- | --- | --- | --- | --- | --- |
| Imbalanced data | 0.9005 | 0.7396 | 0.8917 | 0.8501 | 0.8201 |
| Under-Sampling | 0.7252 | 0.8667 | 0.7804 | 0.7959 | 0.7960 |
| Over-Sampling (WR) | 0.8223 | 0.9127 | 0.8615 | 0.8613 | 0.8675 |
| ADASYN | 0.7753 | 0.8462 | 0.8000 | 0.8137 | 0.8122 |
| SMOTE | 0.9090 | 0.8034 | 0.8634 | 0.8562 | 0.8562 |

to CNN trained with imbalanced data. These reported values indicate that the effect of improving the value for sensitivity, specificity, F-values and accuracy of the minority class due to balanced of the minority class examples. In “Fig. 3(a)”, on the learning curve we can observe the accuracy of the network memorized perfectly the training set (very high accuracy on training) which leads to poor generalization (low accuracy on the test), i.e. CNN model attacked by over-fitting problem on imbalanced data.

The accuracy is evaluated on integrated zoom level and considering image-level accuracy metric. The best recognition rate at image level is obtained from over-sampling with replacement approach (86.13%), while CNN performances on imbalanced data is 85.01%.

These reported accuracy and F-score values based on over-sampling with replacement and SMOTE outperforms the CNN trained with 100%: 200%: 400%: magnification at the image level reported in [1].

### V. CONCLUSION

In this study, we have examined the impact of class imbalance on classification performance of convolutional neural networks and investigated the effectiveness of different methods of addressing the issue. The effect of class imbalance on classification performance is detrimental. Regarding performance of different methods for addressing the imbalance issue, in almost all the situations oversampling emerged as the best method and increased the CNN performances substantially. For both of the dataset, the results confirm that oversampling approach performs consistently better than undersampling approach across all scenarios. It is concluded that oversampling methods, especially synthetic based oversampling is a durable way to counter the impact of class imbalance of histopathological image classification with CNN. However, these experiments need to be repeated with other datasets for confirmation, and further research also can be extended based on cost sensitive learning of deep neural network.

<!-- PAGE 6 -->

ACKNOWLEDGMENT

This work was supported by the Natural Science Foundation of China for Grant 61711138. The author would like to thank to Andrew Janowczyk and Fabio Alexandre Spanhol for providing the databases.

REFERENCES

[1] B. W. Stewart, and C. Wild, "World cancer report 2014: international agency for research on cancer," World Health Organization 503, 2014.

[2] American Cancer Society, "Breast Cancer Facts & Figures 2017-2018," Atlanta: American Cancer Society, Inc. 2017.

[3] American Cancer Society, "Breast Cancer Facts & Figures 2017-2018," Atlanta: American Cancer Society, Inc. 2017.

[4] J. Ferlay et al., "GLOBOCAN 2012 v1.0, cancer incidence and mortality worldwide: IARC Cancer Base no. 11, 2013."

[5] J. E. Joy, E. E. Pneher, and D. B. Pettitt, Eds., "Saving women's lives: strategies for improving breast cancer detection and diagnosis," Washington, D.C.: National Academies Press, 2009.

[6] C. Elron and E. Ellis, "Pathological prognostic factors in breast cancer: i. the value of histological grade in breast cancer: experience from a large study with long-term follow-up," 
*Br J Cancer*
, 19(5), 403-410 (1991).

[7] J. G. Elmore et al., "Diagnostic concordance among pathologists interpreting breast biopsy specimens," 
*JAMA*
, Jan. 13 (11), 1122-1125, 2015.

[8] S. M. Meyer et al., "Breast carcinoma malignancy grading by bloom-richardson system vs proliferation index: reproducibility of grade and advantages of proliferative index," 
*Mol Cancer*
, 18(8), 1067, 2009.

[9] S. Robertson, H. Aizpurua, K. Smith, J. Harman, "Digital image analysis in breast pathology—from image processing techniques to artificial intelligence," 
*Biomedical Engineering*
, 2017.

[10] F. Spanhol, L.S. Oliveira, C. Petitjean, and L. Heutte, "A dataset for breast cancer histopathology image classification," 
*IEEE Transactions on Biomedical Engineering (TBMEL)*
, vol. 63, pp. 1455-1462, 2015.

[11] F. Spanhol, L. S. Oliveira, C. Petitjean, and L. Heutte, "Breast cancer histopathological image classification using convolutional neural network," International Joint conference on Neural Network (IJCNN), IEEE, July, 2560-2567, 2016.

[12] P. Filipczuk, T. Fornaciari, A. Koryczka, and R. Moczkal, "Computer-aided breast cancer diagnosis based on the analysis of cytological images of fine needle biopsies," 
*IEEE Transactions on Medical Imaging*
, vol. 32, no. 12, pp. 2169-2178, 2013.

[13] M. N. Brown, C. Pading, B. Stephen, and J. C. Owen, "The problem of bias in training data in regression problems in medical decision support," 
*Artificial intelligence in medicine*
, vol. 34, no. 1, pp. 51-70, 2002.

[14] M. Kowal et al., "Computer-aided diagnosis of breast cancer based on fine needle biopsy microscopic images," 
*Computers in Biology and Medicine*
, vol. 43, no. 10, pp. 1562-1572, 2013.

[15] K. C. Wong et al., "Pattern of Imbalanced Data: A Review," 
*International Journal of Pattern Recognition and Artificial Intelligence*
, vol. 23, no. 4, pp. 687-702, 2009.

[16] C. Cui-ke, A. Buzsáky, F. González, H. Gilmore, M. Foldman, S. Gámez et al., "Automatic detection of invasive ductal carcinoma in whole slide images with convolutional neural networks," 
*SPIE Medical Imaging*
, Vol. 9641, pp. 96410D-96410D-15, 2016.

[17] A. Janowczyk, A. Madabhushi, "Data Mining for Digital Pathology Image Analysis: A Comprehensive Tutorial with Selected Use Cases," 
*Journal of Pathology Informatics*
, 7-29, 2016.

[18] M. Veta et al., "Breast cancer histopathology image analysis: a review," 
*IEEE Transactions on Biomedical Engineering*
, vol. 61, no. 5, pp. 1400-1411, 2014.

[19] A. Janowczyk, Available: 
[http://indriya.jax.wisc.edu/~campbell/DIC/Brain/Brain2005/Brain2005.zip](http://indriya.jax.wisc.edu/~campbell/DIC/Brain/Brain2005/Brain2005.zip)
, Last accessed on 2018 May 20.

[20] F. Pneher, "Machine Learning from Imbalanced Data Sets 107," 
*Insited*
, 2008.

[21] A. Wong, S. Chan, and C. J. Harris, "A Kernel-Based Two-Class Classifier for Imbalanced Data Sets," 
*IEEE Transactions on Neural Networks*
, vol. 18, no. 1, pp. 28-41, 2007.

[22] M. Kubat, R. C. Holte, and S. Matwin, "Machine Learning for the Detection of Oil Spills in Satellite Radar Images," 
*Machine Learning*
, 30(2), 195-215, 1998.

[23] M. Pezzei, C. Meier, P. Murphy, K. Ali, D. Hame, C. Brust, "Reducing Misclassifications Costs," In 
*Proceedings of the Eleventh International Conference on Machine Learning San Francisco, CA, Morgan Kaufmann, 1993*
.

[24] N. Japkowicz, "The Class Imbalance Problem: Significance and Strategies," 
*Proceedings of International Conference on Artificial Intelligence, IC-AI, 2000*
.

[25] N. V. Chawla, L. O. Hall, K. W. Bowyer, and W. P. Kegelmeyer, "SMOTE: Synthetic Minority Over-sampling Technique," 
*Journal of Artificial Intelligence Research*
, vol. 16, pp. 321-357, 2002.

[26] H. Hsiao, B. Yang, A. Edwards, and L. Shuang, "ADASYN: Adaptive Synthetic Sampling Approach for Imbalanced Learning," 
*International Joint Conference on Neural Networks (IJCNN)*
, 1-12, 2133-2138, 2008.

[27] H. Hsiao and A. B. Garcia, "Learning from Imbalanced Data," In 
*IEEE Conference on Knowledge and Data Engineering 21.19, pp. 1260-1284, 2009*
.

[28] P. Chalde, A. Ulan, and T. Brüstner, "Using Random Forest to Learn Imbalanced Data," 
*Techn. rep. Department of Statistics, University of Bielefeld, 2004*
.

[29] V. Söbös and O. Zencz, "Classification on Data with Biased Class Distributions," 
*Learning from Imbalanced Data: Springer Berlin Heidelberg*
, Vol. 2167, pp. 527-538, 2001.

[30] P. Chalde, M. Matyssewicz, S. Mandy, "Dataset: Tumors, Tumors, Tumors, <a href="ftp://ftp.cs.cmu.edu/∼kumar/bobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstobstob