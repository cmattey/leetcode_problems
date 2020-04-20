class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        ans = -1
        while left<=right:

            mid = (left+right)//2

            if nums[mid]==target:
                ans = mid
                break

            if nums[mid]>=nums[left]:
                if nums[mid]>=target and target>=nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<=target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1


        return ans
