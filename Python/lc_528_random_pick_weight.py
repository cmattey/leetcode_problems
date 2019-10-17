# Time: init: O(n), pickIndex: O(log(n))
# Space: O(n)

class Solution:

    def __init__(self, w: List[int]):

        self.cum_sum = [w[0]]

        for i in range(1, len(w)):
            self.cum_sum.append(w[i]+self.cum_sum[i-1])

        self.max = self.cum_sum[-1]

    def pickIndex(self) -> int:
        import random

        choice = random.randint(1,self.max)

        start = 0
        end = len(self.cum_sum)-1

        index = -1
        while start<=end:

            mid = (start+end)//2
            if choice==self.cum_sum[mid]:
                index = mid
                break
            elif choice<self.cum_sum[mid]:
                end = mid-1
            else:
                start = mid+1

        if index==-1:
            index = start

        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
