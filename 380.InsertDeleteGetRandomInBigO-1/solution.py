class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            # Swap the element that needs to be deleted with the the last element and just pop. This will be much more efficient then traditional pop based on the index.
            # Since we have to remove in O(1) so to find the index of element in O(1) we need a hashmap which will store the val as key and its latest index as value. This data structure is maintained in insert().
            lastHashIndex = self.data[-1]
            valDataIndex = self.hash[val]
            self.hash[lastHashIndex] = valDataIndex
            self.data[-1], self.data[valDataIndex] = self.data[valDataIndex], self.data[-1]
            self.data.pop()
            self.hash.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
