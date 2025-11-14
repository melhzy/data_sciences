# Week 7: Results Section

## Overview

The Results section objectively presents your findings without interpretation. This week focuses on writing clear, comprehensive Results sections that integrate statistical findings with tables and figures.

## Learning Objectives

By the end of this week, you will be able to:
1. Structure Results sections logically
2. Report statistical findings following APA 7 guidelines
3. Integrate tables and figures effectively
4. Distinguish between results and interpretation
5. Use appropriate language and tense
6. Present complex findings clearly

## Required Reading

📄 **Sample Papers** - Study Results sections in:
- `../SamplePapers/Net Photosynthetic Rate.pdf`
- `../SamplePapers/English Language Proficiency.pdf`
- `../SamplePapers/The Urinary Microbiome.pdf`

## Tutorial Content

### 1. Results Section Structure

#### Standard Organization

```markdown
# Results

## Preliminary Analyses
- Sample characteristics
- Data screening
- Assumption checks
- Descriptive statistics

## Primary Analyses
- RQ1/H1 results
- RQ2/H2 results
- RQ3/H3 results

## Supplementary Analyses (if applicable)
- Post-hoc tests
- Sensitivity analyses
- Exploratory findings
```

#### Opening Paragraph Template

```markdown
# Results

## Sample Characteristics

The final analytical sample consisted of N = 678 customers (52% female, 
48% male) with ages ranging from 22 to 67 years (M = 38.4, SD = 11.2). 
On average, customers had been active for 18.7 months (SD = 9.3, range = 
12-48 months). Table 1 presents complete descriptive statistics and 
correlations for all study variables.

Prior to hypothesis testing, we examined data for outliers, normality, 
and missing data patterns (see Method section). All assumptions for 
planned analyses were satisfactorily met or addressed through appropriate 
corrections.
```

### 2. Reporting Statistical Results

#### Basic Formats

**Descriptive Statistics**:

```markdown
Customer satisfaction scores averaged 3.47 (SD = 0.89) on a 5-point scale, 
indicating moderate satisfaction. Usage frequency showed considerable 
variability (M = 8.2 times/month, SD = 6.7, range = 1-28), with a 
positively skewed distribution (skew = 1.12, SE = 0.09).
```

**t-test**:

```markdown
High-usage customers (M = 4.12, SD = 0.67) reported significantly higher 
satisfaction than low-usage customers (M = 3.21, SD = 0.91), t(298) = 9.34, 
p < .001, 95% CI [0.73, 1.09], d = 1.14. This large effect indicates 
substantial practical difference between groups.
```

**ANOVA**:

```markdown
One-way ANOVA revealed significant satisfaction differences across 
customer segments, F(2, 675) = 27.84, p < .001, η² = .08. Bonferroni-
corrected post-hoc tests (see Table 2) indicated that premium customers 
(M = 4.23, SD = 0.61) reported higher satisfaction than both standard 
(M = 3.67, SD = 0.78, p < .001) and basic customers (M = 3.12, SD = 0.94, 
p < .001). Standard and basic customers also differed significantly 
(p = .002).
```

**Correlation**:

```markdown
Consistent with H1, satisfaction was positively correlated with usage 
frequency, r(676) = .47, p < .001, 95% CI [.41, .53], explaining 22% of 
shared variance. Table 1 presents the complete correlation matrix. 
Notably, tenure showed moderate positive associations with both 
satisfaction (r = .31) and usage (r = .28), all ps < .001.
```

**Regression**:

```markdown
Table 3 presents hierarchical regression results. In the final model, 
five predictors explained 43% of satisfaction variance, F(5, 672) = 101.34, 
p < .001, adjusted R² = .42. Controlling for demographics, both usage 
frequency (β = .34, p < .001) and product quality (β = .48, p < .001) 
emerged as significant predictors. Each standard deviation increase in 
usage frequency was associated with a 0.34 standard deviation increase 
in satisfaction, holding other variables constant.
```

**Non-Significant Results**:

```markdown
Contrary to H3, customer age did not significantly predict satisfaction 
after controlling for other variables, β = .05, t(672) = 1.43, p = .15, 
95% CI [-0.02, 0.12]. This null finding suggests age-related differences 
in satisfaction may be confounded with tenure and usage patterns.
```

### 3. Writing About Tables and Figures

#### Referencing Rules

- **First mention**: "Table 1 presents..."
- **Subsequent mentions**: "As shown in Table 1..." or "(see Table 1)"
- **Never write**: "The table below shows..." (tables may move in publication)

#### Integration Examples

**Pointing to tables**:

```markdown
Descriptive statistics and bivariate correlations appear in Table 1. 
Satisfaction positively correlated with usage frequency (r = .47), 
tenure (r = .31), and total spend (r = .24), all ps < .001.

[Insert Table 1]

As shown in Table 1, the strongest predictor of satisfaction was product 
quality perception (r = .63), followed by customer service responsiveness 
(r = .51).
```

**Pointing to figures**:

