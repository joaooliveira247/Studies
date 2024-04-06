def main() -> None:
    operations: dict = {
        "AND(True and True, True and False)": (True and True, True and False),
        "OR (True or True, True or False)": (True or True, True or False),
        "NOT(not False)": not False,
    }

    for operation, result in operations.items():
        print(f"{operation} = {result}")


if __name__ == "__main__":
    main()
