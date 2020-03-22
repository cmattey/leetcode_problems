# 207. Course Schedule
# Time: 2E + V
# Space: E + 2V
# Topological Sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections

        dep_map = collections.defaultdict(list)
        dep_count = collections.defaultdict(int)

        for dep, course in prerequisites:
            dep_map[course].append(dep)
            dep_count[dep]+=1

        indies = [course for course in range(numCourses) if course not in dep_count]

        indie_count = 0

        while indies:

            cur_course = indies.pop(0)

            for course in dep_map[cur_course]:
                dep_count[course]-=1
                if dep_count[course]==0:
                    del dep_count[course]
                    indies.append(course)

        if len(dep_count)>0:
            return False
        return True

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
