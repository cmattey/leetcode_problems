package main

import (
	"fmt"
	"leetcode_problems/advent_code_2020/helpers"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solveDay2("Day2_input.txt"))
}

// SolveDay2 solution for Day2
func solveDay2(filename string) (int, int) {

	strs := helpers.ReadStr(filename)
	ans1 := 0
	ans2 := 0
	for _, st := range strs {

		low, high, char, pw := parse(st)
		if isValid(low, high, char, pw) {
			ans1++
		}

		if isValidNew(low, high, char, pw) {
			ans2++
		}
	}
	return ans1, ans2

}

func isValidNew(pos1, pos2 int, char, pw string) bool {

	count := 0

	if pos1 > 0 && pos2 <= len(pw) {

		if string(pw[pos1-1]) == char {
			count++
		}

		if string(pw[pos2-1]) == char {
			count++
		}
	}

	if count == 1 {
		return true
	}

	return false
}

func isValid(low, high int, char, pw string) bool {

	count := 0
	for _, ch := range pw {

		if string(ch) == char {
			count++
		}
		if count > high {
			return false
		}
	}

	if count < low {
		return false
	}

	return true
}

func parse(st string) (int, int, string, string) {

	s := strings.Split(st, " ")

	// parse low, high
	r := strings.Split(s[0], "-")
	low, _ := strconv.Atoi(r[0])
	high, _ := strconv.Atoi(r[1])

	// parse ch
	ch := s[1][0]

	// parse pw

	pw := s[2]

	return low, high, string(ch), pw
}
