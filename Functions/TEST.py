import sqlite3

def call_database():
    try:
        conn = sqlite3.connect('global_airports_sqlite.db') 
        cursor = conn.cursor()
        
        # Fetch all table names
        cursor.execute(".tables;")
        tables = cursor.fetchall()
        
        # Print the table names
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
        
        conn.close()  # Close the connection when done
        
    except sqlite3.Error as e:
        print("An error occurred:", e)

call_database()
