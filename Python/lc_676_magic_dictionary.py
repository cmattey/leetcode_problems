class MagicDictionary:

    """
    Ver1 (current): Most info stored in set value for a particular key word.
        Time: O(sum((w_i)^2)) build and O(len(word)^2+len(wordList)) search ,
        Space: O(sum((w_i)^2)) build, and O(len(word)^2 + avg(len(w_i)))
        The square comes from the splicing operation which is O(n) in Python
    Ver2 (TBD): Instead of storing generalized neighbors as values, store them as keys, with a counter. Need to take care of case, when searched word is in wordList.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict

        self.smap = defaultdict(set)


    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            for i in range(len(word)):
                self.smap[word].add(word[:i]+'*'+word[i+1:])


    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        gen_words = set()

        for i in range(len(word)):
            gen_words.add(word[:i]+'*'+word[i+1:])

        for pot_word in self.smap:
            if word==pot_word:
                continue
            gen_pot_strings = self.smap[pot_word]

            if len(gen_pot_strings.intersection(gen_words))>0:
                return True

        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
