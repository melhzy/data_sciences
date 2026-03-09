# Week 01: Introduction to Machine Learning

## Lecture Materials

### Viewing the Presentations

This week has an HTML tutorial and lecture slides available online:

#### 1. Introduction to Machine Learning (Hands-on Tutorial)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY530-Machine-Learning/Week01/01_Intro_to_Machine_Learning.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY530-Machine-Learning/Week01/01_Intro_to_Machine_Learning.html)

**Option 3: Download and Open Locally**
- Download `01_Intro_to_Machine_Learning.html` and open it in your web browser

#### 2. Lecture Slides

- Download `ANLY530Lecture01_IntrotoML.pptx` from this directory.

---

## Course Content

This week covers:

### Lecture Topics
- What is Machine Learning?
- Supervised, unsupervised, and reinforcement learning
- Batch vs. online learning; instance-based vs. model-based learning
- The end-to-end ML project workflow
- Key challenges in ML: data quality, overfitting, underfitting
- Math basics: Linear Algebra (vectors, matrices, eigenvectors)

### Hands-on Tutorial Topics
- Setting up reproducible data pipelines
- Types of Machine Learning
  - Simulating and visualizing Supervised Learning (Linear Regression)
  - Simulating and visualizing Unsupervised Learning (K-Means Clustering)
- Four Learning Perspectives (Information, Similarity, Probability, Error)
- ML from a Problem Perspective (Classification vs. Regression)
- Applied Linear Algebra in R
  - Vectors and Matrices
  - Determinants and Inverses
  - Solving Systems of Linear Equations
  - Eigenvectors and Eigenvalues with visual intuition

---

## Materials

- **HTML Tutorial**: `01_Intro_to_Machine_Learning.rmd` → `01_Intro_to_Machine_Learning.html` (Interactive RMarkdown tutorial)
- **Lecture Slides**: `ANLY530Lecture01_IntrotoML.pptx`

---

## Reading

- **Textbook**: *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (Geron, 2019)
  - Chapter 1: The Machine Learning Landscape

---

## Learning Path

### Step 1: Theory
1. Review the lecture slides (`ANLY530Lecture01_IntrotoML.pptx`)
2. Read Chapter 1 in the Geron textbook
3. Understand the taxonomy of machine learning

### Step 2: Practice
1. Work through the tutorial (`01_Intro_to_Machine_Learning.html`)
2. Follow along with the code chunks, observing how math translates to code
3. Understand the conceptual differences shown in the visualizations

### Step 3: Apply
1. Experiment with tweaking the code in the `.rmd` file locally (e.g. changing cluster numbers or noise levels)
2. Verify you can compile the `.rmd` file to HTML on your own machine

---

## Key Concepts

### Machine Learning Taxonomy
- **Supervised Learning**: Learning with labeled data (e.g., Classification, Regression). Goal is to predict.
- **Unsupervised Learning**: Learning with unlabeled data (e.g., Clustering, Dimensionality Reduction). Goal is to discover structure.

### Linear Algebra
- **Vectors**: Ordered lists of numbers representing points in space or feature sets.
- **Matrices**: 2D arrays representing datasets (rows = instances, columns = features) or transformations.
- **Eigenvectors**: Vectors whose direction is not changed by a linear transformation; crucial for techniques like PCA.

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "ggplot2", "knitr", "kableExtra", "seedhash", "gridExtra"))
```

### Recommended Software
- **R**: Latest stable version
- **RStudio/Posit**: Latest version
- **Python 3 via Anaconda**: Required for later weeks and integrations

---

## Quick Links

- [← Back to Course Home](../README.md)

---

<div align="center">

**ANLY 530 - Principles & Applications of Machine Learning**  
*Harrisburg University*

</div>