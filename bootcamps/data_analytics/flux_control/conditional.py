def clause_if() -> None:
    balance: int = 2000
    withdraw: int = int(input("Type value to withdraw: "))

    if withdraw < balance:
        print(f"USD: {withdraw} removed {withdraw - balance} remain")
    elif withdraw == balance:
        print(f"USD: {withdraw} removed {withdraw - balance} remain")
    else:
        print(f"value {withdraw} not available.")
    return


def clause_if_ternary() -> None:
    balance: int = 2000
    withdraw: int = int(input("Type value to withdraw: "))

    status = "Sucess" if balance >= withdraw else "Error"

    print(f"{status} to try withdraw")


def main() -> None:
    clause_if()
    clause_if_ternary()


if __name__ == "__main__":
    main()
