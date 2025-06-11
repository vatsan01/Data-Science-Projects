import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash.dependencies as dd

# Load Google Analytics Data (Ensure your dataset is in the correct format)
df = pd.read_csv("marketing_analytics.csv")

# Data Preprocessing
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Marketing Analytics Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(id="traffic_trend"),
    
    dcc.Dropdown(
        id="channel_dropdown",
        options=[{"label": x, "value": x} for x in df["Channel"].unique()],
        value="Organic Search",
        multi=False,
        placeholder="Select Traffic Channel",
    ),
    
    dcc.Graph(id="conversion_rate"),
])

@app.callback(
    dd.Output("traffic_trend", "figure"),
    [dd.Input("channel_dropdown", "value")]
)
def update_traffic(selected_channel):
    filtered_df = df[df["Channel"] == selected_channel]
    fig = px.line(filtered_df, x="Date", y="Sessions", title=f"Traffic Trend for {selected_channel}")
