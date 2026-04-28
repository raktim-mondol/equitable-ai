<!-- Page 1 -->

Chang et al. Journal of Translational Medicine (2026) 24:108https://doi.org/10.1186/s12967-025-07591-z

Journal of TranslationalMedicine

REVIEW

Open Access

# Applications of artificial intelligence in non-small cell lung cancer: from precision diagnosis to personalized prognosis and therapy

Luyuan Chang1, Haipeng Li2, Wenzong Wu1, Xinyu Liu1, Jiaqi Yan1, Zuo Chen1, Huan Wu2 and Shilong Song1*

## Abstract

Background Non-small cell lung cancer (NSCLC) carries a major global burden. The rapid growth of multimodal medical data challenges conventional methods to deliver stable, transferable and interpretable decisions across heterogeneous longitudinal high dimensional inputs.

Methods This review summarizes advances in artificial intelligence (AI) for NSCLC from 2023 to 2025 and outlines a translation-focused framework that links algorithmic progress to clinical utility. We survey thoracic imaging, digital pathology and multimics together with evaluation practices and implementation guidance. We also adopt a critical perspective.

Results Many high performing deep models remain black boxes, and popular post hoc explanations such as Grad CAM heatmaps are rarely validated for faithfulness or stability, which undermines clinician trust and limits use in high stakes decisions. To address this gap, we propose a minimum evidence package for explainability that comprises sanity checks, quantitative faithfulness tests such as deletion or insertion, ROAR or iROF and infidelity, stability analyses, concept level validation for example TCAV with statistical testing, and prospective human factors studies that demonstrate improved decisions without automation bias. Across modalities, evaluation has expanded beyond discrimination to include calibration, uncertainty quantification (UQ) and subgroup analyses across scanners, sites and populations. However, the evidence base remains constrained by retrospective single center designs, inconsistent external or temporal validation and limited decision curve analysis (DCA). Translational priorities include a staged validation ladder from technical to clinical to prospective deployment, alignment with Software as a Medical Device frameworks, interoperable governance, fairness and economic assessment, and validated explainability coupled with uncertainty aware selective workflows.

Conclusions Looking ahead, progress will depend on multimodal/foundation models, causal and temporal modeling, and regulatory qualification of computable biomarkers with verified explanations, supported by multicenter prospective studies that demonstrate durable generalizability, clinical value and clinician trust.

*Correspondence:Shilong Songshilongsong@bmbw.edu.cn

Full list of author information is available at the end of the article

© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

---

<!-- Page 2 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:1018
Page 2 of 25

Keywords Non-small cell lung cancer (NSCLC), Artificial intelligence (AI), Precision diagnosis, Personalized prognosis, Treatment decision support

## Introduction

Lung cancer remains the leading cause of cancer death worldwide. According to GLOBOCAN 2022, about 2.4 million new cases and 8.2 million deaths occurred globally, making lung cancer ever both highly incident and the leading cause of cancer mortality in many regions [1]. Non-small cell lung cancer (NSCLC) accounts for 80–85% of cases and comprises adenocarcinoma, squamous cell carcinoma, and large-cell carcinoma [2]. Despite advances in early detection, staging, and molecular (LDCT) screening, perioperative immuno-oncology, targeted therapies, and stereotactic radiotherapy, population outcomes remain suboptimal [2–4]. Recent SEER/ACS estimates show an overall 5-year relative survival of about 52% for NSCLC, with pronounced stage gradients: localized about 67%, regional about 40%, and distant about 12% [5]. Poor outcomes reflect late presentation, substantial inter- and intratumoral heterogeneity, and primary or acquired resistance to systemic therapy [6, 7]. These challenges strain traditional diagnostic and prognostic approaches, which struggle to integrate high-dimensional, multimodal information, including imaging, whole-slide histopathology, genomic and transcriptomic profiles, longitudinal clinical data, and environmental exposures, into actionable decisions [8, 9].

Heterogeneity and evolutionary dynamics are central to the biology of NSCLC [6, 7]. Spatially distinct subclones, variable target expression, divergent microenvironmental niches—including inflamed, excluded, and desert phenotypes—and shifting therapeutic selective pressures produce complex response patterns and resistance [10–13]. Environmental exposures, such as tobacco smoke, matter PM2.5, contribute to lung adenocarcinoma, particularly among never-smokers, and interact with molecular drivers such as the epidermal growth factor receptor (EGFR) [14]. This clinical, biological, and environmental heterogeneity motivates methods that learn structure across scales and generate individualized predictions that update over time [8, 15].

Artificial intelligence (AI), particularly machine learning (ML) and deep learning (DL), has progressed from proof of concept to multicenter and early prospective evaluations across oncology workflows [16, 17]. In thoracic imaging, DL systems trained on LDCT and diagnostic CT achieve expert level performance in nodule detection and malignancy risk estimation. They are under prospective evaluation for longitudinal risk prediction in screening cohorts, for example models that predict one to six years of lung cancer risk from a single LDCT [18, 19]. In digital pathology, self-supervised

foundation models and multiple instance learning (MIL) standardize histologic subtyping, quantify immunohistochemistry (IHC) such as the programmed death ligand 1 (PD-L1) tumor proportion score (TPS) with high reproducibility than manual scoring, and increasingly infer actionable biomarkers such as EGFR directly from routine hematoxylin and eosin (H&E) slides [12, 20–22]. Parallel advances in multimodal fusion and representation learning enable integration of radiology, pathology, and genomic data into a unified model for individualized prognosis and treatment selection [8, 23, 24]. Building on these modality-specific gains, we present a unifying framework for multimodal fusion [25]. We define multimodal fusion as the principled integration of imaging, digital pathology, genomics, and clinical data to improve diagnosis, prognosis, and treatment in NSCLC [26]. This review explains how fusion is realized across radiology, pathology, and omics, describes the alignment and aggregation of heterogeneous representations into coherent patient-level embeddings, and shows how fused models are integrated into routine clinical workflows to support decision-making [27]. Throughout, we highlight fusion's contribution to generalization, interpretability, and clinical utility, and we evaluate each application with a consistent toolkit of external validation, calibration, and decision-curve analysis to enable fair, decision-relevant comparisons [28]. At the architectural level, contemporary systems include four major families. First, Transformer backbones use self attention for spatial and contextual integration [29]. Second, temporal and frequency attention, exemplified by Fourier attention (FA) and wavelet attention (WA), enables long-range signal fidelity and multiscale transients in longitudinal imaging and circulating tumor DNA (ctDNA) time series [30–32]. Third, graph neural networks (GNNs) encode pathway and topological constraints for multi-omics integration. Fourth, generative adversarial networks support denoising, super resolution, and stain or style normalization. Together with early prospective evaluations, these trends position AI as a scalable, data-driven layer that augments radiology, pathology, genomics, and clinical decision-making throughout the NSCLC care continuum [16, 33].

A targeted search on PubMed, MEDLINE, Embase, Web of Science, Scopus, and Cochrane CENTRAL identified studies published between 1 January 2023 and 17 August 2025. Search queries combined controlled vocabulary and free-text terms for NSCLC and AI across imaging, digital pathology, multi-omics, prognosis, treatment decision support, and drug discovery. Records were independently screened by two reviewers for relevance to the

---

<!-- Page 3 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 3 of 25

review objectives, with priority given to human NSCLC studies featuring clinically meaningful endpoints and implementation insights. As a narrative review, no pre-registered protocol, formal risk-of-bias assessment, or quantitative synthesis was employed. When necessary to contextualize developments from 2023 to 2025, seminal prior work and select pre-2023 studies were cited. Using this methodology, we review 2023 to 2025 advances across the NSCLC pathway (Fig. 1): precision diagnosis and subtyping using CT, Positron Emission Tomography/Computed Tomography (PET-CT), and Magnetic Resonance Imaging (MRI) radiomics and deep learning [18], as well as whole-slide image biomarker inference [22]; individualized prognosis with multi-omics and multimodal survival models [34]; and decision support for radiotherapy, chemotherapy, targeted therapy, and immunotherapy, together with AI-enabled drug discovery [35]. We also highlight translational requirements, including external validity, calibration, clinical net benefit, fairness, and explainability, and we outline regulatory and workflow-integration considerations [36–38]. Finally, we propose an agenda for trustworthy, interpretable, and equitable deployment [39], including a pragmatic validation ladder and postmarket change-control and recalibration plans.

## Applications of AI in diagnosis and subtyping of NSCLC

### Assisted imaging diagnosis (CT, PET/CT, MRI; radiomics and deep learning)

In thoracic radiology, AI aims to improve sensitivity, specificity, and workflow efficiency in both screening and diagnostic evaluation [34]. Deep learning CNNs trained on chest CT detect and characterize pulmonary nodules, prioritize worklists, and generate quantitative malignancy-risk estimates, which reduces interobserver variability and mitigates reader fatigue in high-volume settings [34–36]. Nodule detection and longitudinal risk stratification are related but distinct tasks [18, 35]. End-to-end 3D CNNs for LDCT screening, exemplified by the 2019 Google system in Nature Medicine, achieved an area under the receiver operating characteristic curve (AUROC) of approximately 0.94 for per-case cancer detection and reduced false positives by about 11% and false negatives by about 5% versus expert readers in retrospective testing [38]. In parallel, the Sybil model, developed and validated across multiple centers and reported in the Journal of Clinical Oncology in 2023, predicts individual one- to six-year lung-cancer risk from a single LDCT without additional clinical covariates. External AUROCs of approximately 0.75–0.81 have been reported,

The diagram illustrates the AI-enabled NSCLC pathway, structured into three main stages and a foundational layer.

- AI achieves precise diagnosis and subtype classification:This stage includes:Imaging techniques such as CT, PET/CT, and MRI:Represented by icons of a CT scanner, a PET/CT scanner, and an MRI machine.Whole slide image:Represented by an icon of a microscope and a slide.Deep Learning:Represented by a neural network icon.Biomarker:Represented by an icon of a DNA helix and a protein structure.
- Imaging techniques such as CT, PET/CT, and MRI:Represented by icons of a CT scanner, a PET/CT scanner, and an MRI machine.
- Whole slide image:Represented by an icon of a microscope and a slide.
- Deep Learning:Represented by a neural network icon.
- Biomarker:Represented by an icon of a DNA helix and a protein structure.
- AI building personalized prognosis prediction:This stage includes:Multi-omics analysis:Represented by icons of DNA, protein, and metabolite structures.Multimodal Survival Model:Represented by a line graph showing survival probability over time.
- Multi-omics analysis:Represented by icons of DNA, protein, and metabolite structures.
- Multimodal Survival Model:Represented by a line graph showing survival probability over time.
- AI-assisted decision support:This stage includes:AI provides decision support for radiotherapy, chemotherapy, targeted therapy, and immunotherapy:Represented by icons of a radiation therapy machine, a chemotherapy bag, a targeted therapy pill, and an immunotherapy antibody.
- AI provides decision support for radiotherapy, chemotherapy, targeted therapy, and immunotherapy:Represented by icons of a radiation therapy machine, a chemotherapy bag, a targeted therapy pill, and an immunotherapy antibody.

Below these stages is a foundational layer titled Building a trustworthy, explainable, and fair NSCLC diagnosis and treatment system, which includes five key components:

- External validity:Represented by an icon of a hospital building.
- Calibration accuracy:Represented by an icon of a ruler.
- Clinical net benefit:Represented by an icon of a line graph.
- Fairness and Interpretability:Represented by an icon of a balance scale.
- Compliance and Integration:Represented by an icon of interlocking gears.

Fig. 1 AI-enabled NSCLC pathway for precise diagnosis, personalized prognosis and clinical decision support

---

<!-- Page 4 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 4 of 25

and such models can inform interval scheduling and escalation pathways for high-risk individuals [18].

In addition to detecting cancer, DL enhances the segmentation of tumors and organs-at-risk, facilitating volumetry, growth-kinetics modeling, and radiotherapy planning [37, 39]. In PET-CT, AI aids in mediastinal staging, such as classifying nodal involvement with AIJROCS around a 90° bin and detecting occult metastases. In MRI, which is less commonly used for thoracic cancers, AI supports brain-metastasis surveillance and target-volume delineation [40–43]. Denoising and super-resolution techniques based on learning further enhance low-dose image quality, preserving quantitative imaging features [44, 45].

Methodologically, comparisons between radiomics and deep learning recur in thoracic oncology [46]. Hand-crafted radiomics extracts shape, intensity, and texture features to infer phenotypes and biomarker surrogates such as histology. EGFR status and invasiveness, yet it is sensitive to heterogeneity in slice thickness, reconstruction kernel, vendor, and to feature engineering choices [46, 47]. Accordingly, pipelines aligned with the Image Biomarker Standardisation Initiative (IBSI) should explicitly document voxel resampling with isotropic 1.0 mm, intensity discretization around a fixed bin size or number, pre filters such as Laplacian of Gaussian (LoG) radii, and the exact feature set; releasing code and parameter files enables independent reproducibility. By contrast, deep learning leverages voxel level signals and peritumor context and often outperforms classical models when trained on diverse, harmonized datasets; however, both paradigms require external validation, calibration, and decision curve analysis (DCA) to demonstrate clinical utility [28, 48, 49] (Table 1). To carry these methods into practice, external validation and calibration must follow disciplined processes including data harmonization, documentation, practical guidance. Lock the full analysis pipeline before any testing begins [52]. Select cohorts that are both geographically and temporally external and that span multiple vendors and protocols. Fit all preprocessing on development data only and apply it unchanged to the external cohort. Split at the patient level and keep

sites and scanners separated to prevent leakage from acquisition signatures [53]. Report discrimination, calibration, and clinical utility together, and provide group results by site, scanner, sex, age, ancestry, stage, and smoking status. See section “Validation, regulation, and workflow integration” for detailed checklists and sample size targets.

Domain shift remains a central challenge for deployment [54]. Performance on external cohorts often falls relative to internal testing because of protocol and population differences, and decreases of about 5 to 10 AUROC points are common across centers [55, 56]. Mitigation strategies include, first, multi domain training across vendors [58, 59], and fourth, using strong data augmentation combined with physics informed harmonization such as ComBat and kernel aware resampling [47, 50, 57]; third, out of distribution (OOD) detection with case level uncertainty estimation to flag low reliability outputs [58, 59], and fourth, using adaptation or augmentation to stabilize predictions at deployment. At a minimum, reports should include internal and external validation splits, calibration curves, and error analyses stratified by scanner vendor, slice thickness, reconstruction kernel, geography, sex, age, and smoking status [60]. Section “Validation, regulation, and workflow integration” provides a document that should use a locked pipeline [61], apply preprocessing learned on development data without modification, and adopt patient splits that are separated by site and scanner, while reporting discrimination, calibration, and decision analysis together; section “Validation, regulation, and workflow integration” provides an execution protocol that reduces optimistic bias and improves transportability [62].

