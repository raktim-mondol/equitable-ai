<!-- Page 1 -->

arXiv:2409.11664v1 [cs.CV] 18 Sep 2024

# Agent Aggregator with Mask Denoise Mechanism for Histopathology Whole Slide Image Analysis

Xitong Ling*Tsinghua UniversityShenzhen, Chinalingxt23@mails.tsinghua.edu.cn

Minxi Ouyang*Tsinghua UniversityShenzhen, Chinaoymx23@mails.tsinghua.edu.cn

Yizhi WangTsinghua UniversityShenzhen, Chinayz-wang22@mails.tsinghua.edu.cn

Xinrui ChenTsinghua UniversityShenzhen, Chinacrr22@mails.tsinghua.edu.cn

Renao YanTsinghua UniversityShenzhen, Chinayra21@mails.tsinghua.edu.cn

Hongbo ChuTsinghua UniversityShenzhen, Chinazhu-hb23@mails.tsinghua.edu.cn

Junru ChengResearch Institute of TsinghuaShenzhen, Chinacheng_jr@foxmail.com

Tian GuanTsinghua UniversityShenzhen, Chinaguanlian@sz.tsinghua.edu.cn

Sufang TianWuhan UniversityWuhan, Chinasftian@whu.edu.cn

Xiaoping Liu†Wuhan UniversityWuhan, Chinaliuxiaoping@whu.edu.cn

Yonghong He†Tsinghua UniversityShenzhen, Chinaheyh@sz.tsinghua.edu.cn

## ABSTRACT

Histopathology analysis is the gold standard for medical diagnosis. Accurate classification of whole slide images (WSIs) and region-of-interests (ROIs) localization can assist pathologists in diagnosis. The gigapixel resolution of WSI and the absence of fine-grained annotations make direct classification and analysis challenging. In weakly supervised learning, multiple instance learning (MIL) presents a promising approach for WSI classification. The prevailing strategy is to use attention mechanisms to measure instance importance for classification. However, attention mechanisms fail to capture inter-instance information, and self-attention causes quadratic computational complexity. To address these challenges, we propose AMD-MIL, an agent aggregator with a mask denoise mechanism. The agent token acts as an intermediate variable between the query and key for computing instance importance. Mask and denoising matrices, mapped from agents-aggregated value, dynamically mask low-contribution representations and eliminate noise. AMD-MIL achieves better attention allocation by adjusting feature representations, capturing micro-metastases in cancer, and

improving interpretability. Extensive experiments on CAMELYON-16, CAMELION-17, TCGA-KIDNEY, and TCGA-LUNG show AMD-MIL’s superiority over state-of-the-art methods.

## CCS CONCEPTS

- • Computing methodologies → Computer vision tasks.

## KEYWORDS

histopathology diagnosis, multiple instance learning, agent attention, mask denoise mechanism

### ACM Reference Format:

Xitong Ling, Minxi Ouyang, Yizhi Wang, Xinrui Chen, Renao Yan, Hongbo Chu, Juan Cheng, Tian Guan, Sufang Tian, Xiaoping Liu, and Yonghong He. 2024. Agent Aggregator with Mask Denoise Mechanism for Histopathology Whole Slide Image Analysis. In Proceedings of the 32nd ACM International Conference on Multimedia (MM ’24), October 28–November 1, 2024, Melbourne, VIC, Australia/Proceedings of the 32nd ACM International Conference on Multimedia (MM ’24), October 28–November 1, 2024, Melbourne, Australia. ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/366467.3681435

*Both authors contributed equally to this research.

†Corresponding authors.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and a fee. Request permission from permissions@tsinghua.edu.cn.MM ’24, October 28–November 1, 2024, Melbourne, VIC, Australia© 2024 Copyright held by the owner author(s). Publication rights reserved to ACM.ACM ISBN 978-98-4007-6686-8/24/10https://doi.org/10.1145/366467.3681435

## 1 INTRODUCTION

The advancement of deep learning technologies and increased computational capacity have significantly enhanced the field of computational pathology [2, 12, 16, 23]. This progress assists physicians in diagnosis and standardizes pathological diagnostics [7, 20]. However, analyzing histopathology whole slide images (WSIs) significantly differs from typical computer vision tasks [19]. A single WSI, with its gigapixel resolution, makes obtaining pixel-level annotations impractical, in contrast to natural images [6]. The Multiple Instance Learning (MIL) method is currently the mainstream framework for analyzing histopathology slides using only

---

<!-- Page 2 -->

MM '24, October 28–November 1, 2024, Melbourne, VIC, Australia

Xiong Ling et al.

Figure 1: Comparison of core modules: (a) pooling agents, (b) proposed trainable agents, (c) self-attention mechanism, (d) proposed agent aggregator with mask denoise mechanism. Mask and denoising are learnable matrices.

WSI-level annotations [18, 24, 31]. MIL methods consider the entire WSI as a bag, with each patch within it as an instance [4, 29]. If any instance within the WSI is classified as cancerous, then the entire WSI is labeled as such [3, 28]. The WSI is labeled as normal only if all instances within it are normal.

Current MIL methods have two stages: segmenting the WSI into patches and using a pre-trained feature extractor to embed features. These features are then aggregated using methods such as mean-pooling, max-pooling, ABMIL [11], DSMIL [13], and TransMIL [21], and then mapped for classification.

ABMIL [14] and DSMIL [13] use lightweight attention mechanisms for information aggregation. However, they overlook relationships between instances, hindering global modeling and capturing long-distance dependencies. TransMIL introduces self-attention [27] within MIL’s aggregator. Self-attention calculates relations between any two patches in a WSI, capturing long-distance dependencies. It also dynamically allocates weights based on input importance, enhancing the model’s ability to process complex data. However, the quadratic complexity of self-attention challenges its application in MIL aggregators. TransMIL uses Nystrom [33] Self-attention in Nystrom Self-attention selects a subset of elements, known as landmarks, to approximate attention scores. Nystrom Self-attention down-samples query and key vectors locally along the instance down dimension. This approach has two main issues: sampling based on adjacent instances can dilute significant instance contributions, and the variance in instance sizes across bags requires padding during down-sampling. This can lead to aggregation imbalances and unstable outcomes.

