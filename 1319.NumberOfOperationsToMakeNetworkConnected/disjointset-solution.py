class DisjointSet:
    def __init__(self, V):
        self.parent = [_ for _ in range(V)]
        self.rank = [0 for _ in range(V)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        ds = DisjointSet(n)

        for u, v in connections:
            ds.union(u, v)

        connectedComponents = 0

        for node, parent in enumerate(ds.parent):
            if node == parent:
                connectedComponents += 1

        return connectedComponents - 1