Several nodule management solutions have received regulatory clearance, bridging research evidence and deployable clinical tools [63, 64]. Examples include Riverain ClearRead CT with EDA 510K clearance in the United States and Veye Lung Nodules with an EU MDR CE mark, which function as concurrent readers for detection, volumetry, and growth assessment in PACS integrated workflows [65–67]. Real world rollouts emphasize additional requirements: seamless RIS and PACS integration, stable inference latency, auditable trails, and

Table 1 Methodological comparison: radiomics vs deep learning

| Topic | Radiomics (hand-crafted) | Deep Learning (end-to-end) | Key references |
| --- | --- | --- | --- |
| Features and inputs | Shape/intensity/texture/features sensitive to acquisition heterogeneity (slice thickness, reconstruction kernel, vendor) | Voxel-level signals plus peri-tumoral context; automatically learned multi-level representations | [46, 47] |
| Reproducibility and standardization | IBSI-aligned parameters: voxel resampling (e.g., 1.0 mm isotropic), intensity discretization, LoG radii; release code and parameter files | Document preprocessing/augmentation/on multi-domain harmonization; document differences between training and inference domains | [28, 47, 50] |
| Performance and generalization | Effective on homogeneous data but vulnerable to domain shift | Often outperforms traditional models on multi-domain/harmonized data | [46, 48] |
| Evidence and reporting | External validation, calibration curves, DCA, and stratified error analyses | Same requirements; additionally adhere to TRIPOD+AI for transparent reporting | [28, 49, 51] |

---

<!-- Page 5 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:1018
Page 5 of 25

collaboration between humans and AI such as AI triaged worklists and structured reports that state uncertainty explicitly in the report, for example, risk including detection, risk stratification, staging, invasiveness, and risk of metastasis, studies should prospectively outcomes and thresholds, report calibration including flexible calibration plots and DCA also called DCA, provide subgroup analyses by vendor, protocol and key demographic and clinical factors or disease IBSI conformant parameters together with reference implementations to enable independent verification [70].

Heatmaps and saliency maps used to explain nodule detection or malignancy risk do not provide evidence of model reasoning in a way that clinicians can use. They can remain stable when labels or weights are randomized, highlight scanner-specific artifacts such as kernel edges, beam-hardening, or bed/table contours, or change significantly with minor preprocessing adjustments [72]. For each imaging task, we recommend reporting the following: sanity checks where saliency should collapse with label or weight randomization, faithfulness metrics such as deletion or insertion curves or ROAR/IROF showing monotonic performance loss when removing important regions compared to matched controls, stability across seeds, augmentations, and scanners, and clinical alignment through concept-level tests such as spiculation or necrosis masks with effect sizes and confidence intervals [73]. Explanations should be accompanied by uncertainty and selective deferral, especially near decision thresholds used for escalation pathways. They must also be evaluated for automation bias in reader studies [74].

#### AI in pathological subtyping and biomarker inference

Digital pathology is another frontier where AI is transforming the diagnosis of NSCLC [15, 20]. Traditionally, histologic subtyping of NSCLC is based on microscopic alterations require meticulous microscopy and multiple ancillary assays, such as IHC for TTF-1 and p40 and fluorescence in situ hybridization or sequencing for genomic alterations [75]. AI analyzes whole slide images (WSI) of tumor tissue to automate and augment these tasks. Deep learning models trained on labeled H&E slides accurately classify NSCLC histopathology, distinguishing adenocarcinoma from squamous carcinoma and other subtypes, with performance comparable to expert pathologists. For example, a 2020 study reported accuracy of approximately 0.95 for differentiating adenocarcinoma from squamous carcinoma on WSIs [76]. WSI pipelines use MIL with attention pooling. Tile-level embeddings are aggregated via self attention or gated attention to produce slide level predictions. Recent variants apply token based Transformers to tile sequences with two dimensional positional encodings. We record the reported layer count, number of attention heads, and

whether frequency aware attention such as FA or WA, or stain aware modules, was used to improve robustness. For IHC quantification, lightweight Vision Transformer heads operating on nucleus or patch tokens are increasingly used to standardize the PD-L1 TPS [29]. A particularly promising application is molecular virtual staining, namely biomarker prediction directly from routine H&E images [20, 77]. Building on foundational work such as that by Coudray and colleagues, who reported an AUROC of approximately 0.82 for EGFR prediction from H&E, Campanella and colleagues in 2025 developed EAGLE, a refined pathology AI that was prospectively evaluated in a real world setting for EGFR prescreening [22]. This model was trained on a dataset of over 5000 digitized biopsies and achieved internal and external AUROC values of approximately 0.85 and 0.87, which translated into approximately 43% fewer reflex molecular tests while maintaining sensitivity. In a prospective deployment simulated study, it achieved an AUROC of 0.89 on new cases and substantially reduced biomarker reporting time [22]. This approach conserves tissue for comprehensive sequencing and shortens the turnaround time for initiating targeted therapy [22]. Similar AI approaches are being explored to predict other actionable alterations, such as anaplastic lymphoma kinase (ALK) or ROS proto oncogene 1 (ROS1) fusions, from morphology. However, their rarity requires larger training datasets [78] (Table 2).

AI-based analysis of immunohistochemical slides yields more consistent protein-biomarker quantification than manual scoring [21, 80]. For example, in 2022 Wu and colleagues developed a deep learning system to score PD-L1 IHC in NSCLC. The model's tumor-proportion scores showed strong agreement with pathologists, with a correlation coefficient of about 0.94, and a mean absolute difference of 0.02. Consistency [21]. The AI in pathology enables precise subtyping of NSCLC by extracting detailed phenotypic information from routine slides [79]. These systems automate tumor classification, identify diagnostically relevant regions for review, and predict molecular markers without invasive procedures. Importantly, these tools are designed to support human experts rather than replace them [81]. With appropriate validation and regulatory approval, AI-augmented pathology can standardize diagnoses across centers and ensure accurate histologic and molecular characterization for each patient, which are foundations of personalized NSCLC care [15, 22].

Notwithstanding these advances, several limitations and sources of bias warrant emphasis. Across H&E based biomarker studies, external validation is inconsistent and subgroup calibration is seldom reported [82]. Many studies do not enforce patient level splits that separate sites and scanners at the partition stage, increasing the risk

---

<!-- Page 6 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 6 of 25

**Table 2**
 NSCLC digital pathology task overview

| Subdomain | Input modality | External validation (centers/batches/scanners) | Clinical use/potential impact | Key references |
| --- | --- | --- | --- | --- |
| Histologic subtyping | H&E whole-slide images (WSI) | Reported in some studies; details NR | Standardized subtyping; reduced subjective variability | [15, 20], [76, 79] |
| Molecular biomarker prediction | H&E WSI | Yes (multicenter; > 1 scanner; batch differences present) | ~43% reduction in reflex molecular tests; tissue conservation; shorter TAT | [20, 22], [77] |
| Prediction of actionable fusions (ALK/ROS1) from morphology | H&E WSI | Larger-scale validation pending (NR) | Piercening to optimize molecular testing | [78] |
| IHC quantification | IHC slides | Some cross-center/reader work (NR) | Standardized IHC scoring supports immunotherapy decision-making | [21, 80] |
| Clinical integration and expert support | WSI/IO, plus reporting systems | Real-world deployment progressing (NR) | Provides explainable evidence to augment, not replace, experts | [28, 49], [51] |

of leakage from acquisition related signatures [83]. Few reports include grayscale or stain normalized ablations, per site performance with confidence intervals, or negative region controls. Saliency maps are often presented without validity checks or quantitative evaluation. We recommend patient level splits that separate sites, explicit per site calibration, color and stain ablations, tumor only masking analyses, and stability tests across random initializations. These reporting elements help distinguishing genuine morphologic associations from confounding factors [84].

In WSI pipelines, tile-length heatmaps often co-localize with staining or batch signatures, or tissue processing borders, instead of tumor morphology [85]. Without color or stain ablations, tumor-only masking, and cross-scanner stability tests, saliency can be misleading [86]. We recommend reporting the following: (i) color-space or stain normalization ablations with effect size and confidence intervals; (ii) negative-region controls, such as background and artifacts; (iii) concept-based validation, such as TCAV for gland formation, keratinization, or TIL density with bootstrap-tested significance; and (iv) slide-level counterfactuals, such as swapping stain or morphology exemplars, to test causal relevance of the explanation. Incorporate prototype-based or concept-bottleneck heads when feasible to improve faithfulness and auditability.

## Role of AI in prognosis prediction and risk assessment

### Integration and analysis of multimomics data

#### Rationale and data types

Prognosis improves when multimomics data that comprise genomics with mutations and copy number alterations, transcriptomics, methylicomics, proteomics, and metabolomics are integrated. ctDNA, image-derived features from radiology and pathology such as radiomics and pathomics, and routine clinical variables [26, 87–89].

AI enables representation learning and discovery of cross modal interactions beyond linear additivity. These advances yield composite risk scores that better capture tumor biology and the host context [48].

#### Model classes and fusion strategies

Model classes and fusion strategies are summarized with follows. Approaches include penalized Cox models with learned embeddings [90], deep survival models such as DeepSurv and DeepTilt, Transformer based fusion for variable length longitudinal sequences [91]; and GNNs that capture pathway and interaction structure. Fusion can occur at the feature level, known as early fusion; at the decision level, known as late fusion; or at intermediate layers via cross attention [9, 91]. Pathway aware regularization improves interpretability by aligning learned representations with biological circuits [92]. To support model selection and reproduction, we summarize core architectural choices, hyperparameter sensitivity, and computational complexity of model classes [93]; see Table 3. Transformer based fusion requires careful specification of tokenization, sequence length and windowing, the number of layers and heads, the hidden width, and the attention variant. Training cost and inference latency scale with the token count and the network depth, which can constrain deployment in resource limited settings [94]. Practical mitigations include parameter efficient fine tuning with adapters or low rank adaptation, mixed precision training, quantization, pruning, and knowledge distillation [95]. For GNNs, the choice among convolutional families such as GCN, GraphSAGE, and GAT interacts with graph construction and neighborhood size, and excessive smoothing or excessive squashing can degrade performance [96]. For whole slide image pipelines, tile size and stride, stain normalization, and the attention pooling strategy strongly affect both accuracy and throughput. Across all classes, the most sensitive hyperparameters typically include the learning rate,

---

<!-- Page 7 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 7 of 25

**Table 3**
 Multimodal AI for NSCLC: from diagnosis to personalized therapy

| Model class | Inputs | Objective | Limitations | Data/compute demand | Key hyperparameters and implementation notes | Key refs |
| --- | --- | --- | --- | --- | --- | --- |
| Penalized Cox with learned embeddings | Hand-crafted and learned representations | Time-to-event | Linear risk composition unless embeddings capture non-linearity | Low to moderate: CPU or single GPU | Regularization strength, embedding size, feature scaling, report convergence and proportional hazards checks | [90] |
| Deep survival model (DeepSurv, SurpHiT) | Images/WSI or omics and clinical | Hazard/risk or discrete-time event probability | Calibration and transparency require care | Moderate: 100s to few GPUs | Learning rate and batch size, early stopping, label discrepancy, report discrete-time, augmentation; report time-dependent AUROC and IBS | [91] |
| Transformer-based fusion | Longitudinal imaging, ctDNA, labs, notes | Sequence modeling of risk over time | Data-hungry; careful masking/temporal encoding needed | High: scales with sequence length and depth; memory bound | Token size and stride, sequence length and windowing, layers and heads, hidden size, attention variant; adapters or LoRA for efficient tuning; mixed precision and quantization for deployment | [91] |
| GNNs | Omics graphs; patient-feature graphs | Risk via structured message passing | Graph construction choices matter; scalability | Moderate; depends on graph density | Aggregation type, neighborhood size, number of layers, avoid oversmoothing; document graph build rules | [92] |
| Fusion strategies | — | — | Early needs harmonized preprocessing; Late may miss interactions; Intermediate more complex | Varies | Decision-level vs cross-attention; report latency and memory impact of fusion block | [9, 91] |

batch size, weight decay, data augmentation, and early stopping criteria. We recommend reporting wall clock training time, GPU type and count, peak memory footprint, and per case inference time, and releasing exact configuration files and fixed random seeds to enable deterministic reruns [97].

#### Recent exemplars and effect sizes

Multimodal survival models that combine CT radiomics, WSI embeddings, mutational signatures, and clinical covariates typically increase the concordance index by 0.05 to 0.12 over clinical baselines and lower the integrated Brier score. External validations show good portability with calibration drift that is usually modest and amenable to recalibration [26, 51, 98, 99]. Early stage I to II studies that combine genomics and pathomics have identified high risk subgroups that gain an absolute 5% to 10% overall survival benefit from adjuvant therapy, whereas low risk groups may be candidates for de-escalation of therapy [76, 100, 101].

#### Dynamic and longitudinal risk

Landmarking and joint models update risk after each assessment, including ctDNA kinetics, radiographic response, and laboratory trends. These approaches outperform static baselines on time dependent area under the curve and enable earlier escalation or de-escalation of therapy [102–106]. Reinforcement learning policies for adaptive sequencing are promising but require prospective oversight and clearly defined safety constraints [107–109].

#### Scale, privacy, and fairness

Multi institutional training is essential to capture real world variability [110]. Federated learning (FL) enables training across sites without moving raw data, while secure aggregation, client side differential privacy, and auditable logs protect confidentiality [111–113]. Fairness audits should be routine, with subgroup calibration and utility metrics such as calibration within groups and equalized odds, and any remediation, including reweighting or adversarial debiasing, should be documented [79, 114].

#### Reporting checklist (prognosis)

Study details: (1) register analysis plans; (2) use internal and external validation across sites and time; (3) report calibration plots and metrics, including area under the curve, concordance index, integrated Brier score, and DCA, with time dependent estimates where relevant; (4) account for competing risks; (5) report subgroup performance by sex, race or ethnicity, geography, and smoking status; and (6) release code, parameter files, and data dictionaries to enable reproducibility.

#### Multimodal survival prediction models

AI driven prognostic models for NSCLC typically output a predicted survival time or a patient specific risk score. These outputs guide clinical decisions, such as whether to add adjuvant chemotherapy after surgery and how intensively to follow a patient [105]. Traditional models, such as tumor node metastasis staging, consider only a few variables, whereas AI models can integrate many features from imaging, pathology, and omics [26]. As a

---

<!-- Page 8 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:1018
Page 8 of 25

result, AI models demonstrate improved discrimination for survival stratification [100].

