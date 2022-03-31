class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs = set()
        hashset = set()
        for num in nums:
            counterPart = num-k
            if counterPart in hashset:
                pairs.add(counterPart)
            hashset.add(num)
        return len(pairs)
