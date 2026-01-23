# Setup Guide

## For Students (ANLY500 Course)

### R Environment Setup
1. **Install R**: Download from [CRAN](https://cran.r-project.org/)
2. **Install RStudio**: Download from [Posit](https://posit.co/download/rstudio-desktop/)
3. **Windows users**: Install [Rtools](https://cran.r-project.org/bin/windows/Rtools/) for package compilation
4. **Install required packages** in R console:
   ```r
   install.packages(c("tidyverse", "ggplot2", "dplyr", "rio", "reshape", 
                      "GGally", "Hmisc", "moments", "psych", "pastecs", 
                      "corrplot", "knitr", "kableExtra", "effectsize", "MOTE"))
   ```

### Opening Course Materials
1. Navigate to `ANLY500-Analytics-I/WeekXX/` folders
2. Open `.rmd` files (lectures) or `lab/*.Rmd` files (assignments) in RStudio
3. Run chunks with Ctrl+Enter (Cmd+Enter on Mac)
4. Knit to HTML (lectures) or Word (labs) using "Knit" button

---

## For Contributors & Instructors

### Python Environment Setup (Optional)
Required only for running the textbook indexing script.

**Option 1: Using Conda (Recommended)**
```bash
# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate data_sciences

# Run indexing script
python index_knowledge.py
```

**Option 2: Using pip**
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies (minimal)
pip install -r requirements.txt

# Run indexing script
python index_knowledge.py
```

### Textbook Indexing Script
- **Purpose**: Indexes Field et al. (2012) textbook for quick keyword searches
- **Location**: `index_knowledge.py` (root directory)
- **Input**: `ANLY500-Analytics-I/Knowledge/Field_ea_2012_Discovering_Statistics_using_R_normalized.txt`
- **Output**: JSON summary to console with:
  - Section headers count and samples
  - Keyword hit counts (Data Screening, Missing Data, Outliers, etc.)
  - First 5 locations for each keyword
- **Dependencies**: Python 3.7+ with standard library only (re, json, os)

### Repository Structure
```
data_sciences/
├── ANLY500-Analytics-I/       # R-based analytics course
│   ├── WeekXX/                # Weekly materials
│   │   ├── *.rmd              # Lectures (Slidy presentations)
│   │   ├── lab/*.Rmd          # Labs (Word documents)
│   │   └── data/              # Example datasets
│   └── Knowledge/             # Textbook (normalized .txt)
├── ANLY699-Applied-Project/   # Research writing course
│   ├── WeekXX-Topic/          # Writing guides
│   └── APA7/                  # APA resources (PDFs)
├── .github/                   # GitHub configuration
│   └── copilot-instructions.md  # AI agent guidelines
├── environment.yml            # Conda environment
├── requirements.txt           # Python dependencies
├── index_knowledge.py         # Textbook indexing script
└── SETUP.md                   # This file
```

### Publishing Workflow
1. Edit `.rmd` or `.Rmd` files in RStudio
2. Knit to HTML (lectures) or Word (labs)
3. Commit both source and output files
4. HTML lectures auto-publish to GitHub Pages: `https://melhzy.github.io/data_sciences/`

### Documentation
- **AI Agent Instructions**: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- **ANLY500 Overview**: [ANLY500-Analytics-I/README.md](ANLY500-Analytics-I/README.md)
- **ANLY699 Guide**: [ANLY699-Applied-Project/RESEARCH_WRITING_GUIDE.md](ANLY699-Applied-Project/RESEARCH_WRITING_GUIDE.md)
