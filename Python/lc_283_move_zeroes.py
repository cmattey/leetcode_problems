# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        nz = 0

        for index, num in enumerate(nums):

            if num!=0:
                nz = index
                nums[nz], nums[z] = nums[z], nums[nz]
                z+=1

        return nums
