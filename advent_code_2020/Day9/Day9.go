package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
)

func main() {
	fmt.Println(solveDay9Part1("Day9_input.txt"))
	// fmt.Println(solveDay9Part1("Day9_input_test.txt"))
}

func solveDay9Part1(filename string) int {
	preambleSize := 25
	// preambleSize := 5
	nums := helpers.ReadNums(filename)

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
