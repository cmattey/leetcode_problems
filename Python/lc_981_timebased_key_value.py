# Time: set = O(1), get = O(logn)
# Space: O(n)

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections

        self.imap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.imap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.imap:
            return ""

        values = self.imap[key]

        left = 0
        right = len(values)-1

        ans = ""
        while left<=right:

            mid = (left+right)//2

            if values[mid][0]<=timestamp:
                ans = values[mid][1]
                left = mid+1
            else:
                right = mid-1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.imap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.imap:
            # values = self.imap[key]
            # bisect.insort_left(values,[timestamp,value])
            # self.imap[key] = values
            self.imap[key].append([timestamp,value]) # no need to do bisect.insort since set is called in incrementing order of timestamp.
        else:
            self.imap[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.imap:
            return ""
        values = self.imap[key]

        # insert_index = bisect.bisect_right(values, [timestamp,values[-1][1]]) # need to put value as max char, and not value of last thing in map
        insert_index = bisect.bisect_right(values, [timestamp,chr(127)]) # since chr(127) is higher than any char, z=122

        if insert_index==0:
            return ""
        else:
            return values[insert_index-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
