package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
)

func main() {
	fmt.Println(SolveDay1("Day1_input.txt"))
}

// SolveDay1 solution for Day1
func SolveDay1(filename string) (int, int) {
	nums := helpers.ReadNums(filename)
	return twoSum2020(nums), threeSum2020(nums)
}

func twoSum2020(nums []int) int {

	numMap := make(map[int]bool)

	for _, num := range nums {

		if _, ok := numMap[2020-num]; ok {
			return num * (2020 - num)
		}

		numMap[num] = true
	}

	return -1
}

func threeSum2020(nums []int) int {

	for i, num1 := range nums {
		numMap := make(map[int]bool)
		for _, num2 := range nums[i+1:] {

			if _, ok := numMap[2020-num1-num2]; ok {
				return num1 * num2 * (2020 - num1 - num2)
			}

			numMap[num2] = true
		}
	}

	return -1
}
