"""
    Logic: Let's say we have to calculate the value of pow(2,10) and store it into 'ans' variable.
        10 can be represented as 1010 in binary.
        Now if we iterate on the bits of 10 i.e, 1010 from right to left,
            Whenever we find a set bit, we know that this bit will contribute to 'ans', therefore 'ans' would be multiplied by the value of x so far.
            Value of x so far means, value of x multiplied by itself(since we need to calculate pow) till the current bit.
        DRY RUN: x = 2, n = 10 or 1010 in binary, ans = 1(default)
            1st iteration, we have an unset bit therefore no contribution to 'ans' and x becomes x*x i.e., 2*2 = 4
            2nd iteration. we have a set bit therefore this bit will contribute to 'ans'. 'ans' becomes, ans*x i.e., 1*4 = 4 and x becomes x*x i.e, 4*4 = 16
            3rd iteration, we again have an unset bit therefore no contribution to 'ans' and x becomes x*x i.e., 16*16 = 256
            4th iteration, we have a set bit therefore this bit will contribute to 'ans'. 'ans' becomes ans*x i.e., 4*256 = 1024 and x becomes x*x.
            No more bit left, therefore ans is 1024
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n > 0:
            while n > 0:
                if n & 1:
                    ans *= x
                x *= x
                n >>= 1
            return ans
        else:
            n *= -1
            while n > 0:
                if n & 1:
                    ans *= x
                x *= x
                n >>= 1
            return 1 / ans
