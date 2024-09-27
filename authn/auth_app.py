from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt

# Crear un Blueprint de Flask para auth
auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# Base de datos simple en memoria para los usuarios y contraseñas
users = {}

@auth_bp.route('/register', methods=['POST'])
def register():
    """Endpoint para registrar un usuario en la app"""
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({'message': 'Falta el nombre de usuario o la contraseña'}), 400

    if username in users:
        return jsonify({'message': 'El usuario ya existe'}), 400

    # Encriptar la contraseña
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users[username] = hashed_password

    return jsonify({'message': f'Usuario {username} registrado correctamente'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Endpoint para el login y la generación de token de autenticación"""
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({'message': 'Falta el nombre de usuario o la contraseña'}), 400

    user_password = users.get(username, None)
    if not user_password or not bcrypt.check_password_hash(user_password, password):
        return jsonify({'message': 'Credenciales inválidas'}), 401

    # Crear token de acceso
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
 