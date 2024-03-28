from __future__ import annotations
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode
import json
import logging
import os
from math import ceil


def consultar_livros(author: str) -> str:
    dados = preparar_dados_para_requisicao(author)
    url = obter_url("https://buscador", dados)
    ret = executar_request(url)
    return ret


def preparar_dados_para_requisicao(author): ...


def obter_url(url, dados): ...


def executar_request(url: str):
    try:
        with urlopen(url, timeout=10) as response:
            result = response.read().decode("utf-8")
    except HTTPError as e:
        logging.exception(f"Error ({e}) to acess url: {url}")
    else:
        return result


def write_archive(path: str, content: str):
    dir_ = os.path.dirname(path)
    try:
        os.makedirs(dir_)
    except OSError:
        logging.exception(f"Permission Error at {dir}")

    try:
        with open(path, "w") as fp:
            fp.write(content)
    except OSError as e:
        logging.exception(f"Permission Error at {dir}")


class Consulta:
    def __init__(self, author: str, title: str, livre: str) -> None:
        self._author = author
        self._title = title
        self._livre = livre
        self._page = 0
        self._data_from_request: dict | None = None
        self._url = "https://buscarlivros"

    @property
    def data_from_request(self) -> dict:
        if not self._data_from_request:
            self._data_from_request = {}
            if self._livre:
                self._data_from_request = {"q": self._livre}
            else:
                if self._author:
                    self._data_from_request["author"] = self._author
                if self._title:
                    self._data_from_request["title"] = self._title

        return self._data_from_request

    @property
    def next(self):
        data_from_request = self._data_from_request
        self._page += 1
        data_from_request["page"] = self._page
        req = Request(self._url, data_from_request)
        if req.data:
            return f"{req.full_url}{'?'}{urlencode(req.data)}"


class Response:
    docs_per_page: int = 50

    def __init__(self, content: str) -> None:
        self._content = content
        self._data = None

    @property
    def content(self):
        return self._content

    @property
    def data(self):
        if not self._data:
            try:
                j = json.loads(self.content)
            except TypeError as e:
                logging.exception(f"wrong type request :{self.content}")
            except json.JSONDecodeError as e:
                logging.exception(f"wrong JSON request: {self.content}")
            else:
                self._data = j
        return self._data

    @property
    def docs(self):
        return self.data.get("docs", [])

    @property
    def pagination_total(self):
        if len(self.docs):
            return ceil(self.data.get("num_docs", 0) / self.docs_per_page)
        return 0


def download_books(author, title, livre):
    consulta = Consulta(author, title, livre)
    consulta.data_from_request
    total_pages = 1
    while True:
        result = executar_request(consulta.next)
        if consulta._page == 1:
            total_pages = 2
        if consulta._page == total_pages:
            break
