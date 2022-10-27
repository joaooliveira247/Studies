class AppSettings:
    _instace = None

    def __new__(cls, *args, **kwargs) -> None:
        if not cls._instace:
            cls._instace = super().__new__(cls, *args, **kwargs)
        return cls._instace

    def __init__(self) -> None:
        """O init será chamado todas as vezes"""
        self.tema = "O tema escuro"
        self.font = "18px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "O tema claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
