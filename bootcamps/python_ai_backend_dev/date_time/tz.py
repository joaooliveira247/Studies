from datetime import datetime, date, time
from pytz import timezone


def main() -> None:
    print(datetime.now(timezone("Europe/Berlin")))
    datetime()
    date()
    time()


if __name__ == "__main__":
    main()
