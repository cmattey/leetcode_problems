class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch]  = TrieNode()

            node = node.children[ch]

        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]

        return node.isEnd


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]

        return True

class TrieNode():

    def __init__(self):
        self.children = {}
        self.isEnd = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
