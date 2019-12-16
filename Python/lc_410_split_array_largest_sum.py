# 15th Dec '19
# Runtime: 28 ms, faster than 96.78% of Python3
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        left = max(nums)
        right = sum(nums)

        ans = float('inf')
        while left<=right:

            guess_max = (left+right)//2

            cur_groups = 1
            cur_sum = 0

            for num in nums:
                cur_sum+=num

                if cur_sum>guess_max:
                    cur_sum = num
                    cur_groups+=1

            if cur_groups<=m:
                ans = guess_max
                right = guess_max-1
            elif cur_groups>m:
                left = guess_max+1

        return ans    


# 15th Nov '19
# Time: O(nlog(sum_array)), n= len(nums)
# Space: O(1)
# Runtime: 32 ms, faster than 96.69% of Python3
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        largest_sum possible ranges = max(nums), sum(nums)
        make guess, get corresponding value of m, optimize for min largest_sum
        Binary Search approach
        """

        left = max(nums)
        right = sum(nums)

        while left<right:

            guess = left+ (right-left)//2

            cur_split = 1
            cur_sum = 0

            for num in nums:
                cur_sum+=num

                if cur_sum>guess:
                    cur_sum = num
                    cur_split+=1

            if cur_split>m: # guess too small
                left = guess+1
            else:
                right = guess
        #     elif cur_split==m: Alternate conditions, faster than 98.75%
        #         right = guess
        #     else:
        #         right = guess-1
        #
        # return left # only left

        return right # or left

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

        repeat to make group size smaller
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
