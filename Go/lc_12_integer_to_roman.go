package Go

import (
	"strings"
)

func intToRoman(num int) string {

	romMap := map[int]string{
		1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M",
	}

	vals := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

	var ans []string

	for num > 0 {
		for _, rom := range vals {
			for num-rom >= 0 {
				ans = append(ans, romMap[rom])
				num -= rom
			}
		}
	}

	return strings.Join(ans, "")
}
