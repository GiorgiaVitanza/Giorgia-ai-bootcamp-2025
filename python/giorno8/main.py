import csv
import sqlite3

with open("Giorgia-ai-bootcamp-2025\python\giorno8\students.csv") as fd:
    reader = csv.reader(fd)
    data = []
    for line in reader:
        for el in line:
            data.append(el.split(';'))

conn = sqlite3.connect("Giorgia-ai-bootcamp-2025\python\giorno8\dataStudents.db")
cur = conn.cursor()

cur.execute(
    '''CREATE TABLE  IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_of_birth INTEGER,
    gender TEXT,
    email TEXT,
    assignments DEFAULT 0
    )
'''
)

conn.commit()

cur.executemany(
    "INSERT INTO students (id, first_name, last_name, year_of_birth, gender, email,  assignments) VALUES (?,?,?,?,?,?,?)", data
)
conn.commit()
cur.close()