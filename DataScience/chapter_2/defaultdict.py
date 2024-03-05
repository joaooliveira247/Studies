from icecream.icecream import ic
from collections import defaultdict


def main() -> None:
    poem: str = """
    Hope is the thing with feathers
    That perches in the soul
    And sings the tune without the words
    And never stops at all,

    Emily Dickinson, Hope is the Thing with Feathers
    """
    word_counts: defaultdict = defaultdict(int)
    poem = poem.strip().splitlines()
    poem = [word for line in poem for word in line.split()]
    for word in poem:
        word_counts[word] += 1

    ic(word_counts)

    dd_list: defaultdict = defaultdict(list)
    dd_list[2].append(1)

    ic(dd_list)

    dd_dict: defaultdict = defaultdict(dict)
    dd_dict["Joel"]["City"] = "Seatle"

    ic(dd_dict)

    dd_pair = defaultdict(lambda: [0, 0])
    dd_pair[2][1] = 1

    ic(dd_pair)


if __name__ == "__main__":
    main()
