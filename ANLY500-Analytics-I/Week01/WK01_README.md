# Week 01: Introduction to R

## Welcome to R!

This is your first week learning R, a powerful programming language for data analysis and statistical computing. This course is designed to help you become comfortable with R even if you've never programmed before. We'll start with the fundamentals and build your skills step by step.

## What You'll Learn This Week

By the end of this week, you will be able to:
1. Understand what R is and why it's valuable for data analysis
2. Navigate the RStudio interface confidently
3. Create and work with different types of data (numbers, text, categories)
4. Store and organize data using vectors, matrices, data frames, and lists
5. Perform calculations and comparisons
6. Load data from CSV files
7. Access and subset specific parts of your data
8. Handle missing data appropriately
9. Use built-in R functions for analysis
10. Write your own simple functions

## Course Materials

- **Lecture Slides**: `WK01_01_introR.html` (also available as PDF)
- **Lab Assignment**: `lab/01_lab_R_learning.Rmd` (30 practice exercises)
- **Practice Data**: `lab/lab_R_learning.csv`

## Topics Covered

### 1. Getting Started with R

- What is R and why is it used for analytics?
- Installing R and RStudio
- Understanding the RStudio interface (Console, Script Editor, Environment, Files)
- R as a powerful calculator
- Running your first R commands

### 2. Creating and Managing Objects

- Using the assignment operator `<-` to store values
- Naming conventions for objects (be clear and descriptive!)
- Checking what's in your workspace with `ls()`
- Removing objects with `rm()`

**Example**:
```r
A <- 5           # Store the value 5 in object named A
ls()             # See all objects
rm(A)            # Remove object A
```

### 3. Data Types in R

R recognizes different types of data:

- **Numeric**: Numbers (e.g., `42`, `3.14`)
- **Character**: Text in quotes (e.g., `"hello"`, `"Adelie"`)
- **Logical**: TRUE or FALSE values
- **Factor**: Categories (e.g., species names, treatment groups)
- **Special values**: 
  - `NA` (missing/not available)
  - `NULL` (empty)
  - `Inf` (infinity)
  - `NaN` (not a number)

**Check data type**:
```r
class(42)         # "numeric"
class("hello")    # "character"
class(TRUE)       # "logical"
```

### 4. Data Structures

R organizes data in different structures depending on your needs:

#### Vectors
- Collections of items of the same type
- Created with `c()` (combine) function
- Example: `c(1, 2, 3, 4, 5)` or `c("A", "B", "C")`

#### Matrices
- 2-dimensional arrays with rows and columns
- All data must be the same type
- Created with `matrix()` function
- Access elements using `[row, column]`

**Example**:
```r
myMatrix <- matrix(data = 1:10, nrow = 5, ncol = 2)
myMatrix[1, 2]    # First row, second column
```

#### Data Frames
- Like matrices but columns can be different types
- Most common structure for datasets
- Each column can be accessed with `$`

**Example**: The `penguins` dataset
```r
penguins$species          # Access species column
penguins[1, 2:3]         # First row, columns 2-3
```

#### Lists
- Can contain different types and structures
- Most flexible data structure
- Elements accessed with `[[]]` or `$`
- Example: Results from statistical models (like `lm()`)

### 5. Basic Operations

#### Arithmetic Operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `^` exponentiation

#### Comparison Operators
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to
- `==` equal to (note: two equal signs!)
- `!=` not equal to

#### Logical Operators
- `&` AND (both conditions true)
- `|` OR (at least one condition true)
- `!` NOT (negates/reverses)

### 6. Working with Data Files

#### Setting Your Working Directory
- **Option 1**: Use `setwd()` function (error-prone when you move files)
- **Option 2**: Use RStudio Projects (recommended!)
- **Option 3**: Use R Markdown files (they automatically use their own location)
- Check current directory: `getwd()`

#### Importing Data
R can read many file types. For CSV files:

```r
# Base R method
mydata <- read.csv("filename.csv")

# Using rio package (works with many formats)
library(rio)
mydata <- import("filename.csv")
```

#### Viewing Your Data
- `View(data)` - Opens data viewer
- `head(data)` - First few rows
- `tail(data)` - Last few rows
- `str(data)` - Structure/overview
- `summary(data)` - Summary statistics

### 7. Subsetting and Accessing Data

One of the most important skills is getting the specific data you need:

#### Using `[ ]` for Subsetting
- `data[1, ]` - first row, all columns
- `data[, 2]` - all rows, second column
- `data[1:5, ]` - rows 1 through 5
- `data[, -1]` - all columns except first

#### Using `$` for Columns
```r
penguins$bill_length_mm    # Get bill_length_mm column
```

#### Logical Subsetting (Filtering)
Filter data based on conditions:
```r
# Penguins with bill length > 54mm
penguins[penguins$bill_length_mm > 54, ]

# Complex conditions using & (AND)
penguins[penguins$bill_length_mm > 54 & penguins$bill_depth_mm > 17, ]
```

#### Using `subset()` Function
Alternative method that's often easier to read:
```r
subset(penguins, bill_length_mm > 54)
```

