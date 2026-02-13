# Week 10: Mediation and Moderation

This module explores advanced regression techniques: Mediation (explaining *how* an effect happens) and Moderation (explaining *when* an effect happens).

## 📚 Lecture Materials

- **[View Tutorial (HTML)](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week10/10_R_for_DataAnalytics.html)** - *Comprehensive Step-by-Step Guide*
- **[View Lecture Slides (HTML)](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week10/10_medmod.html)** - *Use arrow keys to navigate*
- **[Source Tutorial RMarkdown](10_R_for_DataAnalytics.rmd)**
- **[Source Slides RMarkdown](10_medmod.rmd)**

## 🎯 Key Concepts

### Mediation ("The Middle Man")
Mediation explains the mechanism between a predictor (X) and an outcome (Y).
- **Baron & Kenny (1986):** The classic 4-step approach (historical context).
- **Sobel Test:** A frequentist test for the indirect effect (conservative).
- **Bootstrapping (State of the Art 2026):** The modern gold standard for testing indirect effects without normality assumptions.
- **Packages:** Uses `MeMoBootR` for educational demonstration, with notes on `lavaan` and `mediation` for professional use.

### Moderation ("It Depends")
Moderation occurs when the relationship between X and Y changes depending on the level of a third variable (Z).
- **Interaction Effects:** Testing if the slopes are significantly different.
- **Centering:** Why we subtract the mean (interpretation & multicollinearity).
- **Simple Slopes Analysis:** probing the interaction at Low (-1SD), Average, and High (+1SD) levels of the moderator.

## 🛠️ R Packages Used
- `rio`: For easy data import/export
- `ggplot2`: For visualizing interaction effects
- `MeMoBootR`: A custom package for automated mediation/moderation screening and bootstrapping (Educational).

## 📈 State of the Art (2026) Updates
This module has been updated to reflect modern statistical practices:
- **Plain English** definitions for all key terms.
- **Bootstrapping** emphasized over the outdated Baron & Kenny causal steps.
- **Centering** explained with both mathematical and practical rationale.

---
*ANLY 500 - Analytics I | Harrisburg University*
