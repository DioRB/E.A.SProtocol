//Archivo principal que lleva todo al html
import "./interfaz.js";
import {obtenerGrafo} from "./api.js";
import {dibujarGrafo, actualizarGrafo} from "./grafo.js";
import { reiniciarGrafo} from "./api.js";

async function iniciar(){

    const grafo = await obtenerGrafo();

    dibujarGrafo(grafo);

}

iniciar();