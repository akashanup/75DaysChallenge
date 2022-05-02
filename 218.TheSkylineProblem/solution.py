import heapq
import sys


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
            Observation:
                1. The start point of all the buildings could be a potential key point.
                2. The end point of all the buildings could be a potential key point.
                3. Sort these points based on start point then by their respective height so that while iteratng we can be assure that for same starting point, we will et max height point first.
                4. Track the maxHeight while iterating and for any point the maxHeight changes then that point is a key point.
        """
        points = []
        for s, e, h in buildings:
            points.append([s, e, -h])
            # Height is taken as zero to distinguish between starting and ending point.
            points.append([e, 0, 0])

        points.sort(key=lambda x: (x[0], x[2], x[1]))

        keyPoints = [[0, 0]]
        heap = [[0, sys.maxsize]]
        for s, e, h in points:
            # Pop out the buildings which are already left behind.
            while heap and heap[0][1] <= s:
                heapq.heappop(heap)

            # If the current point is the start point of any building then push it to heap.
            if h != 0:
                heapq.heappush(heap, [h, e])

            # If by pushing the current point into heap, the maxHeight changed, then include the current point in answer
            if keyPoints[-1][1] != -heap[0][0]:
                keyPoints.append([s, -heap[0][0]])

        return keyPoints[1:]
