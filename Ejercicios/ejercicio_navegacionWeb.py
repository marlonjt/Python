"""
crear una web de navegación de urls 
"""


def navigation_web():

    stack = []
    while True:
        action = input(
            "ingrese una  url o interactúa con las acciones adelante/atrás/ salir. "
        ).lower()

        if action == "salir":
            print("Saliendo del Programa")
            break
        elif action == "adelante":
            action = input("ingresa nuevamente la url: ")
            stack.append(action)
            print(f"usted se encuentra {stack[-1]}")
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
            else:
                print("No hay paginas web ingresa una")
        else:
            stack.append(action)
            print(f"usted se encuentra {stack[-1]}")
        if len(stack) == 0:
            print("Usted esta en la pagina de inicio")
        else:
            print(f"Usted esta : {stack[len(stack) - 1]}.")


# navigation_web()


def printer():

    queue = []

    while True:
        printer_file = input("ingresa el archivo o imprimir/salir. ")

        if printer_file == "salir":
            print("saliendo de impresión")
            break
        elif printer_file == "imprimir":
            if len(queue) == 0:
                print("No hay nada en cola")
            else:
                print(f"imprimiendo {queue[0]}")
                queue.pop(0)
        else:
            queue.append(printer_file)

        print(f"Cola de impresión: {queue}")


printer()
