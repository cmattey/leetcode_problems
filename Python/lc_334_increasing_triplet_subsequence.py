# Oct28th '19
# Time: O(n)
# Space: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums)<3:
            return False

        first = nums[0]
        second = None

        for num in nums[1:]:

            if num<=first:
                first = num
            elif second==None or num<=second:
                second = num
            else:
                return True

        return False


# Time: O(n)
# Space: O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums)<3:
            return False

        first = nums[0]
        second = '#'

        for num in nums[1:]:

            if num==first:
                continue

            if num<first:
                first = num

            elif second=='#':
                first = min(num,first)
                second = max(num,first)
            elif num<second:
                second = num
            elif num>second:
                return True

        return False
