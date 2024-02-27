"""
Aplicando ejercicios con módulos de python
"""

import random
import datetime

# a = random.sample(range(1, 30), 12)
# b = random.sample(range(1, 30), 16)
# result = [i for i in set(a) if i in b]

# print(result)

# Ejercicio con random y delimitando valores
a = random.sample(
    range(1, 50), 10
)  # sample que obtiene números dentro den rango de limitando 10 valores
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

lista = ["x", "y", "z"]
print(random.sample(lista, 2))

# Calcular en cuanto años se cumple 100
name = input("ingrese su nombre: ")
age = int(input("ingrese su edad: "))

while age <= 0:
    age = int(input("ingrese su edad correcta: "))
now = datetime.datetime.now().year
x = (100 - age) + now
print(type(now))
print(
    "su nombre es "
    + str(name)
    + " su edad es "
    + str(age)
    + " cumplirá cien años en "
    + str(x)
)
