# Week 2: Literature Review

## Overview

The literature review is the foundation of your research. This week focuses on systematically searching, evaluating, and synthesizing academic sources to build a theoretical framework for your capstone project.

## Learning Objectives

By the end of this week, you will be able to:
1. Conduct systematic literature searches using academic databases
2. Evaluate source credibility and relevance
3. Synthesize findings from multiple studies
4. Organize literature thematically
5. Identify research gaps
6. Cite sources properly in APA 7 format

## Required Reading

📄 **Primary Resources**: 
- `../APA7/apa-7-professional-sample-paper-2025-revision.pdf` (pp. 7-9, Introduction section)
- `../APA7/apa-7-student-sample-paper-2025-revision.pdf` (Literature review examples)

## Tutorial Content

### 1. Purpose of Literature Review

A literature review serves multiple functions:

- **Establish Context**: Show what's already known
- **Identify Gaps**: Reveal what hasn't been studied
- **Build Framework**: Connect theories and concepts
- **Justify Research**: Demonstrate why your study matters
- **Avoid Duplication**: Ensure your work is original

### 2. Literature Search Strategies

#### Database Selection

**Analytics & Data Science**:
- ACM Digital Library
- IEEE Xplore
- Web of Science
- Scopus
- Google Scholar

**Business & Management**:
- ABI/INFORM
- Business Source Premier
- JSTOR

**Statistics & Methods**:
- JSTOR
- PubMed (health analytics)
- arXiv (preprints)

#### Search Techniques

**Boolean Operators**:
```
AND: machine learning AND healthcare
OR:  "data mining" OR "knowledge discovery"
NOT: analytics NOT "sports analytics"
```

**Phrase Searching**:
```
"predictive analytics"
"deep learning"
"data visualization"
```

**Wildcards**:
```
analy*    → analysis, analytics, analyze
visuali?e → visualize, visualise
```

#### Systematic Approach

```r
# Documentation in R Markdown

## Literature Search Protocol

**Date**: 2025-01-15
**Databases**: IEEE Xplore, ACM Digital Library, Google Scholar
**Keywords**: ("machine learning" OR "deep learning") AND "customer churn"
**Filters**: 2018-2025, peer-reviewed, English
**Results**: 247 initial hits → 45 relevant after screening
```

### 3. Evaluating Sources

#### CRAAP Test

| Criterion | Questions to Ask |
|-----------|------------------|
| **Currency** | When was it published? Is it up-to-date? |
| **Relevance** | Does it address your research question? |
| **Authority** | Who is the author? What are their credentials? |
| **Accuracy** | Is it peer-reviewed? Are claims supported? |
| **Purpose** | Why was it written? Is there bias? |

#### Source Hierarchy (Analytics Research)

1. **Tier 1**: Peer-reviewed journal articles
2. **Tier 2**: Conference proceedings (ACM, IEEE)
3. **Tier 3**: Books, edited volumes
4. **Tier 4**: Technical reports, white papers
5. **Use Cautiously**: Blog posts, news articles, Wikipedia

### 4. Reading Strategies

#### Efficient Reading Sequence

1. **Abstract**: Is it relevant? (30 seconds)
2. **Introduction**: What's the research question? (2 minutes)
3. **Conclusion**: What did they find? (2 minutes)
4. **Method**: How did they do it? (5 minutes)
5. **Results**: What are the details? (10 minutes)
6. **Full Read**: Deep dive if highly relevant (30+ minutes)

#### Note-Taking Template

```r
# Create a reference management data frame

library(tibble)
library(dplyr)

literature_db <- tibble(
  author = character(),
  year = numeric(),
  title = character(),
  journal = character(),
  key_findings = character(),
  methodology = character(),
  relevance = character(),
  citation_key = character()
)

# Example entry
literature_db <- add_row(literature_db,
  author = "Smith & Jones",
  year = 2023,
  title = "Machine Learning in Healthcare Analytics",
  journal = "Journal of Data Science",
  key_findings = "Random forests outperformed logistic regression",
  methodology = "Comparative study, n=500 patients",
  relevance = "Provides baseline methods for my analysis",
  citation_key = "smith_2023"
)
```

### 5. Synthesizing Literature

#### Organizational Strategies

**Thematic Organization** (Recommended):
```
Introduction
├── Theme 1: Predictive Models in Healthcare
│   ├── Traditional approaches (regression, decision trees)
│   └── Modern approaches (deep learning, ensembles)
├── Theme 2: Feature Selection Methods
│   ├── Filter methods
│   └── Wrapper methods
├── Theme 3: Model Evaluation Metrics
│   ├── Accuracy measures
│   └── Clinical relevance
└── Research Gap: Limited studies on interpretability
```

**Chronological Organization** (Use sparingly):
- Early work (pre-2015)
- Recent developments (2015-2020)
- Current state (2020-present)

**Methodological Organization**:
- Experimental studies
- Observational studies
- Meta-analyses

### 6. APA 7 Citation Formats

#### In-Text Citations

**One Author**:
- Narrative: Smith (2023) found that...
- Parenthetical: Recent studies show... (Smith, 2023)

