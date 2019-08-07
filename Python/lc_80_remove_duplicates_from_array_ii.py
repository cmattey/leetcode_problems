# 80. Remove Duplicates from Sorted Array II
# Time: O(len(nums))
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start = 0
        index = 0
        while index<len(nums):

            if start<2 or (nums[index]!=nums[start-1] or nums[index]!=nums[start-2]):
                nums[start]=nums[index]
                start+=1
            index+=1

        return start
