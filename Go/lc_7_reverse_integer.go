package Go

// Time: O(logn) base 10
// Space: O(1)
func reverse(x int) int {
	isNeg := false
	if x < 0 {
		isNeg = true
		x = -x
	}

	ans := 0
	for x > 0 {
		ans = ans*10 + x%10
		x = x / 10

	}

	if isNeg {
		ans = -ans
		if ans < (-1 * (1 << 31)) {
			return 0
		}
		return ans
	}

	if ans > 1<<31 {
		return 0
	}
	return ans

}
