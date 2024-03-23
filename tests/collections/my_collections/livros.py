from __future__ import annotations


def consultar_livros(author: str) -> str:
    dados = preparar_dados_para_requisicao(author)
    url = obter_url("https://buscador", dados)
    ret = executar_request(url)
    return ret


def preparar_dados_para_requisicao(author): ...


def obter_url(url, dados): ...


def executar_request(url: str): ...
