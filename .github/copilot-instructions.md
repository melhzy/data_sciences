# Data Sciences Teaching Repository

## Project Context
Educational repository for **Harrisburg University analytics courses** combining R-based statistical instruction (ANLY500) with research methodology training (ANLY699). Content is published via GitHub Pages at `https://melhzy.github.io/data_sciences/`. Repository supports self-directed online learning with instructor support.

## Repository Structure
```
data_sciences/
├── ANLY500-Analytics-I/          # 14-week R & statistics course
│   ├── WeekXX/                   # Weekly lecture materials
│   │   ├── *.rmd                 # Slidy presentations (lectures)
│   │   ├── *.html                # Published HTML (GitHub Pages)
│   │   ├── lab/*.Rmd             # Student assignments (Word output)
│   │   ├── data/*.{csv,sav}      # Example datasets
│   │   └── pictures/             # Lecture images
│   └── Knowledge/                # Textbook (Field et al. 2012)
│       └── *.txt                 # Normalized textbook for indexing
├── ANLY699-Applied-Project/      # Capstone research project
│   ├── WeekXX-Topic/             # 14-week research writing guide
│   ├── APA7/                     # APA 7th edition resources (PDFs)
│   └── RESEARCH_WRITING_GUIDE.md # 14-week tutorial overview
├── docs/                         # Alternate GitHub Pages content
└── index_knowledge.py            # Python script for textbook indexing
```

**Key Directory Patterns:**
- **Lectures**: `WeekXX/*.rmd` (lowercase extension) with HTML output in same directory
- **Labs**: `WeekXX/lab/*.Rmd` (uppercase extension) for student Word documents
- **Data files**: Always in `data/` subdirectory (lectures) or lab root (assignments)
- **Images**: `pictures/` subdirectory for lecture graphics

## R Markdown Standards

### Output Format by File Type
- **Lectures** (`WeekXX/*.rmd`): `slidy_presentation` with `incremental: true`
- **Labs** (`WeekXX/lab/*.Rmd`): `word_document` with `reference_docx: default`
- **Author field**: Labs use `"Enter Your Name"` (students fill in)
- **Date**: Always `` `r Sys.Date()` `` (auto-generated)

### Mandatory Setup Chunks
Every `.Rmd` requires machine info tracking for reproducibility:
```r
```{r machine-info, echo=FALSE, results='asis'}
cat("**Machine:**", paste0(Sys.info()['nodename'], " - ", Sys.info()['sysname'], " ", Sys.info()['release']), "\n\n")
```
```

**Standard Chunk Options for Lectures:**
- `echo=TRUE` - Show code in presentation
- `message=FALSE, warning=FALSE` - Suppress package loading messages
- `fig.width=8.4, fig.height=8.4, fig.align='center'` - Standard figure dimensions
- `eval=FALSE` - Show code without executing (for examples)
- `knitr::include_graphics("pictures/image.png")` - Include external images

### Data Import Pattern
Always use **relative paths** with `rio::import()` (handles CSV, SPSS .sav, XLSX):
```r
library(rio)
dataset <- import("data/filename.csv")    # From WeekXX/*.rmd
dataset <- import("05_data.csv")          # From WeekXX/lab/*.Rmd
dataset <- import("../data/file.sav")     # Lab accessing parent data/
```
Never use `read.csv()` directly - `rio` is the standard for multi-format imports.

## ggplot2 Visualization Conventions

### Required "cleanup" Theme
Define once at document start, apply universally for publication-ready graphs:
```r
cleanup <- theme(panel.grid.major = element_blank(),
                panel.grid.minor = element_blank(),
                panel.background = element_blank(),
                axis.line.x = element_line(color = 'black'),
                axis.line.y = element_line(color = 'black'),
                legend.key = element_rect(fill = 'white'),
                text = element_text(size = 15))
```

