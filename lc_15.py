# 15. 3Sum
# Time: O(len(nums)^2)
# Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sol_set = []
        i = 0
        while i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                if cur_sum==0:
                    sol_set.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    right-=1
                    while nums[right]==nums[right+1] and right>left:
                        right-=1

                elif cur_sum<0:
                    left+=1
                else:
                    right-=1

            i+=1
            while i in range(len(nums)-2) and nums[i]==nums[i-1]:
                i+=1

        return sol_set
