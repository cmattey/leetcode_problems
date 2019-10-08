# Time: O(R^2) ~O(1), since max R = 99
# Space: O(R) ~O(1)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        cur_row = [poured]

        for i in range(1,query_row+1):
            new_row = [0]*(len(cur_row)+1)
            for index, val in enumerate(cur_row):
                new_row[index]+= max(0,(cur_row[index]-1)/2)
                new_row[index+1]+= max(0,(cur_row[index]-1)/2)

            cur_row = new_row

        return min(cur_row[query_glass],1)
