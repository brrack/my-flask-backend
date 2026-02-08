from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "backend alive"})

@app.route("/ping")
def ping():
    return jsonify({"pong": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
