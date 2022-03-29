class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = {}
        pairs = 0
        for song in time:
            song = song % 60
            counterpart = 60-song if song else song
            if counterpart in hashmap:
                pairs += hashmap[counterpart]
            if song in hashmap:    
                hashmap[song] += 1
            else:
                hashmap[song] = 1
        return pairs
            
        
