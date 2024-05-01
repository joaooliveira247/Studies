from datetime import date, datetime


def main() -> None:
    CURRENT_DATE: date = date(2024, 5, 1)
    print(CURRENT_DATE, type(CURRENT_DATE))
    print(date.min, date.max)
    print(datetime(2024, 5, 1))
    print(date.today(), datetime.now())


if __name__ == "__main__":
    main()
