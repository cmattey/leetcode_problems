package main

import (
	"fmt"
	"leetcode_problems/advent_code_2021/helpers"
	"strconv"
)

func mainBitsApproach() {

	bins := helpers.ReadStr("day3_input.txt")
	var gamma_rate string
	var epsilon_rate string

	num_bits := len(bins[0])

	for i := 0; i < num_bits; i++ {
		set_bits := 0
		for _, bin := range bins {

			if string(bin[i]) == "1" {
				set_bits++
			}
		}
		if set_bits > len(bins)/2 {
			gamma_rate += "1"
			epsilon_rate += "0"
		} else {
			gamma_rate += "0"
			epsilon_rate += "1"
		}
	}

	gr, _ := strconv.ParseInt(gamma_rate, 2, 64)
	er, _ := strconv.ParseInt(epsilon_rate, 2, 64)

	fmt.Println(gr * er)
}
