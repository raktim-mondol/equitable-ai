

<!-- PAGE 1 -->

Available online at 
[www.sciencedirect.com](#)

**ScienceDirect**

IFAC Paper No. 9.9.26 (2023) 145–156

Papers
Online

CONFERENCE PAPER ARCHIVE

ELSEVIER

## Fairness Evolution in Continual Learning for Medical Imaging

Marina Ceccon
^1^
, Davide Dalle Pezze
^2^
, Alessandro Fabris
^3^
, Gian Antonio Stuto
^1^

^1^
Università degli studi di Milano, Milano, Italy, PD 35197 IT (e-mail: marina.ceccon@unipd.it, gianantonio.stuto@unipd.it)

^2^
Università degli studi di Trieste, Trieste, IT (e-mail: d.dallepezze@unipd.it)

^3^
Università degli studi di Milano, Milano, Italy, PD 34197 IT (e-mail: alessandro.fabris@unis.it)

**Abstract:**
 Deep Learning has advanced significantly in medical applications, aiding disease diagnosis in Chest X-ray images. However, expanding model capabilities with new data remains a challenge. Continual Learning (CL) aims to address. Previous strategies have evaluated CL strategies based on classification performance; however, in sensitive domains such as healthcare, it is crucial to assess performance across socially salient groups to detect potential biases. This study examines how bias evolves across time using domain-specific fairness metrics and how different CL strategies impact this evolution. Our results show that Learning without Forgetting and Pseudo-label achieve optimal classification performance, but Pseudo-label is less biased.

**Copyright © 2023 The Authors. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/)**

**Keywords:**
 Fairness, Continual Learning, Medical Imaging, Bias, Chest X-rays.

### 1. INTRODUCTION

In recent years, Deep Learning (DL) models have been successfully applied to various domains in the medical field, including pathology classification, anatomical segmentation, lesion delineation, image reconstruction, synthesis, registration, and super-resolution (Umnizakova et al., 2023), exhibiting impressive performance across these tasks (Colard et al., 2023).

Despite these advancements, DL models encounter significant challenges when trained on real-world data, especially in dynamic domains such as medical imaging. In these settings, continual updates in the distribution—caused by emerging diseases, new imaging techniques, or shifting patient demographics—can result in substantial distributional shifts (Kumar et al., 2022). Adapting to such changes is critical for model reliability and clinical relevance. However, fine-tuning on new data leads to catastrophic forgetting, where prior knowledge is overwritten (Kirkpatrick et al., 2017). Conversely, retraining models from scratch is often infeasible due to high computational costs and privacy concerns related to storing or accessing old patient data (Dalle Pezze et al., 2023).

Continual Learning (CL) has emerged as a promising solution to this challenge, offering a framework that enables models to adapt to evolving data distributions while preserving prior knowledge. Past studies have explored CL strategies in medical imaging, mainly focusing on optimizing classification accuracy (Akindu and Adebayo, 2022; Leung et al., 2020; Singh et al., 2023). However, in the context of sensitive medical data, accuracy alone is insufficient. It is equally important to assess model fairness, as DL systems may exhibit performance disparities across demographic groups due to protected attributes such as age, gender, and socioeconomic status (Scoyed-Kalantari et al., 2020). These disparities can lead to unequal care or misdiagnosis for vulnerable populations, highlighting the need to incorporate fairness into CL evaluation.

In this study, we analyze the evolution of bias across successive tasks using fairness metrics and investigate how different CL strategies influence bias progression over time. Specifically, we consider a class-imbalanced learning scenario using two widely recognized chest X-ray classification datasets: ChestXpert (CXP) (Irvin et al., 2019) and ChestX-ray14 (NH) (Wang et al., 2017). For both datasets, we construct a stream of five tasks, each involving two or three pathologies, covering 12 total pathologies in CXP and 14 in NH. This setup allows us to study the evolution of classification performance and fairness trends as new datasets are gradually introduced.

Our contributions can be summarized as follows:

