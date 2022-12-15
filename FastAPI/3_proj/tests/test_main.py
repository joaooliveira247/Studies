import httpx


BASE_URL_API: str = "http://localhost:8000/api/v1/courses/"


def test_read_itens() -> None:
    response: httpx.Response = httpx.get(BASE_URL_API)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_read_one_item() -> None:
    _all_itens: httpx.Response = httpx.get(BASE_URL_API)
    response: httpx.Response = httpx.get(
        BASE_URL_API + str(_all_itens.json()[0]["id"])
        )
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_read_one_item_wrong_id() -> None:
    _all_itens: httpx.Response = httpx.get(BASE_URL_API)
    response: httpx.Response = httpx.get(
        BASE_URL_API + str(len(_all_itens.json()) + 1)
    )
    assert response.status_code == 404


def test_create_item() -> None:
    response: httpx.Response = httpx.post(
        BASE_URL_API, json={"title": "Teste", "classes": 999, "time": 999}
    )

    httpx.delete(BASE_URL_API + str(response.json()["id"]))

    assert response.status_code == 201
    assert len(response.json()) > 1


def test_update_item() -> None:
    _create: httpx.Response = httpx.post(
        BASE_URL_API, json={"title": "Teste", "classes": 999, "time": 999}
    )

    _update_json: dict[str, str | int] = {
        "title": "Teste Update", "classes": 666, "time": 666
    }
    response: httpx.Response = httpx.put(
        BASE_URL_API + str(_create.json()["id"]), json=_update_json
    )

    _update_json["id"] = response.json()["id"]

    httpx.delete(BASE_URL_API + str(response.json()["id"]))

    assert response.status_code == 202
    assert response.json() == _update_json


def test_update_item_with_wrong_id() -> None:
    _all_itens: httpx.Response = httpx.get(BASE_URL_API)
    response: httpx.Response = httpx.put(
        BASE_URL_API + str(len(_all_itens.json()) + 1),
        json={"title": "Teste", "classes": 999, "time": 999}
        )
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found."}


def test_delete_item() -> None:
    create: httpx.Response = httpx.post(
        BASE_URL_API, json={"title": "Teste", "classes": 999, "time": 999}
    )
    response: httpx.Response = httpx.delete(
        BASE_URL_API + str(create.json()["id"])
        )
    assert response.status_code == 204
