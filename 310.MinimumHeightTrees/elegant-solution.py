class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        graph = [set() for i in range(n)]
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = graph[leaf].pop()
                # remove the only edge left
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)

            # prepare for the next round
            leaves = newLeaves

        # The remaining nodes are the centroids of the graph
        return leaves
