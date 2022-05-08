"""
Might give TLE
"""



class Solution:
    def isValid(self, num1, num2):
        diff = 0
        for i in range(32):
            diff += int((num1 & 1) != (num2 & 1))
            if diff > 1:
                return False
            num1 >>= 1
            num2 >>= 1
        return diff == 1

    def recur(self, nums, code, used, i):
        if i == len(nums):
            return self.isValid(code[0], code[-1])

        for num in nums[1:]:
            if not used[num] and self.isValid(code[i-1], num):
                used[num] = True
                code[i] = num
                if self.recur(nums, code, used, i+1):
                    return True
                code[i] = None
                used[num] = False
        return False

    def grayCode(self, n: int) -> List[int]:
        nums = [_ for _ in range(2**n)]
        used = [False] * (2**n)
        code = [None] * (2**n)
        code[0] = 0
        used[0] = True
        self.recur(nums, code, used, 1)
        return code
