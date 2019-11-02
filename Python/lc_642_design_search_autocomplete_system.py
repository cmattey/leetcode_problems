class AutocompleteSystem:
    """
    Approach Ideas:
    - Trie
    - Store hotness, and sentence value in last leaf node.(-ve hotness for easy sorting retrieval later)
    - dfs, to visit all child nodes to store all possilbe search results.
    """

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.cur_word = []

        for index, sentence in enumerate(sentences):
            self.add_sentence(sentence, times[index])

    def input(self, c: str) -> List[str]:

        if c!='#':
            self.cur_word.append(c)
            matches = self.search("".join(self.cur_word))
            return [val[1] for val in sorted(matches)[:3]]
        else:
            self.add_sentence("".join(self.cur_word), 1)        # If sentence already exists? hot+=1
            self.cur_word = []

    def search(self, cur_word):

        node = self.root
        matches = []
        for ch in cur_word:
            if ch not in node.children:
                return matches
            else:
                node = node.children[ch]

        return self.dfs(node, matches)

    def dfs(self, node, matches):
        """
        returns list of top 3 matching words
        """
        # print(node)
        if not node:
            return

        if node.isEnd:
            matches.append([node.count, node.entire_data])

        for child in node.children:
            self.dfs(node.children[child], matches)

        # print(matches)
        return matches


    def add_sentence(self, sentence, hot):
        node = self.root

        for ch in sentence:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode()
                node.children[ch] = new_node
                node = node.children[ch]

        node.isEnd = True
        node.count -= hot
        node.entire_data = sentence



class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        self.entire_data = ""

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
