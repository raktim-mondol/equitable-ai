<!-- Page 1 -->

1982

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

# Proportionally Fair Hospital Collaborations in Federated Learning of Histopathology Images

S. Maryam Hosseini, Miled Sikaroudi, Morteza Babaie✉, and H. R. Tizhoosh✉, Senior Member, IEEE

Abstract—Medical centers and healthcare providers have concerns and hence restrictions around sharing data with external medical institutions, including, as a privacy-preserving method, involves learning a site-independent model without having direct access to patient-sensitive data distributed in a centralized fashion. The federated approach relies on decentralized data distribution from various hospitals and clinics. The collaboratively learned global model is supposed to have acceptable performance for the individual sites. However, existing methods focus on minimizing the average of the aggregated loss functions, leading to a biased model that performs perfectly for some hospitals while exhibiting unsatisfactory performance for other sites. In this paper, we improve model ‘fairness’ among participating hospitals by proposing a novel federated learning scheme called Proportionally Fair Federated Learning, short Prop-FFL. Prop-FFL is based on a novel optimization objective function to decrease the performance variance among participating hospitals. This function encourages a fair model, providing us with more uniform performance across participating hospitals. We validate the proposed Prop-FFL on two histopathology datasets as well as two general datasets to shed light on its inherent capabilities. The experimental results suggest promising performance in terms of learning speed, accuracy, and fairness.

Index Terms—Federated learning, proportional fairness, medical imaging, digital pathology, histopathology.

## I. INTRODUCTION

THE prediction power of deep learning methods depends on the size and diversity of the training data. However, large-scale datasets enables the model to more precisely estimate the underlying distribution of the data. For example, the

public availability of the ImageNet [1] with almost 1.2 million diverse data samples has led to considerable advancements in computer vision. Machine learning methods, and deep models, in particular, rely on training datasets that are ideally aggregated from various sources. However, it appears currently impossible to gather large-scale datasets in one central location in medical domain due to privacy-sensitive data [2]. In centralized learning methods for medical imaging, training data is from different medical centers such as hospitals and clinics, which are brought together to a centralized location, commonly called a server. However, hospitals are generally not willing to share their patients’ medical records without other external collaborators because of privacy considerations and regulatory compliance [3]. Therefore, the lack of large-scale diverse datasets publicly available to researchers hinders model development in healthcare. To overcome these challenges, decentralized learning methods are a promising scheme to preserve data privacy while enabling training of generalizable models. Federated learning allows training on multi-institutional datasets without having direct access to data samples.

Federated learning has emerged as a promising solution to protect user-sensitive data by keeping data local. It is a novel decentralized paradigm that plays a critical role in privacy-sensitive applications, opening a new horizon for secured decentralized learning methods. Federated learning as a decentralized approach was first proposed by McManan in 2017 [4]. The main concern of federated learning is data privacy to protect users against data disclosures. It has become a recent active area of research because of increased concern for data privacy and cybersecurity [5]. Federated learning was first proposed for federated mobile networks applications to accommodate decentralized training. It enables mobile users to keep their local data private, training the model locally relying on their private data and sharing only the training results (not data) with the central server and hence other users. This allows the server to train the global model relying only on the aggregated training results of decentralized data. However, federated learning was first proposed for wireless networks, that can be applied to other privacy-sensitive applications such as the medical domain.

There are three principal challenges in histopathology image analysis, which encourage us to employ federated learning. First, histopathology image analysis is a complicated, time-consuming task since images are large with many details relevant for diagnosis. Using AI systems can reduce the workload on pathologists and facilitate diagnosis [6]. Second,

Manuscript received 1 October 2022; revised 20 November 2022; accepted 28 December 2022. Date of publication 5 January 2023; date of current version 29 June 2023. This work was supported by the Ontario Research Funds, Research Excellence (OPRE-RE), Grant and Mayo Clinic Sponsorship. (Corresponding author: H. R. Tizhoosh.)

S. Maryam Hosseini and Miled Sikaroudi are with the Laboratory for Knowledge Inference in Medical Image Analysis (Kimia Lab), University of Waterloo, Waterloo, ON N2L 3G1, Canada, also with the MARS Centre, Vector Institute, Toronto, ON M5G 1M1, Canada. (e-mail: s.maryam.hosseini@uwaterloo.ca; miled.sikaroudi@uwaterloo.ca).

Morteza Babaie is with the Laboratory for Knowledge Inference in Medical Image Analysis (Kimia Lab), University of Waterloo, Waterloo, ON N2L 3G1, Canada, also with the MARS Centre, Vector Institute, Toronto, ON M5G 1M1, Canada. (e-mail: m.babaie@uwaterloo.ca).

H. R. Tizhoosh is with the Laboratory for Knowledge Inference in Medical Image Analysis (Kimia Lab), University of Waterloo, Waterloo, ON N2L 3G1, Canada, also with the MARS Centre, Vector Institute, Toronto, ON M5G 1M1, Canada, and also with the Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN 55905 USA (e-mail: htizhoosh.hamid@mayo.edu).

Digital Object Identifier 10.1109/TMI.2023.3234450

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.

For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

---

<!-- Page 2 -->

HOSSEINI et al.: PROPORTIONALLY FAIR HOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1983

studies have shown that observer variability in histopathology image diagnosis can be significant due to specific diagnostic biases such as the proportionally fair training or working environment [7]. Access to a second (computational) opinion provided by machine learning can make pathologists more confident in their decision and complement their visual assessments. Third, similar to other medical domains, histopathology images contain critical information that we may not be able to share for the sake of patients' privacy [2]. Also, having access to histopathology data from different medical centers is a vital prerequisite to training a generalized model. As such, federated learning seems to be a solution that can address all those challenges. It not only trains deep models to make the diagnosis task more accurate but also reduces inter-observer variability and improves consensus by learning a collaborative model for quantification of tissue morphology without violating patients' privacy.

There are two main components in the federated learning, namely a central server and some local centers [4]:

- • Alocal centeris a clinic or hospital that is willing to participate in the learning of a global model but is not interested in sharing any patient data with other organizations. The local center might also be called a participant or hospital in this paper. Apparently, there exists more than one local center in any federated learning scenario.
- • Acentral serveris the main hub responsible for orchestrating decentralized learning. It facilitates the aggregation of training results from all the local centers and its main goal is to train a global model with acceptable performance for all participants. Therefore, it is also called an aggregation center.

The main concern of this paper is how to aggregate the training results at the central server. Most existing methods train the global model by simply minimizing the average training losses of all local centers. However, these methods do not provide a performance guarantee for each individual hospital since they focus on the average training results. These methods lead to a global model that its performance varies among the hospitals. This is a problem is expected to worsen in real-world scenarios where the data from different medical centers exhibit heterogeneity both in terms of size and distribution.

While we cope with the data heterogeneity by modifying the aggregation of the central server, the central server's method approach that deals with highly non-IID data distributions is personalized federated learning (PFL) [8]. PFL has been proposed to improve individual performances by enabling each client to learn a customized model. However, one major drawback of a PFL model is the loss of generalization since the customized model is trained on a single hospital in each hospital. While PFL can be helpful for some personalized health applications, it is certainly not suitable for other applications requiring a generalized model to avoid disparity in healthcare delivery [9]. Besides, PFL requires further analysis to adjust model parameters for each hospital, which increases the overhead. Therefore, compared with PFL, modifying the

