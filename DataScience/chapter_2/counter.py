from icecream.icecream import ic
from collections import Counter


def main() -> None:
    c = Counter([0, 1, 2, 0])
    ic(c)

    poem: str = """
    Hope is the thing with feathers
    That perches in the soul
    And sings the tune without the words
    And never stops at all,

    Emily Dickinson, Hope is the Thing with Feathers
    """

    poem = poem.strip().splitlines()
    word_counts: Counter = Counter(
        [word for line in poem for word in line.split()]
    )

    ic(word_counts.most_common(10))


if __name__ == "__main__":
    main()
