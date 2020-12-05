package Go

// Time: O(n)
// Space: O(n)

func lengthOfLongestSubstring(s string) int {

	maxLength := 0
	start := 0

	imap := make(map[string]int)

	for index, ch := range s {

		pos, ok := imap[string(ch)]
		if !ok {
			imap[string(ch)] = index
			maxLength = Max(maxLength, index-start+1)
		} else if ok && pos >= start {
			start = pos + 1
			imap[string(ch)] = index
		} else {
			imap[string(ch)] = index
			maxLength = Max(maxLength, index-start+1)
		}
	}

	return maxLength
}

// func Max(x, y int) int {
// 	if x > y {
// 		return x
// 	}
// 	return y
// }
