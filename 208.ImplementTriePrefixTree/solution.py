class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = self.getTrieNode()
            root = root.children[ch]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.endOfWord

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
