class Solution:
    def findLeft(self, nums, key):
        start = 0
        end = len(nums)
        while start < end:
            mid = start + ((end-start)//2)
            if nums[mid] >= key:
                end = mid
            else:
                start = mid+1
        return start

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        # Build the subsequence in increasing order using binary search
        for num in nums:
            if not lis:
                lis.append(num)
            else:
                j = self.findLeft(lis, num)
                # If the index of current element is len(lis) then it means that the current number is largest in the lis so append it at the end.
                if j == len(lis):
                    lis.append(num)
                else:
                    # Swap the current element with the existing element at its appropriate index
                    lis[j] = num
        return len(lis)
