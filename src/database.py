import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "instance" / "tarefae.db"


def get_db_connection(db_path=DATABASE_PATH):
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(db_path=DATABASE_PATH):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    connection = get_db_connection(db_path)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL
                CHECK(length(trim(titulo)) > 0),
            descricao TEXT,
            prioridade TEXT NOT NULL DEFAULT 'media'
                CHECK(prioridade IN ('baixa', 'media', 'alta')),
            status TEXT NOT NULL DEFAULT 'pendente'
                CHECK(status IN ('pendente', 'concluida')),
            data_criacao TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            data_vencimento TEXT
        )
    """)

    connection.commit()
    connection.close()