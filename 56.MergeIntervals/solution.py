class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        end = intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] == intervals[i-1][0]:
                end = max(end, intervals[i][1])
            else:
                merged[-1][1] = end
                if intervals[i][0] > end:
                    merged.append(intervals[i])
                    end = intervals[i][1]
                else:
                    end = max(end, intervals[i][1])
            i += 1
        merged[-1][1] = end
        return merged
