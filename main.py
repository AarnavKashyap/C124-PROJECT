from flask import Flask, jsonify, request
app = Flask(__name__)

contacts = [
    {
        "Contact": 9885637373,
        "Name": "Ram",
        "id": 1,
        "done": False
    },
    {
        "Contact": 9976554321,
        "Name": "Rahul",
        "id": 2,
        "done": False
    }
]

@app.route("/add_data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        })
    contact = {
        "id": contacts[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })

if(__name__ == "__main__"):
    app.run(debug = True)