For example, imputation has been identified imaging features that correlate with outcomes independent of stage [115, 116]. In a pilot study, a deep learning model applied to pre treatment CT scans predicted overall survival in NSCLC, and the model derived risk scores separated patients into distinct prognostic groups. In that same study, the AI ROC was approximately 0.70, outperforming a model that used only clinical factors, which achieved approximately 0.60 [117]. Similarly, AI derived pathomic features from H&E slides have prognostic value. A 2023 study reported five year survival prediction with area under the curve values ranging from 0.85, exceeding models based on tumor grade or stage alone [118]. Together, these approaches enable a digital prognostic assay built from routine diagnostic data [116]. Combining radiology based and pathology based AI predictors with clinical variables yields integrated survival models. Several institutions are evaluating AI based survival nomograms for NSCLC that output individualized survival probabilities. In 2023, Song and colleagues developed a nomogram that combined a deep learning radiomics signature derived from CT with clinicopathologic variables to predict progression free survival in stage IV EGFR mutant NSCLC treated with EGFR inhibitors. The model improved one year progression risk stratification [119].

Beyond static baselines, AI models can provide dynamic prognostic updates [103]. For example, serial imaging combined with ML can assess response trajectories and adjust survival predictions; this approach is known as dynamic risk prediction [40]. In practice, dynamic risk is modeled with sequence Transformers that consume tokens indexed by event or by visit, together with temporal and frequency attention [29]. Four layers captured the temporal and wavelet blocks capture abrupt transients induced by treatment regimens [30–32]. Key hyperparameters to report include sequence length and windowing, the time embedding scheme, which may be absolute or relative, the number of layers and attention heads, and the masking strategy for irregular sampling. Multiple time point radiomic modeling in lung cancer shows that changes in tumor texture or other features after a few therapy cycles predict long term outcomes better than baseline features alone [120]. In addition, multi omics prognostic models have been applied in specific contexts, such as early stage NSCLC after surgery [89]. One AI model integrated gene expression profiles with clinical factors to predict which patients would benefit from adjuvant chemotherapy. It identified a subset of stage I patients at high risk of recurrence who experienced significantly improved survival with chemotherapy, illustrating the potential of AI for

decision making based on prognostic stratification [89, 121].

In summary, AI-based survival-prediction models—especially those built on multimodal data—are achieving higher accuracy and finer risk discrimination in NSCLC [26]. They hold promise for personalized risk assessments that inform patient counseling and rational treatment [122]. [38]. However, prospective validation remains essential [51]. Many published models still require rigorous external validation across diverse cohorts to ensure generalizability beyond their training sets [122]. As these models mature, they could be incorporated into practice via decision-support systems that, for example, flag a “high-risk” patient and prompt closer follow-up or prompt consideration of novel adjuvant therapies [123] (Fig. 2). Despite these advances, important limitations and potential sources of bias remain. First, many studies rely on internal validation and lack temporally or geographically external test cohorts, and the reporting of calibration and DCA is inconsistent [124]. Second, patient level splits that separate sites and scanners are often missing, which can allow acquisition related signatures to inflate performance [83]. Third, dynamic models can inadvertently leak post baseline information into the target or comparator, introducing immortal time bias and overly optimistic estimates. Fourth, approaches to censoring, competing risks, and treatment switching vary widely, and concordance alone does not capture calibration over time. Finally, subgroup calibration by sex, age, ancestry, stage, and site is rarely presented, fairness analyses are uncommon, and most reports omit drift monitoring and change control plans [125].

## AI in treatment decisionmaking and personalised therapy

AI for treatment decision making in NSCLC is moving beyond proof of concept and toward clinically consequential systems. These models integrate high dimensional, multimodal, and longitudinal data from radiology, pathology, multi omics and cDNA, and electronic health records, calibration, DCA, and deployment readiness. Critically, models should output risk over time by using serial imaging, circulating biomarkers such as ctDNA kinetics, and real world data streams. This dynamic updating better reflects disease trajectories and treatment effects in practice. When estimating individualized benefit, causal ML approaches can complement prediction to guide treatment escalation or deescalation.

---

<!-- Page 9 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:108

Page 9 of 25

The diagram illustrates a multimodal data integration and fusion model for dynamic risk prediction in NSCLC. It is structured into four main stages:

- Multi-source data integration:This stage combines four data modalities: Genomics (represented by a DNA helix icon), Imaging (represented by a CT scan icon), Pathology (represented by a microscope icon), and Liquid biopsy (represented by a blood drop and DNA strand icon).
- Model Categories and Fusion Strategies:This stage details the models used for integration and fusion:Penalized Cox Model:Shows a graph of "Penalized Log Hazard" vs. "Drug Sensitivity (%)".Deep Survival Model:Shows a graph of "Survival Probability" vs. "Time".Transformer Fusion Technology:Represented by a series of blue 3D blocks.Graph Neural Network:Represented by a grid of nodes with varying colors.
- Penalized Cox Model:Shows a graph of "Penalized Log Hazard" vs. "Drug Sensitivity (%)".
- Deep Survival Model:Shows a graph of "Survival Probability" vs. "Time".
- Transformer Fusion Technology:Represented by a series of blue 3D blocks.
- Graph Neural Network:Represented by a grid of nodes with varying colors.
- Dynamic Prediction and Interpretation:This stage shows the model's output over time, represented by a timeline with lung icons.Initial Composite Risk Score:The starting point on the timeline.Fourier layer:Captures long-term periodic changes, shown as a graph of a periodic wave.Wavelet Block:Capturing therapy-induced mutational changes, shown as a graph of a single pulse.Updated Risk Score:The final point on the timeline.
- Initial Composite Risk Score:The starting point on the timeline.
- Fourier layer:Captures long-term periodic changes, shown as a graph of a periodic wave.
- Wavelet Block:Capturing therapy-induced mutational changes, shown as a graph of a single pulse.
- Updated Risk Score:The final point on the timeline.

Fig. 2 Multimodal data integration and fusion models for dynamic risk prediction in NSCLC

Reinforcement learning based adaptation is promising but requires explicit safety guardrails and prospective oversight. Against this backdrop, section “Multimodal survival prediction models” summarizes evidence for response and toxicity prediction across radiotherapy, chemotherapy, targeted therapy, and immunotherapy, and highlights actionable operating points and clinical utility (see Fig. 3, section “Response and toxicity prediction across modalities” reviews AI in drug discovery and virtual screening, where generative and structure aware approaches, for example AlphaFold supported pipelines, are accelerating target identification and lead optimization for NSCLC; see Fig. 4).

#### Response and toxicity prediction across modalitiesRadiotherapy

AI improves radiotherapy planning and predicts which patients are likely to benefit from radiation or experience treatment related harm [126]. For planning, recent methodological reviews advocate standardized and externally validated segmentation pipelines with transparent reporting of architectures, key hyperparameters and computational constraints, which enables reliable auto contouring and more consistent plans across sites, including resource limited centers [127–129]. For response prediction, radiomics based models identify imaging features associated with tumor radiosensitivity. For example, radiomic patterns on pre treatment CT have

---

<!-- Page 10 -->

Chang et al. Journal of Translational Medicine

(2026) 24:1018

Page 10 of 25

Drug DiscoveryAI accelerating the discovery of new Drugs

AI predicts new targets    Biomarker prediction    Clinical Trial Design

RadiotherapyPrecise planning, efficacy and toxicity prediction

Local control rate / recurrence risk    Risk of radiation pneumonitis

Personalized dosing plan    Dose monitoring

ChemotherapyIdentify responders to chemo

Response prediction    To avoid dying resistance treatment

Confirmed    Non-responders

Targeted therapyUnique tumor targets, shift resistance

Gene signature analysis    Flow cytometry

Gene resistance mechanisms and sequential treatment recommendations

ImmunotherapyDecoding the tumor microenvironment for efficacy

Long-term benefits vs. risk of hyperprogression

Patient Stratification and Risk Monitoring

AI Clinical Decision Support Engine

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy    Immunotherapy    Drug Discovery

Radiotherapy    Chemotherapy    Targeted therapy

---

<!-- Page 11 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:108
Page 11 of 25

Fig. 4 AI in NSCLC drug discovery: from target identification to patient-specific response prediction

distinguished responders from non responders to first line chemotherapy on baseline CT with modest accuracy of approximately 70% [137]. In addition, AI analysis of blood based biomarkers, for example serum N glycome changes, has been investigated to forecast efficacy [138]. Although no AI test for chemotherapy response is in routine clinical use, these early studies suggest tools that could guide selection between intensive chemotherapy and alternative treatments for individual patients [139].

#### Targeted therapy (EGFR/ALK inhibitors)

In oncogene driven NSCLC, the key question is not only whether a tumor harbors a targetable alteration but also how durable the treatment response will be [140]. AI models are being developed to predict outcomes with targeted therapies and to identify early in treatment which patients may need additional interventions. Among patients with EGFR mutant NSCLC who start EGFR tyrosine kinase inhibitors, only a subset achieve prolonged progression free survival, whereas others progress rapidly because of de novo resistance [141]. Two recent studies applied ML to baseline clinical and

imaging data to predict short progression free survival with EGFR tyrosine kinase inhibitors, thereby flagging high risk patients who might benefit from upfront combination strategies [142]. In these studies, the models identified patients at high risk of early progression within six to nine months with reasonable accuracy. These predictions are clinically actionable. For a patient predicted to respond poorly to EGFR tyrosine kinase inhibitor monotherapy, an oncologist might add chemotherapy or a vascular endothelial growth factor inhibitor at treatment initiation, an approach that can improve outcomes but may increase toxicity [143]. Similarly, in ALK positive NSCLC, where multiple ALK inhibitors are available, AI models are being explored to predict which specific inhibitor a tumor is most likely to respond to based on biological differences derived from omics data [144, 145].

#### Immunotherapy

Because only about 20 to 30% of unselected NSCLC patients respond to immune checkpoint inhibitors, identifying reliable predictive biomarkers is essential [146]. AI has been used to discover new biomarkers and to

---

<!-- Page 12 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:108
Page 12 of 25

integrate multiple signals into more accurate composite predictors [38]. In computational pathology, AI models predict the spatial distribution of tumor cells, which infiltrates on H&E slides to infer tumor immune phenotypes [147]. Rake et al. developed Deep-IO, a deep learning model that predicts immune checkpoint inhibitor outcomes from pre treatment H&E slides. In a cohort of 38 patients with advanced NSCLC, the model accurately independently predicted response and survival and either outperformed or complemented PD-L1 and tumor mutational burden, with an area under the curve of 0.66 for objective response in external validation compared with 0.62 for PD-L1 at least 50%. Combining the AI score with PD-L1 increased the area under the curve to 0.70 and identified responders with higher precision [148]. Radiomic profiling provides a complementary approach. CT features can distinguish hyperprogressive disease from durable benefit on programmed cell death 1 or PD-L1 inhibitors, and one classifier induced hyper-progressors from ordinary progressors with an area under the curve of about 0.87 [38]. Radiomic biomarkers that reflect heterogeneity or volume dynamics have also correlated with outcomes and with immune related adverse events. For example, a baseline CT signature predicted the risk of immunotherapy-induced pneumonitis and enabled closer monitoring [149]. Multimodal models that integrate radiomics, PD-L1 expression, and ctDNA metrics have outperformed individual predictors for one year survival on immunotherapy [26]. By tracking temporal changes during treatment, deep learning models can detect response or progression earlier than the Response Evaluation Criteria in Solid Tumors and thereby prompt earlier treatment changes [102]. Overall, AI driven response prediction across modalities is confirming NSCLC care toward personalized therapy by matching each patient's unique profile to the most effective benefit and minimize harm. Although many models remain experimental, some pathology based immunotherapy predictors are undergoing prospective evaluation with encouraging early results [148, 150].

#### AI in drug discovery and virtual screening

Beyond clinical decision support, AI is reshaping the early phases of NSCLC drug development [38]. AI driven discovery applies computational algorithms to identify therapeutic targets, design novel molecules, and repurpose approved agents, often much faster than traditional laboratory screening [151]. NSCLC exhibits numerous genomic alterations and resistance mechanisms, creating many opportunities for new therapies; however, efficient discovery remains challenging. ML models, including deep generative approaches, learn from large chemical libraries and bioassay data to predict compounds that inhibit cancer targets or overcome resistance [152].

One important application is the discovery of next generation inhibitors against established oncogenic drivers [153]. Resistance to third generation EGFR tyrosine kinase inhibitors, such as osimertinib, often emerges through EGFR T790M and C797S mutations [153]. In 2024, Zhou and colleagues used a ML aided approach to identify CDDO-Me as a potential fourth generation EGFR inhibitor active against EGFR mutant NSCLC. The model screened hundreds of candidates by learning structure-activity relationships, and it predicted CDDO-Me, which was later confirmed experimentally, to strongly suppress proliferation of T790M mutant NSCLC cells, including in xenograft models. This approach marked a significant advance in drug discovery for laboratory testing, demonstrating how AI can accelerate lead compound discovery [152]. Similarly, in 2023, Zhang and colleagues used ML with support vector machines and random forests to design new small molecules targeting EGFR active site mutations, achieving external accuracy greater than 95% and guiding feature optimization, with R2 approximately 0.93 between predicted and experimental activity. These AI designed compounds are now candidates for further preclinical development [154].

AI is used for virtual screening of existing libraries to identify repurposing opportunities in NSCLC [155]. ML algorithms predict drug target interactions and synergistic combinations by mining patterns in historical pharmacologic data [156]. For example, a platform analyzing transcriptomic profiles predicted that a Food and Drug Administration approved kinase inhibitor, not originally indicated for lung cancer, could have activity in KRAS mutant NSCLC; subsequent laboratory testing confirmed this prediction and led to a new clinical trial [157]. Additionally, deep learning models such as GNNs operating on molecular graphs have been used to predict combinations of drugs and chemical targets, for example, KRAS G12C and MET exon 14 skipping, thereby guiding medicinal chemistry efforts [158]. In silico approaches also extend to immunotherapy, with neural networks proposing small molecules or peptides that modulate immune checkpoints or the tumor microenvironment [159].

Another emerging paradigm is the prediction of patient specific drug response enabled by AI [157]. Large cell line screens, for example profiling hundreds of compounds across dozens of lung cancer lines, generate data that AI uses to map genomic profiles to likely drug responses [160]. For example, the open source tool D3EGFR provides a deep learning based web server that predicts the sensitivity of EGFR mutant lung cancers to various tyrosine kinase inhibitors and their combinations [161]. As more cell line and organoid screening data accumulate, AI can match NSCLC tumors to optimal therapies, effectively conducting in silico clinical trials to prioritize

---

<!-- Page 13 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 13 of 25

treatments. This approach is particularly relevant for rare molecular subsets in which real world trials are difficult to conduct [157].

