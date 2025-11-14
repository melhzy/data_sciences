# Week 5: Data Collection

## Overview

This week focuses on executing your data collection plan, ensuring data quality, and documenting the process thoroughly. Whether using primary or secondary data, rigorous data collection is essential for credible research.

## Learning Objectives

By the end of this week, you will be able to:
1. Implement systematic data collection procedures
2. Assess and document data quality
3. Handle missing data appropriately
4. Create data dictionaries and codebooks
5. Maintain data integrity and security
6. Document data collection challenges

## Required Reading

📄 **Sample Papers**: Review data collection sections in:
- `../SamplePapers/Net Photosynthetic Rate.pdf` (Measurement procedures)
- `../SamplePapers/English Language Proficiency.pdf` (Assessment instruments)

## Tutorial Content

### 1. Data Collection Planning

#### Pre-Collection Checklist

```r
# Data collection checklist

collection_plan <- list(
  ## Preparation
  irb_approved = TRUE,
  materials_ready = TRUE,
  pilot_tested = TRUE,
  
  ## Resources
  personnel = "Research assistants trained",
  equipment = "Software licenses acquired",
  storage = "Secure server configured",
  
  ## Timeline
  start_date = "2025-03-01",
  end_date = "2025-04-15",
  milestones = c("Week 1: Setup", "Weeks 2-5: Active collection", 
                 "Week 6: Quality checks")
)
```

#### Pilot Testing

Before full data collection:

1. **Small-scale test** (n = 10-20)
2. **Identify problems**: Unclear instructions, technical issues
3. **Time estimation**: How long does it take?
4. **Refine procedures**: Fix identified issues

```markdown
## Pilot Study

A pilot study (n = 15) was conducted January 15-20, 2025 to test 
procedures. Results indicated that the survey took longer than anticipated 
(M = 18 minutes vs. estimated 12 minutes). Based on pilot feedback, we 
simplified three questions and reduced the total item count from 45 to 38, 
reducing average completion time to 14 minutes.
```

### 2. Secondary Data Collection

#### Database Extraction

```markdown
## Data Extraction

Customer transaction data were extracted from the company's PostgreSQL 
database on March 1, 2025. We used the following inclusion criteria:

- Account created between January 1, 2020 and December 31, 2024
- Minimum of one purchase recorded
- Account status = "active" or "churned" (excluding "suspended")

**SQL Query**. The extraction query (see Appendix A) retrieved 15 fields 
including customer ID, registration date, purchase history, demographic 
information, and churn status. The query returned 47,823 records.
```

```sql
-- Example SQL documentation (in Appendix)
SELECT 
    customer_id,
    registration_date,
    age,
    gender,
    total_purchases,
    total_spend,
    last_purchase_date,
    account_status,
    churned_flag
FROM customers
WHERE registration_date BETWEEN '2020-01-01' AND '2024-12-31'
    AND account_status IN ('active', 'churned')
    AND customer_id IS NOT NULL;
```

#### Data Quality Assessment

```r
# Document data quality checks

library(dplyr)
library(naniar)

# Missing data analysis
missing_summary <- data %>%
  miss_var_summary() %>%
  filter(pct_miss > 0)

# Report in paper:
## Data Quality Assessment

**Missing Data**. We assessed missingness patterns using the naniar 
package (Tierney & Cook, 2023). Missing data rates were generally low: 
purchase_amount (0.2%), customer_age (3.1%), zip_code (1.8%), and 
income (12.4%). The income variable's higher missingness is consistent 
with customers declining to provide this optional information.

**Outliers**. We examined univariate distributions for extreme values. 
Three customers had total_spend values >3 SD above the mean ($50,000+), 
confirmed as legitimate high-value customers through manual review. 
No outliers were excluded.

**Data Integrity**. Logical consistency checks revealed no impossible 
values (e.g., negative ages, future dates). All date fields were 
successfully parsed, and categorical variables contained only expected 
values.
```

### 3. Primary Data Collection

#### Survey Administration

```markdown
## Survey Procedures

The survey was implemented using Qualtrics (2025) and distributed via 
email on March 1, 2025 to 1,250 eligible participants. The email 
included:

1. Brief study description
2. Informed consent information
3. Unique survey link (preventing multiple responses)
4. Estimated completion time (15 minutes)
5. Incentive details ($10 Amazon gift card)

**Reminders**. Non-respondents received reminder emails on Day 5 and 
Day 10. The survey closed on March 15, 2025.

**Response Rate**. Of 1,250 invitations sent, 847 participants initiated 
the survey (68% response rate). After excluding incomplete surveys 
(n = 121, did not reach 75% completion), the final sample comprised 
726 responses (58% usable response rate).
```

