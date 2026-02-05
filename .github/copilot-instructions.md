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

## Development Environment

### R Environment (Primary - Required for Students)
- **Required IDE**: RStudio/Posit (students use free version)
- **Windows users**: Must install Rtools for package compilation
- **Code execution**: Must run chunk-by-chunk (students build incrementally while learning)
- **Core packages**: See "Core R Libraries by Course Week" section

### Python Environment (Optional - For Contributors Only)
Used only for textbook indexing script (`index_knowledge.py`):

**Setup with Conda (Recommended):**
```bash
conda env create -f environment.yml
conda activate data_sciences
```

**Or with pip:**
```bash
pip install -r requirements.txt
```

**Run textbook indexing:**
```bash
python index_knowledge.py
```

Outputs JSON summary of textbook headers and keyword locations to stdout.

**What the indexer extracts:**
- Section headers matching pattern `\d+(\.\d+)+\.?\s+Title` (e.g., "5.5.1. Outliers")
- Keyword occurrences: Data Screening, Accuracy, Missing Data, Outlier, Mahalanobis, MICE, MCAR, MNAR
- Line numbers and context snippets for each match
- Output: JSON with `headers_count`, `headers_sample`, `keywords_hits`, `keywords_locations`

## Student Workflow & Constraints

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

### Data & Plotting Errors
1. **Factor conversion missing** - Forgetting to convert categorical variables before plotting causes continuous scale issues (ggplot2 treats numeric 1, 2 as continuous)
2. **Absolute paths** - Using `"C:/Users/..."` instead of relative paths breaks on instructor's machine
3. **Raw variable names in labels** - Using `xlab("sales_total")` fails "professional graph" requirement (should be `"Total Sales Performance"`)
4. **Missing error bars** - Grouped mean comparisons require `stat_summary(fun.data = mean_cl_normal)` for 95% CI
5. **Forgetting cleanup theme** - Graphs without `+ cleanup` or `theme_bw()` look unprofessional
6. **Non-grayscale colors** - Using bright colors fails when printed in B&W; prefer black/grey palette

### R Markdown Workflow Errors
7. **Not knitting before submission** - Submitting uncompiled `.Rmd` = automatic zero credit
8. **Installing packages in chunks** - `install.packages()` should only run in Console, never in `.Rmd` code
9. **Running chunks out of order** - Students must execute sequentially from top; objects from later chunks don't exist yet
10. **Modifying YAML incorrectly** - Smart quotes or wrong indentation breaks knitting

### ggplot2 Troubleshooting
- **"object not found" in aes()**: Variable name misspelled or data not loaded with `import()`
- **Continuous scale when expecting discrete**: Forgot `factor()` conversion before plotting
- **Error bars don't align with bars**: Use `position = position_dodge(width = 0.90)` in both `geom_bar()` and `stat_summary()`
- **Legend shows "1, 2" instead of labels**: Factor conversion missing or wrong order in `levels =` argument
- **"stat_count() can only have an x or y aesthetic"**: Using `geom_bar()` without `stat = "summary"` for means
- **Blank plot with warnings**: Check that X and Y variables exist in dataset with exact spelling (`str(data)`)
- **Overlapping text in axis**: Add `theme(axis.text.x = element_text(angle = 45, hjust = 1))` for angled labels

## Publishing & Documentation

### GitHub Pages Workflow
- **Primary site**: `https://melhzy.github.io/data_sciences/` serves compiled HTML lectures
- **Alternative preview**: Use `htmlpreview.github.io/?<github-raw-url>` for direct rendering
- **Commit pattern**: Always commit both `.rmd` source AND `.html` output in same directory
- **No build automation**: HTML files are manually knitted in RStudio, then committed
- **Fallback**: `docs/` directory contains alternate static content (mirrors some `ANLY500-Analytics-I/` structure)

**Manual Publishing Steps:**
1. Open `.rmd` file in RStudio
2. Click "Knit" button (or run `rmarkdown::render("filename.rmd")`)
3. Verify HTML output displays correctly in browser
4. Git commit both `.rmd` and `.html` files together
5. Push to GitHub - Pages auto-deploys from main branch
6. Verify published content at `https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/WeekXX/filename.html`

### Textbook Integration
- **Source**: *Discovering Statistics Using R* (Field, Miles, Field 2012)
- **Location**: `ANLY500-Analytics-I/Knowledge/Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`
- **Indexing script**: `index_knowledge.py` (Python, standard library only)
  - **Purpose**: Extracts section headers and keyword locations for quick reference
  - **Section headers**: Regex `\d+(\.\d+)+\.?\s+Title` finds all numbered sections
  - **Keywords tracked**: Data Screening, Accuracy, Missing Data, Outlier, Mahalanobis, MICE, MCAR, MNAR
  - **Output format**: JSON with line numbers and content snippets
  - **Usage**: `python index_knowledge.py` (requires Python 3.7+, no external dependencies)
  - **Environment**: Use `conda env create -f environment.yml` or `pip install -r requirements.txt`

