from array import array


def main() -> None:
    symbols = "$¢£¥€¤"

    genexp = (ord(symbol) for symbol in symbols)

    gen_tuple = tuple(genexp)

    print(gen_tuple)

    genexp = (ord(symbol) for symbol in symbols)

    gen_array = array("I", genexp)

    print(gen_array)

    colors = ["black", "white"]
    sizes = ["S", "M", "L"]

    for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
        print(tshirt)


if __name__ == "__main__":
    main()