aggregation rule at the central server can cope with non-IID data distribution and improve generalization without extra learning.

In this paper, we adopt proportional fair resource allocation of wireless communication systems and introduce proportionally fair federated learning, short Prop-FFL, a novel optimization objective in federated learning, to boost more uniform model performance across participating hospitals. The main goal of Prop-FFL is to train a fair model, which is not biased toward any of the participating hospitals at the expense of having undesirable performance for other local centers. To the best of our knowledge, this is the first time that proportional fairness is formulated to modify the deep learning model.

We review the related literature in the next section where we briefly explain the benchmark data and the fairness criterion in federated learning. We describe the intuition behind Prop-FFL and formulate it in Section III, providing a detailed explanation of the proposed method. In Section IV, we provide various experimental results to evaluate Prop-FFL on two histopathology datasets. Also, we present additional experimental results on two general datasets to verify the effectiveness of Prop-FFL. Finally, we conclude the paper in Section V.

## II. BACKGROUND LITERATURE

Federated learning is a promising method that addresses the fundamental challenges of privacy, ownership, and locality of data [5]. Depending on the task at hand, it enables training machine learning models, in a collaborative fashion, over decentralized data centers such as hospitals, relying on remote decentralized local data [4]. To learn a global model at the aggregation center, all local data centers periodically collaborate with each other through communication with the aggregation center. Each iteration of the federated learning procedure consists of three main steps below [10]:

1. 1)Model distribution– The aggregation center broadcasts the global model parameters to each of the local centers via a secured communication link.
2. 2)Local training– Each local center trains the model parameters at the previous stage, each local center trains the global model by relying on its local data.
3. 3)Global aggregation– All participating local centers send the training results back to the aggregation server. Next, the central server processes the received updates from local centers by updating the global model parameters. This procedure is called global training.

These three steps are repeated until the global model training converges. These steps are common among almost all the federated learning methods. More specifically, various federated learning methods may have different assumptions, formulations, and procedures of implementing each step of the general flow of decentralized learning.

## A. Benchmarking Federated Learning Methods

There are two common benchmark methods in federated learning, FedAvg and FedSGD [4].

---

<!-- Page 3 -->

1984

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

1) FedAvg: In FedAvg, i.e., federated averaging [4], each participating hospital trains the global model on its local data for some number of batches and epochs. Then, the central server simply takes the average of training results across all hospitals.

2) FedSGD: Federated stochastic gradient descent, FedSGD, is another benchmark for federated learning [4]. In FedSGD, participants update model weights only for one batch of data and central server is the main node that can update model parameters by taking the average of the training results. More detail of FedSGD is provided in Algorithm 1.

We choose to start with FedSGD and extend FedSGD in our proposed method since it is computationally efficient for hospitals and has convergence guarantee [4]. The expansion of our proposed method on FedAvg to create more communication efficient framework will be left for future works.

### B. Federated Learning in Medical Domain

The research community has recently started to explore the potentials of federated learning for medical image analysis. FL has been employed for classification, segmentation, and detection tasks applied on various types of medical images, such as CT, MRI, microscopy images, and patches of whole slide images.

For detection examples, authors in [11] used federated learning for abnormal detection in COVID 19 CT images, and authors in [12] used federated learning for abnormal tissue detection in brain MRI images. Segmentation of tumors in brain MRI images in federated learning setting has been studied in [13]. The authors in [14] used private prostate MRI images from three institutions and showed the superiority of federated learning in prostate MRI segmentation. As another example of segmentation, authors in [15] employed federated learning for segmenting covid region in chest CT images.

Algorithm 1 FedSGD [4]. There Are M Local Centers, T Is the Number of Epochs, \eta Is Learning Rate, n_k Is the Number of Samples in kth Local Center, n Is the Total Number of Samples.

Input: M, T, w^{(0)}, \eta

Output: w^{T+1}

1. 1: fort = 0, \dots, T - 1do
2. 2:   Server sendsw^tto all hospitals
3. 3:   fork = 1, 2, \dots, Mdo
4. 4:     Given(k, w^t, \eta), each hospital updates the model for one batch of its data and returns
5. 5:w_k^{t+1}
6. 6:   end for
7. 7:   Each hospitalksendsw_k^{t+1}back to the server
8. 8:   Server updatesw^{t+1}as

w^{t+1} = \sum_{k=1}^M \frac{n_k}{n} w_k^{t+1}

1. 7: end for
2. 8: returnw^{T+1}

As classification examples, skin lesion classification in decentralized scenario has been studied in [16]. Authors in [17] conducted a case study of federated learning on histopathology images with the focus on differential privacy. They have also examined design factors on the classifier trained in federated learning setting. Classification of histopathology images in federated learning fashion have also been investigated in [18]. The proposed method can further reduce the amount of communication between the server and hospitals.

Most of these papers mostly focus on the studying the applicability of federated learning in medical domain. They do not address urgent challenges in federated learning such as fairness among participants.

### C. Fairness in Federated Learning

Most existing federated learning methods focus on the average performance of the global model. However, this might lead to a highly biased performance among participant hospitals. For example, relying on these methods make the model biased towards hospitals with larger datasets, having undesirable performance on those hospitals that have access to only small datasets. Additionally, in real-world scenarios, participants may have different data, i.e., that learning hospital distributions because of different patient populations, focusing on the average performance will result in a model that performs well for some hospitals while having performance degradation on other hospitals. This means that there is no performance guarantee for individual hospitals.

To address this concern, fairness in federated learning has attracted considerable attention recently. The key point of fairness is that fair sharing is not equal sharing always [19]. As a result, one can design FL methods to ascertain that the participant hospitals for which the trained model has unacceptable performance on their data should contribute more to the global loss function. In this regard, q-fair federated learning has been proposed [20]. The authors introduced a set of novel optimization problems, namely q-fairness, to apply fairness in federated learning. Having the parameter q in their proposed optimization problem enables the central server to guide the loss function. The authors also introduced q-fairness FedSGD, or q-FedSGD, to apply fairness in FedSGD. According to our literature review, q-fair federated learning [20] is the benchmark for fairness in federated learning, therefore, we have compared our proposed method with q-FedSGD. There are other works that consider fairness in federated learning. For example authors in [21] introduce a novel form of fairness in federated learning, called min-max optimization. The authors address the fairness problem by employing min-max optimization, focusing on the weakest participant with maximum loss. However, changing the focus of the model toward the worse-performing participant is not reasonable since it may degrade the total performance. The authors in [22] focus on both fairness and robustness of federated learning. They address these challenges by dynamically choosing a fraction of local centers to participate in training. However, this approach cannot be applied in medical domains because there are limited number of participant hospitals

---

<!-- Page 4 -->

HOSSEINI et al.: PROPORTIONAL FAIRNESS COLLABORATION IN FEDERATED LEARNING

1985

as oppose to wireless network applications where there are thousands of mobile users. Authors in [23] address fairness with different approach. They propose a novel collaborative fair federated Learning framework to enforce participants to converge to different models.

### III. PROPORTIONAL FAIRNESS