#### Response Quality Checks

```r
# Attention checks and data quality

quality_checks <- data %>%
  mutate(
    # Time-based flags
    too_fast = completion_time_sec < 300,  # <5 minutes
    too_slow = completion_time_sec > 3600, # >1 hour
    
    # Attention check items
    failed_attention = attention_check != "Strongly Agree",
    
    # Straight-lining (same response to all items)
    straightline = apply(select(., starts_with("item")), 1, 
                         function(x) length(unique(x)) == 1),
    
    # Overall quality flag
    low_quality = too_fast | failed_attention | straightline
  )

# Report exclusions
## Data Screening

**Quality Checks**. We implemented three data quality screens:

1. **Completion time**: Responses completed in <5 minutes (n = 23) 
   were flagged as potentially rushed.
2. **Attention checks**: The survey included two attention check items 
   (e.g., "Please select 'Strongly Agree' for this item"). Participants 
   failing both checks (n = 17) were excluded.
3. **Straight-lining**: Respondents providing identical responses to 
   all Likert items (n = 8) were excluded as potentially inattentive.

After applying quality screens, 678 responses (93% of 726) remained 
for analysis.
```

### 4. Data Documentation

#### Data Dictionary

Create comprehensive documentation:

```r
# Create data dictionary

library(dataMeta)

data_dict <- data.frame(
  variable_name = c("customer_id", "age", "gender", "total_purchases", 
                    "churned"),
  description = c(
    "Unique customer identifier",
    "Customer age in years at registration",
    "Self-reported gender",
    "Count of completed purchases (lifetime)",
    "Whether customer churned by study end"
  ),
  type = c("integer", "integer", "factor", "integer", "logical"),
  values = c(
    "1 to 47823",
    "18 to 85",
    "Male, Female, Non-binary, Prefer not to say",
    "1 to 457",
    "TRUE (churned) or FALSE (active)"
  ),
  missing_n = c(0, 1483, 92, 11, 0),
  missing_pct = c(0.0, 3.1, 0.2, 0.02, 0.0),
  notes = c(
    "Anonymized; original ID stored separately",
    "Age at account creation",
    "12% preferred not to disclose",
    "Excludes refunded/cancelled orders",
    "Defined as no purchases in 180+ days"
  )
)

# Export for supplementary materials
write.csv(data_dict, "data_dictionary.csv", row.names = FALSE)
```

Example table in paper:

| Variable | Description | Type | Range/Values | Missing (%) |
|----------|-------------|------|--------------|-------------|
| customer_id | Unique identifier | Integer | 1-47,823 | 0.0 |
| age | Age at registration | Integer | 18-85 | 3.1 |
| gender | Self-reported gender | Factor | M/F/NB/PNTS | 0.2 |
| total_purchases | Lifetime purchase count | Integer | 1-457 | 0.02 |
| churned | Churned by study end | Logical | TRUE/FALSE | 0.0 |

*Note*. M = Male, F = Female, NB = Non-binary, PNTS = Prefer not to say.

#### Codebook for Surveys

```markdown
## Measures

### Customer Satisfaction Scale (CSS)

Adapted from Johnson (2020). Participants rated agreement with 7 items 
using a 5-point scale (1 = *Strongly Disagree*, 5 = *Strongly Agree*).

**Items**:
1. "I am satisfied with the products/services" [css_1]
2. "The quality meets my expectations" [css_2]
3. "I would recommend to others" [css_3]
4. "The value for money is good" [css_4]
5. "Customer service is responsive" [css_5]
6. "The website/app is easy to use" [css_6]
7. "Overall, I am a satisfied customer" [css_7]

**Scoring**: Items were averaged to create a composite score (range 1-5), 
with higher scores indicating greater satisfaction. Internal consistency 
was excellent (α = .92).

**Variable name**: `satisfaction_score`
```

### 5. Data Storage and Security

#### Best Practices

```markdown
## Data Management

**Storage**. Data were stored on the university's secure, HIPAA-compliant 
server with automated daily backups. Access was restricted to study 
personnel via two-factor authentication.

**De-identification**. Personal identifiers (names, email addresses, 
IP addresses) were removed prior to analysis. A separate linking file 
connecting participant IDs to identifiers was stored in a password-
protected, encrypted file accessible only to the PI.

**Retention**. Per IRB protocol, data will be retained for 5 years 
following publication, after which all files will be securely deleted. 
De-identified data may be shared upon reasonable request, subject to 
data use agreements.

**Version Control**. All analysis scripts and data files were version-
controlled using Git, with repository backups stored on GitHub private 
repository.
```

