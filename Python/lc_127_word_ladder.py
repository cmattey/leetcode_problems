# 127. Word Ladder
# Time: O(avg(len of words)*len(wordList))
# Space: O(avg(len of words)*len(wordList)) # For creating the new words and store visited nodes and queue.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Algo:
        - BFS search
        - maintain visited word set to avoid loops
        - function to find words that differ with given word by one char in wordList
        - put these oneCharDiff into q and visited.
        """

        length = 0

        if endWord not in wordList:
            return length

        bfs_q = [beginWord]

        visited = set()

        while bfs_q:

            len_q = len(bfs_q)
            length+=1
            while len_q>0:
                cur_word = bfs_q.pop(0)

                # print(cur_word,length)

                if cur_word==endWord:
                    return length

                visited.add(cur_word)
                nextWords = self.oneCharDiff(cur_word, wordList)

                for word in nextWords:
                    if word not in visited:
                        visited.add(word)       # To avoid visiting previous oneChar diff words
                        bfs_q.append(word)

                len_q-=1


        return 0



    def oneCharDiff(self, word, wordList):
        """
        Returns a set of words in wordList that differ from word by one char
        """
        wordList = set(wordList)

        oneDiff = []
        for i in range(len(word)):

            for ch in range(97, 97+26):
                new_word = word[:i] + chr(ch) + word[i+1:]

                if new_word in wordList and new_word!=word:
                    oneDiff.append(new_word)

        return set(oneDiff)
