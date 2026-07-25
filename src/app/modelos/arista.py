class Arista:

    def __init__(self, inicio, fin, peso=1, riesgo=0):
        self.inicio = inicio
        self.fin = fin
        self.peso = peso
        self.riesgo = riesgo

    def dictar(self):
        return {
            "inicio": self.inicio,
            "fin": self.fin,
            "peso": self.peso,
            "riesgo": self.riesgo
        }