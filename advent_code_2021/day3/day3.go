package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
	"math"
	"strconv"
)

func main() {
	fmt.Println("vim-go")

	nums := helpers.ReadStr("day3_input.txt")

	var gammaRate string
	var epsilonRate string

	for i := 0; i < len(nums[0]); i++ {
		var numZero int
		var numOne int
		for _, num := range nums {

			strBit := string(num[i])
			if strBit == "1" {
				numOne++
			} else {
				numZero++
			}
		}
		if numOne > numZero {
			gammaRate += "1"
			epsilonRate += "0"
		} else {
			gammaRate += "0"
			epsilonRate += "1"
		}
	}

	gR := binToInt(gammaRate)
	eR := binToInt(epsilonRate)
	fmt.Println(gR, eR, gammaRate, epsilonRate)
	fmt.Println(gR * eR)
	mainBitsApproach()
	day3Part2()
}

func binToInt(bin string) int {
	var pow float64

	l := len(bin)

	var num float64
	for i := l - 1; i >= 0; i-- {
		bitInt, _ := strconv.Atoi(string(bin[i]))
		num += math.Pow(float64(2), pow) * float64(bitInt)
		pow++
	}

	return int(num)
}
