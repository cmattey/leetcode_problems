# Time: O(n^2), where n=numRows
# Space: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pas_tri = []

        for i in range(numRows):
            if i==0:
                pas_tri.append([1])
            elif i==1:
                pas_tri.append([1,1])
            else:
                cur_row = [1]

                for index in range(len(pas_tri[i-1])-1):
                    cur_row.append(pas_tri[i-1][index]+pas_tri[i-1][index+1])
                cur_row.append(1)

                pas_tri.append(cur_row)

        return pas_tri



        
