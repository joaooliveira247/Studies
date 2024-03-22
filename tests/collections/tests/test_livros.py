from my_collections.livros import consultar_livros
from unittest.mock import patch


def test_consultar_livros_retorna_formato_string() -> None:
    result: str = consultar_livros("Agatha Christie")
    assert isinstance(result, str) is True


def test_consultar_livros_chama_preparar_dados_para_uma_vez_e_com_os_mesmos_parametros_de_consultar_livros():
    with patch("my_collections.livros.preparar_dados_para_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")


def test_consultar_livros_chama_obter_url_usando_parametro_retorno_preparar_dados_requisicao():
    with patch(
        "my_collections.livros.preparar_dados_para_requisicao"
    ) as duble_preparar:
        dados = {"author": "Agatha Christie"}
        duble_preparar.return_value = dados
        with patch("my_collections.livros.obter_url") as duble_obter_url:
            consultar_livros("Agatha Christie")
            duble_obter_url.assert_called_once_with("https://buscador", dados)
