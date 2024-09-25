# Pokémon Flask API

Esta es una API basada en Flask que utiliza autenticación JWT para proteger endpoints que interactúan con la [PokéAPI](https://pokeapi.co/). La API permite obtener tipos de un Pokémon, un Pokémon aleatorio según su tipo y el nombre más largo de un Pokémon por tipo.

## Requisitos

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-Bcrypt
- Requests

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/sarae0626/pokemon_data.git
   cd pokemon_data/
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv poke_env
   ```

3. Activa el entorno virtual:
   - En macOS/Linux:
     ```bash
     source poke_env/bin/activate
     ```
   - En Windows:
     ```bash
     poke_env/Scripts/activate
     ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```


## Uso

1. Ejecuta la aplicación:
   ```bash
   python pokemon_app.py
   ```

2. La aplicación estará corriendo en `http://127.0.0.1:5000/`.

## Endpoints

### Autenticación

#### Registro
- **POST** `/auth/register`
  - Registra un nuevo usuario.
  - **Request Body**:
    ```json
    {
      "username": "user123",
      "password": "mypassword"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "Usuario user123 registrado correctamente"
    }
    ```

#### Inicio de sesión
- **POST** `/auth/login`
  - Inicia sesión y obtiene un token de acceso JWT.
  - **Request Body**:
    ```json
    {
      "username": "user123",
      "password": "mypassword"
    }
    ```
  - **Response**:
    ```json
    {
      "access_token": "<jwt_token>"
    }
    ```

### Funcionalidades Pokémon

#### Obtener tipos de un Pokémon
- **POST** `/pokemon_types`
  - Devuelve los tipos del Pokémon ingresado.
  - **Request Headers**:
    - `Authorization: Bearer <jwt_token>`
  - **Request Body**:
    ```json
    {
      "pokemon_name": "pikachu"
    }
    ```
  - **Response**:
    ```json
    {
      "El pokemon pikachu es de tipo": ["electric"]
    }
    ```

#### Obtener un Pokémon aleatorio por tipo
- **POST** `/random_pokemon`
  - Devuelve un nombre de Pokémon aleatorio de un tipo específico.
  - **Request Headers**:
    - `Authorization: Bearer <jwt_token>`
  - **Request Body**:
    ```json
    {
      "pokemon_type": "fire"
    }
    ```
  - **Response**:
    ```json
    {
      "Un pokemon aleatorio de tipo fire es": "charmander"
    }
    ```

#### Obtener el nombre más largo de un Pokémon por tipo
- **POST** `/pokemon_max_name`
  - Devuelve el nombre más largo de un Pokémon por tipo.
  - **Request Headers**:
    - `Authorization: Bearer <jwt_token>`
  - **Request Body**:
    ```json
    {
      "pokemon_type": "grass"
    }
    ```
  - **Response**:
    ```json
    {
      "El pokemon con el nombre más largo de tipo grass es": "venusaur"
    }
    ```

## Seguridad

- Todos los endpoints que interactúan con la PokéAPI están protegidos con autenticación JWT. Es necesario obtener un token de acceso mediante el endpoint `/auth/login` y proporcionarlo en los encabezados de la solicitud como `Authorization: Bearer <token>`.

## Dependencias

- Flask: Framework web utilizado para construir la API.
- Flask-JWT-Extended: Proporciona la autenticación mediante JSON Web Tokens (JWT).
- Flask-Bcrypt: Para encriptar contraseñas de usuarios.
- Requests: Para interactuar con la PokéAPI.
