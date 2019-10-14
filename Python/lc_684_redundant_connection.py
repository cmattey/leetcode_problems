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
