class Solution:
    def dfs(self, graph, node, safeNodes, visited, lookup):
        visited[node] = True
        if lookup[node] is None:
            if node in safeNodes:
                lookup[node] = True
            else:
                isSafeNode = True
                for neighbour in graph[node]:
                    if visited[neighbour]:
                        isSafeNode = False
                    else:
                        isSafeNode = isSafeNode and self.dfs(graph, neighbour, safeNodes, visited, lookup)
                    if not isSafeNode:
                        break
                lookup[node] = isSafeNode
        visited[node] = False
        return lookup[node]

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNodes = set()
        for node, neighbours in enumerate(graph):
            if len(neighbours) == 0:
                safeNodes.add(node)
        if not safeNodes:
            return []

        lookup = [None] * len(graph)
        visited = [False] * len(graph)
        for node in range(len(graph)):
            if self.dfs(graph, node, safeNodes, visited, lookup):
                safeNodes.add(node)

        return sorted(list(safeNodes))



        
