import numpy as np # Librería para operaciones con matrices y vectores, útil para el cifrado Hill.

# ======= Cifrado Hill =======
# Se cifran bloques de letras usando una matriz como clave principal
# Fórmula para el cifrado --> C = (K*P) mod 26
# P = vector con las posiciones de las letras del bloque --> A=0, B=1, ... Z=25
# K = matriz clave, de tamaño n*n
# C = vector cifrado

def gcd(a, b):
    # Calcula el Máximo Común Divisor entre a y b
    # utilizando el algoritmo de Euclides.
    while b:
        a, b = b, a % b
    return a

def inverso_modular(a, m=26):
    # Busca el inverso modular de un número
    # Debe cumplir --> a*x mod 26 = 1
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def determinante(matriz):
    # Calcula el determinante de la matriz en mod 26.
    # Este valor se usa para verificar si la matriz clave es invertible en módulo 26.
    det = round(np.linalg.det(matriz)) # np.linalg.det calcula el determinante.
    return int(det % 26)

def validacion(matriz):
    # La matriz clave solo es válida si su determinante es invertible mod 26
    det = determinante(matriz)
    return gcd(det, 26) == 1

def matriz_inversa(matriz):
    # Calcula la inversa de la matriz en mod 26.
    det = determinante(matriz)
    determinante_inversa = inverso_modular(det)

    if determinante_inversa is None:
        raise ValueError(f"El determinante {det} no tiene inverso modular, la matriz no es válida como clave")

    # Se usa la identidad: adj(K) = det(K) * K^-1
    # np.linalg.inv calcula la inversa de la matriz
    # Se multiplica por el determinante para obtener la adjunta
    adjunta = np.round(det * np.linalg.inv(matriz)).astype(int)

    # Obtenemos la inversa modular con K^-1(mod 26) = det(K)^-1 * adj(K) mod 26
    inversa = (determinante_inversa * adjunta) % 26
    return inversa.astype(int)

def texto_a_bloques(texto, n):
    texto = texto.upper().replace(" ", "") # Eliminamos espacios y convertimos a mayúsculas
    texto = "".join(i for i in texto if i.isalpha()) # Eliminamos caracteres no alfabéticos

    while len(texto) % n != 0: # Rellenamos con 'X' hasta que el texto sea múltiplo de n
        texto += 'X'

    return [texto[i:i + n] for i in range(0, len(texto), n)] # Dividimos el texto en bloques de tamaño n

def cifrar_hill(texto, clave_matriz):
    # Verifica que la clave sea válida antes de cifrar.
    if not validacion(clave_matriz):
        raise ValueError("La matriz clave no es válida --> determinante no invertible mod 26")

    n = clave_matriz.shape[0]       # Obtiene el tamaño de la matriz clave n*n
    bloques = texto_a_bloques(texto, n)
    resultado = ""

    for bloque in bloques:
        # Convierte el bloque de letras en un vector de números A=0, B=1 ...
        vector = np.array([ord(c) - ord('A') for c in bloque])
        # Aplicamos la fórmula del cifrado Hill: C = K*P (mod 26)
        vector_cifrado = clave_matriz.dot(vector) % 26 # .dot() realiza la multiplicación de matriz por vector
        # Convierte el vector cifrado en letras.
        resultado += "".join(chr(int(x) + ord('A')) for x in vector_cifrado)
    return resultado

def descifrar_hill(texto_cifrado, clave_matriz):
    # Para descifrar, se usa la matriz inversa mod 26 de la clave
    inversa = matriz_inversa(clave_matriz)
    n = clave_matriz.shape[0]       # Obtiene el tamaño de la matriz clave n*n
    bloques = texto_a_bloques(texto_cifrado, n)
    resultado = "" # Cadena para almacenar el resultado descifrado

    for bloque in bloques:
        # Convierte el bloque de letras en un vector de números A=0, B=1 ...
        vector = np.array([ord(c) - ord('A') for c in bloque])
        # Aplicamos la fórmula: P = K^-1 * C (mod 26)
        vector_descifrado = inversa.dot(vector) % 26 # .dot() realiza la multiplicación de matriz por vector
        # Convierte el vector descifrado en letras.
        resultado += "".join(chr(int(x) + ord('A')) for x in vector_descifrado)

    return resultado

# Prueba
# Clave 2x2
clave = np.array([[3,3],[2,5]])

cifrado = cifrar_hill("Hola Esto es un test 123 $%&/ .  .", clave)
print("Cifrado Hill:", cifrado)

descifrado = descifrar_hill(cifrado, clave)
print("Descifrado Hill:", descifrado)