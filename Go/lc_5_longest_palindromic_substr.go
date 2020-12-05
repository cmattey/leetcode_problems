package Go

// Time: O(n^2)
// Space: O(n^2), can be reduced to O(1), by expanding around center approach
func longestPalindrome(s string) string {
	if s == "" {
		return ""
	}
	mat := make([][]bool, len(s))
	for i := 0; i < len(s); i++ {
		mat[i] = make([]bool, len(s))
		mat[i][i] = true

		if i+1 < len(s) && s[i] == s[i+1] {
			mat[i][i+1] = true
		}
	}

	max_len := 1
	pal := string(s[0])

	for st := len(s) - 2; st >= 0; st-- {
		for end := st + 1; end < len(s); end++ {

			if st < end && mat[st+1][end-1] && s[st] == s[end] {
				mat[st][end] = true
			}

			if mat[st][end] == true && end-st+1 > max_len {
				max_len = end - st + 1
				pal = string(s[st : end+1])
			}

		}
	}

	return pal

}
