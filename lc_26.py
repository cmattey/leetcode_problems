# 26. Remove Duplicates from Sorted Array
# Time: O(len(nums))
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0
        cur_index = 1
        start = 0

        while cur_index<len(nums):
            if nums[cur_index]==nums[cur_index-1]:
                cur_index+=1
            else:
                start+=1
                nums[start] = nums[cur_index]
                cur_index+=1

        return start+1
