package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
)

const (
	occupied = "#"
	empty    = "L"
	floor    = "."
)

func main() {
	input := helpers.ReadStr("day11_input.txt")
	// input := helpers.ReadStr("day11_test_input.txt")

	fmt.Println(solveDay11Part1(input))
	// fmt.Println(solveDay11Part2(input))
}

func solveDay11Part1(strs []string) int {

	hasChanged := true

	for hasChanged {
		tempBoard := make([]string, len(strs))
		hasChanged = false

		for i := range strs {
			tempBoard[i] = calcNewState(strs, i)
			if tempBoard[i] != strs[i] {
				hasChanged = true
			}
		}

		strs = tempBoard
	}
	return countOccupied(strs)
}

func countOccupied(strs []string) int {

	count := 0
	for _, str := range strs {

		for _, ch := range str {
			if string(ch) == occupied {
				count++
			}
		}
	}
	return count
}

func calcNewState(strs []string, row int) string {

	dirs := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}}
	rowCopy := make([]byte, len(strs[row]))
	for col, ch := range strs[row] {
		if string(ch) == floor {
			rowCopy[col] = []byte(floor)[0]
			continue
		}
		numOccupied := 0
		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]

			if row+dr >= 0 && col+dc >= 0 && row+dr < len(strs) && col+dc < len(strs[0]) {
				if string(strs[row+dr][col+dc]) == occupied {
					numOccupied++
				}
			}
		}

		if numOccupied >= 4 {
			rowCopy[col] = []byte(empty)[0]
		} else if numOccupied == 0 {
			rowCopy[col] = []byte(occupied)[0]
		} else {
			rowCopy[col] = []byte(string(ch))[0]
		}
	}

	return string(rowCopy)
}
