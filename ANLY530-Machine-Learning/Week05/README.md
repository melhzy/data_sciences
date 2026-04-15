# Week 05: Support Vector Machines (SVM)

## Lecture Materials

### Viewing the Presentations

This week has an HTML tutorial and lecture slides available online:

#### 1. Support Vector Machines (Hands-on Tutorial)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY530-Machine-Learning/Week05/Week05-SVM-Tutorial.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY530-Machine-Learning/Week05/Week05-SVM-Tutorial.html)

**Option 3: Download and Open Locally**
- Download `Week05-SVM-Tutorial.html` and open it in your web browser

#### 2. Lecture Slides

- Download `Lecture06-SVM.pptx` from this directory.

---

## Course Content

This week covers:

### Lecture Topics
- What is SVM? Classification by finding the widest road
- Hyperplanes, margins, and support vectors
- Why maximum-margin classification generalises well
- Linear optimisation and the SVM objective function

### Hands-on Tutorial Topics
- The big idea: finding the widest road between classes
- Key terminology in plain English (hyperplane, margin, support vectors, C, kernel)
- Linear SVM: the math behind the road
  - Hard-margin vs. soft-margin classification
  - The C parameter as a strictness dial (with 4-panel visualisation)
- The kernel trick: drawing curved boundaries
  - 1D → 2D lifting intuition
  - Comparing linear, polynomial, and RBF kernels
- RBF kernel deep dive: gamma parameter effects and C × gamma interaction grid
- Building SVMs in R with `e1071`
  - Iris classification and decision boundary
  - Hyperparameter tuning with `tune()` and cross-validation
- Feature scaling: why it's critical for SVM
- Support Vector Regression (SVR) and the epsilon-insensitive tube
- Model comparison: Decision Tree vs. Random Forest vs. Linear SVM vs. RBF SVM
- Multi-class SVM (One-vs-One strategy)
- Advantages, disadvantages, and practical tips

---

## Materials

- **HTML Tutorial**: `Week05-SVM-Tutorial.Rmd` → `Week05-SVM-Tutorial.html` (Interactive RMarkdown tutorial)
- **Lecture Slides**: `Lecture06-SVM.pptx` / `Lecture06-SVM.pdf`

---

## Reading

- **Textbook**: *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (Géron, 2019)
  - Chapter 5: Support Vector Machines
- **scikit-learn documentation**: [1.4. Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
- **Wikipedia**: [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine)

---

## Learning Path

### Step 1: Theory
1. Review the lecture slides (`Lecture06-SVM.pptx`)
2. Read Chapter 5 in the Géron textbook
3. Understand the intuition: maximum-margin classification, support vectors, and the kernel trick

### Step 2: Practice
1. Work through the tutorial (`Week05-SVM-Tutorial.html`)
2. Follow along with the code chunks — observe how the margin, C, gamma, and kernels change the boundary
3. Compare SVM decision boundaries with Decision Tree and Random Forest from previous weeks

### Step 3: Apply
1. Experiment with different C and gamma values on your own datasets
2. Try the polynomial kernel with different degrees
3. Apply SVR to a regression problem of your choice
4. Verify you can compile the `.Rmd` file to HTML on your own machine

---

## Key Concepts

### Support Vector Machines
- **Hyperplane**: The decision boundary that separates classes
- **Margin**: The gap between the closest points of each class; SVM maximises this
- **Support Vectors**: The critical few data points that define the boundary
- **C Parameter**: Trade-off between a wide margin (simple model) and correct classification (complex model)
- **Kernel Trick**: Transform data into higher dimensions so a linear separator works for non-linear data
- **RBF Kernel**: The most popular non-linear kernel; gamma controls each point's influence radius
- **Feature Scaling**: Always required for SVM — standardise features to zero mean and unit variance
- **SVR**: SVM for regression using an epsilon-insensitive tube

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "e1071", "caret", "gridExtra", "scales", "kernlab", "rpart", "randomForest", "seedhash"))
```

### Recommended Software
- **R**: Latest stable version
- **RStudio/Posit**: Latest version

---

## Quick Links

- [← Back to Course Home](../README.md)

---

<div align="center">

**ANLY 530 - Principles & Applications of Machine Learning**  
*Harrisburg University*

</div>
