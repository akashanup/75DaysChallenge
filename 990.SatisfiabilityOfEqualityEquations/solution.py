class DisjointSet:
    def __init__(self, V):
        self.parents = {_: _ for _ in range(V)}
        self.rank = {_: 0 for _ in range(V)}

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parents[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parents[y] = x
            else:
                self.parents[x] = y
                self.rank[y] += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DisjointSet(26)

        equality = [equation for equation in equations if '==' in equation]
        inequality = [equation for equation in equations if '!=' in equation]

        for eqn in equality:
            ds.union(ord(eqn[0]) - ord('a'), ord(eqn[-1]) - ord('a'))

        for eqn in inequality:
            x = ds.find(ord(eqn[0]) - ord('a'))
            y = ds.find(ord(eqn[-1]) - ord('a'))
            if x == y:
                return False

        return True
