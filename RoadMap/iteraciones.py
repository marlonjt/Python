"""
Iteraciones y bucles
"""

import random

for i in range(1, 11):
    print(i, end=",")

i = 0
while i < 10:
    i += 1
    print(i, end=",")


def iteraciones(number):
    if number <= 10:
        print(number, end=",")
        return iteraciones(number + 1)


print(iteraciones(1))


for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")
