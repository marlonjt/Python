number = int(input("Ingrese un numero: "))

if number % 2 == 0 and number % 4 == 0:
    print("es numero par y múltiplo de 4")
elif number %2 == 0:
    print("numero es par")
else:
    print("es numero impar")
