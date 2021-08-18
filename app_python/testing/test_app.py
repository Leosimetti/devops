import time
from datetime import datetime

import pytest
import pytz
from flask.testing import FlaskClient

from app_python.src import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_app(client: FlaskClient):
    for _ in range(3):  # The loop is used to simulate a page refresh
        res = client.get("/")
        assert res.status_code == 200

        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        expected_time = moscow_time.strftime("%H:%M:%S")
        encoded_time = f"It is currently {expected_time} in Moscow".encode()

        assert encoded_time in res.data
        assert b"Vitaliy Korbashov" in res.data

        time.sleep(0.5)
