# Week 4: Research Methodology

## Overview

The methodology section describes HOW you will answer your research questions. This week covers research design, sampling strategies, data collection procedures, and ethical considerations for analytics projects.

## Learning Objectives

By the end of this week, you will be able to:
1. Select appropriate research designs for your questions
2. Develop sampling strategies with justification
3. Plan data collection procedures
4. Address validity and reliability concerns
5. Consider ethical implications and IRB requirements
6. Write a comprehensive Method section

## Required Reading

📄 **Primary Resources**: 
- `../APA7/Scientific Research and Methodology.pdf` (Methodology chapters)
- `../APA7/Introduction to Research Statistical Analysis.pdf` (Study design section)

📄 **Sample Papers**: Examine Method sections in `../SamplePapers/`

## Tutorial Content

### 1. Research Design Types

#### Quantitative Designs

**Experimental Design**:
- Random assignment to conditions
- Manipulation of independent variable
- High internal validity
- Establishes causation

```r
# Example: A/B Test Design
experiment <- list(
  design = "Between-subjects",
  conditions = c("Treatment A", "Treatment B", "Control"),
  assignment = "Random",
  sample_size = "n = 150 per condition (450 total)",
  duration = "2 weeks"
)
```

**Quasi-Experimental**:
- No random assignment
- Natural groups or pre-existing conditions
- Moderate internal validity
- Suggests causation

**Observational/Correlational**:
- No manipulation
- Measures relationships between variables
- Cannot establish causation
- Common in analytics projects

```r
# Example: Predictive Analytics Study
observational <- list(
  design = "Retrospective cohort",
  data_source = "Customer transaction database (2020-2024)",
  sample = "All customers with ≥6 months activity (n = 5,247)",
  analysis = "Logistic regression predicting churn"
)
```

**Survey Research**:
- Self-report data
- Describes attitudes, behaviors, characteristics
- Can be cross-sectional or longitudinal

#### Design Selection Guide

| Research Question | Recommended Design |
|-------------------|-------------------|
| "Does X cause Y?" | Experimental (RCT) |
| "Does X predict Y?" | Observational + regression |
| "How do groups differ?" | Quasi-experimental or comparative |
| "What are the characteristics?" | Descriptive/survey |
| "What are the trends?" | Longitudinal/time series |

### 2. Sampling Strategies

#### Probability Sampling

**Simple Random Sampling**:
- Every element has equal selection probability
- Best for generalizability

```r
# Simple random sample in R
set.seed(123)
population <- 1:10000
sample_ids <- sample(population, size = 500, replace = FALSE)
```

**Stratified Sampling**:
- Divide population into strata (groups)
- Random sample from each stratum
- Ensures representation of subgroups

```r
# Stratified sampling
library(dplyr)

stratified_sample <- data %>%
  group_by(customer_segment) %>%
  sample_n(size = 100) %>%  # 100 from each segment
  ungroup()
```

**Cluster Sampling**:
- Sample groups (clusters), then all within selected clusters
- Useful for geographically dispersed populations

#### Non-Probability Sampling

**Convenience Sampling**:
- Use readily available data
- Common in analytics: existing databases
- Acknowledge as limitation

**Purposive Sampling**:
- Deliberately select specific cases
- Used for specialized populations

**Snowball Sampling**:
- Participants recruit other participants
- For hard-to-reach populations

#### Sample Size Considerations

**Power Analysis**:

```r
# Sample size calculation for t-test
library(pwr)

# Detect medium effect (d = 0.5) with 80% power
pwr.t.test(d = 0.5, sig.level = 0.05, power = 0.8, 
           type = "two.sample")
# Result: n ≈ 64 per group

# For regression (medium effect, 5 predictors)
pwr.f2.test(u = 5, f2 = 0.15, sig.level = 0.05, power = 0.8)
# Result: n ≈ 92
```

**Rule of Thumb (Regression)**:
- Minimum: 10-15 observations per predictor
- Preferred: 20+ observations per predictor
- Example: 5 predictors → n ≥ 100-150

**Machine Learning**:
- More complex models need more data
- Common split: 70% train, 15% validation, 15% test
- Consider class imbalance

### 3. Data Collection Procedures

#### Secondary Data (Common in Analytics)

**Advantages**:
- Cost-effective
- Large sample sizes
- Real-world data

**Considerations**:
- Data quality assessment
- Missing data patterns
- Documentation of source

