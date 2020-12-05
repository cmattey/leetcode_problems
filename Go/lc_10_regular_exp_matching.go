package Go

func isMatch(s string, p string) bool {

	m := make(map[Pair]bool)

	return dp(0, 0, m, s, p)
}

func dp(i int, j int, m map[Pair]bool, s string, p string) bool {

	var ans bool
	val, ok := m[Pair{i, j}]

	if ok {
		return val
	}

	if len(p) == j {
		m[Pair{i, j}] = i == len(s)
		return m[Pair{i, j}]
	}

	first_match := i < len(s) && contains([]string{".", string(s[i])}, string(p[j]))

	if j+1 < len(p) && string(p[j+1]) == "*" {
		ans = dp(i, j+2, m, s, p) || first_match && dp(i+1, j, m, s, p)
	} else {
		ans = first_match && dp(i+1, j+1, m, s, p)
	}

	m[Pair{i, j}] = ans

	return m[Pair{i, j}]
}

func contains(sl []string, s string) bool {
	for _, v := range sl {
		if v == s {
			return true
		}
	}
	return false
}

type Pair struct {
	a int
	b int
}
