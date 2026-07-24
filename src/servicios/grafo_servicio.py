from modelos.arista import Arista
from modelos.nodo import Nodo
from modelos.grafo import Grafo

class GrafoService:
    @staticmethod

    # Ejemplo de grafo para probar
    def grafo_prueba():

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