```markdown
Figure 1 illustrates the relationship between usage frequency and 
satisfaction across three customer segments. The positive association 
was strongest for premium customers (r = .52) compared to standard 
(r = .41) or basic customers (r = .33), suggesting segment moderation.

[Insert Figure 1]

Visual inspection of Figure 1 reveals the non-linear pattern in the 
basic customer segment, where satisfaction plateaus beyond 15 uses/month.
```

### 4. Hypothesis Testing Results

#### Clear Hypothesis Statements

```markdown
## Primary Hypotheses

**H1: Usage frequency positively predicts customer satisfaction**. 
Supporting H1, higher usage frequency significantly predicted greater 
satisfaction, β = .34, t(672) = 8.92, p < .001, 95% CI [0.26, 0.42]. 
In practical terms, customers who used the platform 10+ times monthly 
(high-usage group) showed 26% higher satisfaction scores compared to 
those with <5 monthly uses (low-usage group).

**H2: The usage-satisfaction relationship is moderated by customer 
segment**. To test H2, we added the usage × segment interaction term 
in Step 3 of the regression model (Table 3). The interaction was 
significant, ΔR² = .03, F(2, 670) = 14.67, p < .001, supporting H2. 
Simple slopes analysis (Figure 2) revealed that usage more strongly 
predicted satisfaction for premium (b = 0.08, SE = 0.01, p < .001) 
compared to basic customers (b = 0.03, SE = 0.01, p = .02).

**H3: Product quality mediates the usage-satisfaction relationship**. 
We tested H3 using Hayes' (2018) PROCESS macro (Model 4). Results 
(Figure 3) indicated significant indirect effects: usage predicted 
product quality (a = 0.42, SE = 0.05, p < .001), which in turn predicted 
satisfaction (b = 0.51, SE = 0.04, p < .001). The indirect effect was 
significant, ab = 0.21, 95% CI [0.15, 0.28], supporting mediation. The 
direct effect of usage on satisfaction remained significant (c' = 0.13, 
p = .001), suggesting partial mediation.
```

### 5. Complex Analyses

#### Machine Learning Results

```markdown
## Predictive Modeling

**Model Development**. We compared four classification algorithms to 
predict customer churn: logistic regression (baseline), decision tree, 
random forest, and gradient boosting (XGBoost). Models were trained on 
70% of data (n = 33,237) using 10-fold cross-validation, with 
hyperparameter tuning via grid search. Final models were evaluated on 
the held-out test set (30%, n = 14,244).

**Model Comparison**. Table 4 presents cross-validation performance 
metrics. XGBoost achieved the highest AUC (M = .85, SD = .02), followed 
by random forest (M = .83, SD = .02), decision tree (M = .74, SD = .03), 
and logistic regression (M = .81, SD = .02). Pairwise t-tests indicated 
XGBoost significantly outperformed all other models (all ps < .001), 
except random forest (p = .09).

**Test Set Performance**. On the test set, XGBoost achieved AUC = .86 
(95% CI [.85, .88]), accuracy = 78.4%, sensitivity = 73.8%, specificity = 
80.6%, and F1-score = .71 (Table 5). Compared to the baseline logistic 
regression (AUC = .81), XGBoost improved predictive accuracy by 5 
percentage points. Figure 4 presents the ROC curves for all models.

**Feature Importance**. SHAP (SHapley Additive exPlanations) analysis 
identified the most influential predictors (Figure 5). Usage frequency 
emerged as the strongest predictor (SHAP value = 0.34), followed by 
satisfaction (0.29), tenure (0.21), total spend (0.18), and support 
tickets (0.16). Customer age and gender contributed minimally (SHAP < 0.05).
```

#### Longitudinal/Repeated Measures

```markdown
## Growth Curve Analysis

We used multilevel modeling (MLM) to examine satisfaction trajectories 
over 12 months. Level 1 modeled within-person change (time), while 
Level 2 modeled between-person differences (customer segment).

**Unconditional Model**. The intraclass correlation (ICC = .42) indicated 
that 42% of satisfaction variance was between-persons, justifying MLM. 
Significant variance existed in both intercepts (τ₀₀ = 0.31, p < .001) 
and slopes (τ₁₁ = 0.04, p = .002), suggesting individual differences in 
baseline satisfaction and change rates.

**Conditional Model**. Adding customer segment (Table 6) significantly 
improved fit, χ²(4) = 87.23, p < .001. Premium customers showed higher 
initial satisfaction (γ₀₀ = 4.21, SE = 0.08, p < .001) and steeper 
positive slopes (γ₁₀ = 0.06, SE = 0.01, p < .001) compared to basic 
customers (intercept γ₀₂ = 3.45, slope γ₁₂ = 0.01). Figure 6 plots 
predicted trajectories by segment.
```

### 6. Reporting Non-Significant Results

Always report planned analyses, even if non-significant:

