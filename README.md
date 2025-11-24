# Simple Flask REST API App

A simple REST API built with Flask for managing items with full CRUD operations. This application demonstrates RESTful principles and supports multiple HTTP methods including GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS.

## Features

- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ RESTful API design
- ✅ Support for HEAD and OPTIONS methods
- ✅ Auto-incrementing item IDs
- ✅ Pre-populated default inventory
- ✅ Reset functionality to restore default state
- ✅ OpenAPI/Swagger documentation
- ✅ JSON request/response format

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AayushRajthala99/simple-flask-restapi-app.git
cd simple-flask-restapi-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Home
- `GET /` - Get API information and available endpoints
- `HEAD /` - Get headers for home endpoint
- `OPTIONS /` - Get allowed methods for home endpoint

### Items Collection
- `GET /items` - Retrieve all items
- `POST /items` - Create a new item
- `HEAD /items` - Get headers for items collection
- `OPTIONS /items` - Get allowed methods for items collection

### Single Item
- `GET /items/<id>` - Retrieve a specific item by ID
- `PUT /items/<id>` - Update an entire item
- `PATCH /items/<id>` - Partially update an item
- `DELETE /items/<id>` - Delete an item
- `HEAD /items/<id>` - Get headers for a specific item
- `OPTIONS /items/<id>` - Get allowed methods for a specific item

### Utility
- `POST /reset` - Reset inventory to default state

## Usage Examples

### Get all items
```bash
curl http://localhost:5000/items
```

### Get a specific item
```bash
curl http://localhost:5000/items/1
```

### Create a new item
```bash
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Keyboard",
    "description": "Mechanical keyboard with RGB lighting",
    "price": 89.99,
    "category": "Electronics"
  }'
```

### Update an entire item
```bash
curl -X PUT http://localhost:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Laptop",
    "description": "Updated description",
    "price": 1499.99,
    "category": "Electronics"
  }'
```

### Partially update an item
```bash
curl -X PATCH http://localhost:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1399.99
  }'
```

### Delete an item
```bash
curl -X DELETE http://localhost:5000/items/1
```

### Reset inventory to default
```bash
curl -X POST http://localhost:5000/reset
```

### Check allowed methods
```bash
curl -X OPTIONS http://localhost:5000/items
```

## Default Items

The application comes pre-loaded with 5 default items:

1. **Laptop** - High-performance laptop for programming ($1299.99)
2. **Wireless Mouse** - Ergonomic wireless mouse with USB receiver ($29.99)
3. **Desk Chair** - Comfortable office chair with lumbar support ($249.99)
4. **Coffee Mug** - Ceramic mug with 'World's Best Developer' text ($12.99)
5. **Notebook** - 100-page ruled notebook for notes and sketches ($5.99)

## Data Structure

Each item has the following structure:
```json
{
  "id": 1,
  "name": "Item Name",
  "description": "Item description",
  "price": 99.99,
  "category": "Category Name"
}
```

## API Documentation

The API is fully documented using OpenAPI 3.0 specification. See `swagger.yaml` for complete API documentation.

## Dependencies

- Flask 3.1.2 - Web framework
- Werkzeug 3.1.3 - WSGI utility library
- Jinja2 3.1.6 - Template engine
- click 8.3.1 - Command-line interface toolkit
- blinker 1.9.0 - Signal/event system
- itsdangerous 2.2.0 - Data signing
- MarkupSafe 3.0.3 - String escaping

## Project Structure

```
simple-flask-restapi-app/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── swagger.yaml        # OpenAPI documentation
└── README.md          # This file
```

## Development

The application runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

**Note:** Disable debug mode in production by changing `app.run(debug=False)` in `app.py`.

## License

This project is open source and available for educational purposes.

## Author

AayushRajthala99