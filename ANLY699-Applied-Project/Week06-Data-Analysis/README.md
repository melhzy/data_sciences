# Week 6: Data Analysis

## Overview

This week covers statistical analysis and machine learning model development for analytics projects. You'll learn to select appropriate tests, interpret results, and document your analytical approach following APA guidelines.

## Learning Objectives

By the end of this week, you will be able to:
1. Select appropriate statistical tests for your research questions
2. Check and report assumption violations
3. Conduct and interpret inferential statistics
4. Develop and evaluate predictive models
5. Calculate and report effect sizes
6. Document analytical procedures in R Markdown

## Required Reading

📄 **Primary Resources**: 
- `../APA7/Introduction to Research Statistical Analysis.pdf`
- Review ANLY500 Week02 tutorial for statistical foundations

📄 **Sample Papers**: Examine analysis approaches in:
- `../SamplePapers/Net Photosynthetic Rate.pdf` (Statistical analysis)
- `../SamplePapers/Unveiling the Genetic Networks.pdf` (Complex modeling)

## Tutorial Content

### 1. Statistical Test Selection

#### Decision Tree

```r
# Statistical test selection guide

select_test <- function(research_question, iv_type, dv_type, n_groups) {
  if (research_question == "describe") {
    return("Descriptive statistics: M, SD, frequencies")
  }
  
  if (research_question == "compare") {
    if (dv_type == "continuous") {
      if (n_groups == 2) return("Independent t-test or Mann-Whitney U")
      if (n_groups > 2) return("One-way ANOVA or Kruskal-Wallis")
    }
    if (dv_type == "categorical") {
      return("Chi-square test or Fisher's exact test")
    }
  }
  
  if (research_question == "relationship") {
    if (iv_type == "continuous" & dv_type == "continuous") {
      return("Pearson or Spearman correlation")
    }
  }
  
  if (research_question == "predict") {
    if (dv_type == "continuous") return("Multiple regression")
    if (dv_type == "binary") return("Logistic regression")
    if (dv_type == "count") return("Poisson regression")
  }
}
```

| Research Question | IV Type | DV Type | Recommended Test |
|-------------------|---------|---------|------------------|
| Group difference | Categorical (2 groups) | Continuous | Independent t-test |
| Group difference | Categorical (3+ groups) | Continuous | One-way ANOVA |
| Group difference | Categorical | Categorical | Chi-square test |
| Association | Continuous | Continuous | Pearson correlation |
| Prediction | Multiple | Continuous | Multiple regression |
| Prediction | Multiple | Binary | Logistic regression |
| Prediction | Multiple | Multiple | Multivariate regression |

### 2. Descriptive Statistics

#### Complete Reporting

```r
# Comprehensive descriptive statistics

library(dplyr)
library(psych)

# Generate descriptives
descriptives <- data %>%
  select(age, satisfaction, usage_frequency) %>%
  describe() %>%
  select(n, mean, sd, median, min, max, skew, kurtosis)

# Create APA-style table
library(knitr)
library(kableExtra)

descriptives %>%
  kable(digits = 2, caption = "Descriptive Statistics for Key Variables") %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```

**In-text reporting**:

```markdown
## Descriptive Statistics

Participants' ages ranged from 22 to 67 years (M = 38.42, SD = 11.23, 
Mdn = 36). Customer satisfaction scores averaged 3.47 (SD = 0.89) on a 
5-point scale, slightly above the scale midpoint. Platform usage frequency 
was positively skewed (skew = 1.23, SE = 0.09), with most customers using 
the service 2-3 times per week (Mdn = 2.5 times/week) but some daily 
users (max = 28 times/week).

Table 1 presents descriptive statistics and correlations among study 
variables. As expected, satisfaction and usage frequency were positively 
correlated, r = .34, p < .001.
```

### 3. Assumption Checking

#### Parametric Test Assumptions

```r
# Check assumptions systematically

library(car)
library(nortest)

## 1. Normality
# Visual inspection
ggplot(data, aes(sample = outcome)) +
  stat_qq() +
  stat_qq_line() +
  labs(title = "Q-Q Plot for Outcome Variable")

# Statistical tests
shapiro.test(data$outcome)          # n < 5000
lillie.test(data$outcome)           # n ≥ 5000

## 2. Homogeneity of variance
leveneTest(outcome ~ group, data = data)

## 3. Linearity (for regression)
plot(lm_model, which = 1)  # Residuals vs Fitted

## 4. Independence (often conceptual)
# Document: "Observations were independent; each customer 
# provided data only once."

## 5. Multicollinearity (regression)
vif(lm_model)  # VIF < 10 acceptable, < 5 preferred
```

