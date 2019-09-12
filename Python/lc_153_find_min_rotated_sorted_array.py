# Time: O(log(n))
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:


        start = 0
        end = len(nums)-1

        while start<end:

            mid = (start+end)//2

            if nums[start]<nums[end]:
                return nums[start]
            elif nums[mid]>=nums[start]:
                start = mid+1
            else:
                end = mid


        return nums[start]
