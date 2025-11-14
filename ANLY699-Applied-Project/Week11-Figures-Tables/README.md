# Week 11: Figures & Tables

## Overview

Effective figures and tables communicate complex data clearly and support your narrative. This week covers creating APA-compliant visualizations and tables using R, with emphasis on publication-quality graphics.

## Learning Objectives

By the end of this week, you will be able to:
1. Create APA-compliant tables with proper formatting
2. Design effective data visualizations following best practices
3. Write clear figure and table captions
4. Integrate graphics into R Markdown workflows
5. Export publication-ready figures
6. Decide when to use figures vs. tables

## Required Reading

📄 **Sample Papers** - Examine all figures and tables in:
- `../SamplePapers/Net Photosynthetic Rate.pdf`
- `../SamplePapers/Unveiling the Genetic Networks.pdf`
- `../SamplePapers/The Urinary Microbiome.pdf`

## Tutorial Content

### 1. Tables vs. Figures: When to Use Each

#### Use **Tables** when:
- Exact values matter
- Showing multiple related datasets
- Presenting statistical test results
- Comparing groups on multiple variables
- Readers need to look up specific numbers

#### Use **Figures** when:
- Patterns and trends are key
- Relationships between variables
- Distributions need visualization
- Spatial or temporal patterns
- Visual impact enhances understanding

| Purpose | Table | Figure |
|---------|-------|--------|
| Show exact values | ✅ | ❌ |
| Show trends | ❌ | ✅ |
| Compare groups | ✅ | ✅ |
| Show distributions | ❌ | ✅ |
| Show correlations | ✅ | ✅ |
| Statistical results | ✅ | ❌ |
| Model performance | ✅ | ✅ |

### 2. APA Table Formatting

#### General Rules

- **Numbering**: Sequential (Table 1, Table 2, ...)
- **Title**: Above table, italicized, Title Case for first part
- **Lines**: Horizontal lines only (top, bottom, under headers)
- **Font**: Consistent with text (12pt)
- **Notes**: Below table (general, specific, probability)
- **Decimal alignment**: Align on decimal points

#### Table Components

```
Table 1
Descriptive Statistics and Correlations for Study Variables

Variable         M     SD    1     2     3     4
─────────────────────────────────────────────────
1. Satisfaction  3.47  0.89  —
2. Usage Freq.   8.23  6.71  .47** —
3. Tenure        18.7  9.32  .31** .28** —
4. Age           38.4  11.2  .18** .09   .24** —
─────────────────────────────────────────────────

Note. N = 678. Usage Freq. = monthly platform uses.
*p < .05. **p < .001.
```

#### Creating Tables in R

**Using kable and kableExtra**:

```r
library(dplyr)
library(knitr)
library(kableExtra)

# Descriptive statistics table
descriptives <- data %>%
  select(satisfaction, usage_freq, tenure, age) %>%
  summarise(
    across(everything(), 
           list(M = ~mean(., na.rm = TRUE),
                SD = ~sd(., na.rm = TRUE),
                Min = ~min(., na.rm = TRUE),
                Max = ~max(., na.rm = TRUE)),
           .names = "{.col}_{.fn}")
  ) %>%
  pivot_longer(everything()) %>%
  separate(name, into = c("Variable", "Statistic"), sep = "_") %>%
  pivot_wider(names_from = Statistic, values_from = value)

descriptives %>%
  kable(digits = 2,
        caption = "Descriptive Statistics for Study Variables",
        col.names = c("Variable", "M", "SD", "Min", "Max")) %>%
  kable_styling(bootstrap_options = c("striped", "hover"),
                full_width = FALSE,
                position = "left") %>%
  add_footnote(c("N = 678", "All measures on 5-point scales"),
               notation = "none")
```

**Correlation Matrix**:

