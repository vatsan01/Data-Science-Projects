# 📈 Sales Forecasting Model

## Overview
This project predicts **future sales trends** using **Time Series Analysis** with **ARIMA & Prophet**.

## Features
- **Forecasts monthly sales** based on historical data.
- **Compares ARIMA vs Prophet models** for accuracy.
- **Visualizes sales trends** for better decision-making.

## Technologies Used
- **Python** (pandas, statsmodels, Prophet, matplotlib)
- **Time Series Forecasting** (ARIMA, Prophet)
- **Data Visualization** (Matplotlib)

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/vatsan01/sales-forecasting.git
cd sales-forecasting
pip install -r requirements.txt
```
## Dataset Format 
| Date       | Sales |
|------------|-------|
| 2023-01-01 | 2500  |
| 2023-02-01 | 2700  |
| 2023-03-01 | 2600  |
| 2023-04-01 | 2800  |
| 2023-05-01 | 3000  |

## Running the Forecast
python sales_forecasting.py

Future Enhancements
Improve accuracy using hyperparameter tuning.
Deploy as an API for business intelligence integration.
Add real-time sales data ingestion.
