from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Capa de Datos
data = {"items": []}

# Capa de Negocio
def add_item(item):
    data["items"].append(item)

def get_items():
    return data["items"]

# Capa de Presentación: Servir la página HTML
@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

# Endpoint para agregar un ítem
@app.route('/add', methods=['POST'])
def add():
    item = request.json.get('item')
    add_item(item)
    return jsonify({"status": "success"}), 200

# Endpoint para obtener todos los ítems
@app.route('/items', methods=['GET'])
def items():
    return jsonify({"items": get_items()}), 200

if __name__ == '__main__':
    app.run(debug=True)
