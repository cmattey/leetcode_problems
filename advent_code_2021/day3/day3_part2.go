package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
	"strconv"
)

func day3Part2() {

	bins := helpers.ReadStr("day3_input.txt")

	//o2 calculation
	var binsSatisfied []string
	binsSatisfied = bins
	for i := 0; len(binsSatisfied) > 1; i++ {

		newBins := []string{}
		bit := mostCommon(binsSatisfied, i)

		for _, bin := range binsSatisfied {
			if string(bin[i]) == bit {
				newBins = append(newBins, bin)
			}
		}
		binsSatisfied = newBins
	}

	o2 := binsSatisfied[0]
	binsSatisfied = bins
	for i := 0; len(binsSatisfied) > 1; i++ {
		newBins := []string{}
		bit := leastCommon(binsSatisfied, i)
		for _, bin := range binsSatisfied {
			if string(bin[i]) == bit {
				newBins = append(newBins, bin)
			}
		}
		binsSatisfied = newBins
	}
	co2 := binsSatisfied[0]
	gr, _ := strconv.ParseInt(o2, 2, 64)
	er, _ := strconv.ParseInt(co2, 2, 64)

	fmt.Println(gr * er)
}

func mostCommon(strs []string, pos int) string {
	var ones int
	var zeros int
	for _, str := range strs {
		if string(str[pos]) == "1" {
			ones++
		} else {
			zeros++
		}
	}

	if ones >= zeros {
		return "1"
	}
	return "0"
}

func leastCommon(strs []string, pos int) string {
	var ones int
	var zeros int
	for _, str := range strs {
		if string(str[pos]) == "1" {
			ones++
		} else {
			zeros++
		}
	}

	if ones < zeros {
		return "1"
	}
	return "0"
}
