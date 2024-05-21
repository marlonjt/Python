jugador = input("escoja: 1.piedra, 2.papel o 3.tijeras ")
jugador2 = input("escoja: 1.piedra, 2.papel o 3.tijeras ")

while True:
    if jugador == "piedra" and jugador2 == "piedra":
        print("empate")
    elif jugador == "piedra" and jugador2 == "tijeras":
        print("ganador jugador uno")
    elif jugador == "piedra" and jugador2 == "papel":
        print("ganador jugador dos")
    elif jugador == "papel" and jugador2 == "piedra":
        print("ganador jugador uno")
    elif jugador == "papel" and jugador2 == "tijeras":
        print("ganador jugador dos")
    elif jugador == "papel" and jugador2 == "papel":
        print("empate")
    elif jugador == "tijeras" and jugador2 == "piedra":
        print("ganador jugador dos")
    elif jugador == "tijeras" and jugador2 == "papel":
        print("ganador jugador uno")
    elif jugador == "tijeras" and jugador2 == "tijeras":
        print("empate")
    break
