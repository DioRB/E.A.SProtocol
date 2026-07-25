from flask import Flask, render_template, jsonify
from app.servicios.grafo_servicio import GrafoService

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Ruta para probar el grafo
@app.route("/grafo")
def grafo():
    grafo = GrafoService.grafo_prueba()

    return jsonify(grafo.dictar())

if __name__ == "__main__":
    app.run(debug=True)