In this section, we provide a detailed explanation of our proposed proportionally fair federated learning (Prop-FFL). While the purpose of this multi-server federated learning method is to minimize the average training loss over all participant hospitals, that aggregation might lead to a variable performance among hospitals, having a bias toward some participants that contributed more toward the loss function, and hence adjusting the model parameters. To resolve this issue, we propose to consider during the aggregation procedure on the central server.

Inspired by proportional fair resource allocation methods in the wireless network [24], we introduce Prop-FFL to learn a global model that performs well for all participants, not just some of them. The main goal of Prop-FFL is to enable all hospitals to fairly (not necessarily equally) contribute to the training of the global model. Prop-FFL focuses on the participants with rather poor performance, changing the network parameters to improve their performance. The Prop-FFL ascertains fairness by modifying the optimization problem at the central server. It encourages the model not to have undesirable performance on any of hospitals while minimizing the total training loss.

#### A. Problem Formulation

We consider a set of hospitals \mathcal{M} with M hospitals with privately labeled data indexed by \{1, 2, \dots, M\} \in \mathcal{M}. The amount hospital i \in \mathcal{M} has only access to its local data that is denoted by \mathcal{D}^i. Dataset \mathcal{D}^i consists of n_i training data points denoted by \mathcal{D}^i = \{a_i^1, y_i^1, \dots, a_i^{n_i}\}, where a_i^1 is training input and b_i^1 is its label, e.g., a primary diagnosis. The total number of samples of all hospitals is n = \sum_{i=1}^M n_i. As in most real-world applications, datasets \{\mathcal{D}^i\}_{i=1}^M may not have identical independent distributions (IID).

Prop-FFL applies fairness by encouraging the model to perform similarly on all M hospitals. In Prop-FFL, the optimization objective function composes of two terms, one to use fairness and one to reduce the training loss. The fairness term aims to adjust the model parameters such that all M hospitals have a similar training loss to achieve that, we define the fairness term as an optimization problem that maximizes the multiplicity of loss functions of all M hospitals. We will show that the optimal solution of the fairness term emerges when all the M hospitals have the same training loss. In the following, we elaborate on these two terms of the optimization objective function starting with the fairness term. To mathematically explain, we define the relative training loss of the kth hospital as normalized loss denoted by

F_k^i(w) = \frac{F_k(w)}{\sum_{j=1}^M F_j(w)}, \quad 1 \leq k \leq M, \quad (1)

where w is the global model parameters and F_k(w) is the training loss function of the kth hospital. Obviously, 0 < F_k^i(w) < 1, and \sum_{k=1}^M F_k^i(w) = 1. Next, we define F(w) as the multiplication of hospitals' relative losses given by

F(w) = \prod_{k=1}^M p_k F_k^i(w), \quad (2)

where p_k is the probability associated with the number of samples of the kth hospital where \sum_{k=1}^M p_k = 1 and p_k specifies the amount of samples of the kth hospital in loss function. We consider p_k = \frac{n_k}{n} in our experiments.

To establish fairness, we need to maximize F(w). To make the optimization problem more computationally convenient, we take the log of both sides of (2) to convert the multiplication to summation. Since the log function is strictly increasing, this conversion does not change the optimal solution. Therefore, (2) will be rewritten as

\begin{aligned} \log(F(w)) &= \log \left( \prod_{k=1}^M p_k F_k^i(w) \right) \\ &= \sum_{k=1}^M \log(p_k F_k^i(w)) \end{aligned} \quad (3)

and the optimization problem at the central server will be

\begin{aligned} \max_w \quad & \sum_{k=1}^M \log(p_k F_k^i(w)), \\ \text{s.t.} \quad & F_k^i(w) = \frac{F_k(w)}{\sum_{j=1}^M F_j(w)}. \end{aligned} \quad (4)

The maximum operator in (4) does not aim to increase the amount of loss functions. Since \sum_{k=1}^M F_k^i(w) = 1, the maximization problem cannot violate this constraint and increase the loss functions. Instead, the maximum of F(w) occurs when all hospitals approach the same relative loss while the summation of the relative losses is 1. In other words, the optimal solution of (4) happens when F_k^i(w) = \frac{1}{M}. We have provided the proof for that in Appendix A. This means all M hospitals achieve the same training loss, F_1(w) = F_2(w) = \dots = F_M(w), which is the ultimate goal of Prop-FFL.

We make the proportional fairness optimization problem (4) clear by two examples. Figure 1, illustrates the function plot of (3) when M = 2. \log(F_1(w)) + \log(F_2(w)) where F_1(w) + F_2(w) = 1. As can be seen, the maximum occurs when both participants get the same portion of 1, meaning F_1(w) = F_2(w) = 0.5. As another example, consider 4 hospitals that collaborate in the federated learning fashion. Using the proposed proportional fairness, each of those four hospitals would fairly contribute to learning the global model, achieving the same relative loss F_1(w) = 0.25, 1 \leq k \leq 4.

The optimization problem in (4) can be simplified as

\begin{aligned} \max_w \quad & \sum_{k=1}^M \log(p_k F_k^i(w)) = \min_w \quad \sum_{k=1}^M -\log(p_k F_k^i(w)) \\ & = \min_w \quad \sum_{k=1}^M -\log \left( p_k \frac{F_k(w)}{\sum_{j=1}^M F_j(w)} \right) \end{aligned}

---

<!-- Page 5 -->

1986

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

Fig. 1. The function plot of (3) when M = 2 and p_1 = p_2 = 0.5. The max of \log(F_1) + \log(1 - F_1) happens in F_1 = 0.5. This means that the maximum occurs when both hospitals achieve the same relative loss, F_1 = F_2 = 0.5.

\begin{aligned} &= \min_w \sum_{k=1}^M \log \left( \frac{1}{p_k} \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right) \\ &= \min c + \sum_{k=1}^M \log \left( \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right), \end{aligned} \quad (5)

where c = \sum_{k=1}^M \log \left( \frac{1}{p_k} \right) is a constant. Since c is not a function of w, we can omit that from the objective function. Therefore, the objective function is

\min_w \mathcal{L}(w) = \sum_{k=1}^M \log \left( \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right) \quad (6)

G_k(w)

For notation simplicity, we define G_k(w) as

G_k(w) = \log \left( \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right)

The optimization problem in (6), applies only fairness and adjusts the model's parameters such that all the hospitals get the same relative loss. This objective function does not intend to decrease the training loss. To reduce the training loss, we adopt the objective function \mathcal{Q}(w) from [20]:

\min_w \mathcal{Q}(w) = \sum_{k=1}^M \frac{1}{q+1} F_k^{q+1}(w) \quad (7)

where q is a constant that will be tuned in our experiments, and F_k(w) is the training loss function of the kth hospital. Our final objective function that reduces the total training loss while imposes fairness is a union combination of objective functions (7) and (6) as follows:

\begin{aligned} w^* = \arg \min_w & \left( 1 - \lambda \sum_{k=1}^M \frac{1}{q+1} F_k^{q+1}(w) \right. \\ & \left. + \lambda \sum_{k=1}^M \log \left( \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right) \right) \end{aligned} \quad (8)

term I: \mathcal{L}(w)                      term II: \mathcal{L}(w)

The first term in (8), term I, aims to reduce the total loss. The second term in (8), term II, applies proportional fairness among participants, forcing relative losses to be close to each other. The hyperparameter 0 < \lambda < 1 adjusts the level of fairness in our objective function.

