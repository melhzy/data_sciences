# 📊 ANLY 500 - Analytics I

**Course**: Analytics I  
**Institution**: Harrisburg University  
**Author**: Ziyuan Huang  
**Website**: [https://melhzy.github.io/data_sciences/](https://melhzy.github.io/data_sciences/)

---

## Welcome to ANLY 500 Analytics I

This repository contains comprehensive R tutorials for data analytics, covering foundational concepts through advanced visualization techniques. Each week builds upon previous knowledge with hands-on, code-first workflows grounded in statistical theory.

All materials are designed for entry-level students with extensive plain English explanations, visual demonstrations, and reproducible examples.

---

## 📚 Weekly Tutorials

### [Week 02: R for Data Analytics](Week02/)

Introduction to R programming, data types, descriptive statistics, and basic hypothesis testing. Learn central tendency, dispersion measures, and visualization fundamentals.

**Topics Covered:**
- R basics: variables, data types, operators
- Descriptive statistics: mean, median, mode, SD, variance
- Data visualization fundamentals
- Basic hypothesis testing concepts

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week02/02_R_for_DataAnalytics.html)
- 📂 [Week 02 Folder](Week02/)

---

### [Week 03: Data Wrangling & EDA](Week03/)

Master data import, tidy data principles, dplyr verbs, handling missing values, and exploratory data analysis with ggplot2. Includes correlation and basic inference.

**Topics Covered:**
- Data import and export
- Tidy data principles
- dplyr verbs: filter, select, mutate, summarize
- Handling missing values
- Exploratory data analysis
- Correlation analysis

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.html)
- 📂 [Week 03 Folder](Week03/)

---

### [Week 04: Statistical Inference](Week04/)

Deep dive into hypothesis testing, confidence intervals, effect sizes (Cohen's d), statistical power, and Type I/II errors. Learn the fundamental equation: Outcome = Model + Error.

**Topics Covered:**
- Hypothesis testing framework
- Null and alternative hypotheses
- p-values and significance levels
- Confidence intervals
- Effect sizes (Cohen's d)
- Statistical power and sample size
- Type I and Type II errors

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week04/04_R_for_DataAnalytics.html)
- 📂 [Week 04 Folder](Week04/)

---

### [Week 05: Data Visualization](Week05/)

Comprehensive ggplot2 tutorial covering histograms, scatterplots, bar graphs, line graphs, data reshaping, and professional themes. Master the grammar of graphics!

**Topics Covered:**
- Grammar of Graphics philosophy
- Histograms for distribution analysis
- Scatterplots for relationships
- Bar graphs with error bars
- Line graphs for longitudinal data
- Data reshaping (wide ↔ long)
- Professional customization and themes
- Tufte's principles of data visualization

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week05/05_R_for_DataAnalytics.html)
- 📊 [Original Lecture](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week05/05_graphs.html)
- 📂 [Week 05 Folder](Week05/)

---

### [Week 06: Data Screening Part 1](Week06/)

Essential data cleaning techniques: accuracy checking, handling missing data (MCAR, MAR, MNAR), multiple imputation with MICE, and multivariate outlier detection using Mahalanobis distance.

**Topics Covered:**
- Data accuracy checking
- Missing data mechanisms (MCAR, MAR, MNAR)
- Missing data strategies:
  - Listwise deletion
  - Pairwise deletion
  - Mean/median imputation
  - Multiple imputation (MICE)
- Outlier detection:
  - Z-scores
  - Boxplots and IQR
  - Mahalanobis distance
- Data transformation techniques

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week06/06_R_for_DataAnalytics.html)
- 📊 [Original Lecture](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week06/06_datascreen_1.html)
- 📂 [Week 06 Folder](Week06/)

---

### [Week 07: Data Screening Part 2 - Assumptions](Week07/) 🆕

**⭐ Comprehensive assumption checking with 60+ visualizations!** Master independence, multicollinearity, linearity, normality, and homoscedasticity. Includes influential cases, Cook's Distance, and transformation guide.

