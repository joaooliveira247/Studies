def main() -> None:
    try:
        print(0 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")


if __name__ == "__main__":
    main()