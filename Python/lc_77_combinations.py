# 77. Combinations
# Time: k*nCk  (Review: nCk combinations each of length k)
# Space: k*nCk
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if n==0:
            return []

        if k==0:
            return [[]]

        if k==1:
            return [[i] for i in range(1,n+1)]

        without_n = self.combine(n-1, k)
        with_n = self.combine(n-1, k-1)

        for index in range(len(with_n)):
            with_n[index] = [n]+with_n[index]

        return without_n + with_n
