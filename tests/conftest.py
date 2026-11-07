import pytest

from src.app import create_app


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "test_tarefae.db"

    app = create_app({
        "TESTING": True,
	"SECRET_KEY": "chave-de-teste-nao-utilizar-em-producao",
        "DATABASE_PATH": database_path
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()