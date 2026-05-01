triple = lambda number: number * 3
print(triple(7))

es_positivo = lambda number: number > 0
print(es_positivo(7))
print(es_positivo(-10))

numbers = [3, 15, 7, 22, 10, 18, 4, 11]
numbers_mayores = list(filter(lambda x: x > 10, numbers))
print(numbers_mayores)

frutas = ["uva", "mango", "naranja", "kiwi", "maracuyá", "pera"]
longitud = list(filter(lambda char: len(char) > 5, frutas))
print(longitud)

numbers = [1, 2, 3, 4, 5]
cuadrado = list(map(lambda number: number**2, numbers))
print(cuadrado)

nombres = [" ana", "luis ", " carlos ", " eva"]
capitalize_names = list(map(lambda letter: letter.strip().capitalize(), nombres))
print(capitalize_names)

precios = [30, 80, 120, 45, 95, 15, 200]
mayores = list(filter(lambda p: p > 50, precios))
print(mayores)
descuento = list(map(lambda d: round(d * 0.9, 2), mayores))
print(descuento)

usuarios = [
    {"nombre": "ana", "activo": True},
    {"nombre": "luis", "activo": False},
    {"nombre": "eva", "activo": True},
    {"nombre": "carlos", "activo": False},
    {"nombre": "marta", "activo": True},
]

is_active = list(filter(lambda a: a["activo"], usuarios))
print(is_active)
names_upper = list(map(lambda name: name["nombre"].upper(), is_active))
print(names_upper)