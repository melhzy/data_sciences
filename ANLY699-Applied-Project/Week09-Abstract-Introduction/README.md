# Week 9: Abstract & Introduction

## Overview

Though written last, the Abstract and Introduction are readers' first encounter with your work. This week covers crafting effective abstracts that summarize your study and Introductions that build compelling cases for your research.

## Learning Objectives

By the end of this week, you will be able to:
1. Write structured abstracts following APA 7 guidelines
2. Select effective keywords for discoverability
3. Structure Introductions using the funnel approach
4. Build logical arguments from literature to research questions
5. Write clear purpose statements and hypotheses
6. Hook readers while maintaining scientific tone

## Required Reading

📄 **Sample Papers** - Study abstracts and introductions in all files:
- `../SamplePapers/English Language Proficiency.pdf`
- `../SamplePapers/Net Photosynthetic Rate.pdf`
- `../SamplePapers/The Urinary Microbiome.pdf`
- `../SamplePapers/ADAM-1 An AI Reasoning Model.pdf`
- `../SamplePapers/Unveiling the Genetic Networks.pdf`

## Tutorial Content

### 1. Writing Abstracts

#### APA 7 Requirements

- **Length**: 150-250 words (check journal requirements)
- **Format**: Single paragraph, no indentation
- **Tense**: Past tense for procedures, present for conclusions
- **Content**: Self-contained (no citations usually)
- **Keywords**: 3-5 terms, lowercase except proper nouns

#### Structured Abstract Components

Most research abstracts include 4-5 elements:

1. **Background/Objective** (1-2 sentences): Context and purpose
2. **Method** (2-3 sentences): Design, participants, procedures
3. **Results** (2-3 sentences): Key findings with statistics
4. **Conclusion** (1-2 sentences): Interpretation and implications

#### Example Abstract Template

```markdown
Abstract

[OBJECTIVE] This study examined whether usage frequency predicts customer 
satisfaction in e-commerce platforms and whether this relationship varies 
by customer segment. [METHOD] Data from 678 customers (M_age = 38.4 years, 
52% female) were analyzed using hierarchical regression and moderation 
analysis. Satisfaction was measured via validated 7-item scale (α = .92), 
and usage frequency was tracked via system logs. [RESULTS] Usage frequency 
significantly predicted satisfaction (β = .34, p < .001), with customer 
segment moderating this relationship (ΔR² = .03, p < .001). Premium 
customers showed stronger usage-satisfaction associations (b = 0.08) 
compared to basic customers (b = 0.03). Together with product quality 
perceptions, predictors explained 43% of satisfaction variance. 
[CONCLUSION] Findings suggest that behavioral engagement metrics provide 
early indicators of satisfaction and support segment-specific retention 
strategies. Results extend technology acceptance theory to subscription-
based services.

Keywords: customer satisfaction, usage frequency, e-commerce, user 
engagement, predictive analytics
```

#### Machine Learning Study Example

```markdown
Abstract

[OBJECTIVE] This study developed machine learning models to predict 
customer churn in subscription-based services. [METHOD] Using transaction 
data from 47,481 customers over 48 months, we compared four classification 
algorithms: logistic regression, decision trees, random forests, and 
gradient boosting (XGBoost). Data were split 70/15/15 for training, 
validation, and testing, with 10-fold cross-validation for hyperparameter 
tuning. Twenty-three features were engineered from behavioral and 
demographic data. [RESULTS] XGBoost achieved the highest test set 
performance (AUC = .86, accuracy = 78%, F1 = .71), significantly 
outperforming logistic regression (AUC = .81, p < .001). SHAP analysis 
revealed usage frequency (SHAP = 0.34), satisfaction (0.29), and tenure 
(0.21) as primary predictors, while demographics contributed minimally. 
[CONCLUSION] Ensemble methods substantially improve churn prediction over 
traditional approaches. Behavioral metrics outperform demographics, 
suggesting monitoring systems should prioritize engagement tracking. 
Findings support deployment of predictive analytics for proactive 
retention management.

Keywords: machine learning, churn prediction, XGBoost, predictive analytics, 
customer retention
```

