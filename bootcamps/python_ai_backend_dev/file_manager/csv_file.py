import csv
from pathlib import Path


BASE_DIR: Path = Path(__file__).parent


def main() -> None:
    with open(f"{BASE_DIR / 'example.csv'}", "r", encoding="utf-8") as file:
        for row in csv.reader(file, delimiter=";"):
            print(f"|{'|'.join(row)}|")


if __name__ == "__main__":
    main()
