import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect('SQL airports database\global_airports_sqlite.db')  # Replace 'your_database.db' with the actual name of your database file

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to select all data from the 'airports' table
cursor.execute("SELECT * FROM airports;")

# Fetch all the rows
rows = cursor.fetchall()

# Get the column names
column_names = [description[0] for description in cursor.description]

# Create a DataFrame using pandas
df = pd.DataFrame(rows, columns=column_names)

# Save the DataFrame to an Excel file
df.to_excel('airports from SQL.xlsx', index=False)

# Close the cursor and connection
cursor.close()
conn.close()
