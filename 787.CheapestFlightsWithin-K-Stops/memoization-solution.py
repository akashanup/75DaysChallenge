class Solution:

    def dp(self, graph, src, dst, k, lookup):
        if src == dst:
            return 0

        if k < 0:
            return sys.maxsize

        key = (src, dst, k)
        if key not in lookup:
            cost = sys.maxsize
            for d, c in graph[src]:
                cost = min(cost, c+self.dp(graph, d, dst, k-1, lookup))
            lookup[key] = cost

        return lookup[key]

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {_:[] for _ in range(n)}
        for s, d, c in flights:
            graph[s].append([d, c])

        cost = self.dp(graph, src, dst, k, {})
        return cost if cost < sys.maxsize else -1
