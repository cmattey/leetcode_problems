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

# Oct 27th '19
# Time: ~O(1), due to path compression, ackerman number to be precise
# Space: O(N)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Order of removals matters, but we don't have to find the order, just the count of moves.
        - We can always find an order such that # [size(component)-1] stones can be removed.


        Key observation:
        - Stones which share a row or column for a component
        - Find connected components, the number of moves will be size of component -1. Do this for all components.

        Calculate connected components using Disjoint set units.

        If i store rows as nodes
        - need unique way to store columns. can store ~col = -col-1. or store them beyond range of rows.
        """

        dsu = {}

        for x,y in stones:

            if x not in dsu:
                dsu[x] = x
            if ~y not in dsu:
                dsu[~y] = ~y

            par_x = self.parent(dsu, x)
            par_y = self.parent(dsu, ~y)

            dsu[par_y] = par_x

        # print(dsu)
        return len(stones) - len(set(self.parent(dsu, x[0]) for x in stones))


    def parent(self, dsu, x):

        if dsu[x]!=x:
            dsu[x] = self.parent(dsu, dsu[x])

        return dsu[x]
