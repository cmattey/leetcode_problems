# Time: O(1)
# Space: O(1)
# Better solution to expand to K vectors

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cur_pos = 0
        self.arrs = [v1,v2]

    def next(self):
        """
        :rtype: int
        """
        if len(self.arrs[self.cur_pos])==0:
            self.cur_pos = 0 if self.cur_pos else 1

        ret_val = self.arrs[self.cur_pos].pop(0) # can use dequeu lib and use pop_left for O(1) time popping
        self.cur_pos = 0 if self.cur_pos else 1

        return ret_val

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.arrs[0])>0 or len(self.arrs[1])>0:
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
