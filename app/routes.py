from flask import jsonify, request, render_template
from app.models import Task
from flask_jwt_extended import create_access_token, jwt_required  # Importar jwt_required
from flask import current_app as app
import os

# Endpoint para a página inicial
@app.route('/')
def index():
    # Adiciona o caminho real da pasta templates para depuração
    print("Templates folder:", os.path.abspath("templates"))

    return render_template('index.html')

# Usuários fictícios apenas para exemplo
users = {
    "admin": "admin",
    "user": "user"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Verificando se o usuário e a senha são válidos
    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad username or password"}), 401

    # Criando um token JWT
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Endpoint para listar todas as tarefas (requer autenticação)
@app.route('/tasks', methods=['GET'])
@jwt_required()  # Requer um token JWT
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Endpoint para adicionar uma nova tarefa (requer autenticação)
@app.route('/tasks', methods=['POST'])
@jwt_required()  # Requer um token JWT
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], status="pending")
    new_task.save()
    return jsonify(new_task.to_dict()), 201

# Endpoint para atualizar o status de uma tarefa (requer autenticação)
@app.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()  # Requer um token JWT
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.status = data.get('status', task.status)
    task.save()
    return jsonify(task.to_dict()), 200

# Endpoint para deletar uma tarefa (requer autenticação)
@app.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()  # Requer um token JWT
def delete_task(id):
    task = Task.query.get_or_404(id)
    task.delete()
    return jsonify({"message": "Task deleted"}), 200
