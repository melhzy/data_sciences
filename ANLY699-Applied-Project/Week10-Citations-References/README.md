# Week 10: Citations & References

## Overview

Proper citation is fundamental to academic integrity. This week covers APA 7 citation and reference formats for diverse source types, reference management strategies, and plagiarism avoidance.

## Learning Objectives

By the end of this week, you will be able to:
1. Format in-text citations correctly for all source types
2. Create properly formatted reference list entries
3. Use reference management software effectively
4. Integrate citations into R Markdown workflows
5. Distinguish between acceptable paraphrasing and plagiarism
6. Handle special citation situations (secondary sources, personal communication)

## Required Reading

📄 **Primary Resources**:
- `../APA7/apa-7-professional-sample-paper-2025-revision.pdf` (Focus on References section)
- `../APA7/apa-7-student-sample-paper-2025-revision.pdf` (Citation examples throughout)

📄 Review reference lists in all `../SamplePapers/` files

## Tutorial Content

### 1. In-Text Citation Formats

#### Basic Rules

**One Author**:
- Narrative: Smith (2023) found that...
- Parenthetical: Recent studies show... (Smith, 2023)

**Two Authors**:
- Narrative: Smith and Jones (2023) reported...
- Parenthetical: Findings indicate... (Smith & Jones, 2023)
- Note: Use "and" in narrative, "&" in parentheses

**Three or More Authors**:
- First and all subsequent: Smith et al. (2023)
- Exception: If "et al." creates ambiguity, cite enough authors to distinguish

```markdown
Examples:
- Smith, Jones, & Williams (2023) and Smith, Jones, & Brown (2023) both 
  abbreviated to "Smith et al." would be ambiguous
- Solution: Use "Smith, Jones, Williams, et al." and "Smith, Jones, Brown, et al."
```

#### Same Author, Different Years

```markdown
Smith's research (2020, 2022, 2023) demonstrates...

Multiple studies (Smith, 2020, 2022, 2023) support...
```

#### Same Author, Same Year

Use lowercase letters:

```markdown
Smith (2023a) found X, while Smith (2023b) reported Y.

Research indicates both patterns (Smith, 2023a, 2023b).
```

#### Multiple Citations

Order alphabetically and separate with semicolons:

```markdown
Several studies support this conclusion (Brown, 2021; Chen et al., 2022; 
Davis, 2020; Smith & Jones, 2023).
```

#### Direct Quotes

**Short quotes** (<40 words):

```markdown
Smith (2023) concluded that "customer satisfaction directly influences 
retention rates" (p. 45).

Research shows that "customer satisfaction directly influences retention 
rates" (Smith, 2023, p. 45).
```

**Long quotes** (≥40 words):

```markdown
Smith and Jones (2023) elaborated on the complexity of customer behavior:

    Customer decision-making involves multiple interacting factors 
    including prior experience, social influence, perceived value, and 
    emotional responses. These factors do not operate in isolation but 
    form a complex system where changes in one element cascade through 
    the network, producing sometimes unexpected outcomes. (p. 127)

This perspective emphasizes...
```

Note: Block quotes are indented 0.5 inch, no quotation marks, citation after final punctuation.

### 2. Reference List Formatting

#### General Rules

- Alphabetical by first author's surname
- Hanging indent (0.5 inch)
- Double-spaced
- Authors: Surname, Initials (up to 20 authors; 21+: first 19, ..., last)
- Titles: Sentence case (capitalize only first word, first word after colon, proper nouns)
- Journal titles: Title Case and italicized
- DOI: https://doi.org/xxx (no "Retrieved from" or period after)

#### Journal Articles

**With DOI** (preferred):

```
Author, A. A., & Author, B. B. (Year). Title of article. Title of Journal, 
    volume(issue), page–page. https://doi.org/10.xxxx
```

Examples:

```
Smith, J. K., & Jones, M. L. (2023). Machine learning approaches to customer 
    churn prediction. Journal of Business Analytics, 15(3), 234–251. 
    https://doi.org/10.1016/j.jba.2023.01.004

Chen, W., Davis, R., & Williams, P. (2022). The role of usage patterns in 
    predicting customer satisfaction. International Journal of Consumer 
    Research, 48(2), 112–135. https://doi.org/10.1037/icr0000891
```

**Without DOI** (include URL if online):

```
Brown, A. S. (2021). Customer engagement in e-commerce platforms. Retail 
    Research Quarterly, 33(4), 405–428. https://www.rrq.org/articles/33-4-405
```

