# Financial model logic will go here
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