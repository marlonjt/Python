def dir_reduce(arr):

    OPUESTOS = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }
    pila = []
    for camino in arr:
        if pila and pila[-1] == OPUESTOS[camino]:
            pila.pop()
        else:
            pila.append(camino)

    return pila


camino = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
print(dir_reduce(camino))
