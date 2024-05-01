from datetime import datetime

CURRENT_DATE = datetime.now()


def main() -> None:
    string_date = "01/05/2024 10:50"
    print(CURRENT_DATE.strftime("%d/%m/%Y %H:%M"))
    parser_date: datetime = datetime.strptime(string_date, "%d/%m/%Y %H:%M")
    print(type(string_date), parser_date, type(parser_date))


if __name__ == "__main__":
    main()
