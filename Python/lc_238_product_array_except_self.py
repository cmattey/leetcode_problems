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
                
