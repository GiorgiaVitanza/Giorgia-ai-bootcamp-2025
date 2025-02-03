import random
count = 0
x_ok = random.randint(1,100)
print('Indovina il numero tra 1 e 100!')
while True:    
    try:
        x = int(input('?'))
        count += 1
        if x == x_ok:            
            print(f"Hai indovinato! Tentativi: {count}")
        elif x < x_ok:           
            print("Troppo basso")
        elif x > x_ok:            
            print("Troppo alto")
        

    except ValueError:
        print("Input errato. Riprova.")
        



