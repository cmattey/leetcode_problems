# Time: O(n^2), confirm (Thiking: max combs possible when brackets are n/2 length so combs = n/2*n/2)
# Space: O(n^2)

class Solution:
    def expand(self, S: str) -> List[str]:
        index = 0
        combs = [""]

        while index<len(S):
            if S[index]=='{':
                index+=1
                continue

            cur_options = []
            while index<len(S) and S[index] not in "{}":
                cur_options.append(S[index])
                index+=1

            cur_options = sorted("".join(cur_options).split(','))

            cur_comb = []
            for comb in combs:
                for option in cur_options:
                    cur_comb.append(comb+option)

            combs = cur_comb

            if index<len(S) and S[index] in "{}":
                index+=1

        return combs
