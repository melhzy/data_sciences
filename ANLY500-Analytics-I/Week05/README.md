# Week 05: Data Visualization with ggplot2

## Lecture Materials

### Viewing the Presentations

This week has one HTML presentation and one comprehensive R tutorial:

#### 1. Data Visualization (Lecture Slides)

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Presentation Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week05/05_graphs.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week05/05_graphs.html)

**Option 3: Download and Open Locally**
- Download `05_graphs.html` and open in your web browser

#### 2. R for Data Analytics (Week 05 Hands-on Tutorial) 🆕

**Option 1: View Online (GitHub Pages - Recommended)**
- [View Tutorial Online](https://melhzy.github.io/data_sciences/ANLY500-Analytics-I/Week05/05_R_for_DataAnalytics.html)

**Option 2: Alternative Online Viewer**
- [View via htmlpreview](https://htmlpreview.github.io/?https://github.com/melhzy/data_sciences/blob/main/ANLY500-Analytics-I/Week05/05_R_for_DataAnalytics.html)

**Option 3: Download and Open Locally**
- Download `05_R_for_DataAnalytics.html` and open in your web browser

---

## Course Content

This week builds on Weeks 02-04 and focuses on **data visualization** using R's powerful `ggplot2` package:

### Lecture Topics
- The art of presenting data (Tufte's principles)
- Common visualization mistakes to avoid
- Programming suggestions: code stacking
- Working with files and factor variables
- Data structure formats: wide vs. long
- Rearranging data with `melt()` and `pivot_longer()`

### R Tutorial Topics
- **Grammar of Graphics**: Understanding the layered structure of ggplot2
- **Histograms**: Assessing distributions, detecting outliers, checking normality
- **Scatterplots**: Exploring bivariate relationships, adding regression lines
- **Bar Graphs**: Comparing group means with error bars (SD, SE, 95% CI)
- **Line Graphs**: Visualizing longitudinal and repeated measures data
- **Data Reshaping**: Converting between wide and long formats
- **Professional Customization**: Themes, colors, faceting, annotations
- **Best Practices**: Tufte's principles, colorblind accessibility, saving figures

---

## Materials

- **Lecture Slides**: `05_graphs.rmd` → `05_graphs.html` (Slidy presentation)
- **R Tutorial**: `05_R_for_DataAnalytics.rmd` → `05_R_for_DataAnalytics.html` (Interactive tutorial)
- **Lab Assignment**: `lab/` folder
- **Data Files**: `data/` folder
  - `ChickFlick.sav` - SPSS file for bar graph examples
  - `Exam Anxiety.csv` - Scatterplot examples
  - `Jiminy Cricket.csv` - Wide-to-long reshaping example
  - `Hiccups.csv` - Line graph example
  - `Texting.xlsx` - Two-factor line graph example
  - `festival.csv` - Histogram example
- **Images**: `pictures/` folder (lecture graphics)

---

## Reading

- **Textbook**: Discovering Statistics Using R (Field et al., 2012)
  - Chapter 4: Exploring data with graphs
    - Section 4.1: Why do we need graphs?
    - Section 4.2: What makes a good graph?
    - Section 4.3: Introducing ggplot2
    - Section 4.4: The anatomy of a plot
    - Section 4.5: Graphing relationships (scatterplots)
    - Section 4.6: Histograms
    - Section 4.7: Boxplots
    - Section 4.8: Density plots
    - Section 4.9: Graphing means (bar charts and line graphs)
  
  Local reference file: `D:\Github\data_sciences\ANLY500-Analytics-I\Knowledge\Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`

- **Additional References**:
  - Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.)
  - Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis* (2nd ed.)
  - Wilkinson, L. (2005). *The Grammar of Graphics* (2nd ed.)

---

## Learning Path

### Step 1: Theory
1. Review the Week 05 lecture (`05_graphs.html`)
2. Understand Tufte's principles of data visualization
3. Learn the grammar of graphics and ggplot2's layered approach
4. Study when to use each plot type (histogram, scatter, bar, line)

### Step 2: Practice
1. Work through `05_R_for_DataAnalytics.html`
2. Build histograms to assess distribution shapes
3. Create scatterplots with regression lines
4. Construct bar graphs with error bars
5. Generate line graphs for repeated measures data
6. Practice reshaping data from wide to long format

### Step 3: Apply
1. Complete the lab assignment in `lab/`
2. Create publication-quality figures for your final project
3. Apply professional themes and customization
4. Practice saving high-resolution figures (300 dpi)

---

## Key Concepts

### Tufte's Principles of Good Graphs
1. **Show the data** clearly and accurately
2. **Induce thinking** about substance, not methodology
3. **Avoid distortion** of what the data say
4. **Present many numbers** efficiently
5. **Make large datasets coherent**
6. **Encourage comparison** of different data
7. **Reveal data** at multiple levels of detail

### Grammar of Graphics (ggplot2)
- **Data**: The dataset to visualize
- **Aesthetics (aes)**: Mappings from variables to visual properties (x, y, color, size)
- **Geometries (geom)**: The type of plot (points, lines, bars, etc.)
- **Layers**: Building plots incrementally by adding components

### Plot Type Selection

| Data Structure | Research Question | Plot Type | ggplot2 Function |
|----------------|-------------------|-----------|------------------|
| One continuous | Distribution shape? | Histogram + density | `geom_histogram()` + `geom_density()` |
| One continuous | Outliers? | Boxplot | `geom_boxplot()` |
| One categorical | Frequencies? | Bar chart | `geom_bar()` |
| Two continuous | Relationship? | Scatterplot | `geom_point()` + `geom_smooth()` |
| Continuous by categorical | Group means differ? | Bar chart with error bars | `stat_summary(geom='bar')` |
| Repeated measures | Change over time? | Line graph | `stat_summary(geom='line')` |
| Multiple continuous | Pairwise relationships? | Scatterplot matrix | `GGally::ggpairs()` |

### Error Bar Types
- **Standard Deviation (SD)**: Shows spread of individual scores
- **Standard Error (SE)**: Shows precision of the mean estimate
- **95% Confidence Interval (CI)**: Shows range likely containing the population mean (recommended)

### Data Formats
- **Wide Format**: Each participant = one row; repeated measures = separate columns
- **Long Format**: Each measurement = one row; required for most ggplot2 visualizations
- **Reshaping**: Use `pivot_longer()` (tidyr) or `melt()` (reshape) to convert wide → long

---

## Tools & Packages

### Required R Packages
```r
install.packages(c("tidyverse", "ggplot2", "dplyr", "tidyr", "rio", "Hmisc", "kableExtra"))
install.packages("reshape")  # For melt() function
install.packages("GGally")   # For scatterplot matrices
install.packages("seedhash") # For reproducible analysis
```

### Optional Packages (Recommended)
```r
install.packages(c("RColorBrewer", "viridis", "patchwork", "plotly"))
```

### Recommended Software
- **R**: Version 4.5.2 or higher
- **RStudio/Posit**: Latest version
- **VS Code**: With R extension (alternative)

---

## Common Visualization Mistakes to Avoid

### ❌ Bad Practices
1. **Truncated Y-axis** on bar charts (exaggerates differences)
2. **3D effects** that distort perception
3. **Excessive colors** and patterns (chartjunk)
4. **Missing axis labels** or units
5. **Overlapping text** that's unreadable
6. **Using pie charts** for more than 2-3 categories
7. **Not checking colorblind accessibility**

### ✅ Good Practices
1. **Start Y-axis at zero** for bar charts
2. **Use 2D plots** for clarity
3. **Limit colors** to 3-5 per plot
4. **Label all axes** with units
5. **Ensure text is readable** (size ≥ 12pt)
6. **Use bar/line graphs** instead of pie charts
7. **Test with colorblind simulators**

---

## Example Datasets

### 1. Jiminy Cricket (Wide → Long Reshaping)
- **Study**: Test Disney's "wish upon a star" philosophy
- **Design**: 250 participants, 2 strategies (wish vs. work), measured pre/post
- **Use**: Demonstrates data reshaping for visualization

### 2. Festival Hygiene (Histograms)
- **Study**: Festival attendees' hygiene ratings over 3 days
- **Scale**: 0 (eau de toilet) to 4 (eau de toilette)
- **Use**: Histogram examples, distribution assessment

### 3. Exam Anxiety (Scatterplots)
- **Study**: 103 students' anxiety, revision time, exam scores, gender
- **Use**: Simple and grouped scatterplots, regression lines

### 4. Chick Flick (Bar Graphs)
- **Study**: 40 participants (20M, 20F) watch Bridget Jones or Memento
- **Outcome**: Physiological arousal
- **Use**: One and two-factor bar charts with error bars

### 5. Hiccup Cures (Line Graphs)
- **Study**: 15 participants try 4 hiccup interventions
- **Use**: Single-factor line graph example

### 6. Text Messaging (Two-Factor Line Graphs)
- **Study**: 50 children, texting allowed vs. forbidden, grammar tested at baseline and 6 months
- **Use**: Interaction effects visualization

---

## Code Stacking Best Practice

When building complex ggplot2 visualizations, **stack your code** across multiple lines:

```r
# ✅ GOOD: Stacked code (readable and debuggable)
ggplot(data, aes(x = variable1, y = variable2, color = group)) +
  geom_point(size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = TRUE) +
  xlab("X Axis Label") +
  ylab("Y Axis Label") +
  cleanup +
  scale_color_manual(values = c("blue", "red"))

# ❌ BAD: Single line (hard to read and debug)
ggplot(data, aes(x = variable1, y = variable2, color = group)) + geom_point(size = 3, alpha = 0.7) + geom_smooth(method = "lm", se = TRUE) + xlab("X Axis Label") + ylab("Y Axis Label") + cleanup + scale_color_manual(values = c("blue", "red"))
```

**Why?** When you get an error, R tells you which line failed. Stacked code makes troubleshooting much easier!

---

## Custom Theme Template

Create a reusable theme for consistency across all plots:

```r
# Save this in your script and add "+ cleanup" to every plot
cleanup <- theme(
  panel.grid.major = element_blank(),      # Remove major gridlines
  panel.grid.minor = element_blank(),      # Remove minor gridlines
  panel.background = element_blank(),      # Remove background
  axis.line.x = element_line(color = 'black'),  # Black x-axis
  axis.line.y = element_line(color = 'black'),  # Black y-axis
  legend.key = element_rect(fill = 'white'),    # White legend background
  text = element_text(size = 15)           # Larger text for readability
)
```

---

## Saving High-Quality Figures

```r
# For presentations (PNG)
ggsave("figure1.png", width = 8, height = 5, dpi = 150)

# For publications (PNG, high resolution)
ggsave("figure1.png", width = 8, height = 5, dpi = 300)

# For publications (PDF, vector graphics)
ggsave("figure1.pdf", width = 8, height = 5)

# For editing (SVG, vector graphics)
ggsave("figure1.svg", width = 8, height = 5)
```

**Recommendations**:
- **Web/Presentations**: 150 dpi PNG
- **Print Publications**: 300 dpi PNG or PDF
- **Further Editing**: SVG or PDF

---

## Quick Reference: ggplot2 Layers

| Layer Type | Function | Purpose |
|------------|----------|---------|
| **Data** | `ggplot(data, aes(...))` | Define dataset and aesthetics |
| **Geometry** | `geom_point()`, `geom_line()`, `geom_bar()` | Add visual elements |
| **Statistics** | `stat_summary()`, `stat_smooth()` | Add statistical transformations |
| **Scales** | `scale_x_continuous()`, `scale_color_manual()` | Customize axes and legends |
| **Coordinates** | `coord_flip()`, `coord_cartesian()` | Adjust coordinate system |
| **Facets** | `facet_wrap()`, `facet_grid()` | Create small multiples |
| **Themes** | `theme_minimal()`, `theme()` | Control non-data elements |
| **Labels** | `labs()`, `xlab()`, `ylab()` | Add titles and labels |

---

## Practice Exercises

### Exercise 1: Histogram and Distribution Assessment
Using the `mtcars` dataset, create a histogram of `mpg` with a density curve overlay. Assess whether the distribution is approximately normal.

### Exercise 2: Scatterplot with Groups
Using the `iris` dataset, create a scatterplot of `Sepal.Length` vs. `Sepal.Width` colored by `Species`. Add separate regression lines for each species.

### Exercise 3: Bar Chart with Error Bars
Create a bar chart showing mean `mpg` by number of cylinders (`cyl`) in `mtcars`. Add 95% confidence interval error bars.

### Exercise 4: Line Graph with Interaction
Using a longitudinal dataset, create a line graph showing how an outcome changes over time for different groups. Interpret any interaction effects.

---

## Troubleshooting Common Errors

### Error: "object not found"
- **Cause**: Variable name misspelled or data not loaded
- **Fix**: Check spelling, ensure `library()` and data import ran successfully

### Error: "could not find function 'geom_point'"
- **Cause**: ggplot2 package not loaded
- **Fix**: Run `library(ggplot2)` or `library(tidyverse)`

### Error: "Aesthetics must be valid data columns"
- **Cause**: Variable name in `aes()` doesn't exist in the data
- **Fix**: Check column names with `names(data)`, fix typos

### Error: "Don't know how to automatically pick scale"
- **Cause**: Variable type doesn't match aesthetic (e.g., continuous variable for discrete scale)
- **Fix**: Convert variable with `factor()` or use appropriate scale function

### Lines not connecting in line graphs
- **Cause**: Missing `group` aesthetic
- **Fix**: Add `aes(group = variable)` or `aes(group = 1)` for single line

---

## Quick Links

- [← Week 04 Materials](../Week04/README.md)
- [→ Week 06 Materials](../Week06/README.md)
- [Back to Course Home](../README.md)
- [View All Tutorials (GitHub Pages)](https://melhzy.github.io/data_sciences/)

---

## Additional Resources

### Online Documentation
- [ggplot2 Official Documentation](https://ggplot2.tidyverse.org/)
- [R Graphics Cookbook](https://r-graphics.org/)
- [Data Visualization with ggplot2 Cheatsheet](https://rstudio.github.io/cheatsheets/data-visualization.pdf)

### Books
- Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis* (2nd ed.)
- Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.)
- Wilke, C. O. (2019). *Fundamentals of Data Visualization*

### Interactive Learning
- [R for Data Science - Data Visualization Chapter](https://r4ds.had.co.nz/data-visualisation.html)
- [ggplot2 Extensions Gallery](https://exts.ggplot2.tidyverse.org/gallery/)

---

<div align="center">

**ANLY 500 - Analytics I**  
*Harrisburg University*

Last Updated: December 11, 2025

</div>

