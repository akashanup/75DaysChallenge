class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
    
    def findKeyIndex(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return i
        return None

    def put(self, key: int, value: int) -> None:
        index = self.findKeyIndex(key)
        if index is not None:
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        index = self.findKeyIndex(key)
        if index is not None:
            return self.values[index]
        return -1

    def remove(self, key: int) -> None:
        index = self.findKeyIndex(key)
        if index is not None:
            self.keys.pop(index)
            self.values.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
