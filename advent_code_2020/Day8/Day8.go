package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solveDay8Part1("Day8_input.txt"))
	fmt.Println(solveDay8Part2("Day8_input.txt"))
	// fmt.Println(solveDay8Part1("Day8_test_input.txt"))
	// fmt.Println(solveDay8Part2("Day8_test_input.txt"))
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

func solveDay8Part2(filename string) int {
	strs := helpers.ReadStr(filename)

	for i, st := range strs {

		cmd := strings.Split(st, " ")[0]
		num, _ := strconv.Atoi(strings.Split(st, " ")[1])

		if cmd == "jmp" || cmd == "nop" {
			prev := cmd
			strs[i] = flip(cmd) + " " + strconv.Itoa(num)

			found, newAcc := isValid(strs)
			if found {
				return newAcc
			}
			strs[i] = prev + " " + strconv.Itoa((num))
		}
	}

	return -1
}

func flip(st string) string {
	if st == "jmp" {
		return "nop"
	}
	return "jmp"
}

func isValid(strs []string) (bool, int) {

	seenMap := make(map[int]bool)
	curIndex := 0
	acc := 0
	for {

		if curIndex == len(strs) {
			return true, acc
		}
		if _, ok := seenMap[curIndex]; ok {
			return false, -1
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
}
