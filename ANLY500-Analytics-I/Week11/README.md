# Week 11: Comparing Two Means (The t-test)

This module focuses on one of the most fundamental statistical tools: the **t-test**. We explore how to compare means between two groups, understanding the theoretical underpinnings (Signal-to-Noise Ratio) and practical application in R.

## 📚 Lecture Materials

- **[View Tutorial (HTML)](11_R_for_DataAnalytics.html)** - *Comprehensive Step-by-Step Guide*
- **[View Lecture Slides (HTML)](11_ttests.html)** - *Use arrow keys to navigate*
- **[Source Tutorial RMarkdown](11_R_for_DataAnalytics.rmd)**
- **[Source Slides RMarkdown](11_ttests.rmd)**

## 🎯 Key Concepts

### Signal-to-Noise Ratio
We conceptualize the t-statistic as a ratio:
$$t = \frac{\text{Signal (Difference Between Means)}}{\text{Noise (Variability within Groups)}}$$
- **Signal:** The systematic variation caused by the experimental manipulation.
- **Noise:** The unsystematic variation (error) due to individual differences.

### Types of T-Tests
- **Independent Samples t-test:** Compares two separate groups (e.g., Treatment vs. Control).
- **Dependent (Paired) Samples t-test:** Compares the same participants in two conditions (Repeated Measures) or matched pairs.

### Assumptions & Diagnostics
- **Normality:** Checking if the sampling distribution is normal (Shapiro-Wilk test).
- **Homogeneity of Variance:** Checking if groups have equal spread (Levene's test).

### Effect Sizes
- **Cohen's d:** A standardized measure of the difference ($0.2 = Small, 0.5 = Medium, 0.8 = Large$).
- **Pearson's r:** The strength of the relationship.

## 🛠️ R Packages Used
- `tidyverse`: For data manipulation (`dplyr`) and visualization (`ggplot2`).
- `rio`: For easy data import (`import`).
- `car`: For Levene's test of homogeneity (`leveneTest`).
- `MOTE`: For calculating accurate effect sizes ($d$, $d_{av}$).
- `pwr`: For statistical power analysis.

## 📈 State of the Art (2026) Updates
This module has been updated to reflect modern statistical practices:
- **Visualizing Uncertainty:** Using boxplots with jittered points to show raw data alongside summary statistics.
- **Robustness:** Discussing when assumptions matter and when the t-test is robust (Field et al., 2012).
- **Effect Size Reporting:** Emphasizing that p-values alone are insufficient; effect sizes provide context.

---
*ANLY 500 - Analytics I | Harrisburg University*
