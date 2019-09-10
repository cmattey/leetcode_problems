# Time: O(n)
# Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        m = nums[0]

        imin = nums[0]
        imax = nums[0]

        for index in range(1,len(nums)):

            if nums[index]<0:
                imin,imax = imax,imin

            imax = max(imax*nums[index], nums[index])
            imin = min(imin*nums[index], nums[index])

            m = max(m,imax)

        return m
        
