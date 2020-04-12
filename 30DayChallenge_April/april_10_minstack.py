# push: O(1)
# pop: O(1)
# top: O(1)
# getMin: O(1)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')


    def push(self, x: int) -> None:
        if x<self.min:
            self.min = x

        self.stack.append([x,self.min])


    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = float('inf')


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
