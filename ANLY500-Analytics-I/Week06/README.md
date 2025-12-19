# Week 06: Data Screening and Preparation

## Lecture Materials

### Viewing the Presentations

This week has two HTML presentations covering essential data screening techniques:

#### 1. Data Screening Part 1 (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week06/06_datascreen_1.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week06/06_datascreen_1.html)

**Option 3: Download and Open Locally**
- Download `06_datascreen_1.html` and open in your web browser

#### 2. R for Data Analytics (Week 06 Hands-on Tutorial) 🆕

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week06/06_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week06/06_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `06_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week focuses on **data screening and preparation**, a critical step before any statistical analysis:

### Lecture Topics
- Data screening importance and workflow
- Types of missing data mechanisms (MCAR, MAR, MNAR)
- Strategies for handling missing data
  - Listwise deletion
  - Pairwise deletion
  - Mean/median/mode imputation
  - Multiple imputation (MICE)
- Outlier detection methods
  - Z-scores
  - Boxplots and IQR rule
  - Mahalanobis distance
- Data transformation techniques
- Assumption checking for parametric tests

### R Tutorial Topics
- **Missing Data Analysis**: Identifying patterns, visualizing missingness
- **Missing Data Mechanisms**: Testing for MCAR vs. MAR vs. MNAR
- **Imputation Techniques**: Single imputation vs. multiple imputation with MICE
- **Outlier Detection**: Z-scores, boxplots, visualization techniques
- **Data Transformation**: Log, square root, inverse transformations
- **Normality Assessment**: Histograms, Q-Q plots, Shapiro-Wilk test
- **Practical Workflow**: Step-by-step data screening checklist

---

## Materials

- **Lecture Slides**: `06_datascreen_1.rmd` → `06_datascreen_1.html` (Slidy presentation)
- **R Tutorial**: `06_R_for_DataAnalytics.rmd` → `06_R_for_DataAnalytics.html` (Interactive tutorial)
- **Lab Assignment**: `lab/` folder
  - `06_lab.Rmd` - Student assignment template
  - `06_data.csv` - Practice dataset for lab exercises
- **Data Files**: `data/` folder
  - `data_screening.csv` - Example dataset with missing data and outliers
- **Images**: `pictures/` folder (lecture graphics)
  - `missing.PNG` - Missing data visualization examples

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
  - Chapter 5: The beast of bias
    - Section 5.1: What is bias?
    - Section 5.2: Sources of bias
    - Section 5.3: Outliers
    - Section 5.4: Normality
    - Section 5.5: Homogeneity of variance
    - Section 5.6: Dealing with bias
    - Section 5.7: Transformations
    - Section 5.8: When transformations fail
  
  Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

- **Additional References**:
  - Little, R. J. A., & Rubin, D. B. (2020). *Statistical Analysis with Missing Data* (3rd ed.)
  - Van Buuren, S. (2018). *Flexible Imputation of Missing Data* (2nd ed.)
  - Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7th ed.)

---

## Learning Path

### Step 1: Theory
1. Review the Week 06 lecture (`06_datascreen_1.html`)
2. Understand the three types of missing data mechanisms (MCAR, MAR, MNAR)
3. Learn when to use each missing data handling strategy
4. Study outlier detection methods and their assumptions

### Step 2: Practice
1. Work through `06_R_for_DataAnalytics.html`
2. Identify and visualize missing data patterns
3. Apply multiple imputation using MICE package
4. Detect outliers using Z-scores and boxplots
5. Transform non-normal data and reassess distributions
6. Create complete data screening workflow

### Step 3: Apply
1. Complete the lab assignment in `lab/`
2. Screen data for your final project
3. Document all data cleaning decisions
4. Report missing data and outlier handling in your methods section

---

## Key Concepts

### Missing Data Mechanisms

| Mechanism | Definition | Example | Handling Strategy |
|-----------|------------|---------|-------------------|
| **MCAR** (Missing Completely At Random) | Missing values are unrelated to any variable | Equipment malfunction | Listwise deletion acceptable |
| **MAR** (Missing At Random) | Missing values related to observed data, not the missing values themselves | Older adults skip technology questions | Multiple imputation recommended |
| **MNAR** (Missing Not At Random) | Missing values related to the unobserved values | People with depression skip depression items | Requires specialized models |

### Missing Data Strategies

| Strategy | Description | Advantages | Disadvantages |
|----------|-------------|------------|---------------|
| **Listwise Deletion** | Remove any case with missing data | Simple, unbiased if MCAR | Reduces sample size, power loss |
| **Pairwise Deletion** | Use all available data for each analysis | Retains more data than listwise | Different N for each test, biased if not MCAR |
| **Mean Imputation** | Replace missing with variable mean | Simple, retains sample size | Reduces variance, distorts relationships |
| **Multiple Imputation** | Create multiple plausible datasets | Preserves variance, accounts for uncertainty | Complex, requires MAR assumption |

### Outlier Detection Methods

#### 1. Z-Score Method
- **Cutoff**: |z| > 3.29 (p < .001)
- **Formula**: z = (X - M) / SD
- **Pros**: Simple, standardized
- **Cons**: Assumes normality, univariate only

#### 2. IQR Method (Boxplot Rule)
- **Mild outliers**: < Q1 - 1.5×IQR or > Q3 + 1.5×IQR
- **Extreme outliers**: < Q1 - 3×IQR or > Q3 + 3×IQR
- **Pros**: Robust, non-parametric
- **Cons**: Only considers one variable at a time

#### 3. Mahalanobis Distance
- **Multivariate**: Considers correlations between variables
- **Cutoff**: χ² critical value at p < .001
- **Pros**: Detects multivariate outliers
- **Cons**: Requires larger sample size

### Data Transformations

| Transformation | When to Use | R Code | Effect |
|----------------|-------------|--------|--------|
| **Log** | Positive skew, exponential growth | `log10(x)` or `log(x)` | Compresses high values |
| **Square Root** | Moderate positive skew, count data | `sqrt(x)` | Less aggressive than log |
| **Inverse** | Severe positive skew | `1/x` | Most aggressive |
| **Reflect & Transform** | Negative skew | `log10(max(x) + 1 - x)` | Reverse then transform |
| **Square** | Negative skew (rare) | `x^2` | Expands high values |

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "ggplot2", "dplyr", "rio", "knitr", "kableExtra"))
install.packages(c("mice", "VIM", "naniar"))  # Missing data handling
install.packages(c("moments", "psych", "pastecs"))  # Normality tests
install.packages("car")  # Outlier tests (Mahalanobis)
install.packages("seedhash")  # Reproducible analysis
```

