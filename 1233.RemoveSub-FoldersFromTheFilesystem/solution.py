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

    def prefixExists(self, word):
        root = self.root
        for ch in word:
            if root.endOfWord:
                return True
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.endOfWord


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []
        folder.sort()
        trie = Trie()
        for f in folder:
            chars = f.split('/')
            if not trie.prefixExists(chars):
                trie.insert(chars)
                answer.append(f)
        return answer
