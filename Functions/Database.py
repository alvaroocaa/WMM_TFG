import sqlite3
import pandas as pd

def call_database():

    conn = sqlite3.connect('global_airports_sqlite.db') 

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Airport_database;")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=column_names)
    
    cursor.execute("""
    DELETE FROM Airport_database
    WHERE elevation_ft = '' OR elevation_ft IS NULL
""")

    df.to_excel('airports from SQL.xlsx', index=False) #Save Excel

    #Close connection
    cursor.close()
    conn.close()
