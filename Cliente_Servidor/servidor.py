from flask import Flask, request, jsonify

app = Flask(__name__)

# Lógica de Negocio
data = {"items": []}

def add_item(item):
    data["items"].append(item)

def get_items():
    return data["items"]

@app.route('/add', methods=['POST'])
def add():
    item = request.json.get('item')
    add_item(item)
    return jsonify({"status": "success"}), 200

@app.route('/items', methods=['GET'])
def items():
    return jsonify({"items": get_items()}), 200

if __name__ == '__main__':
    app.run(debug=True)