### 6. Handling Missing Data

#### Assessment Strategies

```r
# Analyze missing data patterns

library(mice)
library(VIM)

# Visualize missing patterns
aggr(data, col = c('navyblue','red'), 
     numbers = TRUE, sortVars = TRUE,
     labels = names(data), cex.axis = .7,
     gap = 3, ylab = c("Missing data","Pattern"))

# Test MCAR assumption
mcar_test(data)

# Report results
## Missing Data Analysis

**Patterns**. Missing data were analyzed using the mice package 
(van Buuren & Groothuis-Oudshoorn, 2011). Little's MCAR test indicated 
that data were missing completely at random (χ² = 147.32, df = 163, 
p = .79), supporting the appropriateness of listwise deletion.

**Handling**. Given the low overall missingness (<5% per variable) and 
MCAR mechanism, we used listwise deletion for the primary analyses. 
Sensitivity analyses using multiple imputation (m = 20 imputations) 
yielded substantively identical results (see supplementary materials).
```

#### Reporting Missing Data

Be transparent:

```markdown
**Sample Attrition**. Figure 1 presents the participant flow diagram. 
Of 1,250 invited, 847 initiated the survey (68%). Exclusions included: 
incomplete responses (n = 121), failed attention checks (n = 17), and 
straight-lining (n = 8). Additional cases were excluded due to missing 
data on key variables (n = 23), yielding a final analytical sample of 
N = 678 (54% of invited, 80% of initiated).
```

### 7. Real-Time Data Quality Monitoring

For ongoing data collection:

```r
# Weekly monitoring report

weekly_check <- function(data, week_num) {
  report <- list(
    week = week_num,
    n_new = nrow(data),
    completion_rate = mean(data$completed),
    avg_time_min = mean(data$duration_sec) / 60,
    quality_flags = sum(data$low_quality),
    missing_avg = mean(is.na(data)) * 100
  )
  
  # Alert if issues
  if (report$completion_rate < 0.75) {
    warning("Low completion rate detected")
  }
  if (report$quality_flags > nrow(data) * 0.10) {
    warning("High quality flag rate (>10%)")
  }
  
  return(report)
}

# Generate weekly reports during collection
```

## Practical Exercise

### Exercise 1: Data Quality Report

For your capstone data, create a data quality report including:

```r
# Template

quality_report <- list(
  ## Sample Description
  n_total = nrow(data),
  date_range = c(min(data$date), max(data$date)),
  
  ## Completeness
  missing_by_var = colMeans(is.na(data)) * 100,
  complete_cases = sum(complete.cases(data)),
  
  ## Validity
  out_of_range = sum(data$age < 18 | data$age > 120, na.rm = TRUE),
  logical_errors = sum(data$end_date < data$start_date, na.rm = TRUE),
  
  ## Reliability (if applicable)
  cronbach_alpha = alpha(satisfaction_items)$total$raw_alpha,
  
  ## Decisions
  exclusions = c("reason 1" = 23, "reason 2" = 17),
  final_n = 678
)

# Write narrative description for Method section
```

### Exercise 2: Create Data Dictionary

Build a complete data dictionary with:
- All variable names
- Descriptions
- Data types
- Valid ranges/values
- Missing data rates
- Special notes

Save as CSV for supplementary materials.

### Exercise 3: Missing Data Analysis

```r
# Conduct and report missing data analysis

# 1. Describe patterns
miss_var_summary(data)

# 2. Visualize
gg_miss_var(data, show_pct = TRUE)

# 3. Test MCAR
mcar_test(data)

# 4. Decide handling strategy and justify
# Write 1 paragraph explaining your approach
```

## Self-Check Questions

1. What information belongs in a data dictionary?
2. How do you calculate a response rate?
3. When is listwise deletion vs. imputation appropriate?
4. What are attention checks and why use them?
5. How should de-identified data be stored?

## Documentation Checklist

For your capstone, ensure you have:

- [ ] Data collection timeline documented
- [ ] Inclusion/exclusion criteria clearly stated
- [ ] Sample size at each stage (invited, responded, included)
- [ ] Missing data rates by variable
- [ ] Data quality checks described
- [ ] Exclusion criteria and counts
- [ ] Data dictionary created
- [ ] Storage and security procedures documented
- [ ] IRB approval referenced

## Next Week

**Week 6: Data Analysis** - Begin statistical analysis and model development with proper documentation of methods and results.

---

*Week 5 of 14 | ANLY699 Research Writing Tutorial*