Moreover, the quadratic complexity issue of self-attention, TransMIL [21] employs Nystrom attention [33] as the substitute for the standard self-attention module. Nystrom attention selects a subset of sequence elements, also known as landmarks, to approximate the attention scores for the entire sequence. Specifically, in the

Nystrom attention mechanism, the local down-sampling of query and key matrices is implemented along the dimension of the instance tokens. This approach has two significant issues. Firstly, since the sampling process relies on adjacent instances, many insignificant ones might dilute the impact of significant instances. Secondly, equidistant division is not always the optimal query strategy, as the distribution of information in a sequence may be uneven. Fixed sampling intervals might fail to capture all crucial information points, leading to a decrease in approximation quality. Thus, these challenges limit the effectiveness of the pooling agent in trainable matrices for effective mapping. Furthermore, to indirectly achieve a more rational distribution of attention scores through adjustments in instance representations, we introduce the mask denoise mechanism for information aggregation.

Agent attention [9] introduces the agent tokens in addition to query, key, and value tokens. Agent tokens act as the agent for the query tokens, aggregating information from the key and value tokens. Although these challenges are inherent to the query token in a broadcasting mechanism. Given the lesser number of agent tokens compared to sequence tokens, the agent mechanism can reduce the computational load of standard self-attention. However, agent tokens are obtained through mean pooling of the query tokens in standard agent attention, making it challenging to adapt to the variable-length token inputs of pathological multiple instance tasks. Additionally, mean pooling, by aggregating features through local averaging, may result in missing important information. Consequently, we adjust the number of agent tokens as a hyperparameter and substitute the mean pooling agent tokens with trainable agent tokens.

Moreover, we introduce the mask denoise mechanism to dynamically refine attention scores by adjusting instance representations. Mask and denoising matrices, matching the agent’s aggregated value dimension, are generated by projecting this value through a linear layer. Mask and denoising matrices are binary matrices of threshold filtering, not directly from the value token but their high-level mapping, allowing dynamic adaptation to the input. Then, the mask directly multiplies with the value, filtering out non-significant representations. However, as the mask applies binary filtering to the value, it might suppress unimportant instances excessively, thereby introducing relative noise. Therefore, we introduce the denoising matrices from the agent-aggregated values to correct the relative noise. We conducted extensive comparative experiments and ablation studies on four datasets to verify the effectiveness of the trainable agent aggregator and mask denoise mechanism.

## 2 RELATED WORK

### 2.1 Multiple Instance Learning for WSI Analysis

MIL focuses on demonstrate significant potential in classifying and analyzing histopathology images. In this framework, a WSI is treated as a bag, and its local regions are instances. MIL paradigms are categorized into three types: instance-based, embedding-based, and bag-based methods. The instance-based method scores each instance and then aggregates these scores to predict the bag’s label.

The embedding-based method employs a pre-trained feature encoder to generate instance representations, which are then aggregated to demonstrate significant potential with Deep Neural

---

<!-- Page 3 -->

Agent Aggregator with Mask Denoise Mechanism for Histopathology Whole Slide Image Analysis

MM '24, October 26–November 1, 2024, Melbourne, VIC, Australia

Figure 2: Overall process: (a) the preprocessing of WSI, (b) overall framework of AMD-MIL, (c) proposed mask denoise mechanism.

Networks (DNN) but reduces the interpretability. Bag-based approaches classify by comparing distances between bags, with the main challenge being identifying a universal distance metric. Current MIL advancements focus on developing specialized feature encoders, enhancing aggregators, data augmentations, and improving training strategies.

Feature encoders pre-trained on natural images often struggle to extract high-level histopathology features, such as specific textures and morphological structures. Transpath [30] trains A hybrid architecture of CNN and a win-transformer feature encoder on one hundred thousand WSI, using a semantically relevant contrastive learning approach. IBMI [15] also utilizes a feature encoder pre-trained on nine pathological datasets through a self-supervised method with MOCOv3 [32]. Representations generated by these pathology-specific feature extractors significantly outperform those obtained from feature encoders pre-trained on ImageNet [5] in downstream tasks.

The most common aggregation strategies for instance-based and embedding-based methods include pooling and attention mechanisms. Mean-MIL and Max-MIL aggregate representations and categorize through the average and maximum values respectively, but fixed aggregation mechanisms cannot adapt to varying inputs. In contrast, AIMIL employs attention mechanisms to aggregate features through trainable weights. Similarly, CLAM uses gated attention and a top-k selection strategy for bag label prediction. TransMIL, on the other hand, applies a linear approximation of self-attention to explore relationships between instances. WIKO [14] introduces a knowledge-aware attention mechanism, enhancing the

capture of relative positional information among instances. HAT-Net+ [1] advances cell graph classification by leveraging a unique, parameter-free strategy to dynamically merge multiple hierarchical representations, effectively capturing the complex relationships and dependencies within cell graphs.

To enhance performance and stability, various methods employ data augmentation. For example, DTFD [35] increases the number of bags using a partitioning pseudo-bag split strategy and uses the double-tier MIL framework to use the intrinsic features.

In terms of training strategies, IBMI [15] uses interventional training to reduce contextual prior. SSI-MIL [34] leverages semantic similarity knowledge distillation to exploit latent bag information. MHM-MIL [25] addresses key instances with hard example mining. LNPI-MIL [22] proposes the training strategy of learning from noise pseudo labels, which can address the problem of semantic misalignment between instances and the bag.

## 2.2 Approximate Self-Attention Mechanism

The self-attention [27] mechanism is capable of grasping dependencies over long sequences, enabling comprehensive modeling, but its quadratic complexity limits the increase in input sequence length. Consequently, research on approximate self-attention mechanisms aims to reduce the complexity to linear while maintaining global modeling capability.

