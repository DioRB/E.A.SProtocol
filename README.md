# E.A.S Protocol
### (Encrypted / Anti-Attack / Solving Protocol)

---

## Integrantes:

- Jair Gomez Narvaez
- Aimer Garcia Esteban Rojas
- Diego Alejandro Robayo Córdoba 

**Docente:** Jhoan Sebastián Tenjo García

---

## Descripción

**E.A.S Protocol (Efficient and Adaptive Secure Protocol)** es una aplicación desarrollada como proyecto para la asignatura **Matemáticas Discretas I** de la Universidad Nacional de Colombia. El sistema simula una red de comunicación representada mediante grafos dirigidos, permitiendo calcular y visualizar la ruta óptima entre dos nodos mediante una versión adaptada del algoritmo de Dijkstra y cifrar o descifrar los mensajes enviados por esa ruta.

Respecto al algoritmo de Dijkstra, a diferencia del algoritmo tradicional, la solución implementada considera no solo el peso de las aristas, sino también el nivel de riesgo de los enlaces y el nivel de confianza de los nodos, utilizando una función de costo personalizada que permite obtener rutas más seguras y eficientes.

Respecto a los algoritmos de criptografia, se implementaron dos esquemas fundamentados en aritmética modular, el cifrado afín, que cifra cada letra del mensaje mediante una transformación lineal módulo 26 y el cifrado hill, que cifra bloques de letras mediante multiplicación matricial en módulo 26, cuenta con soporte para claves de tamaños variables. Para ambos casos, se valida matemáticamente que la clave cumpla con los requisitos, garantizando que todos los mensajes cifrados, puedan descifrarse en el destino.

La aplicación ofrece una interfaz gráfica interactiva donde el usuario puede crear, editar y eliminar nodos y aristas, asignar sus atributos y ejecutar el algoritmo para visualizar paso a paso el proceso de búsqueda de la ruta óptima. Además, incorpora módulos de criptografía para el cifrado y descifrado de mensajes mediante diferentes algoritmos, fortaleciendo el enfoque de seguridad del proyecto.

El proyecto fue desarrollado utilizando **Python**, **Flask**, **JavaScript**, **HTML**, **CSS**, siguiendo una arquitectura modular que facilita el mantenimiento, la escalabilidad y la integración de nuevos componentes.

---

### Requisitos:
Para ejecutar el proyecto es necesario contar con:

- Python 3.10 o superior (version mas reciente si es posible).
- Git (opcional, para clonar el repositorio).
- Un navegador web moderno (Google Chrome, Microsoft Edge, Mozilla Firefox, etc).

Las dependencias del proyecto se encuentran definidas en el archivo `requirements.txt` y pueden instalarse mediante:

```bash
pip install -r requirements.txt
```

Entre las principales bibliotecas utilizadas se encuentran:

- Flask, para el desarrollo del servidor web y la API.
- NumPy (última versión estable), utilizado para operaciones matriciales y la implementación de los algoritmos criptográficos del proyecto.

---

### Instalación
1. Clonar el repositorio:

```bash
git clone https://github.com/DioRB/E.A.SProtocol.git
```

2. Acceder al directorio del proyecto:

```bash
cd E.A.SProtocol
```

3. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

### Ejecución
Una vez instaladas las dependencias, inicie el servidor ejecutando el siguiente comando desde la raíz del proyecto:

```bash
python src/main.py
```

Si la ejecución es correcta, Flask iniciará el servidor local. Abra su navegador y acceda a la siguiente dirección:

```
http://127.0.0.1:5000
```

Desde la interfaz web será posible crear y administrar grafos, configurar los parámetros de los nodos y aristas, ejecutar el algoritmo de Dijkstra adaptado y utilizar los módulos criptográficos implementados en la aplicación.

---

### Ejemplo de uso



---

### Estado Actual del Proyecto
 