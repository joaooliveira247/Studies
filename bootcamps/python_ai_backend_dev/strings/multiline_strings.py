def main() -> None:
    some_thing = "text"
    multi_line: str = f"""
    some
    giant
    {some_thing}
    here
"""

    print(multi_line)


if __name__ == "__main__":
    main()