Since term I and term II in (8) are differentiable and smooth, the optimization problem (8) can be solved by adopting the stochastic gradient descent (SGD). To apply SGD, we need to compute the derivative of the objective function with respect to w. The derivative of \mathcal{Q}(w) with respect to w is

\nabla \mathcal{Q}(w) = \sum_{k=1}^M F_k^q(w) \nabla F_k(w) \quad (9)

and derivative of \mathcal{L}(w) with respect of w can be given as

\nabla \mathcal{L}(w) = \sum_{k=1}^M \nabla G_k(w) \quad (10)

where \nabla G_k(w) is

\begin{aligned} \nabla G_k(w) &= \nabla \log \left( \frac{\sum_{j=1}^M F_j(w)}{F_k(w)} \right) \\ &= \frac{\sum_{j=1}^M (F_k(w) \nabla F_j(w) - \nabla F_k(w) F_j(w))}{\sum_{j=1}^M F_k(w) F_j(w)} \end{aligned} \quad (11)

Finally, given the gradients in (9), (10), and (11), the gradient of the objective function (8) can be formulated as

\Delta = \sum_{k=1}^M (1 - \lambda) F_k^q(w) \nabla F_k(w) + \lambda \nabla G_k(w) \quad (12)

The gradient in (12) allows us to aggregate the updates from all hospitals in a proportional fair setting using SGD, estimating the directions to update the model parameters.

#### B. Proportionally Fair Federated Learning: Prop-FFL

Similar to FedSGD, in Prop-FFL, participating hospitals train the global model using one batch of their local training data. Next, each hospital feeds back the loss function and the gradient of the loss function to the central server. Finally, relying on Prop-FFL, the central server aggregates the training results, updating the model parameters. These steps are repeated until convergence. More details of Prop-FFL have been provided in Algorithm 2.

#### IV. EVALUATION

In this section, we present the experimental results of the proposed Prop-FFL. The effectiveness of Prop-FFL has been verified on four publicly available datasets.

---

<!-- Page 6 -->

HOSSEINI 
*et al.*
: PROPORTIONALLY FAIR HOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1987

**Algorithm 2**
 Proposed Proportionally Fair Federated Learning

**Input:**
 
M
, 
T
, 
w^0
, 
\eta
, 
\lambda

**Output:**
 
w^{T+1}

1. 1: fort = 0,1,\dots,T - 1do
2. 2: Server sendsw^tto all hospitals
3. 3: Each hospitalkcomputesF_k(w^t)and\nabla F_k(w^t)for one batch of data
4. 4: Hospitals sendF_k(w^t)&\nabla F_k(w^t)back to server
5. 5: Server computes\nabla G_t(w^t)based on (11)
6. 6: Server updatesw^{t+1}as

\Delta_k^t = (1 - \lambda) F_k^G(w^t) \nabla F_k(w^t) + \lambda \nabla G_t(w^t)

w^{t+1} = w^t - \eta \sum_{k=1}^M \Delta_k^t

7: end for

8: return 
w^{T+1}

TABLE ISUMMARY OF DATASETS

| Dataset | # Participants | # Samples |
| --- | --- | --- |
| MNIST (non-medical) | 10 | 60,000 |
| FMNIST (non-medical) | 10 | 60,000 |
| Histopathology-Kidney | 4 | 642,277 |
| Histopathology-Lung | 6 | 303,053 |

**A. Image Datasets**

In this section, we provide detailed explanations on the datasets that have been used in our experiments. We study Prop-FFL on two histopathology datasets. Also, we provide additional experimental results on two non-medical datasets to confirm the effectiveness of the proposed method for well-known datasets. The statistical summary of all four datasets has been provided in Table I. In all datasets, data has been divided into 60%, 20%, 20% groups, for training, validation, and testing, respectively. Additional details of datasets and models used in our experiments are described below.

1) MNIST: This dataset is a well-known and widely collected of hand-written digits. The images are black and white of size 28 \times 28 pixels [25]. To investigate the behaviour of our proposed federated learning method, we consider 10 participants in MNIST with non-IID dataset. However, we adopted the approach in [4] to distribute data samples between participants in a non-IID fashion. We first sort data samples based on the digit labels, dividing it into 20 shards of size 3,000 samples each, and then randomly assign 2 shards to each of 10 participants. This partitioning provides us with non-IID data distribution as participants mostly have two digits. For the classification model, we consider a convolutional neural network (CNN) with two 5 \times 5 convolutional layers, each followed with 2 \times 2 max pooling and ReLU activation function. Then, we used two fully connected layers with the first one being output by the ReLU activation and the second one by a softmax output layer.

2) FMNIST: This dataset comprises of size 28 \times 28 images from fashion products. They are gray scale and from 10 fashion categories [26]. To study the federated learning on FMNIST, we have considered 10 participants. The data distribution approach is exactly the same as what we established for MNIST previously. The classifier is also the same as what we have used for MNIST.

3) Histopathology Datasets: For final experiments, we employed the Cancer Genome Atlas (TCGA) [27], [28], the largest public cancer histopathology whole-slide images (WSIs). TCGA provides researchers with more than 30,000 H&E stained histopathology WSIs prepared by various medical centers. In TCGA, the variation between hospitals' data occurs in many different aspects. Figure 2 and Table II present sample patches from four different hospitals of kidney dataset [29] and six different hospitals of lung histopathology dataset [17] respectively. As can be seen, staining can differ significantly among hospitals depending on staining protocols. Additionally, images from different hospitals can have various artifacts that might be characteristic for each hospital. For example, as Figure 2c shows there is a blue ink in the image. Other hospitals might have other artifacts, such as blur, tissue-fold, tears depending on their tissue preparations, imaging protocols, and scanners. While common artifacts are unavoidable during histopathology slide preparation, we propose a protocol that has a quality control unit and the images have an acceptable quality level that machine learning models can access. This assumption is not specific to our method. It is a very general assumption in machine learning that data is reliable with acceptable quality for learning tasks. Only a few studies have looked at the behavior of a deep model in presence of artifacts. However, the laboratory practice at different sites may make the quality control a more urgent need [30], [31], [32]. Those artifacts, as well as different tissue preparation protocols, stain variation, label distribution variability across sites, and using different scanners and protocols may cause non-IID data distribution among hospitals. As recent investigations have reported "normalization and augmentation do not prevent models from learning site-specific characteristics", which cause non-IID challenges, although stain normalization may help increase the accuracy [13], we propose to cope with non-IID data distribution of participant hospitals in a federated learning scenario. We validate the performance of Prop-FFL for the classification of histopathology images of different hospitals using two histopathology datasets, kidney and lung histopathology datasets. Lung and kidney datasets are publicly available in TCGA data base with assigned primary diagnoses as labels for the entire image [27].

- •Kidney Dataset[29]. The WSIs diagnosed withkidney cancerhave been selected from TCGA to construct a dataset of several subtypes. The kidney cancer includes three most frequent subtypes, namely

- – Clear cell renal cell carcinomas (ccRCC),
- – Papillary renal cell carcinomas (pRCC),
- – Chromophobe renal cell carcinomas (crRCC).

---

<!-- Page 7 -->

1988

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

(a) MD Anderson. (b) MSKCC. (c) Int. Genomics Consortium. (d) NCI Urologic Oncology.

