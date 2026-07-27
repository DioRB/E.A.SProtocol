// Interfaz que relaciona todos los elementos graficos de la página con las funciones adjudicadas
import { reiniciarGrafo, ejecutarDijkstra, obtenerNodos, descifrarTexto} from "./api.js";
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

    let bloqueCifrado = "";

    if(resultado.mensaje_cifrado){

        bloqueCifrado = `
            <hr>
            <h4>Mensaje cifrado</h4>
            <p>
                <strong>Algoritmo:</strong>
                ${resultado.mensaje_cifrado.algoritmo}
            </p>
            <p>
                <strong>Cifrado:</strong>
                ${resultado.mensaje_cifrado.cifrado}
            </p>
            <button id="btnDescifrarResultado" class="btn-secondary">
                Descifrar
            </button>
            <textarea
                id="textoDescifradoResultado"
                rows="3"
                readonly
                style="display:none; margin-top:8px"></textarea>
        `;

    } else if(resultado.cifrado_error){

        bloqueCifrado = `
            <hr>
            <h4>Mensaje cifrado</h4>
            <p class="error-cif">
                ${resultado.cifrado_error}
            </p>
        `;

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
        ${bloqueCifrado}

    `;

    const btnDescifrar =
        document.getElementById("btnDescifrarResultado");

    if(btnDescifrar){

        btnDescifrar.addEventListener("click", async () => {

            const salida =
                document.getElementById("textoDescifradoResultado");

            try{

                const r = await descifrarTexto(
                    resultado.mensaje_cifrado.algoritmo,
                    resultado.mensaje_cifrado.cifrado,
                    resultado.mensaje_cifrado.clave_usada
                );

                salida.value = r.texto;
                salida.style.display = "block";

            } catch(error){

                salida.value = "Error: " + error.message;
                salida.style.display = "block";

            }

        });

    }
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

        // Si está activo mandamos mensaje y clave
        let mensaje = null;
        let clave_cifrado = null;

        const checkboxCifrado =
            document.getElementById("activarCifrado");

        if (checkboxCifrado.checked) {
            mensaje =
                document.getElementById("mensajeDijkstra").value;
            clave_cifrado = leerClaveCifradoRuta();
        }

        const resultado =
        await ejecutarDijkstra(
            origen,
            destino,
            lambdaConfianza,
            lambdaRiesgo,
            mensaje,
            clave_cifrado
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


// ===== CIFRADO EN LA RUTA DIJKSTRA =====

// Dibuja los inputs de la clave dependiendo del algoritmo
// Si es afin, a y b, para hill, n y las celdas de la matriz
function dibujarInputsClave(contenedor, algoritmo){

    contenedor.innerHTML = "";

    if(algoritmo === "afin"){

        contenedor.innerHTML = `
            <label for="aRuta">a</label>
            <input type="number" id="aRuta" min="1" max="25" value="5">

            <label for="bRuta">b</label>
            <input type="number" id="bRuta" min="0" max="25" value="8">
        `;

        return;
    }

    if(algoritmo === "hill"){

        contenedor.innerHTML = `
            <label for="nRuta">Tamaño n</label>
            <input type="number" id="nRuta" min="2" max="5" value="2">
            <div id="grillaMatrizRuta"></div>
        `;

        const inputN =
            document.getElementById("nRuta");

        const pintarGrilla = () => {

            const n = Number(inputN.value);
            const grilla =
                document.getElementById("grillaMatrizRuta");

            grilla.innerHTML = "";

            if(n < 2 || n > 5){
                return;
            }

            // Una tabla simple para que se vean las filas y columnas.
            const tabla = document.createElement("table");

            for(let i = 0; i < n; i++){

                const fila = document.createElement("tr");

                for(let j = 0; j < n; j++){

                    const celda = document.createElement("td");
                    const input =
                        document.createElement("input");

                    input.type = "number";
                    input.value = "1";
                    input.id = "celdaRuta_" + i + "_" + j;

                    celda.appendChild(input);
                    fila.appendChild(celda);

                }

                tabla.appendChild(fila);

            }

            grilla.appendChild(tabla);

        };

        inputN.addEventListener("change", pintarGrilla);
        pintarGrilla();

    }

}

// Lee los inputs actuales del bloque y devuelve el objeto clave listo para enviar.
function leerClaveCifradoRuta(){

    const algoritmo =
        document.getElementById("algoritmoCifradoRuta").value;

    if(algoritmo === "afin"){

        return {
            algoritmo: "afin",
            a: Number(document.getElementById("aRuta").value),
            b: Number(document.getElementById("bRuta").value)
        };

    }

    if(algoritmo === "hill"){

        const n = Number(document.getElementById("nRuta").value);
        const matriz = [];

        for(let i = 0; i < n; i++){

            const fila = [];

            for(let j = 0; j < n; j++){

                const input =
                    document.getElementById("celdaRuta_" + i + "_" + j);

                fila.push(Number(input.value));

            }

            matriz.push(fila);

        }

        return {
            algoritmo: "hill",
            n: n,
            matriz: matriz
        };

    }

    return null;

}

// Mostrar o no el bloque cuando se marca el checkbox del cifrado
document
    .getElementById("activarCifrado")
    .addEventListener("change", () => {

        const bloque =
            document.getElementById("bloqueCifradoRuta");

        if(document.getElementById("activarCifrado").checked){
            bloque.style.display = "block";
        } else {
            bloque.style.display = "none";
        }

    });

// Cambiar el algoritmo limpia los inputs y dibuja nuevos
document
    .getElementById("algoritmoCifradoRuta")
    .addEventListener("change", () => {

        const algoritmo =
            document.getElementById("algoritmoCifradoRuta").value;

        const contenedor =
            document.getElementById("inputsClaveRuta");

        dibujarInputsClave(contenedor, algoritmo);

    });

// Inputs por defecto al cargar la página
dibujarInputsClave(
    document.getElementById("inputsClaveRuta"),
    document.getElementById("algoritmoCifradoRuta").value
);

