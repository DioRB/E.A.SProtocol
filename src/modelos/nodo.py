class Nodo:

    def __init__(self, nodo_id, etiqueta, nivel_confianza=1.0, estado="Seguro", x=0, y=0):
        self.id = nodo_id
        self.etiqueta = etiqueta
        self.nivel_confianza = nivel_confianza
        self.estado = estado
        self.x = x
        self.y = y

    def dictar(self):
        return {
            "id": self.id,
            "etiqueta": self.etiqueta,
            "nivel_confianza": self.nivel_confianza,
            "estado": self.estado,
            "x": self.x,
            "y": self.y
        }