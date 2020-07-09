package Go

import (
	"strconv"
)

func letterCombinations(digits string) []string {

	curComb := ""
	allComb := &[]string{}
	if len(digits) == 0 {
		return *allComb
	}

	numMap := map[int]string{2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

	phoneHelper(digits, 0, curComb, allComb, numMap)

	return *allComb

}

func phoneHelper(digits string, start int, curComb string, allComb *[]string, numMap map[int]string) {

	if start == len(digits) {
		*allComb = append(*allComb, curComb)
		return
	}
	num, _ := strconv.ParseInt(string(digits[start]), 10, 64)
	for _, ch := range numMap[int(num)] {
		phoneHelper(digits, start+1, curComb+string(ch), allComb, numMap)
	}
	return
}
