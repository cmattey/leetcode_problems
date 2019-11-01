# Time: O(len(words)*avg_len_word) # Duplicate work for stretchy string, can be avoided using Run length encoding
# Space: O(1), except usage of set. Can use run length encoding to reduce duplicate processing of S, and increase space.

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:


        # s_count = collections.Counter(S)

        count_stretch = 0
        len_s_set = len(set(S))

        for word in words:

            if len(set(word))!=len_s_set:
                continue

            w_start = 0
            s_start = 0

            while w_start<len(word):

                match = True
                # print(word, word[w_start], S[s_start])
                if word[w_start]!=S[s_start]:
                    break

                else:

                    count = 1
                    while w_start+1<len(word) and word[w_start+1]==word[w_start]:
                        w_start+=1
                        count+=1
                    # print(word[s_start], count)
                    w_start+=1
                    w_ch_length = count

                    count = 1
                    while s_start+1<len(S) and S[s_start+1]==S[s_start]:
                        s_start+=1
                        count+=1
                    # print(S[s_start], count)
                    s_start+=1
                    s_ch_length = count

                    if w_ch_length==s_ch_length:
                        continue

                    if w_ch_length>s_ch_length:
                        match = False
                        break

                    if w_ch_length<s_ch_length and s_ch_length<3:
                        match = False
                        break
                    else:
                        continue

            if w_start==len(word) and s_start==len(S) and match:
                count_stretch+=1

        return count_stretch


        