Fig. 2. Histopathology patch samples from each of the four hospitals in kidney datasets.

(a) MD Anderson. (b) MSKCC. (c) Int. Genomics Consortium. (d) NCI Urologic Oncology. (e) NCI Urologic Oncology. (f) NCI Urologic Oncology.

Fig. 3. Histopathology patch samples from each of the four hospitals in lung datasets.

Only diagnostic WSIs scanned at a magnification of 40x have been considered from TCGA. This study included hospitals that had a sufficient number of WSIs spanning across all three subtypes (ccRCC, pRCC, crRCC). Only four hospitals met this requirement in TCGA, namely NCI Urologic Center, International Genomics Center, MSKCC, and MD Anderson. Since WSIs are extremely large with high magnification, they have been divided into small patches for further analysis [34]. We refer readers to [29] for more details on how patches have been extracted from WSIs in this dataset. Table. II represents the number of WSIs and patches of each hospital in kidney histopathology dataset and Figure 5 shows the distribution of kidney cancer sub-types in each hospital. For the kidney classification model, we first employed the

pretrained DenseNet121 [35] to extract image features of length 1,024. We have used DenseNet121 weights pre-trained on the ImageNet image dataset with no further modification. Next, we used a fully connected layer followed by ReLU activation function. Then, we applied three fully connected layers followed by softmax output layer.

• Lung Dataset [17]. This dataset includes TCGA WSIs diagnosed with non-small cell lung cancer (NSCLC) which has two frequent subtypes, namely

- – Lung Adenocarcinoma (LUAD)
- – Lung Squamous Cell Carcinoma (LUSC).

In TCGA, there are only six hospitals that have a sufficient number of WSIs from both LUAD and LUSC

---

<!-- Page 8 -->

HOSSEINI et al.: PROPORTIONALLY FAIR HOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1989

Fig. 4. The distribution of the classes in lung dataset.

Fig. 5. The distribution of the classes in kidney dataset.

| Client | # Slides | # Patches |
| --- | --- | --- |
| C1: MD Anderson Cancer Center | 95 | 138,966 |
| C2: International Genomics Consortium | 87 | 60,149 |
| C3: MSSCC | 198 | 245,041 |
| C4: NCI Urologic Oncology Branch | 44 | 198,101 |

subtypes. The statistics of this dataset for each hospital are presented in Table III and Figure 4. Since WSIs are extremely large, they have been divided into patches of size 1000 × 1000 pixels. We refer readers to [17] for more details on patch extraction and selection. For the classification of lung histopathology WSIs, we first employed pretrained DenseNet121 [35] to extract image features of length 1,024. The pre-trained weights on the ImageNet image dataset for DenseNet121 have been used with no additional adjustment. Next, we employed attention gated multiple instance learning (MIL) to combine the patch feature vectors of each WSI and create a feature of size 1,024 for each WSI [36]. Due to space limitations, we refer readers to [36] for more detail about this MIL network. Next, we used a fully connected layer followed by ReLU activation function. Finally, we applied three fully connected layers followed by softmax output layer. We have used patch-level diagnosis for the kidney dataset and slide-level diagnosis for the lung dataset. There are two reasons why we have used patch-level for one and

TABLE IIITHE SUMMARY OF LUNG HISTOPATHOLOGY DATASET [17]

| Client | # Slides | # Patches |
| --- | --- | --- |
| C1: International Genomics Consortium | 267 | 66,483 |
| C2: Indivumed | 211 | 52,539 |
| C3: Astound | 207 | 51,543 |
| C4: Johns Hopkins | 199 | 49,551 |
| C5: Christiana Healthcare | 225 | 55,507 |
| C6: Rowell Park | 110 | 27,390 |

slide-level for the other. First, we used datasets introduced in the literature and a similar classifier for each. For example, many authors use a MIL classifier for the kidney dataset that trains the network based on the slide-level annotation. However, some authors have used another classifier for the lung dataset, which trains the classifier on patch bases. The second reason is that the number of slides in the fourth hospital in the kidney dataset is insufficient to perform the slide-level evaluation. However, we have enough slides in each hospital in the lung dataset to report slide-level performance.

### B. Impact of\lambda.

Our final loss function is a convex combination of two loss functions in (8), one to reduce the loss in the other one to apply fairness. The parameter 0 \leq \lambda < 1 in (8) determines the weight of each of those two loss functions. We now want to investigate the impact of \lambda on the performance. Figure 6 depicts the training loss and testing accuracy vs. \lambda using training and validation datasets, respectively. The results are obtained after 100 epochs of training. The learning rate and q in (8) have been tuned for each dataset to gain the highest accuracy on the validation dataset. This study provides us with insight into the behaviour of Prop-FL as well as with the default value of \lambda in order to enable full automation. According to Figure 6, \lambda = 0.6 has an acceptable performance on all datasets. Therefore, we considered \lambda = 0.6 as the default value for all experiments in the next section. \lambda = 0.6 means that more focus is on part of the loss function that applies fairness, \lambda = 0.6 means that more focus is on part of the loss function that applies fairness. However, since the nature of the data, data distribution, the number of clients, etc are different between datasets, to gain the best possible performance we also tune this parameter specifically for each dataset. This will result in better performance compared to the default value.

According to Figure 6, as expected, large \lambda values (\lambda \rightarrow 1) degrades the performance. The reason is that \lambda \rightarrow 1 diminishes term \ln(1) in (8) only with term II as the objective function. Since term II in (8) applies only proportional fairness and cannot guarantee the decrease of the training loss, the results for \lambda \rightarrow 1 are rather undesirable. For small \lambda values (\lambda \rightarrow 0) the performance is better than large \lambda values. The reason is that \lambda \rightarrow 0 reduces the objective function in (8) to term I which decreases training loss. Therefore, since it guarantees the training loss reduction, its performance is more acceptable compared to \lambda \rightarrow 1.

---

<!-- Page 9 -->

1990

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

Figure 6 consists of three subplots labeled (a), (b), and (c).
  (a) Average training loss vs. λ: The y-axis is 'Training loss' from 0.5 to 1.1. The x-axis is λ from 0 to 1.0. Four lines represent different datasets: Histopathology-Kidney (blue), Histopathology-Lung (green), MNIST (red), and TNNIST (black).
  (b) Training loss of worst hospital: The y-axis is 'Training loss' from 0.6 to 1.4. The x-axis is λ from 0 to 1.0. The same four datasets are shown.
  (c) Average accuracy vs. λ: The y-axis is 'Testing accuracy' from 0.4 to 1.0. The x-axis is λ from 0 to 1.0. The same four datasets are shown.

Fig. 6. Impact of λ on training loss and accuracy.

Figure 7 consists of five subplots labeled (a) through (e).
  (a) TA of all users: Training loss vs. #Rounds (0 to 200).
  (b) TA of the worst user: Training loss vs. #Rounds (0 to 200).
  (c) standard deviation of all TLs: Standard Deviation vs. #Rounds (0 to 200).
  (d) TA of the worst user: Testing accuracy vs. #Rounds (0 to 200).
  (e) standard deviation of all TAs: Standard Deviation vs. #Rounds (0 to 200).
  All plots compare FedSGD (yellow), q-FedSGD (red), Prop-FFL 0.7 (blue), and Prop-FFL 0.6 (green).

