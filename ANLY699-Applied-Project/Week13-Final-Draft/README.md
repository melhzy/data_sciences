# Week 13: Final Draft Assembly

## Overview

This week brings all components together into a polished, submission-ready manuscript. Focus on final formatting, quality assurance, and preparing supplementary materials.

## Learning Objectives

By the end of this week, you will be able to:
1. Assemble complete manuscripts in proper APA 7 format
2. Create professional title pages and formatting
3. Prepare supplementary materials
4. Generate submission-ready files in multiple formats
5. Perform final quality checks
6. Understand submission requirements

## Required Reading

📄 **Complete Sample Papers**:
- `../APA7/apa-7-student-sample-paper-2025-revision.pdf`
- `../APA7/apa-7-professional-sample-paper-2025-revision.pdf`

Review entire papers for complete structure and formatting.

## Tutorial Content

### 1. Complete Manuscript Structure

#### Student Paper Order

1. **Title Page**
   - Title (bold, centered)
   - Author name
   - Department and Institution
   - Course number and name
   - Instructor name
   - Assignment due date

2. **Abstract** (page 2)
   - 150-250 words
   - Keywords below

3. **Body** (starts page 3)
   - Introduction (no heading)
   - Method
   - Results
   - Discussion

4. **References** (starts new page)

5. **Footnotes** (if any, new page)

6. **Tables** (each on new page)

7. **Figures** (each on new page)

8. **Appendices** (if any, each new page)

#### Professional Paper Order

1. **Title Page**
   - Running head (all caps, max 50 characters)
   - Page number
   - Title (bold, centered)
   - Authors and affiliations
   - Author Note

2. **Abstract** (page 2)
   - Running head and page number
   - "Abstract" (centered, bold)
   - 150-250 words
   - Keywords below

3. **Body** (starts page 3)
   - Running head and page numbers continue
   - Introduction (title repeated, centered, bold)
   - Method, Results, Discussion sections

4. **References** (starts new page)

5. **Footnotes, Tables, Figures, Appendices** (same as student)

### 2. Title Page Formatting

#### Student Paper Title Page Template

```markdown
---
title: "Customer Churn Prediction Using Machine Learning Approaches"
author: "Your Name"
date: "`r Sys.Date()`"
output:
  word_document:
    reference_docx: apa7_student_template.docx
---

# Title Page

<center>
**Customer Churn Prediction Using Machine Learning Approaches**

Your Name

Department of Analytics, Georgetown University

ANLY699: Applied Project

Dr. Instructor Name

`r format(Sys.Date(), "%B %d, %Y")`
</center>

\newpage
```

#### Professional Paper Elements

```markdown
---
title: "Customer Churn Prediction Using Machine Learning Approaches"
shorttitle: "ML FOR CHURN PREDICTION"
author:
  - name: "First Author"
    affiliation: "1"
  - name: "Second Author"  
    affiliation: "2"
affiliation:
  - id: "1"
    institution: "Georgetown University"
  - id: "2"
    institution: "Partner Institution"
authornote: |
  First Author, Department of Analytics, Georgetown University;
  Second Author, Department of Data Science, Partner Institution.
  
  This research was supported by...
  
  Correspondence concerning this article should be addressed to First Author,
  Department of Analytics, Georgetown University, Washington, DC 20057.
  Email: author@georgetown.edu
output:
  word_document:
    reference_docx: apa7_professional_template.docx
---
```

### 3. R Markdown Complete Setup

#### Comprehensive YAML Header

