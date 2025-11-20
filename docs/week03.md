# ANLY500 Week 03: R for Data Analytics

This page summarizes the Week 03 hands-on tutorial focusing on:

- Data import and cleaning
- dplyr verbs and grouped summaries
- Joins and reshaping (long ↔ wide)
- Exploratory Data Analysis (univariate, bivariate, categorical)
- Distribution shape (skewness, kurtosis)
- Standardization (z-scores)
- Correlation (Pearson vs Spearman)
- Assumption checks (normality, variance, independence)
- Basic inference (one-sample & independent t tests, proportion test)
- Effect sizes (Cohen’s d) and APA-style reporting

## Key Files
- Main tutorial R Markdown: `ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.rmd`
- (After knitting) HTML output: `ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.html` (generate by opening the Rmd and clicking Knit or running `rmarkdown::render()` in R).

## Rendering the Tutorial Locally
```r
# In R
install.packages(c("rmarkdown", "tidyverse"))
rmarkdown::render("ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.rmd")
```
The HTML file will be created in the same folder if no output directory is specified.

## GitHub Pages Setup Instructions
To publish this content via GitHub Pages:
1. Push these changes to GitHub.
2. In the GitHub repository UI, go to Settings → Pages.
3. Under "Build and deployment" select:
   - Source: Deploy from branch
   - Branch: `main`
   - Folder: `/docs`
4. Save. GitHub will build the site; the page will appear at: `https://<your-username>.github.io/data_sciences/week03.html` (if you add an `index.md` or `index.html`).

Currently this page is `docs/week03.md`. After Pages is enabled it will be accessible at:
`https://<your-username>.github.io/data_sciences/week03`

(Optional) To make Week03 the home page rename this file to `docs/index.md`.

## Suggested Enhancements (Optional)
- Knit the Rmd and copy the HTML into `docs/week03.html` for direct browser viewing.
- Add screenshots of plots for visual preview.
- Add a short FAQ section linking back to assumption diagnostics.

## Attribution
Conceptual references: Field, Miles, & Field (2012), *Discovering Statistics Using R*.

---
Last updated: Generated from repository state on render.
