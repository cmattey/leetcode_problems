package Go

// Without updating input grid

func numIslands(grid [][]byte) int {

	visited := make(map[[2]int]bool)

	num_islands := 0
	for r := range grid {
		for c := range grid[0] {

			if grid[r][c] == byte('1') && !visited[[2]int{r, c}] {
				num_islands += 1
				dfs(grid, r, c, visited)
			}
		}
	}

	return num_islands
}

func dfs(grid [][]byte, r, c int, m map[[2]int]bool) {
	dirs := [][2]int{{0, 0}, {0, -1}, {0, 1}, {1, 0}, {-1, 0}}

	if !isValid(r, c, grid) {
		return
	}

	m[[2]int{r, c}] = true
	for _, dir := range dirs {
		if !m[[2]int{r + dir[0], c + dir[1]}] {
			dfs(grid, r+dir[0], c+dir[1], m)
		}
	}
}

func isValid(r, c int, grid [][]byte) bool {
	if r < 0 || c < 0 {
		return false
	}

	if r >= len(grid) || c >= len(grid[0]) {
		return false
	}

	if grid[r][c] != byte('1') {
		return false
	}

	return true
}