```yaml
---
title: "Customer Satisfaction and Churn Prediction in E-Commerce Platforms"
shorttitle: "CUSTOMER SATISFACTION AND CHURN"
author:
  - name: "Your Name"
    affiliation: "1"
    corresponding: yes
    email: "your.email@university.edu"
affiliation:
  - id: "1"
    institution: "Georgetown University"
abstract: |
  This study examined customer satisfaction predictors and developed machine 
  learning models to predict churn in e-commerce platforms. Analyzing data 
  from 678 customers, results indicated usage frequency significantly predicted 
  satisfaction (β = .34, p < .001), moderated by customer segment (ΔR² = .03). 
  XGBoost achieved optimal churn prediction (AUC = .86), outperforming logistic 
  regression (AUC = .81). SHAP analysis revealed usage, satisfaction, and 
  tenure as primary predictors. Findings support behavioral engagement monitoring 
  for retention management.
keywords: [customer satisfaction, churn prediction, machine learning, e-commerce, XGBoost]
wordcount: "7,842"
bibliography: references.bib
csl: apa.csl
output:
  word_document:
    reference_docx: apa7_template.docx
    number_sections: false
  pdf_document:
    latex_engine: xelatex
    keep_tex: true
  html_document:
    toc: true
    toc_float: true
    toc_depth: 3
    code_folding: hide
    theme: cosmo
header-includes:
  - \usepackage{setspace}
  - \doublespacing
  - \usepackage{float}
  - \floatplacement{figure}{H}
---
```

#### Document Setup Chunk

````markdown
```{r setup, include=FALSE}
knitr::opts_chunk$set(
  echo = FALSE,           # Hide code by default
  warning = FALSE,        # Hide warnings
  message = FALSE,        # Hide messages
  fig.width = 6,          # Figure width
  fig.height = 4,         # Figure height
  fig.align = "center",   # Center figures
  dpi = 300              # High resolution
)

# Load packages
library(tidyverse)
library(knitr)
library(kableExtra)
library(ggplot2)
library(psych)
library(apaTables)

# Set theme
theme_set(theme_apa())

# Load data
data <- read_csv("data/clean_data.csv")
```
````

### 4. Section Templates

#### Abstract Page

````markdown
\newpage

# Abstract

This study examined... [150-250 words]

*Keywords*: customer satisfaction, churn prediction, machine learning, 
e-commerce, predictive analytics

\newpage
````

#### Introduction

````markdown
# Customer Satisfaction and Churn Prediction in E-Commerce Platforms

[No "Introduction" heading - title serves as Level 1 heading]

Customer retention represents a critical business challenge...

## Theoretical Framework

[Level 2 heading]

### Technology Acceptance Model

[Level 3 heading]

The Technology Acceptance Model (TAM; Davis, 1989) posits...
````

#### Method

````markdown
\newpage

# Method

## Participants

The sample consisted of 678 customers...

## Materials

### Customer Satisfaction Scale

Satisfaction was measured using...

### Usage Data

Behavioral data were extracted from...

## Procedure

Data collection occurred in two phases...

## Data Analysis

All analyses were conducted using R version `r getRversion()` 
[@rcoreteam2025]...
````

#### Results with Tables and Figures

````markdown
\newpage

# Results

## Preliminary Analyses

Table 1 presents descriptive statistics and correlations.

```{r table1}
# Generate correlation table
apa.cor.table(data[, c("satisfaction", "usage_freq", "tenure", "age")],
              filename = NA,
              table.number = 1,
              show.sig.stars = TRUE)
```

## Primary Analyses

### Research Question 1

As hypothesized, usage frequency significantly predicted satisfaction...

Figure 1 illustrates the relationship...

```{r figure1, fig.cap="Customer satisfaction by usage frequency and segment. Error bars represent 95% confidence intervals."}
ggplot(data_summary, aes(x = usage_category, y = mean_satisfaction, 
                         fill = segment)) +
  geom_col(position = "dodge") +
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci),
                position = position_dodge(0.9), width = 0.2) +
  scale_fill_grey() +
  labs(x = "Usage Category", y = "Mean Satisfaction", fill = "Segment") +
  theme_apa()
```
````

#### Discussion

````markdown
\newpage

# Discussion

This study investigated... [Opening paragraph]

## Interpretation of Findings

### Usage-Satisfaction Relationship

The strong positive association...

## Limitations

Several limitations warrant consideration...

## Practical Implications

Findings offer actionable insights...

## Future Directions

Future research should...

## Conclusion

In summary, this study demonstrates...
````

#### References

````markdown
\newpage

# References

