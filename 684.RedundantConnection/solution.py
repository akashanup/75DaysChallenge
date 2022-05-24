class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for vertex in range(1, len(vertices) + 1):
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        # Path compression
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        parent1 = self.find(vertex1)
        parent2 = self.find(vertex2)
        # Union By Rank
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = DisjointSet(edges)
        for vertex1, vertex2 in edges:
            parent1 = disjointSet.find(vertex1)
            parent2 = disjointSet.find(vertex2)
            if parent1 == parent2:
                return [vertex1, vertex2]
            disjointSet.union(vertex1, vertex2)
