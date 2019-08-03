# 413. Arithmetic Slices
# Time: O(n)
# Space: O(1)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Solved using brute force, doing linear time DP solution here
        """

        if len(A)<3:
            return 0

        prev = 0
        count = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                prev = 1+prev
                count +=prev
            else:
                prev = 0

        return count


        """
        Brute-Force by calculating through
        valid_subsets = [[]]
        count_arith_slices = 0

        for i in range(len(A)):
            mini_set = [A[i]]

            for j in range(i+1,len(A)):
                mini_set.append(A[j])
                valid_subsets.append(mini_set[:])

                if len(mini_set)>2:

                    diff = mini_set[1]-mini_set[0]
                    index = 1

                    while index<len(mini_set):
                        if mini_set[index]-mini_set[index-1]!=diff:
                            break
                        index+=1

                    if index==len(mini_set):
                        count_arith_slices+=1
                    else:
                        break

        return count_arith_slices
        """
