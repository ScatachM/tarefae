import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from src.database import init_db, DATABASE_PATH
from src.routes.tarefas import tarefas_bp


csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["DATABASE_PATH"] = DATABASE_PATH

    if test_config:
        app.config.update(test_config)

    if not app.config["SECRET_KEY"]:
        raise RuntimeError("A variável SECRET_KEY não foi configurada.")

    csrf.init_app(app)

    init_db(app.config["DATABASE_PATH"])

    app.register_blueprint(tarefas_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)