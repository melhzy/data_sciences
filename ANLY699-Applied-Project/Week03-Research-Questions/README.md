# Week 3: Research Questions & Hypotheses

## Overview

This week transforms your literature review into specific, testable research questions and hypotheses. You'll learn to formulate questions that are feasible, significant, and aligned with your analytics capabilities.

## Learning Objectives

By the end of this week, you will be able to:
1. Formulate clear, focused research questions
2. Distinguish between exploratory and confirmatory research
3. Develop testable hypotheses
4. Define variables operationally
5. Identify independent, dependent, and control variables
6. Align research questions with appropriate methodologies

## Required Reading

📄 **Primary Resources**: 
- `../APA7/Research Questions.pdf`
- `../APA7/Develop_a_Research_Question.pdf`

📄 **Sample Papers**: Review research questions in `../SamplePapers/`

## Tutorial Content

### 1. Characteristics of Good Research Questions

#### FINER Criteria

A strong research question is:

| Criterion | Description | Example |
|-----------|-------------|---------|
| **F**easible | Can be answered with available resources | ✅ "How does visualization type affect decision accuracy?" vs. ❌ "How does AI affect society?" |
| **I**nteresting | Engages you and others | Topic you're passionate about |
| **N**ovel | Adds new knowledge | Addresses identified gap |
| **E**thical | Can be studied ethically | No harm to participants |
| **R**elevant | Matters to field/practice | Has practical implications |

#### Specificity Levels

**Too Broad** ❌:
- "How does technology affect healthcare?"
- "What is machine learning?"

**Too Narrow** ❌:
- "Did patient #347 have diabetes on March 15, 2024?"
- "What was the mean age in Smith et al.'s study?"

**Just Right** ✅:
- "How does predictive model transparency affect physician trust in AI-assisted diagnosis?"
- "What features best predict customer churn in subscription-based services?"

### 2. Types of Research Questions

#### Descriptive Questions

**Purpose**: Describe characteristics or patterns

**Format**: "What...", "How many...", "To what extent..."

**Examples**:
- What are the demographic characteristics of users who abandon online shopping carts?
- How frequently do data scientists use automated machine learning tools?
- To what extent do companies adopt cloud-based analytics platforms?

**Analysis**: Descriptive statistics, frequencies, visualizations

#### Comparative Questions

**Purpose**: Compare groups or conditions

**Format**: "How does X differ between/among..."

**Examples**:
- How does customer satisfaction differ between mobile and desktop users?
- Do click-through rates vary across different email subject line formats?
- How do predictive accuracies compare between logistic regression and random forests?

**Analysis**: t-tests, ANOVA, Mann-Whitney U, Kruskal-Wallis

#### Relational Questions

**Purpose**: Examine associations between variables

**Format**: "What is the relationship between X and Y?"

**Examples**:
- What is the relationship between data quality and model performance?
- How are user engagement metrics associated with subscription renewal rates?
- Is there a correlation between team size and project completion time?

**Analysis**: Correlation, regression, structural equation modeling

#### Causal Questions

**Purpose**: Determine cause-and-effect relationships

**Format**: "What is the effect of X on Y?", "Does X cause Y?"

**Examples**:
- What is the effect of data visualization complexity on decision-making speed?
- Does personalized content increase user retention rates?
- How does training data size affect neural network accuracy?

**Analysis**: Experimental designs, RCTs, quasi-experimental methods

### 3. From Research Question to Hypothesis

#### Research Question → Hypothesis Flow

```
Research Question (broad, exploratory)
         ↓
Directional Prediction (based on theory/literature)
         ↓
Testable Hypothesis (specific, measurable)
```

**Example**:

**RQ**: What is the relationship between feature engineering and model accuracy?

**Theory**: Literature suggests more informative features improve predictions

**Hypothesis**: Models with engineered features will demonstrate higher accuracy than models using only raw features.

#### Hypothesis Types

**Null Hypothesis (H₀)**:
- Statement of no effect or no relationship
- What we test against statistically
- Example: H₀: There is no difference in accuracy between models with and without feature engineering.

