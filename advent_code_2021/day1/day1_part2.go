package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
)

func day1Part2() {

	nums := helpers.ReadNums("day1_input.txt")

	var incr int
	for i := range nums {
		if i == 0 || i == 1 || i == 2 {
			continue
		} else {
			if nums[i] > nums[i-3] {
				incr++
			}
		}
	}

	fmt.Println(incr)
}
