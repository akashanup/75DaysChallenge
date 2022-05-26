class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = [0]*(n+1)
        for i,j in trust:
            judge[i] -= 1
            judge[j] += 1

        for j in range(1, n+1):
            if judge[j] == n-1:
                return j
        return -1
