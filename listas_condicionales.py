"""
Aplicando ejercidos de if y for
"""

palindrome = input("ingrese palabra: ")
res = palindrome[::-1]

if palindrome == res:
    print("This word is a palindrome \n palindrome: " + res)
else:
    print("This word is not a palindrome \n palindrome: " + res)

"""
Lista para encontrar números que sea pares
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_pares = []
for pares in a:
    if pares % 2 == 0:
        lista_pares.append(pares)
print(lista_pares)

"""
Verificación si el número es impar, par y múltiplo de 4
"""
number = int(input("Ingrese un numero: "))

if number % 2 == 0 and number % 4 == 0:
    print("es numero par y múltiplo de 4")
elif number % 2 == 0:
    print("numero es par")
else:
    print("es numero impar")

# Calcular valores menores 5
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num_menores = []
for menor in lista:
    if menor < number:
        num_menores.append(menor)
print(num_menores)

"""
Aplicando listas inversas
"""
números = []
for x in range(1, 101):
    números.append(x)
print(números)
print("-----------------------------")
números.reverse()  # lista invertida con método reverse()
print(números)

lista = [1, 2, 3, 4, 5]
res = []
for i in lista:
    inversa = [lista[-i]]
    print(inversa)
    res.append(inversa[0])
print(res)

"""
Ejercicio de encontrar valores iguales.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21, 10, 11, 12, 13]

num_repetidos = []
for x in a:
    for y in b:
        if [x] == [y]:
            num_repetidos.append(x)
print(num_repetidos[1:])

print(set(a).intersection(set(b)))  # -> función de intersección

"""
Lista para obtener el numero repetido
"""
myList = [1, 8, 9.8, 8, 10]

res = []
print(len(myList))

for n in range(len(myList)):
    for r in range(len(myList)):
        if n != r:
            if myList[n] == myList[r] and myList[n] not in res:
                res.append(myList[n])
                print(res)

"""
Ejercicios adicionales
"""


def list_ends(a_list):
    return [a_list[0], a_list[len(a_list) - 1]]


print(list_ends([5, 10, 15, 20, 25]))

# compresiones
x = int(input())
y = int(input())
z = int(input())
n = int(input())

out = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(out)
