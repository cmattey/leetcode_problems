# Time: O(V+E), V=len(graph), E=edges in graph
# Space: O(V)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        dsu = {}

        for node in range(len(graph)):

            if node not in dsu:
                process_stack = [node]
                dsu[node] = 'A'

                while process_stack:
                    node = process_stack.pop()

                    for nei in graph[node]:
                        if nei not in dsu:
                            process_stack.append(nei)
                            dsu[nei] = 'B' if dsu[node]=='A' else 'A'
                        elif dsu[nei]==dsu[node]:
                            return False

        return True
                
