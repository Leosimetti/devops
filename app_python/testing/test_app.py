import datetime

import pytest
import pytz
from flask.testing import FlaskClient
from freezegun import freeze_time


def test_endpoints(client: FlaskClient):
    # The available endpoints are accessed
    for endpoint in ["/", "/time"]:
        res = client.get(endpoint)
        # A positive reply is expected
        assert res.status_code == 200


@pytest.mark.parametrize(
    "interval",
    [
        datetime.timedelta(minutes=5),
        datetime.timedelta(days=50, minutes=40),
        datetime.timedelta(hours=30),
        datetime.timedelta(seconds=33),
    ],
)
def test_time(client: FlaskClient, interval):
    # Accessing the endpoint specifically responsible for providing time
    with freeze_time(datetime.datetime.now() + interval):
        for _ in range(3):  # The loop is used to simulate a page refresh
            res = client.get("/time")

            # The time is successfully retrieved
            assert res.status_code == 200

            moscow_time = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
            expected_time = moscow_time.strftime("%H:%M:%S")
            encoded_time = f"{expected_time}".encode()

            # The time corresponds to the actual time
            assert encoded_time in res.data


def test_name(client: FlaskClient):
    # Checking the content of the main page
    res = client.get("/")
    assert res.status_code == 200
    assert b"Vitaliy Korbashov" in res.data
