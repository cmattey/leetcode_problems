# 89. Gray Code
# Time: O(2^n)
# Space: O(n) excluding output result arr.
class Solution:
    def grayCode(self, n: int) -> List[int]:

        arr = ['0']*n

        result = [0]

        self.util(n, 0, result, arr)

        return result

    def util(self, n, pos, result, arr):

        if pos==n:
            return

        # result.append(int("".join(arr), 2))
        self.util(n, pos+1, result, arr)
        arr[pos] = '0' if arr[pos]=='1' else '1'
        result.append(int("".join(arr), 2))
        self.util(n, pos+1, result, arr)
