from app.modelos.arista import Arista
from app.modelos.nodo import Nodo
from app.modelos.grafo import Grafo
from app.algoritmos.dijkstra import Dijkstra

class Simulador:
    @staticmethod

    # Ejemplo de grafo para probar
    def crear_grafo_prueba():

        grafo = Grafo()


        grafo.agregar_nodo(Nodo("A", "A", 0.95,"Seguro", 100, 200))
        grafo.agregar_nodo(Nodo("B", "B", 0.95,"Seguro", 300, 100))
        grafo.agregar_nodo(Nodo("C", "C", 0.95,"Seguro", 300, 300))
        grafo.agregar_nodo(Nodo("D", "D", 0.95,"Seguro", 500, 100))
        grafo.agregar_nodo(Nodo("E", "E", 0.95,"Seguro", 500, 300))

        grafo.agregar_arista(Arista("A", "B", 3))
        grafo.agregar_arista(Arista("A", "C", 2))
        grafo.agregar_arista(Arista("B", "D", 5))
        grafo.agregar_arista(Arista("C", "D", 1))
        grafo.agregar_arista(Arista("D", "E", 2))

        return grafo        

#Recorrer el grafo utilizando el algoritmo Dijkstra (Primera prueba)
grafo = Simulador.crear_grafo_prueba()

ruta, costo = Dijkstra.calcular(
    grafo,
    "A",
    "E"
)

print(ruta)
print(costo)