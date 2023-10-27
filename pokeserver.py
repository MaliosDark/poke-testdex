from flask import Flask, render_template
import os
import json
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/pokemon/<int:pokemon_id>')
def pokemon_detail(pokemon_id):
    data_dir = 'datos_pokemon'
    filename = os.path.join(data_dir, f'pokemon_{pokemon_id}.json')

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            pokemon_data = json.load(file)
        return render_template('pokemon_detail.html', pokemon=pokemon_data)
    else:
        return "Pokémon no encontrado"

@app.route('/')
def index():
    data = []
    # Lee los archivos JSON en datos_pokemon y los agrega a la lista data
    for filename in os.listdir('datos_pokemon'):
        if filename.endswith('.json'):
            with open(os.path.join('datos_pokemon', filename), 'r') as file:
                pokemon_data = json.load(file)
                # Agrega la URL de la imagen a los datos del Pokémon
                pokemon_data['image_url'] = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_data['id']}.png"
                data.append(pokemon_data)

    # Ordena la lista de Pokémon por su número de Pokédex
    data.sort(key=lambda pokemon: pokemon['id'])

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
#############################