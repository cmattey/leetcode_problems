package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
)

func main() {

	nums := helpers.ReadNums("day1_input.txt")

	var incr int
	var prev int
	for i := range nums {
		if i == 0 {
			prev = nums[i]
		} else {
			if nums[i] > prev {
				incr++
			}
		}

		prev = nums[i]
	}

	fmt.Println(incr)
	day1Part2()
}
