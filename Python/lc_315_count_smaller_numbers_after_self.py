# Time: O(n^2), can be done in O(nlogn time)
# Space: O(n)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        op = []
        sorted_nums = []
        for num in nums[::-1]:
            index = bisect.bisect_left(sorted_nums, num)
            op.append(index)
            sorted_nums.insert(index, num)

        return op[::-1]