**Note**: `subset()` automatically removes rows with `NA` values!

#### Combining Data
- `cbind(X, Y)` - Combine as columns
- `rbind(X, Y)` - Combine as rows

### 8. Handling Missing Data

Real datasets often have missing values (shown as `NA`):

#### Identifying Missing Data
```r
is.na(data)              # Returns TRUE for missing values
complete.cases(data)     # Returns TRUE for complete rows (no NAs)
na.omit(data)           # Removes rows with any NAs
```

#### Functions and Missing Data
Many functions return `NA` if there's any missing data:
```r
mean(data)                    # Returns NA if any values missing
mean(data, na.rm = TRUE)      # Removes NAs before calculating
cor(data, use = "pairwise.complete.obs")  # Correlation with NAs
```

### 9. Essential R Functions

#### Getting Help
- `?function_name` - View help documentation
- `help(function_name)` - Same as `?`
- `args(function_name)` - See what arguments function takes
- `example(function_name)` - Run examples from help

#### Descriptive Statistics
- `mean()` - Average
- `median()` - Middle value
- `sd()` - Standard deviation
- `var()` - Variance
- `min()`, `max()`, `range()` - Extreme values
- `sum()` - Total
- `table()` - Frequency counts
- `summary()` - Quick overview with multiple statistics
- `cor()` - Correlation
- `cov()` - Covariance

#### Data Exploration
- `str()` - Structure of object
- `class()` - Type of object
- `length()` - Number of elements
- `dim()` - Dimensions (rows, columns)
- `names()`, `colnames()`, `rownames()` - Variable names
- `ls()` - List objects in environment

### 10. Writing Your Own Functions

Functions let you automate repetitive tasks. They're easier than they look!

**Structure**:
```r
function_name <- function(arguments){
  # what the function does
  result
}
```

**Example**:
```r
# Create a function that squares a number
pizza <- function(x){
  x^2
}

pizza(3)    # Returns 9
pizza(5)    # Returns 25
```

## Lab Assignment

The lab file (`01_lab_R_learning.Rmd`) contains 30 hands-on exercises covering:

1. **Basics** (Q1-6): Logical operators, variables, data types
2. **Vectors** (Q7-12): Creating and working with vectors
3. **Dataframes** (Q13-23): Real data analysis with built-in datasets
4. **Functions** (Q24-25): Creating your own functions
5. **Packages** (Q26-29): Installing and using add-on packages
6. **Data Import** (Q30): Reading external data files

### Working with R Markdown
- R Markdown combines code and written explanations
- Code goes in "chunks" between ` ```{r} ` and ` ``` `
- Run individual chunks with Ctrl+Enter (Windows) or Cmd+Return (Mac)
- "Knit" the entire document to create a Word file

### Your Computing Environment
The lab automatically records:
- Your machine name
- Your operating system (Windows/macOS/Linux)
- OS version

This is important for **reproducible research** - others should be able to recreate your analysis!

## Setup Instructions

### Installing R and RStudio
1. Download R from: https://cran.r-project.org/
2. Download RStudio from: https://posit.co/downloads/
3. Install R first, then RStudio

### Installing Packages
```r
install.packages("rmarkdown")  # For R Markdown documents
install.packages("knitr")      # For creating documents
install.packages("rio")        # For importing various file types
install.packages("palmerpenguins")  # Practice dataset
```

**Note**: You only install packages once, but you need to load them each session:
```r
library(palmerpenguins)
```

### VSCode (Optional Alternative)
If you prefer VSCode instead of RStudio:
1. Install R extension: `REditorSupport.r`
2. Install Quarto extension
3. Configure R path in settings

## Tips for Success

1. **Practice regularly** - Programming is learned by doing
2. **Type code yourself** - Don't just copy-paste
3. **Read error messages** - They're trying to help!
4. **Use comments (`#`)** - Explain your code to your future self
5. **Save your work often** - Ctrl+S is your friend
6. **Ask questions** - Everyone starts as a beginner
7. **Check your data types** - Many errors come from unexpected data types
8. **Remember: R is case-sensitive** - `data` and `Data` are different!

## Common Issues and Solutions

**Problem**: "Object not found"  
**Solution**: Check spelling and make sure you created the object first

**Problem**: Function returns `NA`  
**Solution**: Check for missing data, use `na.rm = TRUE` if appropriate

**Problem**: "Could not find function"  
**Solution**: Load the package with `library()` first

**Problem**: Error when reading data  
**Solution**: Check your working directory with `getwd()` and file path

## Resources

- **R Documentation**: https://www.r-project.org/
- **RStudio Cheatsheets**: https://posit.co/resources/cheatsheets/
- **Quick-R**: https://www.statmethods.net/
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/r

## Next Steps

Week 2 will build on these fundamentals to:
- Work with more complex datasets
- Create professional visualizations
- Perform statistical analyses
- Learn about data transformation and cleaning

Remember: Everyone finds R challenging at first. With practice, it becomes much more natural. You've got this!
