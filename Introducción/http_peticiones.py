import requests

pokemon = input("Ingresa el nombre pokemon o el número: ").lower()
# URL de la PokeAPI para obtener información sobre
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

# Hacer una solicitud GET a la API
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()

    # Imprimir información relevante
    print(f"Name: {data['name']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print("Abilities:")
    for ability in data["abilities"]:
        print(f"  - {ability['ability']['name']}")
    print("Juegos:")
    for game in data["game_indices"]:
        print(f" - {game['version']['name']}")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Cadena de evolución:")

            def get_evolves(data):
                print(f" - {data['species']['name']}")
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print(f"Error {response.status_code} obteniendo las evoluciones.")
    else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
    print(f"Error: {response.status_code}")
