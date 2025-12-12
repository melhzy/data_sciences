# R Markdown Data Visualization Project - Week 05

## Project Overview
This is an **educational R project** focused on data visualization using `ggplot2` and R Markdown. The project consists of lecture materials (presentation slides) and lab assignments for teaching statistical graphics to analytics students.

## Key Technologies & Libraries
- **R Markdown** (.Rmd files) - Primary format for all documents
- **ggplot2** - Core visualization library
- **rio** - Universal data import (handles SPSS .sav, CSV, XLSX)
- **reshape** - Data restructuring (wide ↔ long format transformations)
- **GGally** - Extended ggplot2 visualizations (scatterplot matrices)
- **Hmisc** - Statistical summaries for error bars

## File Structure & Purpose
```
Week05/
├── 05_graphs.rmd          # Main lecture presentation (slidy_presentation)
├── lab/
│   ├── 05_lab.Rmd         # Student lab assignment template (outputs to Word)
│   └── 05_data.csv        # Lab dataset (business marketing study)
└── data/                  # Lecture example datasets
    ├── ChickFlick.sav     # SPSS format: gender × film interaction
    ├── Exam Anxiety.csv   # Scatterplot examples with anxiety/performance
    ├── festival.csv       # Histogram examples (hygiene over time)
    ├── Hiccups.csv        # Line graph with repeated measures
    ├── Jiminy Cricket.csv # Wide→long transformation example
    └── Texting.xlsx       # Excel format: 2×2 mixed design
```

## Critical R Markdown Patterns

### Data Import Convention
Always use relative paths from the .Rmd file location with `rio::import()`:
```r
library(rio)
dataset <- import("data/filename.csv")  # From root-level .Rmd
dataset <- import("05_data.csv")        # From lab/ subdirectory .Rmd
```

### Factor Conversion (Required Before Plotting)
Categorical variables **must** be converted to factors for proper ggplot2 behavior:
```r
data$variable <- factor(data$variable,
                       levels = c(1, 2),
                       labels = c("Label1", "Label2"))
```

### Data Restructuring for ggplot2
**Wide to Long Format** using `reshape::melt()`:
```r
longdata <- melt(widedata,
                 id = c("participant_vars"),      # Columns to keep constant
                 measured = c("timepoint_vars"))  # Columns to stack
colnames(longdata) <- c("NewName1", "NewName2")  # Rename generic outputs
```

### Standard ggplot2 Workflow (Code Stacking Pattern)
Always build plots in layers using the `+` operator across multiple lines:
```r
plotobject <- ggplot(data, aes(x, y, color = group, fill = group))
plotobject +
  geom_*() +                              # Geometric layer
  stat_summary(fun = mean, geom = "bar") +  # Statistical transformation
  stat_summary(fun.data = mean_cl_normal,   # Error bars
               geom = "errorbar",
               width = .2) +
  xlab("Professional X Label") +
  ylab("Professional Y Label") +
  cleanup +                               # Custom theme (see below)
  scale_color_manual(name = "Legend Title",
                    labels = c("Label1", "Label2"),
                    values = c("color1", "color2"))
```

### Custom Theme (Reusable "cleanup" Object)
Define once at the start, reuse everywhere:
```r
cleanup <- theme(panel.grid.major = element_blank(),
                panel.grid.minor = element_blank(),
                panel.background = element_blank(),
                axis.line.x = element_line(color = 'black'),
                axis.line.y = element_line(color = 'black'),
                legend.key = element_rect(fill = 'white'),
                text = element_text(size = 15))
```

## Graph Type Selection Guide
| Data Structure | X Variable | Y Variable | Grouping | Graph Type | Key Functions |
|---------------|-----------|-----------|----------|------------|---------------|
| Distribution | Continuous | Frequency | None | Histogram | `geom_histogram(binwidth = )` |
| Relationship | Continuous | Continuous | Optional | Scatterplot | `geom_point()`, `geom_smooth(method = 'lm')` |
| Group Means | Categorical | Continuous | Optional | Bar Chart | `stat_summary(fun = mean, geom = "bar")` |
| Time Series | Ordered Categorical | Continuous | Optional | Line Graph | `stat_summary(fun = mean, geom = "line", aes(group = ))` |

## Professional Graph Requirements (Lab Grading Criteria)
1. **Proper axis labels** - Use Proper Case, explain variables fully
2. **Error bars** - Use `stat_summary(fun.data = mean_cl_normal)` for grouped data
3. **Legend labels** - Replace variable names with descriptive text via `scale_*_manual()`
4. **Readability** - Apply `cleanup` theme or `theme_bw()`/`theme_classic()`
5. **Appropriate geometry** - Match graph type to data structure
6. **Print-friendly** - Use grayscale colors when possible (graphs are printed B&W)

## Lab Assignment Pattern
Lab files follow this structure:
1. **YAML header** - Output to Word document with custom reference
2. **Machine info chunk** - Auto-generates system details
3. **Abstract/Context** - Describes the dataset and research question
4. **Empty code chunks** - Students fill in with correct visualization code
5. **Assessment criteria** - Listed explicitly for each question

## Common Data Patterns
- **SPSS files (.sav)** - Often have numeric codes (1, 2) that need factor labels
- **Wide format** - Repeated measures stored as separate columns (needs `melt()`)
- **Missing values** - Festival dataset has many blanks (handle appropriately)
- **Mixed designs** - Multiple IVs (between + within subjects) require careful aesthetics setup

## Error Bar Implementation
For confidence intervals (preferred for academic graphs):
```r
stat_summary(fun.data = mean_cl_normal,  # 95% CI by default
             geom = "errorbar",
             position = position_dodge(width = 0.90),  # Align with bars
             width = .2)                               # Cap width
```

## When Editing Student Code
- Check that **factor conversion** happens before plotting
- Verify **relative paths** match the .Rmd file location
- Ensure **axis labels are professional** (not raw variable names)
- Confirm **error bars are present** for grouped comparisons
- Test that code runs **chunk-by-chunk** (students build incrementally)
- Look for **cleanup theme** or `theme_bw()` application

## Output Formats
- **Lecture slides** - `slidy_presentation` with incremental reveals
- **Lab assignments** - `word_document` with `reference_docx` template
- Both use inline R code for dates: `` `r Sys.Date()` ``
