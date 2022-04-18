"""
Logic:
    We will iterate from left to right and maintain a monotonic decreasing queue so that for any size window we always have the maximum element at the head of queue.
    Now we will check for each index of nums whether we can make a window of K size from the index of num present at head of queue till the index of current element.
        If yes then add the head to answer.
    We also need to pop out the elements from queue from head whenever that element goes outside of window size.
"""


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        # Maintain a Monotonic decreasing queue
        queue = deque()
        maxWindow = []
        for key, num in enumerate(nums):
            # Pop out elements from queue until the current element becomes smaller than queue's tail to maintain monotonic decreasing queue.
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(key)
            # Remove first element if it is outside window.
            if queue[0] == key - k:
                queue.popleft()
            # If window has k elements then add to result (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if key >= k - 1:
                maxWindow.append(nums[queue[0]])
        return maxWindow


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
# [3,3,5,5,6,7]
