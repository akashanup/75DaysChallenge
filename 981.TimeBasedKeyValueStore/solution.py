class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][0].append(timestamp)
            self.hashmap[key][1].append(value)
        else:
            self.hashmap[key] = [[timestamp], [value]]

    def getRight(self, nums, maximum):
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right-left)//2)
            if maximum < nums[mid] :
                right = mid
            else:
                left = mid+1
        return left

    def get(self, key: str, timestamp: int) -> str:
        response = ""
        if key in self.hashmap:
            timestamps = self.hashmap[key][0]
            index = self.getRight(timestamps, timestamp) - 1
            if index >= 0:
                response = self.hashmap[key][1][index]
        return response


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
