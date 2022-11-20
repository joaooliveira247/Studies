from collections.abc import Iterator, Iterable
from typing import Any


class MyIterator(Iterator):
    """Like a for"""

    def __init__(self, collection: list[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: list[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: list[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Pedro')
    mylist.add('José')
    mylist.add('João')

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
