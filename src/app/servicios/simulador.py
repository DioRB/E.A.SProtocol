from app.modelos.arista import Arista
from app.modelos.nodo import Nodo
from app.modelos.grafo import Grafo
from app.algoritmos.dijkstra import Dijkstra

class Simulador:
    @staticmethod

    # Ejemplo de grafo para probar
    def crear_grafo_prueba():

        grafo = Grafo()


        grafo.agregar_nodo(Nodo("A","A",0.98,"Seguro",100,200))
        grafo.agregar_nodo(Nodo("B","B",0.55,"Comprometido",300,100))
        grafo.agregar_nodo(Nodo("C","C",0.92,"Seguro",300,300))
        grafo.agregar_nodo(Nodo("D","D",0.75,"En monitoreo",500,100))
        grafo.agregar_nodo(Nodo("E","E",0.99,"Seguro",500,300))

        grafo.agregar_arista(Arista("A","B",3,0.20))
        grafo.agregar_arista(Arista("A","C",2,0.10))
        grafo.agregar_arista(Arista("B","D",5,0.80))
        grafo.agregar_arista(Arista("C","D",1,0.30))
        grafo.agregar_arista(Arista("D","E",2,0.15))

        return grafo        

    
    grafo = None

    @classmethod
    def inicializar(cls):

        if cls.grafo is None:

            cls.grafo = cls.crear_grafo_prueba()

    @classmethod
    def obtener_grafo(cls):

        cls.inicializar()

        return cls.grafo

    @classmethod
    def reiniciar_grafo(cls):

        cls.grafo = cls.crear_grafo_prueba()

        return cls.grafo

