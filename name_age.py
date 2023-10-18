import datetime
name=input("ingrese su nombre: ")
age=int(input("ingrese su edad: "))
now = datetime.datetime.now().year
print(now)
x = (100 - age) + now
print(x)
print("su nombre es " + str(name) + " su edad es " + str(age) + " cumplirá cien años en " + str(x))