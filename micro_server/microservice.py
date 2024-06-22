from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Datos en memoria para almacenar las tareas
tasks = []

# Ruta para servir la página HTML
@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

# Obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append(task)
        return jsonify({"status": "success", "task": task}), 201
    return jsonify({"status": "error", "message": "No task provided"}), 400

# Eliminar una tarea
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        return jsonify({"status": "success", "task": task}), 200
    return jsonify({"status": "error", "message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
