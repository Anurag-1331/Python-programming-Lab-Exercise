"""
Q22. Write a program to perform INSERT, UPDATE, DELETE,
and SELECT operations on a database.
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

# INSERT
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Rahul", 20))

# UPDATE
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, "Rahul"))

# DELETE
cursor.execute("DELETE FROM students WHERE name = ?", ("Rahul",))

# INSERT again for SELECT demo
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Amit", 22))

# SELECT
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()