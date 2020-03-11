# 977. Squares of a Sorted Array

# Review Mar 10th '20
# Time: O(N)
# Space: O(N)

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        first_pos = len(A)

        for index, num in enumerate(A):
            if num>=0:
                first_pos = index
                break

        # first_neg = -1
        # if first_pos==len(A):
        #     first_neg = len(A)-1
        # elif first_pos>0:
        #     first_neg = first_pos-1

        first_neg = first_pos-1

        res = []
        while first_neg>-1 and first_pos<len(A):

            if abs(A[first_neg])<A[first_pos]:
                res.append(A[first_neg]*A[first_neg])
                first_neg-=1
            else:
                res.append(A[first_pos]*A[first_pos])
                first_pos+=1

        while first_neg>-1:
            res.append(A[first_neg]*A[first_neg])
            first_neg-=1

        while first_pos<len(A):
            res.append(A[first_pos]*A[first_pos])
            first_pos+=1

        return res

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
