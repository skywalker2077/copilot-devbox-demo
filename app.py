from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.0"


@app.route("/")
def index():
    return jsonify({"message": "Demo API", "version": VERSION})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
