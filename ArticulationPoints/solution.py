import sys


class Solution:

    def __init__(self):
        self.time = 0

    def dfs(self, graph, u, visited, previsit, low, parent, ap):
        visited[u] = True
        previsit[u] = self.time
        low[u] = self.time
        self.time += 1
        children = 0

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.dfs(graph, v, visited, previsit, low, parent, ap)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children >= 1:
                    ap.append(u)
                if parent[u] != -1 and low[v] > previsit[u]:
                    ap.append(u)
            elif v != parent[u]:
                low[u] = min(low[u], previsit[v])

    def articulationPoints(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Initialize graph
        graph = [[] for u in range(n)]

        # Add edges
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize other variables that are required
        visited = [False] * n
        previsit = [sys.maxsize] * n
        low = [sys.maxsize] * n
        parent = [-1] * n
        ap = []

        # Call DFS
        for u in range(n):
            if not visited[u]:
                self.dfs(graph, u, visited, previsit, low, parent, ap)

        return ap