In summary, AI is accelerating NSCLC drug discovery on several fronts: identifying new candidates such as small molecule and biologic agents for resistance pathways; optimizing leads by predicting how structural changes affect activity and by using reinforcement learning to generate improved analogs; and repurposing or prioritizing agents for defined patient subgroups [162]. The success of AI discovered agents such as CDDO Me against EGFR T790M suggests a future in which AI augmented medicinal chemistry markedly shortens the timeline from target identification to effective therapy [154]. When coupled with rigorous wet laboratory validation, these approaches could expand the therapeutic arsenal for NSCLC, particularly for patients who have exhausted current options [162]. Close collaboration among computational scientists, chemists, and oncologists is essential to ensure that AI predictions are rigorously validated and translated into clinically viable drugs [139]. (Table 4) Despite this progress, important limitations and methodological conflicts remain. First, many studies use random or scaffold split validation, which allows near duplicate chemotypes to enter the test set and inflates performance; temporal splits and external assays from independent sources are needed [163]. Second, assay heterogeneity, batch effects, and differences in experimental

conditions can confound activity labels, and few reports include orthogonal confirmation across multiple assay formats [164]. Third, generative models may propose molecules that are difficult to summarize, unstable, or outside the applicability domain; synthesizability metrics, retrosynthesis success rates, and medicinal chemistry review are rarely reported [165]. Fourth, docking and scoring functions used in label data or triage candidates are noisy and can be slow to learn, and enrichment should be benchmarked against strong baselines with decoys and property matched controls. Fifth, translation from cell lines to patients is limited by context mismatch, off target effects and absorption, distribution, metabolism, and excretion (ADME) constraints; prospective, blinded screens and pre registered evaluations are uncommon. Sixth, uncertainty and calibration are seldom quantified, and studies frequently omit hit rate, precision at top k, and prospective enrichment metrics that would inform decision making [166].

## Challenges, limitations, and ethics

### Data bias and quality

#### Heterogeneity and bias

AI performance in NSCLC depends strongly on data provenance [167]. Variation in CT acquisition parameters such as tube voltage (kVp), current time product mAs, slice thickness, reconstruction kernel, and vendor, and differences in PET protocols such as uptake time and calibration, introduce batch effects that distort learned representations. Digital pathology preanalytic factors including fixation, processing, staining, and scanner optics and compression have similar effects [168]. Labels are often noisy because of interreader variability and evolving diagnostic criteria, and class imbalance caused by rare histologies and uncommon fusions predisposes models to majority class bias and to poorer performance in minority subgroups [169].

### Governance and documentation

Robust governance should include dataset dashboards for radiomics, adhere to IBSI definitions and publish pathology, including ischemic time, fixation, stain, scanner model, and International Color Consortium (ICC) profile, and for imaging, including Digital Imaging and Communications in Medicine (DICOM) tags, dose, and reconstruction kernel; and versioned curation pipelines with provable trails [170]. Such documentation enables reproducibility and supports forensic analysis after deployment [171].

### Standardization and harmonization

For radiomics, adhere to IBSI definitions and publish exact parameters and code; apply physics aware harmonization such as ComBat and kernel aware resampling,

Table 4 Prospective-facing summary of AI for NSCLC drug discovery and virtual screening

| Study (first author, year) | Task/Goal | Key outcomes (quantitative) | Prospective/translational status | Key refs |
| --- | --- | --- | --- | --- |
| Zhou, 2024 | Identify 4th-gen EGFR inhibitor active against resistance | CDDO-Me suppressed T790M-mutant NSCLC growth (inact IC50/TGI NR) | Preclinical; candidate for further development | [152] |
| Abramson (AlphaFold3), 2024 | Complex structure prediction to inform docking/design | SOTA complex prediction (platform) | Integrated in pipelines; pre-clinical utility | [151] |
| Meller (Pocket-Miner), 2023 | Predict cryptic binding pockets | Improved cryptic pocket detection | Design aid; upstream of med-chem | [158] |
| STTT review exemplar | Repurpose FDA-approved kinase inhibitor | Activity confirmed preclinically | Prospective clinical evaluation underway | [155, 157] |
| Zhao, 2025 | Epidental DL for drug-target interactions | Calibrated DTI improvement | Platform tool; supports prioritization | [156] |

---

<!-- Page 14 -->

Chang et al. Journal of Translational Medicine

(2026) 24:108

Page 14 of 25

and verify stability on repeat scan datasets [172]. For pathology, implement stain normalization, scanner aware augmentation, and color deconvolution [173]. Common cross scanner reproducibility through ring trials [173].

Label quality and learning strategies

Use rater agreement protocols and adjudication panels for key endpoints such as L1 TPS near cuts [169]. Leverage weak supervision using MLL, self-supervised pretraining, and active learning to maximize label yield. Address class imbalance with cost sensitive losses, calibrated resampling, and careful evaluation in minority strata while avoiding synthetic oversampling artifacts in texture rich tasks [174].

Generalizability, OOD behavior, and robustness

Report internal to external performance gaps explicitly. Decreases of five to ten points in the AUROC across scanners or across sites are common [49]. Characterize distribution shift using stress tests and challenge sets, covering covariate shift, changes in label prevalence, and concept drift. Implement out of distribution (OOD) detection with Uncertainty Quantification (UQ) to enable selective prediction [175]. Maintain model cards that document failure modes, subgroup caveats, and guardrails. In addition, conduct external validation with a locked pipeline. Use patient level splits that keep sites and scanners separate, and apply preprocessing learned only on development data. Report discrimination, calibration, and decision utility together, and provide subgroup results by site, scanner, sex, age, ancestry, stage, and grouping status; see section “Validation, regulation, and workflow integration” for execution details [28]. To

improve transportability, embed physics inspired modules that encode signal priors, including FA for global frequency structure, WA for multiscale edges and orientations, and low rank tensor decomposition to control capacity. Publish transform settings, low rank factors, and domain shift ablations [30–32].

Privacy and security

Anticipate risks of model extraction, membership inference, and inversion. Where feasible, use FL with secure aggregation and consider differential privacy for sensitive modalities such as whole slide imaging and electronic health records [166]. Perform threat modeling and penetration testing and monitor for anomalous access and potential data exfiltration [177] (Table 5).

Systematic data pitfalls are pervasive in existing studies (Table 6). Common weaknesses include (i) single-center, small-sample cohorts that inflate internal discrimination but fail under domain shift [178]; (ii) subjectivity and inconsistent annotations, particularly at near-threshold endpoints such as PD-L1 at 1% and 50%, with minimal adjudication or measurement error analysis; (iii) systematic case-mix and acquisition biases—including site/ scanner fingerprints, stage distribution, smoking status, ancestry, and socioeconomic proxies—that models learn and amplify [179]; (iv) leakage risks (patient overlap across splits and refitting normalization on combined data) that overstate performance [180]; and (v) imbalanced outcomes (rare fusions and never-smoker subsets) that produce unstable thresholds and poor calibration in under-represented groups [181]. We recommend explicit internal-external reporting with locked pipelines; patient-level splits that keep sites and scanners separate;

Table 5 Reporting and governance checklist

| Item | Minimum requirement for publication | Recommended best practice (deployment-ready) | Metrics/evidence to report | Key references |
| --- | --- | --- | --- | --- |
| Data provenance and metadata | Dataset/dataset; key imaging/pathology metadata (DICOM tags, stain/scanner) | Full provenance logs; versioned curation scripts; audit trails | Data dictionary; inclusion/exclusion flow; preprocessing parameters | [170, 171] |
| Standardization and harmonization | IBSI-conformant radiomics definitions; code/parameters shared | Physics-aware harmonization (ComBat, kernel-aware resampling); pathology stain normalization and scanner-aware augmentation; ring trials | Test-retest stability; cross-scanner/site reproducibility | [50, 172, 173] |
| Label quality | Labeler count and roles; consensus rules | Adjudication panels for key endpoints; near-threshold protocols (e.g., PD-L1) | Inter-rater agreement (κ/ICC); sensitivity analyses to re-labeling | [169] |
| Class imbalance and fairness | Class distributions; basic subgroup metrics | Cross-validation learning; calibrated resampling; fairness audit (by ancestry/site/scanner) | Calibration-within-groups, equalized-odds/PR gaps with Cs | [49, 169, 174] |
| External validity and shift | At least one external test | Internal-external validation across sites/time; stress tests; challenge sets | AUROC/C-index, Brier/ECE; reported internal-external gap (expected 5–10 points); coverage vs. accuracy under selective prediction | [49, 175] |
| Uncertainty and OOD | — | UQ (ensembles/MC-dropout/evaldental); OOD detection; selective denial policy | Calibration plot; risk-coverage curves, deferral utility/DICSSON curves (DCA) | [175] |
| Privacy and security | Ethics approval de-identification | FL + secure aggregation; differential privacy (where feasible); pen-testing | DP ε/δ (if used); federation topology, security test report; access monitoring | [176, 177] |

---

<!-- Page 15 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:1018

Page 15 of 25

**Table 6**
 Data quality pitfalls, subgroup harms, and mitigation/reporting playbook

| Pitfall | Typical manifestation in NSCLC AI | Potential clinical harm | Primary mitigation |
| --- | --- | --- | --- |
| Single-center, small-sample cohorts | High internal AUROC, drop on external sites/scanners | Mis-triage under domain shift; delayed or missed care | Multi-site curation; locked pipelines; internal–external validation |
| Inconsistent/subjective labels | Label noise; unstable thresholds; poor calibration | Overtreatment/undertreatment near cutoffs | Adjudication panels; near-threshold SDPs/UCRC tracking |
| Systemic case-mix bias | Subgroup TPR/FPR gaps; risk miscalibration | Disparate false negatives/positives; unequal benefit | Targeted sampling; reweighting; DRO; subgroup thresholds |
| Acquisition bias | Model keys on device/site signatures | Fragile transportability; scanner-specific failures | Physician-aware harmonization; stain calibration; ring trials |
| Class imbalance | Minority underperformance; unstable PPV/NPV | Missed rare actionable findings | Cost-sensitive loss; calibrated resampling; synthetic data with caution |
| Leakage | Inflated metrics; failure at deployment | Unsafe optimism | Patient-level splits; freeze pre-casing; audit trails |
| OOD/unseen shifts | Confidence mismatch; brittle predictions | Silent failures; unsafe automation | UQ + OOD detection; selective deferral; drift alarms |
| Privacy/security gaps | Data misuse; membership inference | Legal/ethical risk; loss of trust | FL-secure aggregation; DP where feasible; pen-testing |

and joint reporting of discrimination, calibration, and decision-curve analysis, each stratified by site, scanner, sex, age, ancestry, stage, and smoking status [124].

### Explainability and clinical trust

#### From saliency to semantics

Post-hoc saliency methods such as Gradient-weighted Class Activation Mapping, Integrated Gradients, and Layer-wise Relevance Propagation can highlight image regions that influence predictions; however, their faithfulness and stability remain limited without dedicated validation [182]. Where feasible, prioritize intrinsically interpretable designs, including concept-bottleneck models that detect clinical primitives such as spiculation, necrosis, and tumor-infiltrating lymphocyte density; generalized additive models with pairwise interactions (GA+2M); prototype or nearest-neighbor reasoning; and case-retrieval systems that surface similar prior patients and outcomes [183].

#### Evaluating explanations

Quantify faithfulness, defined as sensitivity to counterfactual perturbations; quantify stability, defined as repeatability across runs; and quantify utility, assessed by whether clinicians make better decisions faster. Avoid explanation theater by pairing explanations with quantitative UQ and systematic error analyses [184]. In pathology, complement heatmaps with tile-level concept scores that align with pathologist vocabulary.

#### Uncertainty, calibration, and selective workflows

Distinguish aleatoric and epistemic uncertainty, and use deep ensembles, MC-dropout, evidential networks, or conormal prediction to avoid well-calibrated confidence for each output [185]. Enable abstention in low-confidence or OOD cases, and route such cases to expert

adjudication or confirmatory testing, for example reflex next-generation sequencing for equivocal EGFR pre-screening and manual PD-L1 scoring near 1% or 50% [186].

#### Communication and documentation

Standardize report templates to list the model name and version, training domains, intended use, contraindications, uncertainty bins, and recommended actions. Maintain accessible factsheets and change logs for tumor boards and quality assurance committees [187].

#### Validation, regulation, and workflow integration

##### Validation ladder

Progress deliberately from technical validation that uses cross validation and internal and external splits, to clinical validation through multicenter retrospective studies with prespecified analysis plans, and ultimately to demonstrations of clinical utility through prospective evaluations such as Developmental and Exploratory Clinical Investigations of DECision support systems driven (DECIDE)-AI style pilots, stepped wedge or cluster trials, and, where feasible, Randomized Controlled Trials [188]. At each stage, report discrimination, calibration, DCA, and net reclassification compared with standard care [28].

High retrospective accuracy is necessary but not sufficient for clinical adoption [189]. Translation requires evidence across technical, clinical, and operational domains. First, demonstrate generalizability and calibration under domain shift on external datasets that differ by time, geography, vendor, and protocol [190]. Beyond discrimination, report calibration slope near 1.0, expected calibration error with a prespecified tolerance, and decision-curve analysis at prespecified thresholds with net benefit and linked actions [189]. Provide subgroup

---

<!-- Page 16 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:108
Page 16 of 25

calibration by site, scanner, age, sex, race or ethnicity, stage, and smoking status, with confidence intervals [26]. Second, characterize uncertainty and OOD behavior and define selective output and deferral policies with predefined coverage and deferral triggers [191]. Route low-confidence or OOD cases to expert review or reflex molecular testing, and disclose the impact on net benefit and resource use [27]. Third, address safety and interoperability through seamless integration with Radiology Information Systems and Picture Archiving and Communication Systems, DICOM Structured Reports and Segmentation, Fast Healthcare Interoperability Resources (FHIR), and Clinical Decision Support Hooks [192]. In shadow mode, the system should alert hidden burdens expressed as alerts per 100 cases, coverage–accuracy trade-offs, and re-review rates relative to standard procedures [194]. Fourth, set explicit service-level agreements and safety guardrails, including targets for end-to-end inference latency, failure rates, audit-log completeness, automatic escalation near decision thresholds such as PD-L1 1 and 50%, and human–AI collaboration with mandatory second confirmation for high-risk tasks such as emergency pulmonary embolism detection [195]. Fifth, manage lifecycle governance and change control under medical-device principles by defining drift triggers such as decreases in external AUROC beyond a preset margin or expected calibration error exceeding a threshold [196]. Establish recalibration and rollback plans with version auditing, monitor multicenter performance for adverse AI events, and track the balance between coverage, accuracy, and workload. Sixth, include fairness and economics in the evidence base by auditing in-group calibration and equalized-odds with confidence intervals, and by reporting time-to-treatment reductions, avoided unnecessary tests, budget impact, cost-effectiveness, and the passivity of the system [197, 198]. Together, these standards enable a measurable transition from high-performing models to safe, effective, and efficient clinical tools [194].

