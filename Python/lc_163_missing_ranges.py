# Oct 28th '19
# Time: O(n)
# Space: O(1)

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        nums = [lower-1]+nums+[upper+1]

        ranges = []
        index = 0

        while index<len(nums)-1:

            left = nums[index]
            right = nums[index+1]

            if left!=right-1:

                if right-left==2:
                    ranges.append(str(right-1))
                elif right-left>2:
                    temp_str = str(left+1)+"->"+str(right-1)
                    ranges.append(temp_str)

            index+=1

        return ranges


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        Memory limit exceeded for large values
        """
        overall = set(range(lower, upper+1))


        missing_vals = sorted(list(overall^set(nums)))

        ranges = []

        index = 0

        # print(missing_vals)
        while index<len(missing_vals):

            start = missing_vals[index]
            end = missing_vals[index]
            while index+1<len(missing_vals) and missing_vals[index+1]==end+1:
                end+=1
                index+=1

            if start==end:
                ranges.append(str(start))
            else:
                temp_str = str(start)+"->"+str(end)
                ranges.append(temp_str)

            index+=1

        return ranges
