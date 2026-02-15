import requests

def test_get_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "completed" in data
