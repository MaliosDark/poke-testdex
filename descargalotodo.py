import os
import requests
import json
from tqdm import tqdm

# URL base de la API de PokeAPI
base_url = "https://pokeapi.co/api/v2/pokemon/"

# Número total de Pokémon conocidos (hasta el momento de mi conocimiento en enero de 2022)
total_pokemon = 898

# Directorio donde se guardarán los datos
directory = "datos_pokemon/"

# Crear el directorio si no existe
os.makedirs(directory, exist_ok=True)

# Crear un iterador tqdm para mostrar el progreso
with tqdm(total=total_pokemon) as pbar:
    # Recorre y descarga todos los Pokémon
    for i in range(1, total_pokemon + 1):
        response = requests.get(base_url + str(i))
        if response.status_code == 200:
            data = response.json()
            with open(directory + f"pokemon_{i}.json", "w") as file:
                json.dump(data, file)
        else:
            print(f"No se pudo descargar el Pokémon {i}")
        pbar.update(1)  # Incrementa el indicador de progreso

print("Descarga completa.")
