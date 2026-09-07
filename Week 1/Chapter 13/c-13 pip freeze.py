from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to my Flask Web Server!</h1><p>Go to /api/info to see JSON data.</p>"

@app.route("/user/<username>", methods=["GET"])
def greet_user(username):
    return f"Hello, {username}! Welcome back."
@app.route("/api/info", methods=["GET"])
def get_info():
    server_data = {
        "status": "running",
        "framework": "Flask",
        "language": "Python 3",
        "features": ["Routing", "JSON Handling", "Dynamic URLs"]
    }
    return jsonify(server_data)

if __name__ == "__main__":
    # debug=True automatically reloads the server when you change code
    app.run(host="127.0.0.1", port=5000, debug=True)
