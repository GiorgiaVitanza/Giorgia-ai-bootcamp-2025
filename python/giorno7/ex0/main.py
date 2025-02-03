import csv

with open("Giorgia-ai-bootcamp-2025\python\giorno7\ex0\data.csv") as fd:
     reader = csv.reader(fd)
     data = []
     for line in reader:
          #1. carichi i dati tabellari presenti nel file CSV [`data.csv`](data.csv) in memoria       
          data.append(line)
          
    

    #2. riorganizzi le righe in ordine alfabetico crescente in base al *cognome* delle persone
     def sort_surname(li):
        return li[1]
     
     new_data = sorted(data[1:], key = sort_surname)

#      Stampi le righe ordinate aggiungendo il numero sequenziale (indice)  di ciascuna riga. 
     index = 0
     for row in new_data:
        index += 1
        print([index]+row)

    #scrivere un nuovo file chiamato `data2.csv` in formato CSV con le righe ordinate (senza indice)
     with open('Giorgia-ai-bootcamp-2025\python\giorno7\ex0\data2.csv','w') as fd2:
        writer = csv.writer(fd2)
        for line in new_data:
            writer.writerow(line)
     
     
     



   
    


    
    

    