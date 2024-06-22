from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Datos en memoria para almacenar las cuentas
accounts = {
    "account1": {"balance": 1000},
    "account2": {"balance": 1000}
}

# Ruta para servir la página HTML
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Obtener el balance de una cuenta
@app.route('/balance/<account_id>', methods=['GET'])
def get_balance(account_id):
    if account_id in accounts:
        return jsonify({"account": account_id, "balance": accounts[account_id]["balance"]}), 200
    return jsonify({"status": "error", "message": "Account not found"}), 404

# Transferir dinero entre cuentas
@app.route('/transfer', methods=['POST'])
def transfer():
    source_account = request.json.get('source')
    destination_account = request.json.get('destination')
    amount = request.json.get('amount')

    if not source_account or not destination_account or amount is None:
        return jsonify({"status": "error", "message": "Invalid request"}), 400

    if source_account not in accounts or destination_account not in accounts:
        return jsonify({"status": "error", "message": "Account not found"}), 404

    if accounts[source_account]["balance"] < amount:
        return jsonify({"status": "error", "message": "Insufficient funds"}), 400

    # Iniciar transacción
    try:
        # Restar el monto de la cuenta origen
        accounts[source_account]["balance"] -= amount
        # Añadir el monto a la cuenta destino
        accounts[destination_account]["balance"] += amount
        return jsonify({"status": "success", "source": source_account, "destination": destination_account, "amount": amount}), 200
    except Exception as e:
        # Si ocurre un error, revertir la transacción
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
