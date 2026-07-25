import heapq
from app.modelos.grafo import Grafo


class Dijkstra:
    """
    Calcula la ruta de menor costo entre dos nodos utilizando el algoritmo de Dijkstra.

    Parámetros:
        grafo (Grafo): Grafo sobre el que se ejecuta el algoritmo.
        origen (str): Identificador del nodo inicial.
        destino (str): Identificador del nodo destino.

    Retorna:
        dict:
            ruta (list): Ruta óptima encontrada.
            costo (float): Costo total de la ruta.
            visitados (list): Orden en que se visitaron los nodos.
            distancias (dict): Distancia mínima calculada a cada nodo.
            anteriores (dict): Nodo predecesor de cada nodo.
            timeline (list): Línea de tiempo con todos los eventos del algoritmo.
    """

    @staticmethod
    def calcular(
        grafo: Grafo,
        origen: str,
        destino: str,
        lambda_confianza: float = 2.0,
        lambda_riesgo: float = 1.0
    ) -> dict:

        #VALIDACIONES

        if not grafo.existe_nodo(origen):
            raise ValueError(f"El nodo '{origen}' no existe.")

        if not grafo.existe_nodo(destino):
            raise ValueError(f"El nodo '{destino}' no existe.")

        #ESTRUCTURAS
        distancias = {}
        anteriores = {}
        visitados = set()
        orden_visita = []
        timeline = []
        cola = []

        for nodo_id in grafo.nodos:
            distancias[nodo_id] = float("inf")
            anteriores[nodo_id] = None

        distancias[origen] = 0

        heapq.heappush(
            cola,
            (0, origen)
        )

        #DIJKSTRA

        while cola:

            distancia_actual, actual = heapq.heappop(cola)

            if actual in visitados:
                continue

            visitados.add(actual)
            orden_visita.append(actual)

            timeline.append({
                "tipo": "visita",
                "nodo": actual,
                "distancia": distancia_actual,
                "distancias": distancias.copy(),
                "visitados": list(visitados)
            })

            if actual == destino:
                break

            for arista in grafo.obtener_vecinos(actual):

                vecino = arista.fin
                nodo_vecino = grafo.obtener_nodo(vecino)

                penalizacion_confianza = (
                    lambda_confianza *
                    (1 - nodo_vecino.nivel_confianza)
                )

                penalizacion_riesgo = (
                    lambda_riesgo *
                    arista.riesgo
                )

                costo_arista = (
                    arista.peso
                    + penalizacion_confianza
                    + penalizacion_riesgo
                )

                nuevo_costo = (
                    distancia_actual
                    + costo_arista
                )

                costo_anterior = distancias[vecino]

                if nuevo_costo < costo_anterior:

                    distancias[vecino] = nuevo_costo
                    anteriores[vecino] = actual

                    heapq.heappush(
                        cola,
                        (nuevo_costo, vecino)
                    )

                    actualizado = True

                else:

                    actualizado = False

                timeline.append({
                    "tipo": "relajacion",
                    "desde": actual,
                    "hasta": vecino,
                    "peso": arista.peso,
                    "riesgo": arista.riesgo,
                    "confianza": nodo_vecino.nivel_confianza,
                    "penalizacion_confianza": round(
                        penalizacion_confianza,
                        3
                    ),

                    "penalizacion_riesgo": round(
                        penalizacion_riesgo,
                        3
                    ),

                    "costo_arista": round(
                        costo_arista,
                        3
                    ),

                    "costo_anterior": round(
                        costo_anterior,
                        3
                    ) if costo_anterior != float("inf") else "∞",

                    "nuevo_costo": round(
                        nuevo_costo,
                        3
                    ),
                    "actualizado": actualizado
                })

        #NO EXISTE RUTA
        if distancias[destino] == float("inf"):

            return {
                "ruta": [],
                "costo": None,
                "visitados": orden_visita,
                "distancias": distancias,
                "anteriores": anteriores,
                "timeline": timeline,
                "mensaje": "No existe una ruta entre los nodos."

            }

        #RECONSTRUIR RUTA
        ruta = []

        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]
        ruta.reverse()

        #RESULTADO
        return {
            "ruta": ruta,
            "costo": round(
                distancias[destino],
                3
            ),

            "visitados": orden_visita,
            "distancias": {
                nodo: (
                    round(valor, 3)
                    if valor != float("inf")
                    else "∞"
                )
                for nodo, valor in distancias.items()
            },
            "anteriores": anteriores,
            "timeline": timeline,
            "parametros": {
                "lambda_confianza": lambda_confianza,
                "lambda_riesgo": lambda_riesgo

            }

        }