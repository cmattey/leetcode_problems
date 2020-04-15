# Time: O(n)
# Space: O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count_map = {0:-1}
        cur_count = 0
        max_len = 0

        for index, num in enumerate(nums):

            if num:
                cur_count+=1
            else:
                cur_count-=1

            if cur_count in count_map:
                max_len = max(max_len, index-count_map[cur_count])
            else:
                count_map[cur_count] = index

        return max_len