```r
# Create correlation matrix with significance stars
library(psych)
library(apaTables)

# Simple approach
apa.cor.table(data[, c("satisfaction", "usage_freq", "tenure", "age")],
              filename = "table1_correlations.doc",
              table.number = 1)

# Manual with kable
cor_matrix <- cor(data[, c("satisfaction", "usage_freq", "tenure", "age")], 
                  use = "pairwise.complete.obs")
cor_p <- corr.test(data[, c("satisfaction", "usage_freq", "tenure", "age")])$p

# Format with significance stars
cor_formatted <- ifelse(cor_p < .001, 
                        paste0(round(cor_matrix, 2), "**"),
                        ifelse(cor_p < .05,
                               paste0(round(cor_matrix, 2), "*"),
                               round(cor_matrix, 2)))

cor_formatted[upper.tri(cor_formatted)] <- ""
diag(cor_formatted) <- "—"

cor_table <- as.data.frame(cor_formatted)
rownames(cor_table) <- paste0(1:ncol(cor_matrix), ". ", colnames(cor_matrix))
colnames(cor_table) <- 1:ncol(cor_matrix)

kable(cor_table,
      caption = "Correlations Among Study Variables",
      align = "c") %>%
  kable_styling(full_width = FALSE) %>%
  add_footnote(c("N = 678", "*p < .05. **p < .001"),
               notation = "none")
```

**Regression Results**:

```r
library(sjPlot)
library(sjmisc)
library(sjlabelled)

# Hierarchical regression models
model1 <- lm(satisfaction ~ age + gender + tenure, data = data)
model2 <- lm(satisfaction ~ age + gender + tenure + usage_freq + quality, 
             data = data)

# APA-style regression table
tab_model(model1, model2,
          show.std = TRUE,
          show.ci = FALSE,
          show.se = TRUE,
          show.stat = TRUE,
          show.p = TRUE,
          dv.labels = c("Model 1", "Model 2"),
          pred.labels = c("(Intercept)", "Age", "Gender [Male]", "Tenure",
                          "Usage Frequency", "Product Quality"),
          string.pred = "Predictor",
          string.est = "B",
          string.se = "SE",
          string.stat = "t",
          string.p = "p",
          title = "Hierarchical Regression Predicting Customer Satisfaction",
          file = "table_regression.html")
```

**Group Comparisons**:

```r
# ANOVA summary table
library(gtsummary)

data %>%
  select(segment, satisfaction, usage_freq, age) %>%
  tbl_summary(
    by = segment,
    statistic = list(all_continuous() ~ "{mean} ({sd})",
                     all_categorical() ~ "{n} ({p}%)"),
    digits = all_continuous() ~ 2,
    label = list(satisfaction ~ "Satisfaction",
                 usage_freq ~ "Usage Frequency",
                 age ~ "Age")
  ) %>%
  add_p(test = list(all_continuous() ~ "aov",
                    all_categorical() ~ "chisq.test")) %>%
  add_overall() %>%
  modify_header(label ~ "**Variable**") %>%
  modify_caption("Descriptive Statistics by Customer Segment") %>%
  bold_labels() %>%
  as_kable_extra() %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```

### 3. APA Figure Formatting

#### General Rules

- **Numbering**: Sequential (Figure 1, Figure 2, ...)
- **Caption**: Below figure, Title Case for first part
- **Size**: Readable when reduced (minimum 8pt font in final)
- **Format**: Vector (PDF, SVG) preferred over raster (PNG, JPG)
- **Resolution**: ≥300 DPI if raster
- **Color**: Grayscale friendly (use patterns, shapes)
- **Legend**: Clear and positioned appropriately
- **Axes**: Labeled with units

#### Figure Components

```
[Figure image here]

Figure 1. Customer satisfaction scores by usage frequency and customer 
segment. Error bars represent 95% confidence intervals. Premium customers 
(circles) show steeper satisfaction-usage slopes compared to basic customers 
(triangles).
```

#### Creating Figures in R

**Bar Charts**:

