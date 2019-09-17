# Time: O(len(numbers))
# Space: O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """


        start = 0
        end = len(numbers)-1

        while start<end:

            cur_num = numbers[start]+numbers[end]
            if cur_num==target:
                return [start+1,end+1]
            elif cur_num>target:
                end-=1
            else:
                start+=1

        return None
