def main() -> None:
    lang_version = "Python 3.10.12"
    lang_name = "Python"
    versions = ["3.10.12", "3.11"]

    print(lang_name in lang_version)
    print(lang_version.split(" ")[1] in versions)


if __name__ == "__main__":
    main()
