import heapq
import math
import sys

"""
Logic:
    1. Since multiplication might give precision errors so its better to take log of the probabilities and add them instead of multiplying.
    2. Since the probabilities is between 0 and 1 so if we are taking its log then it will always give a negative value.
    3. Now if we negate all the logarithmic probabilities then we can simply use Dijkstra Shortest Path Algorithm to find the shortest distance from start vertex to end vertex.   
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [set() for _ in range(n)]
        for key, (u, v) in enumerate(edges):
            graph[u].add((v, -math.log10(succProb[key])))
            graph[v].add((u, -math.log10(succProb[key])))

        dist = [sys.maxsize] * n
        dist[start] = 0

        heap = [[0, start]]
        heapq.heapify(heap)

        while heap:
            latestDist, node = heapq.heappop(heap)
            # Since we are not updating whenever the distance of a node is modified. So, to get the latest distance of a node we need to check the distance of the node popping from heap must match with dist array.
            if latestDist == dist[node]:
                for v, w in graph[node]:
                    if dist[node] + w < dist[v]:
                        dist[v] = dist[node] + w
                        heapq.heappush(heap, [dist[v], v])
        return 10**-dist[end] if dist[end] != sys.maxsize else 0
