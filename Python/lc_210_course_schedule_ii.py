# Nov 16th '19
# Time: O(numCourses)
# Space: O(numCourses)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological Sort Solution
        """

        dep_map = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        for dep, course in prerequisites:
            dep_map[course].append(dep)
            in_degree[dep]+=1

        # print(in_degree)
        indies = [course for course in range(numCourses) if course not in in_degree]
        # print(indies)
        order = []
        while indies:
            cur_course = indies.pop(0)
            # print(cur_course)
            order.append(cur_course)

            for course in dep_map[cur_course]:
                in_degree[course]-=1
                if in_degree[course]==0:
                    indies.append(course)

        return order if len(order)==numCourses else []


        """
        DFS solution
        """

        dep_map = collections.defaultdict(list)

        for dep, course in prerequisites:
            dep_map[dep].append(course)

        visited = ["unvisited" for _ in range(numCourses)]

        order = []
        for course in range(numCourses):

            if not self.dfs(course, dep_map, order, visited):
                return []

        return order

    def dfs(self, course, dep_map, order, visited):

        if visited[course]=="in-progress":
            return False
        elif visited[course]=="done":
            return True

        visited[course]="in-progress"

        for dep in dep_map[course]:
            if not self.dfs(dep, dep_map, order, visited):
                return False

        order.append(course)
        visited[course] = "done"
        return True

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