#### Regulatory frameworks

For AI and ML based software as a medical device, align with the International Medical Device Regulators Forum risk frameworks; the United States Food and Drug Administration total product lifecycle principles and pre-determined change control plans for learning systems; the European Organization for Standardization and In Vitro Diagnostic Regulation and the EU AI Act; and the United Kingdom Medicines and Healthcare products Regulatory Agency change programme. Operate under a quality management system compliant with International Organization for Standardization 13485, risk management according to International Organization for Standardization 14971, software lifecycle standards

International Electrotechnical Commission 62304 and International Electrotechnical Commission 82304–1, current cybersecurity guidance, and Good ML Practice [198]. Plan postmarket surveillance with real world performance monitoring and define explicit triggers for recalibration or rollback [199].

#### Clinical Integration and Interoperability

Embed AI into routine clinical systems and data pipelines, including DICOM Segmentation and Structured Report objects, Fast Healthcare Interoperability Resources Observation and Diagnostic Report resources, Clinical Decision Support (CDS) Hooks, and Health Level Seven International order and result messages. Define inference service level agreements, maintain auditable logs and user controls, and run shadow-mode pilots before go-live to quantify alert burden and false positive externalities [193].

#### MLops in healthcare

Manage models as living systems. Maintain dataset and feature versioning; use gated continuous integration and continuous delivery deployments; run synthetic and real world regression tests; monitor for distribution shift; schedule recalibration and periodic reapproval; and maintain documented rollback plans. Define clear roles, responsibilities, and escalation paths for adverse AI events [58, 200].

#### General limitations and comparability across studies

Most multimodal fusion studies summarized here are retrospective and frequently single center, and they report only marginal gains over unimodal baselines, which calls into question clinical significance without net benefit analysis and action linked thresholds [28]. For example, a systematic review by Yu and colleagues of externally validated imaging models found that most algorithms performed worse on external datasets, highlighting the gap between internal discrimination and transportability [201]. In digital pathology, a 2024 meta analysis reported variable accuracy and frequent risk of bias, and a public audit of commercial products showed that only about forty percent had peer reviewed external validation, underscoring limited generalizability [82]. Even in promising cases such as the EAGLE pathology system for EGFR prescreening, internal and external AUROC values were about 0.85 and 0.87, and a prospective silent evaluation reached 0.89; however, these gains require translation into net benefit, explicit decision thresholds, and measurable reductions in time to treatment to establish clinical value [202]. Across prognostic models, reporting of calibration and DCA remains inconsistent, despite long standing guidance that clinical usefulness should be expressed as net benefit across

---

<!-- Page 17 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:1018
Page 17 of 25

clinically relevant thresholds [203]. Methodological pitfalls all but persist, including potential leakage of post baseline information in dynamic models leading to immortal time bias, heterogeneous handling of censoring, competing risks, and treatment switching, and insufficient subgroup calibration by sex, age, ancestry, stage, and site. Finally, cross paper comparisons are often not directly comparable because datasets, endpoints, preprocessing, and evaluation metrics differ, which limits interpretation of reported incremental gains unless studies share harmonized benchmarks, analysis plans, and reporting checklists such as TRIPOD-AI and DECIDE AI. Together, these observations support prospective multicenter evaluations with preregistered analysis plans, external and temporal test cohorts, decision relevant metrics such as net benefit and reclassification, and routine subgroup and site specific calibration to demonstrate durable generalizability and practical clinical impact.

#### External validation and calibration

Execution. Predefine the full pipeline and keep it fixed during testing [204]. Use external cohorts that differ in geography and time and that span multiple vendors and protocols. Fit preprocessing only on development data and apply it unchanged to external data. Enforce patient level splits that separate sites and scanners. Report AUROC and area under the precision recall curve with 95% confidence intervals [205]. Report calibration in the large, the calibration slope and intercept, smooth calibration curves, and expected calibration error. Provide DCA across prespecified thresholds and report the net reduction in interventions at the chosen operating point. For survival outcomes, report the concordance index (C index), time dependent AUROC, and the integrated Brier score, and account for competing risks. Aim for at least 100 events and 100 non events for binary outcomes and at least 200 events for survival, or use internal external cross validation when event counts are limited. Follow TRIPOD plus AI and DECIDE AI for study planning and reporting [28].

Common pitfalls include tuning on the external set, refitting normalization on combined data, mixing patients across sites, altering class priors without recalibration, reporting discrimination without calibration or decision analysis, and omitting subgroup calibration by site, scanner, sex, age, ancestry, and stage. Preregistration, harmonized reporting templates, and routine stratification by site and subgroup help mitigate these risks [28].

#### Future outlook: integration, interpretability, and equity

Realizing the clinical promise of AI in NSCLC requires a shift from isolated single task models to an integrated clinician centered ecosystem that is scalable, interpretable,

and equitable (Fig. 5). Foundation and cross modal Transformer backbones trained on diverse medical corpora can unify signals from imaging, pathology, molecular, and cDNA together with electronic health records. The resulting shared representation supports NSCLC specific fine tuning for diagnosis, biomarker inference, risk trajectories, and treatment ranking. Beyond static baselines, foundational architectures are emerging that links longitudinal imaging and cDNA kinetics with digital twin simulations can update risk in real time and anticipate counterfactual treatment responses. Mechanism aware and causal methods align predictions with biology and estimate individualized benefit under confounding. Conventional modalities such as CT scanners, histology, and therapies evolve while preserving privacy. Successful translation depends on clinician co design, usable explanations, and layered safety that includes uncertainty awareness and OOD aware abstention. It also depends on training in AI literacy and on routine evaluation of cognitive load and time to decision. Standards and equity are essential. Priorities include interoperability through the IBSI, DICOM Structured Report and Segmentation, FHIR, and Clinical Decision Support Hooks; benchmarking on open multicenter data sets; proactive fairness auditing with remediation; and pathways for deployment in low resource settings with clear consent and governance under emerging regulations.

#### Deeper multimodal fusion at scale

##### Foundation and transformer paradigms

The field is converging on foundation models trained on diverse medical corpora, including CT and positron emission tomography, WSI, clinical notes, and structured laboratory data, paired with cross modal Transformers that learn joint latent spaces [206]. Fine tuning for NSCLC prediction and diagnosis such as diagnosis, biomarker inference, risk trajectories, and ranked treatment options from a shared backbone [15]. Self supervised and weakly supervised objectives, including masked modeling and contrastive pairing of image, omics, and text, reduce labeling burden and improve transfer across institutions [20]. Concretely, foundation models tuned for NSCLC typically comprise three components. The first is a modality specific tokenizer, for example three dimensional patch embedding for CT, a tile encoder for WSI, a gene set projector for omics, and a text encoder for clinical notes. The second is a shared Transformer with between twelve and forty eight layers and between twelve and twenty four attention heads, connected by cross attention bridges for intermediate fusion [29]. The third is a personalization layer using adapters and low rank adaptation (LoRA) for site specific adaptation. For longitudinal use, FA or WA blocks can be inserted into temporal layers to couple slow trends and abrupt shifts

---

<!-- Page 18 -->

Chang et al. 
*Journal of Translational Medicine*

(2026) 24:108

Page 18 of 25

The diagram is a circular infographic titled "NSCLC AI Future Outlook: Integration, Explainability, and Equity". At the center is a brain icon with the letters "AI" inside. Radiating from this center are several icons, each with a label. The diagram is divided into three main sectors by large curved lines:

- Clinician centred, explainable AI(left sector): Includes icons for "Foundation and transformer paradigm" (bar chart), "Mechanism-aware AI" (document with a brain), "Continual and FL" (server), "Benchmarking" (bar chart), "Temporal and patient-centric modeling" (play button), "Standards and interoperability" (gears), "Equity by design" (crosshair), "Low-resource deployment" (document), and "Ethics and consent" (handshake).
- Standardisation and equitable access(right sector): Includes icons for "Co-design and usability" (building), "Interactive reasoning" (gears), "Education and literacy" (graduation cap), and "Safety layers" (shield).
- Deeper multimodal fusion at scale(top sector): Includes icons for "Foundation and transformer paradigm", "Mechanism-aware AI", "Continual and FL", and "Benchmarking".

A blue box at the bottom center contains the text: "NSCLC AI Future Outlook: Integration, Explainability, and Equity".

Fig. 5 NSCLC AI future outlook: integration, explainability, and equity

[30–32]. We recommend that future studies report the number of layers, the number of attention heads, the hidden size, the token size and stride, the attention variant, the parameter count, the pretraining corpus and modalities, and the adapter rank.

#### Temporal and patient-centric modeling

Move from snapshots to trajectories. Use sequence models to represent longitudinal imaging, cDNA kinetics, laboratory trends, and therapy timelines, and update risk in real time [103]. Combine these models with digital twin constructs that simulate counterfactual responses under alternative regimens and schedules, enabling “what if” exploration during tumor boards [107].

#### Mechanism-aware AI

Integrate pathway knowledge and causal constraints to reduce spurious associations by using pathway regularized networks, graph causal models that link radiomic heterogeneity to hypoxia and immune evasion programs, and joint models of tumor and host interactions [208].

For drug response modeling, estimate individualized treatment benefit with treatment effect methods such as uplift modeling, causal forests, and targeted maximum likelihood estimation, and explicitly account for confounding through appropriate adjustment or identification strategies [209]. This section’s discussion of causal forests, uplift modeling, and mechanism-aware models is reiterated in the Conclusion as a key set of emerging directions for individualized therapy response prediction.

#### Continual and FL

Anticipate continual updates as scanners, protocols, and therapies evolve [210]. Combine federated training with privacy preserving analytics to keep models current across networks while respecting local data governance requirements [112]. Distribute personalization layers using lightweight adapters that align models to site specific distributions without modifying the shared backbone [206].

---

<!-- Page 19 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:108
Page 19 of 25

### Benchmarking

Establishing strong, multicenter NSCLC benchmarks that span multiple mortality and endpoints, including pathologic complete response, major pathologic response, event free survival, progression free survival, overall survival, and toxicity. Use standardized preproceeding and transparent protocol documentation, and maintain clearly separated training, validation, and test cohorts with temporally separated external tests to enable fair head to head comparisons and reproducibility [210].

### Clinician-centered, explainable AI

#### Co-design and usability

Co-develop solutions with radiologists, pathologists, oncologists, and nurses so that outputs align with clinical mental models, including risk categories with associated confidence, flags tied to clinically relevant thresholds such as PD-L1 near one percent or fifty percent, and concise rationales linked to recognizable clinical features [65]. Evaluate cognitive load and time to decision in simulated tumor boards and iteratively refine the user experience [34].

#### Interactive reasoning

Provide what if and counterfactual tools, link to exemplar cases, and allow threshold adjustment based on patient preferences. Enable selective automation by fully automating low risk, high confidence tasks while requiring human approval for high risk or low confidence outputs [211].

### Education and literacy

Incorporate AI literacy into oncology training, covering uncertainty interpretation, calibration, fairness trade offs, and the limits of generalization. Define competencies and credentialing, including safe overrides and adverse event reporting [212].

### Safety layers

Embed multilayer safeguards, including abstention based on OOD detection and UQ, fail safe defaults, automatic escalation for biomarker predictions near decision thresholds, and drift alarms that notify stakeholders before clinically meaningful degradation [213].

### Standardisation and equitable access

#### Standards and interoperability

Consolidate around ISBI for radiomics, adopt common staining and scanning protocols for digital pathology, and ensure interoperability through DICOM SR and DICOM SEG, FHIR, and CDS Hooks. Publish reference implementations and open test suites to promote reproducibility [15, 50].

### Equity by design

Proactively include underrepresented populations and sites in training and in external validation. Robust stratification within groups and equalized odds by sex, ancestry, socioeconomic status, and geography [49]. When disparities are detected, apply remediation through reweighting, domain specific adapters, or targeted data acquisition.

#### Low-resource deployment

Optimize for edge inference, minimize dependencies, and support offline operation. Provide tiered models matched to local infrastructure, and consider pooled procurement and public private partnerships to reduce costs [214].

#### Ethics and consent

Clearly consents for secondary use, empower governance bodies to evaluate cross-border data flows and legal alignment, and reinvest benefits from AI deployments to improve access and outcomes in the communities that contributed data [215].

Verified explainability should be treated as a first-class requirement. Foundation and cross-modal models for NSCLC should be deployed with verified explanations as first-class outputs, audited according to the minimum evidence package, and accompanied by site-level adapters that maintain both prediction and explanation stability. Prospective evaluations should include human-factors endpoints and automation-bias monitoring. Regulatory dossiers should treat explanation verification with the same importance as discrimination and calibration.

### Conclusions

AI is moving from proof of concept tools to clinically consequential tools in the NSCLC continuum [15]. Beyond matching specialist level accuracy on narrow tasks, the distinctive value of AI is to integrate high dimensional, multimodal, longitudinal information from radiology, pathology, multi omics, and electronic health records into calibrated, individualized inferences that humans cannot reliably integrate at scale [206]. When properly validated and deployed, AI can improve timing, including earlier detection and risk stratification; targeting, through more precise therapy selection with less futile toxicity; and throughput, by enabling standardized and efficient workflows that return clinician time to complex decisions [210]. Current evidence supports AI as an adjunct that enhances screening fidelity, histologic and molecular subtyping, prognostication, and prediction of treatment response and toxicity. However, heterogeneity in external performance, domain shift across scanners and laboratories, and variability in preanalytics mean that models should not be judged by AUROC alone;

---

<!-- Page 20 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:1018
Page 20 of 25

calibration, transportability, uncertainty awareness, and clinical net benefit are also required [15]. In practice, the more useful models generalize across settings with bounded performance loss, disclose uncertainty through selective prediction and abstention, and explain recommendations in clinically meaningful terms such as spiculation, necrosis, tumor infiltrating lymphocytes, and dose and volume drivers to support expert oversight [21, 21c].

Causal and mechanism-aware modeling is a key emerging area central to individualized therapy-response prediction [27]. Causal forests and uplift modeling estimate individual treatment effects under confounding and heterogeneity [28]. Mechanism-aware representation learning encodes biological and physical priors, improving transportability, interpretability, and safety under distribution shift [219]. Clinical credibility requires multicenter evaluation with preregistered analysis plans, geographically and temporally external test cohorts, decoupled-relevant metrics such as net benefit and reclassification, and calibration reported within subgroups and by site [28]. Prospective pilots and pragmatic trials that embed these methods in tumor-board workflows can translate predictions into actionable strategies that balance benefit and risk for each patient.

