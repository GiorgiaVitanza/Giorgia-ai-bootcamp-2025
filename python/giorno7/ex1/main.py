import random
import csv
import datetime



def sorted_csv(fileName,list_high_score):
    #when the program finishes we want to save the data on the csv file
    with open(fileName,'w',newline="") as fd:
        writer = csv.writer(fd)             
        sort_list = sorted(list_high_score,key= lambda li: int(li[1]),reverse=False)
        name_winner = sort_list[0][0]
        
        for line in sort_list:
            writer.writerow(line)
        return name_winner


list_attempts = []
attempts = 0
x_ok = random.randint(1,100)
print('Indovina il numero tra 1 e 100!')

list_high_score = []
   
try:
        while True:   
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
                    name_winner = 'Nobody'           
            try:
                x = int(input('?'))
            except ValueError:
                print("Value Error, an integer expected")
                x = int(input('?'))

            attempts += 1
            if x == x_ok:     
                #win the match
                print(f"Hai indovinato! Tentativi: {attempts}")  
                #collect the number of attempts to determine the high score
                list_attempts.append(attempts)   
                high_score = min(list_attempts)
                if attempts == high_score:
                    # when the player reaches the higher score we want to know his name
                    name_winner = input('Hai fatto un nuovo record! Scrivi il tuo nome:') 
                    # in the following list we save the name the high score and the date
                    list_high_score.append([name_winner, int(high_score), f"Date: {datetime.datetime.now()}"])
                    if content != ['Nobody',100,'Never']:
                            list_high_score.append(content[0])
                    
                
                
                #decision to continue or not
                decision = input('Vuoi continuare a giocare? (scrivi sì o no): ')
                if decision != 'sì' and decision != 'no':
                    print("errore! Scrivi sì o no senza spazi")
                    decision = input('Vuoi continuare a giocare? (scrivi sì o no): ')
                elif decision == 'sì':
                    # if we continue the attempts are set to zero again
                    attempts = 0
                    continue
                elif decision == 'no':
                    # if the player wants to quit, we want to determine the high score that corresponds to the minimum number of attempts
                    name = sorted_csv('Giorgia-ai-bootcamp-2025\python\giorno7\ex1\HighScore.csv',list_high_score)                    
                        
                    print(f"Il record appartiene a: {name}")
                    break
                
                    
            elif x < x_ok:           
                print("Troppo basso")
            else:            
                print("Troppo alto")
    

        




except FileNotFoundError:
    print("file vuoto o non esistente")
    