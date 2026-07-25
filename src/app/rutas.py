from flask import render_template
from flask import jsonify

from app.servicios.simulador import Simulador


def registrar_rutas(app):

    @app.route("/")
    def inicio():

        return render_template("index.html")


    @app.route("/grafo")
    def obtener_grafo():

        grafo = Simulador.crear_grafo_prueba()

        return jsonify(grafo.dictar())