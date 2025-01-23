from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]

# GET /users: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET /users/<id>: Get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST /users: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if "name" in data and "email" in data:
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "email": data["email"]
        }
        users.append(new_user)
        return jsonify(new_user), 201
    return jsonify({"message": "Invalid data"}), 400

# PUT /users/<id>: Update an existing user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        data = request.get_json()
        user["name"] = data.get("name", user["name"])
        user["email"] = data.get("email", user["email"])
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# DELETE /users/<id>: Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [user for user in users if user["id"] != id]
    return jsonify({"message": "User deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
