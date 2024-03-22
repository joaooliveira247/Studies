from __future__ import annotations


def consultar_livros(author: str) -> str:
    dados = preparar_dados_para_requisicao(author)
    obter_url("https://buscador", dados)
    return ""


def preparar_dados_para_requisicao(author): ...


def obter_url(url, dados): ...
