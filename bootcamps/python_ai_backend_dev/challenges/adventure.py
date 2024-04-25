def adventure(n: int) -> None:
    if n <= 0:
        print("Nenhum passo dado na floresta.")
        return
    for i in range(1, n + 1):
        if i == 1:
            print(f"Explorador: {i} passo")
            continue
        print(f"Explorador: {i} passos")


def main() -> None:
    adventure(2)


if __name__ == "__main__":
    main()
