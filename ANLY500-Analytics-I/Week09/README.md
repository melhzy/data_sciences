# Week 09: Linear Regression

## Lecture Materials

### Viewing the Presentations

This week has two HTML presentations covering linear regression and predictive modeling:

#### 1. Linear Regression (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week09/09_regression.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week09/09_regression.html)

**Option 3: Download and Open Locally**
- Download `09_regression.html` and open in your web browser

#### 2. R for Data Analytics (Week 09 Comprehensive Tutorial) 🆕 ⭐

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week09/09_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week09/09_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `09_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week introduces **Linear Regression**, a powerful statistical method for predicting outcomes and quantifying relationships between variables. We move from simple correlation to building predictive models with multiple predictors.

### Lecture Topics
- **Simple Linear Regression**: Predicting Y from X
- **The Regression Line**: Intercepts ($b_0$) and Slopes ($b_1$)
- **Goodness of Fit**: $R^2$, Adjusted $R^2$, and F-ratio
- **Multiple Regression**: Handling multiple predictors simultaneously
- **Hierarchical Regression**: Testing models in blocks (Model 1 vs. Model 2)
- **Assumptions**: Linearity, Homoscedasticity, Independence, Normality, Multicollinearity
- **Dummy Coding**: Handling categorical predictors in regression
- **Outliers & Influential Cases**: Cook's Distance, Leverage, Standardized Residuals

### R Tutorial Topics
- **Data Preparation**: Cleaning and subsetting for regression
- **Simple Regression**: `lm()` function basics and interpretation
- **Multiple Regression**: Adding predictors and interpreting coefficients
- **Hierarchical Regression**: Using `anova()` to compare nested models
- **Standardized Betas**: Comparing predictor strength using `lm.beta`
- **Dummy Coding**: Using `fastDummies` or manual coding for categorical variables
- **Diagnostics**:
  - Visualizing assumptions with `plot(model)`
  - Testing Multicollinearity with `vif()`
  - Checking residuals with `durbinWatsonTest()`
  - Identifying influential cases with Cook's Distance
- **APA Reporting**: How to report regression tables and statistics

---

## Materials

- **Lecture Slides**: `09_regression.rmd` → `09_regression.html` (Slidy presentation)
- **R Tutorial**: `09_R_for_DataAnalytics.rmd` → `09_R_for_DataAnalytics.html`
- **Data Files**: `data/` folder
  - `regression_data.sav` - Main dataset for regression examples (CESD, PIL, AUDIT, DAST)
  - `dummy_code.sav` - Dataset for dummy coding examples
- **Images**: `pictures/` folder (lecture graphics)

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
  - **Chapter 7: Regression** (pp. 299-356)
    - Section 7.1: An introduction to regression
    - Section 7.2: Simple regression (The model, assessing the model)
    - Section 7.3: Multiple regression (Methods, accuracy)
    - Section 7.4: Assumptions of the linear model
    - Section 7.5: Generalizing the model (Cross-validation, Sample size, Multicollinearity)
    - Section 7.6: Regression in R (Simple, Multiple, Hierarchical)
    - Section 7.7: Interpreting regression
    - Section 7.8: Reporting regression
    - Section 7.9: Dummy coding (Categorical predictors)

  Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`
