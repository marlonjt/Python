# imprimir el nombre por el numero ingresado
#nombre = input("ingrese su nombre: ")
#numero = int(input("ingrese el numero:"))
#print((nombre + "\n") * numero) #end python \n
#print(nombre.capitalize()) #primera letra en mayúsculas
#print(nombre.lower()) #todo minúsculas 
#print(nombre.upper()) #todo mayúsculas
#print(nombre.upper(),"tiene", len(nombre),"letras")
#frase = input("ingrese frase: ")
#lista = frase.split()
#lista.reverse() #reverse método para revertir listas
#print(frase[::-1]) # ::-1 sirve para revertir una lista o tuple iterable[inicio:fin:paso]
#vocal = input("ingresa vocal: ")
#print(frase.replace(vocal, vocal.upper())) # replace método para remplazar palabras
email = input("ingresa usuario: ")
print(email[:email.find('@')] + '@ceu.es')