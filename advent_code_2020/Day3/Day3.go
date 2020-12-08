package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
)

func main() {
	matrix := helpers.ReadStr("Day3_input.txt")
	fmt.Println(solveDay3(matrix, 1, 3))

	part2Slopes := [][]int{{1, 1}, {1, 3}, {1, 5}, {1, 7}, {2, 1}}

	ans2 := 1
	for _, slope := range part2Slopes {
		slopeR := slope[0]
		slopeC := slope[1]

		ans2 *= solveDay3(matrix, slopeR, slopeC)
	}

	fmt.Println(ans2)
}

func solveDay3(matrix []string, slopeR int, slopeC int) int {

	ans1 := 0

	row := 0
	col := 0
	for {
		if row >= len(matrix) {
			break
		}

		if col >= len(matrix[row]) {
			col = col % len(matrix[row])
		}

		if string(matrix[row][col]) == "#" {
			ans1++
		}

		row += slopeR
		col += slopeC
	}

	return ans1
}
