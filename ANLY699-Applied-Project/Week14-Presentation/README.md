# Week 14: Research Presentation

## Overview

The final week focuses on presenting your research effectively. You'll learn to create professional presentations, design effective posters, deliver engaging talks, and handle Q&A sessions confidently.

## Learning Objectives

By the end of this week, you will be able to:
1. Create effective research presentation slides
2. Design professional conference posters
3. Deliver clear, engaging oral presentations
4. Handle questions and challenges professionally
5. Adapt presentations for different audiences
6. Present data visualizations effectively

## Tutorial Content

### 1. Presentation vs. Written Paper

#### Key Differences

| Written Paper | Oral Presentation |
|---------------|-------------------|
| Comprehensive detail | Key highlights only |
| Reads linearly | Can skip/reorder |
| Permanent record | Temporary (unless recorded) |
| Reader sets pace | Speaker sets pace |
| Self-contained | Interactive with Q&A |

**Presentation goal**: Communicate 2-3 main messages memorably, not everything you did.

### 2. Slide Presentation Design

#### Structure (15-20 minute talk)

**Slide allocation** (~1-2 minutes per slide):

1. **Title slide** (1 slide)
2. **Introduction/Motivation** (2-3 slides)
   - Problem statement
   - Why it matters
   - Research questions
3. **Method** (2-3 slides)
   - Sample/data
   - Key measures
   - Analysis approach (high-level)
4. **Results** (4-6 slides)
   - Main findings with visuals
   - Focus on 2-3 key results
5. **Discussion** (2-3 slides)
   - Interpretation
   - Implications
   - Limitations
6. **Conclusions** (1 slide)
7. **References** (1 slide, optional backup)
8. **Thank you/Questions** (1 slide)

**Total**: ~15-18 slides for 15-20 minutes

#### Design Principles

**6×6 Rule**:
- Maximum 6 bullets per slide
- Maximum 6 words per bullet
- Better: 3-4 bullets, 4-5 words each

**Text guidelines**:
- Title: 36-44 pt
- Body text: 24-32 pt (minimum 18 pt)
- Sans serif fonts (Arial, Calibri, Helvetica)
- High contrast (dark text on light background)

**Visual hierarchy**:
```
Title (largest, bold)
   Subtitle (medium)
      Bullet point (smaller)
         Sub-bullet (smallest)
```

#### Example Slides

**Title Slide**:

```markdown
─────────────────────────────────────────
CUSTOMER CHURN PREDICTION USING
MACHINE LEARNING APPROACHES

Your Name
Georgetown University
Department of Analytics

ANLY699 Applied Project
April 2025
─────────────────────────────────────────
```

**Problem/Motivation**:

```markdown
─────────────────────────────────────────
THE PROBLEM

• Customer churn costs $1.6 trillion annually
• Acquiring new customers: 5-25x more expensive
• Traditional methods: Limited accuracy

[Simple icon or image illustrating customer leaving]

Research Question: Can ML improve churn prediction?
─────────────────────────────────────────
```

**Method Overview**:

```markdown
─────────────────────────────────────────
STUDY DESIGN

DATA
• 47,481 e-commerce customers
• 48 months (2020-2024)
• 23 behavioral + demographic features

MODELS COMPARED
• Logistic Regression (baseline)
• Random Forest
• XGBoost (winner)

EVALUATION
• 70/15/15 train/validation/test split
• 10-fold cross-validation
• AUC, accuracy, F1-score
─────────────────────────────────────────
```

**Results Slide** (visual-heavy):

```markdown
─────────────────────────────────────────
KEY FINDING: XGBoost Outperforms

[ROC curve chart showing three lines]

Model          AUC    Accuracy
Logistic Reg   .81      74%
Random Forest  .83      76%
XGBoost        .86      78% ⭐

+5 percentage points improvement
─────────────────────────────────────────
```

**Conclusion**:

```markdown
─────────────────────────────────────────
CONCLUSIONS

1. ML improves churn prediction
   ✓ XGBoost: 86% AUC (+5 vs baseline)

2. Behavioral beats demographics
   ✓ Top predictors: Usage, satisfaction, tenure

3. Practical application ready
   ✓ Deploy for early intervention

Future: Real-time monitoring system
─────────────────────────────────────────
```

### 3. Creating Slides in R

#### Using xaringan (R Markdown)