**Alternative Hypothesis (H₁ or Hₐ)**:
- Statement of expected effect or relationship
- What we believe is true
- Example: H₁: Models with feature engineering will have higher accuracy than models without.

**Directional vs. Non-directional**:

```r
# Non-directional (two-tailed)
# H₁: μ₁ ≠ μ₂
"There IS a difference between groups"

# Directional (one-tailed)  
# H₁: μ₁ > μ₂
"Group 1 will be GREATER than Group 2"
```

### 4. Variables and Operational Definitions

#### Variable Types

**Independent Variable (IV)**: What you manipulate or compare
- "Treatment condition" in experiments
- "Group membership" in comparative studies
- Goes on x-axis in visualizations

**Dependent Variable (DV)**: What you measure as outcome
- Affected by the IV
- Goes on y-axis in visualizations

**Control Variables**: Held constant or statistically controlled
- Potential confounds
- Account for alternative explanations

**Moderator Variables**: Affect the strength/direction of IV-DV relationship

**Mediator Variables**: Explain WHY the IV affects the DV

#### Example Variable Identification

**Research Question**: Does data visualization type affect decision accuracy?

```r
# Variable specification in R

study_design <- list(
  independent_variable = "Visualization Type",
  iv_levels = c("Bar Chart", "Line Graph", "Heatmap"),
  
  dependent_variable = "Decision Accuracy",
  dv_measurement = "Percentage of correct decisions",
  
  control_variables = c(
    "Participant Age",
    "Prior Analytics Experience",
    "Task Difficulty"
  ),
  
  potential_moderator = "Domain Expertise",
  potential_mediator = "Cognitive Load"
)
```

#### Operational Definitions

Transform abstract concepts into measurable variables:

| Concept | Operational Definition | Measurement |
|---------|----------------------|-------------|
| "User Engagement" | Time spent on platform + actions taken | Minutes logged + count of clicks/posts |
| "Model Performance" | Predictive accuracy | F1-score, AUC-ROC |
| "Data Quality" | Completeness and consistency | % missing values + constraint violations |
| "Customer Satisfaction" | Self-reported satisfaction | 5-point Likert scale survey |

### 5. Writing Research Questions and Hypotheses

#### Format Template

```markdown
## Research Questions

**RQ1**: [Descriptive] What are the characteristics of [population] 
regarding [variable of interest]?

**RQ2**: [Comparative] How does [outcome] differ between [group A] 
and [group B]?

**RQ3**: [Relational] What is the relationship between [variable X] 
and [variable Y] among [population]?

## Hypotheses

**H1**: [Direction] [Group A] will demonstrate [higher/lower] 
[outcome measure] than [Group B].

**H2**: [Relationship] [Variable X] will be [positively/negatively] 
associated with [Variable Y].

**H3**: [Mediation] The effect of [X] on [Y] will be mediated by [M].
```

#### APA Style Presentation

From `../SamplePapers/` examples:

```markdown
The present study investigated three research questions:

**RQ1**: To what extent do machine learning models improve predictive 
accuracy over traditional statistical methods in customer churn prediction?

**RQ2**: Which features contribute most significantly to churn prediction 
accuracy?

**RQ3**: How does model interpretability affect stakeholder adoption of 
predictive analytics?

Based on prior literature (Smith & Jones, 2023), we hypothesized:

**H1**: Machine learning models (random forest, gradient boosting) would 
demonstrate higher AUC-ROC scores than logistic regression.

**H2**: Behavioral features (e.g., usage frequency, support tickets) would 
show stronger associations with churn than demographic features.
```

### 6. Aligning Questions with Methods

#### Question Type → Analysis Strategy

| Research Question | Design | Analysis |
|-------------------|--------|----------|
| What is the average satisfaction? | Descriptive | Mean, SD, visualization |
| Do groups differ? | Comparative | t-test, ANOVA, chi-square |
| Are variables related? | Correlational | Pearson r, Spearman ρ |
| Does X predict Y? | Predictive | Regression, ML models |
| Does X cause Y? | Experimental | ANOVA, regression with controls |

