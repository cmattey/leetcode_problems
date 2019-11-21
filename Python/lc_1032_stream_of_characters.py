class StreamChecker:

    def __init__(self, words: List[str]):

        self.root = TrieNode()
        self.waitlist = []

        for word in words:
            self.addWord(word)

    def addWord(self, word):

        cur_node = self.root

        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()

            cur_node = cur_node.children[ch]

        cur_node.is_end = True


    def query(self, letter: str) -> bool:

        cur_waitlist = []

        if letter in self.root.children:
            cur_waitlist.append(self.root.children[letter])

        for node in self.waitlist:
            if letter in node.children:
                cur_waitlist.append(node.children[letter])

        self.waitlist = cur_waitlist

        return any(temp.is_end for temp in self.waitlist)





class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
