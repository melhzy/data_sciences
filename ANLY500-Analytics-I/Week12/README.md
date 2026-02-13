# Week 12: Analysis of Variance (ANOVA)

This module expands our statistical toolkit from comparing two groups (t-tests) to comparing **three or more groups** using **ANOVA**. We explore why multiple t-tests fail (Familywise Error Rate) and how the F-Ratio provides a robust solution.

## 📚 Lecture Materials

- **[View Tutorial (HTML)](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week12/12_R_for_DataAnalytics.html)** - *Comprehensive Step-by-Step Guide*
- **[View Lecture Slides (HTML)](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week12/12_lecture_anova.html)** - *Use arrow keys to navigate*
- **[Source Tutorial RMarkdown](12_R_for_DataAnalytics.rmd)**
- **[Source Slides RMarkdown](12_lecture_anova.rmd)**

## 🎯 Key Concepts

### Familywise Error Rate (FWER)
Why can't we just run multiple t-tests?
- Every test carries a 5% risk of a Type I error ($\alpha = 0.05$).
- Running 3 independent tests increases the error rate to $\approx 14\%$.
- **Real World Analogy:** The H1B Lottery (25.6% selection rate). The more years you apply, the higher your chance of "success" (or error, in statistics).

### The Logic of ANOVA
We partition the total variation in the data into two sources:
$$F = \frac{\text{Systematic Variance (Model)}}{\text{Unsystematic Variance (Residual)}}$$

- **SST (Total):** How much do scores vary overall?
- **SSM (Model):** How much do group means vary from the grand mean?
- **SSR (Residual):** How much do individuals vary from their group mean?

### Post Hoc Tests & Trends
- **Omnibus Test:** The F-test tells us *if* there is a difference, but not *where*.
- **Post Hoc Tests (Bonferroni):** Like a "statistical sniper," finding specific group differences while controlling for FWER.
- **Trend Analysis:** Testing for specific shapes (Linear vs. Quadratic) in ordered groups (e.g., Placebo < Low < High).

## 🛠️ R Packages Used
- `tidyverse`: For data manipulation and `ggplot2` visualization.
- `ez`: For easy-to-use ANOVA functions (`ezANOVA`).
- `MOTE`: For calculating effect sizes ($\omega^2$, Omega Squared).
- `rio`: For data import.

## 📈 Visualizations
This week features advanced `ggplot2` techniques to visualize the abstract math of ANOVA:
- **Violin Plots with Mean Diamonds:** Showing distribution shape and central tendency.
- **Visualizing Sum of Squares:** Using `geom_segment` to draw the actual "distances" that make up SST, SSM, and SSR.

---
*ANLY 500 - Analytics I | Harrisburg University*
