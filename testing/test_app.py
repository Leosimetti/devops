from datetime import datetime

import pytest
import pytz
from flask.testing import FlaskClient

from app_python import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_app(client: FlaskClient):
    res = client.get("/")
    assert res.status_code == 200

    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    expected_time = moscow_time.strftime("%H:%M:%S")

    assert f"It is currently {expected_time} in Moscow".encode() in res.data
    assert b"Vitaliy Korbashov" in res.data