# 207. Course Schedule
# Time: O(V+E) vertices + edges
# Space: O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        prereq_map = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited = ["unvisited" for _ in range(numCourses)]

        for cur_course in range(numCourses):

            if not self.dfs(cur_course, visited, prereq_map):
                return False

        return True


    def dfs(self, cur_course, visited, prereq_map):

        if visited[cur_course]=="under_progress":
            # We hit a course that hasn't been completed, hence there's a loop, i.e a course is dependant on itself for completion
            return False
        elif visited[cur_course]=="done":
            return True
        else:
            visited[cur_course] = "under_progress"

        for prereq in prereq_map[cur_course]:
            if not self.dfs(prereq, visited, prereq_map):
                return False

        visited[cur_course]="done"
        return True