::: {#refs}
:::

[References auto-generated from .bib file]
````

### 5. Supplementary Materials

#### What to Include

**Supplementary Materials.pdf**:
1. Complete R code (analysis scripts)
2. Data dictionary/codebook
3. Additional tables/figures not in main text
4. Detailed statistical output
5. Survey instruments
6. Extended methodology details

#### Code Appendix

````markdown
\newpage

# Appendix A: Analysis Code

```{r code-appendix, echo=TRUE, eval=FALSE}
# Data preprocessing
data_clean <- data_raw %>%
  filter(!is.na(satisfaction)) %>%
  mutate(
    usage_category = cut(usage_freq, 
                         breaks = c(0, 5, 15, Inf),
                         labels = c("Low", "Medium", "High"))
  )

# Primary analysis: Hierarchical regression
model1 <- lm(satisfaction ~ age + gender + tenure, data = data_clean)
model2 <- lm(satisfaction ~ age + gender + tenure + usage_freq + quality,
             data = data_clean)

# Model comparison
anova(model1, model2)
summary(model2)

# Machine learning: XGBoost
library(xgboost)
library(caret)

# Train-test split
set.seed(123)
train_index <- createDataPartition(data$churned, p = 0.7, list = FALSE)
train_data <- data[train_index, ]
test_data <- data[-train_index, ]

# XGBoost model
xgb_model <- xgboost(
  data = as.matrix(train_data[, predictors]),
  label = train_data$churned,
  max_depth = 6,
  eta = 0.3,
  nrounds = 100,
  objective = "binary:logistic",
  verbose = 0
)

# Predictions and evaluation
predictions <- predict(xgb_model, as.matrix(test_data[, predictors]))
roc_obj <- roc(test_data$churned, predictions)
auc(roc_obj)
```
````

#### Data Dictionary

```markdown
\newpage

# Appendix B: Data Dictionary

```{r data-dictionary, echo=FALSE}
data_dict <- data.frame(
  Variable = c("customer_id", "age", "gender", "satisfaction", 
               "usage_freq", "tenure", "churned"),
  Description = c(
    "Unique customer identifier",
    "Age in years at registration",
    "Self-reported gender",
    "Satisfaction score (1-5 scale)",
    "Monthly platform usage count",
    "Account tenure in months",
    "Churn status (TRUE/FALSE)"
  ),
  Type = c("Integer", "Integer", "Factor", "Numeric", 
           "Integer", "Numeric", "Logical"),
  Range = c("1-47823", "18-85", "M/F/NB/PNTS", "1-5",
            "0-28", "12-48", "TRUE/FALSE"),
  Missing_Pct = c(0.0, 3.1, 0.2, 0.0, 0.02, 0.0, 0.0)
)

kable(data_dict, 
      caption = "Variable Specifications and Descriptive Information") %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```
````

### 6. Generating Multiple Formats

#### Word Document

```r
# Render to Word
rmarkdown::render("manuscript.Rmd", 
                  output_format = "word_document",
                  output_file = "Manuscript_Final.docx")
```

**Post-processing in Word**:
1. Update table of contents if present
2. Verify page breaks
3. Check figure/table positioning
4. Ensure running head on all pages (professional)
5. Add line numbers if required
6. Final spell check

#### PDF Document

```r
# Render to PDF
rmarkdown::render("manuscript.Rmd",
                  output_format = "pdf_document",
                  output_file = "Manuscript_Final.pdf")
```

**Note**: PDF requires LaTeX installation (TinyTeX recommended)

```r
# Install TinyTeX if needed
install.packages("tinytex")
tinytex::install_tinytex()
```

#### HTML Document

```r
# Render to HTML (for sharing/preview)
rmarkdown::render("manuscript.Rmd",
                  output_format = "html_document",
                  output_file = "Manuscript_Preview.html")
```

### 7. Final Quality Checks

#### Automated Checks

```r
# Spelling
library(spelling)
spell_check_files("manuscript.Rmd")

# Word count
library(koRpus)
tokenize(paste(readLines("manuscript.Rmd"), collapse = " "))

# Or simpler
system("wc -w manuscript.Rmd")  # Unix/Mac
# Or count in Word document

# Check for common issues
library(gramr)
run_grammar_checker("manuscript.Rmd")
```

#### Manual Checks

**Print and read** (errors appear different on paper):
- [ ] Read entire manuscript aloud
- [ ] Check all numbers match across text/tables/figures
- [ ] Verify all references cited in text
- [ ] Verify all in-text citations in reference list
- [ ] Check table/figure numbers sequential
- [ ] Confirm all statistics have proper symbols

**Second pair of eyes**:
- [ ] Have colleague proofread
- [ ] Use text-to-speech to hear awkward phrasing
- [ ] Check against journal/assignment requirements

### 8. Submission Preparation

#### File Naming

Use clear, professional naming:
- `Smith_Churn_Prediction_Manuscript.docx`
- `Smith_Supplementary_Materials.pdf`
- `Smith_Figure1.pdf`
- `Smith_Data_Dictionary.csv`

**Not**:
- `final.docx`
- `paper2.docx`  
- `manuscript_revised_v7_FINAL_USE_THIS.docx`

#### Cover Letter (for journal submission)

```markdown
[Date]

[Editor name]
Editor, [Journal Name]

Dear Dr. [Editor]:

I am pleased to submit our manuscript titled "Customer Satisfaction and 
Churn Prediction in E-Commerce Platforms" for consideration for publication 
in [Journal Name].

This study makes several contributions to the literature on customer 
retention analytics. First, we demonstrate that usage frequency predicts 
satisfaction with customer segment moderation, extending technology 
acceptance theory. Second, we compare machine learning algorithms for 
churn prediction using rigorous validation, showing that XGBoost 
outperforms traditional methods by 5 percentage points in AUC. Third, 
using SHAP analysis, we identify key predictors that could inform 
retention strategies.

This manuscript has not been published previously and is not under 
consideration elsewhere. All authors have approved the manuscript and 
agree with its submission to [Journal Name]. The study was approved by 
our Institutional Review Board (#2025-001). We have no conflicts of 
interest to declare.

Thank you for considering our work. We look forward to your response.

Sincerely,

[Your Name]
Corresponding Author
[Contact Information]
```

## Practical Exercise

### Exercise 1: Complete Assembly

Assemble your complete manuscript:
1. Create proper title page
2. Format abstract page
3. Ensure all sections present and properly ordered
4. Add page numbers and running head (if professional format)
5. Place all tables/figures correctly
6. Generate references automatically

### Exercise 2: Multi-Format Generation

Generate three versions:
1. Word document (for editing/submission)
2. PDF (for archiving/sharing)
3. HTML (for preview/web)

Verify formatting consistent across formats.

### Exercise 3: Supplementary Materials

Create comprehensive supplementary file including:
1. Appendix A: Complete R code
2. Appendix B: Data dictionary
3. Appendix C: Additional tables/figures
4. Appendix D: Detailed statistical output

### Exercise 4: Final Quality Check

Complete entire checklist:
- Run automated checks (spelling, grammar)
- Manual proofread
- Verify all cross-references work
- Check numbers consistency
- Confirm APA compliance
- Have peer review final version

## Self-Check Questions

1. What's the difference between student and professional paper format?
2. Where should tables and figures appear in APA manuscripts?
3. What goes in an Author Note?
4. How should you name submission files?
5. What should a journal submission cover letter include?

## Submission Checklist

Before Week 14:

- [ ] Complete manuscript assembled
- [ ] Proper title page format
- [ ] Abstract and keywords included
- [ ] All sections present and ordered correctly
- [ ] References complete and formatted
- [ ] All tables properly formatted and placed
- [ ] All figures properly formatted and placed
- [ ] Page numbers on all pages
- [ ] Running head (if professional format)
- [ ] Supplementary materials prepared
- [ ] Multiple formats generated
- [ ] All quality checks completed
- [ ] Files named professionally
- [ ] Ready for submission

## Next Week

**Week 14: Research Presentation** - Learn to present your research effectively through slides, posters, and oral presentations.

---

*Week 13 of 14 | ANLY699 Research Writing Tutorial*
