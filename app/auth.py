from flask import jsonify, request
from flask_jwt_extended import create_access_token
from app import app

# Endpoint para login (autenticação)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Aqui você deve validar o usuário e senha (exemplo simples)
    if username == 'admin' and password == 'password':  # Substitua por verificação real
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
