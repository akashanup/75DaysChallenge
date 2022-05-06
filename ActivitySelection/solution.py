class Solution:

    def activitySelection(self, n, start, end):
        duration = [[start[i], end[i]] for i in range(n)]
        duration.sort(key=lambda x: x[1])
        prevActivityEnd = duration[0][1]
        activities = 1
        for i in range(1, n):
            if duration[i][0] > prevActivityEnd:
                activities += 1
                prevActivityEnd = duration[i][1]
        return activities
