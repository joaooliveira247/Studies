def main() -> None:
    """
    Python's dicts are implementation of hash(map/table)
    container key,value data structure composite
    key's can only be immutables values, value cab be Any python type
    dict's are mutables
    """
    empty_dict = {}
    people: dict[str, str | int] = {"name": "some name", "age": 3}
    people["phone"] = "2222222"
    print(empty_dict, people)
    people["address"] = {"street": "somewhere", "number": 28, "code-zone": 231}
    print(people)

    for i in people:
        print(i)


if __name__ == "__main__":
    main()
