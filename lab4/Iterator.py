from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()


class IterableCollection:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return ConcreteIterator(self._items)


collection = IterableCollection([1, 2, 3, 4, 5])
for item in collection:
    print(item)
