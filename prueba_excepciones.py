def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):

    try:
        return num1 / num2
    except ZeroDivisionError:
        return "No se puede dividir para 0"


while True:
    try:
        op1 = int(input("Introduce el primer número: "))

        op2 = int(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("INGRESA UN NUMERO VALIDO")

resultado = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")


if resultado.lower() == "suma":
    print(suma(op1, op2))

elif resultado.lower() == "resta":
    print(resta(op1, op2))

elif resultado.lower() == "multiplica":
    print(multiplica(op1, op2))

elif resultado.lower() == "divide":
    print(divide(op1, op2))

else:
    print("operación no contemplada")

print("operación ejecutada. Continua de ejecución del programa ")