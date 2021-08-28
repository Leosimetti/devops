import time
from datetime import datetime

import pytz
from flask.testing import FlaskClient


def test_endpoints(client: FlaskClient):
    for endpoint in ["/", "/time"]:
        res = client.get(endpoint)
        assert res.status_code == 200


def test_time(client: FlaskClient):
    # Accessing the endpoint responsible for providing time
    for _ in range(5):  # The loop is used to simulate a page refresh
        res = client.get("/time")
        assert res.status_code == 200

        moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
        expected_time = moscow_time.strftime("%H:%M:%S")
        encoded_time = f"{expected_time}".encode()

        assert encoded_time in res.data
        time.sleep(0.5)


def test_name(client: FlaskClient):
    # Checking the content of the main page
    res = client.get("/")
    assert res.status_code == 200
    assert b"Vitaliy Korbashov" in res.data
