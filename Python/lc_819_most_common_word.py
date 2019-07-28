# 819. Most Common Word
# Time: O(len(paragraph))
# Space: O(len(parapgraph))
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict

        for punc in "!?',;.":
            paragraph = paragraph.replace(punc," ")

        word_map = defaultdict(int)
        max_count = 0
        ans = ""
        for word in paragraph.lower().split():

            if word not in banned:
                word_map[word]+=1

                if word_map[word]>max_count:
                    max_count = word_map[word]
                    ans = word

        return ans
