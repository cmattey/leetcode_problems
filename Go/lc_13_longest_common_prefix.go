package Go

func longestCommonPrefix(strs []string) string {

	if len(strs) == 0 {
		return ""
	}
	pref := strs[0]

	for _, word := range strs[1:] {
		newPrefix := ""
		for i, ch := range word {
			if i < len(pref) && ch == rune(pref[i]) {
				newPrefix += string(word[i])
			} else {
				break
			}
		}
		pref = newPrefix
		if len(pref) == 0 {
			return ""
		}
	}

	return pref
}
