number = int(input("Ingrese un numero: "))

# if number % 2 == 0 and number % 4 == 0:
#     print("es numero par y múltiplo de 4")
# elif number %2 == 0:
#     print("numero es par")
# else:
#     print("es numero impar")

#calcular valores menores 5

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num_menores=[]
for menor in lista:
    if menor < number:
        num_menores.append(menor)
print(num_menores)
