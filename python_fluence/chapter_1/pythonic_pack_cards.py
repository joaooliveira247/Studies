from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks: list[str] = [str(n) for n in range(2, 11)] + list("JQKA")
    suits: list[str] = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int):
        return self._cards[position]


def spades_high(card: Card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_values) + suit_values[card.suit]


def main() -> None:
    deck = FrenchDeck()

    print(f"len: {len(deck)}, deck[0]: {deck[0]}, deck[-1]: {deck[-1]}")

    print(choice(deck))

    print(deck[12::13])

    for card in deck:
        print(card)

    print(Card("Q", "hearts") in deck, Card("7", "beasts") in deck)

    for card in sorted(deck, key=spades_high):
        print(card)


if __name__ == "__main__":
    main()
