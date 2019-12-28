# Time: O(n), n = len(A)
# Space: O(1)
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        inc = True
        dec = True

        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                inc = False
            if A[i]<A[i+1]:
                dec = False

        return inc or dec
        