Nyström attention [33] uses the Nyström method to estimate eigenvalues of eigenvectors, approximating self-attention [27] by selecting a few landmarks, reducing computational and storage needs. Focused Linear attention [8] uses nonlinear reweighting to

---

<!-- Page 4 -->

MM '24, October 28–November 1, 2024, Melbourne, VIC, Australia

Xitong Ling et al.

focus on important features. Agent attention [9] introduces agents representing key information, significantly lowering computational complexity by computing attention only among these agents.

These advancements in approximate attention mechanisms provide a new perspective for enhancing aggregators in MIL methods.

### 3 METHODOLOGY

#### 3.1 MIL and Feature extraction

In the MIL methodology, each WSI is conceptualized as a labeled bag, wherein its constituent patches are considered as instances possessing indeterminate labels. Taking binary classification of WSIs as an example, the input WSI X is divided into numerous patches \{(x_1, y_1), \dots, (x_N, y_N)\}, encompassing N instances of x_i. Under the MIL paradigm, the correlation between the bag's label, Y, and the labels of instances y_i is established as follows:

Y = 1, \text{ if } \sum_i y_i > 0, \quad (1)

Given the undisclosed nature of the labels for the instances y_i, the objective is to develop a classifier, \mathcal{M}(X), tasked with estimating \hat{Y}. In alignment with methodologies prevalent in contemporary research, the classifier can be delineated into three steps: feature extraction, feature aggregation, and bag classification. These processes can be defined as follows:

\hat{Y} \leftarrow \mathcal{M}(X) = h(\text{gf}(X)), \quad (2)

where f_g and h represent the feature extractor, feature aggregator, and the MIL classifier.

The feature aggregator is considered to be the most important part of summarizing features, which can aggregate features of different patches. The attention mechanisms can discern the importance of patches in a WSI and it is widely used in the feature aggregator. Attention-based and self-attention-based MIL are the main methods currently used.

In the attention-based MIL [35], the feature aggregator can be defined as:

G = \sum_{i=1}^N a_i h_i = \sum_{i=1}^N f_i(x_i) \in \mathbb{R}^D, \quad (3)

where G is the bag representation, h_i \in \mathbb{R}^D is the extracted feature for the patch x_i through the feature extractor f_i, a_i is the trainable scalar weight for h_i and D is the dimension of vector G and h_i.

In the self-attention-based [27] MIL, the feature aggregator can be defined as:

Q = HW_Q, K = HW_K, V = HW_V, \quad (4)

O = \text{softmax} \left( \frac{QK^T}{\sqrt{d_q}} \right) V = SV, \quad (5)

where W_Q, W_K, and W_V represent trainable matrices, H denotes the collection of patch features, O has integrated the attributes of the other features, and d_q is the dimension of the query vector.

#### 3.2 Attention Aggregator

During the computation of \text{Sim}(i, j) as defined in Eq. 5, the algorithmic complexity scales quadratically with O(N^2). Given that N frequently comprises several thousand elements, this substantially extends the expected computational time. Linear attention offers a reduction in computational time but at the expense of information. To mitigate this issue, transiml [21] employs the Nyström approximation in Eq. 5 [33]. The matrices \hat{Q} and \hat{K} are constructed, and the mean of each segment is computed as follows:

\begin{aligned} \hat{Q} &= [\hat{q}_1; \dots; \hat{q}_m], \quad \hat{q}_j = \frac{1}{m} \sum_{i=(j-1) \times m}^{(j-1) \times m + m-1} q_i, \quad \forall j = 1, \dots, m \quad (6) \\ \hat{K} &= [\hat{k}_1; \dots; \hat{k}_m], \quad \hat{k}_j = \frac{1}{m} \sum_{i=(j-1) \times m}^{(j-1) \times m + m-1} k_i, \quad \forall j = 1, \dots, m \quad (7) \end{aligned}

where \hat{Q} \in \mathbb{R}^{m \times D} and \hat{K} \in \mathbb{R}^{m \times D}.

The approximation of the \hat{S} in Eq. 5 can then be expressed as:

\hat{S} = \text{softmax} \left( \frac{Q\hat{K}^T}{\sqrt{d_q}} \right) Z^* \text{softmax} \left( \frac{\hat{Q}\hat{K}^T}{\sqrt{d_q}} \right), \quad (8)

where, Z^* represents the approximate solution to (\hat{Q}, \hat{K}, Z) = 0, necessitating a linear number of iterations for convergence.

In MIL tasks, Nyström attention filters out patches with important features because of the sampling mechanism. Moreover, the difference in N will lead to an overall imbalance during local downsampling. So we consider agent attention methods with linear time complexity and the agent attention mechanism [9] can be written as:

O = \sigma(QA^T) \sigma(AK^T) V, \quad (9)

where \sigma(\cdot) is the Softmax function, Q, K, V are defined in equation Eq. 4. Here A \in \mathbb{R}^{N \times D} is the agent matrix pooling from Q. The term D stands for the feature dimension, while n refers to the agent dimension and acts as a hyperparameter.

Given that the agent is non-trainable and the distribution of attention scores may be defined by a hyperparameter, it becomes imperative to establish an adaptive agent capable of dynamically adjusting the attention score distribution to enhance model performance and flexibility.

#### 3.3 Agent Mask Denoise Mechanism

As illustrated in Figure 1, our overall framework is based on Eq. 5 and Eq. 9. The proposed overall framework is shown in Figure 2. Before the input features are processed by the model, a class token is embedded into them, resulting in the feature matrix H \in \mathbb{R}^{D \times (N+1)}, where D is the dimension of the features and (N+1) represents the number of patches, including the embedded class token. Trainable Agent (A) in the previously outlined methodology, matrix A in Eq. 9 is initially from matrix Q through mean pooling. A = pooling(Q) (Q \in \mathbb{R}^{N \times D}), indicating a limitation in encapsulating the entirety of information present within Q. To overcome this limitation, A is defined as a trainable matrix. Through matrix A \in \mathbb{R}^{N \times D}, the intermediate matrices QA = QA^T \in \mathbb{R}^{N \times (N+1) \times n}

