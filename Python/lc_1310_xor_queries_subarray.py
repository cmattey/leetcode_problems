# LC Contest 170
# Time: O(n+m), n=len(arr), m= len(queries)
# Space: O(n), O(1) excluding output

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        cum_arr = [0]

        for i in range(len(arr)):
            cum_arr.append(cum_arr[i]^arr[i])

        # print(cum_arr)
        output = []
        for l,r in queries:
            output.append(cum_arr[r+1]^cum_arr[l])

        return output
