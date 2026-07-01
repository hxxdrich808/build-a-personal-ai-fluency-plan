from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data store for demonstration purposes
milestones = [
    {"id": 1, "title": "Week 1: Data Literacy Basics", "status": "pending"},
    {"id": 2, "title": "Month 1: Model Understanding Fundamentals", "status": "pending"},
    {"id": 3, "title": "Quarter 1: Ethical Considerations Project", "status": "pending"}
]

@app.route("/api/milestones", methods=["GET"])
def get_milestones():
    return jsonify(milestones)

@app.route("/api/milestones/<int:mid>", methods=["PATCH"])
def update_milestone(mid):
    data = request.json
    for m in milestones:
        if m["id"] == mid:
            m.update(data)
            return jsonify({"message": "Milestone updated", "milestone": m})
    return jsonify({"error": "Milestone not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
