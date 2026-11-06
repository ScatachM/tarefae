from datetime import datetime, date

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

PRIORIDADES_VALIDAS = ("baixa", "media", "alta")
STATUS_VALIDOS = ("pendente", "concluida")


def validar_data(data):
    if not data:
        return True

    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


@tarefas_bp.route("/", methods=["GET", "POST"])
def index():

    erro = None

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        prioridade = request.form.get("prioridade", "media")
        status = request.form.get("status", "pendente")
        data_vencimento = request.form.get(
            "data_vencimento", ""
        ).strip()

        if not titulo:
            erro = "O título da tarefa é obrigatório."

        elif prioridade not in PRIORIDADES_VALIDAS:
            erro = "A prioridade selecionada é inválida."

        elif status not in STATUS_VALIDOS:
            erro = "O status selecionado é inválido."

        elif not validar_data(data_vencimento):
            erro = "A data de vencimento é inválida."

        else:
            conn = get_db_connection(
                current_app.config["DATABASE_PATH"]
            )

            try:
                conn.execute(
                    """
                    INSERT INTO tarefas (
                        titulo,
                        descricao,
                        prioridade,
                        status,
                        data_vencimento
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        titulo,
                        descricao or None,
                        prioridade,
                        status,
                        data_vencimento or None
                    )
                )

                conn.commit()

            finally:
                conn.close()

            return redirect(url_for("tarefas.index"))

    # Recupera os filtros enviados pela URL
    status_filtro = request.args.get("status", "").strip()
    prioridade_filtro = request.args.get("prioridade", "").strip()

    # Ignora filtros com valores inválidos
    if status_filtro not in STATUS_VALIDOS:
        status_filtro = ""

    if prioridade_filtro not in PRIORIDADES_VALIDAS:
        prioridade_filtro = ""

    # Monta a consulta conforme os filtros selecionados
    condicoes = []
    parametros = []

    if status_filtro:
        condicoes.append("status = ?")
        parametros.append(status_filtro)

    if prioridade_filtro:
        condicoes.append("prioridade = ?")
        parametros.append(prioridade_filtro)

    consulta = "SELECT * FROM tarefas"

    if condicoes:
        consulta += " WHERE " + " AND ".join(condicoes)

    consulta += " ORDER BY id DESC"

    conn = get_db_connection(
        current_app.config["DATABASE_PATH"]
    )

    try:
        tarefas = conn.execute(
            consulta,
            parametros
        ).fetchall()

    finally:
        conn.close()

    hoje = date.today().isoformat()

    return render_template(
        "index.html",
        tarefas=tarefas,
        erro=erro,
        status_filtro=status_filtro,
        prioridade_filtro=prioridade_filtro,
        hoje=hoje
    )


@tarefas_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    erro = None

    conn = get_db_connection(
        current_app.config["DATABASE_PATH"]
    )

    try:
        tarefa = conn.execute(
            """
            SELECT * FROM tarefas
            WHERE id = ?
            """,
            (id,)
        ).fetchone()

        if tarefa is None:
            return redirect(url_for("tarefas.index"))

        if request.method == "POST":
            titulo = request.form.get("titulo", "").strip()
            descricao = request.form.get("descricao", "").strip()
            prioridade = request.form.get("prioridade", "media")
            status = request.form.get("status", "pendente")
            data_vencimento = request.form.get(
                "data_vencimento", ""
            ).strip()

            if not titulo:
                erro = "O título da tarefa é obrigatório."

            elif prioridade not in PRIORIDADES_VALIDAS:
                erro = "A prioridade selecionada é inválida."

            elif status not in STATUS_VALIDOS:
                erro = "O status selecionado é inválido."

            elif not validar_data(data_vencimento):
                erro = "A data de vencimento é inválida."

            else:
                conn.execute(
                    """
                    UPDATE tarefas
                    SET titulo = ?,
                        descricao = ?,
                        prioridade = ?,
                        status = ?,
                        data_vencimento = ?
                    WHERE id = ?
                    """,
                    (
                        titulo,
                        descricao or None,
                        prioridade,
                        status,
                        data_vencimento or None,
                        id
                    )
                )

                conn.commit()

                return redirect(url_for("tarefas.index"))

    finally:
        conn.close()

    return render_template(
        "editar.html",
        tarefa=tarefa,
        erro=erro
    )


@tarefas_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):

    conn = get_db_connection(
        current_app.config["DATABASE_PATH"]
    )

    try:
        conn.execute(
            """
            DELETE FROM tarefas
            WHERE id = ?
            """,
            (id,)
        )

        conn.commit()

    finally:
        conn.close()

    return redirect(url_for("tarefas.index"))