# Time:O(n)
# Space:O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = [1]

        for num in nums:
            left_prod.append(left_prod[-1]*num)

        right_prod = [1]

        for num in reversed(nums):
            right_prod.insert(0, right_prod[0]*num)

        op = []

        for i in range(1, len(nums)+1):
            op.append(left_prod[i-1]*right_prod[i])

        return op
