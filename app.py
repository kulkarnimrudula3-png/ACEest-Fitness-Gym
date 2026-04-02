from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------
# Sample Data (In-Memory DB)
# -----------------------------
members = [
    {"id": 1, "name": "Rahul Sharma", "age": 25, "plan": "Monthly", "status": "Active"},
    {"id": 2, "name": "Priya Patil", "age": 28, "plan": "Quarterly", "status": "Active"},
    {"id": 3, "name": "Roy", "age": 23, "plan": "Monthly", "status": "Active"},
    {"id": 4, "name": "Renna Shinde", "age": 28, "plan": "Quarterly", "status": "Inactive"}
]

# -----------------------------
# Home API
# -----------------------------
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym Management System"
    })


# -----------------------------
# Health Check API
# -----------------------------
@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    }), 200


# -----------------------------
# Get All Members
# -----------------------------
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify({
        "total_members": len(members),
        "members": members
    })


# -----------------------------
# Get Member by ID
# -----------------------------
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return jsonify(member)

    return jsonify({"error": "Member not found"}), 404


# -----------------------------
# Add New Member
# -----------------------------
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    new_member = {
        "id": len(members) + 1,
        "name": data.get("name"),
        "age": data.get("age"),
        "plan": data.get("plan"),
        "status": data.get("status", "Active")
    }

    members.append(new_member)

    return jsonify({
        "message": "Member added successfully",
        "member": new_member
    }), 201


# -----------------------------
# Update Member
# -----------------------------
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()

    for member in members:
        if member["id"] == member_id:
            member["name"] = data.get("name", member["name"])
            member["age"] = data.get("age", member["age"])
            member["plan"] = data.get("plan", member["plan"])
            member["status"] = data.get("status", member["status"])

            return jsonify({
                "message": "Member updated successfully",
                "member": member
            })

    return jsonify({"error": "Member not found"}), 404


# -----------------------------
# Delete Member
# -----------------------------
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members

    members = [m for m in members if m["id"] != member_id]

    return jsonify({
        "message": "Member deleted successfully"
    })


# -----------------------------
# Run Application
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)