```r
library(ggplot2)
library(ggthemes)

# Grouped bar chart
ggplot(data_summary, aes(x = segment, y = mean_satisfaction, fill = usage_category)) +
  geom_col(position = "dodge", color = "black") +
  geom_errorbar(aes(ymin = mean_satisfaction - se, 
                    ymax = mean_satisfaction + se),
                position = position_dodge(0.9), width = 0.2) +
  scale_fill_grey(start = 0.3, end = 0.9) +
  scale_y_continuous(limits = c(0, 5), expand = c(0, 0)) +
  labs(x = "Customer Segment",
       y = "Customer Satisfaction",
       fill = "Usage Category") +
  theme_apa() +
  theme(legend.position = "right",
        panel.grid.major.y = element_line(color = "gray90"),
        axis.line = element_line(color = "black"))

ggsave("figure1_barplot.pdf", width = 6, height = 4, dpi = 300)
```

**Scatterplots**:

```r
# Scatterplot with regression lines by group
ggplot(data, aes(x = usage_freq, y = satisfaction, shape = segment)) +
  geom_point(alpha = 0.6, size = 2) +
  geom_smooth(method = "lm", se = TRUE, color = "black", 
              aes(linetype = segment)) +
  scale_shape_manual(values = c(16, 17, 15),
                     labels = c("Basic", "Standard", "Premium")) +
  scale_linetype_manual(values = c("dotted", "dashed", "solid"),
                        labels = c("Basic", "Standard", "Premium")) +
  labs(x = "Usage Frequency (uses per month)",
       y = "Customer Satisfaction (1-5 scale)",
       shape = "Segment",
       linetype = "Segment") +
  theme_apa() +
  theme(legend.position = c(0.85, 0.15),
        legend.background = element_rect(fill = "white", color = "black"))

ggsave("figure2_scatterplot.pdf", width = 6, height = 4.5, dpi = 300)
```

**Box Plots**:

```r
# Box plot with individual points
ggplot(data, aes(x = segment, y = satisfaction)) +
  geom_boxplot(outlier.shape = NA, fill = "gray80") +
  geom_jitter(alpha = 0.2, width = 0.2, size = 1) +
  stat_summary(fun = mean, geom = "point", shape = 18, size = 4, 
               color = "red") +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  labs(x = "Customer Segment",
       y = "Customer Satisfaction") +
  theme_apa()

ggsave("figure3_boxplot.pdf", width = 5, height = 4, dpi = 300)
```

**Line Graphs**:

```r
# Interaction plot
ggplot(interaction_data, aes(x = usage_freq, y = predicted_satisfaction, 
                              linetype = segment)) +
  geom_line(size = 1) +
  geom_ribbon(aes(ymin = lower_ci, ymax = upper_ci, fill = segment),
              alpha = 0.2) +
  scale_linetype_manual(values = c("solid", "dashed", "dotted")) +
  scale_fill_grey(start = 0.3, end = 0.8) +
  labs(x = "Usage Frequency (uses per month)",
       y = "Predicted Satisfaction",
       linetype = "Segment",
       fill = "Segment") +
  theme_apa() +
  theme(legend.position = "right")

ggsave("figure4_interaction.pdf", width = 6, height = 4, dpi = 300)
```

**ROC Curves**:

```r
library(pROC)
library(ggplot2)

# Plot multiple ROC curves
roc_log <- roc(test_data$churned, pred_log)
roc_rf <- roc(test_data$churned, pred_rf)
roc_xgb <- roc(test_data$churned, pred_xgb)

roc_data <- data.frame(
  specificity = c(roc_log$specificities, roc_rf$specificities, 
                  roc_xgb$specificities),
  sensitivity = c(roc_log$sensitivities, roc_rf$sensitivities, 
                  roc_xgb$sensitivities),
  model = rep(c("Logistic Regression", "Random Forest", "XGBoost"),
              times = c(length(roc_log$specificities),
                       length(roc_rf$specificities),
                       length(roc_xgb$specificities)))
)

ggplot(roc_data, aes(x = 1 - specificity, y = sensitivity, 
                     linetype = model)) +
  geom_line(size = 1) +
  geom_abline(intercept = 0, slope = 1, linetype = "dashed", 
              color = "gray50") +
  scale_linetype_manual(values = c("solid", "dashed", "dotted")) +
  labs(x = "1 - Specificity (False Positive Rate)",
       y = "Sensitivity (True Positive Rate)",
       linetype = "Model") +
  annotate("text", x = 0.6, y = 0.3, 
           label = paste0("AUC: LR = ", round(auc(roc_log), 3),
                         "\nRF = ", round(auc(roc_rf), 3),
                         "\nXGB = ", round(auc(roc_xgb), 3)),
           hjust = 0) +
  theme_apa() +
  theme(legend.position = c(0.7, 0.2))

ggsave("figure5_roc.pdf", width = 5, height = 5, dpi = 300)
```

