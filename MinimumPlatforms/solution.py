class Solution:
    def minimumPlatform(self, n, arr, dep):
        platforms = 1
        maxPlatforms = 1
        arr = sorted(arr)
        dep = sorted(dep)
        i = 1
        j = 0
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1
            elif arr[i] > dep[j]:
                platforms -= 1
                j += 1
            maxPlatforms = max(platforms, maxPlatforms)
        return maxPlatforms