```r
# Matching research design to question

rq1 <- "What predicts customer churn?"
design1 <- "Logistic regression with multiple predictors"
sample1 <- "Historical customer data, n ≥ 1000"

rq2 <- "Does email personalization increase open rates?"
design2 <- "A/B test: personalized vs. generic subject lines"
sample2 <- "Random assignment to conditions, n ≥ 500 per group"

rq3 <- "How do data scientists perceive AI ethics?"
design3 <- "Survey with Likert scales"
sample3 <- "Convenience sample, n ≥ 200"
```

## Practical Exercise

### Exercise 1: Question Evaluation

Evaluate these research questions using FINER criteria:

1. "Is AI good or bad?"
2. "How does training data size affect BERT model performance on sentiment classification?"
3. "What is the relationship between variables?"
4. "Do users prefer dark mode?"

<details>
<summary>Evaluation</summary>

1. **Fails all criteria**: Too vague, not measurable, not feasible
2. **Meets all criteria**: Specific, measurable, feasible, builds on existing research
3. **Fails**: Which variables? What population? Not specific enough
4. **Partially meets**: Needs specification—which users? what context? compared to what?

**Improved #4**: "Do mobile app users (ages 18-35) spend more time in-app when using dark mode compared to light mode?"
</details>

### Exercise 2: Hypothesis Writing

For your capstone project:

1. Write your primary research question
2. Identify IV, DV, and potential controls
3. Write null and alternative hypotheses
4. Specify operational definitions for key variables
5. Justify directional vs. non-directional hypothesis

```r
# Template to complete

my_research <- list(
  question = "___",
  
  variables = list(
    independent = "___",
    dependent = "___",
    controls = c("___", "___")
  ),
  
  hypotheses = list(
    null = "H₀: ___",
    alternative = "H₁: ___"
  ),
  
  operational_definitions = list(
    iv_measure = "___",
    dv_measure = "___"
  ),
  
  justification = "Based on [Author, Year] findings that ___"
)
```

### Exercise 3: Variable Identification

Read a sample paper from `../SamplePapers/` and identify:

1. Research question(s)
2. Hypotheses (if stated)
3. Independent variable(s)
4. Dependent variable(s)
5. Control variables
6. How variables were operationally defined

## Common Pitfalls to Avoid

❌ **Too many research questions**: Focus on 1-3 primary questions

❌ **Unfalsifiable hypotheses**: Must be testable with data

❌ **Confusing correlation and causation**: Be clear about claims

❌ **Vague variable definitions**: Must be measurable/observable

❌ **Hypothesis-data mismatch**: Ensure your data can test your hypothesis

## Self-Check Questions

1. What's the difference between a research question and a hypothesis?
2. When should you use a directional vs. non-directional hypothesis?
3. What makes a research question "feasible"?
4. How do you operationally define an abstract concept?
5. What's the difference between a mediator and a moderator?

## Application to Your Project

Complete your research framework:

**Deliverable**: Research Question Document (2-3 pages)

Include:
1. **Background**: Brief literature context (3-4 sentences)
2. **Research Gap**: What's missing (2-3 sentences)
3. **Research Questions**: 1-3 specific questions
4. **Hypotheses**: Null and alternative for each testable question
5. **Variables Table**:

```r
# Create a variables table

library(knitr)

variables_table <- data.frame(
  Variable = c("IV: ", "DV: ", "CV1: ", "CV2: "),
  Type = c("Categorical/Continuous", "...", "...", "..."),
  Operational_Definition = c("How measured", "...", "...", "..."),
  Source = c("Survey/Database/etc", "...", "...", "...")
)

kable(variables_table, caption = "Variable Specifications")
```

6. **Justification**: Why these questions matter (1 paragraph)

## Next Week

**Week 4: Research Methodology** - Design your study to answer your research questions with rigor and validity.

---

*Week 3 of 14 | ANLY699 Research Writing Tutorial*
