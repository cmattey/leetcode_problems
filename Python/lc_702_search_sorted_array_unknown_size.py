# Time: O(logT)
# Space: O(1)

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        start, end = self.get_search_bounds(reader, target)

        while start<=end:

            mid = (start+end)//2

            cur_num = reader.get(mid)
            if cur_num==target:
                return mid
            elif cur_num>target:
                end = mid-1
            else:
                start = mid+1

        return -1

    def get_search_bounds(self, reader, target):

        start = 0
        end = 1

        while reader.get(end)<target:
            start = end
            end = end*2

        return [start, end]
