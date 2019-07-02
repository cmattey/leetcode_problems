# 18. 4Sum
# Time: O(len(nums)^3)
# Space: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        sol_set = []
        i = 0
        while i<len(nums)-3:
            j = i+1
            while j<len(nums)-2:
                k = j+1
                l = len(nums)-1

                while k<l:
                    cur_sum = nums[i]+nums[j]+nums[k]+nums[l]

                    if cur_sum==target:
                        sol_set.append([nums[i],nums[j],nums[k],nums[l]])

                        k+=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1

                        l-=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1

                    elif cur_sum<target:
                        k+=1
                    else:
                        l-=1

                j+=1
                while j<len(nums)-2 and nums[j]==nums[j-1]:
                    j+=1

            i+=1
            while i<len(nums)-3 and nums[i]==nums[i-1]:
                i+=1

        return sol_set