- We introduce the analysis of fairness metrics in a CL setting for medical imaging.
- We examine the evolution of bias throughout the task stream using the widely adopted CXP and NH datasets in a class-imbalanced learning scenario.
- We compare the impact of different CL strategies on fairness metrics, highlighting their varying effects on bias mitigation.

Our paper is structured as follows. In Sec. 2, we review the existing literature on CL, algorithmic fairness, and their intersections within the medical domain. Sec. 3 details the considered scenario, along with the metrics and methodologies employed. In Sec. 4, we present and discuss the experimental results. Finally, in Sec. 5, we discuss our findings and outline potential directions for future research.

2405-8963 © 2023 The Authors. This is an open access article under the CC BY-NC-ND license. Peer review under responsibility of International Federation of Automatic Control. 10.1016/j.ifacconf.2023.124205

<!-- PAGE 2 -->

Task 1

Labels: Disease 1, Disease 2

Class 1, Class 2

Task 2

Labels: Disease 1, Disease 2

Class 1, Class 2

Task 3

Labels: Disease 1, Disease 2

Class 1, Class 2

Fig. 1. An example of the Continual Learning setting studied to evaluate fairness in the medical domain. In this setting, the model needs to adapt to the evolving medical knowledge by incorporating newly labeled diseases that appear over time.

## 2. RELATED WORKS

### 2.1 Fairness in the Medical Domain

Machine Learning and Deep Learning models used in real-world decision-making may exhibit bias when handling sensitive attributes (Barocas et al., 2019), potentially leading to discriminatory outcomes for minority groups. To tackle this, fairness has emerged as a field in Artificial Intelligence focused on identifying and mitigating bias to develop fairer models.

Related to Fairness in the medical domain, Seyyed-Kalantari et al. (2020) analyze biases in pathology classifiers trained on chest x-ray datasets, evaluating performance across sex, age, race, and insurance type. Their findings show systematic disadvantages for females, Hispanic patients, Medicaid recipients, and younger patients. Similarly, Zhang et al. (2022) train binary classifiers on MMIC-CXR and ChestX-ray14 to predict the conditions Pneumothorax and Fracture. Their main finding is that while fairness-driven methods improve group fairness, they do so at the cost of reduced performance for all groups. Finally, Weng et al. (2023) investigate bias in deep learning models, hypothesizing that breast tissue classes underexposed lung regions and this reduces model performance. By limiting training to one image per patient, they improve fairness without significantly harming accuracy.

### 2.2 Continual Learning in the Medical Domain

In conventional machine learning, models are trained on static datasets, which can lead to performance degradation when encountering novel data. Continual Learning (CL) addresses this by enabling models to incrementally learn a stream of tasks, though it introduces the challenge of catastrophic forgetting—where performance on earlier tasks deteriorates (Lerer et al., 2020).

In CL, models learn from a sequence of tasks without forgetting prior knowledge, addressing the limitations of static training. CL is typically categorized into Domain Incremental Learning (DIL), where the input distribution shifts but class labels remain the same; Class Incremental Learning (CIL), where new classes appear without task identifiers; and Task Incremental Learning (TIL), where task identifiers are known (Lerer et al., 2020).