### Documentation Patterns
- **Week-level READMEs**: Overview of topics, links to materials, learning objectives
- **Enhancement docs**: Some weeks have `ENHANCEMENTS_SUMMARY.md` documenting major updates (see [Week07](ANLY500-Analytics-I/Week07/ENHANCEMENTS_SUMMARY.md))
- **Rubrics**: Some labs have separate `Rubric_WeekXX.md` grading criteria files
- **Analytics progression**: Course follows Descriptive → Predictive → Prescriptive sequence

**Creating Enhancement Documentation:**
When making substantial improvements to lectures, document:
- Visual additions (diagrams, plots, comparisons)
- New conceptual explanations
- Textbook references (Field et al. chapter/page numbers)
- Learning objective improvements
- See [ENHANCEMENTS_SUMMARY.md](ANLY500-Analytics-I/Week07/ENHANCEMENTS_SUMMARY.md) template with sections for each major addition

## File Naming Conventions
- **Lectures**: `##_topic.rmd` (lowercase extension, snake_case) - compiled to HTML for GitHub Pages
- **Labs**: `##_lab.Rmd` (uppercase extension, CamelCase) - compiled to Word for student submission
- **Data files**: `filename.csv` (lowercase, underscores) or `File Name.sav` (SPSS format)
- **Compiled output**: Same base name with `.html` (lectures) or `.docx` (labs) extension
- **Critical distinction**: `.rmd` = Slidy presentations, `.Rmd` = Word documents

### Quick Reference: File Extensions
| Extension | Purpose | Output Format | Location | YAML output |
|-----------|---------|---------------|----------|-------------|
| `.rmd` (lowercase) | Lecture slides | Slidy HTML | `WeekXX/*.rmd` | `slidy_presentation` |
| `.Rmd` (uppercase) | Student labs | Word .docx | `WeekXX/lab/*.Rmd` | `word_document` |

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
1. Open `.rmd` file in RStudio (lowercase extension)
2. Run chunks sequentially using Ctrl+Enter (Cmd+Enter on Mac)
3. Verify `data/` relative paths resolve from .rmd location
4. Check `pictures/` paths for `knitr::include_graphics()` calls
5. Knit to HTML using "Knit" button or `rmarkdown::render("filename.rmd")`
6. Open HTML in browser to verify slides display correctly
7. Commit both `.rmd` and `.html` to GitHub for Pages publishing

**Lab Testing Workflow:**
1. Open `.Rmd` file in RStudio from `lab/` subdirectory (uppercase extension)
2. Verify setup chunks execute: `library()` calls, `rio::import()` with correct paths
3. Test empty answer chunks have valid syntax: `{r q1}`, `{r question-2}`, etc.
4. Knit to Word using "Knit" button (RStudio automatically finds pandoc)
5. Open .docx file to review:
   - Heading hierarchy and formatting
   - Code chunk output visibility (`echo=TRUE` vs `echo=FALSE`)
   - Graph dimensions and clarity (default `fig.width=7, fig.height=5`)
   - Table formatting (if using `kable()` or `kableExtra`)
6. Test student workflow: Fill in one empty chunk, re-knit to verify isolation
7. Check that `author: "Enter Your Name"` prompts student customization

**Common Knitting Issues:**
- **"Pandoc not found"**: RStudio bundles pandoc; if standalone R, install pandoc separately
- **"Object not found"**: Chunks not run in order; click "Restart R and Run All Chunks"
- **Relative path errors**: Check working directory with `getwd()` matches `.Rmd` location
- **YAML parse errors**: Verify indentation (2 spaces, no tabs) and no smart quotes
- **Package loading fails**: Student needs to run `install.packages("pkgname")` in Console first

### Pre-Distribution Checklist
1. Factor conversion precedes all `ggplot()` calls
2. Relative paths correct for `.Rmd` location
3. Axis labels use Proper Case and explain variables
4. Error bars present for grouped mean comparisons
5. `cleanup` theme or `theme_bw()` applied
6. Print-friendly colors (grayscale) used

## Common Development Workflows

### Adding New Week Content to ANLY500
1. **Create week directory**: `mkdir ANLY500-Analytics-I/WeekXX`
2. **Create subdirectories**: `mkdir data lab pictures`
3. **Create lecture file**: `WeekXX/##_topic.rmd` (lowercase .rmd)
4. **Create lab file**: `WeekXX/lab/##_lab.Rmd` (uppercase .Rmd)
5. **Add datasets**: Place in `data/` with descriptive names
6. **Add README.md**: Document learning objectives, topics, dataset sources
7. **Test workflow**: Run chunks sequentially, knit both files, verify paths
8. **Commit pattern**: `git add WeekXX/*.{rmd,html} WeekXX/lab/*.Rmd WeekXX/data/* WeekXX/pictures/*`