Fig. 7. Evaluation on MNIST dataset with Non IID data distribution. The results for Prop-FFL have been provided for λ = 0.6 and the best λ. (TL= training loss, TA=average training loss), TA= testing accuracy, TĀ=average testing accuracy).

TABLE IV

THE ACCURACY OF EACH HOSPITAL IN EACH METHOD FOR KIDNEY DATASET

| Hospitals | Ho1 | Ho2 | Ho3 | Ho4 | Ho5 | Var |
| --- | --- | --- | --- | --- | --- | --- |
| FedSGD | 71.23 ± 0.12 | 72.01 ± 0.04 | 66.87 ± 0.11 | 82.41 ± 0.08 | 32.54 |   |
| q-FedSGD | 76.94 ± 0.36 | 76.78 ± 0.63 | 75.92 ± 0.71 | 83.80 ± 0.45 | 11.22 |   |
| Prop-FFL | 78.84 ± 0.83 | 77.12 ± 0.58 | 76.21 ± 0.56 | 84.36 ± 0.35 | 10.00 |   |

TABLE V

THE ACCURACY OF EACH HOSPITAL IN EACH METHOD FOR LUNG DATASET

| Hospitals | Ho2 | Ho3 | Ho4 | Ho5 | Ho6 | Var |
| --- | --- | --- | --- | --- | --- | --- |
| FedSGD | 66.22 ± 0.02 | 58.06 ± 0.01 | 50.14 ± 0.01 | 74.19 ± 0.01 | 71.20 ± 0.02 | 40.13 ± 0.001 |
| q-FedSGD | 66.68 ± 1.14 | 73.16 ± 1.52 | 62.74 ± 1.57 | 72.63 ± 1.95 | 70.90 ± 1.82 | 59.70 ± 2.08 |
| Prop-FFL | 72.23 ± 1.27 | 76.81 ± 0.59 | 74.57 ± 1.41 | 74.60 ± 0.93 | 76.44 ± 1.62 | 60.81 ± 1.82 |
|   |   |   |   |   |   | 29.84 |

## C. Experiments and Results

Without loss of generality, we assume that all hospitals/users can participate in learning the global model without having any delay and network issue. According to our study in Section IV-B, λ = 0 provides us with acceptable performance on all four datasets (medical and non-medical). Therefore, all results for Prop-FFL have been reported for λ = 0.6 as

well as for the best performing λ in each case. The latter requires additional computational overhead to identify the best lambda value for each dataset. We compare Prop-FFL with two other benchmark methods, FedSGD and q-FedSGD [20]. Learning rate and parameter γ have also been fine tuned to get the best performance for each method. In our experiments, we have added 10-10 to the input of the log function to prevent occurrence of undefined value in logarithmic function.

---

<!-- Page 10 -->

HOSSEINI et al.: PROPORTIONALLY FAIR FAIRHOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1991

Fig. 8. Evaluation on MNIST dataset with Non IID data distribution. The results for Prop-FFL have been provided for \lambda = 0.6 and the best \lambda. (TL= training loss, TL=average training loss), TA= testing accuracy, TA=average testing accuracy).

Fig. 9. Evaluation on Histopathology-kidney dataset. The results for Prop-FFL have been provided for \lambda = 0.6 and the best \lambda. (TL= training loss, TL=average training loss), TA= testing accuracy, TA=average testing accuracy).

As shown in Figure 7 and 8, the training has converged for the general datasets, MNIST and FMNIST, as the training loss and testing accuracy have reached stable behavior. Our method could gain better final accuracy as well as a faster convergence rate compared to other methods. For histopathology datasets, our method exhibits faster convergence, although due to time considerations, we had stopped the training after 300 rounds of weight adjustments. In Figure 7, we evaluate the performance of Prop-FFL on MNIST dataset. The figures in the first and second row demonstrate the performance in terms

of training loss and testing accuracy, respectively. We used batch of size 1024, \lambda = 0.7 was the best value for MNIST dataset. Therefore, we have represented the results for both \lambda = 0.7 and the default value \lambda = 0.6. Figure 7a and 7b represent the average training loss and the worst training loss of ten participants, respectively. Both q-FedSGD and Prop-FFL outperform FedSGD in these two figures. Prop-FFL performs better than q-FedSGD specially in Figure 7b. The standard deviation of training loss of all ten participants has been shown in Figure 7c. As can be seen, Prop-FFL and

---

<!-- Page 11 -->

1992

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

Figure 10 consists of six subplots arranged in a 2x3 grid, labeled (a) through (f). Each subplot shows a different performance metric over 200 rounds for three methods: FedSGD (red line), q-FedSGD (green line), and Prop-FLL with \lambda = 0.6 (yellow line). Shaded regions around the lines indicate variance.

- (a) TL over all hospitals: Training loss vs. #Rounds. FedSGD and q-FedSGD show lower loss than Prop-FLL.
- (b) TL of the worst hospital: Training loss vs. #Rounds. FedSGD and q-FedSGD show lower loss than Prop-FLL.
- (c) TL variance of all hospitals: Standard deviation vs. #Rounds. FedSGD and q-FedSGD show lower variance than Prop-FLL.
- (d) TA of all hospitals: Training accuracy vs. #Rounds. FedSGD and q-FedSGD show higher accuracy than Prop-FLL.
- (e) TA of the worst hospital: Training accuracy vs. #Rounds. FedSGD and q-FedSGD show higher accuracy than Prop-FLL.
- (f) TA variance of all hospitals: Standard deviation vs. #Rounds. FedSGD and q-FedSGD show lower variance than Prop-FLL.

Fig. 10. Evaluation on Histopathology Lung dataset. The results for Prop-FLL have been provided for \lambda = 0.6. (TL= training loss, TL=average training loss), TA= testing accuracy, TA=average testing accuracy).

q-FedSGD perform close and better than FedSGD. Figure 7d and 7e depicts the average testing accuracy and the worst testing accuracy of all ten participants, respectively. As can be seen, Prop-FLL outperforms q-FedSGD. They both surpass FedSGD. Figure 7f represents the standard deviation of testing accuracy of all users. As can be seen, Prop-FLL is slightly better than q-FedSGD and both outperform FedSGD. Figure 8 represents the performance of Prop-FLL on FMNIST dataset. All experimental considerations are similar to what we have done in FMNIST in Figure 7. For FMNIST dataset, Prop-FLL has its best performance for \lambda = 0.8. Therefore, the results have been depicted for both \lambda = 0.6, 0.8.

Figure 9 depicts the performance evaluation on histopathology-kidney dataset. The best performing \lambda on this dataset is \lambda = 0.1. Therefore, the results have been provided for \lambda = 0.1, 0.6. We used batch of size 1024 for this dataset. Figure 9a represents the average training loss of all four hospitals, and Figure 9d represents the average testing accuracy of all four hospitals. As can be seen, Prop-FLL and q-FedSGD outperform FedSGD. The reason is that both Prop-FLL and q-FedSGD performance exceeds FedSGD. The reason is that the objective function does not allow poor performance for any hospitals. 9c and 9f depict the standard deviation of training loss and testing accuracy of all hospitals, respectively. As illustrated, the standard deviation of Prop-FLL is smaller than q-FedSGD, and both smaller than FedSGD. The reason is that q-FedSGD and Prop-FLL have modified the objective function, encouraging a fair

