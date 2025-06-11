# Automated Data Reporting Pipelines

## Overview
This project automates **marketing data extraction, transformation, and reporting** using an **ETL pipeline**.

## Features
- Extracts **marketing campaign data** from **Google BigQuery**
- Transforms data to **calculate KPIs** like **CTR, Conversion Rate, Revenue per Conversion**
- Saves reports as a **CSV file** for further analysis

## Technologies Used
- **Python** (pandas, google-cloud-bigquery)
- **Database** (Google BigQuery)
- **ETL Automation** (SQL queries, pandas)

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourgithub/automated-data-reporting-pipelines.git
cd automated-data-reporting-pipelines
pip install -r requirements.txt
```
## Usage
Configure your Google BigQuery Credentials (bigquery_credentials.json).
Run the script to generate reports:
python automated_reporting.py

## Dataset Format
This script extracts data with the following columns:

| Date       | Campaign Name | Impressions | Clicks | Conversions | Revenue |
|------------|---------------|-------------|--------|-------------|---------|
| 2024-01-01 | Campaign A    | 10,000      | 200    | 50          | 500     |
| 2024-01-02 | Campaign B    | 15,000      | 250    | 60          | 700     |
| 2024-01-03 | Campaign C    | 12,000      | 300    | 70          | 650     |

## Future Enhancements
Connect the pipeline to Google Sheets / Power BI for dynamic reporting.
Add APIs to fetch real-time marketing data.
Automate scheduling via cron jobs.

