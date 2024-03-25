from __future__ import annotations
from my_collections.livros import consultar_livros, executar_request, write_archive
from unittest.mock import patch, MagicMock, mock_open, Mock
from unittest import skip
from urllib.error import HTTPError
import pytest


class StubHTTPResponse:
    # stub fornece os dados pré-configurados, entradas diretas.
    def read(self):
        return b""

    def __enter__(self):
        return self

    def __exit__(self, param_1, param_2, param_3):
        return


@patch("my_collections.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_retorna_formato_string(
    stub_urlopen: MagicMock,
) -> None:
    result: str = consultar_livros("Agatha Christie")
    assert isinstance(result, str) is True


@patch("my_collections.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_chama_preparar_dados_para_uma_vez_e_com_os_mesmos_parametros_de_consultar_livros(
    stub_urlopen: MagicMock,
):
    with patch("my_collections.livros.preparar_dados_para_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")


@patch("my_collections.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_chama_obter_url_usando_parametro_retorno_preparar_dados_requisicao(
    stub_urlopen: MagicMock,
):
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


def stub_urlopen_raise_http_error(url: str, timeout: int):
    fp = mock_open
    fp.close = Dummy
    raise HTTPError(Dummy(), Dummy(), "msg error", Dummy(), fp)


@skip("skiped")
def test_exec_request_raise_http_error():
    with patch("my_collections.livros.urlopen", mock_urlopen_raise_http_error):
        with pytest.raises(HTTPError) as exception:
            executar_request("https://")
        assert "msg error" in str(exception.value)


@skip("skiped")
@patch("my_collections.livros.urlopen")
def test_another_exec_request_raise_http_error(mock_urlopen: MagicMock):
    fp = mock_open()
    mock_instance = Mock()
    fp.close = mock_instance
    mock_urlopen.side_effect = HTTPError(
        mock_instance,
        mock_instance,
        "msg error",
        mock_instance,
        fp,
    )
    with pytest.raises(HTTPError) as exception:
        executar_request("https://")
        assert "msg error" in str(exception.value)


def test_exec_request_log_error_message(caplog: pytest.LogCaptureFixture):
    with patch("my_collections.livros.urlopen", stub_urlopen_raise_http_error):
        result = executar_request("http://")
        error_message = "msg error"
        assert len(caplog.records) == 1
        for rec in caplog.records:
            assert error_message in rec.message


@patch("my_collections.livros.urlopen")
def test_exec_request_log_error_message_two(
    mock_urlopen: MagicMock, caplog: pytest.LogCaptureFixture
):
    fp = mock_open()
    mock_instace = Mock()
    fp.close = mock_instace
    mock_urlopen.side_effect = HTTPError(
        mock_instace,
        mock_instace,
        "msg error",
        mock_instace,
        fp,
    )
    executar_request("http://")
    assert len(caplog.records) == 1
    for register in caplog.records:
        assert "msg error" in register.message


def duble_make_dirs(
    dir,
):
    raise OSError(f"Permission Error at {dir}")


class DubleLogging:
    # MOCK spy -> captura e armazena as informações geradas pelo test
    def __init__(self) -> None:
        self._msg: list[str] = []

    def exception(self, msg: str):
        self._msg.append(msg)

    @property
    def messages(self) -> list[str]:
        return self._msg


def test_write_file_raise_exception_that_not_possible_create():
    archive = "/tmp/archive"
    content = "/books data/"
    duble_logging = DubleLogging()
    with patch("my_collections.livros.os.makedirs", duble_make_dirs):
        with patch("my_collections.livros.logging", duble_logging):
            write_archive(archive, content)
        assert "Permission Error at <built-in function dir>" in duble_logging.messages


@patch("my_collections.livros.os.makedirs")
@patch("my_collections.livros.logging.exception")
@patch("my_collections.livros.open", side_effect=OSError())
def test_write_file_log_error_when_create(
    stub_open: MagicMock, spy_exception: MagicMock, stub_makedirs: MagicMock
):
    print([type(x) for x in [stub_open, spy_exception, stub_makedirs]])
    write_archive("/bla/arquivo.json", "content here")
    spy_exception.assert_called_once_with("Permission Error at <built-in function dir>")


class SpyFP:
    def __init__(self) -> None:
        self._content = None

    def __enter__(self) -> SpyFP:
        return self

    def __exit__(self, param_1, param_2, param_3) -> None: ...

    def write(self, content):
        self._content = content


@patch("my_collections.livros.open")
def test_write_archive_call_write(stub_open: MagicMock):
    archive = "/tmp/archive"
    content = "/books data/"
    spy_fp = SpyFP()
    stub_open.return_value = spy_fp
    write_archive(archive, content)
    assert spy_fp._content == content


@patch("my_collections.livros.open")
def test_write_archive_call_write(stub_open: MagicMock):
    archive = "/tmp/archive"
    content = "/books data/"
    spy_fp: MagicMock = MagicMock()
    spy_fp.__enter__.return_value = spy_fp
    spy_fp.__exit__.return_value = None
    stub_open.return_value = spy_fp

    write_archive(archive, content)
    spy_fp.write.assert_called_once_with(content)
