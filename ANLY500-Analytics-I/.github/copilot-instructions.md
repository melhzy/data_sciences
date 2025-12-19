# ANLY500 Analytics Course Repository

## Project Overview
This is an **educational statistics and data analytics course repository** taught using R and R Markdown. The course covers 14 weeks of content, progressing from R basics through statistical concepts, visualization, and culminating in a final research project. The repository contains lecture materials, lab assignments, and datasets for teaching Principles of Analytics I at Harrisburg University.

## Repository Structure
```
ANLY500-Analytics-I/
├── Week01-Week05/     # Weekly lecture materials (more weeks exist)
│   ├── *.rmd          # Lecture presentations (slidy_presentation)
│   ├── *.html         # Compiled HTML output (published via GitHub Pages)
│   ├── lab/*.Rmd      # Student lab assignments (word_document output)
│   ├── lab/*.csv      # Lab-specific datasets
│   ├── data/*.{csv,sav,xlsx}  # Lecture example datasets
│   └── pictures/      # Images for lecture slides
├── Knowledge/         # Course textbook (Discovering Statistics Using R - Field et al. 2012)
└── archive/          # Historical/backup materials
```

## Key R Markdown Patterns

### Output Format Conventions
- **Lecture materials** (.rmd in WeekXX/): Use `slidy_presentation` with `incremental: true`
- **Lab assignments** (.Rmd in WeekXX/lab/): Use `word_document` with `reference_docx: default`
- **Tutorials**: Use `html_document` with floating TOC, theme: cosmo, code_folding: show

### Standard YAML Header for Labs
```yaml
---
title: "Lab Title"
author: "Enter Your Name"  # Student fills this in
date: "`r Sys.Date()`"     # Auto-generates current date
output: 
  word_document:
    reference_docx: default
---
```

### Mandatory Setup Pattern for All Documents
Every .Rmd file should include a machine info chunk at the top (for reproducibility tracking):
```r
```{r machine-info, echo=FALSE, results='asis'}
cat("**Machine:**", paste0(Sys.info()['nodename'], " - ", Sys.info()['sysname'], " ", Sys.info()['release']), "\n\n")
```
```

### Data Import Convention
Always use **relative paths** from the .Rmd file location with `rio::import()`:
```r
library(rio)
dataset <- import("data/filename.csv")      # From WeekXX/*.rmd
dataset <- import("05_data.csv")            # From WeekXX/lab/*.Rmd
dataset <- import("../data/filename.sav")   # Lab accessing parent folder data
```
**Critical**: `rio` handles multiple formats (.csv, .sav SPSS, .xlsx) automatically. Never use `read.csv()` directly.

### Factor Conversion (Required Before ggplot2)
Categorical variables from datasets **must** be converted to factors before plotting:
```r
data$variable <- factor(data$variable,
                       levels = c(1, 2),               # Existing numeric codes
                       labels = c("Label1", "Label2")) # Display labels for graphs
```
This is especially critical for SPSS .sav files which store categories as numeric codes.

## Data Visualization Standards (ggplot2)

### Code Stacking Pattern (Mandatory Style)
Always build ggplot2 objects incrementally using `+` across multiple lines for readability:
```r
plotobject <- ggplot(data, aes(x = xvar, y = yvar, color = group, fill = group))
plotobject +
  geom_point() +                              # Geometry layer
  stat_summary(fun = mean, geom = "bar") +    # Statistical transformation
  stat_summary(fun.data = mean_cl_normal,     # 95% confidence interval error bars
               geom = "errorbar",
               width = .2) +
  xlab("Professional X Axis Label") +         # No raw variable names
  ylab("Professional Y Axis Label") +
  cleanup +                                   # Reusable custom theme
  scale_color_manual(name = "Legend Title",
                    labels = c("Group A", "Group B"),
                    values = c("black", "grey"))
```

### Reusable "cleanup" Theme
Define this custom theme object once at the start of any visualization document:
```r
cleanup <- theme(panel.grid.major = element_blank(),
                panel.grid.minor = element_blank(),
                panel.background = element_blank(),
                axis.line.x = element_line(color = 'black'),
                axis.line.y = element_line(color = 'black'),
                legend.key = element_rect(fill = 'white'),
                text = element_text(size = 15))
```
Then apply with `+ cleanup` to any ggplot object for professional publication-ready styling.

### Professional Graphing Requirements (Lab Grading Criteria)
All student graphs must include:
1. **Proper Case axis labels** - No raw variable names (e.g., "Sales Performance" not "sales_score")
2. **Error bars** - Use `stat_summary(fun.data = mean_cl_normal)` for grouped comparisons
3. **Legend customization** - Use `scale_*_manual(name = , labels = )` to replace defaults
4. **Print-friendly colors** - Prefer grayscale (graphs are printed in B&W): black, grey, darkgrey
5. **Clean theme** - Apply `cleanup` theme or use `theme_bw()`/`theme_classic()`

### Data Restructuring for ggplot2
**Wide to Long Format** using `reshape::melt()` (required for repeated measures visualizations):
```r
library(reshape)  # Note: modern alternative is tidyr::pivot_longer()
longdata <- melt(widedata,
                 id = c("participant_id", "group"),     # Constant columns
                 measured = c("time1", "time2", "time3"))  # Columns to stack
colnames(longdata)[3:4] <- c("Timepoint", "Score")  # Rename generic "variable" and "value"
```

## Core R Libraries by Week

### Weeks 1-2: R Basics & Descriptive Analytics
- `tidyverse`, `ggplot2`, `dplyr` - Data manipulation and visualization
- `knitr`, `kableExtra` - Table formatting in R Markdown
- `seedhash` - Reproducible random seed generation (custom package)

