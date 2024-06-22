import requests

def add_item(item):
    response = requests.post('http://127.0.0.1:5000/add', json={"item": item})
    return response.json()

def get_items():
    response = requests.get('http://127.0.0.1:5000/items')
    return response.json()

# Ejemplo de uso del cliente
add_item("Item 1")
add_item("Item 2")
print(get_items())
