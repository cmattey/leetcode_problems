# 60. Permutation Sequence
# Time: O(n)
# Space: O(n)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Recursively(or in while loop) get the first digit of the permutation,
        pop the element from arr, and update 'k' accordingly.

        Steps to get first digit:
        Index of first digit-
            1. k/(n-1)!

        first digit = num_arr[index]
        k = k- index*(n-1)!
        """


        num_arr = list(range(1,n+1))

        perm = []
        k-=1
        while num_arr:

            index = k//math.factorial(len(num_arr)-1)
            perm.append(str(num_arr[index]))

            num_arr.pop(index)
            k = k-(math.factorial(len(num_arr))*(index))

        return "".join(perm)
