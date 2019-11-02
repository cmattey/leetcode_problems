# Time: O(nlog(sum(nums)))
# Space: O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        nums = [7,2,5,10,8]
        m = 2

        if m=1 -> max_sum = sum(nums) = 32
        if m==len(nums) -> max_sum = max(nums) = 10

        range for max_sum = [10,32]

        guess max_sum = 32+10//2 = 21
        find number of groups made with max_sum = 21

        groups = 0
        7+2+5 = 14(can't add next 10, since 24>21)
        groups+=1 (=1)
        10+8 (eol)
        groups+=1 (=2)

        find max out of these groups, and return that.
        if num_groups>m: increase size of group, by increasing lower_bound.
        """

        min_sum = max(nums) # num split = len(nums)-1
        max_sum = sum(nums) # num splits = 1
        ans = float('inf')
        while min_sum<max_sum:

            new_sum = (min_sum+max_sum)//2

            temp_sum = 0
            groups = 1
            for num in nums:
                temp_sum+=num

                if temp_sum>new_sum:
                    ans = min(temp_sum-num, ans)
                    temp_sum = num
                    groups+=1

            if groups>m:
                min_sum = new_sum+1
            else:
                max_sum = new_sum

        # print(groups)
        # print(min_sum, max_sum)
        return max_sum
