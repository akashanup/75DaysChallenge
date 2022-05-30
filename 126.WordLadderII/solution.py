import string
from typing import List


class Solution:
    LOWER_CASE_CHARS = string.ascii_lowercase

    def validTransformations(self, wordList, word):
        transformations = []
        for i in range(len(word)):
            for ch in Solution.LOWER_CASE_CHARS:
                transformed = word[:i] + ch + word[i + 1:]
                if transformed in wordList:
                    transformations.append(transformed)
        return transformations

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        layer = {beginWord: [[beginWord]]}
        while layer:
            nextLayer = {}
            for word, transformations in layer.items():
                if word == endWord:
                    return transformations
                else:
                    for transformed in self.validTransformations(wordList, word):
                        if transformed not in nextLayer:
                            nextLayer[transformed] = []
                        for transformation in transformations:
                            nextLayer[transformed].append(transformation+[transformed])
            # Remove visited words to prevent loops.
            wordList -= set(nextLayer.keys())
            layer = nextLayer
        return []


# print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
# print(Solution().findLadders("qa", "sq", ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]))
