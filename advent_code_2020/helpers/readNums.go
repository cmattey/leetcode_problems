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

// ReadStr reads a new line separated file of strings
// and returns a slice of strings
func ReadStr(filename string) []string {
	var strs []string

	file, err := os.Open(filename)
	Check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		strs = append(strs, scanner.Text())
	}

	return strs
}

// Check checks for error, and panics if err not nil
func Check(e error) {
	if e != nil {
		panic(e)
	}
}

func Find(haystack []string, needle string) bool {

	for _, val := range haystack {
		if val == needle {
			return true
		}
	}

	return false
}
