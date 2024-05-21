"""
Aplicando ejercicios con módulos de python
"""

import random
import datetime

a = random.sample(range(1, 30), 12)  # sample recupera valores de una lista.
b = random.sample(range(1, 30), 16)
# recorre las lista y luego verifica si hay valores iguales en la lista b.
result = [i for i in set(a) if i in b]

print(result)

"""
Ejercicio con random y delimitando valores com sample
"""
# sample que obtiene números dentro den rango de limitando 10 valores
a = random.sample(range(1, 50), 10)
b = random.sample(range(1, 50), 12)
print(a)
print(b)
list = []
a = set(a)
b = set(b)
for i in a:
    if i in b:
        list.append(i)
print(list)

"""
Calcular en cuanto años se tendrá 100 años
"""
name = input("ingrese su nombre: ")
age = int(input("ingrese su edad: "))

while age <= 0:
    age = int(input("ingrese su edad correcta: "))

now = datetime.datetime.now().year
x = (100 - age) + now
print(
    "su nombre es "
    + str(name)
    + " su edad es "
    + str(age)
    + " cumplirá cien años en "
    + str(x)
)

"""
funciones con listas y iteraciones  con condicionales
"""
lista = [1, 2, 5, 3, 3, 8, 9, 10, 2]


# función para buscar elementos duplicados y agregar en un nuevo array
def duplicado(x):
    d = []
    for i in x:
        if i not in d:
            d.append(i)
    return d


# set para interceptar números duplicados en un función
def duplicado_v2(x):
    return list(set(x))


print(lista)
print(duplicado(lista))
print(duplicado_v2(lista))
