# 55. Jump Game
# Time: O(len(nums))
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums)<=1:
            return True

        max_pos = nums[0]
        for index in range(len(nums)):

            max_pos = max(max_pos, index+nums[index])

            if index>=max_pos:
                return False

            if max_pos>=len(nums)-1:
                return True

        return False
