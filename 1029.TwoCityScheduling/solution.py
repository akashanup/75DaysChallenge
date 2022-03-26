class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # If all the people travels to the cityA then total cost:
        totalA = 0
        for costA, _ in costs:
            totalA += costA

        # If all the people wish to travel to cityB instead of cityA then the difference in cost would be:
        difference = [costB-costA for costA, costB in costs]

        """
            Since in both the cities the number of people travelling should be equal and their total cost should be minimum,
            So if we move half of the people from cityA to cityB having minimum difference among all the people then the total cost would be the minimum.
        """
        # Total cost of people travelling to cityB instead of cityA having minimum difference:
        totalB = sum(sorted(difference)[:len(costs)//2])
        return totalA + totalB

