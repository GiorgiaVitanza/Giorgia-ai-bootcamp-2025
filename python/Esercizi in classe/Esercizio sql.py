import sqlite3
import csv

data = []
with open("Giorgia-ai-bootcamp-2025\python\Esercizi in classe\data.csv") as fd:
    reader = csv.reader(fd)
    for line in reader:
        data.append(line)


conn = sqlite3.connect("Giorgia-ai-bootcamp-2025\python\Esercizi in classe\my.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Bank (
        id INTEGER PRIMARY KEY,
        quotaAmount INTEGER,
        month INTEGER,  
        agent TEXT,
        username TEXT
    )"""
)
conn.commit()

cur.executemany(
    """INSERT INTO Bank (quotaAmount, month, agent, username) VALUES (?, ?, ?, ?)""",
    data,
)
conn.commit()


cur.close()
