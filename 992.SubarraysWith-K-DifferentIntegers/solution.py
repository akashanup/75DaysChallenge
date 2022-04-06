"""Logic:
1. To directly count the subarrays with exactly K different integers is hard but to find the count of subarrays with at most K different integers is easy.
2. So the idea is to find the count of subarrays with at most K different integers(fn(K)), and the count of subarrays with at most (K – 1) different integers(fn(K – 1)) and finally take their difference, fn(K) – fn(K – 1) which is the required answer.
3. Now, count of subarrays with at most K different elements can be easily calculated through the sliding window technique.
4. The idea is to keep expanding the right boundary of the window till the count of distinct elements in the window is less than or equal to K and when the count of distinct elements inside the window becomes more than K, start shrinking the window from the left till the count becomes less than or equal to K. Also for every expansion, keep counting the subarrays as end – start + 1.
"""


class Solution:
    def atMostKDistinct(self, nums, k):
        hashmap = {}
        subarrays = 0
        start, end = 0, 0
        while end < len(nums):
            if nums[end] in hashmap:
                hashmap[nums[end]] += 1
            else:
                hashmap[nums[end]] = 1
            while len(hashmap) > k:
                hashmap[nums[start]] -= 1
                if hashmap[nums[start]] == 0:
                    del hashmap[nums[start]]
                start += 1
            subarrays += end-start+1
            end += 1
        return subarrays
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k-1)
