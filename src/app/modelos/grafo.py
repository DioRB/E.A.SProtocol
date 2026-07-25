from app.modelos.arista import Arista
from app.modelos.nodo import Nodo

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, nodo: Nodo):

        if nodo.id not in self.nodos:
            self.nodos[nodo.id] = nodo

    def eliminar_nodo(self, nodo_id):

        if nodo_id in self.nodos:
            del self.nodos[nodo_id]

            self.aristas = [
                arista for arista in self.aristas
                if arista.inicio != nodo_id and arista.fin != nodo_id
            ]

    def agregar_arista(self, arista: Arista):

        if arista.inicio in self.nodos and arista.fin in self.nodos:
            self.aristas.append(arista)

    def eliminar_arista(self, inicio, fin):

        self.aristas = [
            arista for arista in self.aristas
            if not (
                arista.inicio == inicio and
                arista.fin == fin
            )
        ]

    def obtener_vecinos(self, nodo_id):

        vecinos = []

        for arista in self.aristas:

            if arista.inicio == nodo_id:
                vecinos.append(arista.fin)

        return vecinos

    def obtener_nodo(self, nodo_id):

        return self.nodos.get(nodo_id)

    def dictar(self):

        return {

            "nodos": [
                nodo.dictar()
                for nodo in self.nodos.values()
            ],

            "aristas": [
                arista.dictar()
                for arista in self.aristas
            ]
        }