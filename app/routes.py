from flask import jsonify, request
from app import app
from app.models import Task
from flask_jwt_extended import jwt_required

# Endpoint para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()  # Supondo que você tenha um ORM configurado
    return jsonify([task.to_dict() for task in tasks]), 200

# Endpoint para adicionar uma nova tarefa
@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], status="pending")
    new_task.save()  # Método para salvar no banco de dados
    return jsonify(new_task.to_dict()), 201

# Endpoint para atualizar o status de uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.status = data.get('status', task.status)
    task.save()
    return jsonify(task.to_dict()), 200

# Endpoint para deletar uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    task.delete()  # Método para remover do banco de dados
    return jsonify({"message": "Task deleted"}), 200
