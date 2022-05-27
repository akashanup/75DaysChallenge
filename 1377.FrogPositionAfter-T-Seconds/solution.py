"""
Logic:
    1. This problem can be solved by using DFS traversal.
    2. While traversal, whenever we reach to any node, we track the probability of reaching that node from its parent.
    3. Once we reach the target node,
        i. If time taken to reach the target node is t then we backtrack to root node(i.e, node #1) and multiply all the probabilities on that path and return it.
        ii. If time taken to reach the target node is less than t, then
            - If there are any other nodes that can be reached from target node(except the already visited nodes) then return 0 as we could never reach the target node in t time because frog never stops jumping.
            - If there are no other nodes, then frog can keep on jumping the target node till time equals to t and then return 1.
    4. Probability of reaching any node from its parent can be calculated as 1/(no.of children of this parent)
"""


class Solution:
    def dfs(self, graph, u, t, target, visited):
        visited.add(u)
        if t == 0:
            return int(u == target)
        if u == target:
            for v in graph[u]:
                if v not in visited:
                    return 0
            return 1
        for v in graph[u]:
            if v not in visited:
                probability = self.dfs(graph, v, t - 1, target, visited)
                if probability > 0:
                    # -1 is done because every node will have 1 connection to its parent in adjacency list, but root node(node #1) has no parent.
                    return round(1 / (len(graph[u]) - 1 if u != 1 else len(graph[u])), 5) * probability
        return 0

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = {_: [] for _ in range(1, n + 1)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(graph, 1, t, target, set())
