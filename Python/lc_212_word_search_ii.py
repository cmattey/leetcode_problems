# Time:
# Space:

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Create trie of words, and do dfs, and check for children in Trie
        """

        root = TrieNode()


        for word in words:
            self.addWord(word, root)

        matched_words = []

        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] in root.children:
                    seen = set()
                    cur_word = []
                    self.dfs(board, row, col, [], root, matched_words, seen)


        return list(set(matched_words))

    def dfs(self, board, row, col, cur_word, cur_node, matched_words, seen):

        # print(cur_word)
        if cur_node.is_end:
            matched_words.append("".join(cur_word))

        if row not in range(len(board)) or col not in range(len(board[0])) or board[row][col] not in cur_node.children or (row,col) in seen:
            return False

        # print(cur_word)
        seen.add((row, col))

        cur_word.append(board[row][col])

        dirs = [(0,-1),(0,1),(1,0),(-1,0)]

        for _dir in dirs:
            self.dfs(board, row+_dir[0], col+_dir[1], cur_word, cur_node.children[board[row][col]], matched_words, seen)

        seen.remove((row, col))
        cur_word.pop()

        return

    def addWord(self, word, root):

        cur_node = root

        for ch in word:

            if ch not in cur_node.children:
                new_node = TrieNode()
                cur_node.children[ch] = new_node

            cur_node = cur_node.children[ch]

        cur_node.is_end = True



class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
