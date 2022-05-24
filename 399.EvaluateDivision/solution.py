from collections import deque


class Solution:
    def bfs(self, graph, source, target):
        if source not in graph:
            return -1

        queue = deque([[source, 1]])
        visited = {source}
        while queue:
            u, val = queue.popleft()
            if u == target:
                return val
            if u in graph:
                for v in graph[u]:
                    if v[0] not in visited:
                        visited.add(v[0])
                        # If a/b = 2, b/c = 3 then a/c =>
                        # (a/b)*(b/c) => a/c = 2*3 => 6
                        queue.append([v[0], val * v[1]])
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i, (u, v) in enumerate(equations):
            if u not in graph:
                graph[u] = []
            graph[u].append([v, values[i]])
            if v not in graph:
                graph[v] = []
            graph[v].append([u, 1 / values[i]])

        answer = [None] * len(queries)

        for i, (u, v) in enumerate(queries):
            answer[i] = self.bfs(graph, u, v)

        return answer