---

<!-- Page 5 -->

Agent Aggregator with Mask Denoise Mechanism for Histopathology Whole Slide Image Analysis

MM 24, October 26–November 1, 2024, Melbourne, VIC, Australia

**Algorithm 1**
 Agent Aggregator With Mask Denoise Mechanism

**Input:**
 
(B, N, D)

**Output:**
 
Y: (B, N, D)

1: 
U // B
-bag features
2: 
q // B
-batch 
N
-token number 
D //
feature dimensions
3: 
Q, K, V: (B, N, D) \leftarrow \text{nn.linear}(H)

4: 
A: (B, N, D) \leftarrow \text{trainable parameters}

5: 
M // N
-number of agent tokens
6: 
Q_A: (B, N, n) \leftarrow \text{torch.matmul}(Q, A^T)

7: 
K_A: (B, N, n) \leftarrow \text{torch.matmul}(A, K^T)

8: 
V_A: (B, N, n) \leftarrow \text{torch.matmul}(A, V)

9: 
M: (B, N, D) \leftarrow \text{nn.linear}(V_A)

10: 
THR: (B, n) \leftarrow \text{nn.linear}(V_A)
, 
\text{squeeze}(1, \text{mean}(-1))

11: 
M_1: (B, N, D) \leftarrow \text{torch.where}(M > THR, 1, 0)

12: 
M_2: (B, N, D) \leftarrow \text{torch.matmul}(M_1, M_1)

13: 
DN: (B, N, D) \leftarrow \text{nn.linear}(V_A)

14: 
VM: (B, N, D) \leftarrow \text{torch.add}(VM, DN)

15: 
Y: (B, N, D) \leftarrow \text{torch.matmul}(Q_A, VM_D)

16: 
U // Y
-weighted bag features
17: 
**return**
 
Y

and K_A = AK^T \in \mathbb{R}^{n \times (N+1)} can be obtained. Utilizing the general attention strategy, the intermediate variable is:

 \begin{aligned}
 V_A &= \sigma(K_A)V \\
 &= \sigma(AK^T)W \in \mathbb{R}^{n \times D}.
 \end{aligned} \quad (10)
 

Mask Agent. In this MIL task, most regions of a WSI do not contribute much to the prediction, so a learnable mask is generated by using the trainable threshold to mask the region of interest.

r = \sigma(p(W_c V_A^T)), \quad (11)

where W_c \in \mathbb{R}^{1 \times D}, function p is an adjustable aggregate function such as mean-pooling, and r is the threshold used in Eq. 12.

Calculate the importance of each feature to optimize the important features in the hidden space. The selection of features will have the risk of information loss. To balance important information selection and the original characteristics of the aggregation, we proposed a new module which can be defined as:

VM_{Di} = V_{Aij} / (M_{ij} + r + DN_{ij}). \quad (12)

where M = VM_{Di} is the threshold matrix to obtain the importance of each feature, and DN = W_{DN}V_A is the denoise matrix to aggregate information. Here, W_{Aij} and W_{DN} are learnable parameters.

Agent Visualization. The foundational agent attention architecture lacks the capability to produce a variable concentration score for sequences. To address this limitation, we outline a methodology that facilitates the visualization of attention scores:

Att_{ij} = \sum_{k=1}^n Q_{Aik} K_{Ajk}, \quad (13)

where Att_{ij} is the attention score of the feature h_i.

AMD. Establishing the aforementioned modules, This framework, a novel framework titled mask denoise mechanism. This framework, as illustrated in Figure 2, encompasses a learning-based agent attention mechanism, representation refinement, and feature aggregation. The algorithm process is shown in Algorithms 1 and the module can be expressed as:

O = \sigma(QA^T)VM_D, \quad (14)

where md represents the mask denoise mechanism, and VM_D represents the matrix calculated from the mechanism Eq. 12.

Due to the differences in the threshold selection method, the other two feature threshold selection strategies are considered as follows:

- •Mean-AMD.Mean selection: selected the average value in the features as the threshold selected by all features.
- •CNN-AMD.CNN selection: through the method of group convolution, the characteristics of different groups are reduced, and the average value between the groups is the threshold.

## 4 EXPERIMENTS

### 4.1 Datasets and Evaluation Metrics

In our study, We use four public datasets to assess our approach.

CAMELYON-16 is a dataset for early-stage breast cancer lymph node metastasis detection. The dataset comprises 339 WSIs, which are officially split into 270 for training and 129 for testing. We use 6-fold cross-validation to ensure that all data are utilized for both training and testing, thereby preventing overfitting to the official test set. In addition, we employ the pre-trained weights from the CAMELYON-16 dataset to perform inference on the external dataset CAMELYON-17 only once. Subsequently, we report both the mean and variance of the evaluation metrics.

TCGA-LUNG includes 1034 WSIs: 528 from LUAD and 507 from LUSC cases. We split the dataset into 65:10:25 for training, validation, and testing. 4-fold cross-validation is used, and the mean and standard deviation of metrics are reported.

TCGA-KIDNEY includes 1075 WSIs: 117 from KICH, 539 from KIRC, and 419 from KIRP cases. We split the dataset into 65:10:25 for training, validation, and testing. We use 4-fold cross-validation and report the mean and standard deviation of metrics.

We report the mean and standard deviation of the macro F1 score, the AUC for one-versus-rest, and the slide-level accuracy (ACC).

### 4.2 Implementation Details

During the pre-processing phase, we generate non-overlapping patches of 256x256 pixels at 20x magnification for the datasets CAMELYON-16, CAMELYON-17, TCGA-KIDNEY, and TCGA-LUNG.

