class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for s in sorted(strs):
            sortedStr = tuple(sorted(s))
            if sortedStr in lookup:
                lookup[sortedStr].append(s)
            else:
                lookup[sortedStr] = [s]
        return list(lookup.values())
