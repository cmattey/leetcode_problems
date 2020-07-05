package Go

func romanToInt(s string) int {

	romMap := map[string]int{
		"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000,
	}

	i := 0
	ans := 0
	for i < len(s) {
		if i == len(s)-1 {
			ans += romMap[string(s[i])]
			i++
		} else {
			if val, ok := romMap[string(s[i])+string(s[i+1])]; ok {
				ans += val
				i += 2
			} else {
				ans += romMap[string(s[i])]
				i++
			}
		}
	}

	return ans

}
