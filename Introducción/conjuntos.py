conjunto = [1, 2, 3, 4, 5]

print(f"lista inicial: {conjunto}")
conjunto.append(6)
print(f"Nuevo valor: {conjunto}")
conjunto.insert(0, 0)
print(f"Insertando valor en la posición 0: {conjunto}")
conjunto.extend([7, 8])
print(f"Agregando valores al final: {conjunto}")
conjunto[2:3] = [12, 13]
print(f"Agregando valores en la posición [2:3]: {conjunto}")
conjunto.remove(0)
print(f"Eliminando un valor en especifico: {conjunto}")
conjunto.pop(2)
print(f"Eliminando con método pop: {conjunto}")
conjunto.pop()
print(f"Eliminando el último valor: {conjunto}")
conjunto[1] = 2
print(f"Remplazando un valor de la lista: {conjunto}")
print(f"Valor encontrado:{4 in conjunto}")
del conjunto[6]
print(f"Eliminando el último valor en especifico: {conjunto}")
conjunto.clear()
print(f"Eliminando todos los elementos: {conjunto}")
try:
    del conjunto
    print(conjunto)
except Exception as e:
    print("Lista eliminada", type(e))


"""
Extra utilizando sets
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {set_1.union(set_2)}")

print(f"Intersección: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")
