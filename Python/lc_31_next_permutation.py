# 31. Next Permutation
# Time: O(len(nums))
# Space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Algo:
        1. Find swap index: where arr[i+1]>arr[i]
        2. Swap arr[i] with element to its right which is "just" larger than it
        3. Sort elements to right of i in increasing order in-place.
        """

        #1.
        swap_index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                swap_index = i
                break

        #2.
        if swap_index>=0:
            swap_with_index = swap_index
            for i in range(swap_index+1,len(nums)):
                if nums[i]>nums[swap_index]:
                    swap_with_index = i
                elif nums[i]<nums[swap_index]:
                    break

            nums[swap_index],nums[swap_with_index] = nums[swap_with_index], nums[swap_index]

        #3.

        left = swap_index+1
        right = len(nums)-1

        while left<right:
            nums[left],nums[right] = nums[right], nums[left]
            left+=1
            right-=1
