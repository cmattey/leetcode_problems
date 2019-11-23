# Time: init:O(len(nums)), update: O(logn), sumRange: O(logn)
# Space: init:O(len(nums)), update: O(1), sumRange: O(1)

class NumArray:

    def __init__(self, nums: List[int]):

        self.n = len(nums)
        self.arr = [None]*(2*self.n-1)

        last_row_index = 0
        for index in range(self.n-1, 2*self.n-1):
            self.arr[index] = nums[last_row_index]
            last_row_index+=1

        for index in range(self.n-2,-1,-1):
            self.arr[index] = self.arr[index*2+1] + self.arr[index*2+2]

        # print(self.arr)

    def update(self, i: int, val: int) -> None:

        i = self.n+i-1

        diff = val-self.arr[i]
        while i>=0:
            self.arr[i]+=diff

            if i%2==0:
                i = i//2-1
            else:
                i = i//2

        # print(self.arr)

    def sumRange(self, i: int, j: int) -> int:

        i = self.n+i-1
        j = self.n+j-1

        cur_sum = 0
        while i<=j:
            # print(i,j)
            if i%2==0:
                cur_sum+=self.arr[i]
                i+=1
            if j%2==1:
                cur_sum+=self.arr[j]
                j-=1

            i = i//2
            j = j//2-1


        return cur_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