This produces a total of an average count of approximately 9024, 7987, 1326, and 10141 patches per bag for the respective datasets.

Uniform hyperparameters are maintained across all experiments. Each experiment is conducted on a workstation equipped with NVIDIA RTX A6000 and a storage capacity of approximately 9024, 7987, 1326, and 10141 patches per bag for the respective datasets. ResNet50 [10] as the feature encoding model. The Adam optimization algorithm is used, incorporating a weight decay of 1e-5. The initial learning rate is set at 2e-4, and cross-entropy loss is employed as the loss function.

---

<!-- Page 6 -->

MM '24, October 28–November 1, 2024, Melbourne, VIC, Australia

Xitong Ling et al.

Table 1: Performance of AMD-MIL on CAMELYON-16, CAMELYON-17, TCGA-LUNG, and TCGA-KIDNEY datasets.

| Method | CAMELYON-16 | CAMELYON-16 | CAMELYON-17 | CAMELYON-17 | TCGA-LUNG | TCGA-LUNG | TCGA-KIDNEY | TCGA-KIDNEY |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | ACC(%) | AUC(%) | ACC(%) | AUC(%) | F1(%) | ACC(%) | F1(%) | ACC(%) | F1(%) |   |   |   |
| MeanMIL | 79.4±12 | 83.3±13 | 78.5±23 | 69.5±14 | 69.3±34 | 85.4±13 | 86.4±32 | 82.0±11 | 90.3±6 | 93.0±4 | 87.9±10 |   |
| MaxMIL | 76.4±91 | 80.4±64 | 75.4±35 | 66.7±16 | 70.2±32 | 85.8±92 | 87.7±12 | 87.4±34 | 88.7±72 | 91.2±38 | 93.5±13 | 86.8±32 |
| ABMIL [11] | 84.8±14 | 85.9±65 | 84.1±22 | 78.7±198 | 77.3±164 | 75.3±132 | 88.4±64 | 83.1±23 | 87.6±10 | 91.6±93 | 94.1±82 | 88.5±23 |
| G-ABMIL [11] | 84.0±26 | 85.3±111 | 83.6±34 | 79.9±76 | 79.3±87 | 76.2±82 | 87.6±77 | 91.0±163 | 86.3±82 | 91.4±15 | 93.8±84 | 90.4±10 |
| CLAM-MB[17] | 91.3±82 | 94.5±78 | 90.7±91 | 83.6±42 | 84.8±371 | 81.3±70 | 89.3±23 | 94.2±18 | 85.1±42 | 91.2±78 | 92.6±66 | 90.2±74 |
| CLAM-SH[17] | 91.9±38 | 94.3±22 | 91.3±34 | 83.9±68 | 85.2±14 | 81.5±41 | 87.3±23 | 93.1±41 | 89.1±44 | 89.7±36 | 93.9±67 | 90.2±68 |
| DSMIL [13] | 85.8±63 | 91.6±72 | 86.2±25 | 72.2±76 | 72.8±66 | 87.2±82 | 85.0±83 | 93.6±82 | 85.9±64 | 90.2±78 | 94.7±66 | 86.2±71 |
| TransMIL [21] | 87.8±24 | 93.7±21 | 88.7±61 | 75.4±62 | 74.6±77 | 87.9±22 | 94.1±12 | 88.2±40 | 91.3±26 | 92.5±75 | 89.3±98 |   |
| DTD [35] | 89.4±23 | 92.9±92 | 88.4±78 | 76.3±67 | 77.8±88 | 75.4±82 | 86.8±14 | 94.7±75 | 86.1±91 | 91.5±79 | 95.3±85 | 90.6±77 |
| RRT [26] | 90.9±68 | 94.7±14 | 90.2±88 | 78.9±22 | 79.5±31 | 78.7±34 | 89.2±98 | 94.4±74 | 85.4±16 | 93.3±23 | 95.7±18 | 91.2±45 |
| WIGK [14] | 91.1±28 | 94.9±18 | 90.8±15 | 80.3±41 | 80.4±38 | 77.8±28 | 89.7±66 | 94.6±72 | 89.3±12 | 93.2±11 | 95.8±94 | 91.9±12 |
| AMD-MIL | 92.9±73 | 96.4±38 | 92.7±83 | 85.0±32 | 85.3±69 | 82.7±24 | 90.5±13 | 95.2±79 | 90.51±9 | 94.4±13 | 97.3±74 | 92.9±61 |

Figure 3: Visualization of AMD-MIL Attention Distribution Compared to Official Annotations on CAMELYON dataset.

### 4.3 Comparison with State-of-the-Art Methods

In this study, we present the experimental results of our newly developed AMD-MIL framework applied to the CAMELYON-16, CAMELYON-17, TCGA-LUNG, and TCGA-KIDNEY datasets. We compare this framework with various methodologies, including

MeanMIL, MaxMIL, ABMIL [11], CLAM [17], DSMIL [13], TransMIL [21], DTD [35], RRT [26], and WIGK [14].

As shown in Table 1, the AMD-MIL framework demonstrates superior performance, achieving AUC scores of 96.4% for CAMELYON-16, 85.3% for CAMELYON-17, 95.2% for TCGA-LUNG, and 97.3% for TCGA-KIDNEY. Notably, these scores consistently exceed those of the previously mentioned comparative methods, highlighting

---

<!-- Page 7 -->

Agent Aggregator with Mask Denoise Mechanism for Histopathology Whole Slide Image Analysis

MM '24, October 26–November 1, 2024, Melbourne, VIC, Australia

the framework's exceptional ability to dynamically adapt to inputs. This adaptability enables the effective capture of key features, accurately representing the original bag features.

As demonstrated in Table 3, we also conduct a comparative analysis to evaluate the impact of different threshold selection methods on the metrics. We find that using a linear layer for aggregation outperforms both average pooling and group convolution.

#### 4.4 Interpretability Analysis

