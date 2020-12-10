package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
)

func main() {
	fmt.Println(solveDay5("Day5_input.txt"))
	// fmt.Println(solveDay5("test_input.txt"))
}

func solveDay5(filename string) int {

	strs := helpers.ReadStr(filename)

	ans := 0
	seenRows := []int{}
	seenCols := []int{}
	for _, st := range strs {

		low, high := 0, 127
		left, right := 0, 7
		r, c := 0, 0
		for i, val := range st {
			if i < 7 {
				if string(val) == "F" {
					r = int((low + high) / 2)
					high = r
				} else {
					r = int((low+high)/2) + 1
					low = r
				}
			} else {
				if string(val) == "L" {
					c = int((left + right) / 2)
					right = c
				} else {
					c = int((left+right)/2) + 1
					left = c
				}
			}
		}
		seenRows = append(seenRows, r)
		seenCols = append(seenCols, c)
		// fmt.Println(r, c)
		curAns := r*8 + c
		// fmt.Println(curAns)
		ans = helpers.Max(ans, curAns)

	}

	return ans
}
