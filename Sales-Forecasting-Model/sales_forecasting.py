import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from fbprophet import Prophet

# Load sales data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

# Train ARIMA Model
arima_model = ARIMA(df["Sales"], order=(5,1,0))
arima_fit = arima_model.fit()
df["ARIMA_Forecast"] = arima_fit.predict(start=len(df)-12, end=len(df)+12, dynamic=True)

# Train Prophet Model
prophet_df = df.reset_index()[["Date", "Sales"]].rename(columns={"Date": "ds", "Sales": "y"})
prophet_model = Prophet()
prophet_model.fit(prophet_df)
future = prophet_model.make_future_dataframe(periods=12, freq='M')
forecast = prophet_model.predict(future)

# Plot Results
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Sales"], label="Actual Sales")
plt.plot(df.index, df["ARIMA_Forecast"], label="ARIMA Forecast")
plt.plot(forecast["ds"], forecast["yhat"], label="Prophet Forecast")
plt.legend()
plt.title("Sales Forecasting")
plt.show()
