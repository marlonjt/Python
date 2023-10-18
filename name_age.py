import datetime

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
