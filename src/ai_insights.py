from openai import OpenAI
import pandas as pd

client = OpenAI()

def generate_ai_insights(df):
    latest = df.iloc[-1]

    prompt = f"""
    You are a financial analyst.

    Analyze the following company metrics:

    Revenue: {latest['Revenue']}
    Profit: {latest['Profit']}
    Profit Margin: {latest['Profit Margin']}
    Marketing Spend: {latest['Marketing']}
    Revenue Growth: {latest['Revenue Growth %']}

    Provide 3 concise insights about performance, risks, and trends.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
