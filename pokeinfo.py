import requests

poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'

def obtain_pokeinfo(url, depth=0):
    POKEAPI = requests.get(url).json()
    pokemon_data = {}  # Diccionario para almacenar la información
    
    for key, value in POKEAPI.items():
        if isinstance(value, list):
            # Si es una lista, iteramos sobre sus elementos
            pokemon_data[key] = []
            for item in value:
                if isinstance(item, dict):
                    # Si el elemento es un diccionario, llamamos recursivamente a la función
                    pokemon_data[key].append(obtain_pokeinfo(url, depth + 1))
                else:
                    pokemon_data[key].append(item)
        elif isinstance(value, dict):
            # Si es un diccionario, llamamos recursivamente a la función
            pokemon_data[key] = obtain_pokeinfo(url, depth + 1)
        else:
            pokemon_data[key] = value
    
    return pokemon_data

pokemon_info = obtain_pokeinfo(poke_point)

# Ahora tienes un diccionario 'pokemon_info' que contiene la información de Pokémon.

# Puedes utilizar esta información para generar HTML u otro tipo de visualización.
