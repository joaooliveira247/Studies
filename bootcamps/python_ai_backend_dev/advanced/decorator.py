import functools


def my_decorator(func: callable) -> None:
    def env(*args, **kwargs):
        print("do something")
        func(*args, **kwargs)
        print("do something")

    return env


@my_decorator
def hello_world(name: str) -> None:
    print("Hello, world")


def double(func: callable) -> callable:
    @functools.wraps(func)
    def env(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return env


@double
def learning(tec: str) -> str:
    print(f"I'm learning {tec}")
    return tec.upper()


def main() -> None:
    # hello_world("Some name")
    print(learning("Python"))
    print(learning.__name__)


if __name__ == "__main__":
    main()
