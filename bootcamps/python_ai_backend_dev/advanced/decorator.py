def my_decorator(func: callable) -> None:
    def env():
        print("do something")
        func()
        print("do something")

    return env


@my_decorator
def hello_world() -> None:
    print("Hello, world")


def main() -> None:
    hello_world()


if __name__ == "__main__":
    main()
