class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = start + ((end - start) // 2)
            if arr[mid] > arr[mid+1]:
                # We are on the decreasing part of arr. So, arr[mid] might be a potential answer but answer may be present to left of mid also. So we need to look for left of mid also.
                end = mid
            else:
                # We are on the increasing part of arr. So, the answer would definitely be present at right ride of mid.
                start = mid + 1
        # The loop terminates when start == end. This also means that start(or end) will have the peak element as well because the if else inside the loop converges towards the peak element.
        return start