```r
# Document data source in Method section
## Data Source

Customer transaction data were obtained from the company's SQL database 
covering January 1, 2020 to December 31, 2024. The dataset included 
purchase history, customer demographics, and service interactions for 
all active accounts (N = 47,823). Data extraction was performed on 
March 15, 2025, using standardized SQL queries (see Appendix A).

**Data Quality**. Prior to analysis, we assessed data completeness. 
Missing data rates were: purchase amount (0.2%), customer age (3.1%), 
and account tenure (0.0%). Records with >20% missing values (n = 342, 
0.7%) were excluded, yielding a final analytical sample of N = 47,481.
```

#### Primary Data Collection

**Surveys**:

```markdown
## Measures

**Customer Satisfaction**. Satisfaction was measured using a 5-item 
scale adapted from Smith and Jones (2022). Items (e.g., "I am satisfied 
with the service quality") used a 7-point Likert scale (1 = *strongly 
disagree*, 7 = *strongly agree*). The scale demonstrated good internal 
consistency (Cronbach's α = .87).

**Usage Frequency**. Participants reported how often they used the 
platform in the past month using a single item: "In the past 30 days, 
how many times did you access the platform?" Response options ranged 
from *never* (0) to *daily* (30+).
```

**Experimental Manipulations**:

```markdown
## Procedure

Participants were randomly assigned to one of three conditions: 
(a) simplified dashboard with ≤5 metrics (n = 48), (b) standard 
dashboard with 10-15 metrics (n = 51), or (c) comprehensive dashboard 
with 20+ metrics (n = 49). Random assignment was achieved using a 
computer-generated random number sequence (see supplementary materials).

Participants completed a 20-minute decision-making task using their 
assigned dashboard. Task accuracy and completion time were recorded 
automatically by the system.
```

### 4. Validity and Reliability

#### Internal Validity

**Threats**:
- Selection bias
- History effects
- Maturation
- Testing effects
- Instrumentation

**Controls**:
- Random assignment (experiments)
- Control groups
- Counterbalancing
- Standardized procedures

#### External Validity

**Generalizability considerations**:
- Population validity: Sample → Target population
- Ecological validity: Lab → Real world
- Temporal validity: Now → Future

**Enhance generalizability**:
- Representative sampling
- Realistic settings/tasks
- Multiple sites/contexts

#### Construct Validity

**For Measures**:
- Face validity: Appears to measure construct
- Content validity: Covers construct domain
- Criterion validity: Correlates with established measures
- Convergent validity: Correlates with similar constructs
- Discriminant validity: Doesn't correlate with dissimilar constructs

#### Reliability

**Types**:
- Internal consistency: Cronbach's α (≥.70 acceptable, ≥.80 good)
- Test-retest: Stability over time
- Inter-rater: Agreement between raters

```r
# Calculate Cronbach's alpha
library(psych)

# Example: 5-item satisfaction scale
satisfaction_items <- data[, c("sat1", "sat2", "sat3", "sat4", "sat5")]
alpha(satisfaction_items)

# Result: raw_alpha = 0.87 (good reliability)
```

### 5. Ethical Considerations

#### Key Ethical Principles

1. **Respect for Persons**: Autonomy, informed consent
2. **Beneficence**: Maximize benefits, minimize harms
3. **Justice**: Fair participant selection

#### Informed Consent Elements

```markdown
## Ethical Considerations

This study was approved by the Institutional Review Board (IRB #2025-001). 
All participants provided informed consent before participation. The 
consent form detailed the study purpose, procedures, potential risks and 
benefits, confidentiality measures, and the right to withdraw without 
penalty.

**Data Privacy**. Customer data were de-identified prior to analysis. 
A unique identifier replaced personal information (names, email addresses, 
phone numbers). The linking file was stored on an encrypted, password-
protected server accessible only to the principal investigator.

**Minimal Risk**. The study involved minimal risk beyond everyday computer 
use. No deception was used, and participants could skip any questions or 
withdraw at any time.
```

#### Data Analytics Specific Issues

- **Privacy**: De-identification, aggregation
- **Consent**: Secondary data use
- **Algorithmic Bias**: Fair model development
- **Transparency**: Disclose data sources and methods

### 6. Writing the Method Section

#### APA Structure

The Method section has four standard subsections:

**1. Participants (or Sample)**:
- Who was studied?
- How many?
- Key characteristics (age, gender, etc.)
- Recruitment method

**2. Materials (or Measures)**:
- What instruments/tools were used?
- Psychometric properties
- For secondary data: Database description

**3. Procedure**:
- Step-by-step what happened
- Timeline
- Experimental manipulations (if any)

**4. Data Analysis**:
- Statistical tests planned
- Software used
- Significance level
- Handling of missing data

#### Example Method Section

