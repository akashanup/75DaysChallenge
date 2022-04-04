"""
Logic:
    To split the string we would need to know the last occurrence of each character because that character won't lie in any further splits.
    Now assume that the first split will happen at the index of last occurrence of first character. Let's call it partitionIndex.
    Iterate over the string and check for each character
        If its index is greater than the partitionIndex then the split should happen at that index.
        Else, update the partitionIndex if the last occurrence of character is greater than partitionIndex.
    Since result requires an array of count of characters partitioned, so we may maintain the partitioned characters and subtract them whenever a partition happens with any index.
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrence = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in lastOccurrence:
                lastOccurrence[s[i]] = i
        
        partitionIndex = lastOccurrence[s[0]]
        
        partitions = []
        partitioned = 0
        
        for index in range(len(s)):
            if index >= partitionIndex:
                partitions.append(index+1-partitioned)
                partitioned += partitions[-1]
                if index < len(s)-1:
                    partitionIndex = lastOccurrence[s[index+1]]
            else:
                partitionIndex = max(partitionIndex, lastOccurrence[s[index]])
        
        return partitions
