//Archivo principal que lleva todo al html
import "./interfaz.js";
import {obtenerGrafo} from "./api.js";
import {dibujarGrafo, actualizarGrafo, resaltarRuta,} from "./grafo.js";
import { reiniciarGrafo, ejecutarDijkstra} from "./api.js";
import {cargarNodosDijkstra} from "./interfaz.js";

async function iniciar(){

    const grafo = await obtenerGrafo();

    dibujarGrafo(grafo);

    cargarNodosDijkstra(grafo);

    actualizarListaNodos();
}

iniciar();