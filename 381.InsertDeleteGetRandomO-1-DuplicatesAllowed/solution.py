from random import choice


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the hashmap.
        Returns true if the hashmap did not already contain the element.
        """
        if val in self.hashmap:
            self.hashmap[val].add(len(self.collection))
        else:
            self.hashmap[val] = {len(self.collection)}

        self.collection.append(val)

        return len(self.hashmap[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the hashmap.
        Returns true if the hashmap contained the element.
        """
        if val not in self.hashmap or len(self.hashmap[val]) == 0:
            return False
        removeIndex, lastElement = self.hashmap[val].pop(), self.collection[-1]
        self.collection[removeIndex] = lastElement
        self.hashmap[lastElement].add(removeIndex)
        self.hashmap[lastElement].discard(len(self.collection) - 1)

        self.collection.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.collection)
