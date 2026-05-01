try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(f"Contenido: {contenido}")
        archivo.close()

except FileNotFoundError:
    print("Error: No se encontró el archivo.")

# exercise  second

with open("datos.txt", "w") as archivo:
    texto = "Primer registro de datos.\n"
    archivo.seek(0)
    archivo.write(texto)
    archivo.close()

with open("datos.txt", "a") as archivo:
    texto2 = "Segundo registro agregado."
    archivo.seek(0)
    archivo.write(texto2)
    archivo.close()

# exercise third

with open("usuarios.txt", "r") as usuarios:
    nombre_limpios = []
    for name in usuarios:
        nombre_limpios.append(name.strip())
    print(nombre_limpios)
    usuarios.close()