model to decrease the performance variation across hospitals. Figure 10 shows the performance on histopathology-lung dataset. The best performing \lambda on this dataset is same as the default value for \lambda. Therefore, the results have been depicted for only \lambda = 0.6. We also used batch size of 72 for this dataset. As shown, the performance of Prop-FLL is better than q-FedSGD and FedSGD by large margin in this dataset compared to histopathology-kidney dataset. Also, FedSGD have poor performance on this dataset. One possible reason for it might be the number of hospitals which is larger in lung dataset. Table IV and V represent the test accuracy per hospital for kidney and lung datasets, respectively. The results have been provided by taking an average over five independent experiments. As can be seen, Prop-FLL provides us with more uniform testing accuracy over participant hospitals as the variance of the testing accuracy of hospitals in Prop-FLL is less than the other two methods.

The communication overhead of Prop-FLL and q-FedSGD is the same as FedSGD since both have been built on top of the FedSGD. The only difference between these three methods is the aggregation rule at the central server, which does not impact the communication overhead. We have applied Prop-FLL on FedAvg. The results are presented in Appendix B. As can be seen, the concept of fairness does not change the FedAvg performance. This result was expected as averaging moves toward the same results for all hospitals, whereas fairness does emphasize individual contributions. Although FedAvg can improve communication overhead as hospitals do not need to communicate with the central server for each batch of data, FedSGD approach has moderate communication costs in some situations where participant hospitals have small datasets. The reason is that the communication cost

---

<!-- Page 12 -->

HOSSEINI et al.: PROPORTIONALLY FAIR HOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1993

of FedSGD is proportional to the number of batches of local datasets. As the total number of batches is small when local datasets are small, FedSGD is more communication efficient. Having small datasets is quite common in the real-world medical domain. Therefore, when participant hospitals have small datasets, Prop-FFL can provide us with fairness at tolerable communication costs.

## V. CONCLUSION

In this paper, we addressed the fairness aspect of federated learning among participants. We proposed proportionally fair federated learning or Prop-FFL, to allow all hospitals to fairly contribute in learning the global model. We have explained the intuitions behind our idea and provided the mathematical formulation of Prop-FFL. The effectiveness of Prop-FFL has been demonstrated on two histopathology datasets as well as two non-medical datasets to gain insight into its behavior. The experimental results revealed that the proposed method outperforms other federated approaches. In Prop-FFL, similar to FedSGD, hospitals do not need to update model parameters. In future works, one may modify Prop-FFL such that hospitals would be able to update the model parameters, similar to FedAvg, creating more communication efficient framework. Additionally, we used fixed step size \eta to update model weights. Employing the second-order SGD to estimate the best step size in each iteration would perhaps improve the convergence of the proposed method.

## APPENDIX A

Proof: The optimization problem (4) is concave with a closed form optimal solution [37]. Using product rule of logarithms, we can simplify (4) to following

\max_w \sum_{k=1}^M \log(p_k) + \log(F_k^*(w)),

\text{s.t. } F_k^*(w) = \frac{F_k(w)}{\sum_{j=1}^M F_j(w)}.

Since p_k is not a function of w, we can remove it from the objective function. Also, we replace the constraint above with the hidden constraint \sum_{k=1}^M F_k^*(w) = 1. Therefore, the optimization problem will be simplified to

\max_w \sum_{k=1}^M \log(F_k^*(w)),

\text{s.t. } \sum_{k=1}^M F_k^*(w) = 1.

We solve this optimization problem by employing Lagrangian approach. Let \mu be the Lagrangian multiplier. Then, we can convert the optimization problem to

\min_{w/\mu} \sum_{k=1}^M \log(F_k^*(w)) + \mu \left( \sum_{k=1}^M F_k^*(w) - 1 \right).

Figure 11 consists of four subplots arranged in a 2x2 grid, labeled (a) through (d). All subplots have a y-axis ranging from 0.5 to 1.2 (for a, b, c) or 0.3 to 0.8 (for d), and an x-axis representing '#Rounds' from 0 to 300. Each plot contains three data series: FedAvg (red line), q-FedAvg (blue line), and Prop-FFL-Avg, \lambda = 0.6 (green line).
  (a) TL over all hospitals: Training loss decreases from ~1.1 to ~0.7. Prop-FFL-Avg shows the lowest loss.
  (b) TL of the worst hospital: Training loss decreases from ~1.1 to ~0.65. Prop-FFL-Avg shows the lowest loss.
  (c) TA of all hospitals: Testing accuracy increases from ~0.4 to ~0.75. Prop-FFL-Avg shows the highest accuracy.
  (d) TA of the worst hospital: Testing accuracy increases from ~0.3 to ~0.7. Prop-FFL-Avg shows the highest accuracy.

Fig. 11 Evaluation in FedAvg scenario on Histopathology-Kidney dataset. The results for Prop-FFL have been provided for default \lambda = 0.6. (TL= training loss, TL-average training loss), TA= testing accuracy, TA-average testing accuracy).

---

<!-- Page 13 -->

1994

IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 42, NO. 7, JULY 2023

(a) TL over all hospitals

(b) TL of the worst hospital

(c) TA of all hospitals

(d) TA of the worst hospital

Fig. 12. Evaluation in FedAvg scenario on Histopathology Lung dataset. The results for FedAvg have been provided for default \lambda = 0.6. (TL= training loss, TL-average training loss), TA= testing accuracy, TA-average testing accuracy).

Using first order stationary condition, we get \frac{1}{F''_{\text{Fed}}} = \mu and \sum_{i=1}^M F''_i(w) = 1. This gives \mu = M and F''_{\text{Fed}}(w) = \frac{1}{M}, which is an optimal solution that satisfies all constraints and KKT conditions.

## APPENDIX B

In this section, we validate the performance of the proposed approach on top of the FedAvg. It means we allow hospitals to train the model on their local data multiple times, updating the model repeatedly before sending training results to the central server. The model parameters including \lambda, q_i and learning rate have been tuned for FedAvg to get the best possible performance in each of those three methods. The experimental results have been presented for both histopathology datasets in Fig. 11 and 12. As can be seen in these figures, the results of Prop-FLL are not promising compared to the other two methods. This happens because the fairness loss term is only considered in the central server aggregation and its impact is considerably reduced in FedAvg. However, we believe that modifying local training at each hospital by changing the local loss function can make Prop-FLL suitable for the FedAvg scenario too. This will be left for future works.

## REFERENCES

