# 📊 Marketing Analytics Dashboard

## Overview
This project builds an **interactive dashboard** to track **website traffic, user behavior, and conversions** using **Google Analytics data**.

## Features
- **Visualizes traffic trends & conversion rates** using **Dash & Plotly**.
- **Dropdown filtering** to analyze performance by traffic source.
- **Dynamic insights** to optimize marketing campaigns.

## Technologies Used
- **Python** (pandas, dash, plotly, flask)
- **Google Analytics (GA4) Data**
- **Data Visualization** (Dash, Plotly)

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/vatsan01/marketing-dashboard.git
cd marketing-dashboard
pip install -r requirements.txt
```
## Dataset Format
| Date       | Channel         | Sessions | Conversion Rate|
|------------|-----------------|----------|----------------|
| 2024-01-01 | Organic Search  | 1500     | 2.5%           |
| 2024-01-02 | Paid Search     | 1200     | 3.0%           |
| 2024-01-03 | Social Media    | 800      | 1.8%           |
| 2024-01-04 | Direct Traffic  | 950      | 2.2%           |
| 2024-01-05 | Referral        | 1100     | 2.7%           |

## Running the Dashboard
python marketing_dashboard.py

## Future Enhancements
Integrate Google Analytics API for real-time data.
Add more visualizations (Bounce Rate, Avg. Session Duration).
Host the dashboard on a cloud platform.