**Reporting violations**:

```markdown
## Assumption Testing

**Normality**. Visual inspection of Q-Q plots and Shapiro-Wilk tests 
indicated that outcome scores deviated from normality in the high-usage 
group (W = 0.94, p = .03) but not the low-usage group (W = 0.98, p = .12). 
Given the moderate deviation and large sample size (n = 327), we proceeded 
with parametric tests, which are robust to minor normality violations 
when n > 30 (Field, Miles, & Field, 2012).

**Homogeneity of Variance**. Levene's test indicated unequal variances 
across groups, F(2, 324) = 4.87, p = .008. Accordingly, we report 
Welch's corrected F-test, which does not assume equal variances.

**Multicollinearity**. Variance inflation factors (VIF) for all predictors 
were below 2.5, indicating no concerning multicollinearity (all VIF < 10; 
O'Brien, 2007).
```

### 4. Inferential Statistics

#### t-tests

```r
# Independent samples t-test

t_result <- t.test(satisfaction ~ group, data = data, var.equal = FALSE)

# Effect size (Cohen's d)
library(effsize)
d_result <- cohen.d(satisfaction ~ group, data = data)

# Report
## Between-Group Comparison

An independent-samples t-test examined whether satisfaction differed 
between high- and low-usage customers. Results indicated significantly 
higher satisfaction among high-usage customers (M = 4.12, SD = 0.67) 
compared to low-usage customers (M = 3.21, SD = 0.91), t(298.43) = 9.34, 
p < .001, 95% CI [0.73, 1.09], d = 1.14. The effect size was large 
(Cohen, 1988), suggesting a substantial practical difference.
```

#### ANOVA

```r
# One-way ANOVA

anova_model <- aov(outcome ~ group, data = data)
summary(anova_model)

# Effect size (eta-squared)
library(effectsize)
eta_squared(anova_model)

# Post-hoc tests (if significant)
library(emmeans)
emmeans(anova_model, pairwise ~ group, adjust = "bonferroni")

# Report
## One-Way ANOVA

A one-way ANOVA examined satisfaction across three customer segments 
(high-frequency, moderate-frequency, low-frequency). Results revealed 
significant differences, F(2, 324) = 27.84, p < .001, η² = .15. 
Post-hoc comparisons using Bonferroni corrections indicated that 
high-frequency customers (M = 4.23, SD = 0.61) reported significantly 
higher satisfaction than both moderate-frequency (M = 3.67, SD = 0.78, 
p < .001) and low-frequency customers (M = 3.12, SD = 0.94, p < .001). 
Moderate- and low-frequency customers also differed significantly (p = .003).
```

#### Correlation

```r
# Correlation analysis

cor_result <- cor.test(data$satisfaction, data$usage, method = "pearson")

# Multiple correlations
cor_matrix <- cor(data[, c("sat", "usage", "age", "tenure")])
library(psych)
corr.test(data[, c("sat", "usage", "age", "tenure")])

# Report
## Correlational Analysis

Satisfaction was positively correlated with usage frequency, r(325) = .47, 
p < .001, 95% CI [.38, .55]. Approximately 22% of variance in satisfaction 
was shared with usage frequency (r² = .22). Table 2 presents the complete 
correlation matrix. All correlations were in the expected directions, 
with satisfaction positively associated with usage (r = .47), customer 
tenure (r = .31), and age (r = .18, all ps < .001).
```

#### Multiple Regression

