# Time: O(|E|), where |E| =  # of edges in graph
# Space: O(|V|), where |V| = # of vertices in graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        node_map = {}

        if not node:
            return None

        self.dfs(node, node_map, None)

        return node_map[node]


    def dfs(self, cur_start, node_map, parent):

        if cur_start in node_map:
            return

        else:
            node_map[cur_start] = Node(cur_start.val,[])
            for neighbor in cur_start.neighbors:
                self.dfs(neighbor, node_map, cur_start)
                node_map[cur_start].neighbors.append(node_map[neighbor])










        
