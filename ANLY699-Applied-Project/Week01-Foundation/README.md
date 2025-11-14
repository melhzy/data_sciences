# Week 1: Research Foundation

## Overview

This week introduces the fundamentals of scientific research and APA 7th edition formatting. You'll learn the structure of research papers, understand the research process, and become familiar with basic APA style requirements.

## Learning Objectives

By the end of this week, you will be able to:
1. Describe the scientific research process
2. Identify the major sections of a research paper
3. Apply basic APA 7 formatting rules
4. Understand the purpose of each paper section
5. Recognize differences between student and professional papers

## Required Reading

📄 **Primary Resource**: `../APA7/Scientific Research and Methodology.pdf`
- Focus on chapters covering research fundamentals
- Note the iterative nature of research

📄 **APA Samples**: 
- `../APA7/apa-7-student-sample-paper-2025-revision.pdf`
- `../APA7/apa-7-professional-sample-paper-2025-revision.pdf`

## Tutorial Content

### 1. The Scientific Research Process

Scientific research follows a systematic approach:

```
Research Question → Literature Review → Hypothesis → Methodology 
     ↓                                                    ↓
 Dissemination ← Discussion ← Results ← Data Collection & Analysis
```

#### Key Principles

- **Objectivity**: Minimize bias through rigorous methods
- **Replicability**: Document procedures so others can replicate
- **Transparency**: Report all findings, including null results
- **Validity**: Ensure measures assess what they claim to measure

### 2. Structure of a Research Paper

All APA research papers follow a consistent structure:

#### Title Page
- Running head (professional papers only)
- Title (bold, centered)
- Author name(s)
- Institutional affiliation
- Course information (student papers)

#### Abstract (150-250 words)
- Concise summary of entire study
- Research question, methods, results, conclusions
- Keywords (3-5 terms)

#### Introduction
- Background and context
- Literature review
- Research gap
- Purpose statement
- Hypotheses

#### Method
- Participants/Sample
- Materials/Measures
- Procedure
- Data analysis plan

#### Results
- Statistical findings
- Tables and figures
- Objective reporting (no interpretation)

#### Discussion
- Interpretation of findings
- Comparison with existing literature
- Limitations
- Implications and future research

#### References
- All cited sources in alphabetical order
- Hanging indent format

### 3. APA 7 Basic Formatting

#### Document Setup

```r
# R Markdown YAML header for APA 7
---
title: "Your Research Title"
author: "Your Name"
date: "2025"
output:
  html_document:
    toc: true
    toc_float: true
  word_document:
    reference_docx: apa7_template.docx
---
```

#### Formatting Requirements

- **Font**: 12-pt Times New Roman, Calibri (11 pt), or Arial (11 pt)
- **Margins**: 1 inch on all sides
- **Line Spacing**: Double-spaced throughout
- **Alignment**: Left-aligned (ragged right)
- **Indentation**: 0.5 inch first line of paragraphs
- **Page Numbers**: Top right corner

#### Heading Levels

APA uses up to 5 heading levels:

```
# Level 1: Centered, Bold, Title Case

## Level 2: Left-Aligned, Bold, Title Case

### Level 3: Left-Aligned, Bold Italic, Title Case

#### Level 4: Indented, Bold, Title Case, Ending with Period.

##### Level 5: Indented, Bold Italic, Title Case, Ending with Period.
```

### 4. Writing Style Guidelines

#### Active vs. Passive Voice

✅ **Preferred (Active)**: "We analyzed the data using regression."
❌ **Avoid (Passive)**: "The data were analyzed using regression."

#### Person and Tense

- **Introduction/Discussion**: Past or present tense
- **Method**: Past tense (what you did)
- **Results**: Past tense (what you found)
- **First person**: Acceptable ("I" or "We")

#### Bias-Free Language

- Use person-first language: "people with diabetes" (not "diabetics")
- Use specific age ranges: "adults aged 25-40" (not "middle-aged")
- Use gender-neutral terms: "participants" (not "subjects")

### 5. Common APA 7 Updates

If familiar with APA 6, note these changes:

| Element | APA 6 | APA 7 |
|---------|-------|-------|
| Running head | "Running head: TITLE" | "TITLE" only |
| Location | City, State: Publisher | Publisher only |
| DOI format | doi:10.xxxx | https://doi.org/10.xxxx |
| Font options | Times New Roman only | Multiple options |
| Paragraph indent | 0.5 inch | 0.5 inch (unchanged) |

