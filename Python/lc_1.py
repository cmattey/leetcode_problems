# 1. Two Sum
# Time: O(len(nums))
# Space: O(len(nums))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        imap = {}

        for index,num in enumerate(nums):
            if target-num in imap:
                return [index,imap[target-num]]
            else:
                imap[num] = index

        return
