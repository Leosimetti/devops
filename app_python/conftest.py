import pytest
from src import create_app


@pytest.fixture(scope="function")
def client():
    app = create_app()

    with app.test_client() as client:
        yield client
