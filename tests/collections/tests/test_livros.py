from my_collections.livros import consultar_livros, executar_request
from unittest.mock import patch, MagicMock, mock_open
from unittest import skip
from urllib.error import HTTPError
import pytest


@skip("this test was skiped")
def test_consultar_livros_retorna_formato_string() -> None:
    result: str = consultar_livros("Agatha Christie")
    assert isinstance(result, str) is True


@skip("skiped")
def test_consultar_livros_chama_preparar_dados_para_uma_vez_e_com_os_mesmos_parametros_de_consultar_livros():
    with patch("my_collections.livros.preparar_dados_para_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")


@skip("skiped_2")
def test_consultar_livros_chama_obter_url_usando_parametro_retorno_preparar_dados_requisicao():
    with patch(
        "my_collections.livros.preparar_dados_para_requisicao"
    ) as duble_preparar:
        dados = {"author": "Agatha Christie"}
        duble_preparar.return_value = dados
        with patch("my_collections.livros.obter_url") as duble_obter_url:
            consultar_livros("Agatha Christie")
            duble_obter_url.assert_called_once_with("https://buscador", dados)


@skip("skiped_3")
def test_consultar_livros_chama_executar_request_usando_retorno_obter_url():
    with patch("my_collections.livros.obter_url") as duble_obter_url:
        duble_obter_url.return_value = "https://buscadordelivros"
        with patch("my_collections.livros.executar_request") as duble_request:
            consultar_livros("Agatha Cristie")
            duble_request.assert_called_once_with("https://buscadordelivros")


class StubHTTPResponse:
    # stub fornece os dados pré-configurados, entradas diretas.
    def read(self):
        return b""

    def __enter__(self):
        return self

    def __exit__(self, param_1, param_2, param_3):
        return


def stub_url_open(url, timeout):
    return StubHTTPResponse()


def test_executar_request_retorna_string():
    with patch("my_collections.livros.urlopen", stub_url_open):
        result = executar_request(
            "https://buscadordelivros?author=Jk+Rowlings",
        )
        assert isinstance(result, str)


def test_another_way_executar_request_retorna_string():
    with patch("my_collections.livros.urlopen") as duble_urlopen:
        duble_urlopen.return_value = StubHTTPResponse()
        result = executar_request(
            "https://buscadordelivros?author=Jk+Rowlings",
        )
        assert isinstance(result, str)


def test_two_another_away_executar_request_returns_string():
    with patch("my_collections.livros.urlopen", return_value=StubHTTPResponse()):
        result = executar_request(
            "https://buscadordelivros?author=Jk+Rowlings",
        )
        assert isinstance(result, str)


@patch("my_collections.livros.urlopen", return_value=StubHTTPResponse())
def test_three_another_away_executar_request_returns_string(duble_urlopen):
    result = executar_request(
        "https://buscadordelivros?author=Jk+Rowlings",
    )
    assert isinstance(result, str)


@patch("my_collections.livros.urlopen")
def test_four_another_away_executar_request_returns_string(
    duble_urlopen: MagicMock,
):
    duble_urlopen.return_value = StubHTTPResponse()
    result = executar_request(
        "https://buscadordelivros?author=Jk+Rowlings",
    )
    assert isinstance(result, str)


class Dummy: ...


def mock_urlopen_raise_http_error(url: str, timeout: int):
    fp = mock_open
    fp.close = Dummy
    raise HTTPError(Dummy(), Dummy(), "msg error", Dummy(), fp)


def test_exec_request_raise_http_error():
    with patch("my_collections.livros.urlopen", mock_urlopen_raise_http_error):
        with pytest.raises(HTTPError) as exception:
            executar_request("https://")
        assert "msg error" in str(exception.value)