### 6. Publishing Research: Preprints

#### What Are Preprints?

Preprints are complete research manuscripts shared publicly **before** peer review. They allow rapid dissemination of findings while you pursue traditional publication.

#### Benefits of Preprints

- **Speed**: Share findings immediately (hours vs. months)
- **Visibility**: Increase discoverability and citations
- **Feedback**: Receive community input before peer review
- **Timestamp**: Establish priority for your work
- **Open Access**: Free access for all readers

#### Preprints.org Platform

**Preprints.org** (https://preprints.org/) is a multidisciplinary preprint server:

**Key Features**:
- Free submission and hosting
- DOI assignment for citability
- Subject-specific sections (Computer Science, Engineering, etc.)
- Optional peer review process
- Integration with MDPI journals

**Submission Process**:

1. **Prepare Manuscript**
   - Complete, unsubmitted manuscript
   - Abstract, keywords, references
   - Figures and tables embedded

2. **Create Account**
   - Register at preprints.org
   - ORCID linking recommended

3. **Upload Materials**
   ```
   Required:
   - Manuscript PDF/Word
   - Title and abstract
   - Subject areas (select 2-3)
   - Keywords (5-8)
   
   Optional:
   - Supplementary files
   - Code repository links
   - Data availability statement
   ```

4. **Metadata Entry**
   - Authors and affiliations
   - Funding information
   - Conflicts of interest
   - Ethics approval statements

5. **Submit and Receive DOI**
   - Review checklist
   - Submit (instant processing)
   - Receive DOI immediately
   - Share link: `https://doi.org/10.20944/preprints[number]`

**After Preprint Publication**:
- ✅ Can still submit to peer-reviewed journals
- ✅ Update preprint with journal reference after acceptance
- ✅ Share preprint link freely
- ✅ Cite preprint DOI in other work

**Example Citation**:

```
Smith, J. A., & Jones, M. B. (2025). Customer churn prediction using 
    machine learning approaches [Preprint]. Preprints. 
    https://doi.org/10.20944/preprints202511.1234.v1
```

**Best Practices**:
- Post preprints after internal review
- Include data/code availability statements
- Update with journal acceptance information
- Respond to community comments professionally

### 7. Publishing in Peer-Reviewed Journals: IEEE Access

#### About IEEE Access

**IEEE Access** is an open-access, peer-reviewed journal ideal for analytics research:

**Journal Characteristics**:
- **Scope**: Multidisciplinary (engineering, computing, technology)
- **Access**: Fully open access (free for readers)
- **Article Processing Charge (APC)**: ~$2,245 USD (as of 2025)
- **Review Speed**: ~4-6 weeks for first decision
- **Publication Speed**: ~2 weeks after acceptance
- **Impact Factor**: ~3.9 (2024)

**Why IEEE Access for Analytics Projects?**

✅ **Broad Scope**: Covers data science, ML, AI, analytics
✅ **Open Access**: Maximum visibility and citations
✅ **Fast Review**: Faster than traditional IEEE journals
✅ **No Length Restrictions**: Comprehensive method/results sections
✅ **Rigorous Review**: Maintains IEEE quality standards

#### Submission Process

**1. Manuscript Preparation**

IEEE Access uses IEEE article template:

```r
# Download template from:
# https://www.ieee.org/publications/authors/author-templates.html

# Or use R Markdown with custom template
---
title: "Your Article Title"
output:
  pdf_document:
    template: ieee_access_template.tex
    keep_tex: true
bibliography: references.bib
csl: ieee.csl
---
```

**Required Sections**:
- Abstract (200-250 words)
- Keywords (5-10)
- Introduction
- Related Work
- Methodology
- Experimental Results
- Discussion
- Conclusion
- References

**Formatting Requirements**:
- Two-column format (template handles this)
- 10pt font
- IEEE reference style (numbered)
- Figures: high resolution (300+ DPI)
- Tables: caption above table

**2. Pre-Submission Checklist**

- [ ] All authors approved manuscript
- [ ] Figures meet resolution requirements
- [ ] References formatted IEEE style
- [ ] Code/data availability statement included
- [ ] Ethics approval documented (if human subjects)
- [ ] Conflicts of interest declared
- [ ] Copyright forms prepared

**3. Online Submission** (ScholarOne)

Navigate to: https://mc.manuscriptcentral.com/ieee-access

```
Step 1: Create Account
- ORCID recommended
- Affiliation details

Step 2: Start New Submission
- Article Type: Regular Paper
- Subject Areas: Select 3-5 relevant areas

Step 3: Upload Files
- Main manuscript (PDF)
- Figures (separate files if required)
- Supplementary materials
- Copyright form

Step 4: Enter Metadata
- Title, abstract, keywords
- Authors and affiliations
- Suggested reviewers (3-5)
- Opposed reviewers (optional)

Step 5: Review and Submit
- Check all fields complete
- Submit manuscript
- Receive confirmation email with manuscript ID
```

**4. Review Process**

**Timeline**:
```
Submission → Editor Assignment (1-3 days)
          ↓
Reviewers Invited (1 week)
          ↓
Reviews Received (3-5 weeks)
          ↓
Decision (Accept/Minor/Major Revision/Reject)
          ↓
Revision Submitted (if required)
          ↓
Final Decision (1-2 weeks)
          ↓
Production and Publication (2 weeks)
```

**Possible Outcomes**:

1. **Accept**: Rare on first submission
2. **Minor Revision**: Address small issues
3. **Major Revision**: Substantial changes needed
4. **Reject**: Manuscript doesn't meet standards

**5. Responding to Reviews**

Create a point-by-point response:

```markdown
RESPONSE TO REVIEWERS

We thank the editor and reviewers for their constructive feedback. 
Below we address each comment and indicate manuscript changes.

REVIEWER 1

Comment 1.1: "The dataset description lacks details about preprocessing."

Response: We agree and have expanded the Data Preprocessing subsection 
(Section III.B, pp. 4-5) to include:
- Missing data handling procedures (2.3% missing values)
- Outlier detection method (IQR ± 1.5)
- Feature scaling approach (standardization)
- Train-test split ratios (70/15/15)

Comment 1.2: "Figure 3 is difficult to read due to small font size."

Response: We increased the font size in Figure 3 to 10pt and improved 
axis label readability. The revised figure appears on p. 8.

[Continue for all comments]

REVIEWER 2

[Address all comments similarly]

SUMMARY OF CHANGES

Major revisions:
1. Expanded data preprocessing details (Section III.B)
2. Added comparison with recent ML methods (Section IV.C)
3. Improved all figures for readability
4. Added discussion of computational complexity (Section V.D)

Minor revisions:
1. Corrected typos in Table 2
2. Updated references with recent 2025 publications
3. Improved clarity in Abstract

Thank you again for the opportunity to revise this manuscript.
```

**6. Post-Acceptance**

After acceptance:
- Receive copyright transfer forms
- Pay APC (~$2,245 USD)
- Review galley proofs carefully
- Approve final version
- Article published with DOI

**Citation Format**:

```
J. A. Smith and M. B. Jones, "Customer churn prediction using machine 
learning approaches," IEEE Access, vol. 13, pp. 12345-12356, 2025, 
doi: 10.1109/ACCESS.2025.1234567.
```

#### Funding for Open Access

**Options to cover APC**:
- University/department research funds
- Grant funding (include APC in budget)
- IEEE membership discounts (10-15% reduction)
- Fee waivers (for underrepresented countries)

#### Alternative IEEE Publication Venues

If IEEE Access doesn't fit:

| Journal | Focus | APC |
|---------|-------|-----|
| **IEEE Transactions on Neural Networks** | Deep learning, AI | $2,495 |
| **IEEE Trans. on Knowledge & Data Eng.** | Data mining, analytics | $2,495 |
| **IEEE Trans. on Cybernetics** | Systems, ML, AI | $2,495 |
| **IEEE Internet of Things Journal** | IoT, smart systems | $2,245 |

**Note**: Traditional IEEE Transactions have longer review times (3-6 months) but higher impact factors.

## Practical Exercise

### Exercise 1: Document Setup

Create a new R Markdown document with proper APA 7 formatting:

```r
# File: week01_exercise.Rmd
---
title: "Impact of Data Visualization on Decision Making"
author: "Your Name"
affiliation: "Your University"
course: "ANLY699: Applied Project"
date: "`r Sys.Date()`"
output:
  html_document:
    theme: cosmo
    toc: true
    toc_float: true
---

# Introduction

Double-spaced text begins here. Use proper citation format when 
referencing sources (Author, Year).

# Method

## Participants

Describe your sample here.

# References

Author, A. A. (Year). Title of article. *Journal Name*, *volume*(issue), 
pages. https://doi.org/10.xxxx
```

### Exercise 2: Paper Structure Analysis

1. Open `../APA7/apa-7-student-sample-paper-2025-revision.pdf`
2. Identify and label each major section
3. Note the heading levels used
4. Count the number of citations in the Introduction
5. Examine the References page formatting

Create a document answering:
- What is the research question?
- How many participants were in the study?
- What statistical tests were used?
- What were the main findings?

### Exercise 3: Preprint Exploration

1. Visit https://preprints.org/
2. Search for papers in your research area (e.g., "machine learning churn prediction")
3. Select 2-3 preprints to examine
4. For each preprint, document:
   - Title and DOI
   - Subject classification
   - Whether it was later published in a journal
   - Number of downloads/views
   - Quality of supplementary materials

**Reflection Questions**:
- What are advantages of posting your capstone as a preprint?
- How could preprint feedback improve your final submission?
- Would you consider posting your work as a preprint? Why or why not?

### Exercise 4: Journal Exploration

1. Visit IEEE Access: https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6287639
2. Search for analytics/data science papers
3. Select 2 papers related to your interests
4. For each paper, analyze:
   - Article structure and sections
   - Types of visualizations used
   - Statistical reporting format
   - Code/data availability statements
   - Average page length

**Questions to Consider**:
- Does your capstone project fit IEEE Access scope?
- What would you need to add/modify for journal submission?
- Is the APC ($2,245) feasible, or are there funding sources?
- Would the 4-6 week review timeline work for your graduation?

## Self-Check Questions

1. What are the main differences between student and professional APA papers?
2. In which sections should you use past tense?
3. What information belongs in an abstract?
4. How should page numbers be formatted?
5. What is the proper indentation for paragraphs?
6. What are the benefits of publishing a preprint?
7. What is the typical Article Processing Charge (APC) for IEEE Access?
8. Can you still submit to a peer-reviewed journal after posting a preprint?

## Answers
<details>
<summary>Click to reveal answers</summary>

1. **Student vs. Professional**: Student papers include course information on title page and omit author note; professional papers include running head and author note.

2. **Past tense**: Method (procedures completed), Results (findings obtained). Present/past in Introduction and Discussion.

3. **Abstract content**: Research question, brief methods, main results, conclusions, implications. Keywords below abstract.

4. **Page numbers**: Top right corner, beginning with title page as page 1.

5. **Paragraph indent**: 0.5 inch (first line only), except for abstracts and block quotes.

6. **Preprint benefits**: Speed (immediate dissemination), visibility (increased citations), community feedback, establish priority, open access for all readers.

7. **IEEE Access APC**: Approximately $2,245 USD (as of 2025).

8. **Yes**: Posting preprints does not prevent journal submission. Most journals (including IEEE) allow preprint posting.
</details>

## Application to Your Project

This week, begin outlining your capstone project:

1. **Preliminary Title**: What is your research about?
2. **Research Area**: What field/domain?
3. **Potential Research Questions**: What do you want to investigate?
4. **Why It Matters**: What is the significance?
5. **Dissemination Plan**: Consider your publication strategy
   - Will you post a preprint for early feedback?
   - Are you targeting a specific journal (e.g., IEEE Access)?
   - What's your timeline for submission?

Save these notes—they'll evolve throughout the course.

## Additional Resources

### APA Style
- [APA Style Blog](https://apastyle.apa.org/blog)
- [Purdue OWL APA 7 Guide](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/apa_changes_7th_edition.html)
- [APA 7 Quick Reference](https://apastyle.apa.org/instructional-aids/reference-guide.pdf)

### Preprints
- [Preprints.org](https://preprints.org/) - Multidisciplinary preprint server
- [arXiv](https://arxiv.org/) - Computer science and statistics preprints
- [bioRxiv](https://www.biorxiv.org/) - Biology preprints
- [OSF Preprints](https://osf.io/preprints/) - General science preprints

### IEEE Access
- [IEEE Access Homepage](https://ieeeaccess.ieee.org/)
- [Author Guidelines](https://ieeeaccess.ieee.org/about-ieee-access/learn-more-about-ieee-access/)
- [Article Template](https://www.ieee.org/publications/authors/author-templates.html)
- [Submission Portal](https://mc.manuscriptcentral.com/ieee-access)

## Next Week

**Week 2: Literature Review** - Learn systematic literature searching, source evaluation, and synthesis strategies.

---

*Week 1 of 14 | ANLY699 Research Writing Tutorial*
