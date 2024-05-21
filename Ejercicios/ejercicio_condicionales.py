"""
Ejercicios de condicionales y aplicación de teoría como funciones
"""

print("Calificación de examen")

alumno = input("ingresa la nota: ")


def prueba(nota):
    valor = "aprobado"
    calificación = nota * 0.1
    print(calificación)
    if calificación < 5:
        valor = "reprobado"
    return valor


print(prueba(int(alumno)))

"""
Calcular año bisiesto aplicando condicionales y operadores.
"""

year = int(input("ingresa el año para comprobar si es bisiesto: "))
# cuatro = year % 4
# cien = year % 100
# cuatrocientos = year % 400
# print('resultado entre 4: ', cuatro)
# print('resultado entre 100: ', cien)
# print('resultado entre 400: ', cuatrocientos)

if year % 4 != 0:  # no divisible entre 4
    print("No es bisiesto por que no es divisible para 4")
elif year % 4 == 0 and year % 100 != 0:  # divisible entre 4 y es diferente entre 100
    print("Es bisiesto residuo de 4 es 0 y 100 es diferente de 0")
elif (
    year % 4 == 0 and year % 100 == 0 and year % 400 != 0
):  # divisible entre 4 y 100 y no entre 400
    print(
        "No es bisiesto por que el residuo de 4 es 0, 100 es 0 y 400 es diferente de 0 "
    )
elif (
    year % 4 == 0 and year % 100 == 0 and year % 400 == 0
):  # divisible entre 4, 100 y 400
    print("Es bisiesto por que residuo de 4 es 0, 100 es 0 y 400 es 0")

"""
Números primos dentro de la función y aplicando condicionales.
"""

num = int(input("ingrese el numero: "))


def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True


print(es_primo(num))

"""
Serie de Fibonacci con función y condicional while
"""


n = int(input("ingrese un numero para imprimir la serie"))


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=",")
        a, b = b, a + b


fibonacci(n)
