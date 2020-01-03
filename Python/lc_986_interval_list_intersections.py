# Time: O(n), where n=len(A)+len(B)
# Space: O(n)

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        a = 0
        b = 0

        ans = []

        while a<len(A) and b<len(B):

            start = max(A[a][0], B[b][0])
            end = min(A[a][1], B[b][1])

            if start<=end:
                ans.append([start, end])

            if end==A[a][1]:
                a+=1
            else:
                b+=1

        return ans
