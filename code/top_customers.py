import pandas as pd
import matplotlib.pyplot as plt

# Load your data into a Pandas DataFrame
data = pd.read_csv('../data/new_retail_data.csv')

# Calculate Customer Score
w1 = 0.7
w2 = 0.3
data['Customer_Score'] = (w1 * data['Total_Amount']) + (w2 * data['Ratings'])

# Get the top 10 customers based on Customer Score
top_customers = data.sort_values(by='Customer_Score', ascending=False).head(10)

# Find the most frequented store for each top customer
most_frequented_stores = top_customers.groupby('Name')['Product_Brand'].agg(lambda x: x.value_counts().index[0])

# Create a DataFrame for the table
top_customer_stores = pd.DataFrame({
    'Name': most_frequented_stores.index,
    'Most Frequented Store': most_frequented_stores.values
})

# Print the table
print(top_customer_stores)


# Since we are dealing with categorical data (store names),
# a bar chart is not the most suitable visualization.
# Instead, we can display the information in a table format.

# Export the table to a new CSV file in ../results/
top_customer_stores.to_csv('../results/top_customer_stores.csv', index=False)
