import pytest
import requests

pytestmark = pytest.mark.api


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_por_id():
    """
    Valida que se pueda consultar un post existente por ID.
    """

    response = requests.get(f"{BASE_URL}/posts/1")
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body
    assert "userId" in body


def test_crear_post():
    """
    Valida que se pueda crear un post mediante POST.
    """

    payload = {
        "title": "Proyecto QA Automation",
        "body": "Prueba de creación de recurso con Requests",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    body = response.json()

    assert response.status_code == 201
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


def test_eliminar_post():
    """
    Valida que se pueda eliminar un post mediante DELETE.
    """

    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200