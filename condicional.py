print("Test If")

alumno = input("ingresa la nota: ")

def prueba(nota):
    valor = "aprobado"
    calificación = nota * 0.1
    print(calificación)
    if calificación < 5:
        valor = "reprobado"
    return valor


print(prueba(int(alumno)))
