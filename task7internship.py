# Importing required libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create and connect to the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create a table and insert dummy sales data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')

# Insert sample data (you can modify this)
sample_data = [
    ("Shoes", 10, 50.0),
    ("Shoes", 5, 55.0),
    ("T-Shirts", 20, 15.0),
    ("T-Shirts", 10, 17.0),
    ("Jeans", 7, 40.0),
    ("Jeans", 8, 42.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 3: Run SQL query to get sales summary
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 4: Print the result
print("Sales Summary:")
print(df)

# Step 5: Plot bar chart for revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close the database connection
conn.close()
