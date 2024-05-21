"""
Introducción a ficheros 
"""

import os

# file_txt = "practica.txt"

# name = "Marlon Joel"
# with open(file_txt, "w") as file:
#     file.write(name)

# with open(file_txt, "r") as file:
#     print(file.read())

# os.remove(file_txt)

"""
Ejercicio de ficheros 
"""

shop_txt = "shop.txt"

open(shop_txt, "a")

while True:
    print("1. Añadir producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("escoja entre las opciones 1 al 6: ")
    match option:
        case "1":
            name = input("Ingresa el producto: ")
            quantity = input("Ingresa la cantidad: ")
            price = input("Ingresa el precio: ")
            with open(shop_txt, "a") as file:
                file.write(f"{name},{quantity},{price}\n")
        case "2":
            name = input("Ingresa el nombre del producto: ")
            with open(shop_txt, "r") as file:
                for line in file.readlines():
                    if line.split(",")[0] == name:
                        print(f"Si hay el:{line}")
                    else:
                        print("No hay el producto")
        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(shop_txt, "r") as file:
                lines = file.readlines()
            with open(shop_txt, "w") as file:
                for line in lines:
                    if line.split(",")[0] == name:
                        file.write(f"{name},{quantity},{price}\n")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre: ")
            with open(shop_txt, "r") as file:
                lines = file.readlines()
            with open(shop_txt, "w") as file:
                for line in lines:
                    if line.split(",")[0] != name:
                        file.write(line)
        case "5":
            with open(shop_txt, "r") as file:
                print(file.read())
        case "6":
            total = 0
            with open(shop_txt, "r") as file:
                for line in file.readlines():
                    components = line.split(",")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(total)
        case "7":
            name = input("Nombre: ")
            total = 0
            with open(shop_txt, "r") as file:
                for line in file.readlines():
                    components = line.split(",")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(total)
        case "8":
            print("Saliendo del programa")
            os.remove(shop_txt)
            break
        case _:
            print("Elige una opción que se muestra")
