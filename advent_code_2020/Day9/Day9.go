package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
)

func main() {
	// nums := helpers.ReadNums("Day9_input.txt")
	testNums := helpers.ReadNums("Day9_input_test.txt")
	// fmt.Println(solveDay9Part1(nums))
	// fmt.Println(solveDay9Part2(nums))
	fmt.Println(solveDay9Part2(testNums))
	// fmt.Println(solveDay9Part1("Day9_input_test.txt"))
}

func solveDay9Part1(nums []int) int {
	// preambleSize := 25
	preambleSize := 5
	numMap := make(map[int]int)
	for _, v := range nums[:preambleSize] {
		numMap[v]++
	}

	for i, num := range nums[preambleSize:len(nums)] {
		found := false
		for k := range numMap {
			if _, ok := numMap[num-k]; ok {
				found = true
				break
			}
		}
		if !found {
			return num
		}

		numToRemove := nums[i]
		numMap[numToRemove]--
		if numMap[numToRemove] == 0 {
			delete(numMap, numToRemove)
		}
		numMap[num]++
	}

	return -1
}

func solveDay9Part2(nums []int) int {

	target := solveDay9Part1(nums)

	rangeStart := 0
	index := rangeStart
	numSlice := make([]int, 0)
	curSum := 0
	for index < len(nums) {
		curSum += nums[rangeStart]
		numSlice = append(numSlice, nums[index])
		if curSum > target {
			rangeStart++
			index = rangeStart
			curSum = 0
			numSlice = make([]int, 0)
		} else if curSum == target {
			fmt.Println(numSlice)
			break
			// ans := computeAns(numSlice)
		} else {
			index++
		}
	}

	return -1
}
