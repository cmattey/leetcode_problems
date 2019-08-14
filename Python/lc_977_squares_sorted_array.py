# 977. Squares of a Sorted Array
# Time: O(n)
# Space: O(n)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        Time: O(nlog(n)) Solution
        Space: O(1)
        A = [num**2 for num in A]
        return sorted(A)
        """

        #Time: O(n) solution
        res = []

        for index in range(len(A)):
            if A[index]>=0:
                break

        start = index

        A = [num**2 for num in A]

        pos_start = start # moves right
        neg_start = start-1   # moves left

        while neg_start>=0 and pos_start<len(A):
            if A[neg_start]<A[pos_start]:
                res.append(A[neg_start])
                neg_start-=1
            else:
                res.append(A[pos_start])
                pos_start+=1

        while neg_start>=0:
            res.append(A[neg_start])
            neg_start-=1

        while pos_start<len(A):
            res.append(A[pos_start])
            pos_start+=1

        return res
