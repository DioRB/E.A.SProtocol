# ======= Cifrado Afín ======= 
# Generalización del cifrado César
# Fórmula para el cifrado --> E(x) = (a*x+b) mod 26
# x = posición de la letra, ejem: A=0, B=1, ..., Z=25
# a y b = claves del cifrado


def gcd(a, b):
    # Calcula el Máximo Común Divisor entre a y b
    # utilizando el algoritmo de Euclides.
    while b:
        # Se reemplazan los valores hasta que el residuo sea 0.
        a, b = b, a % b
    return a

def validacion_clave(a):
    # la clave debe ser coprima con 26.
    return gcd(a, 26) == 1

def inverso_modular(a, m=26):
    # Busca el inverso modular
    # Debe cumplir --> (a*x) mod 26 = 1
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def cifrar_afin(texto, a, b):
    # Verifica que la clave sea válida.
    if not validacion_clave(a):
        raise ValueError(f"a = {a} no es válido, no puede ser divisible por 2 y/o 13.")
    resultado = ""

    # Recorre cada carácter del texto convertido a mayúsculas.
    for i in texto.upper():
        # Solo se cifran letras.
        if i.isalpha():
            # Convierte la letra en un número entre 0 y 25.
            # ord() devuelve el código ASCII de la letra, por ejemplo A=65, B=66...
            # Al restar ord('A'), se obtiene la posición de la letra en el alfabeto:
            # A -> 0, B -> 1 ... Z -> 25.
            x = ord(i) - ord('A')
            # Aplicamos la fórmula del cifrado afín.
            e = (a * x + b) % 26
            # Convierte nuevamente el número obtenido en una letra.
            resultado += chr(e + ord('A'))
        else:
            # Espacios y/o símbolos no se cifran, se agregan tal cual al resultado.
            resultado += i
    return resultado

def descifrar_afin(texto_cifrado, a, b):

    # Obtiene el inverso modular de 'a'.
    a_inv = inverso_modular(a)

    # no es posible recuperar el mensaje si no hay inverso modular.
    if a_inv is None:
            raise ValueError(f"a={a} no es válido, a no debe ser divisible por 2 ni por 13")
    resultado = ""

    # Recorre cada carácter del texto cifrado.
    for i in texto_cifrado.upper():

        if i.isalpha():
            # Convierte la letra cifrada a un número.
            y = ord(i) - ord('A')
            # Aplicamos la fórmula inversa del cifrado afín
            # D(y) = a^-1 * (y-b) mod 26
            x = (a_inv * (y - b)) % 26

            # Convierte nuevamente el número en una letra.
            resultado += chr(x + ord('A'))

        else:
            # Espacios y/o símbolos no se descifran, se agregan tal cual al resultado.
            resultado += i

    return resultado

# Prueba
'''
cifrado = cifrar_afin("Hola Esto es un test 123 $%&/ .  .", a=5, b=8)
print("Cifrado afín:", cifrado)
# Se descifra
descifrado = descifrar_afin(cifrado, a=5, b=8)
print("Descifrado:", descifrado)
'''
