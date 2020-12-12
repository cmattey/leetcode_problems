package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solveDay8Part1("Day8_input.txt"))
	// fmt.Println(solveDay8Part1("Day8_test_input.txt"))
}

func solveDay8Part1(filename string) int {

	strs := helpers.ReadStr(filename)

	seenMap := make(map[int]bool)
	curIndex := 0
	acc := 0
	for {

		if _, ok := seenMap[curIndex]; ok {
			break
		}
		seenMap[curIndex] = true

		st := strs[curIndex]

		cmd := strings.Split(st, " ")[0]
		num, _ := strconv.Atoi(strings.Split(st, " ")[1])

		if cmd == "nop" {
			curIndex++
		} else if cmd == "acc" {
			curIndex++
			acc += num
		} else {
			curIndex += num
		}
	}

	return acc
}
