def main() -> None:
    some_dict = {"name": "some name", "age": 24}
    print(
        some_dict.get("name"),
        some_dict.items(),
        some_dict.keys(),
        some_dict.values(),
    )


if __name__ == "__main__":
    main()
