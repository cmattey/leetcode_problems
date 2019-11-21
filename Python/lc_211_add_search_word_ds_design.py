class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        cur_node = self.root

        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()

            cur_node = cur_node.children[ch]

        cur_node.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        cur_node = self.root

        return self.word_dfs(word, cur_node)


    def word_dfs(self, word, start_node):

        if len(word)==0:
            if start_node.is_end:
                return True
            else:
                return False

        for index, ch in enumerate(word):
            if ch not in start_node.children and ch!='.':
                return False
            elif ch=='.':
                for child in start_node.children:
                    if self.word_dfs(word[index+1:], start_node.children[child]):
                        return True
                return False                    # Notice return False here
            else:
                start_node = start_node.children[ch]

        return start_node.is_end

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
