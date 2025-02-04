import random
import csv
import datetime


list_attempts = []
attempts = 0
x_ok = random.randint(1,100)
print('Indovina il numero tra 1 e 100!')

list_high_score = []
   
try:
    with open('Giorgia-ai-bootcamp-2025\python\giorno7\ex1\HighScore.csv','r',newline="") as fd2:
        content = list(csv.reader(fd2))
        if content != []:
            high_score = content[0][1]
            name_winner = content[0][0]
            for line in content:
                list_attempts.append(int(line[1]))
        else:
            content = ['Nobody',100,'Never']
            list_attempts.append(content[1])                    

        while True:         
            try:
                x = int(input('?'))
            except ValueError:
                print("Value Error, an integer expected")
                x = int(input('?'))

            attempts += 1
            if x == x_ok:     
                print(f"Hai indovinato! Tentativi: {attempts}")  
                list_attempts.append(attempts)
                high_score = min(list_attempts)
                if attempts == high_score:
                    name_winner = input('Hai fatto un nuovo record! Scrivi il tuo nome:')
                    with open('Giorgia-ai-bootcamp-2025\python\giorno7\ex1\HighScore.csv','w',newline="") as fd:
                        writer = csv.writer(fd)
                        list_high_score.append([name_winner, int(high_score), f"Date: {datetime.datetime.now()}"])

                        print(list_high_score)
                        sort_list = sorted(list_high_score,key= lambda li: li[1],reverse=True)
                        name_winner = sort_list[0][0]
                        
                        for line in sort_list:
                            writer.writerow(line)
                attempts = 0
                
                
                
                decision = input('Vuoi continuare a giocare? (scrivi sì o no): ')
                if decision == 'sì':
                    continue
                elif decision == 'no':
                    print(f"Il record appartiene a: {name_winner}")
                    break
                else:
                    print("errore! Scrivi sì o no")
                    continue
            elif x < x_ok:           
                print("Troppo basso")
            else:            
                print("Troppo alto")
    

        




except FileNotFoundError:
    print("file vuoto o non esistente")
    