**In press / Advance online publication**:

```
Williams, K. T. (2024). Predictive analytics for subscription services. 
    Journal of Marketing Research. Advance online publication. 
    https://doi.org/10.1177/00222437241234567
```

#### Books

**Whole book**:

```
Author, A. A. (Year). Book title: Subtitle. Publisher Name. 
    https://doi.org/10.xxxx
```

Examples:

```
Field, A., Miles, J., & Field, Z. (2012). Discovering statistics using R. 
    Sage Publications.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of 
    statistical learning: Data mining, inference, and prediction (2nd ed.). 
    Springer. https://doi.org/10.1007/978-0-387-84858-7
```

**Edited book**:

```
Editor, E. E., & Editor, F. F. (Eds.). (Year). Book title. Publisher.
```

**Chapter in edited book**:

```
Author, A. A. (Year). Chapter title. In E. E. Editor & F. F. Editor (Eds.), 
    Book title (pp. xx–xx). Publisher.
```

Example:

```
Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the 
    technology acceptance model: Four longitudinal field studies. In 
    P. J. Agerfalk & B. Fitzgerald (Eds.), Information systems research: 
    Relevant theory and informed practice (pp. 219–240). Kluwer Academic.
```

#### Conference Proceedings

**Published proceedings**:

```
Author, A. A., & Author, B. B. (Year). Title of paper. In E. E. Editor 
    (Ed.), Proceedings of the Conference Name (pp. xx–xx). Publisher. 
    https://doi.org/10.xxxx
```

**Paper presentation** (unpublished):

```
Smith, J. K. (2023, June 15–17). Machine learning for churn prediction 
    [Paper presentation]. International Conference on Business Analytics, 
    San Francisco, CA, United States.
```

#### Websites and Online Sources

**Webpage with author**:

```
Author, A. A. (Year, Month Day). Page title. Site Name. URL
```

Example:

```
Chen, W. (2023, March 15). Best practices for customer retention analytics. 
    Analytics Insights. https://www.analyticsinsights.com/retention-practices
```

**Webpage with organization as author**:

```
American Psychological Association. (2024, January 10). APA style and 
    grammar guidelines. https://apastyle.apa.org/style-grammar-guidelines
```

**No date**:

```
Smith, J. (n.d.). Customer satisfaction metrics. Marketing Tools. 
    https://www.marketingtools.com/satisfaction-metrics
```

#### Software and R Packages

**R Core**:

```
R Core Team. (2025). R: A language and environment for statistical computing. 
    R Foundation for Statistical Computing. https://www.R-project.org/
```

**R Packages**:

```
Wickham, H., Averick, M., Bryan, J., Chang, W., McGowan, L., François, R., 
    Grolemund, G., Hayes, A., Henry, L., Hester, J., Kuhn, M., Pedersen, T., 
    Miller, E., Bache, S., Müller, K., Ooms, J., Robinson, D., Seidel, D., 
    Spinu, V., ... Yutani, H. (2024). tidyverse: Easily install and load the 
    'tidyverse' (R package version 2.0.0). https://CRAN.R-project.org/
    package=tidyverse
```

Shortcut: Use `citation("packagename")` in R:

```r
# In R console
citation("tidyverse")
citation("ggplot2")
citation("caret")

# Copy the APA format output to your references
```

#### Data Sets

```
Author, A. A. (Year). Title of data set (Version X) [Data set]. Publisher. 
    https://doi.org/10.xxxx
```

Example:

```
UCI Machine Learning Repository. (2023). Customer churn prediction dataset 
    (Version 2.1) [Data set]. University of California, Irvine. 
    https://archive.ics.uci.edu/ml/datasets/churn
```

### 3. Special Citation Situations

#### Secondary Sources

When citing a source you haven't read directly:

```markdown
In-text: Skinner's theory (as cited in Smith, 2023) suggests...

References: Only list Smith (2023), not Skinner

Exception: If you track down and read the original, cite it directly.
```

#### Personal Communication

```markdown
In-text: J. Smith (personal communication, March 15, 2025) reported...

References: DO NOT include—personal communications aren't recoverable
```

Examples of personal communication:
- Emails
- Personal interviews
- Phone conversations
- Private letters

#### No Author

Use title in place of author:

