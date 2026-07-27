from flask import render_template, jsonify, request


from app.servicios.simulador import Simulador
from app.modelos.nodo import Nodo
from app.modelos.arista import Arista
from app.algoritmos.dijkstra import Dijkstra
from app.servicios.cifrado import obtener_algoritmos, cifrar, descifrar



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

    @app.route("/api/nodos", methods=["GET"])
    def obtener_nodos():

        grafo = Simulador.obtener_grafo()

        return jsonify([
            nodo.dictar()
            for nodo in grafo.nodos.values()
        ])

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

    @app.route("/api/dijkstra", methods=["POST"])
    def ejecutar_dijkstra():

        datos = request.get_json()

        origen = datos["origen"]
        destino = datos["destino"]

        lambda_confianza = datos.get(
            "lambda_confianza",
            2.0
        )

        lambda_riesgo = datos.get(
            "lambda_riesgo",
            1.0
        )

        # Mensaje y clave opcioonales
        mensaje = datos.get("mensaje")
        clave_cifrado = datos.get("clave_cifrado")


        grafo = Simulador.obtener_grafo()


        resultado = Dijkstra.calcular(
            grafo,
            origen,
            destino,
            lambda_confianza,
            lambda_riesgo,
            mensaje,
            clave_cifrado
        )


        return jsonify(resultado)

    # Lista de algoritmos
    @app.route("/api/cifrado/algoritmos", methods=["GET"])
    def listar_algoritmos():
        return jsonify(obtener_algoritmos())

    # Ruta para cifrar
    @app.route("/api/cifrado/cifrar", methods=["POST"])
    def cifrar_texto():

        datos = request.get_json(silent=True)
        if datos is None:
            return jsonify({"error": "Cuerpo JSON requerido"}), 400

        algoritmo = datos.get("algoritmo")
        texto = datos.get("texto", "")
        clave = datos.get("clave")

        if algoritmo is None:
            return jsonify({"error": "Falta el campo de algoritmo"}), 400
        if clave is None:
            return jsonify({"error": "Falta el campo de clave"}), 400

        try:
            resultado = cifrar(algoritmo, texto, clave)
        except ValueError as e:
            # Clave inválida
            return jsonify({"error": str(e)}), 400

        return jsonify({"cifrado": resultado})

    # Ruta para descifrar
    @app.route("/api/cifrado/descifrar", methods=["POST"])
    def descifrar_texto():
        datos = request.get_json(silent=True)
        if datos is None:
            return jsonify({"error": "Cuerpo JSON requerido"}), 400

        algoritmo = datos.get("algoritmo")
        texto = datos.get("texto", "")
        clave = datos.get("clave")

        if algoritmo is None:
            return jsonify({"error": "Falta el campo de algoritmo"}), 400
        if clave is None:
            return jsonify({"error": "Falta el campo de clave"}), 400

        try:
            resultado = descifrar(algoritmo, texto, clave)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"texto": resultado})
    