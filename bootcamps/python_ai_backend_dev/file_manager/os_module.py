import os
import shutil
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent


def create_file_to_remove(path: str) -> None:
    with open(path, "w") as file:
        file.write("To remove")


def main() -> None:
    # create folder
    os.mkdir(f"{BASE_DIR / 'teste'}")
    # rename folder/file
    os.rename(f"{BASE_DIR / 'teste'}", f"{BASE_DIR / 'teste_2'}")
    # remove file
    create_file_to_remove(f"{BASE_DIR / 'teste.txt'}")
    os.remove(f"{BASE_DIR / 'teste.txt'}")
    # move file or folder like posix
    create_file_to_remove(f"{BASE_DIR / 'teste.txt'}")
    shutil.move(f"{BASE_DIR / 'teste.txt'}", f"{BASE_DIR / 'teste_2.txt'}")
    os.remove(f"{BASE_DIR / 'teste_2.txt'}")


if __name__ == "__main__":
    main()
