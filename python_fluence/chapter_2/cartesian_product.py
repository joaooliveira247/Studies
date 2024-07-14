def main() -> None:
    colors = ["black", "white"]
    sizes = ['S', 'M', 'L']

    tshirts = [(color, size) for color in colors for size in sizes]

    print(tshirts)

    


if __name__ == "__main__":
    main()