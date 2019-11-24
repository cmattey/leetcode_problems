# Time: O(size(M)*~log(len(M))(inverseAckerman due to path compression))
# Space: O(len(M))

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        Solve using DSU.
        Number of dijoint connected components is the number of friend circles
        """

        dsu = {}


        for row in range(len(M)):
            for col in range(row, len(M[0])):        # since there can be 1 person friend groups (i.e friend with themselves), start col from row, instead of row+1
                if M[row][col]:
                    self.dsu_union(row, col, dsu)

        return len(set(self.dsu_parent(p, dsu) for p in dsu))


    def dsu_union(self, p1, p2, dsu):

        if p1 not in dsu:
            dsu[p1] = p1
        if p2 not in dsu:
            dsu[p2] = p2

        par1 = self.dsu_parent(p1, dsu)
        par2 = self.dsu_parent(p2, dsu)

        dsu[par1] = par2


    def dsu_parent(self, p1, dsu):

        if dsu[p1]!=p1:
            dsu[p1] = self.dsu_parent(dsu[p1], dsu)

        return dsu[p1]
