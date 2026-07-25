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
    def calcular(grafo: Grafo, origen: str, destino: str) -> dict:

        # 1.VALIDACIONES
        if not grafo.existe_nodo(origen):
            raise ValueError(f"El nodo '{origen}' no existe.")

        if not grafo.existe_nodo(destino):
            raise ValueError(f"El nodo '{destino}' no existe.")

        #2. ESTRUCTURAS
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

        heapq.heappush(cola, (0, origen))


        # 3. DIJKSTRA
        while cola:

            distancia_actual, actual = heapq.heappop(cola)

            if actual in visitados:
                continue

            visitados.add(actual)
            orden_visita.append(actual)

            #Registrar visita
            timeline.append({
                "tipo": "visita",
                "nodo": actual,
                "distancia": distancia_actual,
                "distancias": distancias.copy(),
                "visitados": list(visitados)
            })

            if actual == destino:
                break

            #Recorrer todos los vecinos
            for arista in grafo.obtener_vecinos(actual):

                vecino = arista.fin

                nuevo_costo = distancia_actual + arista.peso

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

                #Registrar relajación
                timeline.append({
                    "tipo": "relajacion",
                    "desde": actual,
                    "hasta": vecino,
                    "peso": arista.peso,
                    "costo_anterior": costo_anterior,
                    "nuevo_costo": nuevo_costo,
                    "actualizado": actualizado
                })

        # 4. NO EXISTE RUTA
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

        # 5.RECONSTRUIR RUTA
        ruta = []

        actual = destino

        while actual is not None:

            ruta.append(actual)
            actual = anteriores[actual]

        ruta.reverse()

        #6.RETORNAR RESULTADO
        return {
            "ruta": ruta,
            "costo": distancias[destino],
            "visitados": orden_visita,
            "distancias": distancias,
            "anteriores": anteriores,
            "timeline": timeline
        }