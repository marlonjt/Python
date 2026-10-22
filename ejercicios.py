def remove_every_other(my_list):
    return [pares for indice, pares in enumerate(my_list) if indice % 2 == 0]


print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]))
