from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    current_app
)

from src.database import get_db_connection


tarefas_bp = Blueprint("tarefas", __name__)


@tarefas_bp.route("/", methods=["GET", "POST"])
def index():

    erro = None

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()

        if not titulo:
            erro = "O título da tarefa é obrigatório."

        else:
            conn = get_db_connection(
                current_app.config["DATABASE_PATH"]
            )

            try:
                conn.execute(
                    """
                    INSERT INTO tarefas (titulo, descricao)
                    VALUES (?, ?)
                    """,
                    (titulo, descricao or None)
                )

                conn.commit()

            finally:
                conn.close()

            return redirect(url_for("tarefas.index"))

    conn = get_db_connection(
        current_app.config["DATABASE_PATH"]
    )

    try:
        tarefas = conn.execute(
            """
            SELECT * FROM tarefas
            ORDER BY id DESC
            """
        ).fetchall()

    finally:
        conn.close()

    return render_template(
        "index.html",
        tarefas=tarefas,
        erro=erro
    )