```markdown
In-text: 
- Narrative: A Study of Customer Behavior (2023) found...
- Parenthetical: Research shows patterns ("Study of Customer Behavior," 2023)

References:
Study of customer behavior in e-commerce. (2023). Journal of Retail 
    Research, 45(2), 123–145. https://doi.org/10.xxxx
```

#### Organization as Author

```markdown
In-text:
- First: American Psychological Association (APA, 2020)
- Subsequent: APA (2020)

If no abbreviation is needed:
- World Health Organization (2023)
- World Health Organization (2023) [all instances]

References:
American Psychological Association. (2020). Publication manual of the 
    American Psychological Association (7th ed.).
```

### 4. Reference Management in R Markdown

#### Using BibTeX

**Step 1**: Create .bib file

```bibtex
@article{smith2023,
  author = {Smith, John K. and Jones, Mary L.},
  title = {Machine Learning Approaches to Customer Churn Prediction},
  journal = {Journal of Business Analytics},
  year = {2023},
  volume = {15},
  number = {3},
  pages = {234--251},
  doi = {10.1016/j.jba.2023.01.004}
}

@book{field2012,
  author = {Field, Andy and Miles, Jeremy and Field, Zoë},
  title = {Discovering Statistics using {R}},
  publisher = {Sage Publications},
  year = {2012},
  address = {London}
}
```

**Step 2**: Reference in YAML header

```yaml
---
title: "My Research Paper"
author: "Your Name"
bibliography: references.bib
csl: apa.csl
output:
  html_document:
    toc: true
  word_document:
    reference_docx: apa_template.docx
---
```

**Step 3**: Cite in text

```markdown
Research shows [@smith2023] that machine learning improves prediction.

As demonstrated by @field2012, statistical methods require assumptions.

Multiple studies support this [@smith2023; @field2012; @brown2021].
```

**Step 4**: Generate references automatically

```markdown
# References

<div id="refs"></div>
```

#### Using R Packages

```r
# Install packages
install.packages("citr")        # RStudio Addin for citations
install.packages("RefManageR")  # Reference management
install.packages("knitcitations")

# citr provides GUI citation picker in RStudio
# Tools → Addins → Insert Citation
```

### 5. Avoiding Plagiarism

#### What Counts as Plagiarism?

**Definitely plagiarism**:
- Copying text without quotation marks or citation
- Paraphrasing without citing the source
- Using others' ideas without acknowledgment
- Submitting others' work as your own

**Not plagiarism**:
- Common knowledge (e.g., "R is a programming language")
- Your own original ideas/analyses
- Proper paraphrasing with citation
- Direct quotes with quotation marks and citation

#### Paraphrasing Correctly

**Original text** (Smith, 2023, p. 45):
> "Customer satisfaction is influenced by multiple interacting factors, including service quality, price perceptions, and prior experiences."

❌ **Too close** (plagiarism even with citation):
> Customer satisfaction is affected by multiple interacting factors, such as service quality, price perceptions, and prior experiences (Smith, 2023).

✅ **Acceptable paraphrase**:
> Smith (2023) argues that satisfaction results from complex interplay among service-related, economic, and experiential factors.

✅ **Acceptable paraphrase 2**:
> Multiple elements shape customer satisfaction, with quality, pricing, and history all playing roles (Smith, 2023).

✅ **Direct quote** (if the exact wording matters):
> According to Smith (2023), "customer satisfaction is influenced by multiple interacting factors, including service quality, price perceptions, and prior experiences" (p. 45).

#### When to Cite

**Always cite**:
- Specific facts, statistics, or data
- Others' ideas, theories, or arguments
- Direct quotes
- Paraphrased content
- Figures or tables from other sources (in caption)

**No citation needed**:
- Common knowledge in your field
- Your own data/analyses
- Your own ideas/interpretations

#### Self-Plagiarism

Reusing your own previously published work requires:
- Citation to your earlier work
- Permission from publisher (if copyrighted)
- Disclosure in author note

For unpublished work (e.g., class assignments), check institution policy.

### 6. Reference Management Tools

#### Zotero (Recommended - Free)

**Setup**:
1. Download from https://www.zotero.org
2. Install browser connector
3. Install Better BibTeX plugin
4. Create library folders by project

**Workflow**:
1. Save articles from web (one click with browser connector)
2. Organize into collections
3. Export BibTeX for R Markdown: File → Export Library → BibTeX
4. Link to R Markdown project

**R Integration**:

```r
# Install RStudio Addin
install.packages("citr")

# In YAML header
bibliography: ~/Zotero/my_project.bib

# Use Addins → Insert citation to search Zotero library
```

