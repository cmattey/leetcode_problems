package Go

// Topological Sort solution
// Time Complexity: O(V+2E)
func canFinish(numCourses int, prerequisites [][]int) bool {

	deps := make(map[int][]int)
	numDeps := make(map[int]int)
	for _, val := range prerequisites {
		course := val[0]
		dep := val[1]

		if _, ok := deps[dep]; !ok {
			deps[dep] = []int{}
		}
		deps[dep] = append(deps[dep], course)
		numDeps[course]++
	}

	topSortStack := []int{}

	for i := 0; i < numCourses; i++ {
		if numDeps[i] == 0 {
			topSortStack = append(topSortStack, i)
		}
	}

	for len(topSortStack) > 0 {
		curCourse := topSortStack[len(topSortStack)-1]
		topSortStack = topSortStack[:len(topSortStack)-1]

		for _, course := range deps[curCourse] {
			numDeps[course] = numDeps[course] - 1
			if numDeps[course] == 0 {
				delete(numDeps, course)
				topSortStack = append(topSortStack, course)
			}
		}
	}

	if len(numDeps) > 0 {
		return false
	}
	return true
}

// Identifying cyclic dependancy solution
// Time Complexity: O(V+E)
func canFinishTopological(numCourses int, prerequisites [][]int) bool {

	deps := make(map[int][]int)

	for _, v := range prerequisites {

		course, dep := v[0], v[1]

		if _, ok := deps[course]; !ok {
			deps[course] = []int{}
		}
		deps[course] = append(deps[course], dep)
	}

	for i := 0; i < numCourses; i++ {

		if _, ok := deps[i]; !ok {
			continue
		}

		for _, val := range deps[i] {

			tempMap := make(map[int]string)

			if !traverse(deps, val, tempMap) {
				return false
			}
		}
	}

	return true
}

func traverse(deps map[int][]int, cur int, trackMap map[int]string) bool {

	if val, ok := trackMap[cur]; ok {
		if val == "in_progress" {
			return false
		}
		return true
	}

	trackMap[cur] = "in_progress"

	for _, v := range deps[cur] {

		if !traverse(deps, v, trackMap) {
			return false
		}
	}

	trackMap[cur] = "done"

	return true
}
