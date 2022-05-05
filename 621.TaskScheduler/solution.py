import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # Count frequency of each task
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1

        # Build a max-heap of all the frequencies
        heap = [-val for val in hashmap.values()]
        heapq.heapify(heap)

        # Initialize a queue to hold the tasks which are waiting for cool down period
        queue = deque() # [frequency, timeAtWhichItCanStartExecuting]

        timeTaken = 0
        # Iterate till all the tasks are processed.
        while heap or queue:
            timeTaken += 1
            # Pick the task from heap having the maximum frequency.
            if heap:
                frequency = -heapq.heappop(heap)
                # Since only one task can be processed in a unit time. So process the task.
                frequency -= 1
                # Now if this task is left then it will have to wait for the cooldown period. So, enque the task till its cooldown period is expired.
                if frequency:
                    queue.append([frequency, timeTaken + n])

            # Now process the tasks whose cooling period is expired.
            while queue and queue[0][1] == timeTaken:
                heapq.heappush(heap, -queue.popleft()[0])

        return timeTaken


