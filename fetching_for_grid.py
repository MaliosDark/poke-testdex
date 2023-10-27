from timer import speed_deco
import requests
from flask import render_template


@speed_deco
def fetch_pokemons(index):
    POKEAPI = requests.get(index).json()

    pokelista = []
    list_nav = []

    for item in POKEAPI['results']:
        pokemon = requests.get(item['url']).json()
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]

        # Obtener el ID del Pokémon desde la URL
        pokemon_id = item['url'].split("/")[-2]

        # Añade el ID y la información detallada de cada Pokémon
        pokelista.append(
            {
                'nombre': item['name'],
                'id': pokemon_id,  # Agregar el ID
                'foto': f"https://pokeapi.co/media/sprites/pokemon/{pokemon_id}.png",  # URL de la imagen
                'altura': pokemon['height'],
                'peso': pokemon['weight'],
                'abilities': abilities
            }
        )
    
    list_nav.append(
        {
            'previous': POKEAPI['previous'],
            'next': POKEAPI['next']
        }
    )

    return pokelista, list_nav



