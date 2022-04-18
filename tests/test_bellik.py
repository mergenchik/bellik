import os
import tempfile

import pytest

from bellik import create_app


@pytest.fixture
def client():
	app = create_app()

	with app.test_client() as client:
		yield client


def test_hello_world(client):
	rv = client.get('/hello')
	assert b'Hello' in rv.data