### Code Stacking Pattern (Mandatory Style)
Build plots incrementally across multiple lines:
```r
plotobject <- ggplot(data, aes(x = xvar, y = yvar, color = group, fill = group))
plotobject +
  geom_bar(stat = "summary", fun = mean) +
  stat_summary(fun.data = mean_cl_normal,    # 95% CI error bars
               geom = "errorbar", width = .2) +
  xlab("Professional X Axis Label") +        # No raw variable names
  ylab("Dependent Variable (Units)") +
  cleanup +                                  # Apply custom theme
  scale_color_manual(name = "Group Type",
                    labels = c("Control", "Treatment"),
                    values = c("black", "grey"))  # Grayscale for printing
```

### Professional Graph Requirements (Grading Criteria)
Labs are graded on these visualization standards:
1. **Proper Case axis labels** - Explain variables, not raw names (`sales_total` → `"Total Sales Performance"`)
2. **Error bars required** - Use `stat_summary(fun.data = mean_cl_normal)` for grouped means
3. **Legend customization** - Use `scale_*_manual(name = , labels = )` with descriptive text
4. **Print-friendly colors** - Prefer grayscale (black/grey) as graphs print in B&W
5. **Clean theme** - Apply `cleanup` or `theme_bw()`/`theme_classic()`

### Factor Conversion (Critical Before Plotting)
Categorical variables **must** be factored before ggplot2, especially SPSS .sav numeric codes:
```r
data$variable <- factor(data$variable,
                       levels = c(1, 2),
                       labels = c("Control", "Treatment"))
```

### Wide-to-Long Transformation
Repeated measures data requires reshaping for ggplot2:
```r
library(reshape)  # Legacy package used in course materials
longdata <- melt(widedata,
                 id = c("participant_id", "group"),
                 measured = c("time1", "time2", "time3"))
colnames(longdata)[3:4] <- c("Timepoint", "Score")

# Modern alternative (tidyr - not used in course, but acceptable):
# library(tidyr)
# longdata <- pivot_longer(widedata, 
#                          cols = c(time1, time2, time3),
#                          names_to = "Timepoint", 
#                          values_to = "Score")
```

## Core R Libraries by Course Week
- **Week 1-2**: `tidyverse`, `ggplot2`, `dplyr`, `knitr`, `kableExtra`
- **Week 3**: `moments`, `psych`, `pastecs`, `Hmisc`, `corrplot`
- **Week 5**: `rio`, `reshape`, `GGally`, `Hmisc` (for `mean_cl_normal`)
- **Week 6+**: `effectsize`, `MOTE`

## Student Workflow & Constraints

### Development Environment
- **Required IDE**: RStudio/Posit (students use free version)
- **Windows users**: Must install Rtools for package compilation
- **Code execution**: Must run chunk-by-chunk (students build incrementally while learning)

### Assignment Submission Rules
- Labs must be **knitted to Word** before submission (uncompiled .Rmd = zero credit)
- Students modify `author: "Enter Your Name"` with actual names
- All code must execute successfully in isolated chunks
- Relative paths must work from the `.Rmd` file's actual directory location

### Final Project Timeline (ANLY500)
- **Week 4**: 2-page proposal submission (APA format, Times New Roman 12pt)
- **Data source**: UCI Machine Learning Repository
- **Format**: Individual projects only (no teams allowed)
- **Requirements**: Cover page, 2 pages content, references page; address problem statement, data needs, methods, evaluation metrics, deliverables

## Academic Integrity Expectations
- Students complete work individually unless explicitly stated otherwise
- AI assistants (ChatGPT, Claude, Copilot) **allowed for concept understanding**
- Direct copying from online sources or other students = zero credit
- All sources must be APA-referenced
- Honor Code: "We pledge not to cheat, plagiarize, steal, or lie in matters related to academic work"

