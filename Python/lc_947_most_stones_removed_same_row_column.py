# Time: O(https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity) According to wikipedia for DSU with only
# path compression
# Space: O(N)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Find connected components
        Num moves for each component would be, size(component)-1
        In other words. Total moves = num_stone-num_components

        We can build components using dsu, with each col(represented as ~j (-j-1) so as not to be confused with the rows)
        being connected to the row,where a point exists.
        - Therefore, parent(col) = row if [row,col] point contains a stone
        """

        dsu = DSU()

        for x,y in stones:
            dsu.dsu_union(x,~y)

        return len(stones) - len({dsu.dsu_parent(~y) for x,y in stones})

class DSU:

    def __init__(self):
        self.parent = {}

    def dsu_parent(self, x):

        if x!=self.parent[x]:
            self.parent[x] = self.dsu_parent(self.parent[x])

        return self.parent[x]


    def dsu_union(self, x, y):

        if x not in self.parent:
            self.parent[x] = x
        if y not in self.parent:
            self.parent[y] = y


        par_x = self.dsu_parent(x)
        par_y = self.dsu_parent(y)
        self.parent[par_y] = par_x

        # print(self.parent)
        return
