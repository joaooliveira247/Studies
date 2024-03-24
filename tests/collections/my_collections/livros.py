from __future__ import annotations
from urllib.request import urlopen
from urllib.error import HTTPError
import logging


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
