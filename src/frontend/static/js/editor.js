// Clase que controla todas las configuraciones y estados del editor de la barra superior
class EditorGrafo{

    constructor(){

        this.cy = null;

        this.modo = "seleccionar";

        this.nodoSeleccionado = null;

        this.origenArista = null;

        this.destinoDijkstra = null;

        this.origenMensaje = null;

        this.destinoMensaje = null;

        this.rutaActual = [];

    }

}

export const editor = new EditorGrafo();