#### Mendeley

Similar workflow, free desktop and web app:
- Import PDFs (manual or automatic)
- Add metadata
- Create folders
- Export BibTeX
- Word plugin available

#### EndNote

- Paid (institutional licenses common)
- Robust for large libraries
- Word integration
- Can export BibTeX for R use

### 7. Creating APA-Compliant References in R Markdown

**Complete workflow**:

```yaml
---
title: "Customer Churn Prediction Using Machine Learning"
author: "Your Name"
date: "`r Sys.Date()`"
output:
  word_document:
    reference_docx: apa7_template.docx
  html_document:
    toc: true
    toc_float: true
bibliography: references.bib
csl: apa.csl  # Download from https://github.com/citation-style-language/styles
---
```

```markdown
# Introduction

Customer retention is critical [@smith2023; @jones2021]. The Technology 
Acceptance Model [@davis1989] provides theoretical foundation.

# Method

Data were analyzed using R version `r getRversion()` [@rcoreteam2025] 
with tidyverse [@wickham2024] and caret [@kuhn2023] packages.

# References

::: {#refs}
:::
```

**Generate references automatically**:

```r
# For R packages
writeLines(toBibtex(citation("tidyverse")), "pkg_refs.bib")

# Append multiple packages
pkgs <- c("ggplot2", "dplyr", "caret", "tidyverse")
refs <- lapply(pkgs, citation)
writeLines(unlist(lapply(refs, toBibtex)), "all_packages.bib")
```

## Practical Exercise

### Exercise 1: Format References

Convert these to proper APA 7 references:

1. Book by Smith and Jones published by Wiley in 2022 titled "Data Analytics Methods" (2nd edition)
2. Journal article by Chen in Journal of Statistics vol 45 issue 3 pages 112-134 from 2023, DOI: 10.1234/js.2023.112
3. R package "randomForest" version 4.7-1.1 by Liaw and Wiener in 2024
4. Website by American Marketing Association published March 15, 2023 titled "Customer Retention Strategies"

<details>
<summary>Answers</summary>

1. Smith, A., & Jones, B. (2022). Data analytics methods (2nd ed.). Wiley.

2. Chen, W. (2023). [Article title]. Journal of Statistics, 45(3), 112–134. https://doi.org/10.1234/js.2023.112

3. Liaw, A., & Wiener, M. (2024). randomForest: Breiman and Cutler's random forests for classification and regression (R package version 4.7-1.1). https://CRAN.R-project.org/package=randomForest

4. American Marketing Association. (2023, March 15). Customer retention strategies. https://www.ama.org/retention-strategies
</details>

### Exercise 2: In-Text Citations

Write in-text citations (both narrative and parenthetical) for:

1. Smith's 2023 article
2. A direct quote from page 45 of Jones & Brown's 2022 book
3. Multiple sources: Davis (2021), Chen et al. (2022), Williams (2023)
4. Smith's two articles from 2023

### Exercise 3: Set Up Reference Management

1. Install Zotero or Mendeley
2. Add 10 articles relevant to your capstone
3. Organize into collections/folders
4. Export BibTeX file
5. Link to R Markdown project
6. Practice citing with `citr` addin

### Exercise 4: Create References Section

Draft a complete References section for your capstone with:
- 15-20 journal articles
- 2-3 books
- 2-3 R packages
- 1-2 online sources

Format perfectly in APA 7 style.

## Self-Check Questions

1. How do you cite three or more authors in APA 7?
2. When do you use "and" vs. "&" in citations?
3. Where does the citation go for a block quote?
4. How do you cite the same author with multiple publications in the same year?
5. Should personal communications appear in the reference list?

## Citation Checklist

- [ ] All in-text citations have corresponding reference entries
- [ ] All references have at least one in-text citation
- [ ] Author names formatted correctly (Surname, Initials)
- [ ] Titles in sentence case (except journals)
- [ ] Journal titles italicized and in Title Case
- [ ] DOIs formatted as URLs (https://doi.org/xxx)
- [ ] Hanging indent applied (0.5 inch)
- [ ] Alphabetical order by first author's surname
- [ ] Et al. used correctly (3+ authors, all instances)
- [ ] Direct quotes have page numbers

## Next Week

**Week 11: Figures & Tables** - Create APA-compliant figures and tables with effective data visualization for publication.

---

*Week 10 of 14 | ANLY699 Research Writing Tutorial*
