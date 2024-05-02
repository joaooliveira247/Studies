def main() -> None:
    try:
        with open("my_file.txt", "r") as file:
            print(file.readlines())
    except FileNotFoundError as err:
        print(f"File not found: {err}")


if __name__ == "__main__":
    main()
