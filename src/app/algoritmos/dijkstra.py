import heapq


class Dijkstra:

    @staticmethod
    def calcular(grafo, origen, destino):

        distancias = {}
        anteriores = {}
        visitados = set()
        cola = []

        #Inicializar estructuras
        for nodo_id in grafo.nodos:

            distancias[nodo_id] = float("inf")
            anteriores[nodo_id] = None

        distancias[origen] = 0

        heapq.heappush(cola, (0, origen))

        while cola:

            distancia_actual, actual = heapq.heappop(cola)

            if actual in visitados:
                continue

            visitados.add(actual)

            if actual == destino:
                break

            #Recorrer vecinos
            for arista in grafo.obtener_vecinos(actual):

                vecino = arista.fin

                nuevo_costo = distancia_actual + arista.peso

                if nuevo_costo < distancias[vecino]:

                    distancias[vecino] = nuevo_costo
                    anteriores[vecino] = actual

                    heapq.heappush(
                        cola,
                        (nuevo_costo, vecino)
                    )

        #Reconstruir ruta
        ruta = []

        actual = destino

        while actual is not None:

            ruta.append(actual)
            actual = anteriores[actual]

        ruta.reverse()

        return ruta, distancias[destino]