#### Abstract Writing Tips

**Be Specific**:
- ❌ "Participants completed various measures"
- ✅ "Participants completed the Customer Satisfaction Index (7 items, α = .92)"

**Include Numbers**:
- ❌ "Results showed significant differences"
- ✅ "Results showed significant differences (t = 9.34, p < .001, d = 1.14)"

**Past Tense for What You Did**:
- "Data were analyzed using..." (not "will be analyzed")
- "Results indicated..." (not "indicate")

**Present Tense for General Conclusions**:
- "Findings suggest that engagement predicts satisfaction"
- "Results support the use of machine learning for churn prediction"

#### Keywords Selection

Choose terms that:
- Capture main concepts/variables
- Potential readers might search
- Balance specificity and breadth
- Include method terms if relevant

```r
# Example keyword sets

## Traditional study
c("customer satisfaction", "e-commerce", "usage patterns", 
  "hierarchical regression", "moderation analysis")

## ML/Data Science study
c("machine learning", "churn prediction", "random forest",
  "feature engineering", "predictive modeling")

## Mixed Methods
c("customer experience", "sentiment analysis", "natural language processing",
  "survey research", "mixed methods")
```

### 2. Introduction Structure

#### Funnel Approach

```
[BROAD]    General topic/field (1 paragraph)
    ↓
[NARROWER] Specific research area (2-3 paragraphs)
    ↓
[FOCUSED]  Literature review & gap (3-5 paragraphs)
    ↓  
[SPECIFIC] Purpose & hypotheses (1-2 paragraphs)
```

#### Paragraph-by-Paragraph Outline

**Paragraph 1: Opening Hook**
- Start with broad significance
- Establish importance
- Preview general topic

**Paragraphs 2-3: Context Building**
- Define key concepts
- Provide background
- Cite foundational work

**Paragraphs 4-7: Literature Review**
- Organize thematically
- Synthesize findings
- Build theoretical framework
- Show what's known

**Paragraph 8: Research Gap**
- Identify what's missing
- Explain why it matters
- Justify your study

**Paragraphs 9-10: Current Study**
- State purpose clearly
- Preview design
- List research questions/hypotheses
- Briefly note significance

### 3. Writing the Introduction

#### Opening Paragraph Examples

**Example 1: Problem-focused**

```markdown
# Introduction

Customer retention represents a critical business challenge, with churn 
costs estimated at $1.6 trillion annually across industries (Kumar & Shah, 
2023). Acquiring new customers costs 5-25 times more than retaining 
existing ones (Reichheld & Schefter, 2020), making customer satisfaction 
and retention key profitability drivers. In subscription-based business 
models—increasingly dominant across software, media, and consumer services—
understanding factors that influence satisfaction and predict churn has 
become essential for sustainable growth. Despite extensive research on 
customer satisfaction (Anderson & Mittal, 2022), the role of usage patterns 
in satisfaction formation and churn prediction remains incompletely 
understood, particularly in e-commerce contexts.
```

**Example 2: Theory-focused**

```markdown
# Introduction

The Technology Acceptance Model (TAM; Davis, 1989) posits that perceived 
usefulness and ease of use drive technology adoption and continued usage. 
Subsequent extensions (Venkatesh et al., 2003) incorporate additional 
factors, yet a fundamental question persists: Does actual usage—the 
behavioral manifestation of acceptance—reciprocally influence user 
satisfaction? While TAM predicts usage from satisfaction, self-perception 
theory (Bem, 1972) suggests a reverse path: frequent usage may signal 
positive attitudes, reinforcing satisfaction. Understanding bidirectional 
usage-satisfaction dynamics has practical implications for designing 
engagement strategies that simultaneously drive usage and satisfaction in 
digital platforms.
```

**Example 3: Gap-focused**

