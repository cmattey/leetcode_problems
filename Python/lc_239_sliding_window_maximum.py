# Time: O(n)
# Space: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        left_max = []
        start = 0
        while start<len(nums):
            cur_max = float('-inf')
            for index in range(start, min(start+k, len(nums))):
                cur_max = max(cur_max, nums[index])
                left_max.append(cur_max)

            start = start+k

        right_max = [float('-inf')]*len(nums)

        start = 0
        while start<len(nums):
            cur_max = float('-inf')

            for index in range(min(start+k-1,len(nums)-1), start-1, -1):
                cur_max = max(cur_max, nums[index])
                right_max[index] = cur_max

            start = start+k

        # print(left_max, right_max)
        left = 0
        right = k-1
        max_window = []

        while left<len(nums)-k+1:
            max_window.append(max(right_max[left], left_max[right]))
            left+=1
            right+=1

        return max_window
