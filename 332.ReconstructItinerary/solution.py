class Solution:
    def dfs(self, graph, src, itinerary):
        if src in graph:
            while graph[src]:
                dest = graph[src].pop()
                self.dfs(graph, dest, itinerary)
        itinerary.append(src)

    def findItinerary(self, tickets):
        itinerary = []

        graph = {}

        for src, dest in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dest)

        for src in graph:
            # Since we want lexically sorted answer, therefore append all the destination places in reverse order because when we will recursively process it, destination places will come in sorted order.
            graph[src] = sorted(graph[src], reverse=True)

        self.dfs(graph, "JFK", itinerary)

        return itinerary[::-1]