Looking forward, three inflection points stand out: first, multimodal foundation models tuned for NSCLC should replace fragmented single task pipelines and produce unified outputs from a shared backbone with parameter efficient site personalization; second, causal and longitudinal modeling should become standard by combining treatment effect estimators with dynamic risk models that update after each imaging assessment, ctDNA measurement, or laboratory test; third, AI derived computable biomarkers should advance along four qualification paths: (1) extrapolating from analytical validity and multicenter clinical validity to prospective demonstrations of clinical utility that inform trials, guidelines, and reimbursement [103, 118, 206, 209, 220]; (2) Clinical translation requires an explicit pathway. We recommend a validation ladder that begins with internal and external splits, advances to preregistered multicenter retrospective studies, and culminates in DECIDE AI prospective evaluations and pragmatic trials where feasible [28, 214, 221]. At every stage, report calibration and DCA alongside discrimination, define operating points tied to actions, and prescribe recalibration plans [60, 222]. Deployment should follow Software as a Medical Device principles with postmarket surveillance, drift monitoring, rollback triggers, and change control plans for learning systems [223]. In summary, beyond accuracy and calibration, expectations verified for faithfulness, stability, and clinical utility, integrated with uncertainty-aware selective workflows, are essential for adoption in

high-stakes NSCLC decisions. Our proposed minimum evidence package facilitates the implementation of this requirement.

#### Abbreviations

NSCLC Non-small cell lung cancerLDCT Low-dose computed tomographyEGFR Epidermal growth factor receptorAI Artificial intelligenceAI Machine learningCT Computed TomographyML Multiple instance learningPD-L1 Programmed Death Ligand 1H&E Hematoxylin and EosinFA Fourier attentionWA Wavelet AttentioncDNA Circulating tumor DNAGNNS Graph Neural NetworksAUCROC Area Under the Receiver Operating Characteristic CurvePET-CT Positron Emission Tomography-Computed TomographyMN Magnetic Resonance ImagingIBSI Image Biomarker Standardisation InitiativeLoG Laplacian of GaussianDCA Decision Curve AnalysisIHC ImmunohistochemistryWSI Whole-Slide ImagesTPS Tumor Proportion ScoreALK Anaplastic Lymphoma kinaseROS1 ROS proto-oncogene 1FL Federated LearningUQ Uncertainty QuantificationOOD Out-of-DistributionICC International Color ConsortiumDICOM Digital Imaging and Communications in MedicineFHR Fast Healthcare Interoperability Resources

#### Acknowledgements

Figures 1, 2, 3, 4 and 5 were created with BioRender.com.

#### Author contributions

Conceptualization, Shilong Song; Study design, Luyuan Chang; Manuscript draft, Luyuan Chang; Draft review and editing, Haping Li; Acquisition work, Wenzong Wu; Literature review and analysis, Xinyu Liu; Literature review and analysis, Jiayi Yan; Icon creation, Zuo Chen; Literature review and analysis, Huan Wu.

#### Funding

This work was supported by Natural National Science Foundation of China (82409939). Scientific Research Project of Anhui Province of Health Commission (AHM2022A39167), and Longhua Hospital Program (LH25010410).

#### Data availability

All data for this study have been provided.

#### Declarations

##### Ethics approval and consent to participate

Not applicable.

##### Consent for publication

The authors have seen and approved the final manuscript.

##### Competing interests

The authors declare that they have no competing interests.

#### Author details

1The First Department of Clinical Medicine (First Affiliated Hospital), Bengbu Medical University, Bengbu, Anhui, China

---

<!-- Page 21 -->

Chang et al. 
*Journal of Translational Medicine*
(2024) 24:1018
Page 21 of 25

†Department Mental Health, Bengbu Medical University, Bengbu, Anhui, China

‡The Department of Radiotherapy of the First Affiliated Hospital of Bengbu Medical University, Bengbu, Anhui, China

Received: 28 August 2023 / Accepted: 12 December 2023

Published online: 23 December 2023

References

1. 1. Laversanne M, Sung H, Fleyer J, Siegel RL, Siegelmannati E, et al. Global cancer statistics 2023.GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries: CA Cancer J Clin. 2023;73:429–72.
2. 2. Hendriks ELJ, Remijn J, Favre-Pinot E, Carassino MC, Heymans J, Kri Kern, et al. Non-small-cell lung cancer.Nat Rev Dis Primers. 2024;10:171.
3. 3. Wakelée H, Liberman M, Kato T, Tsuboi M, Lee SH, Gao S, et al. Periparegative pleburotomy for early-stage non-small-cell lung cancer.N Engl J Med. 2016;376:1991–503.
4. 4. Heymann AV, Harpole D, Mitsuhashi T, Taube JM, Galffy G, Hochman M, et al. Periparegory disubstruction for resectable non-small-cell lung cancer.N Engl J Med. 2023;381:181672–44.
5. 5. Kratzer TB, Bandi P, Fredman ND, Smith RA, Travis WD, Jemal A, et al. Lung cancer statistics, 2023.Cancer. 2024;124:1331–41.
6. 6. Frankell EM, Dietzen M, Al Bakir M, Lim A, Karasik T, Ward J, et al. The evolution of lung cancer and impact of subclonal selection in TACRON.Nature. 2013;506:7157–55–33.
7. 7. Al Bakir M, Huebner A, Martinez-Ruiz, Grigoriadis K, Watkins TBK, Pich O, et al. The evolution of non-small cell lung cancer metastases in TACRON.Nature. 2016;537:154–9.
8. 8. Accolla JN, Falconero GJ, Rajaguru P, Topol EJ. Multimodal biomedical AI.Nat Med. 2023;29:819–7.
9. 9. Wasaga A, Tripathi A, Ramachandran RP, Stewart PA, Rasco G. Multimodal data integration for oncology in the era of deep learning: a review.Front Artif Intell. 2024;7:140883.
10. 10. Mo CK, Li X, Chen S, Stornes E, Targino L, Costa ALN, Houston A, et al. Tumour evolution and microenvironment interactions in 2D and 3D spaces.Nature. 2024;543:1189–96.
11. 11. Sun ZG, Hong Z, Zhang C, Wang L, Han Z, Ma D. Immune checkpoint therapy for solid tumors: clinical dilemmas and future trends.Signal Transduct Target Ther. 2023;8:181;320.
12. 12. Wu J, Zhang B, Li W, Hu H, Jiang M, Cold and hot tumors: from molecular mechanisms to targeted therapy.Signal Transduct Targeted Ther. 2024;9:1274.
13. 13. Halliwell J, Geras A, Juzyba D, Safar Naeini A, Filipuk J, Raczkowska A, et al. Integrative spatial and genomic analysis of tumor heterogeneity in breast cancer.Thoracoscopia: Nat Commun. 2023;14:1000.
14. 14. Hill LM, Ilin, Weedle CC, Lee C, Augustin JM, Chen K, et al. Lung adenocarcinoma promotion by air pollutants: nature.2023;167:959–1153–67.
15. 15. Vorontsov E, Bodnar A, Casori A, Shalukov G, Zlechetskova M, Svejkova K, et al. A foundation model for clinical-geographical pathological analysis and rare cancers detection.Nat Med. 2024;30:43–55.
16. 16. Liang K, Josefsson V, Larsson AM, Larsson S, Hogberg C, Sartor H, et al. Artificial intelligence-supported screen reading versus standard double reading in the mammography screening with artificial intelligence trial (MASC): a clinical safety analysis of a randomized, controlled, non-inferiority, single-blind, screening accuracy study.Lancet. 2023;400:936–44.
17. 17. Eisenmann N, Banks S, Mumakul A, Baltus S, Elmer SA, Gormley T, et al. Nation-wide real-world implementation of AI for cancer detection in population-based mammography screening.Nat Med. 2023;13:1917–24.
18. 18. Michael PG, Wohlgemuth J, Yala A, Karstens L, Xiang K, Takigami AK, et al. Sybil: a validated deep learning model to predict future lung cancer risk from a single low-dose chest computed tomography (LDCT) scan.Med. 2024;10:2191–200.
19. 19. Vekalakis NV, Aleet TA, Scholten EM, Saghir Z, Shua M, Szeveliani A, et al. Prior ct improves deep learning for malignancy risk estimation of screening detected pulmonary nodules.Radiology. 2023;318:223318.
20. 20. Chen RL, Ding T, Li WW, Williamson SP, Jurkner G, Song AH, et al. Towards a general-purpose foundation model for computational pathology.Nat Med. 2023;30:850–62.
21. 21. Ito H, Yoshizawa A, Terada A, Nakagawa A, Rokutan-Kurata M, Sugimoto T, et al. A deep learning-based assay for programmed death ligand 1 immunohistochemistry scoring in non-small-cell lung carcinoma: does it help pathologists?Onco Med Pathol. 2023;16:104948.
22. 22. Campanella G, Kumar R, Nanda S, Singal S, Fluder E, Kwan R, et al. Real-world deployment of a deep learning pathology foundation model for lung cancer biomarker detection.Nat Med. 2025.
23. 23. Pavani D, Zompra-Petrides O, Clayton H, Burge S, Crispin-Ottaz M. Radiology and multi-scale data integration for lung oncology.NPJ Comput Med. 2024;10:158.
24. 24. Tran E, Eckardt N, Feber O, Kaiser HJ. Large language models and multimodal foundation models for precision oncology.NPJ Precis Oncol. 2024;10:172.
25. 25. Yeh J, Chen M, Chen Y, Gao G, Zou J, Jia L. Multimodal deep learning approaches for precision oncology: a comprehensive review.Briefings Bioinform. 2022;13:100.
26. 26. Calvo N, Leoussau M, Olhac F, Hovhanisyan-Baghdatian N, Lupion M, Wolf E, et al. Integration of clinical, pathological, radiological, and transcriptomic multi-omics data for precision immunotherapy in non-small-cell lung cancer.Nat Commun. 2021;16:1614.
27. 27. Chen LL, Wu MY, Wang J, Williamson DRG, Dicks D, Lindeman M, et al. Pathology and radiology for precision oncology using histopathology and genomic features for cancer diagnosis and prognosis.Elife Trans Med Imag. 2022;10:457–70.
28. 28. TIPODD AI statement. Updated guidance for reporting clinical predictions models that use regression or machine learning methods.BMJ. 2022;380:m1400.
29. 29. Wang K, He T, Yang Y. Fusion of generative adversarial networks and non-negative matrix factorization for depression fMRI data analysis.Inf Process Med. 2023;50:10961.
30. 30. Ke H, Wang B, F, H, H, Ma H, Wang G, Yin J. Unsupervised deep frequency-channel attention factorization for non-linear feature extraction: a case study of identification and functional connectivity interpretation of Parkinson's disease.Expert Syst Appl. 2024;243:128255.
31. 31. Wang H, Chen Y, Cai C, Chen Y, et al. A non-negative tensor network factorization for non-linear analysis and classification of fMRI data.Appl Soft Comput. 2023;115:103173.
32. 32. Wang K, He M, H, Tang T. Deep wavelet temporal-frequency attention for nonlinear MRI biomarker activation.AD: Pattern Recognit. 2023;165:11543.
33. 33. Wang H, Chen Y, Ma H, Yang Y, et al. Data-driven risk stratification and precision management of pulmonary nodules detected on chest computed tomography.Nat Med. 2024;30:113–84–95.
34. 34. Wendtner K, Krups J, Zauchus F, Wesel M. Effects of artificial intelligence implementation in oncology in medical imaging: a systematic literature review.Artif Intell Anal Med. 2024;124:10255.
35. 35. De Luca GR, Diciton S, Macaluso M. The pivotal role of baseline LDCT for lung cancer screening in the era of artificial intelligence.Arch Biomedoncol. 2023;16:639–47.
36. 36. Hendrix W, Hendrix N, Scholten EM, Mounts M, Tardje-Jong J, Schalekamp S, et al. Deep learning for the detection of benign and malignant pulmonary nodules in non-screening CT scans.Commun Med (Lond). 2023;12:156.
37. 37. Sarkar S, Pet PT, Abazeev M. Deep learning for automated, motion-resolved tumor segmentation in radiotherapy.NPJ Precis Oncol. 2025;9:173.
38. 38. Zhu S, Munier A, Zhang J, Liu J, Xiu, Zhou C, et al. Progress and challenges of artificial intelligence in lung cancer clinical translation.NPJ Precis Oncol. 2025;9:216.
39. 39. Wassettini L, Boes HC, Meyer MT, Padella M, Hinrich C, Sauter AW, et al. Total-Segmentation: robust segmentation of 104 anatomical structures in CT images.Radiother Oncol. 2023;193:104033.
40. 40. Link-KE, Schumraun Z, Liu C, Kwon Y, Jiang J, Tsai-Nsin-Mei M, et al. Longitudinal deep neural networks for assessing metastatic cancer risk on a large scale.Med. 2023;10:100.
41. 41. Rogasch JM, Machine-Learning L, Baumgartner GL, Frost N, Rücker JC, Neudecker J, et al. A machine-learning tool to improve prediction of metastatic lymph node involvement in non-small-cell lung cancer using routinely obtainable [18F]FDG-PET/CT parameters.Eur J Nucl Med Mol Imag. 2023;50:7216–51.
42. 42. Garg S, Garg S, Garg S, Garg S, Dey M, Chen P, Annu M, et al. Synchronous pet-ct for improved diagnosis and prognosis for lung cancer: proof of concept.Cell Rep Med. 2023;4:101463.

---

<!-- Page 22 -->

Chang et al. Journal of Translational Medicine

(2026) 24:1018

Page 22 of 25

43. Zhong Y, Cai C, Chen T, et al. H, Deng J, Yang M, et al. PET/CT based cross-modal deep learning signature to predict occult nodal metastasis in lung cancer. Nat Commun. 2023;14(1):513.

44. Koester M, Matrozdiallo D, Szwarcfroytz TP, van der Werf NR, Wang AS, Sandfort V, et al. Deep learning image reconstruction for ct technical principles and clinical prospects. Radiology. 2023;230(2):125.

45. Yu P, Zhang H, Wang D, Zhang R, Deng M, Yang H, et al. Spatial resolution enhancement using deep learning improves chest disease diagnosis based on thick slice CT. NPI Dig Med. 2023;10(1):13358.

46. Horvath N, Papakonkaou L, Koh DM. Radomics beyond the hype: a critical discussion toward oncologic clinical use. Radiol Artif Intell. 2024;6(4):30437.

47. Cobo M, Menéndez Fernández-Miranda P, Batarrika G, Ureña Gilestia L. Enhancing radiomics and deep learning prospects through the standardization of medical imaging workflows. Front Med. 2024;11(1):1000001.

48. Pai S, Bontempi D, Hadzi C, Puente V, Soakal M, Chauvin TL, et al. Foundation models for cancer imaging biomarkers. Nat Mach Intell. 2024;6(3):154–67.