**Two Authors**:
- Always use "&" in parentheses: (Smith & Jones, 2023)
- Use "and" in narrative: Smith and Jones (2023) demonstrated...

**Three or More Authors**:
- First citation: (Smith et al., 2023)
- All subsequent: (Smith et al., 2023)

**Direct Quotes**:
- Short (<40 words): "Quote text" (Smith, 2023, p. 45)
- Long (≥40 words): Block quote format (indent 0.5 inch)

#### Reference List Formats

**Journal Article**:
```
Author, A. A., & Author, B. B. (Year). Title of article. Journal Name, 
  volume(issue), page-page. https://doi.org/10.xxxx
```

**Book**:
```
Author, A. A. (Year). Book title (Edition). Publisher.
```

**Website**:
```
Author, A. A. (Year, Month Day). Page title. Site Name. URL
```

### 7. Writing the Literature Review

#### Structure

```markdown
## Introduction

The rise of big data has transformed healthcare analytics (Smith, 2023). 
This review examines three key areas: predictive modeling approaches, 
feature engineering techniques, and validation strategies.

## Predictive Modeling Approaches

### Traditional Statistical Methods

Early healthcare analytics relied on logistic regression due to 
interpretability (Jones & Williams, 2019). However, these models 
assume linear relationships...

### Machine Learning Methods

Recent work has explored random forests (Brown et al., 2021) and 
neural networks (Chen, 2022). While these methods achieve higher 
accuracy...

## Research Gap

Despite advances, few studies address model interpretability in 
clinical settings (Davis, 2023). This gap motivates the current study.
```

#### Synthesis Language

**Compare/Contrast**:
- Similarly, Jones (2023) found...
- In contrast to Smith's findings...
- Consistent with prior research...
- These results contradict...

**Show Relationships**:
- Building on this work...
- Extending Smith's framework...
- This finding supports the theory that...

**Identify Gaps**:
- However, no studies have examined...
- Despite this progress, X remains unclear...
- This approach has not been applied to...

## Practical Exercise

### Exercise 1: Literature Search

1. Define your research topic
2. Identify 3-5 key terms
3. Search two academic databases
4. Find 10 relevant articles (2020 or newer)
5. Create a summary table:

```r
# Create your literature table
library(knitr)
library(kableExtra)

lit_summary <- data.frame(
  Author = c("Smith et al.", "Jones & Brown", "..."),
  Year = c(2023, 2022, "..."),
  Method = c("Survey", "Experiment", "..."),
  Sample = c("n=500", "n=200", "..."),
  Key_Finding = c("...", "...", "...")
)

kable(lit_summary, caption = "Literature Summary Table") %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```

### Exercise 2: Citation Practice

Rewrite these citations in proper APA 7 format:

1. Smith wrote in 2023 that machine learning was useful
2. A study by Jones and Williams from 2022 found significant results
3. According to recent research (Brown 2021, Davis 2023) this is important
4. Multiple studies have shown this (Smith 2023, Jones 2022, Chen 2021, Davis 2020)

<details>
<summary>Answers</summary>

1. Smith (2023) found that machine learning was useful.
2. Jones and Williams (2022) found significant results.
3. According to recent research (Brown, 2021; Davis, 2023), this is important.
4. Multiple studies have shown this (Chen, 2021; Davis, 2020; Jones, 2022; Smith, 2023).
   *Note: Multiple citations are ordered alphabetically by first author's surname*
</details>

### Exercise 3: Write a Mini Literature Review

Write 2-3 paragraphs (500 words) reviewing literature on your chosen topic:
- Begin with broad context
- Narrow to your specific focus
- Synthesize (don't just summarize) 5+ sources
- Identify the research gap
- Use proper APA 7 in-text citations

## Tools for Literature Management

### Reference Management Software

**Recommended**:
- **Zotero** (Free, open-source)
- **Mendeley** (Free, with collaboration features)
- **EndNote** (Paid, institutional licenses)

### R Packages

```r
# Citation management in R
install.packages("citr")        # RStudio citation plugin
install.packages("RefManageR")  # BibTeX management
install.packages("knitcitations")

# Example usage
library(knitcitations)
citep("10.1234/example.doi")  # Cite by DOI
bibliography()                 # Generate bibliography
```

## Self-Check Questions

1. What is the difference between a narrative and parenthetical citation?
2. How do you cite a work with 4 authors the first time vs. subsequent times?
3. What should you do if two sources have the same author and year?
4. In what order should multiple citations in parentheses appear?
5. When should you use a direct quote vs. paraphrasing?

## Application to Your Project

Complete these tasks for your capstone:

1. **Search Protocol**: Document your search strategy
2. **Source List**: Identify 15-20 relevant sources
3. **Annotated Bibliography**: Write 150-word summaries of 5 key sources
4. **Thematic Map**: Create a concept map organizing literature themes
5. **Gap Statement**: Write 1-2 paragraphs identifying the research gap

## Next Week

**Week 3: Research Questions & Hypotheses** - Transform your literature review insights into specific, testable research questions.

---

*Week 2 of 14 | ANLY699 Research Writing Tutorial*
