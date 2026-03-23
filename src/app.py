import streamlit as st
import pandas as pd
from src.model import forecast_next_periods
from src.ai_insights import generate_ai_insights

st.title("FP&A Automation Engine")

df = pd.read_csv('data/financials.csv')

# Inputs
growth = st.slider("Revenue Growth %", 0.0, 0.2, 0.05)

# Forecast
forecast_df = forecast_next_periods(df)

st.subheader("Forecast Output")
st.write(forecast_df)

# AI Insights
st.subheader("AI Insights")
st.write(generate_ai_insights(df))