49. Zhang H, Zhan H, Ghoroghji N, Hadzi C, Puente V, et al. The limits of fair medical AI in real-world generalization. Nat Med. 2024;30(3):1283–8.

50. Winyard P, Zwanenburg M, van der Werf NR, et al. A survey. Inf Inf Technol. 2024. The image biomarker Standardization Initiative: standardized convolutional filters for radiomic radiolomics and enhanced clinical insights. Radiology. 2024;310(2):310223–3119.

51. Collins GS, Dhanan P, M, A, Schlüssel MM, Archer L, Van Calster B, et al. Evaluation of clinical prediction models: part (1): from development to external validation. Biom J. 2024;38(4):607–819.

52. Vasey B, Collins GS. Implied commentary: transparent reporting of artificial intelligence models developed for clinical prediction. BMJ. 2024;617(5592):e142622.

53. Sweeney K, Kallenberg M, Deyo R, Deyo R, Y, Graessler M. Checkov and SPECTRE fairness gaps in deep chest X-ray classifiers. Pac Symp Biocomput. 2021;2622–32.

54. Christensen F, Komuk A, Ganesan AR, Welch R, Palés-Huix J, Czekierdowski A, et al. International multicenter validation of AI-driven ultrasound detection of ovarian cancer. Nat Med. 2023;29(1):189–96.

55. Xiang H, Xiao L, Ye L, Li C, et al. A systematic development and validation of an interpretable model integrating multi-modal information for improving ovarian cancer diagnosis. Front Med. 2023;10(1):206.

56. Ying H, Liu X, Zhang M, Ren Z, Zhen S, Wang X, et al. A multicenter clinical AI system study for detection and diagnosis of focal liver lesions. Nat Commun. 2023;14(1):151.

57. Xenea I, Wiles J, Albuquerque J, Rebuffa S, Tanno A, Rino AG, et al. Generative models improve fairness of medical classifiers under diversity shifts. Nat Med. 2024;30(4):1166–73.

58. Koch LM, Baumgartner CF, Beeres P. Distribution shift detection for the postmarketing surveillance of medical algorithms: a retrospective simulation study. NPI Dig Med. 2024;7(1):120.

59. Qian X, Lu W, Zhang J. Adaptive wrapper-Net for single-sample test time adaptation in medical and bio. bioact. Inform Phys. 2024;5(1):82805–81.

60. Collins GS, Moons KGM, Dhanan P, Riley RD, Beaul A, Van Calster B, et al. TRIPOD-4: statement: updated recommendations for reporting clinical prediction models that use regression or machine learning models. BMJ. 2024;388(8678):78.

61. Gallifant J, Ashrafi M, Amershi S, Aghinyazhpzhong Y, Chen S, Cacciaman GM, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2023;29(1):69–89.

62. Vickers AJ, Holand F. Decision curve analysis to evaluate the clinical benefit of prediction models. Spine J. 2021;10(1):1643–48.

63. Amerson N, Tyfossen D, Hofhouwer B, et al. Rago M, van Leeuwen KG. Artificial intelligence in radiology. 2023. commercially available products and scientific evidence. Front Med. 2023;10(1):623919.

64. Singh R, Bapna M, Dabir RA, Suli AZ, Lotter W. How AI is used in FDA authorized medical devices: a taxonomy across 1, 016 authorizations. NPI Dig Med. 2024;8(1):138.

65. Chae A, Yo MS, Sargeya H, Goldberg AD, Chatterjee N, Maclean MT, et al. Strategies for implementing machine learning algorithms in the clinical use of radiology AI. Front Med. 2023;10(1):923710.

66. Farl N, Hinder S, Williams R, Ramare R, Bernabeo MD, van Beek E, et al. Early emergence of integrating AI in radiology: a systematic review. Front Syst Support Syst in radiology settings: a qualitative study. J Am Med Inf Assoc. 2023;11(2):124–34.

67. Geerigzi J, Aghazadeh A, Brown A, Stanton C, Helm E, Jajayakou S, et al. Software using artificial intelligence for nodule and cancer detection in CT lung cancer screening: systematic review of test accuracy studies. Thorax. 2024;79(11):1040–9.

68. Jorg T, Hoffmann MC, Stoeher F, Arnold H, Theedbad A, Mildenberger P, et al. A novel report workflow for automated integration of artificial intelligence results into structured radiology reports. Insights Imag. 2024;5(1):80.

69. Tanno S, Barrett DGF, Seligman A, Chakrati S, Sathari S, See K, et al. Collaboration between clinicians and vision-language models in radiology report generation. Nat Med. 2024;30(5):999–68.

70. Ehteshami O, Seo H, Choukas K, Deyo R, Pagar M, Salanti G. Developing clinical prediction models: a step-by-step guide. BMJ. 2024;388(86726):e142622.

71. Ehteshami O, Seo H, Choukas K, Deyo R, Pagar M, et al. Assessing the Trustworthiness of saliency maps for localizing abnormalities in medical imaging. Radiol Artif Intell. 2021;3(6):2020027.

72. Hutter M, Schödl M, Schödl M. Interpreting perturbation-based saliency maps for explaining ariari agents. Front Artif Intell. 2022;5:93075.

73. Alnagari N, El Bakhri Menai M, Mathiouth R, Almoullali L. Exploring evaluation of clinical prediction models. Front Artif Intell. 2024;9(1):122.

74. Gao Y, Zhou Z, Hong PL, Panchi L, et al. S-Lens: using occlusion-based saliency maps to explain an artificial intelligence tool in lung cancer screening. Front Artif Intell. 2024;9(1):122.

75. Passaro A, Al Baker M, Hamilton SE, Dehlin M, Andrade F, Roy-Choudhury S, et al. Biomarkers: emerging trends and clinical implications for personalized treatment. Cell. 2024;167(7):1617–35.

76. Kluch D, Wang Y, Ahmad W, Boychuk A, Fukuda J, Galka K, et al. Next-generation methods for the analysis of high-dimensional data: evaluation of diagnostic and prognostic algorithms. Cell Rep. 2024;59(10):10697.

77. Xue X, Wang Y, Ahmad W, Boychuk A, Kluch D, Kallenberg R, Hewitt K, et al. Regression-based deep learning predicts molecular biomarkers from pathology slides. Nat Commun. 2024;15(1):223.

78. Arnold S, Ramanaraju M, Chen L, Buschert U, Yama M, Samec T, et al. Predicting ROS1 and alk fusions in NSCLC from H&E slides with a two-step vision transformer approach. NPI Precis Oncol. 2023;5(1):266.

79. Xue X, Wang Y, Ahmad W, Boychuk A, Kluch D, Kallenberg R, et al. A whole-slide foundation model for digital pathology from real-world data. Nature. 2024;630(8103):666–71.

80. van Kolkhooften HJ, van Oortchot T. The eu artificial intelligence Act (2024). Implications for Healthcare. Health Policy. 2024;149(1):152.

81. Lutz B, Schödl M, Chen L, Buschert U, Yama M, Chow AK, et al. A multi-modal generative AI copilot for human pathology. Nature. 2024;630(8103):666–71.

82. McCracken C, Clarke LE, Jennings S, Matthews G, Cartwright E, Fredah-Ajayee H, et al. Artificial intelligence in digital pathology: a systematic review and meta-analysis. Front Med. 2024;11(1):1000001.

83. Howard PM, Dolezal J, Kochany S, Schulte J, Chen H, et al. Let the impact of artificial intelligence in digital pathology on severe covid-19 mortality accuracy and bias. Nat Commun. 2021;12(1):444.

84. DeGrave AJ, Janicki JD, Lee S, et al. A radiographic DIO-1 prediction selects strongly for survival. Front Med. 2020.

85. Häggle M, Seegerin P, Lapuchinsky S, Bockmayer M, Samwel J, Klauschnig F, et al. Resolving challenges in deep learning-based analyses of histopathological images using explanation methods. Sci Rep. 2020;10(1):6423.

86. Kothari J, Shah N, Igle H, Stoles TE, Ousukova AO, Young AN, Wang MD. Removing bias effects from histopathological images for enhanced cancer diagnosis. EJHE. 2020;16(1):837–50.

87. Nakamura T, Watanabe T, Aizawa N, Hata K, Kataoka K, Yokota M, et al. cDNA-based molecular residual disease and survival in resectable colorectal cancer. Nat Med. 2023(1):1327–32.

88. Sober S, Kim H, Kim H, Kim H, Park K, et al. Progenetic and phenotypic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment. Nat Commun. 2024;15(1):1016.

89. Wang M, Wang M, Wang M, Wang M, Wang M, et al. Multi-omics analytics reveal biological and clinical insights in recurrent stage II non-small cell lung cancer. Nat Commun. 2024;15(1):1477.

90. Wang M, Wang M, Wang M, Wang M, Wang M, et al. Auto-supervised interpretable deep learning framework for cancer survival analysis incorporating clinical and molecular data. Front Med. 2024;11(1):1000001.

91. Ing A, Andreakis A, Cosenza MR, Korbel JO. Integrating multimodal and multi-omics data using deep variational path modelling. Nat Mach Intell. 2025;7(10):153–7.

---

<!-- Page 23 -->

Chang et al. 
*Journal of Translational Medicine*
 (2026) 24:1018

Page 23 of 25

42. Hartman, S., Scott, A.M., Karlsson, C., Mohanty, T., Vasta, S.T., Linde, A. et al. Interpreting biologically informed neural networks for enhanced proteomic biomarker discovery and pathway analysis. Nat Commun. 2023;14(1):3539. https://doi.org/10.1038/s41467-023-45810-1

43. Hong, Z. et al. A survey of CNN applications for oncology in the past decade with a focus on cancer registry applications. Artif Intell Rev. 2025;58(1):63-114.

44. Hong, Z., Yuan, Y., Chen, L., Hu, L., Wang, M.H. et al. Out-of-distribution detection in medical image analysis: a survey. ArXiv. 2024a;arXiv:2404.18279.

45. Hong, Z., Hondelink, L., Suranawick, A., Mohanty, N., Maastricht, J.H. MindPT: transformers for histology image analysis. J Pathol Inf. 2023;2023:100386.

46. Hong, Z., Stamou, J.C., Hong, Z., Suranawick, A., Pandian, N., Maastricht, J.H. MindPT: a high-performance system for robust stain normalization of whole-slide images in histopathology. Front Med (Lausanne). 2021;8:6193.

47. Kwon, J.A., Von Custer, B., Kwon, J.A., Kwon, J.A. Deep learning curve analysis: confidence intervals and hypothesis testing for net benefit. Diagn Progn Res. 2023;17(1):11.

48. Steegman, S., Qiu, Y.L., Zheng, Y., Mukherjee, P., Vogel, G. Multimodal brain learning to predict prognosis in adult and pediatric brain tumors. Commun Med. 2023;2(1):14.

49. Tian, R., Hou, F., Zhang, H., Yu, G., Yang, P. J. U. et al. Multimodal fusion model for prognostic prediction and radiotherapy response assessment in head and neck squamous cell carcinoma. Med Phys. 2023;50(12):123304.

50. Sui, S.J., Aminu, M., Kapurte, T., Chen, P., Saad, M.B., Saeblighofer, M. et al. Enhancing NSCLC recurrence prediction with PET/CT and histology data. Cell Commun Tissue Res. 2023;316(1):1-15.

51. Tsai, M., Hsueh, R.S., John, T., Kato, J., Majum, M., Grohe, C. et al. Overall survival with osimertinib in extended EGFR-NSCLC. J Clin Oncol. 2014;32(1):137-47.

52. Anastasio, V. H., Hou, N., Nichols, G., Jagers, R., Sacher, A. F., Eng, A. J. et al. cDNA response after pembrolumab in non-small-cell lung cancer: phase 2 adaptive-trial results. Nat Med. 2023;29(2):359-69.

53. Assaf, Z.F., Zou, F., Em, A.D., Sosnicki, M.A., Young, A. D. et al. Longitudinal circulating tumor DNA-based model associated with survival in metastatic non-small-cell lung cancer. Med Phys. 2023;50(12):123305.

54. Ding, H., Xuan, Y., Xiang, Y. Q. X. S. Identifying key circulating tumor DNA parameters for predicting clinical outcomes in metastatic non-squamous non-small cell lung cancer after first-line chemotherapy. Nat Commun. 2024;15(1):6862.

55. Jee, J., Feng, C., Pochton, C., Tran, T.N., Luthra, A., Waters, M. et al. Automated real-world data integration improves cancer outcome prediction. Nature. 2024;638(8047):78-86.

56. Orcutt, X., Chen, K., Matrang, L., Long, P., Karkh, R.B. Evaluating generalizability of oncology trial results to real-world patients using machine learning-based simulations. Nat Med. 2023;29(5):745-55.

57. Deraza, B., Breda, G., Kempf, C., Baekke, F., Cotte, F., Reiche, C. et al. New regulatory thinking is needed for AI-based precision drug and cell therapies in precision oncology. PNP Oncol Dis. 2024;20(1):123.

58. Jayaraman, P., Desai, J., Sabuncu, M., Nadim, G.H., Salkhaji, A. A Primer on Reinforcement Learning in Medicine for clinicians. NPJ Digit Med. 2024;7(3):37.

59. Tosca, E.M., De Carlo, A., Ronchit, D., Magini, P. Model-informed Reinforcement learning for enabling precision dosing via adaptive Dosing. Clin Pharmacol Ther. 2024;116(6):916-39.

60. Aza, A., Alderman, E.J., Palmer, J., Ganapathi, S., Lavre, A., McCadden, M.D. et al. The value of standards for health datasets in artificial intelligence-based applications. Nat Med. 2023;29(11):12939-48.

61. Aza, M., Mirzian, T., Lavre, E. Navigating the age of AI: implications for regulated digital medical products. NPJ Digit Med. 2024;7(3):37.

62. Chen, B., Shi, J., Huang, L., Feng, S. J. U. et al. Robustly federated learning model for identifying high-risk patients with postoperative gastric cancer recurrence. Nat Commun. 2024;15(1):742.

63. Pan, D., S. Y. V. A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A., A

---

<!-- Page 24 -->

Chang et al. Journal of Translational Medicine (2026) 24:108

Page 24 of 25

137. She Y, He B, Wang F, Zhong Y, Wang T, Liu Z, et al. Deep learning for predicting major pathological response to neoadjuvant chemotherapy in non-small cell lung cancer: a multicenter study. BioMedicine. 2022;8:10484. https://doi.org/10.1016/j.biomed.2022.10484

138. He B, Bansal M, Iyeron N, Cant L, Vella L, Kuhl B, et al. Decoding the “gloypotent”: a new frontier for biomarker discovery in cancer. J Hematol Oncol. 2024;17:112.

