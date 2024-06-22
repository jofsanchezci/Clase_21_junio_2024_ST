from flask import Flask, request, jsonify
from business import BusinessLogic

app = Flask(__name__)
business_logic = BusinessLogic()

@app.route('/add', methods=['POST'])
def add():
    item = request.json.get('item')
    business_logic.add_item(item)
    return jsonify({"status": "success"}), 200

@app.route('/items', methods=['GET'])
def items():
    return jsonify({"items": business_logic.get_items()}), 200

if __name__ == '__main__':
    app.run(debug=True)
