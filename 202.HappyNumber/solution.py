class Solution:
    def getNext(self, number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            number //= 10
            total_sum += digit ** 2
        return total_sum

    def isHappy(self, n: int) -> bool:
        slowRunner = n
        fastRunner = self.getNext(n)
        while fastRunner != 1 and slowRunner != fastRunner:
            slowRunner = self.getNext(slowRunner)
            fastRunner = self.getNext(self.getNext(fastRunner))
        return fastRunner == 1
