from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.0"


@app.route("/")
def index():
    return jsonify({"message": "Demo API", "version": VERSION})


# Issue #1: Add /health endpoint here
# This is where Copilot will make its change during the demo


if __name__ == "__main__":
    app.run(debug=True, port=5000)