**Feature Importance**:

```r
# SHAP values or feature importance
library(xgboost)
library(ggplot2)

importance_data <- xgb.importance(model = xgb_model) %>%
  slice_head(n = 10) %>%
  mutate(Feature = forcats::fct_reorder(Feature, Gain))

ggplot(importance_data, aes(x = Gain, y = Feature)) +
  geom_col(fill = "gray60", color = "black") +
  labs(x = "Feature Importance (Gain)",
       y = NULL) +
  theme_apa() +
  theme(panel.grid.major.x = element_line(color = "gray90"))

ggsave("figure6_importance.pdf", width = 6, height = 4, dpi = 300)
```

### 4. Figure and Table Captions

#### Caption Structure

**Figures**:
```
Figure [#]. [Brief title]. [Additional details needed to understand the 
figure]. [Explanation of symbols, abbreviations, or error bars].
```

Examples:

```
Figure 1. Customer satisfaction by usage frequency and segment. Points 
represent individual customers. Lines show linear regression fits with 
95% confidence bands (shaded regions). Premium customers (circles, solid 
line) show steeper slopes than basic customers (triangles, dotted line).

Figure 2. ROC curves comparing churn prediction models. Diagonal dashed 
line represents chance performance (AUC = 0.50). XGBoost (solid line) 
achieved the highest AUC (.86), followed by Random Forest (.83, dashed) 
and Logistic Regression (.81, dotted).

Figure 3. Feature importance for churn prediction model. Bars represent 
SHAP (SHapley Additive exPlanations) values indicating each feature's 
contribution to model predictions. Higher values indicate greater 
importance.
```

**Tables**:
```
Table [#]
[Brief Title]
```

Note section (below table):
```
Note. [General notes about table]. [Specific notes about particular 
entries]. [Probability notes for significance levels].
```

Examples:

```
Table 1
Hierarchical Regression Predicting Customer Satisfaction

[Table content here]

Note. N = 678. Model 1: R² = .12, F(3, 674) = 30.45, p < .001. Model 2: 
R² = .43, F(5, 672) = 101.34, p < .001. ΔR² = .31, ΔF(2, 672) = 145.67, 
p < .001. Standardized coefficients (β) shown.
*p < .05. **p < .01. ***p < .001.

Table 3
Model Performance Comparison on Test Set

[Table content here]

Note. N_test = 14,244. AUC = Area Under the ROC Curve. CI = 95% confidence 
interval calculated via 1,000 bootstrap resamples. All pairwise comparisons 
significant at p < .001 except RF vs. XGBoost (p = .09).
```

### 5. APA Theme for ggplot2

Create a reusable theme:

```r
# APA theme function
theme_apa <- function(base_size = 12, base_family = "sans") {
  theme_bw(base_size = base_size, base_family = base_family) +
    theme(
      # Remove gray background
      panel.background = element_blank(),
      panel.border = element_blank(),
      
      # Axis lines
      axis.line = element_line(color = "black", size = 0.5),
      
      # Grid lines
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      
      # Axis text
      axis.text = element_text(color = "black", size = base_size * 0.9),
      axis.title = element_text(color = "black", size = base_size, 
                                face = "plain"),
      
      # Legend
      legend.background = element_blank(),
      legend.key = element_blank(),
      legend.title = element_text(size = base_size, face = "plain"),
      legend.text = element_text(size = base_size * 0.9),
      
      # Plot title (if used)
      plot.title = element_text(size = base_size * 1.1, face = "plain", 
                                hjust = 0.5),
      
      # Strip text (for facets)
      strip.background = element_rect(fill = "gray90", color = "black"),
      strip.text = element_text(size = base_size * 0.9, face = "plain")
    )
}

# Use in plots
ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(x = "X Variable", y = "Y Variable") +
  theme_apa()
```

