"""
Logic:
    1. To solve this question, we will use the Dijkstra's Algorithm to find the shortest path for all the connected nodes from a given node.
    2. However, we have a constraint of maxMoves that means the maximum distance between the source node and any other node would be maxMoves.
    3. So initially, let's find the nodes(of original graph) which can be reached from source node within maxMoves.
    4. While finding the nodes, we store the moves left at the time of visiting the node. (This will help later when we will calculate the subdivided nodes).
    5. Once we have found all the possible nodes (of original graph), we move to subdivided nodes as, for each edge from u o v having cnt nodes between them,
        - The total number of subdivided nodes that can be reached between u -> v would be:
            - minimum((moves left(while visiting u) + moves left(while visiting v)), total number of subdivided nodes between u->v)
"""

import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, cnt in edges:
            graph[u].append([v, cnt])
            graph[v].append([u, cnt])

        visited = [-1 for _ in range(n)]

        heap = [[-maxMoves, 0]]
        heapq.heapify(heap)

        while heap:
            movesLeft, u = heapq.heappop(heap)
            if visited[u] == -1:
                visited[u] = -movesLeft
                for v, cnt in graph[u]:
                    movesRequired = -movesLeft - (cnt + 1)
                    if visited[v] == -1 and movesRequired >= 0:
                        heapq.heappush(heap, [-movesRequired, v])

        nodesReached = 0

        # Nodes Reached of original graph
        for u in visited:
            if u >= 0:
                nodesReached += 1

        # Nodes Reached of subdivided graph except the nodes of original graph
        for u, v, cnt in edges:
            moves = 0
            # Moves left while visiting u
            if visited[u] >= 0:
                moves += visited[u]
            # Moves left while visiting v
            if visited[v] >= 0:
                moves += visited[v]

            nodesReached += min(moves, cnt)

        return nodesReached