```r
# Hierarchical regression

# Block 1: Controls
model1 <- lm(satisfaction ~ age + gender + tenure, data = data)

# Block 2: Add predictors of interest
model2 <- lm(satisfaction ~ age + gender + tenure + 
               usage_freq + product_quality, data = data)

# Compare models
anova(model1, model2)

# Summary statistics
summary(model2)
library(sjPlot)
tab_model(model1, model2, show.std = TRUE)

# Report
## Multiple Regression

Table 3 presents hierarchical regression results predicting customer 
satisfaction. Block 1 included demographic controls (age, gender, tenure), 
accounting for 12% of variance, F(3, 321) = 14.62, p < .001. Block 2 
added usage frequency and product quality perceptions, significantly 
improving model fit, ΔR² = .31, ΔF(2, 319) = 78.45, p < .001. 

In the final model (R² = .43, adjusted R² = .42), F(5, 319) = 48.67, 
p < .001, both usage frequency (β = .34, p < .001) and product quality 
(β = .48, p < .001) uniquely predicted satisfaction after controlling 
for demographics. Tenure remained significant (β = .15, p = .002), while 
age and gender were non-significant (ps > .15). These five predictors 
collectively explained 43% of satisfaction variance.
```

### 5. Machine Learning Models

#### Classification Models

```r
# Logistic regression for binary outcome

# Train-test split
library(caret)
set.seed(123)
train_index <- createDataPartition(data$churned, p = 0.70, list = FALSE)
train_data <- data[train_index, ]
test_data <- data[-train_index, ]

# Fit logistic regression
log_model <- glm(churned ~ age + tenure + satisfaction + usage_freq + 
                   total_spend, data = train_data, family = binomial)

# Predictions
predicted_probs <- predict(log_model, test_data, type = "response")
predicted_class <- ifelse(predicted_probs > 0.5, 1, 0)

# Evaluation metrics
library(pROC)
roc_obj <- roc(test_data$churned, predicted_probs)
auc_value <- auc(roc_obj)

confusionMatrix(factor(predicted_class), factor(test_data$churned))

# Report
## Predictive Modeling

**Logistic Regression**. We developed a logistic regression model to 
predict customer churn using five predictors: age, account tenure, 
satisfaction, usage frequency, and total spend. The model was trained 
on 70% of data (n = 23,276) and evaluated on a held-out test set (30%, 
n = 9,976).

Results indicated that all predictors except age were significant 
(Table 4). Lower satisfaction (OR = 0.42, 95% CI [0.38, 0.47]), shorter 
tenure (OR = 0.88, 95% CI [0.85, 0.91]), lower usage frequency (OR = 0.65, 
95% CI [0.61, 0.70]), and lower total spend (OR = 0.91, 95% CI [0.88, 0.94]) 
were associated with increased churn likelihood.

**Model Performance**. On the test set, the model achieved an AUC of .82 
(95% CI [.81, .84]), indicating good discriminative ability. Using a 
probability threshold of 0.5, the model correctly classified 76% of cases, 
with sensitivity = .71 (correctly identified 71% of churners) and 
specificity = .79 (correctly identified 79% of non-churners). The positive 
predictive value was .68, indicating that 68% of customers predicted to 
churn actually did.
```

#### Comparing Multiple Models

```r
# Compare algorithms

library(caret)

# Set up cross-validation
train_control <- trainControl(method = "cv", number = 10, 
                               classProbs = TRUE, 
                               summaryFunction = twoClassSummary)

# Train multiple models
set.seed(123)
models <- list(
  logistic = train(churned ~ ., data = train_data, method = "glm", 
                   family = "binomial", trControl = train_control, 
                   metric = "ROC"),
  
  rf = train(churned ~ ., data = train_data, method = "rf", 
             trControl = train_control, metric = "ROC"),
  
  xgboost = train(churned ~ ., data = train_data, method = "xgbTree", 
                  trControl = train_control, metric = "ROC")
)

# Compare performance
results <- resamples(models)
summary(results)

# Report
## Model Comparison

We compared three classification algorithms: logistic regression (baseline), 
random forest, and gradient boosting (XGBoost). Table 5 presents 
10-fold cross-validation results on the training set. XGBoost achieved 
the highest AUC (M = .85, SD = .02), followed by random forest (M = .84, 
SD = .02) and logistic regression (M = .82, SD = .02). 

Pairwise comparisons indicated XGBoost significantly outperformed logistic 
regression (p < .001) but did not significantly differ from random forest 
(p = .18). Given comparable performance and greater interpretability, we 
selected XGBoost as the final model.

**Test Set Evaluation**. On the held-out test set, the XGBoost model 
achieved AUC = .86 (95% CI [.84, .87]), accuracy = 78%, sensitivity = .74, 
and specificity = .81, outperforming the baseline logistic regression 
by 4 percentage points in AUC.
```

### 6. Effect Sizes

Always report effect sizes alongside p-values:

