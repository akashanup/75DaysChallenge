class Solution:

    def maximumMeetings(self, n, start, end):
        meetings = 1

        timings = [[start[i], end[i]] for i in range(n)]
        timings.sort(key=lambda x: (x[1], x[0]))

        maxTime = timings[0][1]

        for start, end in timings[1:]:
            if maxTime < start:
                meetings += 1
                maxTime = end

        return meetings
