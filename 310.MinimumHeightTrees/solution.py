class Solution:
    def findMinHeightTrees(self, n: int, edges):
        graph = {}
        for node in range(n):
            graph[node] = set()

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        minHeightRoots = [_ for _ in range(n)]
        # Since the maximum number of min height roots could be 2 so prune the leaf nodes layer by layer till we are left with 1 or 2 node.
        while len(minHeightRoots) > 2:
            leaves = set([node for node in minHeightRoots if len(graph[node]) == 1])
            # Prune the leaves from minHeightRoots
            minHeightRoots = [node for node in minHeightRoots if node not in leaves]
            # Prune the leaves from graph
            for leaf in leaves:
                for node in graph[leaf]:
                    graph[node].remove(leaf)
        return list(minHeightRoots)
