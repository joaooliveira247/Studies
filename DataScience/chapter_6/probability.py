from enum import Enum
import random


class Kid(Enum):
    BOY: int = 0
    GIRL: int = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


def main() -> None:
    both_girls: int = 0
    older_girl: int = 0
    either_girl: int = 0

    random.seed(0)

    for _ in range(1000):
        younger: Kid = random_kid()

        older: Kid = random_kid()

        if older == Kid.GIRL:
            older_girl += 1
        if older == Kid.GIRL and younger == Kid.GIRL:
            both_girls += 1
        if older == Kid.GIRL or younger == Kid.GIRL:
            either_girl += 1

    print("P(both | older):", both_girls / older_girl)
    print("P(both | either):", both_girls / either_girl)


if __name__ == "__main__":
    main()
