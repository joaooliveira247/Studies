def main() -> None: 
    symbols = "$¢£¥€¤"

    codes = [ord(symbol) for symbol in symbols]

    print(codes)


if __name__ == "__main__":
    main()