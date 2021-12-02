package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
	"strconv"
	"strings"
)

func part2() {

	info := helpers.ReadStr("day2_input.txt")

	var depth int
	var hPosition int
	var aim int

	for _, val := range info {

		switch {
		case strings.HasPrefix(val, "forward"):
			curH, _ := strconv.Atoi(val[8:])
			hPosition += curH
			depth += aim * curH
		case strings.HasPrefix(val, "down"):
			curD, _ := strconv.Atoi(val[5:])
			aim += curD
		case strings.HasPrefix(val, "up"):
			curD, _ := strconv.Atoi(val[3:])
			aim -= curD
		}
	}

	fmt.Println(depth * hPosition)
}