We conduct an interpretability analysis of AMD-MIL. In Figure 3, the blue-annotated areas denote the official annotations of cancerous regions in the CAMELYON dataset, whereas the heatmap regions represent the distribution of agent attention scores across all patches constituting the WSIs, calculated according to Eq. 13. The attention scores indicate the contribution level of instances to the classification outcome, and it is distinctly observable that areas with high attention scores align closely with the annotated cancerous regions. This demonstrates that the AMD-MIL classification relies on cancerous ROIs, mirroring the diagnostic process of pathologists and thereby providing substantial interpretability for clinical applications. AMD-MIL possesses robust localization capabilities for both macro-metastases and micro-metastases. For example, in Figure 3 (f), which includes both macro- and micro-metastases, AMD-MIL can also concurrently localize to different areas.

#### 4.5 Ablation Study

Effectiveness of Agent Aggregator. The trainable agent aggregator uses agent tokens as intermediate variables for the query and key in the self-attention mechanism. This approach ensures global modeling and approximates linear attention. We compare the trainable agent aggregator with the original pooling agent aggregator and the Nystrom attention aggregator from TransMIL. The original pooling agent aggregator reduces parameter count using an agent mechanism and achieves enhanced global modeling through

Figure 4: Attention distribution of different agent tokens.

Figure 5: Influence of the number of agent tokens

Figure 6: Effectiveness of the mask denoise mechanism.

broadcasting. As shown in Table 2, it significantly outperforms the Nystrom attention aggregator from TransMIL across three datasets.

However, the pooling agent aggregator struggles to adapt dynamically to inputs, and its pooling mechanism may average out important information. Initializing the agent as a trainable parameter results in improved metrics compared to the pooling agent aggregator. This change allows the model to better adapt to varying inputs and maintain the significance of crucial instances, thereby enhancing overall performance.

---

<!-- Page 8 -->

MM '24, October 28–November 1, 2024, Melbourne, VIC, Australia

Xitong Ling et al.

**Table 2: Comparison between TransMIL with AMD-MIL and the effectiveness of the components of AMD-MIL.**