```markdown
# Introduction

Predicting customer churn has attracted substantial research attention, 
with most studies employing traditional statistical methods like logistic 
regression (Neslin et al., 2006; Verbeke et al., 2012). However, these 
approaches assume linear relationships and may overlook complex interaction 
patterns in high-dimensional data. Recent advances in machine learning—
particularly ensemble methods like random forests and gradient boosting—
offer promise for improving prediction accuracy by capturing non-linearities 
and feature interactions (Chen & Guestrin, 2016). Yet few studies 
systematically compare modern ML algorithms against traditional approaches 
using rigorous validation procedures, and even fewer examine which features 
drive predictions. This study addresses these gaps by comparing four 
algorithms and using explainable AI techniques to identify key churn 
predictors.
```

#### Building the Literature Review

**Thematic Organization**:

```markdown
## Theoretical Foundations

Technology acceptance and usage have been extensively studied through 
multiple theoretical lenses. The Technology Acceptance Model (TAM; 
Davis, 1989) emphasizes perceived usefulness and ease of use as primary 
usage determinants. Extensions like UTAUT (Venkatesh et al., 2003) add 
social influence and facilitating conditions. [Continue with 2-3 more 
sentences synthesizing TAM research]

## Usage-Satisfaction Relationships

Prior research consistently finds positive associations between usage 
frequency and satisfaction across contexts. In mobile applications, 
Smith and Jones (2023) reported correlations ranging from r = .25 to 
.42 (mean r = .33 across 8 studies). Similarly, Chen's (2022) meta-
analysis of 47 studies found a mean correlation of r = .37 between 
usage intensity and user satisfaction. [Continue synthesis]

However, most studies examine simple bivariate relationships, with few 
investigating moderators or mediators. Exceptions include Brown et al. 
(2021), who found usage-satisfaction links stronger for instrumental 
versus hedonic applications, and Williams (2020), who identified 
product quality as a potential mediator. [Continue]

## Churn Prediction Approaches

Traditional churn prediction models rely on logistic regression due to 
interpretability (Verbeke et al., 2012). Recent comparisons suggest 
random forests improve prediction by 5-8 percentage points in AUC 
(Hosein et al., 2020). Neural networks show promise but require large 
samples and risk overfitting (Sharma et al., 2021). [Synthesize 
multiple sources]

Feature selection in churn models typically emphasizes RFM (recency, 
frequency, monetary value) variables, with behavioral features generally 
outperforming demographics (Kumar et al., 2019). Yet systematic 
comparisons using explainable AI methods like SHAP values remain rare. 
[Continue]
```

#### Identifying the Gap

Be explicit about what's missing:

```markdown
## The Present Study

Despite extensive research on customer satisfaction and emerging work on 
churn prediction, three gaps persist. First, while usage-satisfaction 
associations are well-documented, few studies examine whether relationships 
vary by customer segment (premium, standard, basic), limiting ability to 
develop targeted strategies. Second, potential mediating mechanisms—such 
as product quality perceptions—remain largely unexplored, restricting 
theoretical understanding. Third, rigorous ML-traditional method comparisons 
using held-out test sets and explainable AI are scarce, hindering evidence-
based algorithm selection.

This study addresses these gaps through three aims: (1) examine usage 
frequency as a satisfaction predictor, testing customer segment moderation; 
(2) investigate product quality as a potential mediator; and (3) develop 
and compare churn prediction models, identifying key features via SHAP 
analysis. We hypothesize that...
```

#### Purpose Statement and Hypotheses

**Clear, Direct Statement**:

```markdown
## Research Questions and Hypotheses

This study examined three primary research questions:

**RQ1**: To what extent does usage frequency predict customer satisfaction?

**RQ2**: Does customer segment moderate the usage-satisfaction relationship?

**RQ3**: Which predictive modeling approach (logistic regression, decision 
tree, random forest, or gradient boosting) achieves optimal churn prediction 
performance?

Based on TAM theory and prior empirical findings, we advanced three 
hypotheses:

**H1**: Usage frequency will positively predict customer satisfaction, 
such that customers with higher usage report greater satisfaction.

**H2**: Customer segment will moderate the usage-satisfaction relationship, 
with stronger associations among premium customers compared to basic 
customers.

**H3**: Product quality perceptions will mediate the relationship between 
usage frequency and satisfaction, such that usage enhances perceived 
quality, which in turn increases satisfaction.

For RQ3, we adopted an exploratory approach given limited comparative 
research, though prior work (Chen & Guestrin, 2016) suggests ensemble 
methods may outperform single models.
```

