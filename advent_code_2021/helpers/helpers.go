package helpers

import (
	"bufio"
	"os"
	"strconv"
)

func ReadNums(filename string) []int {
	var nums []int

	file, _ := os.Open(filename)

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, i)
	}

	return nums
}

func ReadStr(filename string) []string {
	var info []string

	file, _ := os.Open(filename)

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i := scanner.Text()
		info = append(info, i)
	}

	return info
}
