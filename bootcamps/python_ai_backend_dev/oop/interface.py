from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def on(self): ...

    @abstractmethod
    def off(self): ...


class TVControl(RemoteControl):
    def on(self):
        print("Tv ON")

    def off(self):
        print("TV OFF")


class GameControl(RemoteControl):
    def on(self):
        print("Game Control on")

    def off(self):
        print("Remote Control off")


def main() -> None:
    tv = TVControl()
    print(tv)


if __name__ == "__main__":
    main()
