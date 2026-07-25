from flask import Flask

def crear_app():

    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    from .rutas import registrar_rutas

    registrar_rutas(app)

    return app