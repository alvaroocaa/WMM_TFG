import sqlite3
import pandas as pd

def call_database():

    conn = sqlite3.connect('Functions\global_airports_sqlite.db')  # Replace 'your_database.db' with the actual name of your database file

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM airports;")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=column_names)
    
    df = df[(df['lat_dir'] != "U")] #Filter out columns with latitude direction == "U" wich are rows with error


    df.to_excel('airports from SQL.xlsx', index=False) #Save Excel

    #Close connection
    cursor.close()
    conn.close()
