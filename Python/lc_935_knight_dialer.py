# Time: O(n)
# Space: O(1)

class Solution:

    def knightDialer(self, N: int) -> int:
        """
        Iterative solution passes larger test cases
        """

        num_map = {1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3],9:[2,4], 0:[6,4]}

        prev_count = [1]*10

        for i in range(N-1):
            cur_count = [0]*10
            for num in range(10):
                for nei in num_map[num]:
                    cur_count[num] += prev_count[nei]

            prev_count = cur_count


        return sum(prev_count)%(10**9 + 7)


# Time: O(n)
# Space: O(n)

class Solution:

    def knightDialer(self, N: int) -> int:
        """
        TLE for very large input (4942)
        """

        memo = {}

        num_map = {1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3],9:[2,4], 0:[6,4]}

        total = 0
        for i in range(10):
            total+=self.dfs(N-1,num_map, i, memo)

        return total%(10**9 + 7)

    def dfs(self, N, num_map, start, memo):

        if (start, N) in memo:
            return memo[(start, N)]

        if N==0:
            return 1

        temp = 0
        for nei in num_map[start]:
             temp += self.dfs(N-1, num_map, nei, memo)

        memo[(start, N)] = temp%(10**9 + 7)
        return temp
