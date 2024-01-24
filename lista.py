# import random

# a = random.sample(range(1, 30), 12)
# b = random.sample(range(1, 30), 16)
# result = [i for i in set(a) if i in b]

# print(result)

import random

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

lista = ["x", "y", "z"]
print(random.sample(lista, 2))
