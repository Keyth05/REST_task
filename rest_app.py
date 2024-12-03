from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hola", methods=["GET"])
def obtener_hola():
    return jsonify({"mensaje": "Hello World from REST! My name is Keyth Yaguana"})

@app.route("/hola", methods=["POST"])
def crear_hola():
    datos = request.json
    return jsonify({"mensaje": f"Hello {datos.get('name', 'World')}!"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Listen on all interfaces and port 5000