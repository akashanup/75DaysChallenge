import string
from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        lowercaseChars = string.ascii_lowercase
        
        queue = deque([[beginWord, 1]])
        
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for ch in lowercaseChars:
                    if word[i] != ch:
                        transformedWord = word[:i] + ch + word[i+1:]
                        if  transformedWord in wordList:
                            wordList.remove(transformedWord)
                            queue.append([transformedWord, level+1])
            
        return 0
