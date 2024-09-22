from flask import Flask, request, jsonify
import requests
import random

POKE_API_URL = "https://pokeapi.co/api/v2/"

app = Flask(__name__)

# Endpoint 1: Get pokemon type
@app.route('/pokemon_types', methods=['POST'])

def get_pokemon_types():
    data_pokemon_name = request.get_json()
    pokemon_name = data_pokemon_name.get("pokemon_name", "null")
    if pokemon_name == "null":
        message = "Por favor ingrese el Value de la Key 'pokemon_name'"
        return jsonify({'message': message})
    else:
        response = requests.get(POKE_API_URL+"pokemon/"+pokemon_name)
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON (si la API devuelve JSON)
            data = response.json()
            list_pokemon_types = []

            for type_by_pokemon in data["types"]:
                list_pokemon_types.append(type_by_pokemon["type"]["name"])
            return jsonify({f'El pokemon {pokemon_name} es de tipo': list_pokemon_types})
        else:
            message = f"Error {response.status_code} - Pokemon {response.text}"
            return jsonify({'message': message})

# Endpoint 2: Get random pokemon
@app.route('/random_pokemon', methods=['POST'])
def get_pokemon_name():
    data_pokemon_type = request.get_json()
    pokemon_type = data_pokemon_type.get("pokemon_type", "null")
    if pokemon_type == "null":
        message = "Por favor ingrese el Value de la Key 'pokemon_type'"
        return jsonify({'message': message})
    else:
        response = requests.get(POKE_API_URL+"type/"+pokemon_type)
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON (si la API devuelve JSON)
            data = response.json()
            list_pokemon_name = []

            for pokemon_by_type in data["pokemon"]:
                list_pokemon_name.append(pokemon_by_type["pokemon"]["name"])
            pokemon_random = random.choice(list_pokemon_name)
            return jsonify({f'Un pokemon aleatorio de tipo {pokemon_type} es': pokemon_random})
        else:
            message = f"Error {response.status_code} - Type {response.text}"
            return jsonify({'message': message})

# Endpoint 3: Get longest pokemon name
@app.route('/pokemon_max_name', methods=['POST'])

def get_pokemon_max_name():
    data_pokemon_type = request.get_json()
    pokemon_type = data_pokemon_type.get("pokemon_type", "null")
    if pokemon_type == "null":
        message = "Por favor ingrese el Value de la Key 'pokemon_type'"
        return jsonify({'message': message})
    else:
        response = requests.get(POKE_API_URL+"type/"+pokemon_type)
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON (si la API devuelve JSON)
            data = response.json()
            list_pokemon_name = []

            for pokemon_by_type in data["pokemon"]:
                list_pokemon_name.append(pokemon_by_type["pokemon"]["name"])
            pokemon_max_name = max (list_pokemon_name, key=len)
            return jsonify({f'El pokemon con el nombre más largo de tipo {pokemon_type} es': pokemon_max_name})
        else:
            message = f"Error {response.status_code} - Type {response.text}"
            return jsonify({'message': message})
        
if __name__ == '__main__':
    app.run(debug=True)
