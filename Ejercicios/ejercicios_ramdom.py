"""
Generar un número flotante aleatorio
Escribe un programa que genere un número flotante aleatorio entre 0 y 1 y lo multiplique por 100.
Desafío adicional: Redondea el resultado a dos decimales.
"""

import random

number_float = random.random() * 100
print(f"{number_float:.2f}")  # :.2f redondea a dos decimales

"""
Simulación de un dado
Simula el lanzamiento de un dado de seis caras utilizando randint.
Desafío adicional: Simula el lanzamiento de dos dados y suma sus resultados.
"""

dado = random.randint(1, 6)
dado2 = random.randint(1, 6)
print(f"Sumatoria de los dos dados es: {dado+dado2}")

"""
Sorteo de nombres
Crea una lista con nombres y utiliza choice para elegir un ganador al azar.
Desafío adicional: Usa sample para seleccionar tres ganadores únicos.
"""
lista = ["maria", "alejo", "pol", "leo"]
print(f"El ganador es: {random.choice(lista)}")
print(f"Los ganadores son: {random.sample(lista, 3)}")

"""
Barajar cartas
Crea una lista con las cartas de una baraja (por ejemplo: ["A", "2", "3", ..., "K"]) y utiliza shuffle para mezclar.
Desafío adicional: Reparte 5 cartas al azar.
"""
naipe = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(naipe)
print(naipe[:5])