### Updating Existing Lecture with Visualizations
**Pattern from [Week07](ANLY500-Analytics-I/Week07/ENHANCEMENTS_SUMMARY.md):**
1. **Identify enhancement areas**: Concepts needing visual explanation
2. **Create R code for visuals**: Use `par(mfrow=c(2,3))` for multi-panel comparisons
3. **Add textbook references**: Cite Field et al. chapter/page numbers in comments
4. **Document changes**: Create/update `ENHANCEMENTS_SUMMARY.md` with:
   - Overview of what was added
   - Numbered list of major enhancements with ⭐ NEW markers
   - Purpose and key features for each addition
   - Textbook reference citations
5. **Test render**: Knit to HTML, verify all plots display correctly
6. **Commit together**: Source `.rmd`, compiled `.html`, and `ENHANCEMENTS_SUMMARY.md`

### Running Textbook Indexing Script
**When to use:** After updating textbook content or adding new keyword tracking.
```powershell
# Activate conda environment (Windows)
conda activate data_sciences

# Run indexer from repository root
python index_knowledge.py

# Output shows:
# - headers_count: Total numbered sections found
# - headers_sample: First 10 section headers
# - keywords_hits: Count per keyword
# - keywords_locations: Line numbers with context for first 5 hits per keyword
```

### Publishing Lecture Updates to GitHub Pages
```powershell
# 1. Open lecture in RStudio, make edits to .rmd
# 2. Knit to HTML (Ctrl+Shift+K or click "Knit" button)
# 3. Verify output in browser
# 4. Stage both files
git add ANLY500-Analytics-I/WeekXX/##_topic.rmd
git add ANLY500-Analytics-I/WeekXX/##_topic.html

# 5. Commit with descriptive message
git commit -m "Week XX: Add visualization for [concept]"

# 6. Push to trigger GitHub Pages deployment
git push origin main

# 7. Verify live at: https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/WeekXX/##_topic.html
```

### Creating Lab Assignment with Data
**Standard pattern from Week05 lab:**
1. **Prepare dataset**: `05_data.csv` in `lab/` directory with clear variable names
2. **Create lab stub**: `05_lab.Rmd` with YAML `author: "Enter Your Name"`
3. **Add machine-info chunk**: Required first chunk for reproducibility tracking
4. **Create setup chunk**: Load libraries (`rio`, `ggplot2`), import data, factor variables
5. **Add hidden data exploration**: `echo=FALSE` chunk with base R plots for instructor verification
6. **Define cleanup theme**: Include standard theme code for students to use
7. **Write questions**: Empty chunks `{r q1}`, `{r q2}`, etc. with instructions above each
8. **Document assessment criteria**: List graph requirements (labels, error bars, legend, theme)
9. **Test student workflow**: Fill one chunk, knit to Word, verify isolation
10. **Create rubric** (optional): `Rubric_WeekXX.md` with point allocations

## Key Datasets by Week
- **Week 1**: `lab_R_learning.csv`, built-in `airquality`
- **Week 5**: `ChickFlick.sav` (gender × film interaction), `Exam Anxiety.csv` (scatterplots), `festival.csv` (histograms), `Jiminy Cricket.csv` (wide→long example)

## Research Writing (ANLY699)

### Course Structure
APA 7th edition standards enforced throughout. 14-week progression covering:

**Phase 1 (Weeks 1-3)**: Foundation → Literature Review → Research Questions  
**Phase 2 (Weeks 4-6)**: Methodology → Data Collection → Statistical Analysis  
**Phase 3 (Weeks 7-8)**: Results Section → Discussion Section  
**Phase 4 (Weeks 9-14)**: Abstract/Introduction → Citations → Figures/Tables → Revision → Final Draft → Presentation

### Key Resources
- **APA 7 samples**: `APA7/apa-7-{student|professional}-sample-paper-2025-revision.pdf`
- **Methodology guides**: `Scientific Research and Methodology.pdf`, `Introduction to Research Statistical Analysis.pdf`
- **Research design**: `Develop_a_Research_Question.pdf`, `Research Questions.pdf`
- **AI integration**: `AI4Research.pdf` (appropriate use of AI tools in research)

### Writing Standards
- **Font**: Times New Roman 12pt for papers
- **Spacing**: Double-spaced with 1" margins
- **Citations**: APA 7th edition in-text and reference list
- **Sections**: Follow IMRaD structure (Introduction, Method, Results, and Discussion)
- **Figures/Tables**: APA-formatted with proper captions and notes
- **Academic integrity**: AI tools allowed for concept understanding, not direct content generation

### Tutorial Files
Each `WeekXX-Topic/README.md` contains:
- Learning objectives for the week
- Step-by-step writing guidance
- Examples from APA sample papers
- Common mistakes to avoid
- Checklists for section completion

Central guide: [RESEARCH_WRITING_GUIDE.md](ANLY699-Applied-Project/RESEARCH_WRITING_GUIDE.md)

**Tutorial Structure Pattern:**
- **Phase 1 (Weeks 1-3)**: Foundation → Literature Review → Research Questions
- **Phase 2 (Weeks 4-6)**: Methodology → Data Collection → Statistical Analysis
- **Phase 3 (Weeks 7-8)**: Results Section → Discussion Section
- **Phase 4 (Weeks 9-14)**: Abstract/Introduction → Citations → Figures/Tables → Revision → Final Draft → Presentation
