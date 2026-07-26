import { crearNodo, eliminarNodo, crearArista, eliminarArista} from "./api.js";
import { editor } from "./editor.js";

//Función que dibuja el grafo base
export function dibujarGrafo(data){

    let elementos = [];

    data.nodos.forEach(nodo => {

        elementos.push({

            data:{
                id:nodo.id,
                label:nodo.etiqueta,
                estado:nodo.estado
            },

            position:{
                x:nodo.x,
                y:nodo.y
            }

        });

    });

    data.aristas.forEach(arista=>{

        elementos.push({

            data:{
                source:arista.inicio,
                target:arista.fin,
                label:arista.peso
            }

        });

    });

    editor.cy = cytoscape({

        container:document.getElementById("cy"),

        elements:elementos,

        style:[

            { selector:"node", style:{
                    "background-color":"#1F4E79",
                    "border-width":1,
                    "border-color":"#171A21",
                    "shape":"round-rectangle",
                label:"data(label)",
                color:"white",
                    "font-family":"IBM Plex Mono",
                    "font-size":11,
                    "text-valign":"center",
                    "text-halign":"center"
                }
            },
            { selector:"edge", style:{
                    "line-color":"#9BA5AF",
                    "target-arrow-color":"#9BA5AF",
                label:"data(label)",
                    "font-family":"IBM Plex Mono",
                    "font-size":10,
                width:2,
                    "curve-style":"bezier",
                    "target-arrow-shape":"triangle"
                }
            },
            {
                selector:".seleccionado",
                style:{
                    "background-color":"#B7791F",
                    "border-width":3,
                    "border-color":"#171A21"    
                }
            },
            {
                selector:"node.ruta",
                style:{
                    "background-color":"#2F6F4E",  
                    "border-width":2,
                    "border-color":"#173c5c"
                }
            },
            {
                selector:"edge.ruta",
                style:{
                    "line-color":"#2F6F4E",
                    "target-arrow-color":"#2F6F4E",
                    "width":4 
                }
            }
        ],

        layout:{
            name:"preset"
        }

    });

    //Función que crea un nodo al hacer clic
    editor.cy.on("tap", async function(event){

    if(event.target !== editor.cy){
        return;
    }

    switch(editor.modo){

        case "crear_nodo":

            await crearNodoEnPosicion(
                event.position
            );
            break;

    }

});
    // Función que ajusta las acciones por toque en cada nodo al estar en el modo necesario
    editor.cy.on("tap", "node", async function(event){

    const nodo = event.target;

    switch(editor.modo){

        // Elimina el nodo
        case "eliminar":
            editor.nodoSeleccionado = nodo;
            eliminarNodoSeleccionado();
            break;
        
        // Selecciona el nodo
        case "seleccionar":
            seleccionarNodo(nodo);
            mostrarInformacionNodo(nodo);
            break;

        // Crea la arista del nodo inicial al final
        case "crear_arista":
            crearAristaDesdeNodo(nodo);
            break;
    }
});

    // Función que elimina las arista al darle clic
    editor.cy.on("tap","edge", async function(event){

        if(editor.modo!="eliminar"){
            return;
        }
        const arista = event.target;

        const confirmar = confirm(
            "¿Eliminar esta arista?"
        );

        if(!confirmar){
            return;
        }

        await eliminarArista(
            arista.source().id(),
            arista.target().id()
        );
        arista.remove();
    }
);

}

export function obtenerCy(){
    return editor.cy;
}

// Crea el nodo en el lugar y pide la información necesaria
async function crearNodoEnPosicion(posicion){

    const id = prompt("ID del nodo");

    if(!id){
        return;
    }

    const etiqueta = prompt(
        "Etiqueta"
    ) || id;

    const confianza = Number(
        prompt(
            "Nivel de confianza",
            "1"
        )
    );

    const nodo = {

        id:id,
        etiqueta:etiqueta,
        estado:"Seguro",
        nivel_confianza:confianza,
        x:posicion.x,
        y:posicion.y

    };

    try{
        const creado = await crearNodo(nodo);
        agregarNodoVisual(creado);
    }
    catch(error){
        alert(error);
    }
}

