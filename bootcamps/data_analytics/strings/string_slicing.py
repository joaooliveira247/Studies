def main() -> None:
    name: str = "some name"

    print(
        name[0],
        name[:3],
        name[2:],
        name[2 : len(name)],
        name[::2],
        name[::],
        name[::-1],
        sep=" | ",
    )


if __name__ == "__main__":
    main()
