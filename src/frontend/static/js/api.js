// Rutas por las que se crean para manejar la info con el backend. Cada función tiene en su titulo lo que hace
export async function obtenerGrafo() {

    const response = await fetch("/grafo");

    if (!response.ok) {
        throw new Error("No fue posible obtener el grafo.");
    }

    return await response.json();
}

export async function crearNodo(nodo){

    const response = await fetch(

        "/api/nodos",

        {

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(nodo)

        }

    );

    if(!response.ok){

        throw new Error(

            "No se pudo crear el nodo."

        );

    }

    return await response.json();

}

export async function eliminarNodo(id){

    const response = await fetch(

        "/api/nodos/"+id,

        {

            method:"DELETE"

        }

    );

    if(!response.ok){

        throw new Error("No se pudo eliminar.");

    }

}

export async function crearArista(arista){

    const response = await fetch(

        "/api/aristas",

        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(arista)
        }

    );

    if(!response.ok){

        throw new Error(
            "No fue posible crear la arista."
        );

    }

    return await response.json();

}

export async function eliminarArista(inicio, fin){

    const response = await fetch(

        "/api/aristas",

        {

            method:"DELETE",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                inicio:inicio,

                fin:fin

            })

        }

    );

    if(!response.ok){

        throw new Error(

            "No fue posible eliminar la arista."

        );

    }

}

export async function reiniciarGrafo(){

    const response = await fetch(

        "/api/grafo/reiniciar",

        {

            method:"POST"

        }

    );

    if(!response.ok){

        throw new Error("No fue posible reiniciar el grafo.");

    }

    return await response.json();

}