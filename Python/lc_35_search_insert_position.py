# 35. Search Insert Position
# Time: O(log(len(nums)))
# Space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left<=right:

            mid = (left+right)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1

        return left
