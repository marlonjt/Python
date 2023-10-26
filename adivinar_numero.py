import random

num = int(input("Ingrese un numero del 1 al 9: "))

num_ran = random.randint(1, 10)

intentos = 0

while True:
    if num > num_ran:
        print("Ops el número es mayor al número aleatorio!!")
    elif num < num_ran:
        print("Ops el número es menor al número aleatorio!!")
    elif num == num_ran:
        print("Adivinaste el número !!")
        print("Gracias por jugar !!!")
        break

    txt = input("terminar juego? S/N ")
    if txt.lower() == "s":
        print("gracias por jugar")
        break
    elif txt.lower() == "n":
        num = int(input("ingresa nuevamente un número: "))
        intentos += 1
        if intentos == 3:
            print(
                "gracias por jugar te quedaste sin intentos, el número correcto es el :"
                + str(num_ran)
            )
            break
