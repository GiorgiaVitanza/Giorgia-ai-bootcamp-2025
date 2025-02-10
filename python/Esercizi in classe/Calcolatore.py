while True:
    text = input(">>> ")
    if text == "quit":
        print("bye")
        break
    else:
        num1, sign, num2 = text.split()
        if sign == "+":
            print(float(num1) + float(num2))
        elif sign == "-":
            print(float(num1) - float(num2))
        else:
            print("operazione non riconosciuta")
            continue
