def main() -> None:
    name: str = "Some Name"
    age: int = 17
    ADDRESS: str = "somewhere"

    print(f"my name is {name} and my age is {age} years old.")

    age: int = 18

    print(f"now my age now is {age}, and my address is {ADDRESS}")

    full_name, age = "Full Name", 21

    print(
        f"my name is {full_name}, my age is {age} and my address is {ADDRESS}",
    )


if __name__ == "__main__":
    main()