## Common Student Errors to Prevent
1. Forgetting factor conversion before plotting (causes continuous scale issues)
2. Using absolute paths instead of relative paths (breaks on instructor's machine)
3. Raw variable names in axis labels (fails "professional graph" requirement)
4. Missing error bars on grouped mean comparisons
5. Not knitting to Word before submission
6. Installing packages inside `.Rmd` files (should be done in console only)

## Publishing & Documentation
- Lecture HTML published via GitHub Pages at `https://melhzy.github.io/data_sciences/`
- Alternative HTML preview: `htmlpreview.github.io` for direct repo file rendering
- HTML files committed alongside `.rmd` sources in same directory
- Course textbook: *Discovering Statistics Using R* (Field, Miles, Field 2012)
- Textbook normalized to `.txt` format in `Knowledge/` folder for text indexing
- `index_knowledge.py`: Python utility for indexing textbook sections and keywords (headers, Data Screening, MICE, MCAR, MNAR, etc.)
- Analytics progression: Descriptive → Predictive → Prescriptive

## File Naming Conventions
- **Lectures**: `##_topic.rmd` (lowercase extension, snake_case) - compiled to HTML for GitHub Pages
- **Labs**: `##_lab.Rmd` (uppercase extension, CamelCase) - compiled to Word for student submission
- **Data files**: `filename.csv` (lowercase, underscores) or `File Name.sav` (SPSS format)
- **Compiled output**: Same base name with `.html` (lectures) or `.docx` (labs) extension
- **Critical distinction**: `.rmd` = Slidy presentations, `.Rmd` = Word documents

## When Editing Course Materials

### For Lectures (WeekXX/*.rmd)
- Maintain `slidy_presentation` format with `incremental: true`
- Keep code examples concise and fully executable
- Use `knitr::include_graphics("pictures/image.png")` for visuals
- Set appropriate `fig.width`, `fig.height`, `fig.align='center'` in chunks
- Test by knitting to HTML in RStudio using "Knit" button or `rmarkdown::render()`

### For Labs (WeekXX/lab/*.Rmd)
- Leave empty code chunks `{r q##}` for student completion
- Provide clear instructions above each question
- Include explicit assessment criteria in lab description
- Test all starter code runs successfully before distribution
- Verify relative paths match lab/ subdirectory location
- Knit to Word using "Knit" button to verify output formatting

### Testing Course Materials
**Lecture Testing Workflow:**
1. Open `.rmd` file in RStudio
2. Run chunks sequentially to verify code execution
3. Check that `data/` paths resolve correctly
4. Knit to HTML: `rmarkdown::render("filename.rmd")`
5. Verify HTML displays correctly in browser
6. Commit both `.rmd` and `.html` files to GitHub

**Lab Testing Workflow:**
1. Open `.Rmd` file in RStudio from `lab/` directory
2. Verify all setup chunks execute (library loads, data import)
3. Test empty answer chunks have proper syntax `{r q##}`
4. Knit to Word: Click "Knit" button in RStudio
5. Review Word document formatting (headings, code output, graphs)
6. Check that students can fill in empty chunks and re-knit successfully

### Pre-Distribution Checklist
1. Factor conversion precedes all `ggplot()` calls
2. Relative paths correct for `.Rmd` location
3. Axis labels use Proper Case and explain variables
4. Error bars present for grouped mean comparisons
5. `cleanup` theme or `theme_bw()` applied
6. Print-friendly colors (grayscale) used

## Key Datasets by Week
- **Week 1**: `lab_R_learning.csv`, built-in `airquality`
- **Week 5**: `ChickFlick.sav` (gender × film interaction), `Exam Anxiety.csv` (scatterplots), `festival.csv` (histograms), `Jiminy Cricket.csv` (wide→long example)

## Research Writing (ANLY699)
APA 7th edition standards enforced throughout. 14-week progression: Foundation → Literature Review → Research Questions → Methodology → Data Collection → Analysis → Results → Discussion → Abstract/Introduction → Citations → Figures/Tables → Revision → Final Draft → Presentation. All resources in `ANLY699-Applied-Project/APA7/` folder.