```markdown
# Method

## Participants

The sample consisted of 327 customers (158 female, 169 male) from a 
mid-sized e-commerce platform. Participants ranged in age from 22 to 
67 years (M = 38.4, SD = 11.2). Inclusion criteria required customers 
to have (a) active accounts for ≥12 months and (b) made ≥3 purchases 
in the preceding year. Customers who opted out of research participation 
(n = 48) were excluded, yielding a response rate of 87%.

## Materials

**Purchase Data**. Transaction records included purchase date, product 
category, order value, and payment method. Data were extracted from the 
company's PostgreSQL database.

**Customer Satisfaction Survey**. Satisfaction was assessed using the 
Customer Satisfaction Index (CSI; Johnson, 2020), a validated 7-item 
measure (α = .89 in original validation). Items used 5-point scales 
(1 = *very dissatisfied*, 5 = *very satisfied*). In the current sample, 
the CSI demonstrated good reliability (α = .91).

## Procedure

Data collection occurred in two phases. First, historical purchase data 
(January 2023 - December 2024) were extracted on February 1, 2025. 
Second, satisfaction surveys were emailed to eligible customers on 
February 15, 2025, with a 2-week response window. Participants received 
a $10 gift card for completing the 10-minute survey.

## Data Analysis

Analyses were conducted in R version 4.5.2 (R Core Team, 2025) using 
tidyverse (Wickham et al., 2024) and lme4 (Bates et al., 2023) packages. 
We used hierarchical regression to examine predictors of satisfaction, 
entering demographic controls (Block 1), purchase frequency (Block 2), 
and product category preferences (Block 3). Statistical significance 
was set at α = .05. Missing data (<5% per variable) were handled using 
listwise deletion.
```

### 7. Special Considerations for Analytics Projects

#### Machine Learning Studies

```markdown
## Data Preprocessing

**Feature Engineering**. We created 23 derived features including 
recency (days since last purchase), frequency (purchases per month), 
and monetary value (average order value). Categorical variables were 
one-hot encoded. Continuous features were standardized (M = 0, SD = 1).

**Train-Test Split**. Data were randomly partitioned into training (70%, 
n = 33,236), validation (15%, n = 7,122), and test (15%, n = 7,123) sets 
using stratified sampling to maintain class distribution (churn rate ≈ 18% 
across all sets).

## Model Development

We compared four classification algorithms: logistic regression (baseline), 
random forest, gradient boosting (XGBoost), and neural network. 
Hyperparameters were tuned using 5-fold cross-validation on the training 
set. Final models were evaluated on the held-out test set using AUC-ROC, 
precision, recall, and F1-score.
```

## Practical Exercise

### Exercise 1: Design Selection

For each research question, select and justify the appropriate design:

1. "Does personalized email increase click-through rates?"
2. "What factors predict employee turnover?"
3. "How has social media usage changed from 2020-2025?"
4. "Is there a relationship between study time and exam performance?"

### Exercise 2: Write Your Method Section

Draft a complete Method section for your capstone (3-5 pages):

**Required subsections**:
1. Participants/Sample (1 paragraph + demographics table)
2. Materials/Measures (1 paragraph per measure/data source)
3. Procedure (1-2 paragraphs, chronological)
4. Data Analysis (1 paragraph)

**Use this checklist**:
- [ ] Clear description of sample and recruitment
- [ ] Sample size justification (power analysis or rationale)
- [ ] Operational definitions of all variables
- [ ] Reliability/validity information for measures
- [ ] Step-by-step procedure
- [ ] Statistical tests specified
- [ ] Software and packages listed
- [ ] Ethical approval mentioned
- [ ] Past tense throughout

### Exercise 3: Sample Size Justification

Calculate required sample size for your study:

```r
library(pwr)

# Example: Compare two groups (t-test)
# Expected effect size: d = 0.5 (medium)
# Power: 0.80 (standard)
# Significance: 0.05 (two-tailed)

pwr.t.test(d = 0.5, power = 0.80, sig.level = 0.05, 
           type = "two.sample")

# Document your rationale
```

## Self-Check Questions

1. What's the difference between internal and external validity?
2. When should you use stratified vs. simple random sampling?
3. What are the four main subsections of the Method section?
4. How do you report Cronbach's alpha?
5. What information must be in an informed consent form?

## Common Method Section Mistakes

❌ **Vague descriptions**: "We collected data" → ✅ "Data were collected via online survey distributed March 1-15, 2025"

❌ **Missing details**: State sample size, response rate, exclusions

❌ **Wrong tense**: Use past tense (what you did), not future

❌ **No justification**: Explain why you chose specific methods

❌ **Insufficient validity info**: Report psychometric properties

## Next Week

**Week 5: Data Collection** - Implement your methodology and document the data collection process with quality assurance.

---

*Week 4 of 14 | ANLY699 Research Writing Tutorial*
