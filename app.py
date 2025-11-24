from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial default item inventory
DEFAULT_ITEMS = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop for programming",
        "price": 1299.99,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with USB receiver",
        "price": 29.99,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Desk Chair",
        "description": "Comfortable office chair with lumbar support",
        "price": 249.99,
        "category": "Furniture"
    },
    {
        "id": 4,
        "name": "Coffee Mug",
        "description": "Ceramic mug with 'World's Best Developer' text",
        "price": 12.99,
        "category": "Kitchen"
    },
    {
        "id": 5,
        "name": "Notebook",
        "description": "100-page ruled notebook for notes and sketches",
        "price": 5.99,
        "category": "Stationery"
    }
]

# Sample data
items = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop for programming",
        "price": 1299.99,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with USB receiver",
        "price": 29.99,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Desk Chair",
        "description": "Comfortable office chair with lumbar support",
        "price": 249.99,
        "category": "Furniture"
    },
    {
        "id": 4,
        "name": "Coffee Mug",
        "description": "Ceramic mug with 'World's Best Developer' text",
        "price": 12.99,
        "category": "Kitchen"
    },
    {
        "id": 5,
        "name": "Notebook",
        "description": "100-page ruled notebook for notes and sketches",
        "price": 5.99,
        "category": "Stationery"
    }
]

@app.route('/')
def home():
    return jsonify({
        "message": "Simple Flask Application",
        "endpoints": {
            "GET /": "Get API information",
            "HEAD /": "Get headers for home endpoint",
            "OPTIONS /": "Get allowed methods for home endpoint",
            "GET /items": "Retrieve all items",
            "HEAD /items": "Get headers for all items",
            "OPTIONS /items": "Get allowed methods for items collection",
            "POST /items": "Create a new item",
            "GET /items/<id>": "Retrieve a specific item",
            "HEAD /items/<id>": "Get headers for a specific item",
            "OPTIONS /items/<id>": "Get allowed methods for a specific item",
            "PUT /items/<id>": "Update an item",
            "PATCH /items/<id>": "Partially update an item",
            "DELETE /items/<id>": "Delete an item",
            "POST /reset": "Reset Inventory"
        }
    })

# HEAD - Get headers for home endpoint
@app.route('/', methods=['HEAD'])
def head_home():
    response = jsonify({
        "message": "Simple Flask Application",
        "endpoints": {
            "GET /": "Get API information",
            "HEAD /": "Get headers for home endpoint",
            "OPTIONS /": "Get allowed methods for home endpoint",
            "GET /items": "Retrieve all items",
            "HEAD /items": "Get headers for all items",
            "OPTIONS /items": "Get allowed methods for items collection",
            "POST /items": "Create a new item",
            "GET /items/<id>": "Retrieve a specific item",
            "HEAD /items/<id>": "Get headers for a specific item",
            "OPTIONS /items/<id>": "Get allowed methods for a specific item",
            "PUT /items/<id>": "Update an item",
            "PATCH /items/<id>": "Partially update an item",
            "DELETE /items/<id>": "Delete an item",
            "POST /reset": "Reset Inventory"
        }
    })
    return response

# OPTIONS - Get allowed methods for home endpoint
@app.route('/', methods=['OPTIONS'])
def options_home():
    response = jsonify({
        "allowed_methods": ["GET", "HEAD", "OPTIONS"],
        "description": "Home endpoint - provides API information"
    })
    response.headers['Allow'] = 'GET, HEAD, OPTIONS'
    return response

# GET - Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# HEAD - Get headers for all items
@app.route('/items', methods=['HEAD'])
def head_items():
    response = jsonify(items)
    return response

# OPTIONS - Get allowed methods for items collection
@app.route('/items', methods=['OPTIONS'])
def options_items():
    response = jsonify({
        "allowed_methods": ["GET", "HEAD", "POST", "OPTIONS"]
    })
    response.headers['Allow'] = 'GET, HEAD, POST, OPTIONS'
    return response

# GET - Retrieve single item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# HEAD - Get headers for specific item
@app.route('/items/<int:item_id>', methods=['HEAD'])
def head_item(item_id):
    for item in items:
        if item["id"] == item_id:
            response = jsonify(item)
            return response
    return jsonify({"error": "Item not found"}), 404

# OPTIONS - Get allowed methods for specific item
@app.route('/items/<int:item_id>', methods=['OPTIONS'])
def options_item(item_id):
    response = jsonify({
        "allowed_methods": ["GET", "HEAD", "PUT", "PATCH", "DELETE", "OPTIONS"]
    })
    response.headers['Allow'] = 'GET, HEAD, PUT, PATCH, DELETE, OPTIONS'
    return response

# POST - Create new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    # Auto-generate ID based on the last item's ID
    new_id = items[-1]["id"] + 1 if items else 1
    data["id"] = new_id
    items.append(data)
    return jsonify({"message": "Item created", "item": data}), 201

# PUT - Update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    for item in items:
        if item["id"] == item_id:
            item.update(data)
            return jsonify({"message": "Item updated", "item": item})
    
    return jsonify({"error": "Item not found"}), 404

# PATCH - Partially update item
@app.route('/items/<int:item_id>', methods=['PATCH'])
def patch_item(item_id):
    data = request.get_json()
    
    for item in items:
        if item["id"] == item_id:
            item.update(data)
            return jsonify({"message": "Item partially updated", "item": item})
    
    return jsonify({"error": "Item not found"}), 404

# DELETE - Delete item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({"message": "Item deleted", "item": item})
    
    return jsonify({"error": "Item not found"}), 404

# POST - Reset items to default state
@app.route('/reset', methods=['POST'])
def reset_items():
    global items
    items = [item.copy() for item in DEFAULT_ITEMS]
    return jsonify({"message": "Items reset to default state", "items": items})

if __name__ == '__main__':
    app.run(debug=True)