### Key Functions by Package

**Missing Data Visualization**:
```r
library(naniar)
vis_miss(data)  # Visualize missing data patterns
gg_miss_var(data)  # Bar chart of missingness by variable
gg_miss_upset(data)  # Combinations of missingness
```

**Multiple Imputation**:
```r
library(mice)
md.pattern(data)  # Missing data pattern table
imp <- mice(data, m=5, method='pmm', seed=500)  # Impute
complete(imp, 1)  # Get first imputed dataset
pool(with(imp, lm(y ~ x)))  # Pool results across imputations
```

**Outlier Detection**:
```r
# Z-scores
scale(data$variable)  # Standardize
abs(scale(data$variable)) > 3.29  # Identify outliers

# Mahalanobis distance
library(car)
mahalanobis(data, center=colMeans(data), cov=cov(data))
```

**Normality Tests**:
```r
shapiro.test(data$variable)  # Shapiro-Wilk test
library(moments)
skewness(data$variable)  # Skewness statistic
kurtosis(data$variable)  # Kurtosis statistic
```

---

## Data Screening Workflow (Checklist)

### Phase 1: Initial Inspection
- [ ] Load data and check dimensions (`dim()`, `str()`)
- [ ] Examine variable types (`class()`, `summary()`)
- [ ] Verify variable ranges (min, max plausible?)
- [ ] Check for impossible values (e.g., age = 200)

