// Interfaz que relaciona todos los elementos graficos de la página con las funciones adjudicadas
import { reiniciarGrafo, ejecutarDijkstra, obtenerNodos} from "./api.js";
import {actualizarGrafo,resaltarRuta,limpiarResaltado,animarTimeline} from "./grafo.js";
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

export async function actualizarListaNodos(){

    const nodos = await obtenerNodos();


    const origen =
        document.getElementById("origenDijkstra");

    const destino =
        document.getElementById("destinoDijkstra");


    origen.innerHTML="";
    destino.innerHTML="";


    nodos.forEach(nodo=>{


        const opcion1 =
        document.createElement("option");

        opcion1.value=nodo.id;
        opcion1.textContent=nodo.etiqueta;


        const opcion2 =
        document.createElement("option");

        opcion2.value=nodo.id;
        opcion2.textContent=nodo.etiqueta;


        origen.appendChild(opcion1);
        destino.appendChild(opcion2);

    });

}

export function cargarNodosDijkstra(data){

    const origen =
    document.getElementById(
        "origenDijkstra"
    );

    const destino =
    document.getElementById(
        "destinoDijkstra"
    );

    origen.innerHTML="";
    destino.innerHTML="";

    data.nodos.forEach(nodo=>{

        let opcion1 =
        document.createElement("option");

        opcion1.value=nodo.id;
        opcion1.text=nodo.id;

        let opcion2 =
        document.createElement("option");

        opcion2.value=nodo.id;
        opcion2.text=nodo.id;

        origen.appendChild(opcion1);

        destino.appendChild(opcion2);

    });
}

function mostrarResultado(resultado){

    const panel = document.getElementById(
        "resultadoDijkstra"
    );

    if(resultado.ruta.length===0){

        panel.innerHTML=`

            <h3>Resultado</h3>

            <p>${resultado.mensaje}</p>

        `;

        return;

    }

    panel.innerHTML=`
        <h3>Resultado Dijkstra</h3>
        <p>
            <strong>Ruta:</strong><br>
            ${resultado.ruta.join(" → ")}
        </p>
        <hr>
        <p>
            <strong>Costo total:</strong>
            ${resultado.costo}
        </p>
        <h4>Métricas</h4>
        <p>
            Peso total:
            ${resultado.metricas.peso_total}
        </p>
        <p>
            Riesgo total:
            ${resultado.metricas.riesgo_total}
        </p>
        <p>
            Penalización confianza:
            ${resultado.metricas.penalizacion_confianza_total}
        </p>
        <hr>
        <h4>Análisis</h4>
        <p>
            ${resultado.analisis.criterio}
        </p>
        <p>
            Nodos recorridos:
            ${resultado.analisis.nodos_recorridos}
        </p>
        <p>
            Riesgo promedio:
            ${resultado.analisis.riesgo_promedio}
        </p>
        <p>
            Confianza promedio:
            ${resultado.analisis.confianza_promedio}
        </p>
        <hr>
        <h4>Parámetros</h4>
        <p>
            λ confianza:
            ${resultado.parametros.lambda_confianza}
        </p>
        <p>
            λ riesgo:
            ${resultado.parametros.lambda_riesgo}
        </p>

    `;
}


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
        editor.nodoSeleccionado = null;
        editor.origenArista = null;
        editor.rutaActual = [];
        limpiarResaltado();
        cambiarModo("seleccionar");

    });

document
    .getElementById("ejecutarDijkstra")
    .addEventListener(
    "click",

    async()=>{

        const origen =
        document.getElementById(
            "origenDijkstra"
        ).value;

        const destino =
        document.getElementById(
            "destinoDijkstra"
        ).value;

        const lambdaConfianza =
        Number(
            document.getElementById(
                "lambdaConfianza"
            ).value
        );

        const lambdaRiesgo =
        Number(
            document.getElementById(
                "lambdaRiesgo"
            ).value
        );

        const resultado =
        await ejecutarDijkstra(
            origen,
            destino,
            lambdaConfianza,
            lambdaRiesgo
        );

        console.log(resultado);

        await animarTimeline(
            resultado.timeline
        );

        resaltarRuta(
            resultado.ruta
        );

        mostrarResultado(
            resultado
        );
    });

document
    .getElementById("limpiarRuta")
    .addEventListener(
        "click",
        ()=>{

            limpiarResaltado();

            document.getElementById(
                "resultadoDijkstra"
            ).innerHTML="";

        }
    );

