package helpers

import (
	"bufio"
	"os"
	"strconv"
)

// ReadNums reads a new line separated file of integers
// and returns a slice of integers
func ReadNums(filename string) []int {

	var nums []int

	file, err := os.Open(filename)
	Check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, i)
	}

	return nums
}

// Check checks for error, and panics if err not nil
func Check(e error) {
	if e != nil {
		panic(e)
	}
}
