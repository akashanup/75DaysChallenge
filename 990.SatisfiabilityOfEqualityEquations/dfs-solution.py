class Solution:
    def dfs(self, graph, u, target, visited):
        visited.add(u)
        if u == target:
            return True
        for v in graph[u]:
            if v not in visited:
                if self.dfs(graph, v, target, visited):
                    return True
        return False

    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {chr(ord('a')+_):[] for _ in range(26)}

        inequality = []
        for eqn in equations:
            if '!=' in eqn:
                inequality.append([eqn[0], eqn[-1]])
            else:
                graph[eqn[0]].append(eqn[-1])
                graph[eqn[-1]].append(eqn[0])

        for u, v in inequality:
            if self.dfs(graph, u, v, set()):
                return False

        return True
