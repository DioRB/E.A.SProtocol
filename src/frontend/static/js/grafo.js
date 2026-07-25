fetch("/grafo")
    .then(response => response.json())
    .then(data => {

        let elementos = [];

        // Crear nodos
        data.nodos.forEach(nodo => {

            elementos.push({

                data: {
                    id: nodo.id,
                    label: nodo.etiqueta,
                    estado: nodo.estado
                },

                position: {
                    x: nodo.x,
                    y: nodo.y
                }

            });

        });

        // Crear aristas
        data.aristas.forEach(arista => {

            elementos.push({

                data: {
                    source: arista.inicio,
                    target: arista.fin,
                    label: arista.peso
                }

            });

        });

        cytoscape({

            container: document.getElementById("cy"),

            elements: elementos,

            style: [

                {

                    selector: "node",

                    style: {

                        "label": "data(label)",
                        "background-color": "#2E86DE",
                        "color": "white",
                        "text-valign": "center",
                        "text-halign": "center"

                    }

                },

                {

                    selector: "edge",

                    style: {

                        "label": "data(label)",
                        "width": 3,
                        "curve-style": "bezier",
                        "target-arrow-shape": "triangle"

                    }

                }

            ],

            layout: {

                name: "preset"

            }

        });

    });