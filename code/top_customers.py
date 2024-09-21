import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = '../data/new_retail_data.csv'
data_cleaned = pd.read_csv(file_path)

# Handle missing values and correct data types
data_cleaned = data_cleaned.dropna()
data_cleaned['Transaction_ID'] = data_cleaned['Transaction_ID'].astype(int)
data_cleaned['Customer_ID'] = data_cleaned['Customer_ID'].astype(int)
data_cleaned['Phone'] = data_cleaned['Phone'].astype(int)
data_cleaned['Zipcode'] = data_cleaned['Zipcode'].astype(int)
data_cleaned['Age'] = data_cleaned['Age'].astype(int)
data_cleaned['Year'] = data_cleaned['Year'].astype(int)
data_cleaned['Total_Purchases'] = data_cleaned['Total_Purchases'].astype(int)
data_cleaned['Amount'] = data_cleaned['Amount'].astype(float)
data_cleaned['Total_Amount'] = data_cleaned['Total_Amount'].astype(float)
data_cleaned['Ratings'] = data_cleaned['Ratings'].astype(float)
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])
data_cleaned['Time'] = pd.to_datetime(data_cleaned['Time'], format='%H:%M:%S').dt.time
data_cleaned = data_cleaned.drop_duplicates(subset='Transaction_ID')

# Step 1: Customer Segmentation
data_cleaned['Customer_Segment'] = pd.qcut(data_cleaned['Total_Amount'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

# Step 2: Visualization
plt.figure(figsize=(12, 6))

# Bar chart for Customer Segments
plt.subplot(1, 2, 1)
sns.countplot(x='Customer_Segment', data=data_cleaned, palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Segment')
plt.ylabel('Count')

# Scatter plot for Total Amount vs. Ratings
plt.subplot(1, 2, 2)
sns.scatterplot(x='Total_Amount', y='Ratings', hue='Customer_Segment', data=data_cleaned, palette='viridis')
plt.title('Total Amount vs. Ratings')
plt.xlabel('Total Amount')
plt.ylabel('Ratings')

plt.tight_layout()
plt.show()
