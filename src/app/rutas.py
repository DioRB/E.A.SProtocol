from flask import render_template, jsonify, request


from app.servicios.simulador import Simulador
from app.modelos.nodo import Nodo
from app.modelos.arista import Arista
from app.algoritmos.dijkstra import Dijkstra



def registrar_rutas(app):

    ## Home
    @app.route("/")
    def inicio():
        return render_template("index.html")

    ## Endpoint para ver en json la creación del grafo
    @app.route("/grafo")
    def obtener_grafo():

        grafo = Simulador.obtener_grafo()

        return jsonify(grafo.dictar())

    ## Ruta para la creación de los nodos
    @app.route("/api/nodos", methods=["POST"])
    def crear_nodo():

        datos = request.get_json()

        nodo = Nodo(

            nodo_id=datos["id"],
            etiqueta=datos["etiqueta"],

            nivel_confianza=datos.get(
                "nivel_confianza",
                1.0
            ),

            estado=datos.get(
                "estado",
                "Seguro"
            ),

            x=datos.get("x", 100),

            y=datos.get("y", 100)

        )

        grafo = Simulador.obtener_grafo()

        grafo.agregar_nodo(nodo)

        return jsonify(nodo.dictar())

    ## Ruta para la eliminación de nodos
    @app.route("/api/nodos/<id>", methods=["DELETE"])
    def eliminar_nodo(id):

        grafo = Simulador.obtener_grafo()

        grafo.eliminar_nodo(id)

        return jsonify({

            "mensaje":"Nodo eliminado"

        })

    ## Ruta para la creación de aristas
    @app.route("/api/aristas", methods=["POST"])
    def crear_arista():

        datos = request.get_json()

        arista = Arista(

            inicio=datos["inicio"],
            fin=datos["fin"],
            peso=datos["peso"],
            riesgo=datos["riesgo"]

        )

        grafo = Simulador.obtener_grafo()

        grafo.agregar_arista(arista)

        return jsonify(arista.dictar())

    ## Ruta para la eliminación de aristas
    @app.route("/api/aristas", methods=["DELETE"])
    def eliminar_arista():

        datos = request.get_json()

        grafo = Simulador.obtener_grafo()

        grafo.eliminar_arista(

            datos["inicio"],
            datos["fin"]

        )

        return jsonify({

            "mensaje":"Arista eliminada"

        })

    ## Ruta que reinicia el grafo
    @app.route("/api/grafo/reiniciar", methods=["POST"])
    def reiniciar_grafo():

        grafo = Simulador.reiniciar_grafo()

        return jsonify(grafo.dictar())