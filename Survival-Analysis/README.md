# Survival Analysis: A Comprehensive Review

## Notebooks
*   [01. Basic Survival Analysis (KM, Cox PH)](01_Basic_Survival_Analysis.ipynb)
*   [02. Machine Learning Survival Analysis (RSF, Gradient Boosting)](02_ML_Survival_Analysis.ipynb)
*   [03. Deep Learning Survival Analysis (DeepSurv)](03_Deep_Learning_Survival_Analysis.ipynb)

## Table of Contents
1. [Introduction](#1-introduction)
2. [Fundamental Concepts](#2-fundamental-concepts)
3. [Traditional Statistical Methods](#3-traditional-statistical-methods)
4. [Machine Learning Approaches](#4-machine-learning-approaches)
5. [Deep Learning for Survival Analysis](#5-deep-learning-for-survival-analysis)
6. [Evaluation Metrics](#6-evaluation-metrics)
7. [Key Libraries and Tools](#7-key-libraries-and-tools)
8. [References and Further Reading](#8-references-and-further-reading)

---

## 1. Introduction

Survival Analysis (SA), also known as time-to-event analysis, reliability analysis (engineering), or duration analysis (economics), is a branch of statistics for analyzing the expected duration of time until one or more events happen, such as death in biological organisms and failure in mechanical systems.

Unlike standard regression problems where the target variable is always observed, survival analysis deals with **censoring**—where the event of interest has not occurred for some subjects during the observation window.

---

## 2. Fundamental Concepts

### 2.1. The Target Variable ($T$)
The random variable $T$ represents the time until the event of interest. It is strictly positive ($T > 0$).

### 2.2. Censoring
Censoring occurs when we have some information about individual survival time, but we do not know the survival time exactly.
*   **Right Censoring**: The most common type. The event has not occurred by the end of the study, or the subject is lost to follow-up. We know $T > C$ (where $C$ is the censoring time).
*   **Left Censoring**: The event occurred before the study started, and we don't know exactly when.
*   **Interval Censoring**: We know the event occurred between two time points ($t_1 < T < t_2$).

### 2.3. Key Functions
1.  **Survival Function, $S(t)$**:
    The probability that a subject survives longer than time $t$.
    $$S(t) = P(T > t)$$
    Properties: $S(0) = 1$, $S(\infty) = 0$, non-increasing.

2.  **Hazard Function, $h(t)$** (Hazard Rate):
    The instantaneous rate at which events occur, given no event occurred up to time $t$.
    $$h(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t | T \ge t)}{\Delta t} = \frac{f(t)}{S(t)}$$

3.  **Cumulative Hazard Function, $H(t)$**:
    The total accumulated risk up to time $t$.
    $$H(t) = \int_0^t h(u) du = -\ln(S(t))$$

---

## 3. Traditional Statistical Methods

These methods form the foundation of the field and are primarily focused on inference and understanding relationships between variables.

### 3.1. Non-Parametric Methods
Used when we make no assumptions about the underlying distribution of survival times.
*   **Kaplan-Meier Estimator**: The standard for estimating the survival function $S(t)$. It handles right-censoring effectively by recalculating survival probabilities at each distinct event time.
*   **Nelson-Aalen Estimator**: Used to estimate the cumulative hazard function $H(t)$.
*   **Log-Rank Test**: A hypothesis test to compare the survival distributions of two or more groups (e.g., Treatment vs. Control).

### 3.2. Semi-Parametric Methods
*   **Cox Proportional Hazards (PH) Model** (1972):
    The most widely used multivariate approach.
    $$h(t|x) = h_0(t) \exp(\beta^T x)$$
    *   **Assumptions**: The hazard ratio between two subjects is constant over time (Proportional Hazards Assumption).
    *   **Key Feature**: It leaves the baseline hazard $h_0(t)$ unspecified, focusing on estimating the effect of covariates ($\beta$).
    *   **Estimation**: Uses Partial Likelihood Estimation.

### 3.3. Parametric Methods
Used when the survival time distribution is known to follow a specific theoretical distribution.
*   **Accelerated Failure Time (AFT) Models**: Assume covariates accelerate or decelerate the life course of an event.
*   **Distributions**:
    *   *Exponential*: Constant hazard rate (memoryless).
    *   *Weibull*: Monotonic hazard rate (increasing/decreasing/constant).
    *   *Log-Normal*, *Log-Logistic*, *Gamma*.

---

## 4. Machine Learning Approaches

Traditional methods like Cox PH assume linear relationships between log-hazard and covariates. ML methods relax these assumptions to model complex, non-linear interactions.

### 4.1. Tree-Based Methods
*   **Survival Trees**: Adapted decision trees using splitting criteria like the Log-Rank statistic to maximize survival difference between child nodes.
*   **Random Survival Forests (RSF)** (Ishwaran et al., 2008):
    *   Ensemble of survival trees.
    *   Computes the Cumulative Hazard Function (CHF) for each tree and averages them.
    *   Handles high-dimensional data and non-linear effects automatically.
    *   **Metric**: Minimizes prediction error using C-index or Brier Score.

### 4.2. Boosting Methods
*   **CoxBoost**: Applies gradient boosting to the Cox Partial Likelihood.
*   **XGBoost / LightGBM for Survival**:
    *   Objective functions: Cox Partial Likelihood or AFT loss (e.g., Normal/Logistic).
    *   Highly efficient for structured tabular data.

### 4.3. Support Vector Machines (SVM)
*   **Survival SVM**:
    *   *Ranking-based*: Penalizes incorrect ordering of pairs (concordance).
    *   *Regression-based*: Predicts log-survival time or hazard.

---

## 5. Deep Learning for Survival Analysis

The modern era (2017-Present) has seen a surge in Deep Learning (DL) applications, driven by the need to handle unstructured data (images, text, omics) and complex temporal dependencies.

### 5.1. Cox-based Neural Networks
*   **DeepSurv** (Katzman et al., 2018):
    *   Replaces the linear combination $\beta^T x$ in the Cox model with a deep neural network $g_\theta(x)$.
    *   Loss: Negative Log Partial Likelihood.
    *   $$h(t|x) = h_0(t) \exp(g_\theta(x))$$
*   **Cox-Time** (Kvamme et al., 2019):
    *   Extends DeepSurv to handle time-dependent covariates and non-proportional hazards by including time as an input to the network.

### 5.2. Discrete-Time Models
*   **DeepHit** (Lee et al., 2018):
    *   Discretizes time into intervals.
    *   Uses a multi-task network to learn the joint distribution of the first hitting time and event type.
    *   **Key Innovation**: Specifically designed for **Competing Risks** (where multiple events can happen, and one prevents the others).
    *   Loss: Combination of Log-Likelihood and a Ranking Loss (to optimize concordance).

### 5.3. Advanced Architectures
*   **RNNs / LSTMs**:
    *   Used for longitudinal data where covariates change over time (e.g., Dynamic-DeepHit).
    *   Captures the history of a patient's health trajectory.
*   **Neural ODEs**:
    *   Models the hazard or survival function as a continuous-time dynamic system.
    *   Allows for irregular sampling intervals.
*   **Generative Models (GANs / VAEs)**:
    *   *Survival-GAN*: Generates synthetic survival times conditioned on covariates to address data scarcity or privacy.
    *   *VAEs*: Used for latent feature extraction from high-dimensional omics data before survival prediction.

### 5.4. Comparison: DL vs. Traditional
| Feature | Traditional (Cox) | Machine Learning (RSF) | Deep Learning (DeepSurv/DeepHit) |
| :--- | :--- | :--- | :--- |
| **Linearity** | Assumes Linear Log-Hazard | Non-Linear | Highly Non-Linear |
| **Data Types** | Structured (Tabular) | Structured | Structured + Unstructured (Images, Text) |
| **Interpretability** | High (Hazard Ratios) | Moderate (Feature Importance) | Low (Black Box) |
| **Data Size** | Small to Medium | Medium to Large | Large |

---

## 6. Evaluation Metrics

Evaluating survival models is more complex than regression/classification due to censoring.

### 6.1. Discrimination (Ranking)
*   **Concordance Index (C-index)**:
    *   The probability that, for a random pair of subjects, the subject with the higher predicted risk experiences the event sooner.
    *   Range: 0.5 (Random) to 1.0 (Perfect).
    *   *Uno's C-index*: Adjusts for censoring distribution.

### 6.2. Calibration (Accuracy)
*   **Brier Score (BS)**:
    *   Mean Squared Error equivalent for survival.
    *   Measures the accuracy of probabilistic predictions at a specific time point $t$.
    *   $BS(t) = \frac{1}{N} \sum (I(T_i > t) - \hat{S}(t|x_i))^2$ (weighted by inverse censoring probability).
    *   **Integrated Brier Score (IBS)**: Integral of BS over time.

### 6.3. Time-Dependent AUC
*   ROC curves adapted for time-to-event outcomes (e.g., Cumulative/Dynamic AUC).

---

## 7. Key Libraries and Tools

### Python
*   **`lifelines`**: Best for traditional statistical methods (KM, Cox, AFT). Pure Python, easy API.
*   **`scikit-survival`**: Comprehensive ML library. Includes SVMs, Random Survival Forests, Gradient Boosting.
*   **`pycox`**: Built on PyTorch. State-of-the-art DL models (DeepSurv, DeepHit, Cox-Time).
*   **`auton-survival`**: Carnegie Mellon's library for phenotyping and survival analysis.

### R
*   **`survival`**: The core package for SA in R (Kaplan-Meier, Cox).
*   **`glmnet`**: Regularized Cox regression (Lasso/Ridge).
*   **`randomForestSRC`**: High-performance Random Survival Forests.
*   **`mlr3proba`**: Modern machine learning framework for survival analysis benchmarking.

---

## 8. References and Further Reading

1.  **Cox, D. R. (1972).** "Regression Models and Life-Tables". *Journal of the Royal Statistical Society*. (The seminal paper on Cox PH).
2.  **Ishwaran, H., et al. (2008).** "Random survival forests". *The Annals of Applied Statistics*.
3.  **Katzman, J. L., et al. (2018).** "DeepSurv: personalized treatment recommender system using a Cox proportional hazards deep neural network". *BMC Medical Research Methodology*.
4.  **Lee, C., et al. (2018).** "DeepHit: A Deep Learning Approach to Survival Analysis with Competing Risks". *AAAI Conference on Artificial Intelligence*.
5.  **Wang, P., et al. (2019).** "Machine Learning for Survival Analysis: A Survey". *ACM Computing Surveys*.
6.  **Wiegrebe, S., et al. (2024).** "Deep learning for survival analysis: A review". *Artificial Intelligence Review*.
