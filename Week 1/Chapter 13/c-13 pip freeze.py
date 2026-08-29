from flask import Flask, jsonify, request

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define the Home route (Root URL)
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to my Flask Web Server!</h1><p>Go to /api/info to see JSON data.</p>"

# 3. Define a dynamic route that accepts a parameter in the URL
@app.route("/user/<username>", methods=["GET"])
def greet_user(username):
    return f"Hello, {username}! Welcome back."

# 4. Define an API route returning structured JSON data
@app.route("/api/info", methods=["GET"])
def get_info():
    server_data = {
        "status": "running",
        "framework": "Flask",
        "language": "Python 3",
        "features": ["Routing", "JSON Handling", "Dynamic URLs"]
    }
    return jsonify(server_data)

# 5. Run the web server
if __name__ == "__main__":
    # debug=True automatically reloads the server when you change code
    app.run(host="127.0.0.1", port=5000, debug=True)
