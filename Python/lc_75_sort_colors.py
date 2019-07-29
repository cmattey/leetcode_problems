# 75. Sort Colors
# Time: O(len(nums)), single pass
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Double-pass with counting colors separately.
        Single-pass implementation here.
            - Keep track of start for red, white, blue
            - compare what the white index is at every point, and use that
                to manipulate red, white, blue pointers
        """

        red = 0
        white = 0
        blue = len(nums)

        index = 0

        while white < blue:
            if nums[white]==0:
                nums[red],nums[white] = nums[white], nums[red]
                red+=1
                white+=1
            elif nums[white]==1:
                white+=1
            elif nums[white]==2:
                blue-=1
                nums[blue],nums[white] = nums[white], nums[blue]


        # print(nums)