````markdown
---
title: "Customer Churn Prediction"
subtitle: "Using Machine Learning Approaches"
author: "Your Name"
institute: "Georgetown University"
date: "`r Sys.Date()`"
output:
  xaringan::moon_reader:
    css: [default, default-fonts]
    nature:
      highlightStyle: github
      highlightLines: true
      countIncrementalSlides: false
---

# Outline

1. Problem & Motivation
2. Study Design
3. Key Findings
4. Implications

---

# The Problem

.pull-left[
**Churn is costly**
- $1.6T annual impact
- 5-25x acquisition cost
- Limited prediction accuracy

**Research Question**: Can machine learning improve churn prediction?
]

.pull-right[
![](figures/churn_illustration.png)
]

---

# Study Design

```{r echo=FALSE, fig.height=5}
# Include R code for figures
ggplot(data, aes(x = model, y = auc)) +
  geom_col(fill = "steelblue") +
  theme_minimal(base_size = 18)
```

---

class: center, middle

# Key Finding

## XGBoost achieved 86% AUC
### +5 percentage points vs baseline

---

# Conclusions

.large[
1. ✓ Machine learning improves prediction
2. ✓ Behavioral features > demographics
3. ✓ Ready for practical deployment
]

---

class: center, middle

# Questions?

.large[
your.email@georgetown.edu
]
````

#### Using PowerPoint from R

```r
library(officer)
library(rvg)

# Create PowerPoint
pres <- read_pptx()

# Add title slide
pres <- add_slide(pres, layout = "Title Slide", master = "Office Theme")
pres <- ph_with(pres, value = "Customer Churn Prediction",
                location = ph_location_type(type = "ctrTitle"))
pres <- ph_with(pres, value = "Using Machine Learning",
                location = ph_location_type(type = "subTitle"))

# Add content slide with plot
pres <- add_slide(pres, layout = "Title and Content", master = "Office Theme")
pres <- ph_with(pres, value = "Model Performance Comparison",
                location = ph_location_type(type = "title"))

# Add ggplot
plot_obj <- ggplot(results, aes(x = model, y = auc, fill = model)) +
  geom_col() +
  theme_minimal(base_size = 14)

pres <- ph_with(pres, value = dml(ggobj = plot_obj),
                location = ph_location_type(type = "body"))

# Save
print(pres, target = "presentation.pptx")
```

### 4. Conference Poster Design

#### Standard Dimensions

- **Portrait**: 36" (width) × 48" (height)
- **Landscape**: 48" (width) × 36" (height)

Check conference requirements before designing.

#### Layout Sections

```
┌─────────────────────────────────────────────┐
│  TITLE, AUTHORS, AFFILIATIONS               │
├───────────┬───────────────────┬─────────────┤
│           │                   │             │
│ ABSTRACT  │  RESULTS (LARGE)  │ CONCLUSIONS │
│           │                   │             │
│ METHOD    │  [FIGURES/TABLES] │ REFERENCES  │
│           │                   │             │
│ DATA      │  [KEY VISUALS]    │ QR CODE     │
│           │                   │  CONTACT    │
└───────────┴───────────────────┴─────────────┘
```

#### Design Principles

**Typography**:
- Title: 72-96 pt, bold
- Section headers: 48-60 pt
- Body text: 24-36 pt (readable from 6 feet)
- Minimum: 20 pt

**Layout**:
- 3-column format common
- White space = 30-40% of poster
- Visual > Text ratio: Aim for 50:50 or more visuals

**Colors**:
- 2-3 main colors maximum
- High contrast for readability
- Colorblind-friendly palettes
- Institution colors often

#### Creating Posters in R

```r
library(posterdown)

# Create poster template
rmarkdown::draft("my_poster.Rmd",
                template = "posterdown_html",
                package = "posterdown")

# Edit YAML header
---
title: "Customer Churn Prediction Using Machine Learning"
author:
  - name: Your Name
    affiliation: Georgetown University
    email: your.email@georgetown.edu
primary_colour: "#002147"  # Georgetown blue
secondary_colour: "#8D817B"  # Georgetown gray
accent_colour: "#C41230"    # Red for highlights
main_findings:
  - "XGBoost achieved **86% AUC**, outperforming baselines"
  - "Behavioral features > demographic predictors"
  - "Ready for deployment in retention systems"
output:
  posterdown::posterdown_html:
    self_contained: false
---

# Introduction
Customer churn costs...

# Methods
## Data
- 47,481 customers
- 48 months

## Models
```{r}
ggplot(data, ...) + theme_minimal(base_size = 24)
```

# Results
[Large figures here]

# Conclusions
Machine learning approaches...

# References
<div id="refs"></div>
```

