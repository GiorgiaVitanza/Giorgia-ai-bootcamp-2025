import csv
import sqlite3


with open("Giorgia-ai-bootcamp-2025\python\giorno8\students.csv") as fd:
    reader = csv.reader(fd)
    next(reader)
    data = []
    for line in reader:
        for el in line:
            data.append(el.split(';'))

conn = sqlite3.connect("Giorgia-ai-bootcamp-2025\python\giorno8\dataStudents.db")
cur = conn.cursor()

cur.execute( "DROP TABLE students")

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

#gli studenti nati nell'anno 2000
cur.execute("SELECT first_name, last_name FROM students WHERE  year_of_birth = 2000")

#la persona che ha consegnato il maggior numero di assignments (usando `MAX()` in SQL o in Python)
cur.execute("SELECT assignments FROM students")

assignments = cur.fetchall()
max_assignments = max(assignments)
cur.execute("SELECT first_name, last_name FROM students WHERE assignments = (?)",max_assignments)
print(cur.fetchall())
#il cognome delle studentesse di nome "Jane"
cur.execute("SELECT last_name FROM students WHERE first_name = 'Jane'")
print(cur.fetchall())
#stampare la graduatoria degli studenti ordinati in base al numero di assignment usando `ORDER BY` (non farlo in Python!)
cur.execute("SELECT first_name,last_name FROM students ORDER BY assignments")
print(cur.fetchall())
cur.execute("SELECT first_name,last_name FROM students ORDER BY assignments DESC")
print(cur.fetchall())

cur.execute("ALTER TABLE students DROP COLUMN assignments")
conn.commit()
cur.execute("SELECT * FROM students")



with open("Giorgia-ai-bootcamp-2025\python\giorno8\dataStudentsNoAssignments.csv",'w') as fd2:
    writer = csv.writer(fd2)
    for line in cur.fetchall():
        print(line)
        writer.writerow(line)
## Bonus
'''Creare un altro database (con un nome diverso) definendo una seconda tabella con i seguenti campi:
 - id
 - data di consegna di un assignment

Creare due file CSV con la colonna assignment rimossa nella prima tabella `students`. Provare
a replicare i risultati della prima parte dell'esercizio creando dati fittizi e usando
le `JOIN`.'''
conn2 = sqlite3.connect("Giorgia-ai-bootcamp-2025\python\giorno8\SecondStudents.db")
cur2 = conn2.cursor()

#cur2.execute("DROP TABLE SecondStudents")

cur2.execute(
    '''CREATE TABLE  IF NOT EXISTS SecondStudents(
    id INTEGER PRIMARY KEY,
    date INTEGER    
    )
'''
)

conn2.commit()
cur2.close()