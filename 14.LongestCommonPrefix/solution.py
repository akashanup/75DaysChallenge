from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False


class Trie:
    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.getTrieNode()
            node = node.children[ch]
        node.eof = True

    def longestPrefix(self):
        node = self.root
        prefix = []
        while len(node.children) == 1 and not node.eof:
            # This loop will always run only one time
            for child in node.children:
                node = node.children[child]
                prefix.append(child)
        return ''.join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        trie = Trie()
        for idx, word in enumerate(strs):
            if word:
                trie.addWord(word)
            else:
                # To handle empty word. idx will never be same so no prefix for it.
                trie.addWord(str(idx))

        return trie.longestPrefix()


print(Solution().longestCommonPrefix(["ab", "a"]))
