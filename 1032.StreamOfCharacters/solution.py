"""
Logic:
    The way to solve the problem is to notice that we always know the last character to match. That gives us an idea to build a trie of reversed words, and try to match the reversed stream of characters.
    This way, instead of multiple choices to match, we always have one path: to match character by character starting from the end of the stream. We could stop once we meet the "end of word" label, which means success. If we couldn't match a character before we meet that label, that means fail.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = self.getTrieNode()
            root = root.children[ch]
        root.endOfWord = True

    def isPrefix(self, word):
        root = self.root
        # Reverse the word because we need to search for prefix.
        for i in range(len(word) - 1, -1, -1):
            if root.endOfWord:
                return True
            if word[i] not in root.children:
                return False
            root = root.children[word[i]]
        return root.endOfWord


class StreamChecker:
    def __init__(self, words: List[str]):
        self.stream = []
        self.trie = Trie()
        for word in words:
            # Reverse the words so that instead of searching for suffix we need to search for prefix which is comparatively easy.
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.trie.isPrefix(self.stream)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