### 4. Writing Tips

#### Maintain Flow

Use transitions between paragraphs:

- "Building on this theoretical foundation..."
- "However, gaps persist in..."
- "Extending this line of research..."
- "Contrasting with these findings..."
- "Despite these advances..."

#### Balance Citation

- **Over-cited**: "Research shows that satisfaction matters (Smith, 2020; Jones, 2021; Brown, 2022; Williams, 2023; Davis, 2024; Chen, 2025)."
- **Under-cited**: "Satisfaction is important. Usage patterns matter."
- **Balanced**: "Customer satisfaction strongly predicts retention (Smith, 2020) and profitability (Jones, 2021), with effects persisting over multi-year periods (Brown et al., 2022)."

#### Tense Usage

- **Present tense** for established knowledge: "TAM posits that..."
- **Past tense** for specific studies: "Smith (2020) found that..."
- **Present perfect** for accumulated evidence: "Researchers have demonstrated..."

## Practical Exercise

### Exercise 1: Write Your Abstract

Draft a 150-250 word abstract including:
- Objective (1-2 sentences)
- Method (2-3 sentences with specific details)
- Results (2-3 sentences with key statistics)
- Conclusion (1-2 sentences)
- Keywords (3-5 terms)

Use the templates above as guides.

### Exercise 2: Introduction Outline

Create a detailed paragraph-by-paragraph outline:

```markdown
# Introduction [Outline]

**Paragraph 1: Opening**
- Hook with significance/problem
- General topic introduction
- Preview scope

**Paragraph 2: Key Concept 1**
- Define customer satisfaction
- Cite foundational work (3-4 sources)
- Establish importance

**Paragraph 3: Key Concept 2**
- Define usage patterns/engagement
- Measurement approaches
- Theoretical relevance

**Paragraphs 4-5: Literature Theme 1**
- Usage-satisfaction relationships
- Synthesize 5-8 studies
- Identify patterns/inconsistencies

**Paragraphs 6-7: Literature Theme 2**
- Churn prediction approaches
- Traditional vs. ML methods
- Feature importance findings

**Paragraph 8: Research Gap**
- State what's missing (3 specific gaps)
- Explain why it matters
- Justify current study

**Paragraphs 9-10: Current Study**
- State purpose and aims
- List research questions (3)
- Present hypotheses (3) with justification
- Preview significance
```

### Exercise 3: Write Opening Paragraph

Write three different opening paragraphs for your capstone using:
1. **Problem-focused** approach
2. **Theory-focused** approach  
3. **Gap-focused** approach

Choose the most compelling for your paper.

### Exercise 4: Gap Statement

Write 1-2 paragraphs explicitly identifying:
- What is known (from literature review)
- What remains unknown (the gap)
- Why it matters (significance of gap)
- How your study addresses it

## Self-Check Questions

1. What are the four components of a structured abstract?
2. Should you cite sources in the abstract?
3. What is the "funnel approach" to Introductions?
4. Where should your purpose statement appear?
5. What tense should you use for established theories vs. specific studies?

## Quality Checklist

**Abstract**:
- [ ] 150-250 words
- [ ] Includes objective, method, results, conclusion
- [ ] Contains specific statistics
- [ ] Self-contained (understandable alone)
- [ ] 3-5 keywords provided
- [ ] No citations (unless essential)

**Introduction**:
- [ ] Opens with broad significance
- [ ] Defines key concepts
- [ ] Reviews relevant literature (15+ citations)
- [ ] Organizes thematically (not study-by-study)
- [ ] Identifies explicit research gap
- [ ] States clear purpose
- [ ] Lists research questions/hypotheses
- [ ] Provides justification for predictions
- [ ] Flows logically from broad to specific
- [ ] Transitions smoothly between paragraphs

## Next Week

**Week 10: Citations & References** - Master APA 7 citation formats, reference management, and avoiding plagiarism.

---

*Week 9 of 14 | ANLY699 Research Writing Tutorial*
