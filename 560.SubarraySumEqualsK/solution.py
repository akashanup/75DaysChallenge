"""
Logic:
    Iterate over the array and keep a track of sum of all the encountered elements (prefix sum). Let's call it as currentSum. Whenever, we find currentSum == k, we have found a required subarray.
    While iterating, also keep a track of all the currentSum which is calculated. This is done because at any point if currentSum exceeds k then we can check whether currentSum - k has already been found or not. If it does then we have found more subarrays.
    Proof: Let's say for index j, the currentSum exceeds k be currentSum_j and for index i (<j) the currentSum be currentSum_i and if currentSum_j - k == currentSum_i then sum(nums[i:j]) would be equal to k. Hence we have found for sub arrays.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        subarrays = 0
        hashmap = {}
        for num in nums:
            currentSum += num
            if currentSum == k:
                subarrays += 1
            if currentSum - k in hashmap:
                subarrays += hashmap[currentSum-k]
            if currentSum in hashmap:
                hashmap[currentSum] += 1
            else:
                hashmap[currentSum] = 1
        return subarrays
