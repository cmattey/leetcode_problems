# Time: O(n)
# Space: O(1), except recursion stack

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Using Quick Select
        """

        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, end, k):

        if start>end:
            return -1

        pivot = nums[end]

        i = start
        for index in range(start,end):

            if nums[index]<=pivot:
                nums[i],nums[index] = nums[index],nums[i]
                i+=1

        nums[i],nums[end] = nums[end], nums[i]

        if i==len(nums)-k:
            return nums[i]
        elif i>len(nums)-k:
            return self.quickSelect(nums,start,i-1,k)
        else:
            return self.quickSelect(nums,i+1,end,k)