1. [1] J. Deng, W. Deng, R. Socher, L. J. Li, K. J. Li, and L. Fei-Fei, "ImageNet: A large-scale hierarchical image database," inProc. IEEE Conf. Comput. Vis. Pattern Recognit., Aug. 2009, pp. 248–255.
2. [2] N. Rieke et al., "The future of digital health with federated learning,"NPI Digit. Med., vol. 3, no. 1, pp. 1–7, 2020.
3. [3] G. A. Katsis, M. R. Makowski, D. Rickett, and R. F. Braun, "Secure, privacy-preserving and federated machine learning in medical imaging,"Nature Mach. Intell., vol. 6, pp. 305–311, Jun. 2020.
4. [4] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. Y. Arcas, "Communication-efficient learning of deep networks from decentralized data," inProc. 20th Int. Conf. Artif. Intell. Statist., 2017, pp. 1273–1282.
5. [5] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, "Federated learning: Challenges, methods, and future directions,"IEEE Signal Process. Mag., vol. 37, no. 3, pp. 50–60, May 2020.
6. [6] M. N. Gurcan, L. E. Bouhmani, A. A. Matabushi, N. M. Rajpoot, and B. Yener, "Histopathological image analysis: A review,"IEEE Rev. Biomed. Eng., vol. 2, no. 2, pp. 147–171, Feb. 2009.
7. [7] H. R. Tahaos et al., "Searching images for consensus: Can all remove observer variability in pathology?"Amer. J. Pathol., vol. 191, no. 10, pp. 1702–1708, 2021.
8. [8] A. Z. Tan, H. Yu, L. Cui, and Q. Yang, "Towards personalized federated learning,"IEEE Trans. Neural Netw. Learn. Syst., early access, Mar. 18, 2022, doi: 10.1109/TNN.2022.3164699.
9. [9] I. Y. Chen, P. Szolovits, and M. Ghassemi, "Can AI help reduce disparities in general medical and mental health care?"AMA J. Ethics, vol. 21, no. 2, pp. 167–179, 2019.
10. [10] C. Zhang, Y. Xie, H. Bai, B. Yu, W. Li, and Y. Gao, "A survey on federated learning,"Knowl.-Based Syst., vol. 216, Mar. 2021, Art. no. 106775.
11. [11] Q. Dou et al., "Federated deep learning for detecting COVID-19 lung abnormalities in CT: A privacy-preserving multinational validation study,"NPI Digit. Med., vol. 4, no. 1, pp. 1–11, 2021.
12. [12] C. I. Bercsa, B. Wiedler, S. Ruckes, and S. Albargony, "Federated disanagement representation learning for unsupervised brain anomaly detection,"Nature Mach. Intell., vol. 4, no. 8, pp. 685–695, Aug. 2022.
13. [13] M. J. Sheller et al., "Federated learning in medicine: Facilitating multi-institutional collaborations without sharing patient data,"Sci. Rep., vol. 11, no. 1, pp. 1–12, 2020.

---

<!-- Page 14 -->

HOSSEINI et al.: PROPORTIONALLY FAIR HOSPITAL COLLABORATIONS IN FEDERATED LEARNING

1995

[14] K. V. Sarma et al., “Federated learning improves site performance in federated deep learning without data sharing,” J. Amer. Med. Inform. Assoc., vol. 28, no. 6, pp. 1259–1264, 2021.

[15] D. Yang et al., “Federated semi-supervised learning for COVID region segmentation in chest x-ray using multi-national data from China, Italy, Japan,” Med. Image Anal., vol. 70, May 2021, Art. no. 101992.

[16] T. Bidan, N. Naveh, and S. Albragumi, “FedPit: Semi-supervised peer learning for skin lesion classification,” in Proc. Int. Conf. Med. Image Comput. Comput.-Assist. Intervent., Berlin, Germany: Springer, 2021, pp. 336–346.

[17] M. Adnan, S. Kalra, J. C. Cresswell, G. W. Taylor, and H. R. Tzihooosh, “Federated learning and differential privacy for medical image analysis,” Sci. Rep., vol. 12, no. 1, pp. 1–10, Feb. 2022.

[18] S. Kalra, J. Wen, J. C. Cresswell, M. Volkovs, and H. R. Tzihooosh, “ProxyFL: Decentralized federated learning through proxy model sharing,” 2021, arXiv:2111.11343.

[19] L. Daniel and K. Naraynam, “Congestion control 2: Utility, fairness, and optimization in resource allocation,” in Mathematical Modelling for Computer Networks-Part I. Helsinki, Finland: Univ. of Helsinki, 2013, pp. 1–2.

[20] T. Li, M. Sanjabi, A. Beirami, and V. Smith, “Fair resource allocation in federated learning,” 2019, arXiv:1905.04997.

[21] M. Mohri, G. Syvek, and A. T. Suresh, “Agnostic federated learning,” in Proc. Int. Conf. Mach. Learn., 2019, pp. 4615–4625.

[22] T. Huang, W. Liu, W. Wu, L. He, K. Li, and A. Y. Zomaya, “An efficiency-boosting client selection scheme for federated learning with fairness guarantee,” IEEE Trans. Parallel Distrib. Syst., vol. 32, no. 7, pp. 1555–1564, Jul. 2021.

[23] L. Lyu, X. Xu, Q. Wang, and H. Yu, “Collaborative fairness in federated learning,” in Federated Learning, Berlin, Germany: Springer, 2020, pp. 189–204.

[24] H. Kim and Y. Han, “A proportional fair scheduling for multicarrier transmission systems,” IEEE Commun. Lett., vol. 9, no. 3, pp. 210–212, Mar. 2005.

[25] L. Deng, “The MNIST database of handwritten digit images for machine learning research,” IEEE Signal Process. Mag., vol. 29, no. 6, pp. 141–142, Nov. 2012.

[26] H. Xiao, K. Rasul, and R. Volffrag, “Fashion-MNIST: A novel image dataset for benchmarking machine learning algorithms,” 2017, arXiv:1708.07747.

[27] (2006) The Cancer Genome Atlas Program. [Online]. Available: http://www.cancer.gov/tcga

[28] J. N. Weinstein et al., “The cancer genome atlas pan-cancer analysis project,” Nature Genet., vol. 45, no. 2, pp. 1113–1120, Sep. 2013.

[29] M. Sikarudis, S. Rahmameyan, and H. R. Tzihooosh, “Hospitalization image representation learning in digital pathology,” 2022, arXiv:2204.02404.

[30] A. Janoszyk, R. Zuo, H. Gilmore, M. Feldman, and A. Madabhushi, “HistQoc: An open-source quality control tool for digital pathology studies,” JCO Clin. Cancer Informa., no. 3, pp. 1–7, Dec. 2019.

[31] J. A. Retamero, J. Aneiro-Fernandez, and R. G. del Moral, “Complete digital pathology for routine histopathology diagnosis in a multicenter hospital network,” Arch. Pathol. Lab. Med., vol. 144, no. 2, pp. 251–258, Feb. 2020.

[32] B. Schonig-Marklerka et al., “Quality control stress test for deep learning-based diagnostic model in digital pathology,” Modern Pathol., vol. 34, no. 12, pp. 2098–2108, Dec. 2021.

[33] F. M. Howard et al., “The impact of site-specific digital histology signatures on deep learning model accuracy and bias,” Nature Commun., vol. 12, no. 1, pp. 1–13, Jul. 2021.

[34] L. Hou, D. Samaras, T. M. Kure, J. Gao, J. E. Davis, and H. J. Saltz, “Patch-based convolutional neural network for whole slide tissue image classification,” in Proc. IEEE Conf. Comput. Vis. Pattern Recogniz. (CVPR), Jun. 2016, pp. 2424–2433.

[35] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, “Densely connected convolutional networks,” in Proc. IEEE Conf. Comput. Vis. Pattern Recogniz. (CVPR), Jul. 2017, pp. 4700–4708.

[36] M. Ise, J. Tomczak, and M. Welling, “Attention-based deep multi-task instance learning,” in Proc. Int. Conf. Mach. Learn., 2018, pp. 2127–2136.

[37] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.