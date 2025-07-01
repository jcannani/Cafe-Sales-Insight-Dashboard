import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clean dataset
df = pd.read_csv('cleaned_data.csv')

# Convert data column to datatime type
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Create a monthly sales summary
monthly_sales = df.groupby(df['Transaction Date'].dt.to_period('M'))['Total Spent'].sum()

# Plot monthly sales
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Cafe Sales')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()
