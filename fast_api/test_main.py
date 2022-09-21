from fastapi.testclient import TestClient
from main import app
import pytest
import requests


client = TestClient(app)


def test_read_main():
	response = client.get('/')
	assert response.status_code == 200
	assert 'Hello, world!' in response.json()


def test_read_model():
	response = client.get("/models/lenet")
	assert response.status_code == 200
	assert 'LeCNN all the images' in response.text
