# Time: O(n^3), generating n^2 substrings, and doing n work for each
# Space: O(n^3)

class Solution:
    def encode(self, s: str) -> str:

        memo = {}

        return self.encode_util(s, memo)

    def encode_util(self, s, memo):

        if s in memo:
            return memo[s]

#       List of all possible encodings
        encodings = [s]

#       Check repeated substring, similar problem 459. Repeated Substring Pattern
        s_i =  (s+s).find(s,1)

        if s_i!=-1 and s_i!=len(s):
            encodings.append(str(len(s)//s_i) + "["+self.encode_util(s[:s_i], memo) + "]")

#       Encodings at all possible breakpoints
        for i in range(1, len(s)):
            encodings.append(self.encode_util(s[:i], memo) + self.encode_util(s[i:], memo))

        encodings.sort(key = len)

        memo[s] = encodings[0]
        return encodings[0]
