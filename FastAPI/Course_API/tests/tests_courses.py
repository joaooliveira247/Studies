import httpx
from course_api.models.course_model import CourseModel

BASE_API_URL: str = "http://localhost:8000/api/v1/courses/"
BASE_HEADER: dict[str, str] = {
    "content-type": "application/json",
    "accept": "application/json",
}


def test_get_course() -> None:
    response: httpx.Response = httpx.get(BASE_API_URL, params=BASE_HEADER)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_course() -> None:
    __course: dict[str, str | int] = {
        "title": "Course Test",
        "classes": 333,
        "time": 333,
    }
    response: httpx.Response = httpx.post(
        BASE_API_URL, headers=BASE_HEADER, json=__course
    )
    __course["id"] = response.json()["id"]
    httpx.delete(BASE_API_URL + str(response.json()["id"]))
    assert response.status_code == 201
    assert response.json() == __course


def test_get_one_course() -> None:
    response: httpx.Response = httpx.get(
        BASE_API_URL + "1", params=BASE_HEADER
    )
    assert response.status_code == 200
    assert type(response.json()) == dict


def test_update_item() -> None:
    _create: httpx.Response = httpx.post(
        BASE_API_URL, json={"title": "Teste", "classes": 999, "time": 999}
    )

    _update_json: dict[str, str | int] = {
        "title": "Teste Update",
        "classes": 666,
        "time": 666,
    }
    response: httpx.Response = httpx.put(
        BASE_API_URL + str(_create.json()["id"]), json=_update_json
    )

    _update_json["id"] = response.json()["id"]

    httpx.delete(BASE_API_URL + str(response.json()["id"]))

    assert response.status_code == 202
    assert response.json() == _update_json


# def test_update_item_with_wrong_id() -> None:
#     _all_itens: httpx.Response = httpx.get(BASE_API_URL)
#     response: httpx.Response = httpx.put(
#         BASE_API_URL + str(len(_all_itens.json()) + 1),
#         json={"title": "Teste", "classes": 999, "time": 999},
#     )
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Course not found."}


def test_delete_item() -> None:
    create: httpx.Response = httpx.post(
        BASE_API_URL, json={"title": "Teste", "classes": 999, "time": 999}
    )
    response: httpx.Response = httpx.delete(
        BASE_API_URL + str(create.json()["id"])
    )
    assert response.status_code == 204
