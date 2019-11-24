# Time: O(V+E)
# Space: O(V+E)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        num_graph = collections.defaultdict(list)

        for (x,y),val in zip(equations, values):
            num_graph[x].append([y, val])
            num_graph[y].append([x,1/val])

        # print(num_graph)
        op = []
        for x,y in queries:
            # print("Inside", x, y)
            if x not in num_graph or y not in num_graph:
                op.append(-1.0)
                continue

            seen = set()
            count = self.dfs(num_graph, x, y, seen)
            op.append(count)

        return op

    def dfs(self, num_graph, x, y, seen):
        # print(x,y, seen)
        if x==y:
            return 1.0

        for neigh, conv_val in num_graph[x]:
            if neigh not in seen:
                seen.add(neigh)

                ret_val = self.dfs(num_graph, neigh, y, seen)

                if ret_val>-1.0:
                    return ret_val*conv_val


        return -1.0
