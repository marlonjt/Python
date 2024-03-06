"""
Utilizar funciones sobre variables string y calculando operaciones matemáticas.
"""

# imprimir el nombre por el numero ingresado
# nombre = input("ingrese su nombre: ")
# numero = int(input("ingrese el numero:"))
# print((nombre + "\n") * numero) #end python \n
# print(nombre.capitalize()) #primera letra en mayúsculas
# print(nombre.lower()) #todo minúsculas
# print(nombre.upper()) #todo mayúsculas
# print(nombre.upper(),"tiene", len(nombre),"letras")
# frase = input("ingrese frase: ")
# lista = frase.split()
# lista.reverse() #reverse método para revertir listas
# print(frase[::-1]) # ::-1 sirve para revertir una lista o tuple iterable[inicio:fin:paso]
# vocal = input("ingresa vocal: ")
# print(frase.replace(vocal, vocal.upper())) # replace método para remplazar palabras
email = input("ingresa usuario: ")
print(email[: email.find("@")] + "@ceu.es")

# Calcular masa corporal ingresando datos
print("Calcular peso y altura")
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
masa_corporal = peso / (altura * altura)
print("Tu índice de masa corporal es donde " + str(round(masa_corporal, 2)))

# frase ingresada e imprimido en sentido contrario
word = input("ingrese la para imprimir en reversa: ")


def phrase_reverse(word):
    result = word.split()  # eliminar elementos de string y convirtiéndolo en un array
    return result[::-1]


# aplicación de join para que imprima en forma de string y no de array
print(" ".join(phrase_reverse(word)))

# aplicando método reverse en función
word = input("ingrese la para imprimir en reversa: ")


def phrase_reverse(word):
    result = word.split()  # eliminar elementos de string y convirtiéndolo en un array
    result.reverse()
    return " ".join(result)


# aplicación de join para que imprima en forma de string y no de array
print(phrase_reverse(word))


# funciones con listas y iteraciones  con condicionales
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