139. Lotter W, Hassett MJ, Schultz N, Kehl KL, Van Elm EM, Crenari E. Artificial intelligence in oncology: current landscape, challenges, and future Directions. Cancer Discov. 2024;14:671–76.

140. Schneider JL, Lin J, Shaw AT. AI: positive lung cancer: a moving target. Nat Rev Cancer. 2023;23:30–42.

141. Lou N, Gao R, Shi N, Han K. Plasma metabolomics profiling of EGFR-mutant non-small cell lung cancer treated with third-generation EGFR-TKI in Data. Cell. 2011;131:1369.

142. Huang D, Li Z, Jiang T, Yang C, Lin N. Artificial intelligence in lung cancer: current applications, future perspectives, and challenges. Front Oncol. 2024;14:683101.

143. Panchard D, Jhnie PA, Cheng Y, Jiang C, Yanagitani N, Kim SW, et al. Osimertinib with or without chemotherapy in EGFR-mutated advanced NSCLC. N Engl J Med. 2023;389:1935–48.

144. Berko EK, Wetk GM, Mataria S, Petrova ZO, Wu MA, Smith CM, et al. Circulating tumor DNA reveals a novel driver mutation in EGFR-mutated advanced NSCLC. N Engl J Med. 2016;374:200–10.

145. Cai Z, Apolinario S, Balao AR, Pacini C, Susa MD, Vinga S, et al. Synthetic augmentation of cancer cell line multi-omic datasets using unsupervised deep learning. Nat Commun. 2023;14:1201.

146. Hong L, Aminu M, Liu S, Lu Y, Petronas M, Saad MB, et al. Efficacy and oncologic non-comparative phase II study of immune-checkpoint inhibitors and chemotherapy in non-small cell lung cancer. Nat Commun. 2024;15:141695.

147. Parra ER, Zhang J, Jiang M, Tamegawa A, Panduramam RK, Behrens C, et al. Immune cellular patterns of distribution affect outcomes of patients with non-small cell lung cancer. Nat Commun. 2023;14:1294.

148. Rakusa M, Tafevoghji M, Khatibzadeh A, Khatibzadeh A, Garrelle F, et al. Deep learning model for predicting immunotherapy response in advanced non-small cell lung cancer. JAMA Oncol. 2023;13(12):1018–18.

149. Delatos L, Khorami M, Vawaragane VS, Jazien K, Ding Y, Muhta P, et al. Novel radioimmunology approach to predict and characterize pneumonia in stage II NSCLC. N Engl J Med. 2023;389:1090.

150. Saad MB, Athan P, Qong L, Yernay L, Lu Y, Boslaky D, et al. Machine-learning driven strategies for adapting immunotherapy in metastatic NSCLC. Nat Commun. 2023;14:16823.

151. Abramson J, Adler J, Dunger J, Evans R, Green P, Pitzel A, et al. Accurate structure prediction of covalent interactions with AlphaFold 4. Nature. 2024;630(8101):493–500.

152. Salybekov AV, Katinin V, Conover J, et al. Approaches sharing streaming drug discovery. Nature. 2024;630(8101):493–500.

153. Chmikelec K, Mok T, Wu H, Yan JH, Ahn MJ, Ramalingam SS, et al. Analysis of acquired resistance mechanisms to osimertinib in patients with EGFR-mutated advanced non-small cell lung cancer from the AURA3 trial. Nat Commun. 2023;14:1107.

154. Zhou R, Liu Z, Wu T, Pan T, Li C, Mao K, et al. Machine learning aided discovery of T790M mutant EGFR inhibitor CDDO-Me effectively suppresses non-small cell lung cancer growth. Cell Commun Dis. 2021;6:1585.

155. Xia S, Sun H, Huang H, Jin LW. Drug repurposing for cancer therapy: Signal Transduct Target Ther. 2024;9:192.

156. Zhao Y, Xing Y, Zhang Y, Xing Y, Wan M, Y.T, et al. Evidential deep learning-based drug target interaction prediction. Nat Commun. 2023;14:16915.

157. Chen S, Kuperus R, Müller M, Künzli M, Dohm J, Dohm J, et al. Machine learning: Perception predicts patient response and resistance to treatment using single-cell transcriptomics of their tumors. Nat Cancer. 2024;56:938–52.

158. Mellinga M, Wadd M, Barowski J, Kohnsberger M, Lethemmer M, Ovesko F, et al. Predicting locations of cryptic pockets from single protein structures using the PocketMixer graph neural network. Nat Commun. 2023;14:1177.

159. Soshan N, Tavelier C, Baudin C, Gaudin D, J. J. R. Vasquez-Perez J, et al. Artificial intelligence-powered discovery of small molecules inhibiting T-cell and cancer B-cell responses. Nat Commun. 2023;14:1177.

160. Lawrence PJ, Burns N, Jiang X. Enhancing drug and cell line representations via contrastive learning for improved anti-cancer drug prioritization. NPJ Precis Oncol. 2024;8:116.

161. Shi Y, Hu X, Zhang Q, Cheng S, Sun P, Zhang Q, et al. DISGREP: a webserver for deep learning-guided drug sensitivity prediction and drug response information retrieval for EGFR-mutated-driven lung cancer. Brief Bioinform. 2024;25:1.

162. Zhang Q, Yang X, Wang Y, Liu Y, Huang L, Liu C, et al. Artificial intelligence in drug development. Nat Med. 2023;29(11):161–69.

163. Sheridan RP, Time-slice X, Wang Y, Huang L, et al. A method for estimating the goodness of prospective prediction. J Chem Inf Model. 2023;63:6478–90.

164. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

165. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

166. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

167. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

168. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

169. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

170. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

171. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

172. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

173. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

174. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

175. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

176. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

177. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

178. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

179. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

180. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

181. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

182. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

183. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

184. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

185. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

186. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci. 2014;369(1241):1101–11.

187. Ashpri R, Hughes-Oliver JA. Cheminform. 2023;15(11):102.

188. Dabholi R, Nunez J, Wang X, Zhang M, Farns S, Painsi J, Zha H, et al. Higgs in the assay: chemical mechanisms of assay interference and promiscuous enzyme inhibition studied using a lyophilic F-scanvenging HTS. J Med Chem. 2015;58(20):1191–9.

189. Handa T, Thomas MM, Kagalagawa J, Bimber J, et al. On the difficulty of valuing the value of a drug. Philos Trans R Soc B Biol Sci

---

<!-- Page 25 -->

Chang et al. 
*Journal of Translational Medicine*
(2026) 24:108
Page 25 of 25

183. Abpaul G, Hölder A, Chelly Dasgupta Z, Zeitelou K, Monnett S. Should models be explainable to clinicians? Criv Care. 2024;28(1):301.

184. Nagendran M, Foster P, Komorowski M, Gordon AC, Fasal AQ. Quantifying the effect of AI recommendations with explanations on prescription decision making. NPI Digi Med. 2023;3(1):296.

185. Liu X, Liu Z, Cheng J, Xu C, Wang D. Improving explainability and integrability of medical AI to promote health care professional acceptance and use: mediating systematic review. Med Internet Res. 2025;27:e37374.

186. Dujstheijn KD, Winkens J, Barbaresi H, Ghazan S, Starrett N, Pawlowski N, et al. Enhancing the reliability and accuracy of AI-enabled diagnosis via a self-supplementary-driven iterative feedback loop. Nat Med. 2024;30(1):117.

187. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE AI. Nat Med. 2022;28(5):924–33.

188. Roth CJ, Petersen C, Clunz D, Towbin AJ, Cram D, Primo R, et al. HMSS-SIM (Healthcare Impact Modeling System) for clinical reflections and future Directions. J Am Imp Med. 2024;37(2):e242–3.

189. Van Calster I, Meleis AI, Van Den Heuvel M, Wynants L, Steyerberg EW. Validation: the Achilles' heel of predictive analytics. BMC Med. 2017;17(1):120.

190. Filnayou SS, Subbawaraya S, Singh K, Bowers J, Kupke A, Zittman J, et al. The clinician and data scientist: a conceptual framework. Artif Intell Med. 2018;105:281–98.

191. Zhu Z, Zhang XY, Cheng Z, Liu CL. Revisiting confidence estimation: towards reliable failure prediction. IEEE Trans Pattern Anal Mach Intell. 2024;46(5):3770–87.

192. Peepal R, J. 2025;19:8838.

193. Tejan AI, Cook TS, Husain M, Siepel Schmidt T, D'onnell ML. Integrating and adopting AI in the radiology workflow: a Primer for clinicians and integrating the healthcare Enterprise (HE) profiles. Radiology. 2024;310(2):e26253.

194. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE AI. Nat Med. 2022;28(5):924–33.

195. Pencia N, D'Agostino RB Sr, Demer OV. Novel metrics for evaluating improvement in discrimination: net recalculation and integrated-adequacy improvement for normal variables and nested models. Stat Med. 2021;40(13):2101–13.

196. Van der RD, Collins GS. Stability of clinical prediction models developed using statistical or machine learning methods. Biom J. 2023;65(2):e200320.

197. Hussain D, Drummond MJ, Augustowski F, de Bekker-Goubé S, Briggs AJ, Carswell E, et al. Consolidated health economic evaluation reporting standards 2022 (cheers 2022) statement: updated reporting guidance for health economic evaluations. Manag Care Spec Pharm. 2022;20(2):146–5004.

198. Zhou K, Gattiger G. The evolving regulatory paradigm of AI in MedTech: a review of perspectives and where we are today. Ther Innov Regul Sci. 2024;58(3):456–64.

199. Singh V, Cheng S, Kwan AC, Elinger J. United Food and Drug Administration regulation of clinical software in the era of artificial intelligence and machine learning. Mayo Clin Proc Digit Health. 2023;93(10):100231.

200. Wells BJ, Nguyen HH, McWilliams A, Pallab M, Bovi A, Kuzma K, et al. A practical framework for appropriate implementation and review of artificial intelligence (FAIR AI) in healthcare. NPI Digi Med. 2022;6(1):514.

201. Yu AC, Michaye B, Ergi E. External validation of deep learning algorithms for radiologic diagnosis: a systematic review. Radiol Artif Intell. 2022;4(3):e20094.

202. Campagnoli G, Kumar N, Nanda S, Singh S, Fluder E, Kwan R, et al. Real-world deployment of a fine-tuned pathology foundation model for lung cancer radiology detection. Nat Commun. 2023;14(1):3002–10.

203. Vickers AJ, van Calster B, Steyerberg EW. A simple, step-by-step guide to interpreting decision curve analysis. Diagn Progn Res. 2019;13:1.

204. Wolbers M, Bünche R, Koller MT, Wittenham K, Gentsi TA. Concordance for prognostic models with competing risks. Biostatistics. 2014;15(3):526–39.

205. Rozsuh P, Sun H, Wang F, Fan P, Gao Y, Massel M, Vera Garcia DJ, Singh Y, et al. Mitigating bias in radiology machine learning. J Data handling Radiol Artif Intell. 2022;6(3):20250.

206. Moan B, Barisiewicz O, Akad ZSA, Krumholz M, Leskovsek J, Topol EJ, et al. Foundation models for generative artificial intelligence. Nature. 2022;616(7995):239–45.

207. Laubacher R, Mehradi S, Shmulevich I, Trayanova V. Digital twins in medicine. Nat Comput Sci. 2024;4(1):84–91.

208. Li H, Han Z, Sun H, Wang F, Fan P, Gao Y, et al. Cynegic: explainable graph neural network framework with attention mechanisms for cancer gene module discovery. Front Genet. 2024;15(1):135. https://doi.org/10.3389/fgene.2024.135. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11450760/.

209. Feuerstein S, Frauen W, Melnychuk K, Schweisslietl J, Hess S, Curth A, et al. Casual machine learning for predicting treatment outcomes. Nat Med. 2024;30(1):117.

210. Perez-Goffard R, Ghanati-Lahen N, Mahmoudi de Kather J-N. A guide to artificial intelligence for cancer researchers. Nat Rev Cancer. 2024;24(6):427–41.

211. Ghanati-Lahen N, Perez-Goffard R, Ghanati-Lahen J, Dreyer KJ, et al. A visual-language foundation model for computational pathology. Nat Med. 2024;30(1):117.

212. Car J, Ong ZC, Erilich FH, Lehighly D, Kemp S, Svob K, et al. The digital health foundation model in medical education: framework an interna-external evaluation. Front Med. 2024;11(1):135. https://doi.org/10.3389/fmed.2024.953313.

213. Sahlen J, Jaskar J, Wahlh AK, Edwards S, Glenan E, H. R, et al. Application of simultaneous uncertainty quantification and segmentation for oopharyngeal cancer use-case with Bayesian deep learning. Commun Med (Lond). 2024;9(1):10.

214. Han GR, Ghorchavar A, Eyrilmaz S, Yee S, Palaniyami S, Ghosh R, et al. Machine learning in ophthalmology: a review of innovations, challenges, and opportunities. Nat Commun. 2025;16(1):11665.

215. Gibert S. The EU passes the AI Act and its implications for digital medicine are unclear. NPI Digi Med. 2024;10(1):135.

216. Zhou Q, ZH, Y. H, Peng S. Clinical impact and quality of randomized controlled trials involving veterans evaluating artificial intelligence prediction models: a systematic review. NPI Digi Med. 2021;4(1):154.

217. Athey S, Tibshirani J, Wagner S. Generalized random forests. Ann Stat. 2018;46(2):1148–74.

218. Binuya MAE, EngaardtEG, Schuas W, Schmidt MK, Steyerberg EW. Methodological guidance for the evaluation and deployment of clinical prediction models: a systematic review. BMC Med Res Methodol. 2022;22(1):116.

219. Vasey B, Nagendran M, Campbell B, Clifton D, Collins S, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE AI. BMJ. 2022;376(8407):n9094.

220. Campagnoli G, Kumar N, Nanda S, Singh S, Fluder E, Kwan R, et al. Real-world deployment of a fine-tuned pathology foundation model for lung cancer biomarker detection. Nat Med. 2023.

221. Martinides AP, Dellewijn CD, de Visser RO, Nag H, Njar V, Kals AL, et al. Concordance of randomised controlled trials for artificial intelligence interventions with the CONSORT-AI reporting guidelines. Nat Commun. 2024;15(1):619.

222. Liu Z, Scatche T, Pouchere P, Ouyang Y, Egovana N, Freeman R, et al. Assessing calibration and bias of a deployed machine learning multination prediction model within a large healthcare system. NPI Digi Med. 2023;6(1):149.

223. Hills HJ, Vasey JJ, Cliff ERS, van de Geest-Aspers K, Bizzo R, Dreyer KJ, et al. The latent pre-cancer challenge of regulating artificial intelligence in radiology. NPI Digi Med. 2024;7(1):69.

## Publisher's Note

This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, provided that you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.