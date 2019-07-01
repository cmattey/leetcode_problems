# 16. 3Sum Closest
# Time: O(len(nums)^2)
# Space: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum = float('inf')

        i = 0

        while i<len(nums)-2:
            left = i+1
            right = len(nums)-1

            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]

                diff = abs(target-cur_sum)
                if diff==0:
                    return cur_sum
                elif diff<abs(closest_sum-target):
                    closest_sum = cur_sum

                if cur_sum<target:
                    left+=1
                else:
                    right-=1

            i+=1
            while nums[i]==nums[i-1] and i<len(nums)-2:
                i+=1

        return closest_sum
