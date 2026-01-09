# Week 07: Data Screening Part 2 - Assumptions Testing

## Lecture Materials

### Viewing the Presentations

This week has two HTML presentations covering statistical assumptions for parametric tests:

#### 1. Data Screening Part 2 (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/docs/ANLY500-Analytics-I/Week07/07_datascreen_2.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week07/07_datascreen_2.html)

**Option 3: Download and Open Locally**
- Download `07_datascreen_2.html` and open in your web browser

#### 2. R for Data Analytics (Week 07 Comprehensive Tutorial) 🆕 ⭐

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/docs/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `07_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week continues from Week 06 and focuses on **testing statistical assumptions** for parametric analyses. After cleaning data (Week 06), we must verify that our data meet the requirements of parametric statistical tests.

### Lecture Topics
- The five key assumptions for parametric statistics
- Independence and the Durbin-Watson test
- Additivity and multicollinearity (VIF)
- Linearity assessment with residual plots
- Normality testing and the Central Limit Theorem
- Homogeneity of variance and homoscedasticity
- The "fake regression" approach for diagnostics

### R Tutorial Topics (Enhanced with 60+ Visualizations!)
- **Visual Workflow**: Complete assumption checking process diagram
- **Understanding Residuals**: Raw, standardized, and studentized residuals
- **Influential Cases**: Outliers vs. high leverage vs. influential cases
- **Independence**: Durbin-Watson test, ACF plots, autocorrelation patterns
- **Multicollinearity**: Correlation matrices, VIF interpretation, visual examples
- **Linearity**: Q-Q plots, residual plots, pattern recognition
- **Normality**: Central Limit Theorem demonstration, Shapiro-Wilk test, skewness/kurtosis
- **Homogeneity/Homoscedasticity**: Levene's test, residual patterns, funnel shapes
- **Cook's Distance**: Identifying influential cases that change the model
- **Data Transformations**: Log, square root, reciprocal transformations with visualizations
- **Alternative Approaches**: What to do when assumptions fail
- **Comprehensive Dashboard**: 12-panel diagnostic summary

---

## Materials

- **Lecture Slides**: `07_datascreen_2.rmd` → `07_datascreen_2.html` (Slidy presentation)
- **R Tutorial**: `07_R_for_DataAnalytics.rmd` → `07_R_for_DataAnalytics.html` (2,791 lines, 8,243 HTML lines!)
- **Enhancement Summary**: `ENHANCEMENTS_SUMMARY.md` (Complete documentation of all visualizations)
- **Data Files**: `data/` folder
  - `data_screening.csv` - Pre-screened dataset from Week 06
- **Images**: `pictures/` folder (lecture graphics)
  - `2.png` - Assumption checking diagrams
  - `3.png` - Diagnostic plot examples

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
  - Chapter 5: The beast of bias
    - Section 5.7: Assumptions of parametric data
    - Section 5.7.1: Normality
    - Section 5.7.2: Homogeneity of variance
    - Section 5.7.3: Interval data
    - Section 5.7.4: Independence
  - Chapter 7: Regression
    - Section 7.7: Assessing the regression model
    - Section 7.7.1: Diagnostic plots
    - Section 7.7.1.1: Outliers and residuals
    - Section 7.7.1.2: Influential cases
    - Section 7.7.1.3: Assessing the assumption of independence
    - Section 7.7.2: Assessing the regression model II: generalization
    - Section 7.7.2.1: Checking assumptions
    - Section 7.7.2.4: Multicollinearity
    - Section 7.9.5: Checking assumptions about the residuals
  
  Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

- **Additional References**:
  - Berry, W. D. (1993). *Understanding Regression Assumptions*
  - Cook, R. D., & Weisberg, S. (1982). *Residuals and Influence in Regression*
  - Fox, J. (2015). *Applied Regression Analysis and Generalized Linear Models* (3rd ed.)
  - Stevens, J. P. (2002). *Applied Multivariate Statistics for the Social Sciences* (4th ed.)

---

## Learning Path

### Step 1: Review Week 06
1. Ensure you understand data cleaning from Week 06
2. Review missing data handling and outlier detection
3. Have a clean dataset ready for assumption testing

### Step 2: Theory
1. Review the Week 07 lecture (`07_datascreen_2.html`)
2. Understand the five key assumptions
3. Learn when each assumption matters most

### Step 3: Hands-On Practice
1. Work through the comprehensive tutorial (`07_R_for_DataAnalytics.html`)
2. Study the 60+ visualizations showing good vs. bad patterns
3. Practice with the provided dataset
4. Run the diagnostic dashboard on your own data

### Step 4: Key Concepts to Master
- **Residuals**: Understand the difference between raw, standardized, and studentized residuals
- **Influential Cases**: Distinguish outliers from high leverage from influential cases
- **Visual Patterns**: Recognize what violations look like in diagnostic plots
- **Decision Making**: Know when to proceed, transform, or use alternatives
- **Cook's Distance**: Interpret Cook's D > 1 as a serious concern

### Step 5: Practice Exercises
1. Complete Exercise 1: Full assumption check on `mtcars` dataset
2. Complete Exercise 2: Identify violations from residual plots
3. Complete Exercise 3: Interpret VIF values and address multicollinearity

---

## Key Features of This Week's Tutorial

### 🎨 Comprehensive Visualizations
- **60+ individual plots** explaining concepts step-by-step
- **12-panel comparison grids** showing good vs. bad examples
- **Color-coded status indicators** (✓ green, ⚠ orange, ✗ red)
- **Interactive diagnostic dashboard** for complete assessment

### 📚 Theoretical Grounding
- **8 detailed IEEE citations** to Field et al. with specific page numbers
- **Plain English explanations** for every technical concept
- **Real-world analogies** to make concepts accessible
- **Glossary** of all technical terms

### 💻 Practical Tools
- **Fake regression approach** for generating diagnostics
- **Interpretation guides** for every test and plot
- **Transformation guide** with R code examples
- **Decision trees** for handling violations
- **Reproducible examples** using `seedhash`

### 🎯 Learning Objectives
After completing this tutorial, you will be able to:
1. Understand the purpose and importance of assumption checking
2. Distinguish between different types of residuals
3. Identify outliers vs. influential cases
4. Test independence using Durbin-Watson and interpret ACF plots
5. Detect multicollinearity using correlations and VIF
6. Assess linearity using Q-Q plots and residual plots
7. Evaluate normality using multiple methods
8. Apply the Central Limit Theorem to sample size decisions
9. Check homogeneity and homoscedasticity
10. Transform data to fix assumption violations
11. Choose alternative methods when assumptions cannot be met
12. Interpret a comprehensive diagnostic dashboard
13. Make informed decisions about proceeding with analyses

---

## What's New in This Tutorial

### Major Enhancements (See `ENHANCEMENTS_SUMMARY.md` for full details)

1. **Visual Workflow Diagram** - Complete flowchart of the assumption checking process
2. **Understanding Residuals** - Visual explanation of residual = observed - predicted
3. **Types of Residuals Comparison** - 6-panel visualization comparing all residual types
4. **All Five Assumptions at a Glance** - 12-panel comparison grid
5. **Understanding Influential Cases** - Visual distinction between outliers and influential cases
6. **Independence Visualization** - 6-panel display of autocorrelation patterns
7. **Multicollinearity Concept** - 3-panel scatterplot demonstration
8. **Linearity Concept** - 6-panel view of linear vs. non-linear relationships
9. **Central Limit Theorem Demonstration** - 6-panel visualization of sampling distributions
10. **Homoscedasticity Explained** - 6-panel detailed view of variance patterns
11. **Data Transformations Guide** - 12-panel visualization of common transformations
12. **Alternative Approaches Table** - Comprehensive guide for handling violations
13. **Comprehensive Diagnostic Dashboard** - 12-panel master dashboard
14. **Data Overview Dashboard** - 6-panel summary of the dataset

---

## Technical Details

### Document Statistics
- **Total Lines (Rmd)**: 2,791 lines
- **Total Lines (HTML)**: 8,243 lines
- **Code Chunks**: 50+ (including visualization chunks)
- **Visualizations**: 60+ individual plots
- **Tables**: 15+ summary/comparison tables
- **Sections**: 9 major parts with subsections
- **Practice Exercises**: 3 hands-on exercises with solutions

### Software Requirements
```r
# Required packages
library(tidyverse)
library(ggplot2)
library(rio)
library(mice)
library(car)
library(moments)
library(corrplot)
library(knitr)
library(kableExtra)
library(seedhash)
library(DiagrammeR)
```

### Reproducibility
- All visualizations use `seedhash` for reproducibility
- MD5 Hash: Generated from "Week07 Data Screening Part 2 - ANLY500"
- Seeds available for all random operations
- Session info included at end of document

---

## Tips for Success

### Before Starting
1. ✅ Complete Week 06 (data cleaning)
2. ✅ Install all required R packages
3. ✅ Have RStudio or VS Code with R extension ready
4. ✅ Review basic regression concepts from earlier weeks

### While Working Through the Tutorial
1. 📖 Read the "Plain English" explanations first
2. 👀 Study the visualizations carefully - they show what to look for
3. 💻 Run the code chunks yourself - don't just read
4. 🎨 Compare your plots to the "good" and "bad" examples
5. 📝 Take notes on the interpretation guides

### Common Pitfalls to Avoid
- ❌ Don't skip the visual checks - they're as important as statistical tests
- ❌ Don't remove data points just because they fail a test
- ❌ Don't ignore the Central Limit Theorem (N ≥ 30 helps with normality)
- ❌ Don't confuse outliers with influential cases
- ❌ Don't forget that independence violations are the most serious

### When to Get Help
- 🤔 If you can't interpret a diagnostic plot
- 🤔 If multiple assumptions are violated
- 🤔 If transformations don't fix the problems
- 🤔 If you're unsure whether to proceed with your analysis

---

## Connection to Other Weeks

### Builds On
- **Week 02**: Basic R programming, descriptive statistics
- **Week 03**: Data wrangling, exploratory data analysis
- **Week 04**: Statistical inference, hypothesis testing
- **Week 05**: Data visualization with ggplot2
- **Week 06**: Data screening part 1 (cleaning, missing data, outliers)

### Prepares For
- **Week 08+**: Actual statistical analyses (t-tests, ANOVA, regression)
- **Future analyses**: You'll use these diagnostic skills for every analysis

---

## Assessment

### Lab Assignment
- Complete the Week 07 lab assignment (if provided)
- Apply assumption checking to a provided dataset
- Interpret diagnostic plots and make recommendations
- Document your decisions and reasoning

### Self-Assessment Questions
1. Can you explain the difference between an outlier and an influential case?
2. Can you interpret a Durbin-Watson statistic?
3. Can you identify multicollinearity from a VIF table?
4. Can you recognize non-linearity in a residual plot?
5. Can you explain when the Central Limit Theorem applies?
6. Can you distinguish homoscedasticity from heteroscedasticity?
7. Can you choose an appropriate transformation for skewed data?
8. Can you interpret Cook's Distance values?

---

## Additional Resources

### Online Resources
- [ggplot2 Documentation](https://ggplot2.tidyverse.org/)
- [car Package Documentation](https://cran.r-project.org/web/packages/car/index.html)
- [MICE Package Documentation](https://cran.r-project.org/web/packages/mice/index.html)

### Video Tutorials
- Search for "regression diagnostics in R"
- Search for "assumption checking in R"
- Search for "Cook's Distance interpretation"

### Practice Datasets
- Use built-in R datasets: `mtcars`, `iris`, `diamonds`
- Try the tutorial code with your own research data
- Practice with datasets from previous weeks

---

## Troubleshooting

### Common Issues

**Issue**: "Error: package 'X' not found"
- **Solution**: Run `install.packages("X")` first

**Issue**: "Error in data.frame(): arguments imply differing number of rows"
- **Solution**: Check that VIF calculation handles factor variables correctly (fixed in this tutorial)

**Issue**: Plots don't look like the examples
- **Solution**: Check that you're using the same seed values

**Issue**: Can't knit the Rmd file
- **Solution**: Ensure all packages are installed and data files are in the correct location

---

## Citation

If you use this tutorial in your work, please cite:

```
Huang, Z. (2026). Week 07: R for Data Analytics (Data Screening Part 2 - Assumptions).
ANLY 500 Analytics I, Harrisburg University. 
Retrieved from https://melhzy.github.io/data_sciences/docs/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html
```

Based on:
```
Field, A., Miles, J., & Field, Z. (2012). Discovering Statistics Using R. 
London: SAGE Publications.
```

---

## Feedback and Contributions

This tutorial is part of the ANLY 500 Analytics I course materials. For questions, corrections, or suggestions:

- **Repository**: [github.com/melhzy/data_sciences](https://github.com/melhzy/data_sciences)
- **Issues**: Submit via GitHub Issues
- **Course**: ANLY 500 Analytics I, Harrisburg University

---

## Version History

- **v1.0** (January 2026): Initial comprehensive release
  - 60+ visualizations added
  - Influential cases section added
  - Residual types comparison added
  - Transformation guide added
  - Comprehensive diagnostic dashboard added
  - Full IEEE citations to Field et al.

---

**Last Updated**: January 8, 2026

**Author**: Ziyuan Huang

**Course**: ANLY 500 - Analytics I

**Institution**: Harrisburg University

---

<div align="center">

### 🎓 Ready to Master Statistical Assumptions? 

**[Start the Tutorial Now!](https://melhzy.github.io/data_sciences/docs/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html)**

</div>
