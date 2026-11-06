from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return """
            <h1>Bem-vindo ao Tarefaê!</h1>
            <p>Seu gerenciador de tarefas está sendo desenvolvido.</p>
        """

    return app


app = create_app()