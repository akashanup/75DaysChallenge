class Solution:
    def recur(self, x, n, lookup):
        # Base case 1
        if n == 0 or x == 1:
            return 1
        # Base case 2
        if n == 1:
            return x
        """
            Since a^x * a^y can be written as a^(x+y),
            If n is even then,
                pow(x,n) can be written as pow(x,n/2)*pow(x,n/2) because the exponent gets added when numbers are multiplied.
                For example, pow(2,6) can be written as pow(2,3)*pow(2,3)
            Else,
                pow(x,n) can be written as pow(x,n/2)*pow(x,n/2)*pow(x,1)
                For example, pow(2,7) can be written as pow(2,3)*pow(2,3)*pow(2,1)
        """
        if n not in lookup:
            # Odd
            if n & 1 == 1:
                lookup[n] = self.recur(x, n // 2, lookup) * self.recur(x, n // 2, lookup) * self.recur(x, 1, lookup)
            else:
                # Even
                lookup[n] = self.recur(x, n // 2, lookup) * self.recur(x, n // 2, lookup)
        return lookup[n]

    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return self.recur(x, n, {})
        else:
            return 1 / self.recur(x, -n, {})
