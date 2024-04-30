from typing import Callable

# function as parameter


def msg(name: str) -> str:
    print("Run message")
    return f"Hello {name}"


def long_msg(name: str) -> str:
    print("Run long message")
    return f"Hello {name}, How're you ?"


def run(func: Callable[[str], str], *args) -> str:
    print("Running")
    return func(*args)

# inner function

def main() -> None:
    run(msg, "Some Name")


if __name__ == "__main__":
    main()
