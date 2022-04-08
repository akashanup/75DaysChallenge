"""
    Logic:
        Here we need to think greedy on the capacity of the conveyor as,
            1. The minimum capacity of the conveyor could be the max(weights)
            2. The maximum capacity could be the sum(weights).
        Now we can assume a non-decreasing array whose values starts from minimum Capacity and goes till maximum Capacity.
        Our goal is to find the minimum value in the above capacity range for which all the packages could be shipped within D days.
        We can either sequentially check for each capacity to fulfil the above condition
        OR
        Since the capacity array is sorted, We can use binary search to optimally meet the above condition.
"""


class Solution:
    def isValid(self, weights, proposedCapacity, days):
        capacity = 0
        daysTaken = 0
        for weight in weights:
            if weight > proposedCapacity:
                return False
            if capacity + weight <= proposedCapacity:
                capacity += weight
            else:
                capacity = weight
                daysTaken += 1
        daysTaken += 1
            
        return daysTaken <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        minCapacity = end
        while start < end:
            mid = start + ((end-start)//2)
            if self.isValid(weights, mid, days):
                # Potential answer found.
                minCapacity = mid
                end = mid
            else:
                # Need to increase the capacity!
                start = mid + 1
        return minCapacity
