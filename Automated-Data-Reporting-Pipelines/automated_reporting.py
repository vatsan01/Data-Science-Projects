import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

# Load Google BigQuery credentials
credentials = service_account.Credentials.from_service_account_file("bigquery_credentials.json")
client = bigquery.Client(credentials=credentials)

# Query to extract data from BigQuery
query = """
SELECT date, campaign_name, impressions, clicks, conversions, revenue
FROM `project.dataset.ad_performance`
WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
"""

# Extract Data
df = client.query(query).to_dataframe()

# Data Transformation
df["CTR"] = (df["clicks"] / df["impressions"]) * 100
df["Conversion Rate"] = (df["conversions"] / df["clicks"]) * 100
df["Revenue per Conversion"] = df["revenue"] / df["conversions"]

# Save Transformed Data
df.to_csv("ad_performance_report.csv", index=False)

print("Automated data report generated successfully!")
