class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        currSum = 0
        ans = 0
        for num in nums:
            currSum += num
            if (currSum % k) in hashmap:
                ans += hashmap[currSum % k]
            if currSum % k in hashmap:
                hashmap[currSum % k] += 1
            else:
                hashmap[currSum % k] = 1
        return ans