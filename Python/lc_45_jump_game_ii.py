# Time: O(n)
# Space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0

        farthest = nums[0]
        if farthest>=len(nums)-1:
                return 1

        min_jumps =1
        index = 1

        while index<len(nums):

            prev_farthest = farthest

            while index<len(nums) and index<=prev_farthest:
                farthest = max(farthest, index+nums[index])
                index+=1

            min_jumps+=1
            if farthest>=len(nums)-1:
                return min_jumps

            if farthest<=prev_farthest:
                return -1


        return min_jumps
