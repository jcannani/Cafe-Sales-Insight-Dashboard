import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Cafe Sales Interactive Dashboard')

# Load the clean dataset
df = pd.read_csv('cleaned_data.csv')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Sidebar filters
item_filter = st.sidebar.selectbox('Filter by Item', df['Item'].unique())
date_range = st.sidebar.date_input('Select Date Range', [df['Transaction Date'].min(), df['Transaction Date'].max()])

# Apply filters
filtered_df = df[
    (df['Item'] == item_filter) &
    (df['Transaction Date'] >= pd.to_datetime(date_range[0])) &
    (df['Transaction Date'] <= pd.to_datetime(date_range[1]))
]

# Group data by date (daily total sales)
daily_sales = filtered_df.groupby('Transaction Date', as_index=False)['Total Spent'].sum()

# Show a chart
fig = px.line(daily_sales, x='Transaction Date', y='Total Spent', title=f'Sales Over Time for {item_filter}')
st.plotly_chart(fig)

# Show data summary
st.write('Summary Table', filtered_df.describe())