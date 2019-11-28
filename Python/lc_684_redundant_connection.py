# Nov 25th '19
# O(~N), ~O(n*(ack(N))) inverse Ackerman function
# O(N)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = {}
        rank = collections.defaultdict(int)

        for p1, p2 in edges:

            par1 = self.dsu_parent(p1, dsu, rank)
            par2 = self.dsu_parent(p2, dsu, rank)

            if par1==par2:
                return [p1, p2]

            self.dsu_union(p1, p2, dsu, rank)




    def dsu_union(self, p1, p2, dsu, rank):

        par1 = self.dsu_parent(p1, dsu, rank)
        par2 = self.dsu_parent(p2, dsu, rank)

        if rank[par1]>=rank[par2]:
            dsu[par2] = par1
        elif rank[par1]<rank[par2]:
            dsu[par1] = par2

    def dsu_parent(self, p1, dsu, rank):

        if p1 not in dsu:
            dsu[p1] = p1
            rank[p1] = 1

        if dsu[p1]!=p1:
            dsu[p1] = self.dsu_parent(dsu[p1], dsu, rank)

        return dsu[p1]



# Time: ~O(n). Haven't used union by rank in dsu yet
# Space: O(n) self.sets in dsu implementation

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Dis-joint set implementation using union by rank, and path compression

        Note: While initializing sets, need to initialize the parent values to
        themselves, instead of -1, since now we are compressing tree, and parent
        return `self.sets[element]`, instead of `element` like in the implementation
        we did in DSU without compression.
        """
        dsu = DSU(10001)

        for edge in edges:
            if not dsu.union(edge[0],edge[1]):
                return edge

class DSU:

    def __init__(self, N):
        self.sets = [[-1,1]]*N # 0-index: parent, 1-index: rank
        self.sets = list(range(N)) # need to use initial parent value = index instead of -1
        self.rank = [1]*N
        # print(self.sets)

    def parent(self, element):
        # print(element)
        if self.sets[element]!=element:
            self.sets[element] = self.parent(self.sets[element])

        return self.sets[element]

    def union(self, el1, el2):

        par1 = self.parent(el1)
        par2 = self.parent(el2)

        if par1==par2:
            return False

        if self.rank[par1]>self.rank[par2]:
            self.sets[par2] = par1
            self.rank[par1]+=self.rank[par2]

        elif self.rank[par1]<self.rank[par2]:
            self.sets[par1] = par2
            self.rank[par2]+=self.rank[par1]

        if self.rank[par1]==self.rank[par2]:
            self.rank[par1]+=self.rank[par2]
            self.sets[par2] = par1

        return True


# Time: O(n^2). Haven't used union by rank in dsu yet
# Space: O(n) self.sets in dsu implementation

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Dis-joint set unit solution, without union by rank and path compression
        """
        dsu = DSU(10001)

        for edge in edges:
            if not dsu.union(edge[0],edge[1]):
                return edge

class DSU:

    def __init__(self, N):
        self.sets = [-1]*N

    def parent(self, element):

        if self.sets[element]!=-1:
            return self.parent(self.sets[element])

        return element

    def union(self, el1, el2):

        par1 = self.parent(el1)
        par2 = self.parent(el2)

        if par1==par2:
            return False

        self.sets[par2] = par1
        return True




# Time: O(n^2)
# Space: O(n)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        If adding a node leads to a loop, return that edge
        Using DFS O(n^2) time
        """
        from collections import defaultdict

        graph = defaultdict(list)


        for source, target in edges:
            seen = set()
            if self.dfs(seen,graph, source, target):
                return [source, target]

            graph[source].append(target)
            graph[target].append(source)

    def dfs(self, seen, graph, source, target):

        if source==target:
            return True

        if source in seen:
            return False

        seen.add(source)
        for neighbor in graph[source]:

            if self.dfs(seen, graph, neighbor, target):
                return True
