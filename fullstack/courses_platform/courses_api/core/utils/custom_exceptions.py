from typing import Any

from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: Any, context: Any) -> Response:
    response = exception_handler(exc, context)

    if response is not None:
        if response.data.get("messages"):
            del response.data["messages"]

        if response.data.get("success") is None:
            response.data["success"] = False

    return response
