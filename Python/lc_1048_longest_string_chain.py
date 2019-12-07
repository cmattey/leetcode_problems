# Time: nlogn + n*k^2  , n = len(words) <-check, k = max len word
# Space: n

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        create map like so:

        1: (a,1),(b,1)
        2: (ba,1)
        3: (bca,1),(bda,1)...
        """
        import collections
        over_all_max = -1
        word_map = collections.defaultdict(list)

        for word in words:
            word_map[len(word)].append([word, 1])

        lens = list(word_map.keys())
        lens.sort()

        for l in lens:
            if l==1 or l-1 not in lens:
                continue

            prev_words = word_map[l-1]

            temp_words = []
            for w,cur_count in word_map[l]:
                for pw, prev_count in prev_words:
                    if self.isAdj(pw, w):
                        cur_count = max(cur_count, prev_count+1)
                        over_all_max = max(cur_count, over_all_max)
                temp_words.append((w,cur_count))

            word_map[l] = temp_words
            # print(word_map[l])

        return over_all_max if over_all_max!=-1 else 1


    def isAdj(self, word1, word2):
        mismatch_count = 0

        pw_i = 0
        w_i = 0

        while w_i<len(word2) and pw_i<len(word1):
            if word2[w_i]!=word1[pw_i]:
                mismatch_count+=1
                w_i+=1
            else:
                w_i+=1
                pw_i+=1

            if mismatch_count>1:
                return False

        return True
