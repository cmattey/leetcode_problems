# Time: O(n),n = num of columns
# Space: O(1), except output

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        op_mat = [[],[]]
        for index in range(len(colsum)):
            if colsum[index]==2:
                if upper>0 and lower>0:
                    op_mat[0].append(1)
                    op_mat[1].append(1)
                    upper-=1
                    lower-=1
                else:
                    return []
            elif colsum[index]==1:
                if upper>lower:
                    if upper>0:
                        op_mat[0].append(1)
                        op_mat[1].append(0)
                        upper-=1
                    else:
                        return []

                else:
                    if lower>0:
                        op_mat[0].append(0)
                        op_mat[1].append(1)
                        lower-=1
                    else:
                        return []
            else:
                op_mat[0].append(0)
                op_mat[1].append(0)

        return op_mat if (upper==0 and lower==0) else []
