"""
Q21. Write a program to connect to a database and create a table.
"""

import sqlite3

# Step 1: Connect to database ( if file is not pesent it will created )
conn = sqlite3.connect("student.db")

# Step 2: create Cursor object 
cursor = conn.cursor()

# Step 3: Table create 
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Step 4: Changes save permanent
conn.commit()

# Step 5: Connection close
conn.close()

print("Database connected and table created successfully.")