**Topics Covered:**
- **The Five Key Assumptions:**
  1. Independence (Durbin-Watson test)
  2. Additivity/Multicollinearity (VIF)
  3. Linearity (Q-Q plots, residual plots)
  4. Normality (Shapiro-Wilk, Central Limit Theorem)
  5. Homogeneity/Homoscedasticity (Levene's test)
- **Advanced Diagnostics:**
  - Understanding residuals (raw, standardized, studentized)
  - Influential cases vs. outliers vs. high leverage
  - Cook's Distance interpretation
  - Visual pattern recognition
- **Solutions:**
  - Data transformations (log, sqrt, reciprocal)
  - Alternative approaches when assumptions fail
  - Comprehensive diagnostic dashboard

**Special Features:**
- 60+ individual plots and visualizations
- 12-panel comparison grids (good vs. bad examples)
- Color-coded status indicators (✓ ⚠ ✗)
- Complete diagnostic dashboard
- Transformation guide with R code
- Decision trees for handling violations
- 8 detailed IEEE citations to Field et al.

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html) (2,791 lines of code!)
- 📊 [Original Lecture](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week07/07_datascreen_2.html)
- 📋 [Enhancement Summary](Week07/ENHANCEMENTS_SUMMARY.md)
- 📂 [Week 07 Folder](Week07/)

---

### [Week 08: Correlation Analysis](Week08/) 🆕

**⭐ Complete correlation guide with 50+ visualizations!** Master Pearson, Spearman, Kendall correlations, partial/semi-partial correlations, and APA reporting. Includes Anscombe's Quartet and advanced techniques.

**Topics Covered:**
- **Understanding Correlation:**
  - Correlation coefficients and interpretation (-1 to +1)
  - Covariance and shared variance (r²)
  - Correlation vs. causation
  - Restriction of range and outlier effects
- **Parametric Methods:**
  - Pearson's product-moment correlation (r)
  - Assumptions: linearity, normality, homoscedasticity
  - Confidence intervals and significance testing
- **Non-Parametric Methods:**
  - Spearman's rho (rank-based correlation)
  - Kendall's tau (ordinal data, tied ranks)
  - When to use non-parametric alternatives
- **Specialized Correlations:**
  - Point-biserial correlation (dichotomous variables)
  - Partial correlations (controlling for third variables)
  - Semi-partial correlations (unique variance)
  - Comparing dependent/independent correlations
- **R Implementation:**
  - `cor()`, `cor.test()`, `rcorr()` function comparison
  - `corrplot` package for heatmaps
  - `GGally::ggpairs()` for scatterplot matrices
  - `ppcor` for partial correlations
  - `cocor` for comparing correlations
