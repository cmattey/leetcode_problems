package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solveDay4("Day4_input.txt"))
}

func solveDay4(filename string) int {
	strs := helpers.ReadStr(filename)
	// requiredFields := map[string]bool{
	// 	"byr": true, "iyr": true, "eyr": true, "hgt": true, "hcl": true, "ecl": true,
	// 	"pid": true}

	fieldArr := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	ans1 := 0

	curRecord := []string{}
	for i, st := range strs {

		if len(st) != 0 {
			curRecord = append(curRecord, st)
		}

		if len(st) == 0 || i == len(strs)-1 {
			record := strings.Join(curRecord, " ")
			fields := getFields(record)
			accept := true
			for _, key := range fieldArr {
				if _, ok := fields[key]; !ok {
					accept = false
					break
				}
				pvalue, _ := fields[key]
				accept = validateRules(key, pvalue)
				if !accept {
					break
				}
			}

			if accept == true {
				ans1++
			}
			curRecord = []string{}
		}
	}

	return ans1
}

func validateRules(key, value string) bool {
	val := true
	switch key {
	case "byr":
		val = validateByr(value)
	case "iyr":
		val = validateIyr(value)
	case "eyr":
		val = validateEyr(value)
	case "hgt":
		val = validateHgt(value)
	case "hcl":
		val = validateHcl(value)
	case "ecl":
		val = validateEcl(value)
	case "pid":
		val = validatePid(value)
	}

	return val
}

func validatePid(value string) bool {
	if len(value) != 9 {
		return false
	}

	_, err := strconv.Atoi(value)

	if err != nil {
		return false
	}

	return true
}

func validateEcl(value string) bool {
	validClr := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

	found := helpers.Find(validClr, value)

	return found
}

func validateHcl(value string) bool {
	if string(value[0]) != "#" || len(value) != 7 {
		return false
	}

	validChars := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}

	for _, val := range value[1:] {
		found := helpers.Find(validChars, string(val))
		if !found {
			return false
		}
	}

	return true
}

func validateHgt(value string) bool {

	if !(value[len(value)-2:] == "cm" || value[len(value)-2:] == "in") {
		return false
	}

	if value[len(value)-2:] == "cm" {
		hg, err := strconv.Atoi(value[:len(value)-2])
		if err != nil {
			return false
		}

		if hg >= 150 && hg <= 193 {
			return true
		}
		return false
	}
	if value[len(value)-2:] == "in" {
		hg, err := strconv.Atoi(value[:len(value)-2])
		if err != nil {
			return false
		}

		if hg >= 59 && hg <= 76 {
			return true
		}
		return false
	}

	return false
}

func validateEyr(value string) bool {
	year, err := strconv.Atoi(value)

	if err != nil {
		return false
	}

	if year >= 2020 && year <= 2030 {
		return true
	}
	return false
}

func validateIyr(value string) bool {
	year, err := strconv.Atoi(value)

	if err != nil {
		return false
	}

	if year <= 2020 && year >= 2010 {
		return true
	}
	return false
}

func validateByr(value string) bool {

	year, err := strconv.Atoi(value)

	if err != nil {
		return false
	}

	if year <= 2002 && year >= 1920 {
		return true
	}

	return false
}

func getFields(record string) map[string]string {
	fields := make(map[string]string)

	keyVal := strings.Split(record, " ")
	for _, kv := range keyVal {
		field := strings.Split(kv, ":")[0]
		fields[field] = strings.Split(kv, ":")[1]
	}

	return fields

}
