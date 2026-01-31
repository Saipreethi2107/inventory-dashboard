import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard title
st.title("Inventory Optimization & Forecasting Dashboard")
st.write("Retail analytics across 5 regional warehouses using KPI design + forecasting.")

# Load CSV
df = pd.read_csv("inventory_data.csv")

# Calculate KPIs
df['stock_to_sales'] = df['stock'] / df['sales']
df['inventory_turnover'] = df['sales'] / df['stock']

# Sidebar filters
warehouse = st.sidebar.selectbox("Select Warehouse", df['warehouse'].unique())
sku = st.sidebar.selectbox("Select SKU", df['sku'].unique())

df_filtered = df[(df['warehouse'] == warehouse) & (df['sku'] == sku)]

# Show KPIs
st.subheader("Key Metrics")
st.metric("Average Stock-to-Sales Ratio", round(df_filtered['stock_to_sales'].mean(), 2))
st.metric("Average Inventory Turnover", round(df_filtered['inventory_turnover'].mean(), 2))

# Stock & Sales over time
st.subheader("Stock & Sales Over Time")
fig1 = px.line(df_filtered, x='date', y=['stock', 'sales'], labels={'value':'Units'})
st.plotly_chart(fig1)

# Purchases vs Stock chart
st.subheader("Stock vs Purchases")
fig2 = px.bar(df_filtered, x='date', y=['stock','purchases'], barmode='group')
st.plotly_chart(fig2)
