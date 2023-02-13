from fastapi.testclient import TestClient
from main import app
import pytest
import requests
from src.enums.global_enums import GlobalErrorMessages

client = TestClient(app)


def test_read_main():
	response = client.get('/')
	assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
	assert 'Hello, world!' in response.json()


def test_read_model():
	response = client.get("/models/lenet")
	received_posts = response.json()
	print(received_posts)
	assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
	assert 'LeCNN all the images' in response.text
	assert len(received_posts) == 2, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value