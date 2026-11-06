from datetime import date, timedelta

import sqlite3


def obter_id_tarefa(app, titulo):
    conn = sqlite3.connect(app.config["DATABASE_PATH"])
    try:
        resultado = conn.execute(
            "SELECT id FROM tarefas WHERE titulo = ?",
            (titulo,)
        ).fetchone()
        return resultado[0]
    finally:
        conn.close()


def test_pagina_inicial_carrega(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Tarefa" in resposta.data


def test_cadastrar_tarefa(client):
    resposta = client.post(
        "/",
        data={
            "titulo": "Estudar Python",
            "descricao": "Praticar testes automatizados",
            "prioridade": "alta",
            "status": "pendente",
            "data_vencimento": ""
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Estudar Python" in resposta.data


def test_nao_cadastrar_tarefa_sem_titulo(client):
    resposta = client.post(
        "/",
        data={
            "titulo": "   ",
            "descricao": "Tarefa sem título",
            "prioridade": "media",
            "status": "pendente",
            "data_vencimento": ""
        }
    )

    assert resposta.status_code == 200
    assert "O título da tarefa é obrigatório.".encode() in resposta.data


def test_editar_tarefa(client, app):
    client.post(
        "/",
        data={
            "titulo": "Tarefa antiga",
            "descricao": "Descrição original",
            "prioridade": "media",
            "status": "pendente",
            "data_vencimento": ""
        }
    )

    tarefa_id = obter_id_tarefa(app, "Tarefa antiga")

    resposta = client.post(
        f"/editar/{tarefa_id}",
        data={
            "titulo": "Tarefa atualizada",
            "descricao": "Descrição modificada",
            "prioridade": "alta",
            "status": "concluida",
            "data_vencimento": ""
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Tarefa atualizada" in resposta.data
    assert b"Tarefa antiga" not in resposta.data


def test_excluir_tarefa(client, app):
    client.post(
        "/",
        data={
            "titulo": "Tarefa para excluir",
            "descricao": "",
            "prioridade": "baixa",
            "status": "pendente",
            "data_vencimento": ""
        }
    )

    tarefa_id = obter_id_tarefa(app, "Tarefa para excluir")

    resposta = client.post(
        f"/excluir/{tarefa_id}",
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Tarefa para excluir" not in resposta.data


def test_filtrar_tarefas_por_status(client):
    client.post(
        "/",
        data={
            "titulo": "Tarefa pendente",
            "prioridade": "media",
            "status": "pendente"
        }
    )

    client.post(
        "/",
        data={
            "titulo": "Tarefa concluida",
            "prioridade": "media",
            "status": "concluida"
        }
    )

    resposta = client.get("/?status=pendente")

    assert resposta.status_code == 200
    assert b"Tarefa pendente" in resposta.data
    assert b"Tarefa concluida" not in resposta.data


def test_filtrar_tarefas_por_prioridade(client):
    client.post(
        "/",
        data={
            "titulo": "Tarefa urgente",
            "prioridade": "alta",
            "status": "pendente"
        }
    )

    client.post(
        "/",
        data={
            "titulo": "Tarefa simples",
            "prioridade": "baixa",
            "status": "pendente"
        }
    )

    resposta = client.get("/?prioridade=alta")

    assert resposta.status_code == 200
    assert b"Tarefa urgente" in resposta.data
    assert b"Tarefa simples" not in resposta.data

def test_identificar_tarefa_atrasada(client):
    ontem = (date.today() - timedelta(days=1)).isoformat()

    client.post(
        "/",
        data={
            "titulo": "Tarefa atrasada",
            "prioridade": "alta",
            "status": "pendente",
            "data_vencimento": ontem
        }
    )

    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"atrasada" in resposta.data
    assert b"Tarefa atrasada" in resposta.data


def test_tarefa_com_data_futura_nao_esta_atrasada(client):
    amanha = (date.today() + timedelta(days=1)).isoformat()

    client.post(
        "/",
        data={
            "titulo": "Tarefa futura",
            "prioridade": "media",
            "status": "pendente",
            "data_vencimento": amanha
        }
    )

    resposta = client.get("/")

    assert resposta.status_code == 200

    assert b'class="no-prazo"' in resposta.data


def test_tarefa_concluida_nao_esta_atrasada(client):
    ontem = (date.today() - timedelta(days=1)).isoformat()

    client.post(
        "/",
        data={
            "titulo": "Tarefa concluida atrasada",
            "prioridade": "alta",
            "status": "concluida",
            "data_vencimento": ontem
        }
    )

    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Tarefa concluida atrasada" in resposta.data
    assert b'class="no-prazo"' in resposta.data