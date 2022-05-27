class Solution:
    def dfs(self, graph, u, visited):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                self.dfs(graph, v, visited)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        connectedComponents = 0
        visited = set()
        for u in range(n):
            if u not in visited:
                self.dfs(graph, u, visited)
                connectedComponents += 1

        return connectedComponents-1
