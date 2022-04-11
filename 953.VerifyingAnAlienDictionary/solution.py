class Solution:
    def isGreater(self, hashmap, w1, w2):
        i, j = 0, 0
        while i < len(w1) and j < len(w2):
            if hashmap[w1[i]] < hashmap[w2[j]]:
                return False
            if hashmap[w1[i]] > hashmap[w2[j]]:
                return True
            i += 1
            j += 1
        return len(w1) > len(w2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i in range(26):
            hashmap[order[i]] = i
        for i in range(len(words)-1):
            # Check if w1 is greater than w2.
            if self.isGreater(hashmap, words[i], words[i+1]):
                return False
        return True
