class Solution:
    def dfs(self, graph, visited, v):
        visited[v] = True
        for u in range(len(graph)):
            if graph[v][u] and not visited[u]:
                self.dfs(graph, visited, u)
            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False] * len(isConnected)
        for v in range(len(isConnected)):
            if not visited[v]:
                provinces += 1
                self.dfs(isConnected, visited, v)
        return provinces