| Test | Effect Size | Interpretation (Cohen, 1988) |
|------|-------------|------------------------------|
| t-test | Cohen's d | Small: 0.2, Medium: 0.5, Large: 0.8 |
| ANOVA | η² or ω² | Small: .01, Medium: .06, Large: .14 |
| Correlation | r | Small: .10, Medium: .30, Large: .50 |
| Regression | R² or ΔR² | Small: .02, Medium: .13, Large: .26 |
| Chi-square | Cramér's V | Small: .10, Medium: .30, Large: .50 |
| Odds Ratio | OR | 1.5 (small), 3.5 (medium), 9 (large) |

```r
# Calculate effect sizes

library(effectsize)

# For t-test
cohens_d(satisfaction ~ group, data = data)

# For ANOVA
eta_squared(aov_model, partial = TRUE)

# For regression
r2(lm_model)

# For logistic regression
oddsratio(glm_model)

# For correlation - r itself is the effect size
```

### 7. APA Reporting Guidelines

#### Statistical Reporting Format

**General template**:
*Test statistic*(df) = value, *p* = exact value, effect size = value

**Examples**:

- **t-test**: *t*(324) = 4.52, *p* < .001, *d* = 0.87
- **ANOVA**: *F*(2, 321) = 18.45, *p* < .001, η² = .10
- **Correlation**: *r*(325) = .47, *p* < .001
- **Chi-square**: χ²(2, *N* = 327) = 14.23, *p* < .001, *V* = .21
- **Regression**: *b* = 0.34, SE = 0.07, β = .28, *t*(319) = 4.86, *p* < .001

**p-value reporting**:
- Exact values when *p* ≥ .001: *p* = .037
- For very small: *p* < .001 (not *p* = .000)
- Never write *p* = ns or *p* > .05

**Confidence intervals**:
- Always include for primary results
- 95% CI [lower, upper]
- Example: *d* = 0.87, 95% CI [0.52, 1.22]

## Practical Exercise

### Exercise 1: Analysis Plan

Create a detailed analysis plan for your capstone:

```markdown
## Data Analysis Plan

### Preliminary Analyses
1. Descriptive statistics for all variables
2. Missing data analysis
3. Assumption checking for planned tests

### Primary Analyses
**RQ1**: [State research question]
- **Test**: [e.g., Independent t-test]
- **Variables**: IV = [X], DV = [Y]
- **Effect size**: Cohen's d
- **Assumptions**: Normality, homogeneity of variance

**RQ2**: [State research question]
- **Test**: [e.g., Multiple regression]
- **Variables**: DV = [Y], IVs = [X1, X2, X3]
- **Effect size**: R², ΔR²
- **Assumptions**: Linearity, multicollinearity, normality of residuals

### Sensitivity Analyses
- Outlier exclusion analysis
- Alternative missing data handling
- Robustness checks

### Software
All analyses conducted in R version 4.5.2 using packages: tidyverse, 
psych, car, effsize, caret.
```

### Exercise 2: Report Results

Analyze a subset of your data and write a complete results paragraph:

- State the research question
- Report the statistical test
- Include descriptive statistics
- Report test statistic, df, p-value
- Include effect size and CI
- Interpret the finding

### Exercise 3: Create Results Tables

Generate APA-formatted tables:

**Table 1**: Descriptive statistics and correlations
**Table 2**: Regression results (if applicable)
**Table 3**: Model comparison (if applicable)

```r
# Use these packages
library(apaTables)
library(sjPlot)
library(gtsummary)
```

## Self-Check Questions

1. When should you use Welch's t-test instead of Student's t-test?
2. What's the difference between R² and adjusted R²?
3. How do you interpret an odds ratio of 2.5?
4. What effect size should you report for ANOVA?
5. When is it appropriate to report *p* < .001 vs. exact p-values?

## Common Analysis Mistakes

❌ **Only reporting p-values**: Always include effect sizes

❌ **Ignoring assumptions**: Check and report violations

❌ **Data dredging**: Don't run dozens of tests and only report significant ones

❌ **Wrong test selection**: Match test to research question and data types

❌ **Confusing significance and importance**: *p* < .05 ≠ meaningful effect

## Next Week

**Week 7: Results Section** - Learn to write comprehensive, objective Results sections with integrated tables and figures.

---

*Week 6 of 14 | ANLY699 Research Writing Tutorial*
