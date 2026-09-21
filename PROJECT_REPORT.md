# Netflix Data Analytics Project Report

## 1. Executive Summary
This project analyzes the Netflix Movies and TV Shows dataset using an end-to-end data analytics workflow. The raw dataset contains **8,807 records and 12 original columns**. The analysis covers data quality, preprocessing, exploratory analysis, Python-based visualization, SQL analysis, Excel reporting, KPIs and an interactive dashboard.

## 2. Dataset Overview
- Rows: **8,807**
- Original columns: **12**
- Movies: **6,131**
- TV Shows: **2,676**
- Unique countries represented after primary-country extraction: **86**
- Duplicate rows detected: **0**
- Date-added range: **01 January 2008 to 25 September 2021**

## 3. Data Quality
Missing values were found mainly in director, cast, country, date_added, rating and duration. No duplicate rows were detected in the supplied file. Missing analytical categorical values were labeled **Unknown** rather than silently dropping those records.

### Missing values in the original dataset
show_id            0
type               0
title              0
director        2634
cast             825
country          831
date_added        10
release_year       0
rating             4
duration           3
listed_in          0
description        0

## 4. Data Cleaning & Transformation
- Trimmed whitespace from text fields.
- Converted `date_added` to a proper date type.
- Created year/month fields from `date_added`.
- Extracted numeric duration into `duration_value`.
- Extracted duration units into `duration_unit`.
- Created `listed_in_primary` from the first listed genre.
- Created `country_primary` from the first listed country.
- Labeled missing analysis fields as `Unknown`.

## 5. Exploratory Data Analysis

### Content Type
   Type  Titles
  Movie    6131
TV Show    2676

### Top 10 Primary Genres
                   Genre  Titles
                  Dramas    1600
                Comedies    1210
      Action & Adventure     859
           Documentaries     829
  International TV Shows     774
Children & Family Movies     605
          Crime TV Shows     399
                Kids' TV     388
         Stand-Up Comedy     334
           Horror Movies     275

### Top 10 Countries
       Country  Titles
 United States    3211
         India    1008
United Kingdom     628
        Canada     271
         Japan     259
        France     212
   South Korea     211
         Spain     181
        Mexico     134
     Australia     117

### Top Ratings
Rating  Titles
 TV-MA    3207
 TV-14    2160
 TV-PG     863
     R     799
 PG-13     490
 TV-Y7     334
  TV-Y     307
    PG     287
  TV-G     220
    NR      80

## 6. Key Findings
1. The dataset contains **8,807 Netflix titles**.
2. Movies account for **69.6%** of records, while TV Shows account for **30.4%**.
3. The primary-genre analysis shows which categories have the largest representation in the supplied dataset.
4. Country analysis identifies the leading countries represented in the catalog.
5. Release-year analysis can be used to identify periods of increased Netflix content production.
6. The date-added analysis provides a view of when titles entered the Netflix catalog.
7. Missing-value handling is important because director, cast and country are incomplete for a meaningful share of records.

## 7. Python
Python was used for loading, cleaning, feature engineering, KPI calculation and visualization with Pandas, NumPy, Matplotlib and Seaborn.

## 8. SQL
SQL queries were prepared for total titles, content type, release trends, ratings, genres, countries, duration and season analysis.

## 9. Excel
An Excel workbook was created with KPI, data-quality, content-type, genre, country, rating and trend sheets.

## 10. Dashboard
An interactive Plotly HTML dashboard was created with:
- Total Titles KPI
- Movies KPI
- TV Shows KPI
- Countries KPI
- Movies vs TV Shows chart
- Release-year trend
- Top genres
- Top countries

## 11. Portfolio Value
This project demonstrates practical skills in:
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Python/Pandas/NumPy
- SQL
- Excel
- Data visualization
- Dashboard development
- Business-oriented insight generation

## 12. Files
- `netflix_analysis.py` — Python analysis code
- `netflix_analysis.sql` — SQL queries
- `requirements.txt` — Python dependencies
- `Netflix_Analysis.xlsx` — Excel analysis workbook
- `Netflix_Dashboard.html` — Interactive dashboard
- `netflix_movies (1).csv` — Original dataset

## 13. Conclusion
The project converts a raw Netflix catalog into a structured analytical dataset and presents the results through Python, SQL, Excel and an interactive dashboard. The workflow is suitable for demonstrating an end-to-end Data Analyst project in a portfolio or interview.
