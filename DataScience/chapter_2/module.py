import re as regex
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

def main() -> None:
    my_regex = regex.compile("[0-9]+", regex.I)

    plt.plot(...)

    lookup = defaultdict(int)
    my_counter = Counter()

    # Don't do this:
    # 
    # match = 10
    # from re import *
    # print(match) this can be a variable or a function


if __name__ == "__main__":
    main()