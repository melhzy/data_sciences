# ANLY 500 - Week 02 Lab Grading Rubric
**Assignment:** Introduction to Data Analytics 1 - HW2  
**Total Points:** 100  
**Passing Grade:** 70 (C)

---

## Part 1: Variables, Hypothesis, Designs (40 points)

Students answer conceptual questions based on the research abstract about offshore outsourcing.

| Question | Points | Grading Criteria |
|----------|--------|------------------|
| **1. Hypothesis** | 5 | Student identifies a clear, testable hypothesis related to outsourcing effects on cost savings, job creation, or economic impact. |
| **2. Independent Variable** | 3 | Student correctly identifies an IV (e.g., outsourcing location, where jobs are sent, country choice). |
| **2a. IV Type** | 2 | Student correctly classifies IV as **nominal** or **categorical**. Partial credit (1 pt) if mentioned but not explicitly stated. |
| **3. Dependent Variable** | 3 | Student correctly identifies a DV (e.g., cost savings, economic impact, job numbers, business success). |
| **3a. DV Type** | 2 | Student correctly classifies DV as **ratio**, **continuous**, or **interval**. Partial credit (1 pt) if mentioned but not explicitly stated. |
| **4. Measurement Error** | 5 | Student discusses potential sources of measurement error (e.g., currency conversion, reporting accuracy, calculation methods, self-report bias). |
| **5. Research Design Type** | 3 | Student identifies study as **observational**, **correlational**, **survey-based**, or **descriptive**. |
| **5a. Design Justification** | 2 | Student explains rationale (e.g., "no manipulation of variables," "uses existing data," "no random assignment"). Partial credit (1 pt) for brief/incomplete justification. |
| **6. Reliability Measurement** | 5 | Student explains how to assess DV reliability (e.g., test-retest reliability, internal consistency, Cronbach's alpha, repeated measurements). |
| **7. Ecological Validity** | 5 | Student assesses whether findings generalize to real-world settings and provides reasoning. |
| **8. Cause & Effect** | 3 | Student states whether causation can be claimed (answer should be "no" or "limited" for observational design). |
| **8a. Causation Rationale** | 2 | Student explains why causation cannot be established (e.g., "no manipulation," "confounding variables," "observational data"). Partial credit (1 pt) for incomplete explanation. |
| **9. Data Collection Type** | 3 | Student identifies collection method as **secondary data**, **archival data**, or **existing data**. |
| **TOTAL PART 1** | **40** | |

### Part 1 Grading Notes
- All questions require **written responses** demonstrating understanding of research methodology concepts
- No R coding required in Part 1
- Award partial credit for responses that show understanding but lack complete detail
- Deduct points for missing key terminology or incomplete reasoning

---

## Part 2: R Programming & Data Analysis (60 points)

Students perform statistical analysis using R on the `03_lab.csv` dataset containing outsourcing data.

| Question | Points | Type | Grading Criteria | Interpretation Required? |
|----------|--------|------|------------------|--------------------------|
| **1. Frequency Table** | 10 | Code | Student uses `table()` function to create frequency table of Jobs variable. Code must execute and produce valid output. | No |
| **2. Histograms** | 10 | Code | Student creates histograms for both Cost and Cost2 using `hist()` function with `breaks=15` parameter. **Deduct 3 pts if breaks parameter missing.** | No |
| **3a. Most Normal Distribution** | 5 | **Interpretation** | Student provides **written interpretation** identifying which cost savings variable appears most normal and explains why (e.g., "symmetric," "bell-shaped," "centered around mean"). | **YES - 50% penalty if missing** |
| **3b. Multimodal Distribution** | 5 | **Interpretation** | Student provides **written interpretation** identifying which variable is multimodal and explains why (e.g., "shows multiple peaks," "two distinct modes"). | **YES - 50% penalty if missing** |
| **3c. Skewed Distribution** | 5 | **Interpretation** | Student provides **written interpretation** identifying which variable is skewed, specifies direction (positive/negative or right/left), and explains (e.g., "long tail extending right"). | **YES - 50% penalty if missing** |
| **3d. Kurtotic Distribution** | 5 | **Interpretation** | Student provides **written interpretation** identifying which variable shows kurtosis and explains (e.g., "heavy tails," "peaked center," "leptokurtic"). | **YES - 50% penalty if missing** |
| **4. Z-score Calculation** | 10 | Code | Student uses `scale()` function or manual calculation `(x - mean(x)) / sd(x)` to compute z-scores for both cost savings variables. | No |
| **6. Extreme Values** | 10 | Code + Answer | Student identifies and counts values with z-scores beyond ±1.96 (p < .05). Must provide **numeric counts** for both variables. **Deduct 5 pts if counts not provided.** | No |
| **7. Min/Max Business IDs** | 10 | Code + Answer | Student identifies business IDs with highest and lowest cost savings using both cost columns. Must provide specific **ID numbers**. | No |
| **TOTAL PART 2** | **60** | | | |

### Part 2 Critical Grading Rule: 50% Penalty for Missing Interpretations

**Questions 3a-3d explicitly require written interpretations of histogram visualizations.**

#### Full Credit (5 points per question)
Student provides:
- ✅ Correct identification of the distribution
- ✅ Written explanation using appropriate statistical terminology
- ✅ Reference to visual features observed in the histogram

**Example:** *"Cost Savings 1 appears most normal because it displays a symmetric, bell-shaped distribution with data centered around the mean and no obvious skewness."*

#### 50% Penalty (2-3 points per question)
Student provides:
- ✅ Histogram code that executes correctly
- ✅ Visual output showing the distribution
- ❌ **NO written interpretation or explanation**

**Example:** *[Shows only code: `hist(data$Cost, breaks=15)` with graph output but no text explanation]*

#### Zero Credit (0 points)
- No code provided
- Code does not execute
- Interpretation is completely incorrect
- Question left blank

### Why the 50% Penalty?

Lab instructions state: **"Examine these histograms to answer the following questions:"**

This requires students to:
1. **Generate** visualizations (coding skill)
2. **Interpret** distributions (statistical literacy)
3. **Communicate** findings (scientific writing)

Simply showing a graph demonstrates only 1 of 3 competencies.

---

## Grade Scale

| Letter Grade | Point Range | Percentage |
|--------------|-------------|------------|
| **A** | 90-100 | 90-100% |
| **B** | 80-89 | 80-89% |
| **C** | 70-79 | 70-79% |
| **D** | 60-69 | 60-69% |
| **F** | 0-59 | Below 60% |

---

## Common Deductions

### Part 1
- **-1 to -2 pts:** Variable type not clearly stated (IV/DV classification)
- **-1 pt:** Design justification too brief ("because it's observational" without elaboration)
- **-3 pts:** Missing data collection type entirely
- **-5 pts:** No discussion of measurement error sources
- **-5 pts:** Missing reliability or ecological validity assessment

### Part 2
- **-3 pts:** Histogram missing `breaks=15` parameter
- **-2.5 to -3 pts per question:** Missing interpretation on Q3a-d (50% penalty)
- **-5 pts:** Code provided but extreme value counts not stated
- **-5 to -10 pts:** Code does not execute or produces errors
- **-10 pts:** Entire question missing (Q1, Q2, Q4, Q6, Q7)

---

## Grading Workflow

### Step 1: Verify Submission Format
- ✅ Submitted as Word document (.docx) or HTML
- ✅ Student name in author field
- ✅ Code chunks executed and showing output
- ✅ All questions addressed

### Step 2: Grade Part 1 (40 points)
- Read each written response
- Check for key concepts and terminology
- Award full, partial, or zero credit per question
- Note specific feedback for improvement

### Step 3: Grade Part 2 (60 points)
- Verify code executes and produces correct output
- For Q1, Q2, Q4, Q6, Q7: Award full credit if code/output present
- **For Q3a-d:** Check for written interpretations
  - Full credit: Interpretation present
  - 50% penalty: Code only, no interpretation
  - Zero credit: Nothing provided
- Check numeric answers are provided for Q6-Q7

### Step 4: Calculate Total & Letter Grade
- Sum Part 1 + Part 2 scores
- **Maximum:** Part 1 = 40, Part 2 = 60, Total = 100
- Assign letter grade per scale above

### Step 5: Provide Feedback
- List specific areas of strength
- Identify questions with missing interpretations
- Suggest improvements for future assignments

---

## Academic Integrity Note

Students may use:
- ✅ Course lecture materials and textbook
- ✅ R documentation and help files
- ✅ AI assistants for concept clarification (ChatGPT, Claude, Copilot)
- ✅ Discussion with classmates about general concepts

Students may NOT:
- ❌ Copy code directly from other students
- ❌ Submit work completed by another person
- ❌ Use solutions from previous semesters
- ❌ Plagiarize written explanations

**All sources must be properly cited in APA format.**

---

## Rubric Version
- **Version:** 1.0
- **Last Updated:** December 18, 2025
- **Course:** ANLY 500 Analytics I
- **Instructor:** Ziyuan Huang