- **Advanced Topics:**
  - Anscombe's Quartet demonstration
  - Outlier influence visualization
  - Effect sizes (Cohen's guidelines)
  - APA-style reporting with examples
  - Common pitfalls and solutions

**Special Features:**
- 50+ visualizations and scatterplots
- Three practice exercises with complete solutions
- Comprehensive function reference table
- Venn diagrams for shared variance
- Assumption checking workflows
- Professional correlation matrices
- Complete glossary of terms
- 9 detailed IEEE citations to Field et al. Chapter 6

**Materials:**
- 📄 [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week08/08_R_for_DataAnalytics.html) (2,700+ lines of code!)
- 📊 [Original Lecture](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week08/08_correlation.html)
- 📂 [Week 08 Folder](Week08/)

---

## 🎯 Key Features

### Code-First Approach
All examples are executable and reproducible. You can run every code chunk yourself and experiment with modifications.

### Theory-Grounded
IEEE-style citations from Field, Miles, and Field (2012) *Discovering Statistics Using R*. Every major concept is properly referenced with specific page numbers.

### Beginner-Friendly
- Plain English explanations for every technical concept
- Real-world analogies to make concepts accessible
- "In plain English" sections throughout
- Extensive interpretation guides
- Troubleshooting sections

### Professional Quality
- Publication-ready figures and tables
- Comprehensive data visualizations
- Professional formatting and styling
- Complete documentation

### Reproducible
- Seedhash integration for consistent results
- MD5 hashes for verification
- Session info included
- All code is self-contained

---

## 📖 Course Structure

### Prerequisites
- Basic computer literacy
- Willingness to learn programming
- No prior R experience required

### Learning Path
1. **Weeks 02-03**: R fundamentals and data wrangling
2. **Week 04**: Statistical inference foundations
3. **Week 05**: Data visualization mastery
4. **Weeks 06-07**: Data screening and assumption checking
5. **Week 08**: Correlation analysis and relationships
6. **Weeks 09+**: Advanced statistical analyses (regression, t-tests, ANOVA)

### Time Commitment
- Each tutorial: 2-4 hours to work through
- Practice exercises: 1-2 hours per week
- Lab assignments: 2-3 hours per week

---

## 💻 Software Requirements

### Required Software
- **R** (version 4.0 or higher): [Download R](https://cran.r-project.org/)
- **RStudio** (recommended): [Download RStudio](https://posit.co/download/rstudio-desktop/)
  - Alternative: VS Code with R extension

### Required R Packages
```r
# Core packages
install.packages(c(
  "tidyverse",    # Data wrangling and visualization
  "ggplot2",      # Advanced plotting
  "dplyr",        # Data manipulation
  "tidyr",        # Data reshaping
  "rio",          # Data import/export
  "knitr",        # Report generation
  "rmarkdown"     # Document creation
))

# Week-specific packages
install.packages(c(
  "mice",         # Multiple imputation (Week 06)
  "car",          # Regression diagnostics (Week 07)
  "moments",      # Skewness and kurtosis (Week 07)
  "corrplot",     # Correlation visualization (Weeks 07-08)
  "GGally",       # Scatterplot matrices (Week 08)
  "Hmisc",        # Advanced correlations (Week 08)
  "ppcor",        # Partial correlations (Week 08)
  "cocor",        # Comparing correlations (Week 08)
  "psych",        # Correlation matrices with p-values (Week 08)
  "kableExtra",   # Table formatting
  "seedhash",     # Reproducible seeds
  "DiagrammeR"    # Flowcharts and diagrams (Week 07)
))
```

---

## 📚 Textbook and References

### Primary Textbook
**Field, A., Miles, J., & Field, Z. (2012).** *Discovering Statistics Using R.*  
London: SAGE Publications.

Local reference file: `Knowledge/Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

### Additional References
- Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.)
- Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis* (2nd ed.)
- Wilkinson, L. (2005). *The Grammar of Graphics* (2nd ed.)
- Little, R. J. A., & Rubin, D. B. (2020). *Statistical Analysis with Missing Data* (3rd ed.)
- Van Buuren, S. (2018). *Flexible Imputation of Missing Data* (2nd ed.)
- Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7th ed.)

---

## 🎓 Learning Objectives

By the end of this course, students will be able to:

1. **Program in R**: Write, debug, and execute R code for data analysis
2. **Wrangle Data**: Import, clean, transform, and reshape datasets
3. **Visualize Data**: Create publication-quality graphics using ggplot2
4. **Test Hypotheses**: Conduct and interpret statistical tests
5. **Screen Data**: Identify and handle missing data, outliers, and violations
6. **Check Assumptions**: Verify parametric test requirements
7. **Interpret Results**: Communicate findings clearly and accurately
8. **Reproduce Analyses**: Create fully reproducible research workflows

---

## 📂 Repository Structure

```
ANLY500-Analytics-I/
├── README.md                 # This file
├── Knowledge/                # Reference materials
│   └── Field_ea_2012_...txt # Textbook reference
├── _template/                # R Markdown templates
├── Week01/                   # Introduction
├── Week02/                   # R Basics
│   ├── README.md
│   ├── 02_R_for_DataAnalytics.rmd
│   ├── 02_R_for_DataAnalytics.html
│   ├── lab/
│   └── pictures/
├── Week03/                   # Data Wrangling
│   ├── README.md
│   ├── 03_R_for_DataAnalytics.rmd
│   ├── 03_R_for_DataAnalytics.html
│   └── lab/
├── Week04/                   # Statistical Inference
│   ├── README.md
│   ├── 04_R_for_DataAnalytics.rmd
│   ├── 04_R_for_DataAnalytics.html
│   └── proposal/
├── Week05/                   # Data Visualization
│   ├── README.md
│   ├── 05_R_for_DataAnalytics.rmd
│   ├── 05_R_for_DataAnalytics.html
│   ├── 05_graphs.rmd
│   ├── 05_graphs.html
│   ├── data/
│   ├── lab/
│   └── pictures/
├── Week06/                   # Data Screening Part 1
│   ├── README.md
│   ├── 06_R_for_DataAnalytics.rmd
│   ├── 06_R_for_DataAnalytics.html
│   ├── 06_datascreen_1.rmd
│   ├── 06_datascreen_1.html
│   ├── data/
│   ├── lab/
│   └── pictures/
└── Week07/                   # Data Screening Part 2
    ├── README.md
    ├── 07_R_for_DataAnalytics.rmd (2,791 lines!)
    ├── 07_R_for_DataAnalytics.html (8,243 lines!)
    ├── 07_datascreen_2.rmd
    ├── 07_datascreen_2.html
    ├── ENHANCEMENTS_SUMMARY.md
    ├── data/
    └── pictures/
```

---

## 🚀 Getting Started

### For Students

1. **Clone the repository**:
   ```bash
   git clone https://github.com/melhzy/data_sciences.git
   cd data_sciences/ANLY500-Analytics-I
   ```

2. **Install R and RStudio** (see Software Requirements above)

3. **Install required packages**:
   ```r
   source("install_packages.R")  # If available
   # Or manually install packages listed above
   ```

4. **Start with Week 02**:
   - Read the [Week 02 README](Week02/README.md)
   - Open `02_R_for_DataAnalytics.rmd` in RStudio
   - Work through the tutorial step-by-step

5. **Progress sequentially** through each week

### For Instructors

- All materials are freely available for educational use
- Each week has a comprehensive README with learning objectives
- Lab assignments are included in `lab/` folders
- Rubrics are provided where applicable
- All code is reproducible with seedhash

---

## 📊 Highlights by Week

### Week 02: Foundation
- First steps in R programming
- Understanding data types and structures
- Basic statistical concepts

### Week 03: Data Skills
- Professional data wrangling workflows
- Tidy data principles in practice
- Exploratory data analysis techniques

### Week 04: Statistics
- Hypothesis testing framework
- Understanding p-values and confidence intervals
- Effect sizes and power analysis

### Week 05: Visualization
- Grammar of Graphics mastery
- Publication-quality figures
- Tufte's principles in practice

### Week 06: Data Quality
- Comprehensive missing data handling
- Multiple imputation with MICE
- Outlier detection strategies

### Week 07: Assumptions ⭐
- **Most comprehensive tutorial** (2,791 lines!)
- **60+ visualizations** explaining concepts
- **Complete diagnostic workflow**
- **Transformation guide** with examples
- **Decision trees** for violations

### Week 08: Correlation 🆕
- **Complete correlation guide** (2,700+ lines!)
- **50+ visualizations** and scatterplots
- **Anscombe's Quartet** demonstration
- **Partial/semi-partial** correlations
- **APA reporting** with examples

---

## 🎨 Visual Learning

This course emphasizes visual learning with:

- **550+ figures** across all weeks
- **Color-coded examples** (✓ green = good, ✗ red = bad)
- **Side-by-side comparisons** of correct vs. incorrect approaches
- **Diagnostic dashboards** for comprehensive checks
- **Flowcharts and decision trees** for workflows
- **Annotated plots** with interpretation guides
- **Correlation matrices** and scatterplot arrays
- **Anscombe's Quartet** and classic statistical demonstrations

---

## 💡 Tips for Success

### Before Starting
- ✅ Install all required software
- ✅ Set up a dedicated workspace
- ✅ Download all course materials
- ✅ Join the course discussion forum (if available)

### While Learning
- 📖 Read the plain English explanations first
- 💻 Run every code chunk yourself
- 🎨 Study the visualizations carefully
- ✍️ Take notes on key concepts
- 🔄 Experiment with modifications

### When Stuck
- 🤔 Re-read the "In plain English" sections
- 📊 Compare your output to the examples
- 🔍 Check the troubleshooting sections in READMEs
- 💬 Ask questions in the discussion forum
- 📧 Contact the instructor

### Common Pitfalls to Avoid
- ❌ Skipping the setup chunks
- ❌ Not installing required packages
- ❌ Copying code without understanding
- ❌ Ignoring warning messages
- ❌ Not checking your working directory

---

## 🔧 Troubleshooting

### Common Issues

**Issue**: "Error: package 'X' not found"
- **Solution**: Run `install.packages("X")`

**Issue**: "Error: could not find function"
- **Solution**: Load the package with `library(package_name)`

**Issue**: "Error in file(file, 'rt'): cannot open the connection"
- **Solution**: Check your working directory with `getwd()` and set it correctly

**Issue**: Plots don't appear
- **Solution**: Make sure you're running code in RStudio or have a graphics device open

**Issue**: Can't knit Rmd files
- **Solution**: Install `rmarkdown` and `knitr` packages

---

## 📈 Course Statistics

- **Total Lines of R Code**: 15,000+
- **Total Visualizations**: 500+
- **Total Pages (PDF equivalent)**: 1,000+
- **Weeks of Content**: 7 (with more coming)
- **Practice Exercises**: 50+
- **Lab Assignments**: 7+
- **IEEE Citations**: 50+

---

## 🌐 Online Resources

### Course Website
- **Main Site**: [https://melhzy.github.io/data_sciences/](https://melhzy.github.io/data_sciences/)
- **GitHub Repository**: [https://github.com/melhzy/data_sciences](https://github.com/melhzy/data_sciences)

### Individual Week Links
- [Week 02 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week02/02_R_for_DataAnalytics.html)
- [Week 03 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.html)
- [Week 04 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week04/04_R_for_DataAnalytics.html)
- [Week 05 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week05/05_R_for_DataAnalytics.html)
- [Week 06 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week06/06_R_for_DataAnalytics.html)
- [Week 07 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week07/07_R_for_DataAnalytics.html) ⭐
- [Week 08 Tutorial](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week08/08_R_for_DataAnalytics.html) 🆕

### External Resources
- [R Documentation](https://www.rdocumentation.org/)
- [RStudio Cheatsheets](https://posit.co/resources/cheatsheets/)
- [ggplot2 Documentation](https://ggplot2.tidyverse.org/)
- [Stack Overflow - R Tag](https://stackoverflow.com/questions/tagged/r)

---

## 📝 Citation

If you use these materials in your work, please cite:

```
Huang, Z. (2026). ANLY 500 Analytics I: Comprehensive R Tutorials for Data Analytics.
Harrisburg University. Retrieved from https://melhzy.github.io/data_sciences/
```

Based on:
```
Field, A., Miles, J., & Field, Z. (2012). Discovering Statistics Using R. 
London: SAGE Publications.
```

---

## 🤝 Contributing

This is an educational repository. For questions, corrections, or suggestions:

- **Issues**: Submit via [GitHub Issues](https://github.com/melhzy/data_sciences/issues)
- **Pull Requests**: Welcome for typo fixes and improvements
- **Contact**: Through Harrisburg University course channels

---

## 📜 License

These materials are provided for educational purposes. Please respect academic integrity policies when using these materials.

---

## 🙏 Acknowledgments

- **Field, Miles, and Field** for the excellent *Discovering Statistics Using R* textbook
- **Hadley Wickham** for the tidyverse and ggplot2
- **RStudio/Posit** for the amazing IDE
- **Harrisburg University** for supporting this course
- **All students** who have provided feedback and suggestions

---

## 📅 Version History

- **v1.1** (January 22, 2026): Week 08 correlation analysis added 🆕
  - Complete correlation tutorial with 50+ visualizations
  - Pearson, Spearman, Kendall correlations
  - Partial and semi-partial correlations
  - Anscombe's Quartet and assumption violations
  - Comprehensive APA reporting guide
  - 9 IEEE citations to Field et al. Chapter 6
- **v1.0** (January 2026): Initial comprehensive release
  - Weeks 02-07 complete
  - 60+ visualizations in Week 07
  - Full IEEE citations throughout
  - Comprehensive READMEs for all weeks

---

## 🎯 What's Next?

### Upcoming Content
- Week 09: Simple and multiple regression
- Week 10: t-tests and group comparisons
- Week 11: ANOVA (one-way and factorial)
- Week 12: Advanced ANOVA topics
- Week 13: Non-parametric tests
- Week 14: Final project guidance

### Stay Updated
- Watch the [GitHub repository](https://github.com/melhzy/data_sciences) for updates
- Check the [course website](https://melhzy.github.io/data_sciences/) regularly
- Follow course announcements

---

<div align="center">

## 🎓 Ready to Start Your Data Analytics Journey?

### [Begin with Week 02 →](Week02/)

### [Visit Course Website →](https://melhzy.github.io/data_sciences/)

---

**ANLY 500 - Analytics I**  
*Harrisburg University*

Built with ❤️ using R, RMarkdown, and ggplot2

**Last Updated**: January 8, 2026

</div>
