package Go

import (
	"strconv"
	"strings"
)

func myAtoi(str string) int {

	str = strings.TrimSpace(str)

	if len(str) == 0 {
		return 0
	}

	var output []string

	if str[0] == '-' || str[0] == '+' {
		output = append(output, string(str[0]))
		str = str[1:]
	}

	nums := "0123456789"

	for _, ch := range str {
		if ch == rune(' ') || !strings.Contains(nums, string(ch)) {
			break
		}

		output = append(output, string(ch))

	}

	o, _ := strconv.ParseInt(strings.Join(output, ""), 10, 64)

	if o < (-1 * (1 << 31)) {
		return -1 * 1 << 31
	}

	if o > 1<<31-1 {
		return 1<<31 - 1
	}

	return int(o)
}
