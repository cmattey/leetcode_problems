# Time: O(n^2)
# Space: O(n)

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []


    def book(self, start: int, end: int) -> bool:

        for i,j in self.overlaps:
            if start<j and i<end:
                return False

        for i,j in self.calendar:
            if start<j and i<end:
                self.overlaps.append([max(start,i),min(end,j)])

        self.calendar.append([start,end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
