# import libraries
import pandas as pd

# Load dataset
df = pd.read_csv('data/financials.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort values
df = df.sort_values('Date')

# --- Core Financial Calculations ---

# Total Costs
df['Total Costs'] = df['Salary Cost'] + df['Marketing'] + df['Other Costs']

# Profit
df['Profit'] = df['Revenue'] - df['Total Costs']

# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Revenue']

# Revenue Growth
df['Revenue Growth %'] = df['Revenue'].pct_change()

print(df.tail())

# --- Forecasting Logic ---

def forecast_next_periods(df, periods=3):
    last_row = df.iloc[-1]
    forecast_rows = []

    for i in range(periods):
        new_row = last_row.copy()

        # Assumptions
        new_row['Revenue'] *= 1.05
        new_row['Salary Cost'] *= 1.02
        new_row['Marketing'] *= 1.03

        # Recalculate
        new_row['Total Costs'] = new_row['Salary Cost'] + new_row['Marketing'] + new_row['Other Costs']
        new_row['Profit'] = new_row['Revenue'] - new_row['Total Costs']
        new_row['Profit Margin'] = new_row['Profit'] / new_row['Revenue']

        forecast_rows.append(new_row)
        last_row = new_row

    return pd.DataFrame(forecast_rows)

forecast_df = forecast_next_periods(df)

print(forecast_df)

# --- Insight Generation ---

def generate_insights(df):
    latest = df.iloc[-1]
    insights = []

    profit_margin = latest['Profit Margin']
    marketing_ratio = latest['Marketing'] / latest['Revenue']
    growth = latest['Revenue Growth %']

    # Profitability insight
    if profit_margin < 0.2:
        insights.append("⚠️ Profit margin below 20% - cost pressure detected")
    else:
        insights.append("✅ Profitability is healthy")

    # Marketing efficiency
    if marketing_ratio > 0.3:
        insights.append("⚠️ Marketing spend is high relative to revenue")
    else:
        insights.append("✅ Marketing spend is within reasonable range")

    # Growth insight
    if pd.notna(growth):
        if growth < 0.02:
            insights.append("⚠️ Revenue growth is slowing")
        else:
            insights.append("✅ Revenue growth is stable")

    return insights

print(generate_insights(df))
