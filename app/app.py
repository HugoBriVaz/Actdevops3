from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # Cambié el mensaje para confirmar que esta es la versión nueva
    return jsonify({"message": "¡Sistemas funcionando - Hugo Brihuega!"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Importante: host="0.0.0.0" permite que Docker hable con el mundo exterior
    app.run(host="0.0.0.0", port=5000)
