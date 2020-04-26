class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur_max = float('-inf')

        for index in range(len(nums)):
            cur_max = max(index+nums[index], cur_max)
            if cur_max<=index and index<len(nums)-1:
                return False

            if cur_max>=len(nums)-1:
                return True

        return True
