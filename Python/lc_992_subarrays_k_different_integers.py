# Time: O(n)
# Space: O(n)

class Solution:
    import collections
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        """
        Exact K distinct = At-most K distinct - At-most K-1 distinct
        """

        atmostK = self.atmostKDistinct(A,K)
        atmostK_minus_one = self.atmostKDistinct(A,K-1)

        return atmostK - atmostK_minus_one

    def atmostKDistinct(self, A, K):

        ans = 0
        index = 0
        count_map = collections.defaultdict(int)
        left = 0

        while index<len(A):
            count_map[A[index]]+=1

            while len(count_map)>K:

                count_map[A[left]]-=1
                if count_map[A[left]]==0:
                    del count_map[A[left]]

                left+=1

            index+=1
            ans += index-left

        return ans
