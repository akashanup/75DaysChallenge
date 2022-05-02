import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for i in range(1, n + 1):
            graph[i] = []

        for u, v, w in times:
            graph[u].append([w, v])

        shortestPathGraph = {}

        heap = [[0, k]]  # [distance, node]

        # Dijkstra's algorithm
        while heap:
            # Always pop the min distance node.
            minDist, u = heapq.heappop(heap)

            if u not in shortestPathGraph:
                shortestPathGraph[u] = minDist
                for dist, v in graph[u]:
                    heapq.heappush(heap, [dist + minDist, v])

        # If any node is not visited then return -1 else max dist
        return max(shortestPathGraph.values()) if len(shortestPathGraph) == n else -1
