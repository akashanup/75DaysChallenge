class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


class Solution:
    def getMaxDeadline(self, jobs):
        maxDeadLine = 0
        for job in jobs:
            maxDeadLine = max(maxDeadLine, job.deadline)
        return maxDeadLine

    def JobScheduling(self, jobs, n):
        # Find the maximum deadline among all the jobs
        maxDeadLine = self.getMaxDeadline(jobs)

        # Make an array of deadlines from 0 to maxDeadline denoting the deadline slots.
        slots = [True for _ in range(maxDeadLine)]

        # Sort the jobs based on profit in decreasing order to always accommodate those jobs which has more profit.
        jobs.sort(key=lambda x: x.profit, reverse=True)

        maxProfit = 0
        for job in jobs:
            deadline, profit = job.deadline, job.profit
            # Last slot of any job could be (deadline - 1) as every job takes a unit amount of time.
            lastSlot = deadline - 1
            # Check if any slot is available before the last slot of current job
            while lastSlot >= 0 and slots[lastSlot] is False:
                lastSlot -= 1
            if lastSlot >= 0 and slots[lastSlot] is True:
                slots[lastSlot] = False
                maxProfit += profit

        return [len(slots) - sum(slots), maxProfit]
