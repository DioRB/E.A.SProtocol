import numpy as np

# Prefijos pues chocan con otras funciones
from app.criptografia.cesar import cifrar_afin as cifrar_afin_mod, descifrar_afin as descifrar_afin_mod
from app.criptografia.hill import cifrar_hill, descifrar_hill

# Lista de algoritmos para frontend
ALGORITMOS = [
    {
        "nombre": "afin",
        "etiqueta": "Cifrado Afín",
        "parametros": [
            {"nombre": "a", "etiqueta": "a", "tipo": "numero", "min": 1, "max": 25},
            {"nombre": "b", "etiqueta": "b", "tipo": "numero", "min": 0, "max": 25}
        ]
    },
    {
        "nombre": "hill",
        "etiqueta": "Cifrado Hill",
        "parametros": [
            {"nombre": "n", "etiqueta": "Tamaño de la matriz n x n", "tipo": "numero", "min": 2, "max": 5}
        ],
        "matriz": True
    }
]

def obtener_algoritmos():
    return ALGORITMOS

def cifrar_afin(texto, clave):
    # Clave de afín, es un diccionario con a y b
    a = int(clave["a"])
    b = int(clave["b"])
    return cifrar_afin_mod(texto, a, b)

def descifrar_afin(texto, clave):
    a = int(clave["a"])
    b = int(clave["b"])
    return descifrar_afin_mod(texto, a, b)

def _armar_matriz(clave):
    # La clave de Hill, es un diccionario con n y una matriz
    n = int(clave["n"])
    celdas = clave["matriz"]

    # Validamos coincida con n
    if len(celdas) != n:
        raise ValueError(f"La cantidad de filas es diferente a {n}")

    matriz = []
    for fila in celdas:
        if len(fila) != n:
            raise ValueError(f"La cantidad de columnas es diferente a {n}")
        # Cada celda la pasamos a entero, evitando problemas con aritmética modular
        nueva_fila = []
        for valor in fila:
            nueva_fila.append(int(valor))
        matriz.append(nueva_fila)
    return np.array(matriz)

def _cifrar_hill(texto, clave):
    matriz = _armar_matriz(clave)
    return cifrar_hill(texto, matriz)

def _descifrar_hill(texto, clave):
    matriz = _armar_matriz(clave)
    return descifrar_hill(texto, matriz)

# Funciones de cifrado y descifrado dependiendo del algoritmo.
def cifrar(algoritmo, texto, clave):
    if algoritmo == "afin":
        return cifrar_afin(texto, clave)

    if algoritmo == "hill":
        return _cifrar_hill(texto, clave)

    raise ValueError(f"Algoritmo no soportado: {algoritmo}")

def descifrar(algoritmo, texto, clave):
    if algoritmo == "afin":
        return descifrar_afin(texto, clave)

    if algoritmo == "hill":
        return _descifrar_hill(texto, clave)

    raise ValueError(f"Algoritmo no soportado: {algoritmo}")

