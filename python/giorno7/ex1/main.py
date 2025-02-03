import random
import csv
import datetime


list_attempts = []
attempts = 0
x_ok = random.randint(1,100)
print('Indovina il numero tra 1 e 100!')

count_record = 0
while True:    
    try:
        with open('Giorgia-ai-bootcamp-2025\python\giorno7\ex1\HighScore.csv','r') as fd2:
            content = fd2.readline()
            high_score = content[2]
            

        x = int(input('?'))
        attempts += 1
        if x == x_ok:     
            print(f"Hai indovinato! Tentativi: {attempts}")  
            list_attempts.append(attempts)
            high_score = min(list_attempts)
            if attempts == high_score:
                count_record += 1 
                name_winner = input('Hai fatto un nuovo record! Scrivi il tuo nome:')
                with open('Giorgia-ai-bootcamp-2025\python\giorno7\ex1\HighScore.csv','w') as fd:
                    writer = csv.writer(fd)
                    writer.writerow([count_record, name_winner, high_score, f"Date: {datetime.datetime.now()}"])
            attempts = 0
            
            
            decision = input('Vuoi continuare a giocare? (scrivi sì o no): ')
            if decision == 'sì':
                continue
            elif decision == 'no':
                print(f"Il record appartiene a: {name_winner}")
                break
            else:
                input("errore! Scrivi sì o no")
        elif x < x_ok:           
            print("Troppo basso")
        else:            
            print("Troppo alto")
        

    except ValueError:
        print("Input errato. Riprova.")
        continue
        
# Rendere persistente il high score salvando su file, in
# formato JSON oppure CSV (a scelta della programmatrice), 
# i dati seguenti:
#  - nome del giocatore
#  - numero di tentativi fatti
#  - data e ora del record



