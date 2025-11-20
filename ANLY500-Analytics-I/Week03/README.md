# Week 03: Data Wrangling, EDA, and Basic Inference

## Lecture Materials

### Viewing the Presentations

This week has one HTML presentation and one hands-on R tutorial:

#### 1. Introduction to Data Analytics II (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week03/03_introDA_2.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week03/03_introDA_2.html)

**Option 3: Download and Open Locally**
- Download `03_introDA_2.html` and open in your web browser

#### 2. R for Data Analytics (Week 03 Hands-on Tutorial)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week03/03_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `03_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week builds on Week 02 and focuses on practical analytics workflows:

### Lecture Topics
- Tidy data principles and pipelines
- Data import/export (CSV, Excel)
- Data wrangling with dplyr
- Missing data and basic cleaning
- Joins and reshaping (pivoting)
- Exploratory Data Analysis (EDA)
- Basic statistical inference (t tests, proportions)

### R Tutorial Topics
- Importing and cleaning data with `readr`, `janitor`, `skimr`
- Core dplyr verbs: `filter`, `select`, `mutate`, `summarise`, `group_by`
- Derived features and categorical bucketing
- Safe joins: `left_join`, `inner_join`, `anti_join`
- Reshaping data: `pivot_longer`, `pivot_wider`
- EDA visuals in `ggplot2` (histograms, scatter, grouped bars with SE)
- One-sample and two-sample t tests; proportion tests

---

## Materials

- **Lecture Slides**: `03_introDA_2.rmd` → `03_introDA_2.html` (Slidy presentation)
- **R Tutorial**: `03_R_for_DataAnalytics.rmd` → `03_R_for_DataAnalytics.html` (Interactive tutorial)
- **Lab Assignment**: `lab/` folder
- **Images**: `pictures/` folder (lecture graphics)

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
	- Chapter 3–4: Exploring data, cleaning, assumptions
	- Chapter 9: Comparing two means (t tests)
  
	Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

---

## Learning Path

### Step 1: Theory
1. Review the Week 03 lecture (`03_introDA_2.html`)
2. Revisit tidy data and data quality concepts
3. Understand when to use joins and reshaping

### Step 2: Practice
1. Work through `03_R_for_DataAnalytics.html`
2. Replicate the wrangling and EDA examples
3. Run the t tests on your own small dataset

### Step 3: Apply
1. Complete the lab in `lab/`
2. Perform EDA on a dataset of your choice
3. Write H0/H1 and run one inferential test

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "readr", "readxl", "janitor", "skimr", "kableExtra"))
install.packages("seedhash")  # For reproducible analysis
```

### Recommended Software
- **R**: Version 4.5.2 or higher
- **RStudio/Posit**: Latest version
- **VS Code**: With R extension (alternative)

---

## Quick Links

- [← Week 02 Materials](../Week02/README.md)
- [Back to Course Home](../README.md)

---

<div align="center">

**ANLY 500 - Analytics I**  
*Georgetown University*

Last Updated: `r format(Sys.Date(), '%B %d, %Y')`

</div>
