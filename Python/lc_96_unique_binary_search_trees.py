# Time: O(n^2)
# Space: O(n)

class Solution:
    def numTrees(self, n: int) -> int:

        """
        DP - Solution
        """
        memo = [-1]*(n+1)

        return self.util(n,memo)


    def util(self, n, memo):

        count = 0
        if n==0:
            return 1
        if n<=2:
            return n

        if memo[n]!=-1:
            return memo[n]

        for i in range(1, n+1):
            left = self.util(i-1, memo)
            right = self.util(n-i, memo)

            count+= left*right

        memo[n] = count
        return count


        """
        Recursive

        count = 0
        if n==0:
            return 1
        if n<=2:
            return n


        for i in range(1, n+1):
            left = self.numTrees(i-1)
            right = self.numTrees(n-i)

            count+= left*right

        return count
        """
    
