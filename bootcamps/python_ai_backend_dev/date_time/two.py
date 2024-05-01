from datetime import datetime, timedelta
from enum import Enum

CURRENT_DATE: datetime = datetime.now()


class EnumCar(str, Enum):
    P = "P"
    M = "M"
    G = "G"


def classifier_car(size: str) -> str:
    times: dict[str, timedelta] = {
        "P": timedelta(minutes=30),
        "M": timedelta(minutes=45),
        "G": timedelta(minutes=60),
    }
    msg: str = "the car arrived at  {} and left at {}"
    match size := size.upper():
        case EnumCar.P:
            return msg.format(CURRENT_DATE, CURRENT_DATE + times[size])
        case EnumCar.M:
            return msg.format(CURRENT_DATE, CURRENT_DATE + times[size])
        case EnumCar.G:
            return msg.format(CURRENT_DATE, CURRENT_DATE + times[size])
        case _:
            raise Exception("Car size not found.")


def main() -> None:
    next_week = CURRENT_DATE + timedelta(7)
    print(next_week, type(next_week))
    print(classifier_car("g"))


if __name__ == "__main__":
    main()
