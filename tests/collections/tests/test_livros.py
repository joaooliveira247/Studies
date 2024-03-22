from my_collections.livros import consultar_livros


def test_consultar_livros_retorna_formato_string() -> None:
    result: str = consultar_livros("Agatha Christie")
    assert isinstance(result, str) is True
