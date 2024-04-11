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
# email = input("ingresa usuario: ")
# print(email[: email.find("@")] + "@ceu.es")

"""
Calcular masa corporal ingresando datos y operadores.
"""
print("Calcular peso y altura")
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
masa_corporal = peso / (altura * altura)
print("Tu índice de masa corporal es donde " + str(round(masa_corporal, 2)))

"""
frase ingresada y salida en sentido contrario.
"""
word = input("ingrese la para imprimir en reversa: ")


def phrase_reverse(word):
    result = word.split()  # eliminar elementos de string y convirtiéndolo en un lista.
    return result[::-1]  # devolver la lista en sentido contrario.


# aplicación de join para que imprima en forma de string y no de lista.
print(" ".join(phrase_reverse(word)))

"""
aplicando método reverse en función de frase.
"""


def phrase_reverse(word):
    result = word.split()  # eliminar elementos de string y convirtiéndolo en un lista.
    result.reverse()
    return " ".join(result)


print(phrase_reverse(word=input("ingrese una frase para imprimir: ")))


"""
verificación de email que tenga el carácter de @, no al inicio o al final.
"""
email = input("ingresa un email: ")

validar = email.find("@")
c = email.count("@")
v2 = email.rfind("@")
v3 = len(email)
print(c, validar, v2, v3)
print(type(v2))

if validar == 0 or c != 1 or v2 == (len(email) - 1):
    print("correo invalido")
else:
    print("correo valido")
