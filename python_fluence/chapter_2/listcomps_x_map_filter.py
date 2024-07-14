def main() -> None:
    symbols = "$¢£¥€¤"
    listcomps = [ord(s) for s in symbols if ord(s) > 127]

    print(listcomps)

    map_filter = list(filter(lambda c: c > 127, map(ord, symbols)))

    print(map_filter)


if __name__ == "__main__":
    main()
