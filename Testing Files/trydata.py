#This is the file for me to practice my database knowledge

import sqlite3
connection = sqlite3.connect("people.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Shayaan", 18))
connection.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)