### 5. Oral Presentation Delivery

#### Preparation

**Practice timeline**:
- 1 week before: First full run-through
- 3 days before: 3-5 practice runs
- 1 day before: Final practice with timer
- Morning of: Quick mental review

**What to practice**:
- ✓ Transitions between slides
- ✓ Explaining figures clearly
- ✓ Pacing (not too fast/slow)
- ✓ Emphasis on key points
- ✓ Handling potential questions

#### During Presentation

**Opening**:
```
"Good morning. Thank you for the opportunity to present today.

My name is [Name], and I'm going to talk about predicting customer 
churn using machine learning.

[PAUSE - make eye contact]

The problem we're addressing is...
```

**Body**:
- Face the audience (not the screen)
- Use pointer sparingly
- Explain every figure/table
- Pause after important points
- Monitor time (but don't rush)

**Describing figures**:
```
❌ "As you can see in this figure..."

✅ "This figure shows the ROC curves for three models. 
   The solid line represents XGBoost, which achieved 
   the highest AUC of .86. This outperformed the 
   logistic regression baseline by 5 percentage points."
```

**Conclusion**:
```
"To summarize, we found three key results:

First, XGBoost substantially improved churn prediction.
Second, behavioral features were more predictive than demographics.
Third, the model is accurate enough for practical deployment.

These findings suggest that companies should prioritize 
behavioral engagement monitoring.

Thank you. I'm happy to take questions."
```

#### Handling Q&A

**Structure**:
1. Listen fully (don't interrupt)
2. Pause briefly (think)
3. Clarify if needed ("If I understand correctly, you're asking about...")
4. Answer directly
5. Check if answer was sufficient ("Does that address your question?")

**Example exchanges**:

**Q**: "Did you test for overfitting?"

**A**: "Yes, great question. We used three strategies: First, a held-out test set that wasn't touched during model development. Second, 10-fold cross-validation. Third, we monitored train-test performance gaps. The test set AUC was within 2 percentage points of cross-validation, suggesting minimal overfitting."

**Q**: "Why XGBoost instead of neural networks?"

**A**: "Two reasons: First, our sample size of 47,000 is adequate for XGBoost but potentially too small for deep learning. Second, interpretability was important for stakeholder adoption, and XGBoost with SHAP values provided clear feature importance rankings."

**If you don't know**:
"That's an interesting question that we didn't investigate in this study. However, I'd speculate that... [or] I'd need to look into that further and could follow up with you later."

### 6. Audience Adaptation

#### Technical Audience (Conference)

- More methodological detail
- Statistical specifics
- Limitations discussion
- Technical terminology fine

#### Business Audience (Stakeholders)

- Focus on implications
- ROI discussion
- Minimal jargon
- Actionable recommendations

#### General Audience (Public)

- Simple language
- Analogies and examples
- Visual explanations
- Practical relevance

### 7. Remote Presentations

#### Technical Setup

**Before presenting**:
- Test audio/video
- Close unnecessary applications
- Disable notifications
- Have backup plan (phone dial-in)
- Share screen practice

**During presentation**:
- Mute when not speaking (if breakout)
- Look at camera, not screen
- Use "presenter view" if available
- Monitor chat for questions
- Record if permitted

### 8. Creating Effective Visuals

#### Data Visualization for Talks

**Simplify**:
- ❌ 10 lines on one plot
- ✅ Highlight 2-3 key lines, gray out others

**Annotate**:
```r
ggplot(data, aes(x = usage, y = satisfaction)) +
  geom_point() +
  geom_smooth(method = "lm", color = "red", size = 1.5) +
  annotate("text", x = 15, y = 4.5, 
           label = "r = .47, p < .001",
           size = 8, color = "red") +
  annotate("segment", x = 10, y = 4, xend = 12, yend = 4.3,
           arrow = arrow(), color = "red", size = 1) +
  annotate("text", x = 9, y = 4,
           label = "Strong\npositive\nrelationship",
           size = 7, hjust = 1) +
  theme_minimal(base_size = 20)
```

**Progressive disclosure** (for complex visuals):
```r
# Build up plot across multiple slides

# Slide 1: Just points
ggplot(data, aes(x, y)) + geom_point()

# Slide 2: Add regression line
ggplot(data, aes(x, y)) + geom_point() + geom_smooth()

# Slide 3: Add group colors
ggplot(data, aes(x, y, color = group)) + 
  geom_point() + geom_smooth()

# Slide 4: Add annotations
[Full annotated version]
```

## Practical Exercise

### Exercise 1: Create Presentation

Develop a 15-minute presentation:
1. Create 15-18 slides
2. Focus on 2-3 main messages
3. Include 3-4 key visuals
4. Add speaker notes
5. Time yourself presenting

### Exercise 2: Design Poster

Create a conference poster:
1. Use posterdown or PowerPoint
2. Follow 3-column layout
3. Make figures large and clear
4. Include QR code to full paper
5. Get feedback from peers

### Exercise 3: Practice Delivery

Record yourself presenting:
1. Do full 15-minute talk
2. Watch recording critically
3. Note filler words, pacing issues
4. Identify unclear explanations
5. Re-record after improvements

### Exercise 4: Prepare Q&A

Anticipate 10 potential questions:
1. Methodological challenges
2. Alternative explanations
3. Limitations and concerns
4. Practical applications
5. Future directions

Write brief answers for each.

## Self-Check Questions

1. How many main messages should a 15-minute talk convey?
2. What's the 6×6 rule for slides?
3. What font size is minimum for poster body text?
4. How should you describe figures during presentations?
5. What should you do if you don't know the answer to a question?

## Presentation Checklist

Final preparation:

- [ ] Slides follow design principles
- [ ] All figures clearly labeled
- [ ] Text readable from back of room
- [ ] Practiced 3+ times with timer
- [ ] Anticipated Q&A prepared
- [ ] Technical setup tested
- [ ] Backup plan ready
- [ ] Contact information on slides
- [ ] Appropriate for audience level
- [ ] Within time limit

## Conclusion: Research Writing Journey

### What You've Accomplished

Over 14 weeks, you've learned to:

✅ **Structure** research following APA 7 guidelines
✅ **Review** literature systematically and synthesize findings
✅ **Formulate** testable research questions and hypotheses
✅ **Design** rigorous methodologies  
✅ **Collect** and document data with quality assurance
✅ **Analyze** data using appropriate statistical methods
✅ **Report** results objectively and completely
✅ **Interpret** findings in context of existing literature
✅ **Write** clear, concise, professional manuscripts
✅ **Cite** sources properly and manage references
✅ **Create** publication-quality figures and tables
✅ **Revise** systematically with peer feedback
✅ **Assemble** complete, submission-ready manuscripts
✅ **Present** research effectively to varied audiences

### Your Capstone Legacy

Your ANLY699 project represents:
- A contribution to knowledge in your field
- Evidence of your analytical capabilities
- A portfolio piece for your career
- Foundation for future research

### Continuing Your Research Journey

**Next steps**:

1. **Publish your work**
   - Conference presentations
   - Journal submissions
   - Blog posts or white papers

2. **Build on findings**
   - Address limitations in follow-up studies
   - Extend to new contexts
   - Collaborate with others

3. **Stay current**
   - Follow relevant journals
   - Attend conferences
   - Join professional organizations

4. **Share knowledge**
   - Mentor others
   - Teach workshops
   - Contribute to open science

### Final Thoughts

Research writing is a skill that improves with practice. Every paper you write will be better than the last. The systematic approach you've learned—from literature review through final presentation—will serve you throughout your career.

Your contribution matters. Data science research advances when practitioners like you document your work rigorously, share your findings openly, and build on each other's insights.

**Thank you for your dedication to this 14-week journey. Best wishes for your continued success in analytics and research!**

---

*Week 14 of 14 | ANLY699 Research Writing Tutorial - Complete!*

---

## Additional Resources

### Writing Resources
- APA Style Official Website: https://apastyle.apa.org
- Purdue OWL: https://owl.purdue.edu
- R Markdown: https://rmarkdown.rstudio.com

### R Packages for Research Writing
- `papaja`: APA manuscripts in R Markdown
- `apaTables`: APA-formatted tables
- `citr`: Citation management
- `knitr`, `kableExtra`: Tables
- `ggplot2`: Visualizations

### Communities
- R4DS Online Learning Community
- RStudio Community
- Stack Overflow (R tag)
- ResearchGate
- Twitter #RStats, #AcademicTwitter

### Continuous Learning
- DataCamp, Coursera courses
- R-bloggers
- Journal of Statistical Software
- PeerJ, PLOS ONE (open access journals)

**Keep learning. Keep writing. Keep contributing!**