```markdown
**No Support for H4**. Contrary to predictions, customer age did not 
moderate the usage-satisfaction relationship. The age × usage interaction 
was non-significant, β = -.03, t(670) = -0.78, p = .44, 95% CI [-0.11, 0.05], 
ΔR² < .001. Satisfaction patterns were similar across age groups.

**Exploratory Analysis**. Post-hoc, we examined whether the null finding 
might reflect restricted age range (89% of sample aged 25-50). Splitting 
at the median (age 38) yielded no significant differences in the usage-
satisfaction slope, younger: b = 0.34, older: b = 0.36, difference 
p = .72. Thus, age appears genuinely unrelated to this relationship in 
our sample.
```

### 7. Ordering Results

#### Logical Flow Options

**Option 1: Research Question Order**
- Present results matching question sequence from Introduction
- Most common and reader-friendly

**Option 2: Analysis Complexity**
- Start simple (descriptives, bivariate)
- Progress to complex (regression, moderation)

**Option 3: Thematic**
- Group related findings
- E.g., "Usage Patterns" then "Satisfaction Predictors"

**Recommendation**: Follow your research questions but start with:

```markdown
# Results

## Preliminary Analyses
[Descriptives, assumptions, data screening]

## Descriptive Statistics and Bivariate Associations
[Means, SDs, correlations - provides context]

## Research Question 1
[First RQ results]

## Research Question 2
[Second RQ results]
...

## Supplementary Analyses
[Post-hoc, sensitivity, exploratory]
```

### 8. Language and Style

#### Objective Tone

✅ **Objective**: Results indicated significantly higher satisfaction...
❌ **Subjective**: Results proved our theory correct...

✅ **Objective**: The model achieved 78% accuracy...
❌ **Interpretive**: The model performed excellently...

✅ **Objective**: Usage frequency explained 22% of variance...
❌ **Causal (unless experimental)**: Usage frequency caused satisfaction to increase...

#### Past Tense

Use past tense throughout Results:

- "Customers **reported** higher satisfaction"
- "The model **achieved** 78% accuracy"
- "Assumptions **were** satisfactorily met"
- "Results **indicated** significant differences"

#### Avoid Redundancy

❌ "The results showed that there was a significant difference"
✅ "Results revealed significant differences"

❌ "As can be seen in Table 1, the correlation was..."
✅ "Table 1 shows the correlation was..."

## Practical Exercise

### Exercise 1: Write Results Sections

For each analysis type, write a complete results paragraph:

1. **Descriptive results**: Describe your sample and key variables
2. **Primary analysis**: Report your main statistical test
3. **Secondary analysis**: Report a follow-up or exploratory test
4. **Table reference**: Integrate at least one table
5. **Figure reference**: Integrate at least one figure

### Exercise 2: Convert SPSS/R Output to APA Text

Given these results, write APA-formatted text:

```
t-test output:
t = 3.47, df = 198, p = .0006
Group 1: M = 3.82, SD = 0.92, n = 100
Group 2: M = 3.21, SD = 1.04, n = 100
Cohen's d = 0.62
```

<details>
<summary>Answer</summary>

Group 1 participants (M = 3.82, SD = 0.92) reported significantly higher 
scores than Group 2 participants (M = 3.21, SD = 1.04), t(198) = 3.47, 
p < .001, d = 0.62. This medium-to-large effect suggests meaningful 
differences between groups.
</details>

### Exercise 3: Results Section Outline

Create a complete outline for your capstone Results section:

```markdown
# Results [outline]

## Opening paragraph
- Final sample size and characteristics
- Reference to Table 1 (descriptives/correlations)

## Preliminary Analyses
- Data screening outcomes
- Assumption check summary

## RQ1: [State question]
- Statistical test used
- Key findings
- Reference to Table X or Figure Y
- Effect size and interpretation

## RQ2: [State question]
- [Same structure]

## Supplementary Analyses
- Post-hoc tests
- Sensitivity checks
- Exploratory findings

## Closing statement
- Brief summary linking to Discussion
```

## Self-Check Questions

1. What tense should you use in the Results section?
2. Should you interpret findings in Results?
3. How should you report a non-significant finding?
4. What goes in preliminary analyses?
5. How should you reference tables and figures?

## Results Section Checklist

Before moving to Week 8, ensure your Results include:

- [ ] Opening paragraph with sample description
- [ ] Preliminary analyses (screening, assumptions)
- [ ] Results for ALL planned analyses (even non-significant)
- [ ] Descriptive statistics (M, SD) for key variables
- [ ] Test statistics with df, p-values, and effect sizes
- [ ] 95% confidence intervals for key effects
- [ ] References to all tables and figures
- [ ] Past tense throughout
- [ ] Objective tone (no interpretation)
- [ ] Clear organization (matches research questions)
- [ ] Appropriate precision (usually 2 decimal places)

## Next Week

**Week 8: Discussion Section** - Learn to interpret your findings, connect to literature, address limitations, and draw meaningful conclusions.

---

*Week 7 of 14 | ANLY699 Research Writing Tutorial*