### Phase 2: Missing Data
- [ ] Identify missing data patterns (`vis_miss()`, `md.pattern()`)
- [ ] Calculate percentage missing per variable
- [ ] Test for MCAR mechanism (Little's test)
- [ ] Decide on handling strategy (deletion vs. imputation)
- [ ] If imputing, use MICE with appropriate method
- [ ] Compare complete-case vs. imputed analyses

### Phase 3: Outliers
- [ ] Create boxplots for each continuous variable
- [ ] Calculate z-scores, flag |z| > 3.29
- [ ] Check for multivariate outliers (Mahalanobis distance)
- [ ] Investigate outlier cases (data entry errors?)
- [ ] Decide: keep, transform, or remove
- [ ] Document decisions

### Phase 4: Assumptions
- [ ] Assess normality (histograms, Q-Q plots, Shapiro-Wilk)
- [ ] Check for skewness (|skew| > 2 problematic)
- [ ] Check for kurtosis (|kurtosis - 3| > 7 problematic)
- [ ] Test homogeneity of variance (Levene's test)
- [ ] Apply transformations if needed
- [ ] Recheck assumptions after transformation

### Phase 5: Documentation
- [ ] Record sample size before/after cleaning
- [ ] Document all missing data decisions
- [ ] List all outliers removed/transformed
- [ ] Report all transformations applied
- [ ] Note any deviations from normality
- [ ] Save cleaned dataset with version number

---

## Common Data Screening Mistakes to Avoid

### ❌ Bad Practices
1. **Ignoring missing data** and proceeding with analysis
2. **Always deleting outliers** without investigation
3. **Using mean imputation** (distorts variance)
4. **Not testing missing data mechanism** before choosing strategy
5. **Transforming without checking if needed**
6. **Not documenting data cleaning decisions**
7. **Screening data after seeing results** (p-hacking)

### ✅ Good Practices
1. **Always visualize missing data patterns** before deciding strategy
2. **Investigate outliers** - could be data entry errors or true extreme values
3. **Use multiple imputation (MICE)** when appropriate
4. **Test MCAR assumption** with Little's test
5. **Transform only when assumptions violated**
6. **Document every data cleaning step** in your methods
7. **Screen data before any hypothesis testing**

---

## MICE (Multiple Imputation by Chained Equations)

### Why MICE?
- Preserves variability (unlike mean imputation)
- Accounts for uncertainty in missing values
- Creates multiple plausible datasets (typically 5-20)
- Pools results across imputations
- More accurate standard errors and p-values

### MICE Workflow
```r
library(mice)

# Step 1: Check missing data pattern
md.pattern(data)

# Step 2: Impute (m=5 datasets, method='pmm' for numeric)
imp <- mice(data, m=5, method='pmm', seed=500, printFlag=FALSE)

# Step 3: Check convergence
plot(imp)  # Should show mixing

# Step 4: Get imputed datasets
complete_data <- complete(imp, "long")  # Long format (all 5 stacked)
complete_data1 <- complete(imp, 1)      # Just first imputed dataset

# Step 5: Analyze each imputed dataset
fit <- with(imp, lm(outcome ~ predictor1 + predictor2))

# Step 6: Pool results
pooled <- pool(fit)
summary(pooled)
```

### MICE Imputation Methods
- **`pmm`**: Predictive mean matching (default for numeric, recommended)
- **`norm`**: Bayesian linear regression (numeric, assumes normality)
- **`logreg`**: Logistic regression (binary)
- **`polyreg`**: Multinomial logistic regression (categorical >2 levels)
- **`polr`**: Proportional odds model (ordinal)

---

## Example Datasets

### 1. Data Screening Dataset
- **File**: `data/data_screening.csv`
- **Purpose**: Practice dataset with intentional missing data and outliers
- **Variables**: 
  - Demographic variables (age, gender)
  - Continuous outcomes with missing values
  - Variables with outliers (extreme scores)
- **Use**: Demonstrate complete data screening workflow

### 2. Lab Dataset
- **File**: `lab/06_data.csv`
- **Purpose**: Student practice dataset for lab assignment
- **Features**: Real-world messiness (missing, outliers, non-normality)
- **Use**: Students apply data screening techniques independently

---

## Reporting Data Screening (APA Style)

### Missing Data Section
> "Data were screened for missing values. Little's MCAR test indicated that data were missing completely at random, χ²(df) = XX.XX, p = .XXX. Of the 200 participants, 15 (7.5%) had missing data on at least one variable. Missing data ranged from 2% (Variable A) to 12% (Variable B). Multiple imputation using chained equations (MICE; Van Buuren & Groothuis-Oudshoorn, 2011) with predictive mean matching was used to create five imputed datasets. Results were pooled across imputations using Rubin's rules (Rubin, 1987)."

### Outlier Section
> "Outliers were examined using z-scores (|z| > 3.29, p < .001) and boxplots. Five univariate outliers were identified across three variables. Visual inspection and Mahalanobis distance (χ² critical value = XX.XX, p < .001) revealed two multivariate outliers. Upon investigation, these cases represented valid extreme scores rather than data entry errors and were retained in analyses. Sensitivity analyses with and without outliers revealed no substantive differences in results."

### Normality Section
> "Normality was assessed using histograms, Q-Q plots, and Shapiro-Wilk tests. Variable C showed significant positive skew (skewness = 2.45, SE = 0.17) and departed from normality, W = 0.89, p < .001. A log10 transformation was applied, which successfully normalized the distribution (skewness = 0.45; W = 0.98, p = .135). All subsequent analyses used the transformed variable."

---

## Quick Reference: When to Use Each Strategy

### Missing Data Decision Tree
```
Is the data MCAR?
├─ Yes (Little's test p > .05)
│  ├─ Missing < 5%? → Listwise deletion OK
│  └─ Missing > 5%? → Multiple imputation (retain power)
└─ No (MAR or MNAR suspected)
   ├─ Can you model missingness? → Multiple imputation with auxiliary variables
   └─ Cannot model? → Sensitivity analyses, report limitations
```

### Outlier Decision Tree
```
Is it a data entry error?
├─ Yes → Correct or remove
└─ No
   ├─ Univariate outlier only?
   │  ├─ |z| < 3.29? → Keep
   │  └─ |z| > 3.29? → Consider transformation
   └─ Multivariate outlier?
      ├─ Mahalanobis p < .001? → Investigate context
      └─ Keep if theoretically valid, report sensitivity analysis
```

### Transformation Decision Tree
```
Check skewness and kurtosis
├─ |skew| < 2 AND |kurtosis - 3| < 7? → No transformation needed
└─ Violated?
   ├─ Positive skew?
   │  ├─ Mild → Square root
   │  ├─ Moderate → Log
   │  └─ Severe → Inverse
   ├─ Negative skew?
   │  └─ Reflect then apply positive skew transformation
   └─ Recheck normality after transformation
```

---

## Troubleshooting Common Errors

### Error: "mice() cannot handle factor variables with >53 levels"
- **Cause**: Too many levels for imputation
- **Fix**: Recode or use different method, or remove variable from imputation

### Error: "system is computationally singular"
- **Cause**: Perfect multicollinearity in imputation model
- **Fix**: Remove redundant predictors from MICE predictor matrix

### Warning: "Logged values are NaN"
- **Cause**: Variable contains zero or negative values
- **Fix**: Add constant before log: `log10(x + 1)` or `log10(x - min(x) + 1)`

### Error: "Shapiro-Wilk test not applicable (n > 5000)"
- **Cause**: Sample too large for Shapiro-Wilk
- **Fix**: Use visual inspection (Q-Q plot) or Anderson-Darling test

### Missing data visualizations not showing
- **Cause**: `naniar` or `VIM` package not loaded
- **Fix**: Run `library(naniar)` or `library(VIM)`

---

## Practice Exercises

### Exercise 1: Missing Data Analysis
Using the `airquality` dataset, identify missing data patterns, test for MCAR, and apply multiple imputation. Compare means before and after imputation.

### Exercise 2: Outlier Detection
Using the `mtcars` dataset, identify univariate outliers using z-scores and boxplots. Calculate Mahalanobis distance to detect multivariate outliers.

### Exercise 3: Transformation
Using the `iris` dataset, assess normality of `Sepal.Width`. If non-normal, apply an appropriate transformation and reassess.

### Exercise 4: Complete Screening Workflow
With a provided messy dataset, perform all data screening steps: missing data, outliers, normality. Document every decision and create a cleaned dataset ready for analysis.

---

## Quick Links

- [← Week 05: Data Visualization](../Week05/README.md)
- [→ Week 07 Materials](../Week07/README.md) *(Coming Soon)*
- [Back to Course Home](../README.md)
- [View All Tutorials (GitHub Pages)](https://melhzy.github.io/data_sciences/)

---

## Additional Resources

### Online Documentation
- [MICE Package Documentation](https://amices.org/mice/)
- [naniar Package for Missing Data](https://naniar.njtierney.com/)
- [VIM Package for Missing Data Visualization](https://cran.r-project.org/web/packages/VIM/index.html)

### Books
- Van Buuren, S. (2018). *Flexible Imputation of Missing Data* (2nd ed.) - [Free online](https://stefvanbuuren.name/fimd/)
- Little, R. J. A., & Rubin, D. B. (2020). *Statistical Analysis with Missing Data* (3rd ed.)
- Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7th ed.)

### Interactive Learning
- [R for Data Science - Missing Values](https://r4ds.had.co.nz/transform.html#missing-values)
- [MICE Vignette](https://www.gerkovink.com/miceVignettes/)
- [Data Screening Tutorial (YouTube)](https://www.youtube.com/results?search_query=data+screening+in+r)

### Software
- [SPSS Missing Value Analysis](https://www.ibm.com/docs/en/spss-statistics/29.0.0?topic=analysis-missing-value) (Alternative)
- [Stata MI Commands](https://www.stata.com/manuals/mi.pdf) (Alternative)

---

## Final Project Checkpoint

By Week 06, you should have:
- [ ] Selected your dataset from UCI Machine Learning Repository
- [ ] Imported data into R successfully
- [ ] Completed initial data inspection
- [ ] Identified any missing data or data quality issues
- [ ] Begun data screening workflow
- [ ] Started documenting data cleaning decisions

**Next Week**: Begin your primary statistical analyses with cleaned data!

---

<div align="center">

**ANLY 500 - Analytics I**  
*Harrisburg University*

Last Updated: December 18, 2025

</div>
