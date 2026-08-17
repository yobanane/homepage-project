def test_index_returns_hello_world(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello world"}


def test_healtz_returns_ok(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404
