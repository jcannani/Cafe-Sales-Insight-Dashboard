import pandas as pd

# Load the raw dataset
df = pd.read_csv('cafe_sales.csv')

# Convert text-based numbers into real numbers
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')

# Why: errors='coerce' replaces bad values like "ERROR" with NaN (null values)

# Drop rows missing key info
df = df.dropna(subset=['Item','Quantity', 'Price Per Unit', 'Total Spent'])

# Optional cleanup (replace unknowns w/proper nulls)
df['Payment Method'] = df['Payment Method'].replace(['UNKNOWN', ''], pd.NA)
df['Location'] = df['Location'].replace(['UNKNOWN',''], pd.NA)

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

print('Data cleaned and saved')

