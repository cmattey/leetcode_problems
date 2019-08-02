# 210. Course Schedule II
# Time: O(V+E)
# Space: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        prereq_map = defaultdict(list)

        for course, pre_req in prerequisites:
            prereq_map[course].append(pre_req)


        visited = ["unvisited" for _ in range(numCourses)]

        order = []

        for course in range(numCourses):
            if not self.dfs(course, visited, prereq_map, order):
                return []

        return order


    def dfs(self, course, visited, prereq_map, order):

        if visited[course]=="under_progress":
            return False

        elif visited[course]=="done":
            return True

        elif visited[course]=="unvisited":
            visited[course] = "under_progress"

        for prereq in prereq_map[course]:
            if not self.dfs(prereq, visited, prereq_map, order):
                return False

        order.append(course)
        visited[course] = "done"

        return True
