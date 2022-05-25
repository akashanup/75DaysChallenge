class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {_:[] for _ in range(n)}
        for s, d, c in flights:
            graph[s].append([d, c])

        stops = 0
        cost = 0
        queue = deque([[src, cost, stops]])

        minCost = [sys.maxsize] * n
        while queue:
            s, cost, stops = queue.popleft()
            if stops <= k:
                for d, c in graph[s]:
                    if cost+c < minCost[d]:
                        minCost[d] = cost+c
                        queue.append([d, cost+c, stops+1])

        return minCost[dst] if minCost[dst] != sys.maxsize else -1
