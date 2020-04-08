# Time: O(n)
# Space: O(n)
class Solution:
    def countElements(self, arr: List[int]) -> int:

        import collections

        counter = collections.Counter(arr)

        ans = 0
        for num in counter:
            if num+1 in counter:
                ans+= counter[num]

        return ans
