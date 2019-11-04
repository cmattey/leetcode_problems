# 34. Find First and Last Position of Element in Sorted Array

# Nov 1st '19
# Time: O(logn)
# Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1,-1]

        low = 0
        high = len(nums)-1

#         Left-Bound
        while low<high:
            mid = (low+high)//2

            if nums[mid]>=target:
                high = mid
            else:
                low = mid+1

        left = high

        if nums[left]!=target:
            return [-1,-1]

        low = 0
        high = len(nums)-1

        while low<high:

            mid = (low+high)//2 +1  # Key is to make this mid, right-biased

            if nums[mid]<=target:
                low = mid
            else:
                high = mid-1

        right = low

        if nums[right]!=target:
            return [-1,-1]

        return [left,right]

# Time: O(log(len(nums)))
# Space: O(1) except recursion stack
class Solution:
    left_start = -1
    right_start = -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums)-1

        self.modBinarySearch(nums,target,left,right)

        return [self.left_start,self.right_start]


    def modBinarySearch(self, nums, target, left, right):

        if left<=right:
            mid = (left+right)//2
            # print(left,right,mid)
            if nums[mid]==target:
                if mid==0:
                    self.left_start = mid
                elif mid-1>=0 and nums[mid-1]!=target:
                    self.left_start = mid

            if nums[mid]==target:
                if mid==len(nums)-1:
                    self.right_start = mid
                elif mid+1<len(nums) and nums[mid+1]!=target:
                    self.right_start = mid

            if nums[mid]<=target:
                self.modBinarySearch(nums,target,mid+1,right)

            if nums[mid]>=target:
                self.modBinarySearch(nums,target,left,mid-1)

        return
