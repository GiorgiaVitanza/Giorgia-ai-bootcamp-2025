import sqlite3

conn = sqlite3.connect('Giorgia-ai-bootcamp-2025\python\Esercizi in classe\my.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            created DATE DEFAULT CURRENT_TIMESTAMP
            )''')
conn.commit()