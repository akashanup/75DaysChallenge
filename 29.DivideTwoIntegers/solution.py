class Solution:
    """
        Logic:
            Since we have to avoid the usage of '/', '%', '*' operators so what we could do is,
                we could subtract the dividend by double multiplier of divisor until dividend becomes smaller than divisor.
            For example, dividend = 40, divisor = 3
                1. Can we take 3 out of 40? Yes! So, dividend => 40-3 = 37, divisor => 3*2 = 6
                2. Can we take 6 out of 37? Yes! So, dividend => 37-6 = 31, divisor => 6*2 = 12
                3. Can we take 12 out of 31? Yes! So, dividend => 31-12 = 19, divisor => 12*2 = 24
                4. Can we take 24 out of 19? No! Now we have to again follow the above approach by resetting the divisor.
                    So, dividend = 19, divisor = 3
                        And ans till now is, 1 + 2 + 4 = 7
                5. Can we take 3 out of 19? Yes! So, dividend => 19-3 = 16, divisor => 3*2 = 6
                6. Can we take 6 out of 16? Yes! So, dividend => 16-6 = 10, divisor => 6*2 = 12
                7. Can we take 12 out of 10? No! Now we have to again follow the above approach by resetting the divisor.
                    So, dividend = 10, divisor = 3
                        And ans till now is, 7 + 1 + 2 = 10
                8. Can we take 3 out of 10? Yes! So, dividend => 10-3 = 7, divisor => 3*2 = 6
                9. Can we take 6 out of 7? Yes! So, dividend => 7-6 = 1, divisor => 3*2 = 12
                6. Terminate the iterations because dividend < divisor.
                        And ans till now is, 10 + 1 + 2 = 13
    """

    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend):
            return 0

        positive = (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)

        if abs(divisor) == abs(dividend):
            return 1 if positive else -1

        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > 1:
            while dividend >= divisor:
                tempDivisor = divisor
                multiple = 1
                while dividend >= tempDivisor:
                    dividend -= tempDivisor
                    ans += multiple
                    multiple = multiple << 1
                    tempDivisor = tempDivisor << 1
        else:
            ans = dividend

        if not positive:
            ans = -ans

        ans = max(-2 ** 31, ans)
        ans = min(ans, 2 ** 31 - 1)

        return ans


print(Solution().divide(40, 3))
