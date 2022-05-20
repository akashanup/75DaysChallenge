class Solution:

    def __init__(self):
        self.time = 0

    def dfs(self, graph, u, visited, previsit, low, parent, bridges):
        visited[u] = True
        previsit[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                self.dfs(graph, v, visited, previsit, low, parent, bridges)
                low[u] = min(low[u], low[v])
                if low[v] > previsit[u]:
                    bridges.append([u, v])
            elif v != parent[u]:
                low[u] = min(low[u], previsit[v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
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
        bridges = []

        # Call DFS
        for u in range(n):
            if not visited[u]:
                self.dfs(graph, u, visited, previsit, low, parent, bridges)

        return bridges
    
