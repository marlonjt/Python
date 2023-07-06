year = int(input("ingresa el año para comprobar si es bisiesto: "))
# cuatro = year % 4
# cien = year % 100
# cuatrocientos = year % 400 
# print('resultado entre 4: ', cuatro)
# print('resultado entre 100: ', cien)
# print('resultado entre 400: ', cuatrocientos)

if year % 4 != 0: #no divisible entre 4
	print("No es bisiesto por que no es divisible para 4")
elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y es diferente entre 100
    print("Es bisiesto residuo de 4 es 0 y 100 es diferente de 0")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 100 y no entre 400
    print("No es bisiesto por que el residuo de 4 es 0, 100 es 0 y 400 es diferente de 0 ")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
    print("Es bisiesto por que residuo de 4 es 0, 100 es 0 y 400 es 0")