| Dataset | Component | Component | Component | Component | Component | ACC(%) | AUC(%) | F1(%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | Nystrom | agent | train | mask | denoise | ACC(%) | AUC(%) | F1(%) |
| CAMELYON-16 | ✓ |   |   |   |   | 87.83 24 | 93.73 21 | 88.73 61 |
| CAMELYON-16 |   | ✓ |   |   |   | 89.33 90 | 93.83 08 | 88.63 09 |
| CAMELYON-16 |   |   | ✓ |   |   | 91.23 62 | 95.63 06 | 91.23 67 |
| CAMELYON-16 |   |   |   | ✓ |   | 93.03 72 | 96.03 00 | 92.73 80 |
| CAMELYON-16 |   |   |   |   | ✓ | 92.93 73 | 96.42 89 | 92.72 83 |
| LUNG | ✓ |   |   |   |   | 87.93 22 | 94.13 12 | 88.23 40 |
| LUNG |   | ✓ |   |   |   | 88.48 46 | 95.90 86 | 88.48 88 |
| LUNG |   |   | ✓ |   |   | 87.53 00 | 92.63 47 | 87.43 12 |
| LUNG |   |   |   | ✓ |   | 90.21 19 | 94.60 91 | 90.21 19 |
| LUNG |   |   |   |   | ✓ | 90.51 51 | 95.20 70 | 90.51 59 |
| KIDNEY | ✓ |   |   |   |   | 91.12 56 | 92.25 75 | 89.32 08 |
| KIDNEY |   | ✓ |   |   |   | 93.76 43 | 97.03 57 | 91.16 04 |
| KIDNEY |   |   | ✓ |   |   | 93.71 13 | 97.76 57 | 91.46 18 |
| KIDNEY |   |   |   | ✓ |   | 93.41 06 | 97.60 57 | 90.76 13 |
| KIDNEY |   |   |   |   | ✓ | 94.41 13 | 97.36 74 | 92.91 01 |

We explore the attention distribution patterns among agent tokens as shown in Figure 4. The first agent token focuses on non-cancerous tissues, whereas the second targets cancerous zones. This suggests that different agent tokens have unique focal points. This variance ensures that during broadcasting, diverse queries focus on their respective areas, enhancing the model’s ability to differentiate between critical and non-critical regions.

The number of agent tokens is crucial for AMD-MIL performance. Figure 5 shows results from experiments on four datasets with agent token counts of 52, 64, 128, 256, 384, and 512. The ACC on the CAMELYON-16 dataset fluctuates with more agent tokens, possibly due to its small size causing instability. On the CAMELYON-17 dataset, the AUC increases with more agent tokens, while the ACC initially increases and then decreases. On the CAMELYON-16 dataset, the AUC and, on the TCGA datasets, both the AUC and ACC maintain stable performance. This consistency aligns with findings from experiments adjusting agent token numbers in shallow attention stacks on natural images [8].

Effectiveness of Mask Denoise Mechanism. The mask denoise mechanism enhances the allocation of attention scores by selectively masking out less significant representations. Denoising matrices are employed to mitigate noise introduced during the masking process. Table 2 presents a comparison of metrics for the agent aggregator with and without the mask denoise mechanism, demonstrating average performance improvements. Figure 6 illustrates the contrast in the distribution of instance attention scores. Even without the mask denoise mechanism, some WSIs are correctly classified. However, higher attention sometimes targets non-cancerous areas, reducing interpretability. For micro-metastatic cancer, this bias can result in errors, posing significant clinical challenges. With the mask denoise mechanism, attention scores are more focused on cancerous ROIs, thereby reducing attention to non-cancerous regions. This suggests that the mask denoise mechanism enhances interpretability by dynamically correcting attention scores.

**Figure 7: Model convergence of AMD-MIL and TransMIL.**

As shown in Figure 7, we compare the convergence of AMD-MIL and TransMIL. AMD-MIL shows more stable and better performance.

**Table 3: Different thresh select methods on Camelyon-16.**

| Thresh | ACC(%) | AUC(%) | F1(%) |
| --- | --- | --- | --- |
| Mean | 91.32 12 | 96.02 21 | 91.03 43 |
| CNN | 91.23 66 | 95.83 39 | 91.03 60 |
| Linear | 92.93 73 | 96.42 89 | 92.73 83 |

## CONCLUSION

In pathological image analysis, attention-based aggregators significantly advance MIL methods. However, traditional attention mechanisms, due to their quadratic complexity, struggle with processing high-resolution images. Additionally, approximate linear self-attention mechanisms have inherent limitations. To address these challenges, we introduce AMD-MIL, a novel approach for dynamic agent aggregation and representation refinement. Our validation on four distinct datasets demonstrates not only AMD-MIL’s effectiveness but also its ability for instance-level interpretability.

---

<!-- Page 9 -->

Agent Aggregator with Mask Denoising Mechanism for Histopathology Whole Slide Image Analysis

MM-21, 2024, November 21, 2024, Melbourne, VIC, Australia

ACKNOWLEDGEMENT

This study was supported by the Component Project of Shenzhen Pathology Medical Innovation Intelligent Diagnosis Engineering Research Center (XMH2203510054) and Jinli Fuyouan Guan Food Group Co., Ltd. This work was also supported by the Science and Technology Foundation of Shenzhen City grant number KJCYZ202102211170370202.

REFERENCES

1. [1] Hu, X., Hu, X., Zhao, X., Wu, X., Zhang, Zheng, Zhang, Jingyan, Wu, Hualei Huang, Yongyang Xiong, Xiangyuan Gong, and Wending Wang. 2024. A Scalable Graph-Based Framework for Multi-Organ Histology Image Classification.IEEE Journal of Medical and Biological Engineering12 (2024), 1199–1209. doi:10.1109/JMBE.2023.19910.
2. [2] Kirsch, R., Kurt A. Bajer, Didier I. Ramm, Vamdarine Velcheti, and Anant Mahadulabai. 2019. Artificial intelligence in digital pathology—new tools for diagnosis and precision medicine.Nature Reviews Clinical medicine18 (2019), 700–715.
3. [3] S. C. Camps, Matthew C. Humana, G. Lema, G. Desalvas, Alain Mirdeilh, Vitor Werneck Kraus Silva, Klaus J. Busam, Edi Bogu, Victor E. Renter, David S. Klimstra, and Nishantha P. Jha. 2019. A deep convolutional pathologist training network supervised deep learning on whole slide images.Nature medicine25 (2019), 1901–1909.
4. [4] [14] J. Chen, Chengkuan Chen, Yiyoung Li, Tiffany Y. Chen, Andrew D. Trister, Rahul G. Krishnan, and Faral Mahmood. 2022. Scaling vision transformers to global histology via multi-scale feature fusion.arXiv preprint arXiv:2206.11455.https://doi.org/10.48550/arXiv.2206.11455.
5. [5] [15] Wei-Dong Peng, Shih-Hao Chen, and Chih-Chung Hsiao. 2019. A large-scale hierarchical image database. In2009 IEEE conference on computer vision and pattern recognition. IEEE Computer Vision 9681–9691.
6. [6] [16] Andre Estare, Alexandre Roelqbert, Bharath Ramaswamy, Volodymyr Kaleshov, Mark DePietro, Katherine Chen, Chaitin Cai, Greg Corrado, Sebastian Thuma, and Jeff Dean. 2019. A guide to deep learning in healthcare.Nature medicine25 (2019), 24–29.
7. [7] [17] Yu Fu, Alexander W. Jung, Ramon Viala Montes, Santiago Gonzalez, Harald Vollrath, Aretim Shumakid, Lucy E. Meres, Jeremie Linares Linares, Luisa Moore, and Moritz Gersing. 2020. Passive remote computational histopathology reveals metastases, tumor composition and prognosis.Nature cancer11 (2020), 806–810.
8. [8] [18] [18] J. Chen, Xin-Yu Pan, Ying-Yin Han, Shih-Jong, and Guo-Huang Tsai. 2020. Pathet transformer: Vision transformer using focused linear attention.arXiv preprint arXiv:2007.07779.
9. [9] [19] [19] Dongchen Han, Tianmu Yu, Ying Han, Zhifan Xia, Shiji Song, and Gao Huang. 2020. Agent Attention: A Hierarchical Graph-based Pathologist Pathway for Whole-Slide Image Recognition.IEEE Conference on Computer Vision 1167–1175. doi:10.1109/ICCV.2020.00874.
10. [10] [20] [20] Kaiming He, Xiangyue Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. InProceedings of the IEEE conference on computer vision and pattern recognition. 70–76.
11. [11] [21] [21] Aleksandrs Ilie, Jakub Tenczak, and Max Welting. 2018. Attention-based deep multiple instance learning. InInternational conference on machine learning. PMLR, 2117–2126.
12. [12] [22] [22] Jakob Nikola Kolbe, Alexander T. Pearson, Nick Halama, Dirk Jager, Jermias Krause, Sven H. Lowen, Alexander Marx, Peter Boer, Frank Tecke, Uli B. Neumann, et al. 2019. Deep learning can predict microsatellite instability directly from histology in gastrointestinal cancer.Nature medicine25 (2019), 1054–1056.
13. [13] [23] [23] Bin Li, Yin Li, and Kevin W. Elcisci. 2021. Dual-stream multiple instance learning network for whole slide image classification with self-supervised contrastive learning. InProceedings of the IEEE/CVF conference on computer vision and pattern recognition. 14318–14328.
14. [14] [24] [24] Jiawen Lu, Youxin Chen, Jiongu Chao, Qibao Sun, Tian Guan, Anjia Han, and Yonghong Zou. 2024. Dynamic Graph Representation with Knowledge-aware Attention for Histopathology Whole-Slide Image Analysis.arXiv preprint arXiv:2408.07794(2024).
15. [15] [25] [25] Xingrong Lin, Zhiqian Xie, Hongyue Hu, Yi Xu, and Chang-Wen Chen. 2023. Interventional Big Multi-Instance Learning on Whole-Slide Pathological Images. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). 18389–18399.
16. [16] [26] [26] Ming Y. Liu, Tiffany Y. Chen, Drew B. Williamson, Michael Zhao, Maha Shady, Nadim J. Jabre, and Faral Mahmood. 2024. 90.84-based pathologist origins criteria for cancers of unknown primary.Nature594, 7864 (2024), 110–116.
17. [17] [27] [27] Ming Y. Liu, Drew B. Williamson, Tiffany Y. Chen, Richard J. Scott, Maurizio Barberi, and Faral Mahmood. 2024. Data-efficient and weakly supervised computational pathology on whole-slide images.Nature biomedical Engineering5 (2023), 455–470.
18. [18] [28] [28] S. Adali, S. Momen and Tonda L. Price. 1997. A framework for multiple-instance learning.Advances in neural information processing systems10 (1997).
19. [19] [29] [29] Scott Mayer, McKinley, Maurin Sarnacki, Varun Goskhale, Jonathan Godwin, Jonathan Godwin, Jonathan Godwin, Jonathan Godwin, Mary Chen, Mary Chen, Mary Chen, Aara Daria, et al. 2020. International evaluation of an AI system for breast cancer diagnosis on whole-slide images.Nature584 (2020), 115–120.
20. [20] [30] [30] Erick Moe, Dylan Bonum, Takahashi Kudo, William Graf, Markas Covart, and David R. S. Kessel. 2020. A deep learning framework for histology.Nature584 (2020), 1213–1216.
21. [21] [31] [31] S. Adali, S. Momen, and Yuan Feng. 2019. Joint Vision, Joint Imaging, Joint Data, 2020. TransMol. Transformer based correlated multiple instance learning for histology and pathology diagnosis.Advances in neural information processing systems34 (2021), 2134–2147.
22. [22] [32] [32] Zhihuan Shen, Yifeng Wang, Yang Chen, Hao Han, Shaohai Liu, Haifeng Wang, Shihao A. Wu, Xiaohu An, Yuhao Tang, Yuhao Tang, and Jiaoyu Mao. 2020. Promoting multiple instance learning in whole slide images. InProceedings of the IEEE/CVF conference on computer vision and pattern recognition. 21495–21505.
23. [23] [33] [33] Andrew H. Song, Guillaume Jaume, Drew F. Williamson, Ming Y. Lu, Anurag K. Agrawal, and S. Momen. 2020. A deep learning framework for histology: a digital and computational pathology.Nature Reviews Bioengineering11 (2023), 98–106.
24. [24] [34] [34] Chetina L. Sindhuji, Oshan Ciga, and Aneel L. Maitre. 2017. Deep neural network-based histological histopathology.Nature.https://doi.org/10.1038/s41591-017-0013-8.
25. [25] [35] [35] Wenhao Tang, Sheng Huang, Xiangyu Zhang, Fengqiu Zhou, Yi Zhang, and Bo Lu. 2019. A multi-scale attention framework with multiple instance learning for whole slide image classification. InProceedings of the IEEE/CVF International Conference on Computer Vision. 479–487.
26. [26] [36] [36] Wenhao Tang, Fengqiu Zhou, Sheng Huang, Xiang Yu, Yi Zhang, and Bo Lu. 2019. Feature Re-Embedding: Toward Foundation Model-Level Performance in Pathological Histology.arXiv preprint arXiv:2002.17228(2020).
27. [27] [37] [37] Jiaxin Xiang, Yuhao Tang, Sheng Huang, and Fengqiu Zhou. 2017. Attention is all you need.arXiv preprint arXiv:1612.05703.
28. [28] [38] [38] W. Wang, Jiao Chen, Caisa Cao, Guangming Liu, Qi Dou, Qiao Huang, Muyan Cao, and Pengyan Xie. 2022. Weakly-supervised learning for whole slide-language cancer classification. InMedical imaging with deep learning. Springer Nature, Yongquan Yan, Peng Zhang, Xiang Bai, and Wenyou Liu. 2018. Resolving multiple instance neural networks.Pattern Recognition74 (2018), 24–34.
29. [29] [39] [39] X. Xie, Wang, Sen Yang, Xin Zhang, Minghui Wang, Jing Zhang, Wei Yang, Junsho Huang, and Xiao Han. 2022. Transforming unsupervised contrastive learning for histopathological image classification.Medical image analysis81 (2021), 102559.
30. [30] [40] [40] Jiaxin Xiang and Jun Zhang. 2022. Exploring low-rank property in multiple instance learning for whole slide image classification. InThe Eleventh International Conference on Learning Representations.
31. [31] [41] [41] Chen Xie, Xie Saining, and He Kaiming. 2021. An empirical study of training self-supervised visual transformers.arXiv preprint arXiv:2104.03021(2021).
32. [32] [42] [42] Huayong Xiong, Zhenpeng Zou, Radha Chakraborty, Mingtang Tan, Guan Fan, Yin Li, and Vikas Singh. 2021. NystromNet: A nystrom-based algorithm for approximating self-attention. InProceedings of the AAAI Conference on Artificial Intelligence. Vol. 35, 14138–14148.
33. [33] [43] [43] Zehui Ye, Yonghong Li, and Tian Guan. 2023. Semantic-Similarity Collaborative Knowledge Distillation Framework for Whole-Slide Image Classification. In2023 IEEE International Conference on Bioinformatics and Biomedicine (BIBM). 1655–1661.
34. [34] [44] [44] Hai Xiang, Yuhao Tang, Yuhao Tang, Xiang Hong, Xuanyou Yang, Sarah E. Coupland, and Yalin Zhang. 2022. Difc-mll: Double-tree feature distillation multiple instance learning for histopathology whole slide image classification. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 18402–18412.