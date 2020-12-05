package epi

// Brute Force
func parity(x int) int {
	result := 0
	for x > 0 {
		// last_bit := x%10
		result = result ^ (x & 1)
		x >>= 1
	}

	return result
}