### Week 3: Statistical Distributions
- `moments` - Skewness and kurtosis calculations
- `psych` - Descriptive statistics (`describe()` function)
- `pastecs` - Statistical summaries (`stat.desc()`)
- `Hmisc` - Additional statistics and error bar calculations
- `corrplot` - Correlation matrix visualizations

### Week 4: Statistical Models
- `dplyr`, `tidyr` - Advanced data manipulation
- `MOTE`, `effectsize` - Effect size calculations

### Week 5: Data Visualization
- `ggplot2` - Core plotting (mandatory for all graphs)
- `rio` - Universal data import (handles .csv, .sav, .xlsx)
- `reshape` - Wide-to-long format conversion
- `GGally` - Extended visualizations (scatterplot matrices via `ggpairs()`)
- `Hmisc` - Error bar statistics (`mean_cl_normal` function)

## Educational Context & Workflow

### Student Development Environment
- **Primary IDE**: RStudio/Posit (required for students)
- **Windows users**: Must install Rtools for package compilation
- **Course delivery**: Fully online, self-directed with instructor support

### Assignment Submission Requirements
- Labs must be **knitted to Word** documents (uncompiled .Rmd files not graded)
- Students modify `author: "Enter Your Name"` field with their actual names
- Code must run **chunk-by-chunk** (students build incrementally while learning)

### Final Project Structure (Week 4-14 Timeline)
- **Week 4**: Students submit 2-page proposal (APA format, Times New Roman 12pt)
- **Data source**: UCI Machine Learning Repository (https://archive.ics.uci.edu/datasets)
- **Format**: Individual projects only (no teams)
- **Requirements**: Cover page, 2 pages content, references; address problem statement, data needs, methods, evaluation metrics, deliverables

### Publishing Workflow
- Lecture HTML files are published via **GitHub Pages** at `https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/`
- Alternative viewer: htmlpreview.github.io for direct repo file rendering

## Common Data Patterns

### Dataset Types by Source
- **SPSS files (.sav)**: Numeric category codes (1, 2) → require factor labels before plotting
- **Wide format**: Repeated measures as separate columns → needs `melt()` before ggplot2
- **Missing values**: Common in datasets like festival.csv → handle with `na.rm = TRUE` or `na.omit()`
- **Mixed designs**: Multiple independent variables (between + within subjects) → careful aesthetics setup

### Example Datasets by Week
- Week 1: `lab_R_learning.csv`, built-in `airquality`
- Week 5: `ChickFlick.sav` (gender × film interaction), `Exam Anxiety.csv` (scatterplots), `festival.csv` (histograms), `Jiminy Cricket.csv` (wide→long example)

## Best Practices When Editing Code

### For Lecture Materials (.rmd files)
- Maintain `slidy_presentation` format with `incremental: true` for progressive reveal
- Keep code examples concise and fully executable
- Include visual examples via `knitr::include_graphics("pictures/image.png")`
- Use `fig.align='center'` and set appropriate `fig.width`/`fig.height` in chunks

### For Lab Assignments (lab/*.Rmd files)
- Leave empty code chunks `{r q1}` for students to fill in
- Provide clear instructions above each question
- Include assessment criteria explicitly in lab description
- Test that any starter code runs successfully before distribution
- Verify relative paths match the lab/ subdirectory location

### Code Verification Checklist
1. **Factor conversion** happens before any `ggplot()` call
2. **Relative paths** are correct for the .Rmd file's actual location
3. **Axis labels** use Proper Case and explain the variable (not raw names)
4. **Error bars** present for any grouped mean comparisons
5. **cleanup theme** or `theme_bw()` applied for publication quality
6. **Print-friendly colors** used (grayscale preference for B&W printing)

## Conceptual Foundation

### Course Philosophy (Field et al. 2012 Text)
- Emphasizes understanding **why** statistical methods work, not just mechanical application
- Critical focus on **measurement levels** (nominal, ordinal, interval, ratio) - determines valid statistical tests
- **Reproducibility**: Machine info tracking, seed generation for random processes
- **Professional standards**: All output should be publication-ready for academic journals

### Analytics Progression (Weeks 1-14)
1. **Descriptive Analytics**: What happened? (histograms, summary stats, distributions)
2. **Predictive Analytics**: What could happen? (correlation, regression, modeling)
3. **Prescriptive Analytics**: What should we do? (optimization, decision support)

## When Assisting Students

### Common Student Errors to Watch For
- Forgetting to factor categorical variables before plotting (results in continuous scale issues)
- Using absolute paths instead of relative paths (breaks on instructor's machine)
- Raw variable names in axis labels (fails "professional graph" requirement)
- Missing error bars on grouped comparisons (required for academic standards)
- Not knitting to Word before submission (uncompiled .Rmd files get zero credit)
- Installing packages inside .Rmd files (should be done in console, not document)

### Academic Integrity Expectations
- Students should complete work individually unless explicitly stated otherwise
- AI assistants (ChatGPT, Claude, Copilot) are allowed for understanding concepts
- Direct copying from online sources or other students results in zero credit
- All sources must be properly referenced (APA style preferred)
- Honor Code: "We pledge not to cheat, plagiarize, steal, or lie in matters related to academic work"

## Technical Notes

- `.vscode/settings.json` references conda/Python config (may be for instructor's broader data science workspace - this course is R-focused)
- Week05 contains a `.github/copilot-instructions.md` specific to that week's visualization module (more detailed than needed for repo-level guidance)
- R version flexibility expected across student machines - code should be version-agnostic where possible
- Windows vs. Mac path handling: use `/` in relative paths, avoid hardcoded absolute paths