Common CL strategies include rehearsal-based methods, which retain samples from past tasks (e.g., Experience Replay (Rohinik et al., 2019); regularization-based methods, which constrain the model to preserve old knowledge (e.g., Learning without Forgetting (Li and Hoiem, 2017)); and architecture-based approaches, which dynamically modify network structure (Rusu et al., 2016).

In the medical domain, machine learning models must often adapt to new knowledge while preserving prior information. Changes in the environment or medical equipment can introduce distribution shifts in input data, affecting model performance (Lenga et al., 2020). Moreover, new diseases may emerge or be retrospectively labeled after initial training (Singh et al., 2023). To address these challenges, researchers explored continual learning (CL) applications in medical settings. Singh et al. (2023) introduce three tasks, in a CIL scenario, covering 12 classes using replay, and Akundi and Sivaswamy (2022) propose a distillation-based method across five sequential tasks. Cocon et al. (2025) further explore a New Instances and New Classes scenario, combining distillation and rehearsal.

### 2.3 Fairness in Continual Learning

Recent research has increasingly addressed fairness within continual learning settings. Truong et al. (2025) propose FALCON, a method that employs contrastive clustering for attention mechanisms to mitigate bias during semantic scene segmentation. Bass Roy Chowdhury and Chattervedi (2025) develop FaRIL, which sustains fairness across sequential tasks by controlling representation compression. Similarly, Chaturani et al. (2023) apply domain-incremental continual learning to facial expression recognition, employing continual adaptation for bias mitigation. Despite these advances, to the best of our knowledge, no prior work has systematically evaluated or compared the fairness performance of continual learning methods on clinical data. This study addresses this gap by benchmarking multiple continual learning algorithms on chest X-ray

<!-- PAGE 3 -->

classification tasks, assessing both predictive accuracy and fairness across demographic subgroups.

### 3. EXPERIMENTAL SETTING

#### 3.1 Considered scenario

We model a medical imaging scenario in which a computer-aided diagnosis system assists specialists in interpreting X-ray scans. The system is continuously updated to accommodate an expanding set of pathologies, with developers adding newly annotated images and organizing them into tasks for sequential improvement.

We consider a Class-Incremental Learning (CIL) setup using the CXpP dataset (Irvin et al., 2019) and the NIH dataset (Wang et al., 2017). As in typical multi-label continual learning (Dalle Pezze et al., 2023), information about previously learned classes is omitted from new tasks, even if they still appear in the images. This mirrors challenges in Object Detection and Semantic Segmentation within Continual Learning (Cernelel et al., 2020).

For both datasets, we define a stream of 5 tasks, each linked to 2 or 3 pathologies. Following prior work in continual object detection (Shmelkov et al., 2017), each task includes only images with at least one relevant pathology. Tasks may contain overlapping images, depending on pathology correlation. We exclude “No Finding” images only, as they are not associated with any pathology. Only one image per patient is included, following evidence that this improves model fairness without substantially harming classification performance (Weng et al., 2023).

#### 3.2 Evaluated methods

We consider several Continual Learning (CL) strategies:

- **Fine-Tuning:**Sequential training on new data without mechanisms for retaining prior knowledge. Typically regarded as the lower CL performance bound.
- **Replay**(Rohinik et al., 2019): We use a 50% mix ratio and a memory buffer size of 3% of the original dataset. Samples are stored and replayed uniformly at random.
- **LoF-LoF**(Li and Hoiem, 2017): Uses the combined lossL = L_{CL} + L_{LoF}, whereL_{CL}handles the current task andL_{LoF}is the distillation loss. We set\tau = 2as in Li and Hoiem (2017).
- **Pseudo-Label**(Guan et al., 2018): For each class, we determine a threshold that maximizes the F1 score on the validation set of its corresponding origin task. The teacher model’s outputs for previously learned classes are then binarized using these class-specific thresholds.
- **LoF-LoF+Replay**: Combines Replay with LoF, using the same hyperparameters and sampling strategy as the individual methods.
- **LoF-LoF+Training:**Trains the model on all tasks simultaneously, assuming access to the full dataset at once. While not a CL method, it serves as an upper-bound baseline, unaffected by the sequential forgetting.

### 3.3 Evaluation metrics

To assess performance, we use ROC AUC, a standard metric for classification tasks. It is computed by plotting the True Positive Rate (TPR) against the False Positive Rate (FPR) across various thresholds. Given the task stream setting, we report the average AUC over all pathologies from all tasks seen up to a given point.

For fairness, we use the Equality of Opportunity (EO) metric, which evaluates TPR disparities across demographic groups. This addresses the problem of underdiagnosis in minority populations (Seyyed-Kalantari et al., 2021), where models often produce lower TPRs for disadvantaged groups. EO for pathology 
i
 (in task 
j
) is defined in Eq. (1), with 
\sigma_i
 as the task’s test set, as 
g
 is the model’s prediction, 
y_i
 the ground truth, 
\theta
 the advantaged group, and 
d
 the disadvantaged group:

EO_i = \frac{TPR_{\theta}(\sigma_i | \theta = \sigma_i, y_i = \oplus)}{TPR_{d}(\sigma_i | \theta = \sigma_i, y_i = \ominus)} \quad (1)

Since it measures a difference in TPRs, we additionally report it to us as TPR gap. We examine fairness across gender and age. Specifically, we compare performance between males and females, and across age groups 0-20, 20-40, 40-60, and 60-80. Males are treated as the advantaged group; for age, patients under 20 are advantaged, while those over 60 are disadvantaged. As with AUC, we compute EO over all tasks seen up to 
j
 and report the average.

### 4. RESULTS

Here, we present the experimental results obtained on the CXpP dataset. The corresponding outcomes for the NIH dataset are summarized in Table 1. While the analysis focuses on the CXpP dataset, the findings generalize to NIH due to the consistency observed across both datasets.

#### 4.1 Analysis on the classification performance

Fig. 2. AUC metric, evaluated on each strategy, averaged over all the pathologies seen so far (CXpP).

As shown in Fig. 2, the model trained with joint training on the CXpP dataset achieves an average AUC of 0.78, comparable to the state-of-the-art (Seyyed-Kalantari et al., 2020). The slight drop may stem from excluding “No Finding” images and limiting the time per patient.

<!-- PAGE 4 -->

Figure 3: Fairness metric results on CXP.

It is important to note that, among the CL methods examined, we focus our analysis of fairness metrics on those demonstrating satisfactory AUC performance—specifically, LwF, Pseudo-Label, and LwF Replay. This focus is justified by the principle that fairness evaluation is meaningful only when the model maintains sufficient accuracy and mitigates catastrophic forgetting. In the case of joint training on the entire dataset, previous studies have shown that models trained on CXP and NIH exhibit bias favoring male patients (Seyyed-Kalantari et al., 2020). In our setting, although the average TPR is still higher for males, the observed gap is smaller—only 0.008. This discrepancy from prior work may result from limiting the dataset to one imbalanced patient, a strategy shown to reduce performance disparities (Weng et al., 2023), as well as from excluding “No Finding” images. While the gap is minimal in this static setting, it remains essential to assess whether this trend holds in the Continual Learning scenario. Fig. 3a shows the EO between male and female patients across all methods, while Fig. 3b presents the TPRs for male and female patients for LwF, Pseudo-Label, and LwF Replay across all tasks. For LwF, potentially the strongest task, male TPRs are consistently higher, resulting in a stronger EO than observed in joint training, potentially indicating underestimation of women. In contrast, for Pseudo-Label, the EO fluctuates across tasks but converges toward zero. Similarly, LwF Replay yields an almost null EO by the end of the task stream.

Fig. 4: Age EO on CXP of all the considered CL strategies.

4.3 Analysis on the Fairness evolution on the age attribute

Lastly, we analyze the performance of the different strategies across the age groups. In Sec. 3.3, on the CXP dataset, joint training shows the highest TPR for the 60–20 group and the lowest for the 60+ group, with a gap of 0.15. Fig. 4 plots this gap across the task stream for all strategies. TPR results for all age groups using the top three methods are shown in Fig. 5.

From the plots we can notice that, considering LwF and Pseudo-Label, after training on all tasks, the TPR is the highest on people younger than 20 and the lowest on people older than 60. Moreover, the two methods display very similar EOs: the difference between the highest TPR and the lowest is around 0.06 for both LwF and Pseudo-Label. When considering the LwF Replay approach, we observe that the final gap is very small, taking the value of 0.023.

4.4 Overall considerations

In Table 1 the results of all strategies on both datasets are reported. Overall, the LwF Replay approach is the best in terms of age gap, however, its suboptimality in terms

<!-- PAGE 5 -->

Marina Cecconi et al. / IJAC: PaperOnline 59:26 (2025) 145–150

149

| Strategy/Metric | CXP Dataset | NIH Dataset |
| --- | --- | --- |
| AUC | Gender EO | Age EO | AUC | Gender EO | Gender EO | Age EO |
| Joint Training | **0.78** | 0.008 | 0.008 | 0.78 | -0.010 | -0.024 | -0.024 |
| Fine-Tuning | 0.55 | 0.002 | 0.014 | 0.57 | 0.016 | -0.115 | -0.115 |
| Reply | 0.60 | -0.013 | 0.005 | 0.60 | -0.022 | -0.005 | -0.005 |
| LoF | 0.68 | 0.028 | 0.000 | 0.65 | 0.013 | 0.040 | 0.040 |
| Pseudo-Label | **0.69** | 0.001 | 0.061 | **0.68** | 0.003 | 0.043 | 0.043 |
| Reply LoF | 0.67 | -0.002 | 0.023 | 0.65 | -0.021 | -0.002 | -0.002 |

(a) TPR of each age group considering the LoF approach.

(b) TPR of each age group considering the Pseudo-Label approach.

(c) TPR of each age group considering the LoF Reply approach.

of classification performance, on both datasets, and the gender EO on the NIH dataset limit its employability. On the other hand, Pseudo-Label performs better in terms of AUC and gender EO, exhibiting a slightly higher value in terms of age EO. In other words, Pseudo-Label exhibits the best combination of results.

It’s worth mentioning that, in the case of the LoF Reply approach, the most favored and disfavored age groups do not correspond to the age EO results of the models resulted from the joint training. Moreover, the gender EO gap favoring males observed in the results of the LoF strategy is not present in the static setting in which the joint model was trained. This further emphasizes the unpredictability of fairness results when considering a CL scenario, hence the need of considering fairness metrics in these settings.

### 5. CONCLUSION AND FUTURE WORK

In this study, we leveraged continual learning (CL) techniques to address the medical image diagnosis problem. Specifically, we explored a class-incremental learning (CL) scenario where new diseases are introduced incrementally and assessed how biases evolve as the model adapts. We observed that traditional approaches like Reply struggle to retain past knowledge, whereas LoF and Pseudo-Label outperform Reply and LoF Reply, with Pseudo-Label showing slightly better overall performance.

We further evaluated the fairness of CL methods by analyzing Equality of Opportunity (EO) between male and female groups, and among different age groups. Results show that Pseudo-Label exhibits the best EO regarding gender, and achieves the highest classification performance while maintaining reasonable fairness across age groups. Conversely, LoF and LoF Reply exhibit greater gender bias and slightly lower AUC values. Thus, Pseudo-Label emerges as a promising CL method for medical image diagnosis, balancing classification performance and fairness.

While our findings are significant, further research is needed to fully understand and mitigate biases in CL applications. Although LoF and Pseudo-Label help reduce forgetting, a considerable performance gap remains compared to static training. Evaluating additional methods will be crucial to improving overall performance while preserving fairness. Moreover, while our analysis focuses on a CL setting, real-world medical applications may involve more complex scenarios worth exploring. As part of future work, we also plan to integrate and systematically evaluate fairness-aware techniques within this continual learning setting, aiming to close the observed gap in performance across demographic groups. Overall, this study serves as

<!-- PAGE 6 -->

```latex
\begin{table}
\caption{Continued from previous page}
\begin{tabular}{p{0.5\textwidth}p{0.5\textwidth}}
\hline
\hline
\textbf{REFERENCES} & \textbf{REFERENCES} \\
\hline
\hline
\begin{minipage}{0.5\textwidth}
\textit{Akundi, P. and Sivaswamy, J. (2022). Incremental learning for an adaptive real-system application. In \textit{2022 IEEE International Symposium on Biomedical Imaging (ISBI)}, 1-4. IEEE.} \\
\textit{Barocas, S., Hardt, M., and Narayanan, A. (2019). Fairness and Machine Learning: Limitations and Opportunities. fairmlbook.org.} \\
\textit{Basu Roy Chowdhury, S. and Chaturvedi, S. (2023). Sustaining fairness in incremental learning. In \textit{Proceedings of the AAAI Conference on Artificial Intelligence}, volume 37, 6797-6805. doi:10.1609/aaai.v37i26.25833.} \\
\textit{Cecconi, F., P. Pezze, D. D'Urso, and S. Susto, G.A. (2025). Multi-label continual learning for the medical domain: A novel benchmark. In \textit{30th IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)}, 7163-7172. doi:10.1109/WACV51041.2025.} \\
\textit{Celad, P., Iglesias, E., Sorribes-Fdez, J., Romero, V., Vieta, A.S., and Borrajo, L. (2023). A survey on continual learning applied to deep learning from small artificial neural networks to generative models. \textit{Neural Computing and Applications}, 35(10), 2291-2323.} \\
\textit{Cermelli, P., Mancini, M., Bubu, S.R., Ricci, E., and Caputo, B. (2020). Modeling the background for incremental learning in semantic segmentation. In \textit{Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition}, 9223-9232. IEEE.} \\
\textit{Chaturvedi, N., Kara, O., and Gunes, H. (2023). Domain-incremental continual learning for mitigating bias in facial expression and action recognition. \textit{IEEE Transactions on Affective Computing}, 14(4), 3191-3206. doi:10.1109/taffc.2023.3317622.} \\
\textit{Dalle Peze, D., D'Urso, J., Masiéro, C., Tosato, A., Bagni, A., and Susto, G.A. (2023). A multi-label benchmark for learning from small data: deep learning approaches for packaging equipment monitoring. \textit{Engineering Applications of Artificial Intelligence}, 124, 106623.} \\
\textit{Guan, L., Wu, Y., Zhao, J., and Ye, C. (2018). Learn to learn with incrementally trained neural networks. \textit{IEEE Intelligent Vehicles Symposium (IV)}, 403-408. IEEE.} \\
\textit{Irvin, J., Rajpurkar, P., Ko, M., Yu, Y., Chute, C.S., Chen, A., Madhavan, A., Hajaj, B., Bhatia, S., Rupakumar, K., et al. (2019). CheXpert: A large chest radiograph dataset with uncertainty labels and expert comparison. In \textit{Proceedings of the AAAI Conference on Artificial Intelligence}, volume 33, 580-591.} \\
\textit{Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A.A., Milan, K., Quan, J., Ramalho, E., Grabska-Barwinska, A., et al. (2017). Overcoming catastrophic forgetting in neural networks. \textit{Proceedings of the national academy of sciences}, 114(13), 3521-3526.} \\
\textit{Kumar, P., Chaudhan, J., Bozorgpour, A., Azad, R., and Hoiem, D. (2020). Learning to learn from a single image: A comprehensive review of recent advancements and future prospects. \textit{arXiv preprint arXiv:2005.17004}.} \\
\end{minipage}
&
\begin{minipage}{0.5\textwidth}
\textit{Lenga, M., Schulz, H., and Saalbach, A. (2020). Continual learning for domain adaptation in chest x-ray classification. In \textit{Medical Imaging with Deep Learning}, 413-423. PMLR.} \\
\textit{Loser, T., Lomovska, V., Stotan, A., Mahoni, D., Filliat, D., and Diederich, M. (2020). Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges. \textit{Information fusion}, 58, 52-68.} \\
\textit{Li, Z. and Hoiem, D. (2017). Learning without forgetting. \textit{IEEE transactions on pattern analysis and machine intelligence}, 40(12), 2935-2947.} \\
\textit{Rolnick, D., Ahuja, A., Schwartz, J., Lillibridge, T., and Wayne, G. (2019). Experience replay for continual learning. \textit{Advances in Neural Information Processing Systems}, 32.} \\
\textit{Rusu, A.A., Babicovitz, N.C., Desjardins, G., Sover, H., Kirkpatrick, J., Rupakumar, K., Pascanu, R., and Hadsell, R. (2016). Progressive neural networks. \textit{arXiv preprint arXiv:1606.04671}.} \\
\textit{Srivastava, R., Hinton, G.E., Krizhevsky, A., Sutskever, I., and Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. \textit{The Journal of Machine Learning Research}, 15(1), 1929-1958.} \\
\textit{Srivastava, R., Hinton, G.E., Krizhevsky, A., Sutskever, I., and Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. \textit{The Journal of Machine Learning Research}, 15(1), 1929-1958.} \\