### 6. Exporting for Publication

#### Vector Formats (Preferred)

```r
# PDF (best for print)
ggsave("figure1.pdf", width = 6, height = 4, dpi = 300, device = cairo_pdf)

# EPS (alternative vector format)
ggsave("figure1.eps", width = 6, height = 4, device = cairo_ps)

# SVG (web-friendly vector)
ggsave("figure1.svg", width = 6, height = 4)
```

#### Raster Formats (When Required)

```r
# PNG (web, PowerPoint)
ggsave("figure1.png", width = 6, height = 4, dpi = 300, type = "cairo")

# TIFF (some journals require)
ggsave("figure1.tiff", width = 6, height = 4, dpi = 300, compression = "lzw")
```

#### Size Guidelines

**Journal standard sizes** (check specific journal):
- Single column: 3.5 inches wide
- 1.5 column: 5.5 inches wide
- Double column (full width): 7 inches wide
- Height: Typically 3-7 inches

**APA style**:
- Figures should be readable at published size
- Minimum 8-point font in final version
- Aspect ratio often 4:3 or 16:9

### 7. Integrating into R Markdown

```r
# In R Markdown chunk
```{r figure1, fig.cap="Customer satisfaction by usage frequency and segment. Error bars represent 95% confidence intervals.", fig.width=6, fig.height=4}

ggplot(data, aes(x = usage_freq, y = satisfaction, group = segment)) +
  stat_summary(fun = mean, geom = "line", aes(linetype = segment)) +
  stat_summary(fun.data = mean_cl_normal, geom = "errorbar", width = 0.2) +
  scale_linetype_manual(values = c("solid", "dashed", "dotted")) +
  labs(x = "Usage Frequency (uses per month)",
       y = "Mean Satisfaction",
       linetype = "Segment") +
  theme_apa()
```

**For tables**:

```{r table1}
kable(descriptives,
      digits = 2,
      caption = "Descriptive Statistics for Study Variables") %>%
  kable_styling(bootstrap_options = "striped")
```

## Practical Exercise

### Exercise 1: Create Descriptive Table

Generate Table 1 for your capstone including:
- Descriptive statistics (M, SD, Range)
- Correlation matrix
- Proper APA formatting
- Clear notes section

### Exercise 2: Create Comparison Figure

Create a figure comparing groups or showing relationships:
- Use appropriate plot type
- Apply APA theme
- Add proper labels and legend
- Write complete caption
- Export as PDF (300 DPI)

### Exercise 3: Results Visualization

Create a figure showing your main finding:
- Choose visualization that highlights key result
- Include error bars or confidence intervals
- Format for publication
- Write informative caption

### Exercise 4: Model Performance

If using ML, create:
- ROC curve or performance comparison
- Feature importance plot
- Proper captions explaining metrics

## Self-Check Questions

1. When should you use a table vs. a figure?
2. Where does the caption go for tables vs. figures?
3. What information belongs in a figure caption?
4. Should tables have vertical lines in APA style?
5. What's the minimum resolution for publication figures?

## Quality Checklist

**Tables**:
- [ ] Numbered sequentially (Table 1, 2, 3...)
- [ ] Title above table (italicized, descriptive)
- [ ] Horizontal lines only (no vertical)
- [ ] Decimal alignment
- [ ] Clear column headers
- [ ] Notes below table (general, specific, probability)
- [ ] Referenced in text before appearing

**Figures**:
- [ ] Numbered sequentially (Figure 1, 2, 3...)
- [ ] Caption below figure (descriptive)
- [ ] Axes clearly labeled with units
- [ ] Legend included if needed
- [ ] Readable at published size (8pt minimum)
- [ ] Grayscale-friendly (or note color version)
- [ ] High resolution (≥300 DPI)
- [ ] Referenced in text before appearing

## Next Week

**Week 12: Revision & Editing** - Learn systematic revision strategies, peer review processes, and common writing issues to polish your manuscript.

---

*Week 11 of 14 | ANLY699 Research Writing Tutorial*
