# Time: O(n), n=len(nums)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        imap = {}

        for index, num in enumerate(nums):
            if target-num in imap:
                return [imap[target-num], index]
            else:
                imap[num] = index

        return [None, None]
