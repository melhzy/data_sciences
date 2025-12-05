# Week 04: Statistical Inference and Effect Sizes

## Lecture Materials

### Viewing the Presentations

This week has one HTML presentation and one hands-on R tutorial:

#### 1. Introduction to Data Analytics III (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week04/04_introDA_3.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week04/04_introDA_3.html)

**Option 3: Download and Open Locally**
- Download `04_introDA_3.html` and open in your web browser

#### 2. R for Data Analytics (Week 04 Hands-on Tutorial)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week04/04_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week04/04_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `04_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week builds on Weeks 02-03 and focuses on the foundations of statistical inference:

### Lecture Topics
- The fundamental equation: Outcome = Model + Error
- Measuring model fit: Sum of Squares, Variance, Standard Deviation
- Degrees of freedom and the N-1 correction
- Standard Error vs. Standard Deviation
- The Central Limit Theorem
- Confidence Intervals
- Null Hypothesis Significance Testing (NHST)
- Type I and Type II errors
- Statistical power
- Effect sizes: Cohen's d and Pearson's r

### R Tutorial Topics
- Manual calculations of SS, Variance, and SD
- The `apply` family of functions (`apply`, `lapply`, `sapply`, `tapply`)
- Modern tidyverse alternatives with `dplyr`
- Calculating and visualizing Standard Error
- Constructing Confidence Intervals
- Conducting hypothesis tests (one-sample and two-sample t-tests)
- Power analysis with the `pwr` package
- Effect size calculations with `effectsize` and `MOTE`
- Multiple comparison corrections (Bonferroni, Holm, FDR)

---

## Materials

- **Lecture Slides**: `04_introDA_3.rmd` → `04_introDA_3.html` (Slidy presentation)
- **R Tutorial**: `04_R_for_DataAnalytics.rmd` → `04_R_for_DataAnalytics.html` (Interactive tutorial)
- **Proposal Materials**: `proposal/` folder (Final project guidelines and APA sample)
- **Images**: `pictures/` folder (lecture graphics)

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
  - Chapter 2: Everything you ever wanted to know about statistics
    - Section 2.5: Populations and samples
    - Section 2.6: Statistical models
    - Section 2.7: Going beyond the data
  - Chapter 9: Comparing two means (t-tests)
  
  Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

---

## Learning Path

### Step 1: Theory
1. Review the Week 04 lecture (`04_introDA_3.html`)
2. Understand the fundamental equation: Outcome = Model + Error
3. Learn the difference between SD and SE
4. Study the logic of NHST and the Lady Tasting Tea example

### Step 2: Practice
1. Work through `04_R_for_DataAnalytics.html`
2. Perform manual calculations of SS, Variance, and SD
3. Run t-tests and calculate effect sizes
4. Conduct a power analysis for your own research question

### Step 3: Apply
1. Begin working on the Final Project Proposal (see `proposal/` folder)
2. Practice reporting results with effect sizes
3. Apply NHST and effect size concepts to a real dataset

---

## Key Concepts

### The Fundamental Equation
- **Outcome = Model + Error**: Everything in statistics follows this pattern
- The mean is a simple model; deviations are the error

### Measuring Fit
- **Sum of Squares (SS)**: Total squared error
- **Variance**: Average squared error (SS / df)
- **Standard Deviation**: Square root of variance (original units)

### Degrees of Freedom
- **df = N - 1** when estimating from the mean
- The rugby team analogy: 14 players can choose freely, the 15th has no choice

### Standard Error vs. Standard Deviation
- **SD**: Spread of individual scores around the sample mean
- **SE**: Spread of sample means around the population mean

### Confidence Intervals
- A range likely containing the population parameter
- 95% CI = Mean ± 1.96 × SE

### NHST Framework
- **H₀**: No effect (null hypothesis)
- **H₁**: Effect exists (alternative hypothesis)
- **p < .05**: Reject H₀ (but this is arbitrary!)

### Error Types and Power
- **Type I Error (α)**: False positive (rejecting true H₀)
- **Type II Error (β)**: False negative (missing real effect)
- **Power = 1 - β**: Probability of detecting a real effect

### Effect Sizes
| Size | Cohen's d | Pearson's r | Variance Explained |
|------|-----------|-------------|-------------------|
| Small | 0.2 | 0.1 | 1% |
| Medium | 0.5 | 0.3 | 9% |
| Large | 0.8 | 0.5 | 25% |

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "psych", "knitr", "kableExtra", "moments"))
install.packages("seedhash")  # For reproducible analysis
```

### Optional Packages (Recommended)
```r
install.packages(c("effectsize", "pwr", "MOTE"))
```

### Recommended Software
- **R**: Version 4.5.2 or higher
- **RStudio/Posit**: Latest version
- **VS Code**: With R extension (alternative)

---

## Final Project Proposal

This week includes materials for the Final Project Proposal:

- **Guidelines**: `proposal/final_project_guidelines.docx`
- **APA 7 Sample**: `proposal/apa-7-professional-sample-paper-2025-revision.pdf`
- **Formatting Sample**: `proposal/sample_fp_formatting_sample.docx`
- **README**: `proposal/README.md` (detailed instructions)

---

## Quick Links

- [← Week 03 Materials](../Week03/README.md)
- [Back to Course Home](../README.md)
- [View Week 02 Materials](../Week02/README.md)

---

<div align="center">

**ANLY 500 - Analytics I**  
*Harrisburg University*

Last Updated: December 4, 2025

</div>
