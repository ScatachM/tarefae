from flask import Flask

from src.database import init_db, DATABASE_PATH
from src.routes.tarefas import tarefas_bp


def create_app():
    app = Flask(__name__)

    app.config["DATABASE_PATH"] = DATABASE_PATH

    init_db(app.config["DATABASE_PATH"])

    app.register_blueprint(tarefas_bp)

    return app


app = create_app()