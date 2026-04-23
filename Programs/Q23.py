"""
Q23. Demonstrate transaction control (commit and rollback) in database
operations.
"""

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

try:
    # INSERT (not committed yet)
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Ravi", 23))

    # Commit the transaction
    conn.commit()
    print("Data committed successfully.")

    # Another INSERT (will be rolled back)
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Error", 99))

    # Force an error
    x = 1 / 0

    conn.commit()

except:
    # Rollback if any error occurs
    conn.rollback()
    print("Transaction rolled back due to error.")

finally:
    conn.close()