// Posiciona el nodo en el lugar
export function agregarNodoVisual(nodo){

    editor.cy.add({
        group:"nodes",
        data:{
            id:nodo.id,
            label:nodo.etiqueta,
            estado:nodo.estado
        },
        position:{
            x:nodo.x,
            y:nodo.y
        }
    });
}

// Selecciona el nodo
function seleccionarNodo(nodo){

    if(editor.nodoSeleccionado){
        editor.nodoSeleccionado.removeClass("seleccionado");
    }
    editor.nodoSeleccionado = nodo;
    editor.nodoSeleccionado.addClass("seleccionado");
}

// Borra el nodo seleccionado
async function eliminarNodoSeleccionado(){
    if(!editor.nodoSeleccionado){
        return;
    }

    const confirmar = confirm(
        "¿Eliminar este nodo?"
    );

    if(!confirmar){
        return;
    }

    await eliminarNodo(
        editor.nodoSeleccionado.id()
    );

    editor.nodoSeleccionado.remove();
    editor.nodoSeleccionado = null;

}

// Crea la arista con inicio y fin seleccionados
async function crearAristaDesdeNodo(nodo){

    if(editor.origenArista == null){

        editor.origenArista = nodo;

        nodo.addClass("seleccionado");
        return;
    }

    if(editor.origenArista.id() == nodo.id()){

        editor.origenArista.removeClass("seleccionado");

        editor.origenArista = null;
        return;
    }

    const peso = Number(
        prompt("Peso")
    );

    const riesgo = Number(
        prompt("Riesgo",0)
    );

    const arista = {

        inicio:editor.origenArista.id(),
        fin:nodo.id(),
        peso:peso,
        riesgo:riesgo
    };

    try{

        const creada = await crearArista(arista);
        agregarAristaVisual(creada);
    }

    catch(error){
        alert(error.message);
    }

    editor.origenArista.removeClass("seleccionado");
    editor.origenArista = null;

}

// Crea la arista visualmente
function agregarAristaVisual(arista){

    editor.cy.add({

        group:"edges",
        data:{
            source:arista.inicio,
            target:arista.fin,
            label:arista.peso
        }

    });
}

// Actualiza el grafo al base. Borra todos los cambios
export function actualizarGrafo(data){

    editor.cy.elements().remove();

    const elementos = [];

    data.nodos.forEach(nodo=>{

        elementos.push({
            group:"nodes",
            data:{
                id:nodo.id,
                label:nodo.etiqueta,
                estado:nodo.estado
            },
            position:{
                x:nodo.x,
                y:nodo.y
            }
        });
    });

    data.aristas.forEach(arista=>{
        elementos.push({
            group:"edges",
            data:{
                source:arista.inicio,
                target:arista.fin,
                label:arista.peso
            }
        });
    });

    editor.cy.add(elementos);
}

// Utiliza dijkstra para resaltar la ruta más optima
export function resaltarRuta(ruta){

    editor.cy.elements().removeClass("ruta");

    for(let i=0;i<ruta.length-1;i++){

        const origen = ruta[i];
        const destino = ruta[i+1];

        const arista = editor.cy.edges().filter(edge=>{
            return (
                edge.source().id()==origen &&
                edge.target().id()==destino
            );
        });

        arista.addClass("ruta");

    }

    ruta.forEach(id=>{

        editor.cy.getElementById(id)
            .addClass("ruta");
    });
}

export function limpiarResaltado(){

    editor.cy.elements()
        .removeClass("ruta")
        .removeClass("seleccionado");

}

function mostrarInformacionNodo(nodo){


    document
    .getElementById("sinSeleccion")
    .style.display="none";


    document
    .getElementById("infoNodo")
    .style.display="block";


    document
    .getElementById("nodoId")
    .textContent=nodo.id();


    document
    .getElementById("nodoEtiqueta")
    .textContent=nodo.data("label");


    document
    .getElementById("nodoEstado")
    .textContent=nodo.data("estado");


    document
    .getElementById("nodoConfianza")
    .textContent=nodo.data("confianza") ?? "N/A";


    const vecinos = nodo.neighborhood("node");


    document
    .getElementById("nodoConexiones")
    .textContent=vecinos.length;


    document
    .getElementById("nodoVecinos")
    .textContent=
        vecinos
        .map(n=>n.id())
        .join(", ");

}