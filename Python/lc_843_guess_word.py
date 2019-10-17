# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        """
        O(n), matching approach.
        Try minmax approach as well.
        """
        from collections import defaultdict
        import random

        for i in range(6):
            guess = random.choice(wordlist)
            matches = master.guess(guess)
            print(guess,matches)
            wordlist = [w for w in wordlist if sum(i==j for i,j in zip(guess,w))==matches]
            # print(wordlist)
