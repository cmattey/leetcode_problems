# Nov 15th '19
# Time: O(n)
# Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Cleaner, Linear time, linear space solution
        """
        left_prod = [None]*len(nums)
        left_prod[0] = 1
        for index in range(1, len(nums)):
            left_prod[index] = left_prod[index-1]*nums[index-1]

        right_prod = [None]*len(nums)
        right_prod[len(nums)-1] = 1
        for index in range(len(nums)-2,-1,-1):
            right_prod[index] = right_prod[index+1]*nums[index+1]

        output = [None]*len(nums)
        for index in range(len(nums)):
            output[index] = left_prod[index]*right_prod[index]

        return output

# Time: O(len(nums))
# Space: O(1), excluding output array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Linear Time, Constant Space solution
        """

        left = ['#']*len(nums)

        for index, num in enumerate(nums):
            if index==0:
                left[index] = nums[index]
            else:
                left[index] = left[index-1]*nums[index]

        r = 1
        for index in range(len(nums)-1, -1, -1):
            if index==len(nums)-1:
                left[index] = left[index-1]*r
                r = nums[index]*r
            elif index==0:
                left[index] = r
            else:
                left[index] = left[index-1]*r
                r = nums[index]*r

        return left

        """
        Linear Time and Linear Space Solution

        left = ['#']*len(nums)
        right = ['#']*len(nums)

        for index, num in enumerate(nums):
            if index==0:
                left[index] = nums[index]
            else:
                left[index] = left[index-1]*nums[index]

        end = len(nums)-1
        for index in range(end, -1, -1):
            if index==len(nums)-1:
                right[index] = nums[index]
            else:
                right[index] = right[index+1]*nums[index]

        output = ['#']*len(nums)

        for index in range(len(nums)):
            if index==0:
                output[index] = right[index+1]
            elif index==len(nums)-1:
                output[index] = left[index-1]
            else:
                output[index] = left[index-1]*right[index+1]

        return output
        """
