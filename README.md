# Sales Performance Analysis

## Overview

This script calculates a **Customer Score** based on two key factors—**Total Amount Spent** and **Customer Ratings**—to identify the top 10 customers from a retail dataset. It then determines the most frequented store for each top customer and saves this information in a CSV file. The script uses **Pandas** for data manipulation and **Matplotlib** for visualization (though not in the current version).

## Dependencies

Make sure the following Python libraries are installed before running the script:

- **pandas**: For data manipulation and analysis.
- **matplotlib**: (optional) Used for visualization if expanded.

To install the required libraries, you can run:

```bash
pip install pandas matplotlib
```

## Data Requirements

- The input data file should be a CSV named `new_retail_data.csv` located in the `../data/` directory.
- The CSV file must include the following columns:
  - `Name`: Customer name.
  - `Total_Amount`: Total spending of the customer.
  - `Ratings`: Customer satisfaction ratings.
  - `Product_Brand`: Brand/store information for products purchased.

## Steps in the Script

1. **Load Data**:

   - The script reads in customer data from a CSV file using the Pandas `read_csv()` function.

2. **Calculate Customer Score**:

   - A weighted score is calculated for each customer using the following formula:
     ```python
     Customer_Score = (0.7 * Total_Amount) + (0.3 * Ratings)
     ```
     where `w1 = 0.7` and `w2 = 0.3` are weights assigned to Total Amount and Ratings, respectively.

3. **Identify Top 10 Customers**:

   - The script sorts the customers by their Customer Score in descending order and selects the top 10.

4. **Find Most Frequented Store**:

   - For each of the top 10 customers, the script identifies their most frequented store (determined by the most purchased product brand).

5. **Output Table**:

   - The script generates a table showing the top 10 customers and their most frequented store, printing it in the console.

6. **Save Results**:
   - The table is saved as a CSV file named `top_customer_stores.csv` in the current working directory.

## Output

- A CSV file called `top_customer_stores.csv` containing two columns:
  - `Name`: The name of the top customers.
  - `Most Frequented Store`: The store they frequent the most.

## Future Enhancements

- Add visualization options, such as bar charts or pie charts, for more intuitive data representation.
- Expand the scoring system to include more factors like **purchase frequency** or **customer lifetime value**.

## How to Run the Script

1. Ensure the input file (`new_retail_data.csv`) is in the `../data/` directory.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Check the output CSV file (`top_customer_stores.csv`) in your current directory.

Feel free to modify the code to suit your data or scoring needs!
