def main() -> None:
    operations: dict = {
        "comparasion(200 == 200)": 200 == 200,
        "diff(450 != 300)": 450 != 300,
        "lower than(450 < 300)": 450 < 300,
        "greater than(450 > 300)": 450 > 300,
        "lower than or equal(400 <= 300)": 400 <= 300,
        "greater than or equal(400 >= 300)": 400 >= 300,
    }

    for operation, result in operations.items():
        print(f"{operation} = {result}")


if __name__ == "__main__":
    main()
