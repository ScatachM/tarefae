from flask import Flask

from src.database import init_db, DATABASE_PATH
from src.routes.tarefas import tarefas_bp


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["DATABASE_PATH"] = DATABASE_PATH

    if test_config:
        app.config.update(test_config)

    init_db(app.config["DATABASE_PATH"])

    app.register_blueprint(tarefas_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)