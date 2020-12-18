package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
	"sort"
)

func main() {
	// nums := helpers.ReadNums("day10_test_input.txt")
	nums := helpers.ReadNums("day10_input.txt")

	fmt.Println(part1(nums))
	fmt.Println(part2(nums))
}

func part2(nums []int) int {

	numSet := make(map[int]int)

	for _, v := range nums {
		numSet[v] = 0
	}

	sort.Ints(nums)

	numSet[0] = 1
	for _, v := range nums {
		numSet[v] = numSet[v-1] + numSet[v-2] + numSet[v-3]
	}

	return numSet[nums[len(nums)-1]]
}

func part1(nums []int) int {

	sort.Ints(nums)

	diff1 := 0
	diff3 := 0

	prev := 0
	for _, v := range nums {

		if v-prev == 1 {
			diff1++
		} else if v-prev == 3 {
			diff3++
		}

		prev = v
	}

	return diff1 * (diff3 + 1)
}
