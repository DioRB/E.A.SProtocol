// Interfaz que relaciona todos los elementos graficos de la página con las funciones adjudicadas
import { reiniciarGrafo } from "./api.js";
import { actualizarGrafo } from "./grafo.js";
import { editor } from "./editor.js";

export function cambiarModo(nuevoModo){

    editor.modo = nuevoModo;

    actualizarToolbar();

}

function actualizarToolbar(){
    document
        .querySelectorAll(".toolbar button")
        .forEach(b=>b.classList.remove("activo"));

    // Switch de cada estado y funcionalidad. En cada case se observa lo que hace
    switch(editor.modo){

        case "crear_nodo":
            document
                .getElementById("modoNodo")
                .classList.add("activo");
            break;

        case "crear_arista":
            document
                .getElementById("modoArista")
                .classList.add("activo");
            break;

        case "eliminar":
            document
                .getElementById("modoEliminar")
                .classList.add("activo");
            break;

        default:
            document
                .getElementById("modoSeleccionar")
                .classList.add("activo");
    }

}

actualizarToolbar();

// los eventos para cada botón
document
    .getElementById("modoSeleccionar")
    .addEventListener("click", () => {

        cambiarModo("seleccionar");

    });

document
    .getElementById("modoNodo")
    .addEventListener("click", () => {

        cambiarModo("crear_nodo");

    });

document
    .getElementById("modoArista")
    .addEventListener("click", () => {

        cambiarModo("crear_arista");

    });

document
    .getElementById("modoEliminar")
    .addEventListener("click", () => {

        cambiarModo("eliminar");

    });

document
    .getElementById("modoDijkstra")
    .addEventListener("click", () => {

        cambiarModo("dijkstra");

    });

document
    .getElementById("modoCifrado")
    .addEventListener("click", () => {

        cambiarModo("cifrado");

    });


document
    .getElementById("reiniciar")
    .addEventListener("click", async () => {

        const confirmar = confirm(
            "¿Desea reiniciar el grafo?"
        );

        if (!confirmar) {
            return;
        }

        const grafo = await reiniciarGrafo();

        actualizarGrafo(grafo);

        cambiarModo("seleccionar");

    });